#!/usr/bin/env python3
"""Reconcile editorial cron jobs with context/verticals.json (config-as-data).

Run ON THE VPS:  python3 scripts/sync_crons.py            # apply
                 python3 scripts/sync_crons.py --dry-run   # show the plan only
                 python3 scripts/sync_crons.py --check     # exit 1 if drifted (no writes)

Contract: exactly one `Full Pipeline: <vertical>` job per registry entry, on the
cadence the registry declares, running the pipeline sequence the registry
declares. Four ways that can fail, all of them reported:

  missing  — a registry vertical with no job            → create
  drifted  — a job whose schedule != registry cadence   → edit
  stale
  prompt   — a job whose instruction != prompt_for(v)   → edit
             (the registry owns the step sequence, so a step added to the
             template — e.g. the `synthesize_topics.py --seed` step — cannot
             silently fail to reach the live fleet)
  orphan   — a `Full Pipeline:` job for a vertical that is no longer in the
             registry (retired vertical, e.g. home_systems_reno replaced by the
             Home & Lifestyle set)                      → reported; removed only
                                                          with --retire-orphans

The create-only version of this script skipped any job whose name already
existed, so a cadence change in the registry never reached the live job —
`--check` (wired into scripts/verify.sh) is what makes that class of drift loud.

Adding a vertical: append an entry to context/verticals.json with a "cadence",
re-run this script, then `node scripts/vertical-sync.mjs --vendor` in
/root/software-factory-core so the coverage-ledger snapshot matches.

Staggering: every pipeline job fires in a 30-minute slot (10:30-13:00 UTC) and the
registry's slots are unique per weekday — concurrent full pipelines share the
frontier (kie.ai) and deepseek endpoints, and a 6-way 06:00 collision is what we
were seeing before. Keep slots unique per day when adding a vertical.

Off-peak: DeepSeek bills weekday tokens at 2x inside 01:00-04:00 and 06:00-10:00 UTC
(weekends are off-peak all day), and the scheduler reads these hours on the host clock,
which is UTC here. Every weekday cadence therefore sits at/after 10:30 UTC — the first
slot after the 06:00-10:00 window — so a slow pipeline cannot start inside the 2x band.
`plan()`-adjacent `peak_violations()` is what refuses a registry edit that lands in peak;
scripts/check_offpeak_crons.py applies the same rule to the whole live fleet (watchdogs,
one-shots, interval jobs).
"""
import json
import os
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKDIR = REPO  # self-locating: /root/editorial-factory on the VPS
PREFIX = "Full Pipeline: "

# The evergreen fleet is a second schedule, not a second step: one `Evergreen Pipeline: <vertical>`
# job per registry `evergreen_cadence`. A news run and an evergreen run for the same vertical are
# separate jobs because they are separate pipelines with separate gates — the Judge's >=8
# freshness/synthesis gate cannot score a durable topic (Novelty carries 0.40), so folding the
# evergreen pass into the news instruction would dead-end every token on the news gate first.
# The registry owns this instruction text too (see plan()'s stale-prompt class).
EVERGREEN_PREFIX = "Evergreen Pipeline: "

# Live jobs deliver to the Slack home channel (#loop-ai) — that is where the
# @Simon approve gate is read. bot-chat:editor is not wired in this workspace.
DELIVER = os.environ.get("EDITORIAL_CRON_DELIVER", "slack")
# Fleet tier (owner, 2026-10-05): the editorial pipelines are high-volume content
# generation, not the frontier decision work, so they run on the cheap tier. Only the
# frontier agents (simon, phoebe, product-director) and the two factory watchdogs
# (Build/Growth Watchdog) stay on deepseek-v4-pro. Override with EDITORIAL_CRON_MODEL.
MODEL = os.environ.get("EDITORIAL_CRON_MODEL", "deepseek-flash")
PROVIDER = os.environ.get("EDITORIAL_CRON_PROVIDER", "deepseek")
JOBS_PATH = os.environ.get(
    "EDITORIAL_CRON_JOBS", os.path.expanduser("~/.hermes/cron/jobs.json")
)

CHECK = "--check" in sys.argv
DRY_RUN = "--dry-run" in sys.argv or CHECK
RETIRE_ORPHANS = "--retire-orphans" in sys.argv

# DeepSeek peak windows, [start_hour, end_hour) Mon-Fri, in UTC (the host clock the scheduler
# reads cadences in). Peak tokens cost 2x. Mirrored by scripts/check_offpeak_crons.py, which
# audits the non-registry jobs too; this copy is what stops a registry edit from *creating*
# a peak-scheduled pipeline.
PEAK_WINDOWS_UTC = ((1, 4), (6, 10))
PEAK_DAYS = (1, 2, 3, 4, 5)


def in_peak_hour(hour):
    return any(lo <= hour < hi for lo, hi in PEAK_WINDOWS_UTC)


def cadence_verdict(cadence):
    """('ok'|'peak'|'unknown', message) for a 5-field cron cadence, weekday fires only."""
    parts = (cadence or "").strip().split()
    if len(parts) != 5:
        return "unknown", f"not a 5-field cron expression: {cadence!r}"
    minute, hour, dom, month, dow = parts
    try:
        dows = list(range(0, 7)) if dow == "*" else [int(d) % 7 for d in dow.split(",")]
    except ValueError:
        return "unknown", f"unreadable day-of-week field: {dow!r}"
    weekdays = [d for d in dows if d in PEAK_DAYS]
    if not weekdays:
        return "ok", "weekend only — weekends are off-peak all day"
    if hour == "*":
        hours = None
    elif hour.startswith("*/") or "," in hour or "-" in hour:
        hours = None
    else:
        try:
            hours = [int(hour)]
        except ValueError:
            return "unknown", f"unreadable hour field: {hour!r}"
    if hours is None or any(in_peak_hour(h) for h in hours):
        return "peak", (f"cadence '{cadence}' fires inside a DeepSeek peak window "
                        f"(Mon-Fri 01:00-04:00 / 06:00-10:00 UTC, 2x tokens)")
    return "ok", "weekday fires are outside the peak windows"


def peak_violations(verticals):
    """Every registry cadence (both fleets) that fires inside a DeepSeek peak window."""
    out, seen = [], set()
    for v in verticals:
        for key in ("cadence", "evergreen_cadence"):
            cadence = v.get(key)
            if not cadence:
                continue
            verdict, msg = cadence_verdict(cadence)
            if verdict in ("peak", "unknown") and (v["id"], cadence) not in seen:
                seen.add((v["id"], cadence))
                out.append((v, cadence, msg))
    return out


def load_verticals():
    with open(os.path.join(REPO, "context", "verticals.json")) as f:
        return json.load(f).get("verticals", [])


def read_live(prefix=PREFIX):
    """Read the scheduler's persistent store, for one fleet. Absent store = not the cron host."""
    if not os.path.exists(JOBS_PATH):
        return None
    with open(JOBS_PATH) as f:
        raw = json.load(f)
    jobs = raw["jobs"] if isinstance(raw, dict) else raw
    out = []
    for j in jobs:
        name = j.get("name") or ""
        if not name.startswith(prefix):
            continue
        sched = j.get("schedule") or {}
        out.append(
            {
                "id": j.get("id"),
                "name": name,
                "vertical": name[len(prefix):],
                "cadence": sched.get("expr") or sched.get("display") or "",
                "enabled": bool(j.get("enabled", True)),
                "prompt": j.get("prompt") or "",
            }
        )
    return out


def prompt_for(v):
    vid = v["id"]
    label = v.get("label", vid)
    return (
        f"Run the full editorial pipeline for vertical '{vid}' ({label}) per the "
        f"skills in {WORKDIR}/skills/ (radar_30day -> synthesize_topics --seed -> "
        f"virality_judge -> fact_check -> story_draft -> claude_humanizer). "
        f"After the Radar writes context/recon_proposals/YYYY-MM-DD_{vid}_signals.md, run "
        f"`python3 scripts/synthesize_topics.py --seed context/recon_proposals/YYYY-MM-DD_{vid}_signals.md` "
        f"to seed that file's Candidate Synthesis Pairs block (mechanical and advisory: it never scores "
        f"the >=8 gate, and \"no valid pair\" is a legitimate result — re-run it if you add or remove a "
        f"signal row, or scripts/verify.sh §8 will read the block as stale). Then pass the seeded file to "
        f"the Judge. When the article clears verification and the frontier rewrite, PERSIST it in the "
        f"same run — `python3 scripts/publish.py context/drafts/<slug>_final.md` writes published/, the "
        f"published log, Supabase and the sitemap, then flip the run-log row in "
        f"context/content_calendar.md. Persistence to the reader site + Supabase is NOT approval-gated. "
        f"Only outbound distribution (LinkedIn / Ghost / Reddit) waits for the @Simon approve gate — "
        f"surface the LinkedIn/Reddit copy and halt there. Write artifacts to context/recon_proposals/ "
        f"and context/drafts/."
    )


def evergreen_prompt_for(v):
    """The evergreen run's instruction. Same shape as prompt_for(), different pipeline.

    The two fleets deliberately do not share a template: the news instruction's gate is a 30-day
    freshness gate, and reusing it here would let a model 'clear' an evergreen brief by scoring it
    as news (or dead-end every durable topic on Novelty, which carries 0.40).
    """
    vid = v["id"]
    label = v.get("label", vid)
    return (
        f"Run the EVERGREEN pipeline for vertical '{vid}' ({label}) per "
        f"{WORKDIR}/skills/evergreen_topics.md (evergreen_topics -> evergreen_gate --brief -> "
        f"fact_check -> story_draft -> claude_humanizer). This is NOT a news sweep: the topic does "
        f"not have to be new, it has to be USEFUL to the persona and stay true for months — so the "
        f"30-day window and the virality Judge DO NOT run here, and a topic whose value expires "
        f"inside 90 days belongs in the news pipeline instead. Pick the topic from the evidence "
        f"sources that skill lists (the vertical's own primary_angles, the persona's wants in "
        f"context/personas.json, context/growth_os/founder-voice.md and customer-truth.md, the "
        f"intel feeds, and GSC striking-distance queries when impressions are meaningful) — never "
        f"from a topic you invented. Write the brief to "
        f"context/recon_proposals/YYYY-MM-DD_{vid}_evergreen_brief.md, then run "
        f"`python3 scripts/evergreen_gate.py --brief context/recon_proposals/"
        f"YYYY-MM-DD_{vid}_evergreen_brief.md` — the gate fetches every cited primary source and "
        f"needs >= 3 distinct https sources that actually contain the figure cited, plus a named "
        f"persona decision and a de-dup check against the last 180 days of this vertical's briefs "
        f"and published articles; it writes the `<!-- evergreen-gate: -->` marker that "
        f"scripts/verify.sh reads (re-run it if you add or remove a source row, or the marker reads "
        f"as stale). A run where no candidate clears the gate returns \"no publish\" and says why — "
        f"that is a legitimate outcome, never pad it with an unsourced or throwaway topic. Only then "
        f"does the brief go to fact_check -> story_draft -> claude_humanizer. When the article "
        f"clears verification and the frontier rewrite, PERSIST it in the same run — `python3 "
        f"scripts/publish.py context/drafts/<slug>_final.md` writes published/, the published log, "
        f"Supabase and the sitemap, then flip the run-log row in context/content_calendar.md. "
        f"Persistence to the reader site + Supabase is NOT approval-gated. Only outbound "
        f"distribution (LinkedIn / Ghost / Reddit) waits for the @Simon approve gate — surface the "
        f"LinkedIn/Reddit copy and halt there. The draft must carry `archetype: evergreen` and "
        f"`evergreen: true` in its frontmatter. Write artifacts to context/recon_proposals/ and "
        f"context/drafts/."
    )


def cadence_slots(cadence):
    """[(dow, hour, minute)] for a 5-field cron cadence. [] when it is not a fixed weekly hour
    (expressions like `*/6` or a day/month restriction), which the collision gate cannot judge."""
    parts = (cadence or "").strip().split()
    if len(parts) != 5:
        return []
    minute, hour, dom, month, dow = parts
    if not (minute.isdigit() and hour.isdigit()):
        return []
    if dom != "*" or month != "*":
        return []
    if dow == "*":
        days = list(range(7))
    else:
        try:
            days = [int(d) % 7 for d in dow.split(",")]
        except ValueError:
            return []
    return [(d, int(hour), int(minute)) for d in days]


def slot_collisions(verticals):
    """(slot, first claimant, second claimant) for every (weekday, hour, minute) two registry
    cadences share, across BOTH fleets.

    Slots are 30 minutes apart and unique per weekday because concurrent pipelines stampede the
    shared DeepSeek endpoint and the pinned frontier stylist (a 6-way 06:00 collision is what the
    staggering was introduced for). Until now that invariant was a manual discipline — the table was
    'verified from the live store, not by eye'. The evergreen fleet doubled the number of slots to
    check, so it is a gate.
    """
    seen, clashes = {}, []
    for v in verticals:
        for key in ("cadence", "evergreen_cadence"):
            cadence = v.get(key)
            for dow, hour, minute in cadence_slots(cadence or ""):
                slot = (dow, hour, minute)
                who = f"{PREFIX}{v['id']}" if key == "cadence" else f"{EVERGREEN_PREFIX}{v['id']}"
                if slot in seen:
                    clashes.append((slot, seen[slot], who))
                else:
                    seen[slot] = who
    return clashes


def plan(verticals, live, prefix=PREFIX, cadence_key="cadence", enabled_key="news_enabled",
         prompt_fn=None):
    """Drift classes for ONE fleet (the news fleet unless told otherwise).

    Returns (missing, drifted, orphans, paused, stale_prompt, disabled):
      disabled — the registry says this mode is OFF for the vertical but a live job still exists.
                 The registry owns the job's *existence*, so `news_enabled: false` /
                 `evergreen_enabled: false` is a real setting: apply removes the job (and
                 `--check` fails until it is removed). Re-enabling recreates it — one sync run.
                 Reusing pause() here would be ambiguous with an operator's deliberate pause,
                 which this tool must leave alone (`paused`).
    """
    prompt_fn = prompt_fn or prompt_for
    by_vertical = {j["vertical"]: j for j in live}
    registry_ids = {v["id"] for v in verticals}
    missing, drifted, orphans, paused, stale_prompt, disabled = [], [], [], [], [], []
    # An absent `evergreen_cadence` means "this vertical has no evergreen run", not "the fleet is
    # missing a job" — only the news cadence is mandatory per registry entry.
    cadence_optional = prefix != PREFIX
    for v in verticals:
        cadence = v.get(cadence_key)
        j = by_vertical.get(v["id"])
        if not v.get(enabled_key, True):
            if j is not None:
                disabled.append((v, j))
            continue
        if not cadence:
            if cadence_optional:
                continue
            missing.append((v, None, f"missing '{cadence_key}' in registry"))
            continue
        if j is None:
            missing.append((v, cadence, None))
            continue
        if j["cadence"] != cadence:
            drifted.append((v, cadence, j))
        # Prompt drift: the registry owns the instruction text too. Without this class the
        # pipeline sequence a job actually runs can silently diverge from the SOPs (a step
        # added to the registry template never reaches the live fleet — the same failure the
        # create-only sync had with cadences).
        if j.get("prompt") != prompt_fn(v):
            stale_prompt.append((v, j))
        if not j["enabled"]:
            paused.append((v, j))
    orphans = [j for j in live if j["vertical"] not in registry_ids]
    return missing, drifted, orphans, paused, stale_prompt, disabled


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


# (prefix, cadence_key, enabled_key, prompt_fn, label) — the registry carries BOTH fleets, so both
# are reconciled from it. A hand-made evergreen job is invisible to `--check` in exactly the way a
# hand-made pipeline job was, so the same rule applies: never hand-create one.
FLEETS = (
    (PREFIX, "cadence", "news_enabled", prompt_for, "news"),
    (EVERGREEN_PREFIX, "evergreen_cadence", "evergreen_enabled", evergreen_prompt_for, "evergreen"),
)


def fleet_states(verticals):
    """[(prefix, cadence_key, enabled_key, prompt_fn, label, live, classes)] for every fleet."""
    out = []
    for prefix, cadence_key, enabled_key, prompt_fn, label in FLEETS:
        live = read_live(prefix)
        classes = plan(verticals, live, prefix=prefix, cadence_key=cadence_key,
                       enabled_key=enabled_key, prompt_fn=prompt_fn)
        out.append((prefix, cadence_key, enabled_key, prompt_fn, label, live, classes))
    return out


def report_states(states):
    for prefix, _ck, _ek, _pf, label, live, classes in states:
        missing, drifted, orphans, paused, stale_prompt, disabled = classes
        print(f"  [{label} fleet] {len(live)} live job(s)")
        for v, cadence, err in missing:
            print(f"    MISSING       {prefix}{v['id']}  ({err or cadence})")
        for v, cadence, j in drifted:
            print(f"    DRIFTED       {prefix}{v['id']}  live='{j['cadence']}' registry='{cadence}'")
        for v, j in stale_prompt:
            print(f"    STALE PROMPT  {prefix}{v['id']}  (live instruction != registry instruction)")
        for v, j in disabled:
            print(f"    DISABLED      {prefix}{v['id']}  ({label}_enabled is false in the registry; "
                  f"job still live — apply removes it)")
        for j in orphans:
            print(f"    ORPHAN        {j['name']}  ({j['cadence']}, not in registry)")
        for v, j in paused:
            print(f"    PAUSED        {j['name']}  (paused by operator; left alone)")


def main():
    verticals = load_verticals()
    if read_live() is None:
        print(f"SKIP: no cron store at {JOBS_PATH} — not the scheduler host.")
        return 0

    states = fleet_states(verticals)
    peaks = peak_violations(verticals)
    clashes = slot_collisions(verticals)
    total_live = sum(len(s[5]) for s in states)
    print(f"registry: {len(verticals)} verticals | live pipeline jobs: {total_live}")
    report_states(states)
    for v, cadence, _msg in peaks:
        print(f"    PEAK          {v['id']}  {cadence} — DeepSeek 2x window "
              f"(Mon-Fri 01:00-04:00 / 06:00-10:00 UTC); move it to at/after 10:30 UTC")
    for slot, first, second in clashes:
        dow, hour, minute = slot
        print(f"    COLLISION     {first} and {second} both fire {hour:02d}:{minute:02d} "
              f"on weekday {dow} — concurrent pipelines stampede the shared endpoints")

    drifted_classes = [c for s in states for c in s[6] if c]
    drift = bool(drifted_classes or peaks or clashes)
    if CHECK:
        print("check: " + ("DRIFT" if drift else
                           f"ok — {len(verticals)} verticals in sync across both fleets "
                           f"(cadence + prompt + enabled + off-peak + slots)"))
        return 1 if drift else 0
    if peaks or clashes:
        # Fail closed: never reconcile the fleet ONTO a 2x-token schedule or a shared slot.
        print(f"refusing to apply: {len(peaks)} peak cadence(s), {len(clashes)} slot collision(s)")
        return 1
    if DRY_RUN:
        print("dry-run: no changes written" if drift else "dry-run: nothing to do")
        return 0

    created = updated = removed = failed = 0
    for prefix, _ck, _ek, prompt_fn, label, _live, classes in states:
        missing, drifted, orphans, paused, stale_prompt, disabled = classes
        for v, cadence, _err in missing:
            if not cadence:
                continue
            r = run(
                ["hermes", "cron", "create", cadence, prompt_fn(v),
                 "--name", prefix + v["id"], "--deliver", DELIVER,
                 "--workdir", WORKDIR, "--model", MODEL, "--provider", PROVIDER]
            )
            if r.returncode == 0:
                print(f"created: {prefix}{v['id']}  ({cadence})")
                created += 1
            else:
                print(f"FAILED: {prefix}{v['id']}  {r.stderr.strip()[:200]}")
                failed += 1
        for v, cadence, j in drifted:
            r = run(["hermes", "cron", "edit", j["id"], "--schedule", cadence])
            if r.returncode == 0:
                print(f"updated: {prefix}{v['id']}  {j['cadence']} -> {cadence}")
                updated += 1
            else:
                print(f"FAILED: edit {prefix}{v['id']}  {r.stderr.strip()[:200]}")
                failed += 1
        for v, j in stale_prompt:
            r = run(["hermes", "cron", "edit", j["id"], "--prompt", prompt_fn(v)])
            if r.returncode == 0:
                print(f"updated prompt: {prefix}{v['id']}")
                updated += 1
            else:
                print(f"FAILED: prompt {prefix}{v['id']}  {r.stderr.strip()[:200]}")
                failed += 1
        for v, j in disabled:
            r = run(["hermes", "cron", "remove", j["id"]])
            if r.returncode == 0:
                print(f"removed ({label}_enabled false): {prefix}{v['id']}")
                removed += 1
            else:
                print(f"FAILED: remove {prefix}{v['id']}  {r.stderr.strip()[:200]}")
                failed += 1
        for j in orphans:
            if not RETIRE_ORPHANS:
                print(f"orphan left in place: {j['name']} (re-run with --retire-orphans)")
                continue
            r = run(["hermes", "cron", "remove", j["id"]])
            if r.returncode == 0:
                print(f"retired orphan: {j['name']}")
                removed += 1
            else:
                print(f"FAILED: remove {j['name']}  {r.stderr.strip()[:200]}")
                failed += 1

    # Verify by re-reading the store — never claim a state we did not observe.
    after = fleet_states(verticals)
    residual = [c for s in after for c in s[6] if c]
    per_fleet = ", ".join(f"{s[4]} {len(s[5])}/{sum(1 for v in verticals if v.get(s[1]) and v.get(s[2], True))}"
                          for s in after)
    print(
        f"done: {created} created, {updated} updated, {removed} removed, {failed} failed | "
        f"verify: {per_fleet} jobs | "
        f"{len(residual)} residual drift, {len(peak_violations(verticals))} peak, "
        f"{len(slot_collisions(verticals))} collision"
    )
    return 1 if (failed or residual or peak_violations(verticals) or slot_collisions(verticals)) else 0


if __name__ == "__main__":
    sys.exit(main())
