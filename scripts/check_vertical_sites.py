#!/usr/bin/env python3
"""Guard: every editorial vertical must have exactly one WordPress destination row.

Compares context/verticals.json (the pipeline's source of truth for which verticals exist)
against public.vertical_sites in Supabase (the source of truth for where each one publishes).

Fails (exit 1) on:
  - a vertical in verticals.json with no row in vertical_sites   (article would have no home)
  - a row in vertical_sites for a vertical that no longer exists (stale routing)
  - a URL that violates the cms.<domain> rule, or a trailing slash
  - a row marked active = false for a live vertical

Usage:
  python3 scripts/check_vertical_sites.py            # read the live table
  python3 scripts/check_vertical_sites.py --json     # machine-readable result

Credentials: SUPABASE_URL + SUPABASE_SERVICE_ROLE_KEY from the environment or ./.env
(the same keys scripts/sync_all_to_supabase.mjs and publish.py already use).
"""

from __future__ import annotations

import json
import os
import pathlib
import sys
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
VERTICALS = ROOT / "context" / "verticals.json"
TABLE = "vertical_sites"


def load_env() -> None:
    """Read ./.env without overriding anything already exported."""
    env_file = ROOT / ".env"
    if not env_file.exists():
        return
    for raw in env_file.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def supabase_config() -> tuple[str, str]:
    load_env()
    url = os.environ.get("SUPABASE_URL", "").rstrip("/")
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")
    if not url or not key:
        sys.exit("FAIL: SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY must be set (env or ./.env)")
    return url, key


def fetch_rows(url: str, key: str) -> list[dict]:
    endpoint = f"{url}/rest/v1/{TABLE}?select=vertical_id,cms_base_url,site_domain,frontend_url,active"
    req = urllib.request.Request(endpoint, headers={
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Accept": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")[:300]
        if exc.code == 404 or "PGRST205" in body or "does not exist" in body:
            sys.exit(
                f"FAIL: public.{TABLE} is not in the schema cache — the migration has not been\n"
                f"      applied yet. Run supabase/migrations/0003_vertical_sites.sql in the\n"
                f"      Supabase SQL editor, then re-run this check.\n      ({body})"
            )
        sys.exit(f"FAIL: Supabase returned HTTP {exc.code}: {body}")
    except urllib.error.URLError as exc:
        sys.exit(f"FAIL: could not reach Supabase: {exc}")


def check() -> dict:
    url, key = supabase_config()
    rows = fetch_rows(url, key)
    declared = {v["id"] for v in json.loads(VERTICALS.read_text())["verticals"]}
    routed = {r["vertical_id"]: r for r in rows}

    problems: list[str] = []
    for vertical_id in sorted(declared - set(routed)):
        problems.append(f"vertical '{vertical_id}' has no destination row in {TABLE}")
    for vertical_id in sorted(set(routed) - declared):
        problems.append(f"{TABLE} routes unknown vertical '{vertical_id}' (not in verticals.json)")

    for vertical_id, row in sorted(routed.items()):
        cms, domain, frontend = row["cms_base_url"], row["site_domain"], row["frontend_url"]
        if cms != f"https://cms.{domain}":
            problems.append(f"'{vertical_id}': cms_base_url '{cms}' is not https://cms.{domain}")
        if frontend != f"https://{domain}":
            problems.append(f"'{vertical_id}': frontend_url '{frontend}' is not https://{domain}")
        if cms.endswith("/") or frontend.endswith("/"):
            problems.append(f"'{vertical_id}': trailing slash in a URL ('{cms}' / '{frontend}')")
        if row.get("active") is False and vertical_id in declared:
            problems.append(f"'{vertical_id}': routed to {domain} but marked active=false")

    by_domain: dict[str, int] = {}
    for row in routed.values():
        by_domain[row["site_domain"]] = by_domain.get(row["site_domain"], 0) + 1

    return {
        "ok": not problems,
        "declared_verticals": len(declared),
        "routed_verticals": len(routed),
        "by_domain": dict(sorted(by_domain.items())),
        "problems": problems,
    }


def main() -> int:
    result = check()
    if "--json" in sys.argv:
        print(json.dumps(result, indent=2))
    else:
        print(f"vertical_sites: {result['routed_verticals']}/{result['declared_verticals']} verticals routed")
        for domain, count in result["by_domain"].items():
            print(f"  {domain:18s} {count:2d} vertical(s)")
        for problem in result["problems"]:
            print(f"  FAIL: {problem}")
        print("check: " + ("ok — every vertical has exactly one cms.<domain> destination"
                           if result["ok"] else f"{len(result['problems'])} problem(s)"))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
