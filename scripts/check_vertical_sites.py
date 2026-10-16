#!/usr/bin/env python3
"""Guard: every editorial vertical must have exactly one WordPress destination row.

Compares context/verticals.json (the pipeline's source of truth for which verticals exist)
against public.vertical_sites in Supabase (the source of truth for where each one publishes),
then against each destination CMS's own `vertical` taxonomy (the source of truth for what a
front can route on).

Fails (exit 1) on:
  - a vertical in verticals.json with no row in vertical_sites   (article would have no home)
  - a site_domain that is not a reader front registered in context/frontends.json
  - a cms_base_url that is not one of the fronts' own cms.<domain> hosts, or a trailing slash
  - a row marked active = false for a live vertical
  - a routed vertical whose destination CMS registers the `vertical` taxonomy but holds no term
    for it (the push fails closed — see scripts/wp_draft.py resolve_vertical_term)

Reported, not failed (statements about the estate, not defects):
  - a destination CMS that registers no `vertical` taxonomy at all (cms.wellroost.com today:
    one front serves that CMS, so a post needs no routing key),
  - a CMS that could not be read (its pushes fail loudly on their own), and
  - a routing row for a vertical this registry does not declare — the table is shared by every
    producer publishing through these CMSes, so it is named rather than failed, which is how a
    stale row of ours is still visible.

Usage:
  python3 scripts/check_vertical_sites.py            # read the live table and both CMSes
  python3 scripts/check_vertical_sites.py --json     # machine-readable result
  python3 scripts/check_vertical_sites.py --no-cms   # routing rows only, no CMS request

Credentials: SUPABASE_URL + SUPABASE_SERVICE_ROLE_KEY from the environment or ./.env
(the same keys scripts/sync_all_to_supabase.mjs and publish.py already use). The CMS reads are
public REST calls and need no credentials.
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
FRONTS = ROOT / "context" / "frontends.json"
TABLE = "vertical_sites"
VERTICAL_TAXONOMY = "vertical"     # the CMS taxonomy whose term slug IS the editorial vertical id


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


def _get_json(url: str, missing_ok: bool = False):
    """A public REST read. `missing_ok` turns a 404 into None (an endpoint that is not there),
    anything else into an explicit error rather than an empty result."""
    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            raw = response.read().decode("utf-8", "replace")
        return json.loads(raw) if raw.strip() else None
    except urllib.error.HTTPError as exc:
        if missing_ok and exc.code == 404:
            return None
        body = exc.read().decode("utf-8", "replace")[:200]
        raise RuntimeError(f"{url} -> HTTP {exc.code}: {body}") from None
    except urllib.error.URLError as exc:
        raise RuntimeError(f"could not reach {url}: {exc}") from None


def declared_fronts() -> set[str]:
    """The reader fronts the estate publishes to — context/frontends.json, the same registry
    scripts/frontends.py and the internal-link corpus read. A routing row's `site_domain` names one
    of these (the front the article is published for), and its CMS is one of their `cms.<domain>`
    hosts: several fronts can read the same CMS, so the CMS is not necessarily the row's own front.
    """
    try:
        rows = json.loads(FRONTS.read_text())
    except (OSError, json.JSONDecodeError) as exc:
        sys.exit(f"FAIL: could not read {FRONTS}: {exc}")
    return {str(r.get("domain")) for r in rows if r.get("domain")}


def cms_vertical_terms(cms_base_url: str) -> set[str] | None:
    """The verticals a destination CMS can name on a post — or None when it registers no such
    taxonomy.

    This is the check that turns "the push will fail closed" into something the operator learns
    BEFORE a run: scripts/wp_draft.py resolves the term by slug on the destination and refuses to
    publish a vertical whose term is missing (`resolve_vertical_term`). Term slugs are the
    editorial vertical ids, so the two sets are directly comparable.

    Public reads: the taxonomy list, then that taxonomy's terms. A 404 on the taxonomy list is read
    as "not registered" (it is how a site without the taxonomy answers); a 404 on the TERMS route is
    an empty set, so a routed vertical there is reported rather than silently passed.
    """
    taxonomies = _get_json(f"{cms_base_url}/wp-json/wp/v2/taxonomies", missing_ok=True) or {}
    definition = (taxonomies or {}).get(VERTICAL_TAXONOMY) if isinstance(taxonomies, dict) else None
    if not definition:
        return None
    rest_base = definition.get("rest_base") or VERTICAL_TAXONOMY
    terms = _get_json(f"{cms_base_url}/wp-json/wp/v2/{rest_base}"
                      f"?per_page=100&_fields=slug", missing_ok=True) or []
    return {str(t.get("slug")) for t in terms if isinstance(t, dict) and t.get("slug")}


def probe_cms(rows: list[dict]) -> tuple[dict, dict]:
    """({domain: terms | None}, {domain: why it could not be read}) for the destinations in use."""
    terms: dict[str, set[str] | None] = {}
    errors: dict[str, str] = {}
    for domain, base in sorted({(r["site_domain"], r["cms_base_url"]) for r in rows}):
        try:
            terms[domain] = cms_vertical_terms(base)
        except RuntimeError as exc:
            errors[domain] = str(exc)
    return terms, errors


def audit(declared: set[str], rows: list[dict],
          cms_terms: dict[str, set[str] | None] | None = None,
          cms_errors: dict[str, str] | None = None,
          fronts: set[str] | None = None) -> dict:
    """The routing audit as a pure function of the registry and the live rows (testable offline).

    Beyond the destination rules, this covers the WordPress *category*: a vertical with no
    `wp_category_id` produces a draft in the CMS's default category (Uncategorized), which is a step
    the operator used to do by hand on every post and, if missed, a published post that appears on no
    category page and in no listing. A missing column means the migration was never applied — named
    here rather than left as a raw 42703.

    `cms_terms` / `cms_errors` (optional) add the destination-CMS half: the terms of its `vertical`
    taxonomy, and the destinations whose CMS could not be read. Passing neither keeps this function
    a pure routing check of the registry against the table, which is how the offline suite uses it.
    """
    routed = {r["vertical_id"]: r for r in rows}
    problems: list[str] = []
    notices: list[str] = []

    for vertical_id in sorted(declared - set(routed)):
        problems.append(f"vertical '{vertical_id}' has no destination row in {TABLE}")
    # A row for a vertical this registry does not declare is expected now that the table is shared
    # by every producer publishing through these CMSes, so it is reported rather than failed —
    # but it IS reported, so a stale row of ours cannot hide among the other producer's.
    for vertical_id in sorted(set(routed) - declared):
        notices.append(
            f"{TABLE} routes '{vertical_id}', which context/verticals.json does not declare "
            f"(another producer's vertical, or a row retired here but not deleted)")

    has_category_column = any("wp_category_id" in row for row in rows)
    if not has_category_column and rows:
        problems.append(
            f"{TABLE}.wp_category_id does not exist — {CATEGORY_MIGRATION} has not been applied, so "
            f"every CMS draft is filed under WordPress's default category (Uncategorized) and the "
            f"operator has to re-file each post by hand. Apply it in the Supabase SQL editor.")

    for vertical_id, row in sorted(routed.items()):
        cms, domain, frontend = row["cms_base_url"], row["site_domain"], row["frontend_url"]
        if frontend != f"https://{domain}":
            problems.append(f"'{vertical_id}': frontend_url '{frontend}' is not https://{domain}")
        if cms.endswith("/") or frontend.endswith("/"):
            problems.append(f"'{vertical_id}': trailing slash in a URL ('{cms}' / '{frontend}')")
        # One CMS serves several fronts (cms.giniloh.com feeds giniloh.com AND aichieve.net), so the
        # rule is not "the CMS sits on the front's own domain" — site_domain names the FRONT the
        # article is published for, and the CMS is that front's own `cms.<domain>` host or another
        # front's (both fronts read the same library). A row naming some other host publishes off the
        # estate, which is what this catches.
        host = cms.removeprefix("https://").split("/")[0]
        if not host.startswith("cms.") or (fronts and host[4:] not in fronts):
            problems.append(
                f"'{vertical_id}': cms_base_url '{cms}' is not one of the fronts' own https://cms."
                f"<domain> hosts" + (f" ({', '.join(sorted(fronts))})" if fronts else ""))
        if fronts and domain not in fronts:
            problems.append(
                f"'{vertical_id}': site_domain '{domain}' is not a reader front in "
                f"context/frontends.json — a routing row names the front it publishes for")
        if row.get("active") is False and vertical_id in declared:
            problems.append(f"'{vertical_id}': routed to {domain} but marked active=false")
        if has_category_column and row.get("wp_category_id") is None and vertical_id in declared:
            problems.append(
                f"'{vertical_id}' ({domain}): no wp_category_id — its drafts land in Uncategorized; "
                f"set one in {CATEGORY_MIGRATION} (the id is per-site, and scripts/wp_draft.py "
                f"validates it against the destination before pushing)")

    # The destination CMS half: the term a front routes on. A vertical routed to a CMS that
    # registers the taxonomy but holds no term for it is a push that will fail closed — better
    # named here, where the fix is one term, than at 17:30 inside a publish run.
    cms_report: dict[str, object] = {}
    for domain in sorted(cms_terms or {}):
        slugs = (cms_terms or {})[domain]
        cms_report[domain] = None if slugs is None else sorted(slugs)
        if slugs is None:
            notices.append(
                f"{domain} registers no '{VERTICAL_TAXONOMY}' taxonomy — articles published there "
                f"carry no vertical, which is correct only while one front serves that CMS (the term "
                f"is what routes a post when one CMS feeds several fronts)")
            continue
        for vertical_id in sorted(v for v, r in routed.items()
                                  if r["site_domain"] == domain and v in declared and v not in slugs):
            problems.append(
                f"'{vertical_id}' ({domain}): the CMS registers the '{VERTICAL_TAXONOMY}' taxonomy "
                f"but has no '{vertical_id}' term — the push fails closed rather than publishing an "
                f"article no front can route; create the term (POST /wp-json/wp/v2/{VERTICAL_TAXONOMY} "
                f"with slug+name, or in wp-admin)")
    for domain in sorted(cms_errors or {}):
        notices.append(f"{domain}: could not read the CMS's taxonomies "
                       f"({(cms_errors or {})[domain]}) — its vertical coverage is unverified here, "
                       f"and its pushes fail loudly on their own")
        cms_report.setdefault(domain, "unreadable")

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
        "cms_vertical_terms": cms_report,
        "notices": notices,
        "problems": problems,
    }


def check(with_cms: bool = True) -> dict:
    url, key = supabase_config()
    rows = fetch_rows(url, key)
    declared = {v["id"] for v in json.loads(VERTICALS.read_text())["verticals"]}
    fronts = declared_fronts()
    if not with_cms:
        return audit(declared, rows, fronts=fronts)
    terms, errors = probe_cms(rows)
    return audit(declared, rows, terms, errors, fronts)


def main() -> int:
    result = check(with_cms="--no-cms" not in sys.argv)
    if "--json" in sys.argv:
        print(json.dumps(result, indent=2))
    else:
        print(f"vertical_sites: {result['routed_verticals']}/{result['declared_verticals']} verticals routed")
        for domain, count in result["by_domain"].items():
            categories = result["routed_by_category"].get(domain) or {}
            detail = (", ".join(f"#{cid}×{n}" for cid, n in categories.items())
                      if categories else "no category routing")
            print(f"  {domain:18s} {count:2d} vertical(s)   {detail}")
        for domain, terms in (result.get("cms_vertical_terms") or {}).items():
            if terms is None:
                print(f"  {domain:18s} no '{VERTICAL_TAXONOMY}' taxonomy (nothing to specify per post)")
            elif terms == "unreadable":
                print(f"  {domain:18s} not read")
            else:
                print(f"  {domain:18s} {len(terms):2d} '{VERTICAL_TAXONOMY}' term(s)")
        for notice in result.get("notices") or []:
            print(f"  note: {notice}")
        for problem in result["problems"]:
            print(f"  FAIL: {problem}")
        print("check: " + ("ok — every vertical has exactly one cms.<domain> destination"
                           if result["ok"] else f"{len(result['problems'])} problem(s)"))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
