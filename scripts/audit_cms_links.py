#!/usr/bin/env python3
"""Audit the internal anchors inside the CMS post bodies — read-only, writes nothing to the CMS.

    python3 scripts/audit_cms_links.py                 # summary + the worst posts
    python3 scripts/audit_cms_links.py --json          # machine-readable, for the fixer
    python3 scripts/audit_cms_links.py --post 880      # one post

Why the obvious question is the wrong one
-----------------------------------------
"Does this post link to another site?" is measured against the CMS install and answers almost nothing
here, because one shared CMS now serves several fronts that pull different category subsets of it. What
matters is whether an anchor is internal **on the front that serves the post**, and since 2026-10-15 that
is not the same question: giniloh.com dropped 85 of its articles to aichieve.net, so a `https://giniloh.com/...`
anchor inside one of those bodies is a cross-site link for the reader on aichieve.net while looking
perfectly "same-site" to any per-install check.

So every anchor to a reader front is classified against the post's SERVE SET — the fronts whose own
sitemap publishes that slug (from `context/internal_links.json`, whose `sites_live` map is built exactly
that way):

    internal       resolves on every front that serves the post, already relative → nothing to do
    cross-site     the DEFECT: the post is rendered by more than one front and the anchor is one of
                   their absolute URLs (it leaves the site for every reader but one), or the anchor
                   points at a front that does not serve this post at all
                   → rewrite to the relative path those fronts share
    same-front     a single front serves the post and the anchor is that front's own absolute URL:
                   already internal where it is read → reported; rewritten only with
                   `--include-same-front` (the fixer's flag)
    divergent      the fronts publish the target at different paths (giniloh `/calculators/x/` vs
                   aichieve `/tools/x/`) → one relative path cannot be right on both; report it
    retired        the target is in no front's sitemap at all → report it; deleting reader-visible
                   text is the owner's call, never a mechanical cleanup
    self-link      the post links to its own page → reported; removable with `--drop-self-links`
    external       any other host: not ours

Read-only: this script never writes to a CMS, a row or the corpus. It exists so the repair (Task C2/C3)
can be sized, ordered and reviewed before anything is written.
"""

from __future__ import annotations

import argparse
import collections
import json
import pathlib
import re
import sys
import urllib.parse

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import wp_draft as wd  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX = ROOT / "context" / "internal_links.json"
REPORT = ROOT / "context" / "cms_link_audit.json"
A_HREF = re.compile(r"""<a\s[^>]*href=["']([^"']+)["']""", re.I)

FRONT_HOSTS = ("giniloh.com", "wellroost.com", "aichieve.net")


def load_corpus() -> tuple[dict, dict]:
    """`(sites_live, paths_by_front)` from the internal-link corpus.

    `sites_live[slug]` is `{front: path}` for every front that publishes that page — the serve set.
    `paths_by_front[front]` is every path that front publishes, so a target's presence can be checked
    without a second crawl.
    """
    index = json.loads(INDEX.read_text(encoding="utf-8"))
    sites_live = {c["slug"]: dict(c.get("sites_live") or {}) for c in index.get("candidates", [])}
    paths: dict[str, set[str]] = collections.defaultdict(set)
    for c in index.get("candidates", []):
        if c.get("path"):
            paths[c["site"]].add(c["path"])
    return sites_live, paths


def classify(href: str, *, serve: set[str], paths: dict, slug: str) -> str:
    """One anchor's class — delegated to `fix_cms_links.classify`, the single owner of the rule.

    Two classifiers that can disagree is exactly the drift this repo keeps paying for: the audit decides
    what the repair will touch, so they must be the same function. The classes are the fixer's:
    `internal`, `cross-site` (the defect), `same-front` (cosmetic), `divergent`, `retired`, `self-link`,
    `external`.
    """
    import fix_cms_links as fx                       # deferred: fix_cms_links imports THIS module
    return fx.classify(href, slug=slug, serve=serve, paths=paths)


def audit_post(*, cms_domain: str, post: dict, sites_live: dict, paths: dict) -> dict:
    html = (post.get("content") or {}).get("rendered") or ""
    slug = post.get("slug") or ""
    # The fixer's own serve-set rule, fallback included: a post the corpus does not know is served by
    # its own front. Re-deriving it here (the first revision read `sites_live` directly, with no
    # fallback) made the audit classify exactly the posts the fixer had just rewritten as if they had
    # no serving front at all — an instrument that disagrees with the tool it verifies is worse than no
    # instrument.
    import fix_cms_links as fx
    serve = fx.serve_set_for(slug, cms_domain, sites_live)
    anchors = []
    for href in A_HREF.findall(html):
        cls = classify(href, serve=serve, paths=paths, slug=slug)
        if cls != "external":
            anchors.append({"href": href, "class": cls})
    counts = collections.Counter(a["class"] for a in anchors)
    return {"cms": cms_domain, "id": post.get("id"), "slug": slug, "link": post.get("link", ""),
            "serve": sorted(serve), "anchors": len(anchors), "counts": dict(counts),
            "needs_fix": counts.get("cross-site", 0), "detail": anchors}


def cms_installs() -> dict[str, str]:
    rows = wd.supabase_get("vertical_sites?select=site_domain,cms_base_url")
    out: dict[str, str] = {}
    for r in rows or []:
        d = (r.get("site_domain") or "").strip()
        c = (r.get("cms_base_url") or "").strip()
        if d and c:
            out.setdefault(d, c)
    return out


def fetch_posts(domain: str, cms: str, only_id: int | None = None) -> list[dict]:
    user, password = wd.credentials_for(domain)
    wp = wd.WordPress(cms, user, password)
    fields = "id,slug,link,content"
    if only_id:
        try:
            _, one = wp._call("GET", f"posts/{only_id}?_fields={fields}")
        except RuntimeError:
            # The id belongs to the OTHER install (each CMS numbers its own posts), so this one simply
            # does not have it. Not an error: `--post 878` should audit that post wherever it lives.
            return []
        return [one] if one else []
    out, page = [], 1
    while True:
        try:
            _, rows = wp._call("GET",
                               f"posts?status=publish&per_page=50&page={page}&_fields={fields}")
        except RuntimeError:                  # REST 400 on a page past the last one
            break
        if not rows:
            break
        out += rows
        page += 1
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").splitlines()[0])
    parser.add_argument("--json", action="store_true", help="print the full report as JSON")
    parser.add_argument("--post", type=int, help="audit a single post id")
    args = parser.parse_args()

    wd.load_env()
    sites_live, paths = load_corpus()
    installs = cms_installs()

    reports = []
    for domain, cms in installs.items():
        for post in fetch_posts(domain, cms, args.post):
            rep = audit_post(cms_domain=domain, post=post, sites_live=sites_live, paths=paths)
            if rep["anchors"]:
                reports.append(rep)

    REPORT.write_text(json.dumps(reports, indent=1) + "\n", encoding="utf-8")
    if args.json:
        print(json.dumps(reports, indent=1))
        return 0

    totals = collections.Counter()
    for r in reports:
        totals.update(r["counts"])
    print(f"posts with a front anchor: {len(reports)}   (wrote {REPORT.relative_to(ROOT)})")
    print("anchors by class: " + ", ".join(f"{k}={v}" for k, v in totals.most_common()))
    fixable = [r for r in reports if r["counts"].get("cross-site")]
    print(f"posts with a cross-site anchor (the repair set): {len(fixable)} "
          f"({sum(r['counts'].get('cross-site', 0) for r in fixable)} anchors)")
    rest = collections.Counter()
    for r in reports:
        rest.update({k: v for k, v in r["counts"].items()
                     if k in ("same-front", "retired", "divergent", "self-link")})
    print("reported, never rewritten by default: " + ", ".join(f"{k}={v}" for k, v in rest.most_common()))
    print("\nworst 10:")
    for r in sorted(fixable, key=lambda x: -x["needs_fix"])[:10]:
        print(f"  {r['cms']:14s} #{r['id']:<5} {r['slug'][:44]:44s} "
              f"serve={','.join(r['serve']) or '-':28s} {r['counts']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
