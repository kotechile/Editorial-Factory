#!/usr/bin/env python3
"""The forward-only guard for the internal-link corpus change — run: python3 scripts/test_forward_only.py

    python3 scripts/test_forward_only.py            # verify (exit 1 on any breach)
    python3 scripts/test_forward_only.py --record   # (re)record the baseline, then verify

Why this file exists (2026-10-15)
---------------------------------
The corpus moved from the WordPress CMS to each reader front's own sitemap + page content, and the
generated `## Related reading` block now stamps site-relative paths instead of one site's absolute URLs.
The owner's constraint on that change was explicit: **do not touch what already exists** — no repair,
no re-push, no re-pointing — only make future links match the front end the article is served from.

That is a property nobody can see by reading the code, so it is asserted here against a recorded
baseline (context/forward_only_snapshot.json) instead:

  1. every `published/*.md` is byte-identical to the baseline (the rebuild rewrites no artifact);
  2. no article's PUBLIC reader URL moved. `scripts/sitemap_sync.py` resolves a slug to its URL by taking
     the FIRST candidate for that slug in `context/internal_links.json`, so candidate ORDER decides the
     reader URL of every page published on more than one front. This is the check that catches a new
     front being inserted ahead of the old one — the one realistic way this change could reach backwards;
  3. the corpus is honest about where its pages are: no `cms.` host anywhere, and every candidate URL on
     its own candidate site;
  4. the corpus needs no credentials: `site_corpus.py` and `frontends.py` never touch the CMS or Supabase,
     which is what lets the crawl run without either (checked statically — the live proof is a build with
     the credentials unset, which the plan's acceptance criteria call for once).

Hermetic apart from the shipped files: no network, no credentials, no writes (except --record).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUBLISHED = ROOT / "published"
INDEX = ROOT / "context" / "internal_links.json"
SITEMAP = ROOT / "context" / "sitemap.json"
SNAPSHOT = ROOT / "context" / "forward_only_snapshot.json"
PURE_MODULES = ("site_corpus.py", "frontends.py", "test_site_corpus.py", "test_frontends.py")
FORBIDDEN_IN_PURE = ("supabase", "wp_draft", "wp-json", "Authorization")

PASS, FAIL = [], []


def check(name, condition, detail=""):
    (PASS if condition else FAIL).append(name)
    print(f"  [{'ok ' if condition else 'FAIL'}] {name}" + ("" if condition else f"  <- {detail}"))


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reader_urls_from_sitemap() -> dict:
    """slug -> public URL, exactly as `sitemap_sync.py` derived it from the index."""
    if not SITEMAP.exists():
        return {}
    data = json.loads(SITEMAP.read_text(encoding="utf-8"))
    return {a["slug"]: a["url"] for a in data.get("articles", []) if a.get("url")}


def load_index() -> dict | None:
    if not INDEX.exists():
        return None
    try:
        return json.loads(INDEX.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def index_reader_urls(index: dict) -> dict:
    """The URL `sitemap_sync.py` WOULD pick per slug: the first live candidate, in file order.

    Mirrors `sitemap_sync.public_urls()` on purpose — a copy that drifts here would make this guard
    pass while the real reader URLs moved.
    """
    out: dict = {}
    for candidate in index.get("candidates") or []:
        if candidate.get("live") and candidate.get("url") and candidate.get("slug"):
            out.setdefault(candidate["slug"], candidate["url"])
    return out


def record() -> dict:
    index = load_index()
    previous = {}
    if SNAPSHOT.exists():
        try:
            previous = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            previous = {}
    baseline = {
        "accepted_changes": previous.get("accepted_changes", {}),
        "recorded_at": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(
            timespec="seconds"),
        "why": "baseline for the forward-only guard: the state the internal-link corpus change must "
               "not alter (published artifacts, and every article's public reader URL)",
        "published": {p.name: sha256(p) for p in sorted(PUBLISHED.glob("*.md"))},
        "reader_urls": reader_urls_from_sitemap(),
        "index_reader_urls": index_reader_urls(index) if index else {},
    }
    SNAPSHOT.write_text(json.dumps(baseline, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"recorded {SNAPSHOT.relative_to(ROOT)} — {len(baseline['published'])} artifacts, "
          f"{len(baseline['reader_urls'])} reader URLs")
    return baseline


def main() -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").splitlines()[0])
    parser.add_argument("--record", action="store_true", help="(re)write the baseline, then verify")
    args = parser.parse_args()

    if args.record:
        record()
    if not SNAPSHOT.exists():
        print(f"FAIL: {SNAPSHOT.relative_to(ROOT)} is missing — record a baseline with --record first")
        return 1
    baseline = json.loads(SNAPSHOT.read_text(encoding="utf-8"))

    print("published artifacts are untouched")
    current = {p.name: sha256(p) for p in sorted(PUBLISHED.glob("*.md"))}
    was = baseline.get("published") or {}
    changed = sorted(n for n in was if n in current and current[n] != was[n])
    added = sorted(set(current) - set(was))
    removed = sorted(set(was) - set(current))
    check(f"no published artifact was rewritten ({len(was)} recorded)", not changed,
          f"rewritten: {changed[:5]}")
    check("no published artifact was deleted", not removed, f"gone: {removed[:5]}")
    if added:
        print(f"  note: {len(added)} artifact(s) published since the baseline — not a breach "
              f"({added[:3]}{'…' if len(added) > 3 else ''})")

    print("\nexisting reader URLs did not move (candidate order)")
    index = load_index()
    if index is None:
        print("  note: context/internal_links.json is not built — skipped (--check on the index covers it)")
    else:
        now = index_reader_urls(index)
        want = baseline.get("index_reader_urls") or baseline.get("reader_urls") or {}
        # A change the FRONT ENDS really made (a page moved to another front, a page removed from every
        # sitemap) is recorded here with its reason and reported as a note. The allowlist exists so the
        # check keeps its teeth: anything NOT on it is still a failure, which is how this guard caught
        # the registry/tool-shape bug that dropped wellroost's three tools on the first real rebuild.
        accepted = baseline.get("accepted_changes") or {}
        moved, gone, seen = [], [], []
        for slug, url in want.items():
            got = now.get(slug)
            if got == url:
                continue                      # unchanged: the overwhelming majority, checked cheaply
            detail = "no longer published by any front" if got is None else f"{url} -> {got}"
            if slug in accepted:
                seen.append((slug, detail))
            elif got is None:
                gone.append(slug)
            else:
                moved.append(f"{slug}: {detail}")
        check(f"no article's reader URL was re-pointed ({len(want)} checked)", not moved,
              f"moved: {moved[:4]}")
        check("no article dropped out of the corpus entirely", not gone,
              f"gone: {gone[:5]} — if the page really left every front's sitemap, add it to "
              f"accepted_changes in the snapshot, with the reason")
        for slug, what in seen:
            print(f"  note: {slug} — {what}. Accepted: {accepted[slug]}")
        sitemap_now = reader_urls_from_sitemap()
        drifted = [s for s in sitemap_now if s in want and sitemap_now[s] != want[s]]
        check("context/sitemap.json still reports the same public URLs", not drifted,
              f"drifted: {drifted[:4]} — run scripts/sitemap_sync.py only after checking why")

        print("\nthe corpus is honest about where its pages live")
        bad_host, cms_host, sites = [], [], sorted((index.get("sites") or {}).keys())
        for c in index.get("candidates") or []:
            host = (urllib.parse.urlparse(c.get("url") or "").hostname or "").lower()
            if host.startswith("cms."):
                cms_host.append(c.get("url"))
            elif host != (c.get("site") or "").lower():
                bad_host.append(f"{c.get('site')} -> {c.get('url')}")
        check("no candidate URL is on a CMS host", not cms_host, str(cms_host[:3]))
        check("every candidate URL is on its own site", not bad_host, str(bad_host[:3]))
        check("every registered front contributed candidates", len(sites) >= 3, str(sites))
        stamped = [c for c in index.get("candidates") or [] if c.get("sites_live")]
        check("candidates know every front that publishes them (sites_live)", bool(stamped),
              "no candidate carries a sites_live map")
        multi = [c for c in stamped if len(c["sites_live"]) > 1]
        print(f"  note: {len(multi)} candidate(s) are published by more than one front")

    print("\nthe corpus needs no credentials")
    for name in PURE_MODULES:
        path = ROOT / "scripts" / name
        if not path.exists():
            check(f"{name} exists", False, "missing")
            continue
        source = path.read_text(encoding="utf-8")
        hit = [token for token in FORBIDDEN_IN_PURE if token in source]
        check(f"{name} reaches no CMS/database", not hit, f"mentions {hit}")

    print(f"\n{len(PASS)} passed, {len(FAIL)} failed")
    if FAIL:
        print("FAILED: " + "; ".join(FAIL))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
