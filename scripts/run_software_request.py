#!/usr/bin/env python3
"""Act on a 'run software generation now' request made in PressFlow.

PressFlow runs in a Coolify container: it can write Supabase, but it cannot touch this host's
cron store. So its button records `software_run_requested_at` in the generation_control record,
and this script — run by the zero-token `PressFlow Software Run Watcher` cron every 15 minutes —
dispatches the Weekly Market Recon (the software side's generation loop) exactly once per request
and records `software_run_handled_at`.

    python3 scripts/run_software_request.py            # dispatcher (cron)
    python3 scripts/run_software_request.py --status   # print the control record
    python3 scripts/run_software_request.py --set articles_enabled=false --by "jorge"
    python3 scripts/run_software_request.py --set software_enabled=true  --by "jorge"

Prints one line only when it acts, so the watcher stays silent on a quiet tick.
"""
import argparse
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import generation_gate as gate  # noqa: E402

# The software side's generation loop: Weekly Market Recon in /root/software-factory-core.
SOFTWARE_JOB_ID = "19c6cbf92990"
HERMES = os.environ.get("HERMES_BIN", "hermes")


def parse_stamp(value):
    """ISO-8601 text → aware datetime. Missing/garbage sorts first.

    The two writers disagree on the suffix (`toISOString()` emits `Z`, Python emits `+00:00`), and
    a plain string compare ranks 'Z' above '+' — which made a freshly handled request look older
    than the request it had just handled, i.e. an infinite re-dispatch. Parse, never compare text.
    """
    text = str(value or "").strip()
    if not text:
        return gate.datetime.min.replace(tzinfo=gate.timezone.utc)
    try:
        return gate.datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError:
        return gate.datetime.min.replace(tzinfo=gate.timezone.utc)


def maybe_dispatch(control):
    """Dispatch the recon once per unhandled request. Returns a one-line report or None."""
    if control.get("software_enabled") is False:
        return None  # paused: leave the request queued, the switch is the owner's call
    requested = parse_stamp(control.get("software_run_requested_at"))
    requested_text = str(control.get("software_run_requested_at"))
    handled = parse_stamp(control.get("software_run_handled_at"))
    if not control.get("software_run_requested_at") or requested <= handled:
        return None

    try:
        res = subprocess.run([HERMES, "cron", "run", SOFTWARE_JOB_ID],
                             capture_output=True, text=True, timeout=120)
    except (OSError, subprocess.SubprocessError) as err:
        return f"software run request {requested}: dispatch FAILED ({err})"
    if res.returncode != 0:
        detail = (res.stderr or res.stdout or "").strip().splitlines()
        return f"software run request {requested}: dispatch FAILED ({detail[-1] if detail else 'exit ' + str(res.returncode)})"

    record, storage, error = gate.write_control(
        {"software_run_handled_at": gate.datetime.now(gate.timezone.utc).isoformat(timespec="seconds"),
         "software_run_note": f"dispatched by PressFlow request at {requested_text}"},
        by="pressflow-watcher", touch=False,  # a dispatch is not a switch change — do not rewrite `updated_by`
    )
    if error:
        return f"software run request {requested}: dispatched, but recording it failed ({error})"
    return f"software run request {requested}: dispatched Weekly Market Recon (control stored in {storage})"


def main():
    parser = argparse.ArgumentParser(description="Dispatch a queued PressFlow software-generation run.")
    parser.add_argument("--status", action="store_true", help="print the control record and exit")
    parser.add_argument("--set", nargs=1, metavar="KEY=BOOL", help="write one switch (articles_enabled|software_enabled)")
    parser.add_argument("--by", default=None, help="who is flipping the switch")
    args = parser.parse_args()

    if args.status:
        control, source, warn = gate.read_control()
        print(json.dumps({"source": source, "warning": warn, "control": control}, indent=2))
        return 0

    if args.set:
        key, _, raw = args.set[0].partition("=")
        if key not in ("articles_enabled", "software_enabled"):
            print(f"refusing: '{key}' is not a switch (articles_enabled|software_enabled)", file=sys.stderr)
            return 2
        value = raw.strip().lower() not in ("false", "0", "no", "off")
        record, storage, error = gate.write_control({key: value}, by=args.by or "host-cli")
        print(f"{key} = {value} (stored in {storage})" + (f" — warning: {error}" if error else ""))
        return 0 if not error else 1

    report = maybe_dispatch(gate.read_control()[0])
    if report:
        print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
