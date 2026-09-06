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

files = sorted((ROOT / "published").glob("*.md"))
if not files:
    print("no published/*.md to sync")
    sys.exit(0)

for f in files:
    data = publish.parse_draft(str(f))
    ok = publish.sync_to_supabase(data, {})
    print(("  OK   " if ok else "  FAIL ") + f.name)
