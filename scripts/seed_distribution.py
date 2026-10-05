#!/usr/bin/env python3
"""
scripts/seed_distribution.py — prepare the app-promotion to-do queue.

**Preparation, not distribution.** It asks the deployed PressFlow dashboard to build the to-do
cards for every app in `context/promoted_apps.json` (the dashboard's own
`POST /api/distribution/seed`). It never posts anything, never flips a card's status, never
rewrites text an operator edited, and never creates a second card for an app that already has one —
that is the seed endpoint's documented behaviour and this script only calls it.

The queue used to be built from `published/*.md` articles; it now promotes the software factory's
live apps, which is why the coverage check counts apps rather than articles.

Automatic in the publish pass (`scripts/publish.py` calls it after refreshing the sitemap), and
runnable by hand:

    python3 scripts/seed_distribution.py              # seed now
    python3 scripts/seed_distribution.py --refresh    # regenerate the text of `ready` cards only
    python3 scripts/seed_distribution.py --check      # exit 1 if a promoted app has no card
    python3 scripts/seed_distribution.py --dry-run    # print the request without sending it

Auth: `PRESSFLOW_AUTH_SECRET` (repo .env, or the deploy environment) is sent as `x-editorial-key`.
Override the target with `PRESSFLOW_BASE_URL` or `--url`.
"""

import argparse
import json
import os
import pathlib
import sys
import urllib.error
import urllib.request

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_BASE_URL = "https://pressflow.aichieve.net"
SEED_PATH = "/api/distribution/seed"
QUEUE_PATH = "/api/distribution/tasks"
APPS_FILE = REPO_ROOT / "context" / "promoted_apps.json"


def load_env():
    """Load repo .env into os.environ without clobbering real environment values."""
    env_file = REPO_ROOT / ".env"
    if not env_file.exists():
        return
    for line in env_file.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def base_url(explicit=None):
    return (explicit or os.environ.get("PRESSFLOW_BASE_URL") or DEFAULT_BASE_URL).rstrip("/")


def _request(path, method="GET", payload=None, timeout=30, url=None):
    secret = os.environ.get("PRESSFLOW_AUTH_SECRET", "").strip()
    req = urllib.request.Request(
        f"{base_url(url)}{path}",
        data=json.dumps(payload).encode("utf-8") if payload is not None else None,
        method=method,
        headers={"Content-Type": "application/json", "x-editorial-key": secret},
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def seed(refresh=False, timeout=30, url=None):
    """Ask the dashboard to build to-do cards for every promoted app. Idempotent."""
    return _request(SEED_PATH, "POST", {"refresh": bool(refresh)}, timeout=timeout, url=url)


def queue_state(timeout=30, url=None):
    return _request(QUEUE_PATH, "GET", None, timeout=timeout, url=url)


def promoted_apps():
    """{app slug: app name} for every app the to-do list promotes.

    The catalog is the same file the dashboard seeds from, so coverage is measured against the
    thing that actually produces the cards rather than a second list that can drift.
    """
    try:
        data = json.loads(APPS_FILE.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}
    out = {}
    for app in data.get("apps", []):
        slug = str(app.get("slug", "")).strip()
        if slug:
            out[slug] = str(app.get("name", slug))
    return out


def uncovered(apps, tasks):
    """Promoted apps with no card in the queue. Cards are matched on source_id."""
    have = {str(t.get("source_id", "")).strip() for t in tasks}
    return [name for slug, name in sorted(apps.items()) if slug not in have]


def coverage_report(timeout=30, url=None):
    state = queue_state(timeout=timeout, url=url)
    missing = uncovered(promoted_apps(), state.get("tasks", []))
    return state, missing


def main(argv=None):
    parser = argparse.ArgumentParser(description="Prepare the app-promotion to-do queue (no posting)")
    parser.add_argument("--refresh", action="store_true",
                        help="Also regenerate the text of existing `ready` cards")
    parser.add_argument("--check", action="store_true",
                        help="Exit 1 if any promoted app has no to-do card (no writes)")
    parser.add_argument("--dry-run", action="store_true", help="Print the request without sending it")
    parser.add_argument("--url", help=f"Dashboard base URL (default {DEFAULT_BASE_URL})")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args(argv)

    load_env()
    if args.dry_run:
        print(f"POST {base_url(args.url)}{SEED_PATH} {{'refresh': {bool(args.refresh)}}} "
              f"with x-editorial-key from PRESSFLOW_AUTH_SECRET "
              f"({'set' if os.environ.get('PRESSFLOW_AUTH_SECRET') else 'MISSING'})")
        print(f"promoted apps: {len(promoted_apps())}")
        return 0

    if not os.environ.get("PRESSFLOW_AUTH_SECRET", "").strip():
        print("Error: PRESSFLOW_AUTH_SECRET is not set (repo .env or environment) — the dashboard "
              "rejects the request without it", file=sys.stderr)
        return 2

    try:
        if args.check:
            state, missing = coverage_report(url=args.url)
            counts = state.get("counts", {})
            print(f"queue: {state.get('total', 0)} cards ({counts.get('ready', 0)} ready, "
                  f"{counts.get('published', 0)} published, {counts.get('deleted', 0)} deleted) "
                  f"| storage: {state.get('storage')}")
            if missing:
                for name in missing:
                    print(f"FAIL: no promotion card for app '{name}' — run "
                          f"`python3 scripts/seed_distribution.py`")
                return 1
            print("coverage: OK — every promoted app has a to-do card")
            return 0

        result = seed(refresh=args.refresh, url=args.url)
        state, missing = coverage_report(url=args.url)
        if not args.quiet:
            print(f"✓ promotion prep: {result.get('created', result.get('added', '?'))} card(s) added, "
                  f"{result.get('pruned', 0)} pruned "
                  f"| queue now {state.get('total', 0)} cards "
                  f"({state.get('counts', {}).get('ready', 0)} ready)")
            if missing:
                print(f"! {len(missing)} promoted app(s) still have no card: {', '.join(missing[:4])}")
        return 0
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")[:200]
        print(f"Error: dashboard returned HTTP {exc.code}: {body}", file=sys.stderr)
        return 2
    except Exception as exc:  # network, DNS, timeout, malformed JSON
        print(f"Error: could not reach {base_url(args.url)}: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
