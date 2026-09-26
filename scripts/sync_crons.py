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

Staggering: every pipeline job fires in a 30-minute slot (06:00-08:30 UTC) and the
registry's slots are unique per weekday — concurrent full pipelines share the
frontier (kie.ai) and deepseek endpoints, and a 6-way 06:00 collision is what we
were seeing before. Keep slots unique per day when adding a vertical.
"""
import json
import os
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKDIR = REPO  # self-locating: /root/editorial-factory on the VPS
PREFIX = "Full Pipeline: "

# Live jobs deliver to the Slack home channel (#loop-ai) — that is where the
# @Simon approve gate is read. bot-chat:editor is not wired in this workspace.
DELIVER = os.environ.get("EDITORIAL_CRON_DELIVER", "slack")
MODEL = os.environ.get("EDITORIAL_CRON_MODEL", "deepseek-v4-pro")
PROVIDER = os.environ.get("EDITORIAL_CRON_PROVIDER", "deepseek")
JOBS_PATH = os.environ.get(
    "EDITORIAL_CRON_JOBS", os.path.expanduser("~/.hermes/cron/jobs.json")
)

CHECK = "--check" in sys.argv
DRY_RUN = "--dry-run" in sys.argv or CHECK
RETIRE_ORPHANS = "--retire-orphans" in sys.argv


def load_verticals():
    with open(os.path.join(REPO, "context", "verticals.json")) as f:
        return json.load(f).get("verticals", [])


def read_live():
    """Read the scheduler's persistent store. Absent store = not the cron host."""
    if not os.path.exists(JOBS_PATH):
        return None
    with open(JOBS_PATH) as f:
        raw = json.load(f)
    jobs = raw["jobs"] if isinstance(raw, dict) else raw
    out = []
    for j in jobs:
        name = j.get("name") or ""
        if not name.startswith(PREFIX):
            continue
        sched = j.get("schedule") or {}
        out.append(
            {
                "id": j.get("id"),
                "name": name,
                "vertical": name[len(PREFIX):],
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


def plan(verticals, live):
    by_vertical = {j["vertical"]: j for j in live}
    registry_ids = {v["id"] for v in verticals}
    missing, drifted, orphans, paused, stale_prompt = [], [], [], [], []
    for v in verticals:
        cadence = v.get("cadence")
        if not cadence:
            missing.append((v, None, "missing 'cadence' in registry"))
            continue
        j = by_vertical.get(v["id"])
        if j is None:
            missing.append((v, cadence, None))
            continue
        if j["cadence"] != cadence:
            drifted.append((v, cadence, j))
        # Prompt drift: the registry owns the instruction text too. Without this class the
        # pipeline sequence a job actually runs can silently diverge from the SOPs (a step
        # added to the registry template never reaches the live fleet — the same failure the
        # create-only sync had with cadences).
        if j.get("prompt") != prompt_for(v):
            stale_prompt.append((v, j))
        if not j["enabled"]:
            paused.append((v, j))
    orphans = [j for j in live if j["vertical"] not in registry_ids]
    return missing, drifted, orphans, paused, stale_prompt


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def main():
    verticals = load_verticals()
    live = read_live()
    if live is None:
        print(f"SKIP: no cron store at {JOBS_PATH} — not the scheduler host.")
        return 0

    missing, drifted, orphans, paused, stale_prompt = plan(verticals, live)
    print(f"registry: {len(verticals)} verticals | live pipeline jobs: {len(live)}")

    for v, cadence, err in missing:
        print(f"  MISSING  {PREFIX}{v['id']}  ({err or cadence})")
    for v, cadence, j in drifted:
        print(f"  DRIFTED  {PREFIX}{v['id']}  live='{j['cadence']}' registry='{cadence}'")
    for v, j in stale_prompt:
        print(f"  STALE PROMPT  {PREFIX}{v['id']}  (live instruction != registry instruction)")
    for j in orphans:
        print(f"  ORPHAN   {j['name']}  ({j['cadence']}, not in registry)")
    for v, j in paused:
        print(f"  PAUSED   {j['name']}  (paused by operator; left alone)")

    drift = bool(missing or drifted or orphans or stale_prompt)
    if CHECK:
        print("check: " + ("DRIFT" if drift else
                           f"ok — {len(verticals)} verticals in sync (cadence + prompt)"))
        return 1 if drift else 0
    if DRY_RUN and not drift:
        print("dry-run: nothing to do")
        return 0
    if DRY_RUN:
        print("dry-run: no changes written")
        return 0

    created = updated = failed = 0
    for v, cadence, _err in missing:
        if not cadence:
            continue
        r = run(
            ["hermes", "cron", "create", cadence, prompt_for(v),
             "--name", PREFIX + v["id"], "--deliver", DELIVER,
             "--workdir", WORKDIR, "--model", MODEL, "--provider", PROVIDER]
        )
        if r.returncode == 0:
            print(f"created: {PREFIX}{v['id']}  ({cadence})")
            created += 1
        else:
            print(f"FAILED: {PREFIX}{v['id']}  {r.stderr.strip()[:200]}")
            failed += 1
    for v, cadence, j in drifted:
        r = run(["hermes", "cron", "edit", j["id"], "--schedule", cadence])
        if r.returncode == 0:
            print(f"updated: {PREFIX}{v['id']}  {j['cadence']} -> {cadence}")
            updated += 1
        else:
            print(f"FAILED: edit {PREFIX}{v['id']}  {r.stderr.strip()[:200]}")
            failed += 1
    for v, j in stale_prompt:
        r = run(["hermes", "cron", "edit", j["id"], "--prompt", prompt_for(v)])
        if r.returncode == 0:
            print(f"updated prompt: {PREFIX}{v['id']}")
            updated += 1
        else:
            print(f"FAILED: prompt {PREFIX}{v['id']}  {r.stderr.strip()[:200]}")
            failed += 1
    for j in orphans:
        if not RETIRE_ORPHANS:
            print(f"orphan left in place: {j['name']} (re-run with --retire-orphans)")
            continue
        r = run(["hermes", "cron", "remove", j["id"]])
        if r.returncode == 0:
            print(f"retired orphan: {j['name']}")
        else:
            print(f"FAILED: remove {j['name']}  {r.stderr.strip()[:200]}")
            failed += 1

    # Verify by re-reading the store — never claim a state we did not observe.
    after = read_live()
    m2, d2, o2, _p2, s2 = plan(verticals, after)
    print(
        f"done: {created} created, {updated} updated, {failed} failed | "
        f"verify: {len(verticals) - len(m2)}/{len(verticals)} verticals scheduled, "
        f"{len(d2)} drifted, {len(s2)} stale prompt, {len(o2)} orphan"
    )
    return 1 if (failed or m2 or d2 or s2) else 0


if __name__ == "__main__":
    sys.exit(main())
