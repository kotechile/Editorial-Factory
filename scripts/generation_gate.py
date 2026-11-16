#!/usr/bin/env python3
"""Is this generation loop allowed to run right now?

Every pipeline run (news / evergreen / review, and the software-side recon) starts with this
check so an owner switch in PressFlow takes effect on the NEXT tick — without waiting for a
registry pull, a cron sync or a redeploy.

    python3 scripts/generation_gate.py --mode news --vertical agentic_ai
    python3 scripts/generation_gate.py --mode software
    python3 scripts/generation_gate.py --mode articles --json

Exit codes:
    0  generation allowed (prints one OK line)
    3  generation paused (prints one PAUSED line — the run must stop before spending a token)
    2  bad usage

Sources, most authoritative first:
    1. Supabase `factory_config` key `generation_control`  (PressFlow writes this)
    2. context/generation_control.json                     (repo fallback / cold start)
    3. vertical mode flags: context/verticals.json, then the control record's `disabled_verticals`

Why the vertical list lives in the control record and not `editorial_verticals`: that mirror table
is empty in this project and its fleet columns (`news_enabled` / `evergreen_enabled` /
`review_enabled`) were never added, so a gate that read it would either 400 or see nothing. One
record that PressFlow writes and every run reads is the only version that cannot disagree with
itself.

Failure policy: an infrastructure error (Supabase down, table missing, network timeout) never
blocks a run — the gate falls back to the file copy and says so on the printed line. Only an
explicit disabled flag stops a run. A gate that fails closed on a network blip would silently
stop the whole fleet, which is the failure this repo has been bitten by before.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTROL_PATH = os.path.join(REPO, "context", "generation_control.json")
VERTICALS_PATH = os.path.join(REPO, "context", "verticals.json")
ENV_PATH = os.path.join(REPO, ".env")

CONTROL_KEY = "generation_control"
MODE_TO_FLAG = {"news": "news_enabled", "evergreen": "evergreen_enabled", "review": "review_enabled"}

DEFAULT_CONTROL = {
    "articles_enabled": True,
    "software_enabled": True,
    "disabled_verticals": {},
    "updated_at": None,
    "updated_by": "default",
}


def load_env():
    if not os.path.exists(ENV_PATH):
        return
    with open(ENV_PATH) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                k, v = k.strip(), v.strip().strip("'\"")
                if k not in os.environ or not os.environ[k]:
                    os.environ[k] = v


def supabase_creds():
    load_env()
    url = os.environ.get("SUPABASE_URL", "").rstrip("/")
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "") or os.environ.get("SUPABASE_KEY", "")
    return url, key


def supabase_get(path, timeout=4.0):
    """GET a PostgREST path. Returns (rows, error). Never raises."""
    url, key = supabase_creds()
    if not url or not key:
        return None, "supabase not configured"
    req = urllib.request.Request(
        f"{url}/rest/v1/{path}",
        headers={"apikey": key, "Authorization": f"Bearer {key}", "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as res:
            body = res.read().decode("utf-8")
            return (json.loads(body) if body else []), None
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError, ValueError) as err:
        return None, f"{type(err).__name__}: {err}"


def read_control():
    """(control_dict, source, warning) — Supabase first, file second, defaults last."""
    rows, err = supabase_get(f"factory_config?key=eq.{CONTROL_KEY}&select=value")
    if isinstance(rows, list) and rows:
        raw = rows[0].get("value")
        try:
            parsed = json.loads(raw) if isinstance(raw, str) else raw
            if isinstance(parsed, dict):
                return {**DEFAULT_CONTROL, **parsed}, "supabase", None
        except (ValueError, TypeError):
            pass
    warning = f"supabase control unreadable ({err})" if err else None
    if os.path.exists(CONTROL_PATH):
        try:
            with open(CONTROL_PATH) as f:
                parsed = json.load(f)
            if isinstance(parsed, dict):
                return {**DEFAULT_CONTROL, **parsed}, "file", warning
        except (ValueError, OSError):
            pass
    return dict(DEFAULT_CONTROL), "default", warning


def supabase_write(path, method, payload, timeout=6.0):
    """POST/PATCH a PostgREST path. Returns (data, error); never raises."""
    url, key = supabase_creds()
    if not url or not key:
        return None, "supabase not configured"
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(f"{url}/rest/v1/{path}", data=body, method=method, headers={
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "Prefer": "return=representation,resolution=merge-duplicates",
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as res:
            text = res.read().decode("utf-8")
            return (json.loads(text) if text else None), None
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError, ValueError) as err:
        return None, f"{type(err).__name__}: {err}"


def write_control(patch, by=None, stamp=None, timeout=6.0, touch=True):
    """Merge `patch` into the control record. Writes Supabase, then mirrors the file.

    Returns (record, storage, error). The file write is not optional even when Supabase answers:
    a run that cannot reach Supabase still has to see the switch, and PressFlow renders the file
    copy when its own Supabase read fails.
    """
    current, _source, _warn = read_control()
    now = stamp or datetime.now(timezone.utc).isoformat(timespec="seconds")
    record = ({**current, **patch, "updated_at": now,
               "updated_by": by or current.get("updated_by") or "pressflow"}
              if touch else {**current, **patch})
    # `_`-prefixed keys are documentation for the committed file, not state: keep them out of the
    # row PressFlow renders, and keep the note in the file when it is rewritten below.
    note = current.get("_note")
    stored = {k: v for k, v in record.items() if not k.startswith("_")}
    storage = "file"
    error = None
    rows, _err = supabase_get(f"factory_config?key=eq.{CONTROL_KEY}&select=id")
    if isinstance(rows, list):
        if rows:
            _data, error = supabase_write(
                f"factory_config?id=eq.{rows[0].get('id')}", "PATCH",
                {"value": json.dumps(stored), "updated_at": now}, timeout=timeout)
        else:
            _data, error = supabase_write(
                "factory_config", "POST",
                {"key": CONTROL_KEY, "value": json.dumps(stored)}, timeout=timeout)
        if error is None:
            storage = "supabase"
    else:
        error = _err
    try:
        out = {"_note": note, **stored} if note else dict(stored)
        with open(CONTROL_PATH, "w") as f:
            json.dump(out, f, indent=2)
            f.write("\n")
    except OSError as err:
        error = error or f"file write failed ({err})"
    return record, storage, error


def read_vertical_row(vertical_id):
    """(vertical_row_or_None, source, warning) — the local registry, read directly.

    Deliberately no Supabase call: this runs at the top of every pipeline, and the registry file
    ships with the repo, so it is always present and always the same shape.
    """
    if os.path.exists(VERTICALS_PATH):
        try:
            with open(VERTICALS_PATH) as f:
                registry = json.load(f)
            for v in registry.get("verticals", []):
                if v.get("id") == vertical_id:
                    return v, "file", None
        except (ValueError, OSError) as err:
            return None, "unreadable", f"registry unreadable ({err})"
    return None, "missing", None


def describe_stamp(who, when):
    who = (who or "an operator").strip()
    when = (when or "").strip()
    return f"switched off by {who}" + (f" at {when}" if when else "")


def decide(control, mode, vertical_id=None, vertical_row=None):
    """Pure decision. Returns (allowed, code_word, reason)."""
    if mode == "software":
        if control.get("software_enabled") is False:
            return False, "software", (
                "software generation is switched OFF ("
                + describe_stamp(control.get("updated_by"), control.get("updated_at"))
                + ")"
            )
        return True, "software", "software generation is ON"

    if control.get("articles_enabled") is False:
        return False, "articles", (
            "article generation is switched OFF ("
            + describe_stamp(control.get("updated_by"), control.get("updated_at"))
            + ")"
        )

    flag = MODE_TO_FLAG.get(mode)
    if not flag:
        return False, "usage", f"unknown mode '{mode}'"

    disabled = control.get("disabled_verticals") or {}
    if isinstance(disabled, dict) and vertical_id in disabled:
        entry = disabled.get(vertical_id) or {}
        return False, "vertical", (
            f"vertical '{vertical_id}' is switched OFF in PressFlow ("
            + describe_stamp(entry.get("by"), entry.get("at"))
            + ")"
        )

    if vertical_row is None:
        # Never block a run because the registry row could not be read: the vertical mode flags are
        # an extra switch, not the security boundary. The master switch above still applies.
        return True, "vertical-missing", (
            f"vertical '{vertical_id}' not found in the registry — mode '{mode}' treated as ON"
        )

    if vertical_row.get(flag) is False:
        return False, "vertical", (
            f"vertical '{vertical_id}' has '{flag}' switched OFF — no '{mode}' run is allowed"
        )
    return True, "ok", f"vertical '{vertical_id}' {mode} mode is ON"


def main():
    parser = argparse.ArgumentParser(description="Gate a generation loop on the owner switches.")
    parser.add_argument("--mode", required=True, choices=["news", "evergreen", "review", "articles", "software"])
    parser.add_argument("--vertical", default=None, help="vertical id (required for articles modes)")
    parser.add_argument("--json", action="store_true", help="machine-readable verdict")
    args = parser.parse_args()

    mode = args.mode
    articles_mode = mode in ("articles",) or mode in MODE_TO_FLAG
    if articles_mode and not args.vertical:
        print("GENERATION GATE ERROR: --vertical is required for an article mode", flush=True)
        return 2

    control, control_source, control_warn = read_control()

    vertical_row = None
    vertical_source = None
    vertical_warn = None
    if articles_mode:
        vertical_row, vertical_source, vertical_warn = read_vertical_row(args.vertical)

    if mode == "articles":
        allowed = control.get("articles_enabled") is not False
        reason = (
            "article generation is ON"
            if allowed
            else "article generation is switched OFF ("
            + describe_stamp(control.get("updated_by"), control.get("updated_at"))
            + ")"
        )
        word = "articles"
    else:
        allowed, word, reason = decide(control, mode, args.vertical, vertical_row)

    warnings = [w for w in (control_warn, vertical_warn) if w]
    if args.json:
        print(json.dumps({
            "allowed": allowed,
            "mode": mode,
            "vertical": args.vertical,
            "reason": reason,
            "control_source": control_source,
            "vertical_source": vertical_source,
            "warnings": warnings,
        }))
        return 0 if allowed else 3

    suffix = f" [control={control_source}" + (f", vertical={vertical_source}" if vertical_source else "") + "]"
    if warnings:
        suffix += f" (warning: {'; '.join(warnings)})"
    verdict = "GENERATION OK" if allowed else "GENERATION PAUSED"
    print(f"{verdict} ({word}): {reason}.{suffix}", flush=True)
    return 0 if allowed else 3


if __name__ == "__main__":
    sys.exit(main())
