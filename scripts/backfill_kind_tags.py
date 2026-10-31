#!/usr/bin/env python3
"""Tag the already-published archive news / evergreen / review — the backfill for kind tags.

`scripts/wp_draft.py` now tags every post it pushes (resolve_kind_term). Everything published before
that went live carries no tag at all, so a news/evergreen filter over the archive would show only the
newest handful. This script reads the classification the desk already made, writes it onto the live
posts, and reports exactly which posts it could not classify — it never guesses.

WHERE THE KIND COMES FROM (in this order, per published artifact):

  1. `kind:` in the artifact frontmatter       — written by runs after 2026-10-31;
  2. `archetype: evergreen|review`              — what the evergreen and review fleets required;
  3. a matching `<date>_<vertical>_signals.md`  — the news fleet's own brief, which is the only
     brief a news run ever writes (the other two write `_evergreen_brief.md` / `_review_brief.md`).

A post with no artifact, or an artifact that satisfies none of the three, is reported as
`unclassified` and left alone. A wrong tag on a live post is a misclassification an editor would have
to notice by hand; a missing one is visible in this script's own report.

Usage:
  python3 scripts/backfill_kind_tags.py                     # dry run: what it would tag, per site
  python3 scripts/backfill_kind_tags.py --limit 5           # dry run, the 5 newest per site
  python3 scripts/backfill_kind_tags.py --limit 5 --apply   # the small inspectable batch
  python3 scripts/backfill_kind_tags.py --apply             # the whole archive
  python3 scripts/backfill_kind_tags.py --site wellroost.com --apply

Credentials: the same WP_<SITE>_USER / WP_<SITE>_APP_PASSWORD the push uses, plus SUPABASE_URL and
SUPABASE_SERVICE_ROLE_KEY for the routing rows and the row-side bookkeeping (both from ./.env).
The tag terms are created on each destination if they are missing (post_tag is writable with the
same app password; the `vertical` vocabulary is not, and is not touched here).
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import wp_draft as wd  # noqa: E402
import publish  # noqa: E402  (derive_kind — ONE classification rule, shared with the persist pass)


def _frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    head = text.split("---", 2)[1]
    out = {}
    for line in head.splitlines():
        if ":" in line and not line.lstrip().startswith("#"):
            key, value = line.split(":", 1)
            out[key.strip()] = value.strip().strip('"').strip("'")
    return out


def kind_map(root: pathlib.Path) -> tuple[dict[str, tuple[str, str]], list[str]]:
    """{slug: (kind, how it was decided)} for every published artifact, plus the unclassified ones."""
    briefs = {p.stem for p in (root / "context" / "recon_proposals").glob("*.md")}
    mapping: dict[str, tuple[str, str]] = {}
    unclassified: list[str] = []
    for path in sorted((root / "published").glob("*.md")):
        fm = _frontmatter(path.read_text(encoding="utf-8"))
        slug = fm.get("slug") or re.sub(r"^\d{4}-\d{2}-\d{2}_", "", path.stem)
        date, vertical = fm.get("date", ""), fm.get("vertical", "")
        news_brief = f"{date}_{vertical}_signals" in briefs
        kind = publish.derive_kind(fm, news_brief=news_brief)
        if not kind:
            unclassified.append(slug)
            continue
        if str(fm.get("kind") or "").strip().lower() in wd.KINDS:
            how = "frontmatter kind:"
        elif str(fm.get("archetype") or "").strip().lower() in wd.KINDS:
            how = "frontmatter archetype:"
        elif kind == "evergreen":
            how = "frontmatter evergreen: true"
        else:
            how = f"news brief {date}_{vertical}_signals.md"
        mapping[slug] = (kind, how)
    return mapping, unclassified


def load_overrides(path: str) -> dict[str, tuple[str, str]]:
    """{slug: (kind, how)} from a decisions file — kinds an owner approved, not inferred ones.

    Some live posts have no artifact and no row anywhere (a hand-made CMS post, a push from another
    producer), so nothing on disk can classify them. Rather than guess, the proposal is reviewed and
    recorded once in `context/kind_decisions.json`; this makes that decision applyable and, above
    all, re-runnable — running the backfill again must not silently drop a decided tag.
    """
    data = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    posts = data.get("posts") if isinstance(data, dict) else data
    out: dict[str, tuple[str, str]] = {}
    for row in posts or []:
        slug = str((row or {}).get("slug") or "").strip()
        kind = str((row or {}).get("kind") or "").strip().lower()
        if not slug or kind not in wd.KINDS:
            raise SystemExit(f"FAIL: {path}: bad row {row!r} (kind must be one of {', '.join(wd.KINDS)})")
        out[slug] = (kind, f"decided: {data.get('decided', 'no date')} — {row.get('reason') or ''}".strip())
    return out


def destinations(db) -> dict[str, str]:
    """{cms_base_url: a site_domain on that CMS} — one credential scope per CMS, never a guess."""
    _, rows = db._call("GET", f"{wd.SITES_TABLE}?select=cms_base_url,site_domain,active")
    out: dict[str, str] = {}
    for row in rows or []:
        cms = (row.get("cms_base_url") or "").rstrip("/")
        domain = row.get("site_domain") or ""
        if not cms or not domain or row.get("active") is False:
            continue
        # Prefer the front whose own host is the CMS's (cms.<domain>): its credentials are the ones
        # the desk already has, while a second front over the same CMS needs an alias.
        if cms == f"https://cms.{domain}":
            out[cms] = domain
        else:
            out.setdefault(cms, domain)
    return out


def live_posts(wp) -> list[dict]:
    posts: list[dict] = []
    for page in range(1, 40):
        _, batch = wp._call("GET", f"posts?per_page=100&page={page}&status=publish"
                                   f"&orderby=date&order=desc&_fields=id,slug,date,tags")
        if not batch:
            break
        posts += batch
        if len(batch) < 100:
            break
    return posts


def main() -> int:
    parser = argparse.ArgumentParser(description="Tag the published archive news / evergreen / review")
    parser.add_argument("--apply", action="store_true",
                        help="Write the tags (default: dry run, prints what it would do)")
    parser.add_argument("--limit", type=int, default=None,
                        help="Only the N newest live posts per site — a small inspectable batch")
    parser.add_argument("--site", default=None,
                        help="Only this front domain (giniloh.com, wellroost.com)")
    parser.add_argument("--overrides", default=None,
                        help="A decisions file (context/kind_decisions.json) whose kinds beat the "
                             "inferred ones — for posts that have no artifact at all")
    args = parser.parse_args()

    root = pathlib.Path(__file__).resolve().parent.parent
    wd.load_env()
    mapping, unclassified = kind_map(root)
    if args.overrides:
        decided = load_overrides(args.overrides)
        mapping.update(decided)
        print(f"overrides: {len(decided)} decided kind(s) from {args.overrides}")
    counts = {k: sum(1 for v in mapping.values() if v[0] == k) for k in wd.KINDS}
    print(f"artifacts classified: {len(mapping)} "
          + ", ".join(f"{k} {n}" for k, n in counts.items()))
    if unclassified:
        print(f"unclassified artifacts (left alone): {len(unclassified)} — "
              f"{', '.join(unclassified[:6])}{'…' if len(unclassified) > 6 else ''}")

    db = wd.Supabase(*wd.supabase_config())
    sites = destinations(db)
    if args.site:
        sites = {cms: dom for cms, dom in sites.items() if dom == args.site}
    if not sites:
        print("FAIL: no destination CMS to read", file=sys.stderr)
        return 1

    failures = 0
    for cms, domain in sorted(sites.items()):
        try:
            user, password = wd.credentials_for(domain)
        except SystemExit:
            print(f"  {cms}: no credentials for {domain} — skipped", file=sys.stderr)
            failures += 1
            continue
        wp = wd.WordPress(cms, user, password)
        terms: dict[str, dict] = {}
        definition = (wp.taxonomies() or {}).get(wd.KIND_TAXONOMY) or {}
        rest_base = definition.get("rest_base") or wd.KIND_REST_BASE
        for kind in wd.KINDS:
            if not args.apply:
                # A dry run must not create a term: it reports what the apply would add.
                term = wp.term_by_slug(rest_base, kind) if definition else None
                if term:
                    terms[kind] = term
                else:
                    print(f"  {domain}: would create the '{kind}' tag (term absent)")
                continue
            try:
                term, note = wd.resolve_kind_term(wp, kind)
            except Exception as exc:                    # noqa: BLE001 - surface, never swallow
                print(f"  {domain}: could not resolve the '{kind}' tag: {exc}", file=sys.stderr)
                failures += 1
                continue
            if term:
                terms[kind] = term
            if note:
                print(f"  {domain}: {note}")
        posts = live_posts(wp)
        if args.limit is not None:
            posts = posts[:args.limit]
        print(f"\n{domain} ({cms}) — {len(posts)} live post(s) examined")

        tally = {"already": 0, "tagged": 0, "would": 0, "unmapped": 0, "failed": 0}
        for post in posts:
            slug = post.get("slug") or ""
            kind = mapping.get(slug, ("", ""))[0]
            if not kind:
                tally["unmapped"] += 1
                continue
            term = terms.get(kind)
            if not term and args.apply:
                tally["unmapped"] += 1          # the term could not be created: reported above
                continue
            current = sorted(int(t) for t in (post.get("tags") or []))
            wanted = [int(term["id"])] if term else []
            if wanted and current == sorted(wanted):
                tally["already"] += 1
                continue
            if not args.apply:
                where = f"tag {term['id']}" if term else f"tag '{kind}' to be created"
                print(f"  would tag {slug}: {kind} ({where}, now {current or 'none'})")
                tally["would"] += 1
                continue
            try:
                wp._call("POST", f"posts/{int(post['id'])}", {"tags": wanted})
            except Exception as exc:                    # noqa: BLE001
                print(f"  FAILED {slug}: {exc}", file=sys.stderr)
                tally["failed"] += 1
                failures += 1
                continue
            stored = sorted(int(t) for t in (wp.read_back(post["id"]).get("tags") or []))
            if stored != sorted(wanted):
                print(f"  FAILED {slug}: sent tag(s) {wanted}, CMS holds {stored}", file=sys.stderr)
                tally["failed"] += 1
                failures += 1
                continue
            print(f"  tagged {slug}: {kind} (tag {term['id']})")
            tally["tagged"] += 1

        print(f"  already correct {tally['already']} | tagged {tally['tagged']} | "
              f"{'would tag' if not args.apply else 'would tag 0'} {tally['would']} | "
              f"no artifact {tally['unmapped']} | failed {tally['failed']}")

    print("\n" + ("DRY RUN — nothing written; add --apply" if not args.apply else "done"))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
