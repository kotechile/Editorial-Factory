#!/usr/bin/env python3
"""Off-peak guard: no scheduled LLM run may spend weekday tokens at DeepSeek's 2x rate.

DeepSeek's peak windows (2026-09 pricing) are **Mon-Fri 01:00-04:00 and 06:00-10:00 UTC**;
weekends are entirely off-peak, and a token served inside a window costs 2x an off-peak token.
Everything Hermes schedules fires on the *host clock*, which is UTC on this VPS, so a cadence's
hour field is read as UTC — the guard fails loudly if the host timezone ever stops being UTC,
because that silently re-labels every cadence in this fleet.

What it checks (the whole live fleet, not just the editorial pipelines):

  * every **enabled** job whose schedule is a 5-field cron expression and that is not a
    ``no_agent`` script job (those make no model call, so their hour is free);
  * jobs on a recurring interval (``every 2h``) — these cannot be proven off-peak at all, since a
    sub-daily repeat necessarily crosses a window, so they are reported instead of waved through;
  * one-shot ISO timestamps, judged against the same windows.

The rule itself lives in ``sync_crons.cadence_verdict`` so the reconciler cannot create a
peak-scheduled pipeline while this audit calls the same code.

Print nothing when everything is off-peak — it is wired into scripts/verify.sh, which the
`Editorial Verify Gate` cron job runs, and that contract is "empty stdout = silent, no Slack noise".

  python3 scripts/check_offpeak_crons.py            # audit the live fleet (host clock)
  python3 scripts/check_offpeak_crons.py --list     # also list off-peak jobs and skips
"""
import json
import os
import sys
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sync_crons as sc  # noqa: E402  (store path + the peak rule, one definition)

LIST = "--list" in sys.argv


def host_offset_minutes():
    """Offset of the clock the scheduler reads cadences in (local time)."""
    offset = datetime.now().astimezone().utcoffset()
    return int((offset or timedelta()).total_seconds() // 60)


def verdict_for_stamp(stamp):
    """One-shot jobs: check the timestamp itself."""
    if not stamp:
        return "unknown", "one-shot without a readable timestamp"
    try:
        when = datetime.fromisoformat(str(stamp).replace("Z", "+00:00"))
    except ValueError:
        return "unknown", f"unreadable one-shot timestamp {stamp!r}"
    if when.weekday() >= 5 or not sc.in_peak_hour(when.hour):
        return "ok", f"one-shot at {stamp} is off-peak"
    return "peak", f"one-shot at {stamp} lands inside a 2x-token peak window"


def check_jobs(jobs):
    """[(name, job_id, verdict, message)] for every job that can spend money in a window."""
    findings = []
    for j in jobs:
        name = j.get("name") or j.get("id") or "?"
        job_id = j.get("id") or "?"
        if not j.get("enabled", True):
            findings.append((name, job_id, "skip", "paused — never fires"))
            continue
        if j.get("no_agent"):
            findings.append((name, job_id, "skip", "no_agent script job — makes no model call"))
            continue
        sched = j.get("schedule") or {}
        kind = sched.get("kind")
        expr = sched.get("expr") or sched.get("display") or ""
        if kind in (None, "cron") and expr:
            verdict, message = sc.cadence_verdict(expr)
            findings.append((name, job_id, verdict, message))
            continue
        if kind == "interval" or expr.lower().startswith("every") or expr.endswith(("m", "h", "d")):
            findings.append(
                (name, job_id, "recurring",
                 f"recurring interval '{expr}' cannot stay out of the peak windows — pin a "
                 f"weekday cron time at/after 10:30 UTC")
            )
            continue
        stamp = sched.get("at") or sched.get("run_at") or sched.get("timestamp")
        if kind in ("once", "one_shot", "absolute") or stamp:
            findings.append((name, job_id, *verdict_for_stamp(stamp)))
            continue
        findings.append((name, job_id, "unknown", f"unrecognized schedule {sched!r}"))
    return findings


def main():
    if not os.path.exists(sc.JOBS_PATH):
        print(f"check_offpeak_crons: skip — no scheduler store at {sc.JOBS_PATH}")
        return 0

    offset = host_offset_minutes()
    with open(sc.JOBS_PATH) as f:
        raw = json.load(f)
    jobs = raw["jobs"] if isinstance(raw, dict) else raw

    findings = check_jobs(jobs)
    problems = []

    if offset != 0:
        problems.append(
            f"host clock is UTC{offset // 60:+03d}:{abs(offset) % 60:02d} — cadence hours are read "
            f"in local time while the DeepSeek peak windows are UTC, so this audit is not valid"
        )
    for name, job_id, verdict, message in findings:
        if verdict in ("peak", "recurring", "unknown"):
            problems.append(f"{verdict}: {name} ({job_id}) — {message}")

    if LIST:
        print(f"off-peak audit: {len(jobs)} jobs, host offset {offset} min, "
              f"peak = Mon-Fri 01:00-04:00 + 06:00-10:00 UTC")
        for name, job_id, verdict, message in findings:
            print(f"  [{verdict:9s}] {name} ({job_id}) — {message}")

    if not problems:
        return 0

    print(f"OFF-PEAK GATE FAILED — {len(problems)} problem(s); DeepSeek peak = Mon-Fri "
          f"01:00-04:00 + 06:00-10:00 UTC (2x token price):")
    for p in problems:
        print(f"  {p}")
    print("  fix: move the job to a weekday slot at/after 10:30 UTC (or into 04:00-06:00 UTC). "
          "Editorial pipelines: edit context/verticals.json, then run scripts/sync_crons.py. "
          "Other jobs: `hermes cron edit <job_id> --schedule '<expr>'`.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
