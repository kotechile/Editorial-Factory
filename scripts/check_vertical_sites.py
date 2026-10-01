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
    """Every column: `select=*` so a routing column added by a later migration (wp_category_id,
    migrations/0004) is picked up the moment it is applied — and so this guard can say which
    migration is missing instead of failing with a raw 42703."""
    endpoint = f"{url}/rest/v1/{TABLE}?select=*"
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


CATEGORY_MIGRATION = "supabase/migrations/0004_vertical_sites_category.sql"


def audit(declared: set[str], rows: list[dict]) -> dict:
    """The routing audit as a pure function of the registry and the live rows (testable offline).

    Beyond the destination rules, this covers the WordPress *category*: a vertical with no
    `wp_category_id` produces a draft in the CMS's default category (Uncategorized), which is a step
    the operator used to do by hand on every post and, if missed, a published post that appears on no
    category page and in no listing. A missing column means the migration was never applied — named
    here rather than left as a raw 42703.
    """
    routed = {r["vertical_id"]: r for r in rows}
    problems: list[str] = []

    for vertical_id in sorted(declared - set(routed)):
        problems.append(f"vertical '{vertical_id}' has no destination row in {TABLE}")
    for vertical_id in sorted(set(routed) - declared):
        problems.append(f"{TABLE} routes unknown vertical '{vertical_id}' (not in verticals.json)")

    has_category_column = any("wp_category_id" in row for row in rows)
    if not has_category_column and rows:
        problems.append(
            f"{TABLE}.wp_category_id does not exist — {CATEGORY_MIGRATION} has not been applied, so "
            f"every CMS draft is filed under WordPress's default category (Uncategorized) and the "
            f"operator has to re-file each post by hand. Apply it in the Supabase SQL editor.")

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
        if has_category_column and row.get("wp_category_id") is None and vertical_id in declared:
            problems.append(
                f"'{vertical_id}' ({domain}): no wp_category_id — its drafts land in Uncategorized; "
                f"set one in {CATEGORY_MIGRATION} (the id is per-site, and scripts/wp_draft.py "
                f"validates it against the destination before pushing)")

    by_domain: dict[str, int] = {}
    by_category: dict[str, dict[str, int]] = {}
    for vertical_id, row in routed.items():
        domain = row["site_domain"]
        by_domain[domain] = by_domain.get(domain, 0) + 1
        category = row.get("wp_category_id")
        if has_category_column and vertical_id in declared and category is not None:
            by_category.setdefault(domain, {})
            by_category[domain][str(category)] = by_category[domain].get(str(category), 0) + 1

    return {
        "ok": not problems,
        "declared_verticals": len(declared),
        "routed_verticals": len(routed),
        "category_column": has_category_column,
        "routed_by_category": {d: dict(sorted(c.items())) for d, c in sorted(by_category.items())},
        "by_domain": dict(sorted(by_domain.items())),
        "problems": problems,
    }


def check() -> dict:
    url, key = supabase_config()
    rows = fetch_rows(url, key)
    declared = {v["id"] for v in json.loads(VERTICALS.read_text())["verticals"]}
    return audit(declared, rows)


def main() -> int:
    result = check()
    if "--json" in sys.argv:
        print(json.dumps(result, indent=2))
    else:
        print(f"vertical_sites: {result['routed_verticals']}/{result['declared_verticals']} verticals routed")
        for domain, count in result["by_domain"].items():
            categories = result["routed_by_category"].get(domain) or {}
            detail = (", ".join(f"#{cid}×{n}" for cid, n in categories.items())
                      if categories else "no category routing")
            print(f"  {domain:18s} {count:2d} vertical(s)   {detail}")
        for problem in result["problems"]:
            print(f"  FAIL: {problem}")
        print("check: " + ("ok — every vertical has exactly one cms.<domain> destination"
                           if result["ok"] else f"{len(result['problems'])} problem(s)"))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
