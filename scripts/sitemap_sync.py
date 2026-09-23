#!/usr/bin/env python3
"""Derive context/sitemap.json from published/*.md.

`context/sitemap.json` is the SEO tab's article index and the input to the Growth OS /
GSC-feedback loops. It used to be hand-maintained and drifted silently: after the
2026-09-19 fresh-start commit it still listed four deleted 09-03/09-04/09-07 articles,
omitted everything published since, and carried a stale `editorialfactory.io` base URL.

Published markdown is the source of truth for "is it live?", so the sitemap is derived
from it. Run this after every publish:

    python3 scripts/sitemap_sync.py           # rewrite context/sitemap.json
    python3 scripts/sitemap_sync.py --check   # exit 1 if it disagrees with published/

`verify.sh` runs --check, so a publish that forgets this step fails the gate instead of
leaving a dashboard advertising articles that no longer exist.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUB_DIR = ROOT / "published"
SITEMAP = ROOT / "context" / "sitemap.json"
DEFAULT_BASE = "https://pressflow.aichieve.net/published"


def base_url() -> str:
    return os.environ.get("PRESSFLOW_READER_BASE_URL", DEFAULT_BASE).rstrip("/")


def parse_frontmatter(text: str) -> dict:
    m = re.match(r"^---\s*\n([\s\S]*?)\n---", text)
    if not m:
        return {}
    data: dict = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", line)
        if not km:
            continue
        key, raw = km.group(1), km.group(2).strip()
        if raw.startswith("[") and raw.endswith("]"):
            try:
                data[key] = json.loads(raw)
            except json.JSONDecodeError:
                data[key] = [s.strip().strip("\"'") for s in raw[1:-1].split(",") if s.strip()]
        elif len(raw) > 1 and raw[0] == raw[-1] and raw[0] in "\"'":
            data[key] = raw[1:-1]
        else:
            data[key] = raw
    return data


def h2_topics(text: str) -> list:
    body = text.split("\n## Sources")[0]
    return re.findall(r"^##\s+(.+)$", body, re.M)


def entry_for(path: Path, base: str) -> dict:
    text = path.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)
    slug = path.name[:-3]
    secondary = fm.get("secondary_keywords") or []
    if isinstance(secondary, str):
        secondary = [secondary]
    return {
        "slug": slug,
        "title": fm.get("title") or fm.get("meta_title") or slug,
        "url": f"{base}/{path.name}",
        "vertical": fm.get("vertical", ""),
        "primary_keyword": fm.get("primary_keyword", ""),
        "secondary_keywords": secondary,
        "h2_topics": h2_topics(text),
        "target_persona": fm.get("persona") or fm.get("target_persona", ""),
        "date": fm.get("date", ""),
    }


def build() -> dict:
    base = base_url()
    articles = [entry_for(p, base) for p in sorted(PUB_DIR.glob("*.md"))]
    return {
        "updated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "base_url": base,
        "articles": articles,
    }


def _without_timestamp(data: dict) -> dict:
    data = dict(data)
    data.pop("updated_at", None)
    return data


def main() -> int:
    ap = argparse.ArgumentParser(description="Derive context/sitemap.json from published/*.md")
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if sitemap.json disagrees with published/")
    args = ap.parse_args()

    fresh = build()
    if args.check:
        if not SITEMAP.exists():
            print(f"FAIL: {SITEMAP.relative_to(ROOT)} is missing ({len(fresh['articles'])} published articles)")
            return 1
        current = json.loads(SITEMAP.read_text(encoding="utf-8"))
        if _without_timestamp(current) != _without_timestamp(fresh):
            have = {a.get("slug") for a in current.get("articles", [])}
            want = {a.get("slug") for a in fresh["articles"]}
            missing = sorted(want - have)
            stale = sorted(have - want)
            print("FAIL: context/sitemap.json has drifted from published/")
            if missing:
                print(f"  missing (published but not in the sitemap): {missing}")
            if stale:
                print(f"  stale (in the sitemap but not in published/): {stale}")
            if not missing and not stale:
                print("  same slugs, different field values — run scripts/sitemap_sync.py")
            print("  fix: python3 scripts/sitemap_sync.py")
            return 1
        print(f"sitemap:    ok — {len(fresh['articles'])} published articles in sync")
        return 0

    SITEMAP.write_text(json.dumps(fresh, indent=2) + "\n", encoding="utf-8")
    print(f"sitemap:    wrote {len(fresh['articles'])} articles to context/sitemap.json "
          f"(base {fresh['base_url']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
