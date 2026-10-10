#!/usr/bin/env python3
"""Prove, against the real CMS, that the generated JSON-LD and inline SVG actually reach WordPress.

A push-only connector cannot answer "is the schema/SVG in WordPress": the 201 says the request was
accepted, while WordPress (or a plugin, or the editor) is free to sanitize, re-encode or drop anything
in `post_content` on save. This script closes that gap: it builds ONE article's payload out of real
generated material — a verified citation-hub dossier's `Dataset` node plus a real artifact's chart —
creates it as a clearly-labelled, explicitly DRAFT post, reads it back with `context=edit`, compares
every delivered field, confirms the probe is not publicly visible, and (unless `--keep`) trashes it
again and confirms the CMS is back at its baseline.

The probe pins its own payload to `status: "draft"` on purpose: the connector's default is now
`publish` (the reader sites are the destination), and a transport check must never put a test post in
front of readers. Pinning it here is what keeps the "not publicly visible" checks below meaningful.

Nothing here touches Supabase: the payload is built in memory and never written to a row.

Usage:
  python3 scripts/check_cms_delivery.py --vertical agentic_ai
  python3 scripts/check_cms_delivery.py --vertical agentic_ai --keep    # leave the draft to inspect
"""

from __future__ import annotations

import argparse
import base64
import importlib.util
import json
import pathlib
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import article_assets  # noqa: E402
import citation_hub_dossier as chd  # noqa: E402
import wp_draft as wd  # noqa: E402

PASS, FAIL = [], []


def check(name: str, condition: bool, detail: str = ""):
    (PASS if condition else FAIL).append(name)
    print(f"  [{'ok ' if condition else 'FAIL'}] {name}{'' if condition else f'  <- {detail}'}")


def anonymous_count(base: str) -> str:
    """Published-post count without credentials (the `x-wp-total` header), or the error text."""
    request = urllib.request.Request(f"{base}/wp-json/wp/v2/posts?per_page=1&status=publish",
                                     method="HEAD")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.headers.get("x-wp-total", "?")
    except urllib.error.HTTPError as exc:
        return f"HTTP {exc.code}"
    except Exception as exc:                        # noqa: BLE001
        return str(exc)[:60]


def anonymous_slugs(base: str, slug: str) -> list:
    try:
        with urllib.request.urlopen(f"{base}/wp-json/wp/v2/posts?slug={slug}&_fields=id,slug",
                                    timeout=30) as response:
            return json.loads(response.read().decode() or "[]")
    except Exception as exc:                        # noqa: BLE001
        return [{"error": str(exc)[:80]}]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--vertical", default="agentic_ai", help="a vertical routed in vertical_sites")
    parser.add_argument("--article", default=None, help="published/*.md to take the body + chart from")
    parser.add_argument("--keep", action="store_true", help="leave the delivery-check draft in place")
    args = parser.parse_args()

    db = wd.Supabase(*wd.supabase_config())
    site = db.site_for(args.vertical)
    base = site["cms_base_url"]
    user, password = wd.credentials_for(site["site_domain"])
    wp = wd.WordPress(base, user, password)

    print(f"target      : {site['site_domain']} ({base})")
    print(f"vertical    : {args.vertical}\n")

    # ── the material: a REAL verified dossier (no invented metrics) + a real artifact's chart ──
    dossier = chd.get_claimed_dossier(args.vertical, "agentic ai enterprise benchmarks")
    ok, errors, _report = chd.verify_dossier(dossier)
    check("the dossier behind the test node is verified against its live sources", ok, str(errors)[:120])

    artifact = pathlib.Path(args.article) if args.article else max(
        (REPO_ROOT / "published").glob("*.md"),
        key=lambda p: len(article_assets.chart_series(p.read_text(encoding="utf-8"))[0]))
    enriched, notes = article_assets.ensure_assets(artifact.read_text(encoding="utf-8"))
    print(f"  [assets] {artifact.name}: {'; '.join(notes)}")

    slug = f"delivery-check-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}"
    headline = "DELIVERY CHECK — schema + chart transport (safe to delete)"
    dataset = chd.generate_dataset_schema(dossier, headline, "Transport check for JSON-LD delivery.",
                                          slug)
    row = {
        "id": "delivery-check",
        "title": headline,
        "content": enriched,
        "tags": [args.vertical],
        "metadata": {
            "slug": slug,
            "vertical": args.vertical,
            "headline": headline,
            "seo": {
                "meta_description": "Verifies that a generated Dataset node and an inline SVG chart "
                                    "reach the CMS intact. Created and removed by "
                                    "scripts/check_cms_delivery.py.",
                "schema": {"@context": "https://schema.org", "@graph": [dataset]},
            },
        },
    }

    payload, mapping_notes = wd.build_payload(row, site, publisher_name=site["site_domain"])
    # The connector publishes by default. This probe is test residue, not content: pin it to draft so
    # running the check can never publish a "DELIVERY CHECK" placeholder to the reader site.
    payload["status"] = "draft"
    sent_ld, sent_svg = payload["content"].count("application/ld+json"), payload["content"].count("<svg")
    sent_bytes = len(payload["content"])
    print(f"payload     : {sent_bytes} chars | {sent_ld} JSON-LD block(s) | {sent_svg} inline SVG(s)")
    print(f"              slug {slug}\n")
    check("the payload actually carries a chart (else the SVG checks below prove nothing)",
          sent_svg >= 1, f"selected {artifact.name}: no chartable series found in published/")

    before_published = anonymous_count(base)
    post, action = wp.upsert(payload)
    post_id = post.get("id")
    print(f"pushed      : {action} post {post_id} ({post.get('status')}) "
          f"{base}/wp-admin/post.php?post={post_id}&action=edit\n")

    try:
        # ── read it back and compare ──
        stored = wp.read_back(post_id)
        problems = wd.delivery_problems(payload, stored)
        stored_content = (stored.get("content") or {}).get("raw") or ""
        check("the CMS holds the exact body that was sent",
              stored_content.strip() == payload["content"].strip(),
              f"sent {sent_bytes} chars, CMS holds {len(stored_content)}")
        check("the JSON-LD <script> block survived the save", stored_content.count("application/ld+json") == sent_ld)
        check("...and its node parses back to the same JSON",
              json.dumps(wd._ld_blocks(stored_content), sort_keys=True)
              == json.dumps(wd._ld_blocks(payload["content"]), sort_keys=True))
        check("...with the destination's identity, not the generator's",
              site["frontend_url"] in stored_content and "editorial-factory.com" not in stored_content)
        check("the inline SVG chart survived the save as markup",
              stored_content.count("<svg") == sent_svg and "&lt;svg" not in stored_content)
        check("the excerpt (the frontends' <meta description> source) is populated",
              bool(wd._plain_text((stored.get("excerpt") or {}).get("raw"))))
        check("no delivery problem reported by the connector's own read-back", problems == [], str(problems))
        check("the probe post is DRAFT (the connector publishes by default; a probe must not)",
              stored.get("status") == "draft", str(stored.get("status")))

        # ── and it is not public ──
        check("the draft is absent from the anonymous post list", anonymous_slugs(base, slug) == [],
              str(anonymous_slugs(base, slug)))
        check("the published-post count is unchanged by the push", anonymous_count(base) == before_published,
              f"{before_published} -> {anonymous_count(base)}")
    finally:
        if args.keep:
            print(f"\n  --keep: draft {post_id} left in place for inspection")
        else:
            # force=true: a delivery-check draft is test residue, not content for the operator to triage.
            status, _ = wp._call("DELETE", f"posts/{int(post_id)}?force=true")
            print(f"\n  cleaned up: DELETE posts/{post_id} -> HTTP {status}")
            try:
                after = wp.read_back(post_id)
                check("the draft is removed (nothing left behind to triage)",
                      str(after.get("status")) in ("trash", "deleted"), str(after.get("status")))
            except Exception as exc:                # noqa: BLE001 - a 404 also means it is gone
                check("the draft is gone (404 on read-back)", "404" in str(exc), str(exc)[:80])
            check("no delivery-check post remains in the anonymous list",
                  anonymous_slugs(base, slug) == [])

    print(f"\n{len(PASS)} passed, {len(FAIL)} failed")
    for name in FAIL:
        print(f"  FAILED: {name}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
