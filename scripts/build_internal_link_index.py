#!/usr/bin/env python3
"""Build the internal-link candidate index for the two live sites.

    python3 scripts/build_internal_link_index.py           # rebuild context/internal_links.json + .md
    python3 scripts/build_internal_link_index.py --check    # CI/staleness guard, writes nothing

Why it exists
-------------
Internal links were sourced from context/sitemap.json, which only knows the articles this pipeline
published. The 28 articles already live on giniloh.com and wellroost.com — written by hand, and the
strongest link targets on either site — were invisible to the generator, so drafts shipped with an
empty `<!-- internal-links -->` block and readers got no internal links at all.

Two sources, deliberately
-------------------------
  * The CMS says what EXISTS: published posts, their real titles, their categories.
  * The FRONTEND SITEMAP says what RESOLVES. Both Astro fronts answer 200 with the homepage for an
    unknown URL, so "it returned HTTP 200" proves nothing here; a sitemap entry does. A post that is
    published in the CMS but missing from the sitemap (the frontend has not been rebuilt since) is
    recorded under not_live and never offered as a link target — pointing a reader at it would send
    them, and any crawler, to the homepage.

Both sites' frontends also expose non-article targets (calculators, category hubs). Those are
indexed too, as kind="calculator"/"category", because for a decision-engine site a calculator is
often the most useful thing to link out to. Articles rank higher when scores tie.
"""

from __future__ import annotations

import argparse
import html
import json
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import wp_draft as wd  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX_JSON = ROOT / "context" / "internal_links.json"
INDEX_MD = ROOT / "context" / "internal_links.md"
STALE_AFTER_DAYS = 30

# Used when Supabase is unreachable, so the index still builds from the two known sites.
FALLBACK_SITES = [
    ("giniloh.com", "https://cms.giniloh.com", "https://giniloh.com"),
    ("wellroost.com", "https://cms.wellroost.com", "https://wellroost.com"),
]

# Path segments that are site furniture, not link targets worth suggesting.
SKIP_SEGMENTS = {"/", "/about", "/contact", "/privacy", "/terms", "/author", "/categories",
                 "/calculators"}


def is_section_page(path: str, section: str) -> bool:
    """`/calculators/<slug>/` — the section page itself, not a nested permutation of it.

    Both frontends publish a page per ROLE for every calculator (`/calculators/career-ai-resilience/`
    → `/chief-executives/`, `/chief-sustainability-officers/`, …), which is 1,029 URLs on giniloh.com
    alone (measured). Those are live pages, but a per-role variant is not a "go deeper" target for an
    article — indexing them turned a 55-candidate corpus into 1,073 and would have let a nested page
    win a link on two incidental shared words.
    """
    parts = [p for p in (path or "").split("/") if p]
    return len(parts) == 2 and parts[0] == section


def site_list() -> tuple[list[tuple[str, str, str]], str]:
    """The sites to index, from public.vertical_sites when available (one row per vertical)."""
    row = wd.supabase_get("vertical_sites?select=site_domain,cms_base_url,frontend_url")
    if row is None:
        return FALLBACK_SITES, "fallback (Supabase unreachable)"
    seen: dict[str, tuple[str, str, str]] = {}
    for entry in row:
        domain = (entry.get("site_domain") or "").strip()
        if domain and domain not in seen:
            seen[domain] = (domain, entry.get("cms_base_url", ""), entry.get("frontend_url", ""))
    sites = [s for s in seen.values() if s[1] and s[2]]
    return (sites, "public.vertical_sites") if sites else (FALLBACK_SITES, "fallback (no rows)")


def fetch(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (editorial-factory index)"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read().decode("utf-8", "replace")


def fetch_sitemap(frontend: str) -> list[str]:
    """Live URLs on the frontend. This is the only trustworthy liveness signal we have."""
    xml = fetch(f"{frontend.rstrip('/')}/sitemap.xml")
    urls = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml)
    if not urls:
        raise RuntimeError(f"{frontend}/sitemap.xml listed no URLs — refusing to build an empty index")
    return [urllib.parse.urldefrag(u.strip())[0] for u in urls]


def fetch_categories(wp: "wd.WordPress") -> dict[int, str]:
    _, rows = wp._call("GET", "categories?per_page=100&_fields=id,name")
    return {int(c["id"]): html.unescape(c["name"]) for c in rows or []}


def fetch_published(wp: "wd.WordPress") -> list[dict]:
    _, rows = wp._call("GET", "posts?status=publish&per_page=100&_fields=id,slug,title,categories,excerpt,modified")
    return rows or []


def path_segment(url: str) -> str:
    parts = [p for p in urllib.parse.urlparse(url).path.split("/") if p]
    return parts[-1] if parts else ""


def title_from_slug(slug: str) -> str:
    return " ".join(w.capitalize() if w.islower() else w for w in re.split(r"[-_]+", slug) if w)


def strip_html(text: str) -> str:
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", text or "")).split())


def build() -> dict:
    wd.load_env()
    sites, site_source = site_list()
    candidates: list[dict] = []
    not_live: list[dict] = []
    categories_by_site: dict[str, dict[int, str]] = {}

    for domain, cms, frontend in sites:
        user, password = wd.credentials_for(domain)
        wp = wd.WordPress(cms, user, password)
        categories = fetch_categories(wp)
        categories_by_site[domain] = categories
        posts = fetch_published(wp)
        live_urls = fetch_sitemap(frontend)
        by_segment = {path_segment(u): u for u in live_urls}

        for post in posts:
            slug = (post.get("slug") or "").strip()
            url = by_segment.get(slug, "")
            entry = {
                "site": domain,
                "kind": "article",
                "id": post.get("id"),
                "slug": slug,
                "title": strip_html((post.get("title") or {}).get("rendered", "")),
                "url": url or f"{frontend.rstrip('/')}/{slug}/",
                "categories": [categories.get(int(c), str(c)) for c in (post.get("categories") or [])],
                "category_ids": [int(c) for c in (post.get("categories") or [])],
                "excerpt": strip_html((post.get("excerpt") or {}).get("rendered", ""))[:280],
                "modified": post.get("modified", ""),
                "live": bool(url),
            }
            if url:
                candidates.append(entry)
            else:
                not_live.append({**entry, "reason": "published in the CMS but absent from the frontend sitemap"})

        # Non-article targets the frontend actually publishes.
        for url in live_urls:
            path = urllib.parse.urlparse(url).path
            segment = path_segment(url)
            if not segment or path.rstrip("/") in SKIP_SEGMENTS:
                continue
            if segment in by_segment and any(c["url"] == url for c in candidates):
                continue
            if path.startswith("/calculators/") and is_section_page(path, "calculators"):
                kind = "calculator"
            elif path.startswith("/categories/") and is_section_page(path, "categories"):
                kind = "category"
            else:
                continue
            candidates.append({
                "site": domain, "kind": kind, "id": None, "slug": segment,
                "title": title_from_slug(segment) + (" calculator" if kind == "calculator" else ""),
                "url": url, "categories": [], "category_ids": [], "excerpt": "",
                "modified": "", "live": True,
            })

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "site_source": site_source,
        "sites": {d: {"cms": c, "frontend": f} for d, c, f in sites},
        "categories": {d: {str(k): v for k, v in cats.items()} for d, cats in categories_by_site.items()},
        "candidates": candidates,
        "not_live": not_live,
    }


def write_report(index: dict) -> None:
    lines = [f"# Internal-link candidates — {index['generated_at']}", "",
             f"Source of sites: {index['site_source']}. Liveness is decided by each frontend's "
             "sitemap.xml, not by an HTTP status.", ""]
    for domain in index["sites"]:
        rows = [c for c in index["candidates"] if c["site"] == domain]
        articles = [c for c in rows if c["kind"] == "article"]
        lines += [f"## {domain} — {len(articles)} live article(s), "
                  f"{len(rows) - len(articles)} other target(s)", ""]
        for c in sorted(rows, key=lambda r: (r["kind"] != "article", r["title"])):
            cats = ", ".join(c["categories"]) or "—"
            label = f"{c['title']}" if c["kind"] == "article" else f"{c['title']} ({c['kind']})"
            lines.append(f"- [{label}]({c['url']}) — {cats}")
        lines.append("")
    if index["not_live"]:
        lines += ["## Published in a CMS but NOT live on its site (never suggested as a link target)", ""]
        for c in index["not_live"]:
            lines.append(f"- {c['site']} #{c['id']} `{c['slug']}` — {c['reason']}")
        lines.append("")
    INDEX_MD.write_text("\n".join(lines), encoding="utf-8")


def check() -> int:
    if not INDEX_JSON.exists():
        print("FAIL: context/internal_links.json is missing — run build_internal_link_index.py")
        return 1
    index = json.loads(INDEX_JSON.read_text(encoding="utf-8"))
    if not index.get("candidates"):
        print("FAIL: the index holds no candidates")
        return 1
    built = datetime.fromisoformat(index["generated_at"])
    age = (datetime.now(timezone.utc) - built).days
    problems = []
    if age > STALE_AFTER_DAYS:
        problems.append(f"index is {age} days old (limit {STALE_AFTER_DAYS})")
    # A candidate whose URL has dropped out of the sitemap would link readers to a soft-404.
    for domain, meta in index["sites"].items():
        try:
            live = set(fetch_sitemap(meta["frontend"]))
        except Exception as exc:                      # noqa: BLE001 - report, do not crash the gate
            problems.append(f"{domain}: could not re-read the sitemap ({exc})")
            continue
        gone = [c["url"] for c in index["candidates"] if c["site"] == domain and c["url"] not in live]
        if gone:
            problems.append(f"{domain}: {len(gone)} candidate URL(s) no longer in the sitemap, e.g. {gone[0]}")
    if problems:
        for p in problems:
            print(f"FAIL: {p}")
        return 1
    print(f"internal-link index OK — {len(index['candidates'])} candidate(s), {age}d old")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the internal-link candidate index for the live sites.")
    parser.add_argument("--check", action="store_true", help="verify freshness and liveness, write nothing")
    args = parser.parse_args()
    if args.check:
        return check()

    index = build()
    INDEX_JSON.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    write_report(index)
    articles = [c for c in index["candidates"] if c["kind"] == "article"]
    others = [c for c in index["candidates"] if c["kind"] != "article"]
    print(f"indexed {len(articles)} live article(s) and {len(others)} other target(s) "
          f"across {len(index['sites'])} site(s)")
    for domain in index["sites"]:
        n = len([c for c in articles if c["site"] == domain])
        print(f"  {domain}: {n} article(s)")
    if index["not_live"]:
        print(f"  {len(index['not_live'])} post(s) published in a CMS but not live on its site:")
        for c in index["not_live"][:6]:
            print(f"    {c['site']} #{c['id']} {c['slug']}")
    print(f"  wrote {INDEX_JSON.relative_to(ROOT)} and {INDEX_MD.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
