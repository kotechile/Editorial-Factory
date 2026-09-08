#!/usr/bin/env python3
"""Sync persisted articles to the shared factory-core Supabase (public.articles).

Idempotent on metadata->>'slug'. Reads SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY from
this repo's .env (wired to the software-factory's factory-core project). Parses each
published/*.md and upserts via publish.sync_to_supabase.
"""
import os, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Load .env (repo-local) into process env for publish.sync_to_supabase.
for line in (ROOT / ".env").read_text().splitlines():
    line = line.strip()
    if line and "=" in line and not line.startswith("#"):
        k, v = line.split("=", 1)
        os.environ.setdefault(k, v.strip())

sys.path.insert(0, str(ROOT / "scripts"))
import publish  # noqa: E402  (uses os.environ at call time)

import argparse

parser = argparse.ArgumentParser(description="Sync articles (published and drafts) with rich SEO metadata to Supabase.")
parser.add_argument("files", nargs="*", help="Specific markdown file(s) to sync. If omitted, defaults to published/*.md (or context/drafts/*.md with --drafts).")
parser.add_argument("--drafts", action="store_true", help="Sync context/drafts/*_final.md instead of published/*.md")
parser.add_argument("--all", action="store_true", help="Sync both context/drafts/*_final.md and published/*.md")
args = parser.parse_args()

target_files = []
if args.files:
    for fp in args.files:
        p = pathlib.Path(fp)
        if p.exists():
            target_files.append(p)
        else:
            print(f"Warning: file not found: {fp}")
elif args.all:
    target_files = sorted((ROOT / "published").glob("*.md")) + sorted((ROOT / "context" / "drafts").glob("*_final.md"))
elif args.drafts:
    target_files = sorted((ROOT / "context" / "drafts").glob("*_final.md"))
else:
    target_files = sorted((ROOT / "published").glob("*.md"))

if not target_files:
    print("no markdown files found to sync")
    sys.exit(0)

print(f"Syncing {len(target_files)} article(s) to Supabase (URL: {os.environ.get('SUPABASE_URL', 'not set')})...")
for f in target_files:
    data = publish.parse_draft(str(f))
    ok = publish.sync_to_supabase(data, {})
    kw_info = f" [KW: {data.get('primary_keyword') or 'none'}]" if data.get('primary_keyword') else ""
    print(("  OK   " if ok else "  FAIL ") + f.name + kw_info)

