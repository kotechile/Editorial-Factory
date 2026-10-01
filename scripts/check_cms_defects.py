#!/usr/bin/env python3
"""Standing defect check for the two WordPress CMSes.

Catches, on every run, the two defects that were previously only found by hand:

  1. a raw vertical id in a live title or slug  — e.g. the published giniloh post titled
     "enterprise_build_vs_buy: The $250k AI Upkeep Tax", which put the vertical id into the H1,
     <title>, og:title and the Article schema headline at once.
  2. the same article on BOTH sites — the routing table sends each vertical to exactly one CMS,
     so a slug present on both is either a stale manual push or a misroute. It is also the shape
     of a cross-site duplicate-content problem if both are published.

Contract (watchdog): print NOTHING and exit 0 when clean; print the findings and exit 1 when a
defect is found, so the job that runs it reports to Slack instead of staying silent.

Usage:
  python3 scripts/check_cms_defects.py            # human-readable, exit 1 on defects
  python3 scripts/check_cms_defects.py --json     # machine-readable

Credentials: WP_<SITE>_USER / WP_<SITE>_APP_PASSWORD from the environment or ./.env (the same
pair scripts/wp_draft.py uses). Read-only: it never writes to either CMS.
"""

from __future__ import annotations

import base64
import html
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request
from difflib import SequenceMatcher

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITES = {"giniloh.com": "https://cms.giniloh.com", "wellroost.com": "https://cms.wellroost.com"}
VERTICAL_ID = re.compile(r"^[a-z][a-z0-9]*(_[a-z0-9]+){1,}\s*:")
BODY_SIMILARITY = 0.60      # identical copies sit at ~1.00; different articles at <0.10


def load_env() -> None:
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


def plain(markup: str) -> str:
    text = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", markup or "")
    text = re.sub(r"(?s)<[^>]+>", " ", text)
    text = html.unescape(text).replace("\u2019", "'")
    text = re.sub(r"[^a-zA-Z0-9' ]+", " ", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def auth_for(site_domain: str) -> str:
    label = site_domain.split(".")[0].upper()
    user = os.environ.get(f"WP_{label}_USER") or os.environ.get("WP_USER", "")
    password = os.environ.get(f"WP_{label}_APP_PASSWORD") or os.environ.get("WP_APP_PASSWORD", "")
    if not user or not password:
        sys.exit(f"FAIL: no WordPress credentials for {site_domain} (set WP_{label}_USER / WP_{label}_APP_PASSWORD)")
    return "Basic " + base64.b64encode(f"{user}:{password}".encode()).decode()


def fetch_posts(site_domain: str, base: str) -> list[dict]:
    request = urllib.request.Request(
        f"{base}/wp-json/wp/v2/posts?status=any&per_page=100&context=edit"
        f"&_fields=id,slug,status,title,content,link,categories,featured_media",
        headers={"Authorization": auth_for(site_domain), "Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8", "replace") or "[]")
    except urllib.error.HTTPError as exc:
        sys.exit(f"FAIL: {base} returned HTTP {exc.code} for the post list")
    except urllib.error.URLError as exc:
        sys.exit(f"FAIL: could not reach {base}: {exc}")


def uncategorized_id(site_domain: str, base: str) -> int | None:
    """WordPress's default category id, so a post filed there can be called out."""
    request = urllib.request.Request(
        f"{base}/wp-json/wp/v2/categories?per_page=100&_fields=id,slug",
        headers={"Authorization": auth_for(site_domain), "Accept": "application/json"})
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            for category in json.loads(response.read().decode("utf-8", "replace") or "[]"):
                if category.get("slug") == "uncategorized":
                    return int(category["id"])
    except Exception:                                          # noqa: BLE001 - best effort
        pass
    return None


def check() -> dict:
    posts: dict[str, list[dict]] = {}
    defects: list[str] = []

    for site_domain, base in SITES.items():
        rows = fetch_posts(site_domain, base)
        posts[site_domain] = rows
        default_category = uncategorized_id(site_domain, base)
        for post in rows:
            title = html.unescape(re.sub(r"<[^>]+>", "", post["title"]["rendered"])).strip()
            if VERTICAL_ID.match(title):
                defects.append(f"vertical id in a {post['status']} title — {site_domain} #{post['id']} "
                               f"'{title[:64]}' ({post['link']})")
            if VERTICAL_ID.match(post["slug"]):
                defects.append(f"vertical id in a slug — {site_domain} #{post['id']} "
                               f"'{post['slug']}' ({post['link']})")
            # Published only: a live post filed under the default category never appears on a
            # category page, and every published post on both sites otherwise carries one.
            if post["status"] == "publish":
                categories = post.get("categories") or []
                if not categories:
                    defects.append(f"published post with NO category — {site_domain} #{post['id']} "
                                   f"'{post['slug']}' ({post['link']})")
                elif default_category and categories == [default_category]:
                    defects.append(f"published post left in Uncategorized — {site_domain} #{post['id']} "
                                   f"'{post['slug']}' ({post['link']})")

    # Same slug on one site twice (WP allows a draft and a published post to share a slug).
    for site_domain, rows in posts.items():
        seen: dict[str, list[dict]] = {}
        for post in rows:
            seen.setdefault(post["slug"], []).append(post)
        for slug, group in seen.items():
            if len(group) > 1:
                ids = ", ".join(f"#{p['id']}/{p['status']}" for p in group)
                defects.append(f"same slug twice on {site_domain} — '{slug}' ({ids})")

    # Same slug on both sites, and identical bodies across sites.
    for slug in {p["slug"] for p in posts["giniloh.com"]} & {p["slug"] for p in posts["wellroost.com"]}:
        pair = [(s, p) for s, rows in posts.items() for p in rows if p["slug"] == slug]
        states = ", ".join(f"{s}#{p['id']}/{p['status']}" for s, p in pair)
        defects.append(f"same slug on BOTH sites — '{slug}' ({states})")

    giniloh = [(p, plain(p["content"]["rendered"])) for p in posts["giniloh.com"]]
    wellroost = [(p, plain(p["content"]["rendered"])) for p in posts["wellroost.com"]]
    for a, a_text in giniloh:
        for b, b_text in wellroost:
            if a["slug"] == b["slug"] or len(a_text) < 400 or len(b_text) < 400:
                continue
            ratio = SequenceMatcher(None, a_text, b_text).ratio()
            if ratio >= BODY_SIMILARITY:
                defects.append(f"identical articles on both sites ({ratio:.2f}) — "
                               f"giniloh #{a['id']} '{a['slug']}' vs wellroost #{b['id']} '{b['slug']}'")

    return {
        "ok": not defects,
        "scanned": {site: len(rows) for site, rows in posts.items()},
        "defects": defects,
    }


def main() -> int:
    load_env()
    result = check()
    if "--json" in sys.argv:
        print(json.dumps(result, indent=2))
    elif result["defects"]:
        scanned = ", ".join(f"{site} {count}" for site, count in result["scanned"].items())
        print(f"CMS defect check: {len(result['defects'])} problem(s) — scanned {scanned}")
        for defect in result["defects"]:
            print(f"  - {defect}")
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
