#!/usr/bin/env python3
"""Build the internal-link candidate index from each reader front's own live content.

    python3 scripts/build_internal_link_index.py            # rebuild context/internal_links.json + .md
    python3 scripts/build_internal_link_index.py --check     # CI/staleness guard, writes nothing
    python3 scripts/build_internal_link_index.py --offline    # use the page cache only (no network)

Why the source changed (2026-10-15)
-----------------------------------
The corpus used to be the WordPress CMS: `posts?status=publish` per site, with the frontend sitemap
consulted only for liveness. That stopped being true when one shared CMS began serving several
frontends that PULL different subsets of articles: a CMS row no longer says which site serves a page,
`public.vertical_sites` cannot express a pull target (aichieve.net has no row and is not getting one),
and the CMS needs a separate credential per site while the reader sites need none.

So the fronts answer for themselves now:

  * a front's own `sitemap.xml` (or `sitemap-index.xml`) says what it publishes, and
  * the page itself says what it is: `Article` JSON-LD supplies the headline, the description and the
    modified date, and the `BreadcrumbList` supplies the category hub the page is filed under.

The CMS keeps exactly two jobs, both configuration rather than content:

  1. `wp_category_id` -> category NAME for the vertical a draft is routed to (routing is unchanged, so
     this id is still what files a draft under the right CMS category); and
  2. the optional `not_live` diff — posts published in a CMS but absent from that site's sitemap. That
     list already existed and is printed by the sweep; it is kept as-is and is never a candidate source.

Liveness is still decided by the sitemap and only the sitemap: both Astro fronts have answered 200 with
the homepage for an unknown URL, so an HTTP status proves nothing. `site_corpus.fetch_page` adds the
sharper guard on top — the page's own `<link rel="canonical">` must equal the URL we asked for, which is
how a removed-but-still-answering page is kept out of the corpus.

Every candidate carries the paths it resolves to on EVERY front that publishes it (`sites_live`). That
map is what lets `scripts/internal_links.py` stamp a link as a site-relative path and still be sure it
resolves on each front that will serve the article — see the plan in
`.hermes/plans/2026-10-15_063129-internal-links-from-live-sites.md`.
"""

from __future__ import annotations

import argparse
import html
import json
import pathlib
import re
import sys
import urllib.parse
from datetime import datetime, timezone

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import frontends as fe  # noqa: E402
import site_corpus as sc  # noqa: E402
import wp_draft as wd  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX_JSON = ROOT / "context" / "internal_links.json"
INDEX_MD = ROOT / "context" / "internal_links.md"
CACHE_DIR = ROOT / "context" / ".site_cache"
STALE_AFTER_DAYS = 30

# Used when Supabase is unreachable, so the index still builds from the known sites. aichieve.net has
# no CMS and no routing rows by design: it is a front that pulls, so its entry carries an empty CMS.
FALLBACK_SITES = [
    ("giniloh.com", "https://cms.giniloh.com", "https://giniloh.com"),
    ("wellroost.com", "https://cms.wellroost.com", "https://wellroost.com"),
    ("aichieve.net", "", "https://aichieve.net"),
]

_ACRONYM_OR_COLON = re.compile(r"\b[A-Z]{2,}\b|:\s*$")


def site_list() -> tuple[list[tuple[str, str, str]], str]:
    """The fronts to index, in REGISTRY ORDER: `(domain, cms_base_url, frontend_url)`.

    `context/frontends.json` is the source of truth for WHICH fronts serve pages (it can express a pull
    target like aichieve.net, which `public.vertical_sites` cannot — that table names where a vertical
    publishes, and it is deliberately unchanged). Routing still supplies the per-domain CMS base URL,
    which is only ever used to resolve category names.

    The ORDER is load-bearing, not cosmetic: `scripts/sitemap_sync.py` resolves a slug to its public URL
    by taking the FIRST candidate for that slug, so whichever front comes first here owns the reader URL
    of every page published on more than one front. The registry leads with giniloh.com for exactly that
    reason — an article live on both giniloh.com and aichieve.net must keep the URL it already had, and
    adding a front must never re-point an article that is already live.
    """
    fronts = fe.load()
    rows = wd.supabase_get("vertical_sites?select=site_domain,cms_base_url")
    if rows is None:
        print("  routing rows unavailable — using the registry's known CMS bases", file=sys.stderr)
        cms_by_domain = {d: c for d, c, _u in FALLBACK_SITES}
        source = "context/frontends.json (routing rows unreachable)"
    else:
        cms_by_domain = {(r.get("site_domain") or "").strip(): (r.get("cms_base_url") or "").strip()
                         for r in rows}
        source = "context/frontends.json, CMS base per domain from public.vertical_sites"
        unknown = sorted(d for d in cms_by_domain if d and d not in {f["domain"] for f in fronts})
        if unknown:
            print(f"WARNING: routing names {', '.join(unknown)} but context/frontends.json does not — "
                  f"those sites are not indexed", file=sys.stderr)

    sites = [(f["domain"], cms_by_domain.get(f["domain"], ""), f["frontend_url"]) for f in fronts]
    return sites, source


def cms_category_names(domain: str, cms: str) -> dict[int, str]:
    """`{wp_category_id: name}` for one site's CMS — routing config, never a candidate source.

    Best effort by design: a front with no CMS (or a CMS that is down, or credentials that are absent)
    yields `{}`, and the build continues. Nothing in the link path depends on it.
    """
    if not cms:
        return {}
    try:
        user, password = wd.credentials_for(domain)
        if not (user and password):
            return {}
        wp = wd.WordPress(cms, user, password)
        _, rows = wp._call("GET", "categories?per_page=100&_fields=id,name")
    except Exception as exc:                                       # noqa: BLE001 - optional config
        print(f"  {domain}: CMS category names unavailable ({exc}) — hub slugs are used instead",
              file=sys.stderr)
        return {}
    # Unescaped: the CMS serves "Supply Chain &amp; Operations", and that name is slugified to match a
    # front's own hub slug (`supply-chain-operations`). Escaped, it slugifies to `supply-chain-amp-
    # operations`, matches nothing, and every article silently loses the second front from its render
    # set — the exact failure this corpus is supposed to prevent.
    return {int(c["id"]): html.unescape((c.get("name") or "").strip()) for c in rows or []}


def cms_not_live(domain: str, cms: str, live_paths: set[str]) -> list[dict]:
    """Posts published in a CMS but absent from that front's sitemap — an EXISTING, advisory diff.

    Kept because a live sweep prints it (a trashed post still served by a stale build was a real
    incident) and dropping it would silently change that output. It never proposes a candidate.
    """
    if not cms:
        return []
    try:
        user, password = wd.credentials_for(domain)
        if not (user and password):
            return []
        wp = wd.WordPress(cms, user, password)
        _, rows = wp._call("GET", "posts?status=publish&per_page=100&_fields=id,slug,title,modified")
    except Exception:                                              # noqa: BLE001 - advisory only
        return []
    out = []
    for post in rows or []:
        slug = (post.get("slug") or "").strip()
        if slug and f"/{slug}/" not in live_paths:
            title = re.sub(r"<[^>]+>", " ", (post.get("title") or {}).get("rendered", "") or "")
            out.append({"site": domain, "kind": "article", "id": post.get("id"), "slug": slug,
                        "title": " ".join(title.split()), "url": "", "categories": [],
                        "category_ids": [], "excerpt": "", "modified": post.get("modified", ""),
                        "live": False,
                        "reason": "published in the CMS but absent from the frontend sitemap"})
    return out


def _slugify_name(name: str) -> str:
    """`"Supply Chain & Operations"` -> `"supply-chain-operations"` (the fronts' own hub slug shape)."""
    return re.sub(r"[^a-z0-9]+", "-", (name or "").lower()).strip("-")


def humanise_slug(slug: str) -> str:
    return " ".join(w.capitalize() if w.islower() else w for w in re.split(r"[-_]+", slug) if w)


def build(cache_dir: pathlib.Path | None = None, *, offline: bool = False, fetch=None) -> dict:
    wd.load_env()
    cache_dir = cache_dir or CACHE_DIR
    sites, site_source = site_list()

    urls_by_domain: dict[str, list[str]] = {}
    pages: dict[str, list[dict]] = {}
    for domain, _cms, frontend in sites:
        try:
            urls_by_domain[domain] = sc.discover_sitemaps(frontend, fetch=fetch)
        except sc.SiteCorpusError as exc:
            # Never write a smaller index than the last good one: a front that cannot be read is a
            # failure of the build, not a site with no pages.
            raise SystemExit(f"FAIL: {domain}: {exc}")
        shapes = [u for u in urls_by_domain[domain] if fe.is_candidate_shape(u, domain)]
        pages[domain] = sc.metadata_for(shapes, frontend=frontend, cache_dir=cache_dir, fetch=fetch,
                                        offline=offline)

    # slug -> {front: path}. The same article served by two fronts is one slug with two paths, and it
    # is this map that decides whether a link can be stamped for every front that will serve it.
    sites_live: dict[str, dict[str, str]] = {}
    for domain, metas in pages.items():
        for meta in metas:
            sites_live.setdefault(fe.slug_of(meta["url"]), {})[domain] = fe.path_of(meta["url"])

    candidates: list[dict] = []
    hub_slugs: dict[str, list[str]] = {}
    for domain, _cms, _frontend in sites:
        metas = pages[domain]
        hubs = fe.served_categories(domain, urls_by_domain[domain])
        hub_slugs[domain] = sorted(hubs)

        for meta in metas:
            slug = fe.slug_of(meta["url"])
            kind = meta["kind"]
            names = [c["name"] for c in meta.get("categories", []) if c.get("name")]
            candidates.append({
                "site": domain,
                "kind": kind,
                "id": None,                     # no CMS row stands behind a front page any more
                "slug": slug,
                "title": meta.get("title") or humanise_slug(slug),
                "url": meta["url"],
                "path": fe.path_of(meta["url"]),
                # The paths this page resolves to on every front that publishes it. A link may only be
                # stamped when this covers every front that will serve the article.
                "sites_live": dict(sites_live.get(slug, {})),
                "categories": names or ([humanise_slug(slug)] if kind == "category" else []),
                "category_ids": [],
                "category_slugs": meta.get("category_slugs", []),
                "excerpt": meta.get("excerpt", ""),
                "modified": meta.get("modified", ""),
                "live": True,
                "source": "frontend-sitemap",
            })

        # Category hubs and tools/calculators need no second pass: they are candidate-shaped URLs, so
        # `metadata_for` already fetched them and classified them. (An earlier revision re-derived them
        # from the URL list, which would have re-added a hub page whose metadata had been REJECTED — a
        # page that is not the page we asked for is never a link target.)

    # Category names: the CMS answers for the routing id when it can, the front's own hub page title is
    # the fallback. Only the reader-facing "— more on <category>" copy uses them.
    categories: dict[str, dict[str, str]] = {}
    for domain, cms, _frontend in sites:
        by_id = cms_category_names(domain, cms)
        names = {str(k): v for k, v in by_id.items() if v}
        # A hub's name is the hub page's own title (the site suffix stripped by the corpus reader).
        # Humanising the slug instead produced "Ai Stack Tool Tco" in reader-facing copy.
        hub_titles = {fe.slug_of(m["url"]): (m.get("title") or "")
                      for m in pages[domain] if m["kind"] == "category"}
        for slug in hub_slugs.get(domain, []):
            if not any(v and _slugify_name(v) == slug for v in names.values()):
                names[f"hub:{slug}"] = hub_titles.get(slug) or humanise_slug(slug)
        categories[domain] = names

    not_live: list[dict] = []
    for domain, cms, _frontend in sites:
        live_paths = {fe.path_of(u) for u in urls_by_domain[domain]}
        not_live += cms_not_live(domain, cms, live_paths)

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "site_source": site_source,
        "sites": {d: {"cms": c, "frontend": f} for d, c, f in sites},
        "hub_slugs": hub_slugs,
        "categories": categories,
        "candidates": candidates,
        "not_live": not_live,
    }


def write_report(index: dict) -> None:
    lines = [f"# Internal-link candidates — {index['generated_at']}", "",
             f"Source of sites: {index['site_source']}. Candidates are the pages each front end "
             "publishes (its own sitemap), described by the page itself; liveness is the sitemap plus "
             "the page's own canonical URL, never an HTTP status.", ""]
    for domain in index["sites"]:
        rows = [c for c in index["candidates"] if c["site"] == domain]
        articles = [c for c in rows if c["kind"] == "article"]
        hubs = ", ".join(index.get("hub_slugs", {}).get(domain, [])) or "—"
        lines += [f"## {domain} — {len(articles)} live article(s), "
                  f"{len(rows) - len(articles)} other target(s)", "",
                  f"Category hubs this front serves: {hubs}", ""]
        for c in sorted(rows, key=lambda r: (r["kind"] != "article", r["title"])):
            label = c["title"] if c["kind"] == "article" else f"{c['title']} ({c['kind']})"
            cats = ", ".join(c["categories"]) or "—"
            # The OTHER fronts that publish this page — the page's own front is already its link.
            others = {d: p for d, p in c["sites_live"].items() if d != c["site"]}
            also = " · ".join(f"{d}{p}" for d, p in sorted(others.items()))
            lines.append(f"- [{label}]({c['url']}) — {cats}" + (f" — also served by {also}" if also else ""))
        lines.append("")
    if index.get("not_live"):
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

    # A candidate must belong to the site it claims: a cms.* host in the corpus is the old, wrong model.
    for c in index["candidates"]:
        host = (urllib.parse.urlparse(c.get("url") or "").hostname or "").lower()
        if host.startswith("cms."):
            problems.append(f"{c['site']}: candidate URL is on a CMS host ({c['url']})")
        elif host != (c.get("site") or "").lower():
            problems.append(f"{c['site']}: candidate URL is not on its own site ({c['url']})")

    # A candidate whose URL has dropped out of the sitemap would link readers to a soft-404.
    for domain, meta in index["sites"].items():
        try:
            live = set(sc.discover_sitemaps(meta["frontend"]))
        except Exception as exc:                      # noqa: BLE001 - report, do not crash the gate
            problems.append(f"{domain}: could not re-read the sitemap ({exc})")
            continue
        gone = [c["url"] for c in index["candidates"] if c["site"] == domain and c["url"] not in live]
        if gone:
            problems.append(f"{domain}: {len(gone)} candidate URL(s) no longer in the sitemap, e.g. {gone[0]}")
    if problems:
        for p in problems[:8]:
            print(f"FAIL: {p}")
        return 1
    print(f"internal-link index OK — {len(index['candidates'])} candidate(s), {age}d old")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the internal-link candidate index from the "
                                                 "reader fronts' own live content.")
    parser.add_argument("--check", action="store_true", help="verify freshness and liveness, write nothing")
    parser.add_argument("--offline", action="store_true", help="use the cached pages only (no network)")
    parser.add_argument("--cache-dir", default=str(CACHE_DIR), help="page cache directory")
    args = parser.parse_args()
    if args.check:
        return check()

    index = build(pathlib.Path(args.cache_dir), offline=args.offline)
    INDEX_JSON.write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    write_report(index)
    articles = [c for c in index["candidates"] if c["kind"] == "article"]
    others = [c for c in index["candidates"] if c["kind"] != "article"]
    print(f"indexed {len(articles)} live article(s) and {len(others)} other target(s) "
          f"across {len(index['sites'])} site(s)")
    for domain in index["sites"]:
        n = len([c for c in articles if c["site"] == domain])
        hubs = len(index.get("hub_slugs", {}).get(domain, []))
        print(f"  {domain}: {n} article(s), {hubs} category hub(s)")
    if index["not_live"]:
        print(f"  {len(index['not_live'])} post(s) published in a CMS but not live on its site:")
        for c in index["not_live"][:6]:
            print(f"    {c['site']} #{c['id']} {c['slug']}")
    print(f"  wrote {INDEX_JSON.relative_to(ROOT)} and {INDEX_MD.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
