#!/usr/bin/env python3
"""Sync editorial cron jobs from context/verticals.json (config-as-data).

Run ON THE VPS:  python3 scripts/sync_crons.py

To ADD a vertical: append an entry to context/verticals.json with a "cadence"
cron expression, then re-run this script. It is idempotent — it creates any
missing "Full Pipeline: <id>" job and leaves existing ones untouched.
"""
import json
import os
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKDIR = REPO  # self-locating: /root/editorial-factory on the VPS
DELIVER = "bot-chat:editor"
PREFIX = "Full Pipeline: "


def load_verticals():
    path = os.path.join(REPO, "context", "verticals.json")
    with open(path) as f:
        data = json.load(f)
    return data.get("verticals", [])


def existing_names():
    out = subprocess.run(
        ["hermes", "cron", "list"], capture_output=True, text=True
    )
    names = set()
    for line in out.stdout.splitlines():
        if "Name:" in line:
            names.add(line.split("Name:", 1)[1].strip())
    return names


def prompt_for(v):
    vid = v["id"]
    label = v.get("label", vid)
    return (
        f"Run the full editorial pipeline for vertical '{vid}' ({label}) per the "
        f"skills in {WORKDIR}/skills/ (radar_30day -> virality_judge -> fact_check "
        f"-> story_draft -> claude_humanizer). Halt at the @Simon approve gate — do "
        f"not publish without approval. Write artifacts to context/recon_proposals/ "
        f"and context/drafts/."
    )


def main():
    verticals = load_verticals()
    existing = existing_names()
    created = skipped = failed = 0

    for v in verticals:
        vid = v["id"]
        cadence = v.get("cadence")
        if not cadence:
            print(f"SKIP {vid}: missing 'cadence'")
            continue
        name = PREFIX + vid
        if name in existing:
            skipped += 1
            continue
        r = subprocess.run(
            ["hermes", "cron", "create", cadence, prompt_for(v),
             "--name", name, "--deliver", DELIVER, "--workdir", WORKDIR],
            capture_output=True, text=True,
        )
        if r.returncode == 0:
            print(f"created: {name}  ({cadence})")
            created += 1
        else:
            print(f"FAILED: {name}  {r.stderr.strip()[:200]}")
            failed += 1

    print(f"done: {created} created, {skipped} already present, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
