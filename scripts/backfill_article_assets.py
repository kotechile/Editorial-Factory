#!/usr/bin/env python3
"""Bring already-published articles up to the derived-asset contract (SEO metadata + chart).

The problem this closes: every article persisted before `scripts/publish.py` learned to derive these
carried `seo: {secondary_keywords: []}` and nothing else, so the CMS draft's excerpt fell back to a
lead paragraph and no draft carried a visual — "why is there no schema/SVG in WordPress" is answered
by "the generator never produced one", and this is the repair for the rows already in flight.

What it writes, per article:
  - published/<date>_<slug>.md   — the reader copy, with the derived frontmatter keys and the chart
  - public.articles              — metadata.seo (meta_title/meta_description + provenance, schema
                                   when the artifact has one) and the body/content columns

Deliberately NOT a publish run: it does not append to context/published_log.md, does not re-create
distribution cards, and does not deploy. Re-run the CMS sweep afterwards to push and verify:
    python3 scripts/wp_draft.py --all

Idempotent: an article that already carries the keys and (where chartable) a chart is left untouched.
Usage:
    python3 scripts/backfill_article_assets.py                 # dry run (default)
    python3 scripts/backfill_article_assets.py --apply
    python3 scripts/backfill_article_assets.py --apply --slug disney-hulu-fourth-hike-subscription-creep
"""

from __future__ import annotations

import argparse
import json
import os
import pathlib
import sys
import urllib.parse
import urllib.request

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import article_assets  # noqa: E402
import publish as publish_mod  # noqa: E402

FIELDS = "id,metadata,content"


def supabase_patch(table: str, slug: str, payload: dict) -> int:
    url = os.environ.get("SUPABASE_URL", "").rstrip("/")
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")
    request = urllib.request.Request(
        f"{url}/rest/v1/{table}?metadata->>slug=eq.{urllib.parse.quote(slug)}",
        data=json.dumps(payload).encode(),
        headers={"apikey": key, "Authorization": f"Bearer {key}",
                 "Content-Type": "application/json", "Accept": "application/json",
                 "Prefer": "return=minimal"},
        method="PATCH")
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.status


def live_columns() -> set[str] | None:
    url = os.environ.get("SUPABASE_URL", "").rstrip("/")
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")
    return publish_mod._articles_live_columns(url, key)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--apply", action="store_true", help="write the changes (default: dry run)")
    parser.add_argument("--slug", default=None, help="limit to one slug")
    parser.add_argument("--no-supabase", action="store_true",
                        help="rewrite the published files only (no database write)")
    parser.add_argument("--push", action="store_true",
                        help="after applying, update each article's CMS draft and verify the read-back"
                             " (scripts/wp_draft.py push_by_slug)")
    args = parser.parse_args()

    publish_mod.load_env()
    files = sorted((REPO_ROOT / "published").glob("*.md"))
    if args.slug:
        files = [f for f in files if args.slug in f.name]
        if not files:
            print(f"FAIL: no published/*.md matches slug {args.slug!r}")
            return 1

    columns = None if args.no_supabase else live_columns()
    if columns is not None:
        print(f"  (live articles columns: {', '.join(sorted(columns))})\n")

    wp_draft = None
    if args.push:
        import importlib.util
        wp_spec = importlib.util.spec_from_file_location("wp_draft", REPO_ROOT / "scripts" / "wp_draft.py")
        if wp_spec is None or wp_spec.loader is None:
            print("FAIL: cannot load scripts/wp_draft.py")
            return 1
        wp_draft = importlib.util.module_from_spec(wp_spec)
        wp_spec.loader.exec_module(wp_draft)

    touched = 0
    for path in files:
        before = path.read_text(encoding="utf-8")
        try:
            data = publish_mod.parse_draft(str(path))
        except Exception as exc:                    # noqa: BLE001 - report per file, keep going
            print(f"  FAIL {path.name}: {exc}")
            continue
        enriched, notes = publish_mod.apply_derived_assets(before)
        slug = data["slug"]
        changed_file = enriched != before
        seo = {
            "meta_title": data.get("meta_title") or None,
            "meta_title_source": data.get("meta_title_source") or None,
            "meta_description": data.get("meta_description") or None,
            "meta_description_source": data.get("meta_description_source") or None,
            "schema": data.get("schema"),
        }
        seo = {k: v for k, v in seo.items() if v not in (None, "", [], {})}
        print(f"  {path.name}")
        print(f"    slug: {slug} | meta_title: {(seo.get('meta_title') or '(none)')[:48]!r}")
        print(f"    meta_description: {len(seo.get('meta_description') or '')} chars "
              f"({seo.get('meta_description_source') or 'from the artifact'})")
        print(f"    schema: {'yes — ' + str((data.get('schema') or {}).get('@type')) if data.get('schema') else 'none in artifact'}")
        print(f"    chart: {'in the file' if '<svg' in enriched else 'not chartable'} | "
              f"{'file rewrite needed' if changed_file else 'file already current'}")
        touched += 1 if changed_file else 0

        if not args.apply:
            continue
        if changed_file:
            path.write_text(enriched, encoding="utf-8")
        if args.no_supabase:
            continue

        existing = fetch_row(slug)
        if not existing:
            print(f"    ! no Supabase row for {slug} — file updated, database left alone")
            continue
        # Merge, never replace: metadata holds the wordpress write-back and the sources list.
        merged = dict(existing[0].get("metadata") or {})
        merged["seo"] = {**(merged.get("seo") or {}), **seo}
        payload = {"metadata": merged}
        for column in ("content", "body_md"):
            if columns is None or column in columns:
                payload[column] = data["body_md"]
        status = supabase_patch("articles", slug, payload)
        print(f"    → Supabase PATCH {status}: metadata.seo + {'content' if 'content' in payload else 'no body column'}")

        if args.push and wp_draft is not None:
            try:
                result = wp_draft.push_by_slug(slug)
                verdict = "verified" if result["verified"] else f"NOT VERIFIED: {result['problems']}"
                print(f"    → CMS draft {result['status']} post {result['post_id']}: {verdict}")
                print(f"      {result['edit_url']}")
            except Exception as exc:                # noqa: BLE001 - per-article, never fatal
                print(f"    ! CMS push failed for {slug}: {exc}")

    print(f"\n  {touched} of {len(files)} published file(s) needed a rewrite"
          f"{'' if args.apply else ' (dry run — nothing written; pass --apply)'}")
    return 0


def fetch_row(slug: str) -> list[dict]:
    url = os.environ.get("SUPABASE_URL", "").rstrip("/")
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")
    request = urllib.request.Request(
        f"{url}/rest/v1/articles?select={FIELDS}&metadata->>slug=eq.{urllib.parse.quote(slug)}",
        headers={"apikey": key, "Authorization": f"Bearer {key}", "Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=45) as response:
        return json.loads(response.read().decode() or "[]")


if __name__ == "__main__":
    sys.exit(main())
