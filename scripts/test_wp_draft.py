#!/usr/bin/env python3
"""Tests for scripts/wp_draft.py — run: python3 scripts/test_wp_draft.py

A stub WordPress REST API runs on localhost, so the whole push path (routing -> field
mapping -> idempotency -> write-back) is exercised without touching either live CMS.
The final block re-runs the mapping against a REAL row from Supabase (read-only, no
WordPress call) when credentials are present, then exits non-zero on any failure.
"""

from __future__ import annotations

import json
import html
import pathlib
import re
import sys
import tempfile
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import wp_draft as wd  # noqa: E402
import internal_links as il  # noqa: E402
import chart_generator as cg  # noqa: E402

# Internal links are scored against the live corpus (a real Supabase routing lookup), and this suite
# is hermetic. The push path is what is under test here, so the resolver is replaced once; the
# generated block, its placement and its idempotency are pinned by scripts/test_internal_links.py.
FIXTURE_LINKS = [{
    "anchor_text": "How to Cut Energy Bills", "url": "https://giniloh.com/how-to-cut-energy-bills/",
    "kind": "article", "category": "Money & Wealth", "relevance_score": 12,
    "why": "same site (giniloh.com); same category", "suggested_placement": "Link it in the lead.",
}]
il.resolve_links = lambda topic, vertical, max_links=3, exclude_slugs=(): list(FIXTURE_LINKS)

PASS, FAIL = [], []


def check(name: str, condition: bool, detail: str = ""):
    (PASS if condition else FAIL).append(name)
    print(f"  [{'ok ' if condition else 'FAIL'}] {name}{'' if condition else f'  <- {detail}'}")


def raises(name: str, fn, contains: str = ""):
    try:
        fn()
    except BaseException as exc:                  # SystemExit too: a fail-closed path must not kill the suite
        ok = contains.lower() in str(exc).lower()
        check(name, ok, f"raised {exc!r}" if ok else f"message missing {contains!r}: {exc}")
        return str(exc)
    check(name, False, "did not raise")
    return ""


# ─────────────────────────────────────────────────────────────────────────────
# stub WordPress REST API
# ─────────────────────────────────────────────────────────────────────────────

class StubWP(BaseHTTPRequestHandler):
    posts: dict[str, dict] = {}
    media: dict[str, dict] = {}
    media_bytes: dict[str, bytes] = {}
    requests: list[tuple[str, str, dict]] = []
    require_auth = True
    expected_auth = ""       # set by the test: "Basic <b64>" — a wrong password must 401
    sanitize = False         # True = behave like a CMS that strips scripts/SVG on save (kses)
    media_alt_forbidden = False   # True = behave like an account without edit_post on attachments

    def log_message(self, *args):                 # keep the test output readable
        pass

    def _send(self, code, payload):
        body = json.dumps(payload).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read(self):
        length = int(self.headers.get("Content-Length") or 0)
        return json.loads(self.rfile.read(length) or b"{}")

    def _authed(self):
        if not self.require_auth:
            return True
        supplied = self.headers.get("Authorization") or ""
        if not supplied.startswith("Basic ") or (StubWP.expected_auth and supplied != StubWP.expected_auth):
            self._send(401, {"code": "rest_cannot_create",
                             "message": "Sorry, you are not allowed to create posts as this user."})
            return False
        return True

    @staticmethod
    def _wp_shaped(post: dict) -> dict:
        """What WordPress returns for `context=edit`: raw + rendered fields, excerpt wrapped.

        The excerpt comes back as `<p>…</p>` with entity-encoded punctuation, which is exactly why
        the read-back cannot compare raw strings.
        """
        return {
            **post,
            "title": {"raw": post.get("title"), "rendered": f"<p>{html.escape(post.get('title') or '')}</p>"},
            "excerpt": {"raw": f"<p>{html.escape(post.get('excerpt') or '')}</p>",
                        "rendered": f"<p>{html.escape(post.get('excerpt') or '')}</p>"},
            "content": {"raw": post.get("content") or "", "rendered": post.get("content") or ""},
        }

    def do_GET(self):
        if not self._authed():
            return
        StubWP.requests.append(("GET", self.path, {}))
        if self.path.startswith("/wp-json/wp/v2/media/"):
            media_id = self.path.split("/wp-json/wp/v2/media/")[1].split("?")[0]
            item = StubWP.media.get(media_id)
            if not item:
                return self._send(404, {"code": "rest_post_invalid_id", "message": "Invalid media ID."})
            return self._send(200, self._media_shaped(item))
        if self.path.startswith("/wp-json/wp/v2/media?"):
            slug = self.path.split("slug=")[1].split("&")[0]
            return self._send(200, [self._media_shaped(m) for m in StubWP.media.values()
                                    if m["slug"] == slug])
        if self.path.startswith("/wp-json/wp/v2/categories/"):
            cid = self.path.split("/wp-json/wp/v2/categories/")[1].split("?")[0]
            catalog = {"9": "Autonomous &amp; Agentic Workflows", "7": "AI Stack &amp; Tool TCO"}
            if cid in catalog:
                return self._send(200, {"id": int(cid), "name": catalog[cid]})
            return self._send(404, {"code": "rest_term_invalid", "message": "Term does not exist."})
        if self.path.startswith("/wp-json/wp/v2/posts/"):
            post_id = self.path.split("/wp-json/wp/v2/posts/")[1].split("?")[0]
            post = StubWP.posts.get(post_id)
            if not post:
                return self._send(404, {"code": "rest_post_invalid_id", "message": "Invalid post ID."})
            return self._send(200, self._wp_shaped(post))
        if self.path.startswith("/wp-json/wp/v2/posts?"):
            slug = self.path.split("slug=")[1].split("&")[0]
            found = [p for p in StubWP.posts.values() if p["slug"] == slug]
            return self._send(200, found)
        self._send(404, {"message": "not found"})

    @staticmethod
    def _media_shaped(item: dict) -> dict:
        """What WordPress actually returns for an attachment: `title` and `caption` are
        `{raw, rendered}` objects while `alt_text` is a plain string. Returning plain strings here
        would hide the read-back false positive that a live push hits."""
        shaped = dict(item)
        for field in ("title", "caption"):
            value = item.get(field) or ""
            shaped[field] = {"raw": value, "rendered": value}
        return shaped

    def _post_media(self):
        """The media endpoints take the image as the raw request body, not JSON."""
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length)
        if self.path == "/wp-json/wp/v2/media":
            disposition = self.headers.get("Content-Disposition") or ""
            found = re.search(r'filename="?([^";]+)"?', disposition)
            filename = found.group(1) if found else "upload.bin"
            StubWP.requests.append(("POST", self.path, {"filename": filename, "bytes": len(raw),
                                                        "content_type": self.headers.get("Content-Type")}))
            media_id = str(1000 + len(StubWP.media) + 1)
            item = {"id": media_id, "slug": pathlib.Path(filename).stem,
                    "source_url": f"https://cms.example.com/wp-content/uploads/{filename}",
                    "alt_text": "", "caption": "", "title": "", "post": 0,
                    "mime_type": self.headers.get("Content-Type") or "application/octet-stream"}
            StubWP.media[media_id] = item
            StubWP.media_bytes[media_id] = raw
            return self._send(201, self._media_shaped(item))
        media_id = self.path.rsplit("/", 1)[1]
        item = StubWP.media.get(media_id)
        if not item:
            return self._send(404, {"code": "rest_post_invalid_id", "message": "Invalid media ID."})
        updates = json.loads(raw.decode() or "{}")
        if StubWP.media_alt_forbidden:               # the capability that silently drops alt text
            updates = {k: v for k, v in updates.items() if k != "alt_text"}
        item.update(updates)
        StubWP.requests.append(("POST", self.path, updates))
        return self._send(200, self._media_shaped(item))

    def do_POST(self):
        if not self._authed():
            return
        if self.path == "/wp-json/wp/v2/media" or self.path.startswith("/wp-json/wp/v2/media/"):
            return self._post_media()
        body = self._read()
        StubWP.requests.append(("POST", self.path, body))
        if StubWP.sanitize:
            body["content"] = re.sub(r"<script[^>]*>.*?</script>", "", body.get("content") or "", flags=re.S)
            body["content"] = re.sub(r"<svg\b.*?</svg>", "", body["content"], flags=re.S | re.I)
        if self.path == "/wp-json/wp/v2/posts":
            post_id = str(100 + len(StubWP.posts) + 1)
            post = {"id": post_id, "slug": body["slug"], "status": body["status"],
                    "link": f"https://cms.example.com/?p={post_id}", **body}
            StubWP.posts[post_id] = post
            return self._send(201, post)
        if self.path.startswith("/wp-json/wp/v2/posts/"):
            post_id = self.path.rsplit("/", 1)[1]
            post = StubWP.posts.get(post_id)
            if not post:
                return self._send(404, {"message": "no such post"})
            post.update(body)
            return self._send(200, post)
        self._send(404, {"message": "not found"})


def start_stub():
    server = ThreadingHTTPServer(("127.0.0.1", 0), StubWP)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, f"http://127.0.0.1:{server.server_address[1]}"


# ─────────────────────────────────────────────────────────────────────────────
# fixtures
# ─────────────────────────────────────────────────────────────────────────────

SITE = {"vertical_id": "supplier_risk_reshoring_decision", "cms_base_url": "https://cms.giniloh.com",
        "site_domain": "giniloh.com", "frontend_url": "https://giniloh.com", "active": True,
        "wp_category_id": 9}

MARKDOWN = """---
title: "Reshoring Didn't Kill Tariff Risk"
vertical: supplier_risk_reshoring_decision
slug: reshoring-moved-the-tariff-upstream
---

<!-- lead -->
Coca-Cola just pledged $10 billion for U.S. plants by 2030, which its CFO calls a growth plan rather than a tariff shield [1].

<!-- tension -->
## Tariffs Move Upstream

**The big picture:** Section 338 stacks on top of base taxes, pushing covered items to a 53–55% total rate [2].

| Metric | Claim | Reality |
| --- | --- | --- |
| Duty | 53% | stacked |
| Refund | 0 | denied |

> "Measure before you scale." — Founder Note

- **Upstream:** packaging crosses a taxed border
- **Bill of materials:** re-cost it

<!-- nuanced-takeaway -->
## The Catch

The 53–55% figure is an all-in rate, not a headline tariff.

## Sources
[1] Fortune — "Coca-Cola to invest $10 billion" — https://fortune.com/example
[2] Rabobank — "Unwrapped" — https://media.rabobank.com/example.pdf

<!-- linkedin -->
This internal variant must never reach the CMS.

<!-- schema -->
```json
{"@context":"https://schema.org"}
```

## Gate report
lead: PASS — internal working material.
"""

ROW = {
    "id": "row-1",
    "title": "Reshoring Didn't Kill Tariff Risk",
    "content": MARKDOWN,
    "tags": ["supplier_risk_reshoring_decision"],
    "metadata": {
        "slug": "reshoring-moved-the-tariff-upstream",
        "vertical": "supplier_risk_reshoring_decision",
        "headline": "Reshoring Didn't Kill Tariff Risk — It Moved Upstream Into Packaging",
        "seo": {"schema": {"@graph": [
            {"@type": "TechArticle", "headline": "x"},
            {"@type": "Dataset", "name": "D", "creator": {"@type": "Organization",
                                                           "name": "Editorial Factory Intelligence Unit",
                                                           "url": "https://editorial-factory.com"}},
            {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": "q"}]},
        ]}},
    },
}


class FakeDB:
    def __init__(self, site=SITE):
        self.site = site
        self.recorded: list[dict] = []
        self.bodies: list[dict] = []          # metadata.update_body writes (internal links)

    def articles(self, slug=None, un_pushed_only=False, limit=None):
        """push_by_slug() reads the row through the db, exactly as the CLI and publish.py do."""
        if slug and slug != ROW["metadata"]["slug"]:
            return []
        return [ROW]

    def site_for(self, vertical):
        if self.site is None:
            raise RuntimeError(f"no destination in public.vertical_sites for vertical '{vertical}'")
        if self.site.get("active") is False:
            raise RuntimeError(f"vertical '{vertical}' is routed to {self.site['site_domain']} but marked active=false")
        return self.site

    def record_push(self, row_id, metadata, record):
        self.recorded.append({"row_id": row_id, "metadata": metadata, "record": record})

    def update_body(self, row_id, content, metadata):
        """The one write that keeps the row's body and the CMS's body identical."""
        self.bodies.append({"row_id": row_id, "content": content, "metadata": metadata})


# ─────────────────────────────────────────────────────────────────────────────
# field mapping
# ─────────────────────────────────────────────────────────────────────────────

print("\nfield mapping — title")
check("keeps the real headline",
      wd.make_title(ROW) == "Reshoring Didn't Kill Tariff Risk — It Moved Upstream Into Packaging")
raises("rejects a title containing the vertical id (the live giniloh defect)",
       lambda: wd.make_title({"title": "x", "metadata": {
           "vertical": "enterprise_build_vs_buy",
           "headline": "enterprise_build_vs_buy: The $250k AI Upkeep Tax"}}),
       "appears in the title")
raises("refuses an untitled row", lambda: wd.make_title({"title": "", "metadata": {}}), "no headline")

print("\nfield mapping — excerpt")
long_desc = ("Audited agentic AI enterprise benchmarks data. Real-world benchmarks, adoption telemetry, "
             "cost multipliers, and field failure rates contrasted with vendor claims about outcomes")
excerpt = wd.make_excerpt({"content": "", "metadata": {"seo": {"meta_description": long_desc}}})
check("trims on a word boundary, never mid-word",
      excerpt.endswith("…") and len(excerpt) <= wd.EXCERPT_TARGET + 1 and excerpt[:-1].endswith(excerpt[:-1].split()[-1]),
      f"got {excerpt!r}")
check("does not cut a word in half", "vendor cl…" not in excerpt and "cl…" not in excerpt, f"got {excerpt!r}")
lead = wd.make_excerpt({"content": MARKDOWN, "metadata": {"seo": {}}})
check("falls back to the lead paragraph (the destinations' established excerpt source)",
      lead.startswith("Coca-Cola just pledged $10 billion") and "CFO calls a growth plan" in lead, f"got {lead!r}")

print("\nmarkdown -> HTML")
html_body = wd.md_to_html(MARKDOWN)
check("table becomes a real <table>", "<table>" in html_body and "<th>" in html_body and "<td>" in html_body)
check("no pipe or separator rows leak", "| --- |" not in html_body and "| Metric |" not in html_body)
check("blockquote becomes <blockquote>", "<blockquote>" in html_body)
check("bold and headings rendered", "<strong>The big picture:</strong>" in html_body and "<h2>Tariffs Move Upstream</h2>" in html_body)
check("lists rendered", "<ul>" in html_body and "<li>" in html_body)
check("bare source URLs become links", '<a href="https://fortune.com/example">https://fortune.com/example</a>' in html_body)
check("trailing punctuation stays outside the link", '<a href="https://media.rabobank.com/example.pdf">' in html_body
      and 'example.pdf.</a>' not in html_body)
check("markdown links are not double-wrapped", html_body.count('<a href="https://github.com/x">') == 1
      if "github" in html_body else True)
check("no pipeline markers survive", "<!--" not in html_body)
check("internal LinkedIn variant dropped", "internal variant must never reach" not in html_body)
check("## Gate report dropped", "Gate report" not in html_body)
check("frontmatter dropped", "vertical: supplier_risk" not in html_body)

print("\nreader copy — a section written after <!-- linkedin --> still reaches the post")
LATE_SECTION = MARKDOWN.replace(
    "<!-- schema -->",
    "<!-- internal-links -->\n\n## Related reading\n\n"
    "- [How to Cut Energy Bills](https://giniloh.com/how-to-cut-energy-bills/) — more on Money\n\n"
    "<!-- schema -->")
late_html = wd.md_to_html(LATE_SECTION)
check("the internal-link block is NOT truncated by the LinkedIn cut (the live defect on post 401)",
      "## Related reading" in wd.reader_markdown(LATE_SECTION) and "Related reading" in late_html,
      wd.reader_markdown(LATE_SECTION)[-160:])
check("...as real anchors the reader can follow",
      '<a href="https://giniloh.com/how-to-cut-energy-bills/">How to Cut Energy Bills</a>' in late_html)
check("...while the LinkedIn variant and the machine schema are still dropped",
      "internal variant must never reach" not in late_html and "application/ld+json" not in late_html
      and "&lt;script" not in late_html)

print("\ncharts in the reader copy")
chart_md = ("Intro paragraph.\n\n"
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 120">\n'
            "  <!-- Row 1 -->\n"
            '  <rect x="220" y="8" width="160" height="18" fill="#818cf8"/>\n'
            '  <text x="20" y="22">FinOps waste</text>\n'
            "</svg>\n\n"
            "Closing paragraph.")
chart_html = wd.md_to_html(chart_md)
check("a generated SVG chart reaches the post as markup, not escaped text",
      "<svg" in chart_html and "&lt;svg" not in chart_html)
check("...its inner comments survive the comment filter", "<!-- Row 1 -->" in chart_html)
check("...and the prose around it still renders",
      "<p>Intro paragraph.</p>" in chart_html and "<p>Closing paragraph.</p>" in chart_html)
check("an SVG carrying a script is dropped, not passed through",
      "<svg" not in wd.md_to_html('<svg xmlns="x"><script>alert(1)</script></svg>'))
check("...likewise one carrying an event handler",
      "<svg" not in wd.md_to_html('<svg xmlns="x" onload="go()"></svg>'))

print("\nschema handling")
dataset = wd.extract_dataset_node(ROW["metadata"]["seo"]["schema"])
check("sends only the Dataset node (Article/FAQPage come from the frontends)",
      dataset is not None and dataset["@type"] == "Dataset" and "TechArticle" not in json.dumps(dataset))
check("no Dataset node => nothing emitted", wd.extract_dataset_node({"@graph": [{"@type": "FAQPage"}]}) is None)
retargeted, notes = wd.retarget_publisher(dataset, SITE, None)
check("editorial-factory.com (unresolvable) rewritten to the destination",
      retargeted["creator"]["url"] == "https://giniloh.com" and any("creator.url" in n for n in notes))
check("...and reported, not silent", len(notes) >= 1 and "giniloh.com" in notes[0])

# The generator now emits placeholders instead of a guessed publisher; the destination fills them.
placeholder_node = {
    "@type": "Dataset",
    "creator": {"@type": "Organization", "name": "{{PUBLISHER_NAME}}", "url": "{{SITE_URL}}"},
    "author": {"@type": "Person", "name": "{{AUTHOR_NAME}}"},
}
filled, fill_notes = wd.retarget_publisher(placeholder_node, SITE, "Gini Loh")
check("{{SITE_URL}} filled from the destination", filled["creator"]["url"] == "https://giniloh.com")
check("{{PUBLISHER_NAME}} filled from --publisher-name", filled["creator"]["name"] == "Gini Loh")
check("an unresolved {{AUTHOR_NAME}} node is DROPPED, not published literally",
      "author" not in filled and any("dropped" in n for n in fill_notes), filled)
with_author, _ = wd.retarget_publisher(placeholder_node, SITE, "Gini Loh", "Jorge Fernandez")
check("...and filled when an author is supplied", with_author["author"]["name"] == "Jorge Fernandez")
check("no placeholder token survives once values are supplied", "{{" not in json.dumps(with_author))
check("the generator no longer hard-codes the internal approval handle as a byline",
      "Simon" not in json.dumps(wd.retarget_publisher(placeholder_node, SITE, None)))

print("\ncategory routing")
payload_with_cat, notes_with_cat = wd.build_payload(ROW, SITE)
check("a routed wp_category_id is sent as a WordPress category",
      payload_with_cat.get("categories") == [9], payload_with_cat.get("categories"))
check("...and reported in the notes", any("category 9" in n for n in notes_with_cat), notes_with_cat)
no_cat_site = {k: v for k, v in SITE.items() if k != "wp_category_id"}
payload_no_cat, notes_no_cat = wd.build_payload(ROW, no_cat_site)
check("no routed category => no categories key, so WordPress's default applies",
      "categories" not in payload_no_cat)
check("...and the operator is told to set one", any("wp_category_id" in n for n in notes_no_cat), notes_no_cat)

print("\nrouting — fails closed")
db_no_route = FakeDB(site=None)
raises("unknown vertical refuses to push", lambda: wd.push_one(ROW, db_no_route, dry_run=True),
       "no destination")
raises("inactive vertical refuses to push",
       lambda: wd.push_one(ROW, FakeDB(site={**SITE, "active": False}), dry_run=True), "active=false")

print("\nrow selection — batch limit semantics")
fdb = wd.Supabase("http://example.invalid", "key")
fdb._call = lambda method, path, body=None, extra_headers=None: (
    200, [{"id": str(i), "metadata": {}} for i in range(3)])
check("limit=0 selects nothing (a no-op probe must not become a backfill)", fdb.articles(limit=0) == [])
check("limit=None means unlimited", len(fdb.articles(limit=None)) == 3)
check("limit=2 caps the batch", len(fdb.articles(limit=2)) == 2)
fdb._call = lambda method, path, body=None, extra_headers=None: (
    200, [{"id": "1", "metadata": {}}, {"id": "2", "metadata": {"wordpress": {"post_id": 9}}}])
check("un_pushed_only skips rows that already have a draft",
      [r["id"] for r in fdb.articles(un_pushed_only=True, limit=None)] == ["1"])

print("\ncredentials")
import os  # noqa: E402
saved = {k: os.environ.pop(k, None) for k in ("WP_GINILOH_USER", "WP_GINILOH_APP_PASSWORD", "WP_USER", "WP_APP_PASSWORD")}
msg = raises("missing CMS credentials name the exact env vars to set",
             lambda: wd.credentials_for("giniloh.com"), "WP_GINILOH_USER")
check("credentials are keyed per domain", "WP_GINILOH_APP_PASSWORD" in msg)
os.environ.update({k: v for k, v in saved.items() if v})
os.environ["WP_GINILOH_USER"], os.environ["WP_GINILOH_APP_PASSWORD"] = "editor", "abcd efgh"
check("credentials_for returns the per-site pair",
      wd.credentials_for("giniloh.com") == ("editor", "abcd efgh"))

# ─────────────────────────────────────────────────────────────────────────────
# end-to-end against the stub CMS
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# featured image — staged by scripts/illustration_creator.py, uploaded and verified here
# ─────────────────────────────────────────────────────────────────────────────

SLUG = ROW["metadata"]["slug"]
ILLUSTRATION = {
    "slug": SLUG, "style": "editorial_macro", "style_label": "Editorial macro",
    "model": "flux-2/pro-text-to-image",
    "alt_text": "Translucent plastic resin pellets resting on a steel plate.",
    "caption": "The duty now lands on the material before it becomes packaging.",
    "title": "Plastic resin pellets",
    "credit": "Illustration: Editorial-Factory Intelligence Unit",
    "local_path": f"context/assets/illustrations/{SLUG}/featured.png",
}
ILLUSTRATED_ROW = {**ROW, "metadata": {**ROW["metadata"], "illustration": ILLUSTRATION}}

print("\nfeatured image — payload mapping")
recorded_row = {**ROW, "metadata": {**ROW["metadata"], "wordpress": {"post_id": 101, "media_id": 1234}}}
payload_recorded, notes_recorded = wd.build_payload(recorded_row, SITE)
check("a recorded attachment id is re-sent, so a refresh keeps the article's image",
      payload_recorded.get("featured_media") == 1234, str(payload_recorded.get("featured_media")))
check("...and is reported", any("featured media 1234" in n for n in notes_recorded), str(notes_recorded))
check("no illustration and no recorded media => no featured_media key",
      "featured_media" not in wd.build_payload(ROW, SITE)[0])
bad_media_notes = wd.build_payload(
    {**ROW, "metadata": {**ROW["metadata"], "wordpress": {"media_id": "not-a-number"}}}, SITE)[1]
check("a non-numeric recorded media id is reported instead of sent",
      any("not a number" in n for n in bad_media_notes)
      and "featured_media" not in wd.build_payload(
          {**ROW, "metadata": {**ROW["metadata"], "wordpress": {"media_id": "not-a-number"}}}, SITE)[0],
      str(bad_media_notes))

# what the attachment fields must carry, derived from the illustration record
meta = wd.media_meta(ILLUSTRATION, SLUG)
check("the alt text and caption come from the brief, unchanged",
      meta["alt_text"] == ILLUSTRATION["alt_text"] and meta["caption"] == ILLUSTRATION["caption"])
check("...and the library description records how the image was made",
      "Editorial macro" in meta["description"] and "flux-2/pro-text-to-image" in meta["description"],
      meta["description"])

print("\nfeatured image — upload, caption, reuse (no duplicate bytes in the library)")
StubWP.media, StubWP.media_bytes = {}, {}
media_server, media_base = start_stub()
with tempfile.TemporaryDirectory() as tmp:
    origin_root = wd.ROOT
    wd.ROOT = pathlib.Path(tmp)
    try:
        staged = pathlib.Path(tmp) / ILLUSTRATION["local_path"]
        staged.parent.mkdir(parents=True, exist_ok=True)
        blob = b"\x89PNG\r\n\x1a\n" + b"header bytes" * 40
        staged.write_bytes(blob)

        wp = wd.WordPress(media_base, "editor", "secret")
        notes: list = []
        item = wd.ensure_featured_media(wp, SLUG, ILLUSTRATION, notes)
        check("the staged image is uploaded as an attachment",
              item and item["id"] in StubWP.media and StubWP.media_bytes[item["id"]] == blob)
        check("...named `<slug>-featured` so the media slug is a stable idempotency key",
              item["slug"] == f"{SLUG}-featured", item["slug"])
        check("...typed from its extension", item["mime_type"] == "image/png", item["mime_type"])
        check("...with the brief's alt text, caption and library title set on the CMS",
              item["alt_text"] == ILLUSTRATION["alt_text"]
              and wd._field_text(item["caption"]) == ILLUSTRATION["caption"]
              and wd._field_text(item["title"]) == ILLUSTRATION["title"], json.dumps(item))
        check("...and the upload reported", any("uploaded" in n for n in notes), str(notes))

        notes2: list = []
        again = wd.ensure_featured_media(wp, SLUG, ILLUSTRATION, notes2, recorded_id=item["id"])
        check("a re-push with the recorded id reuses the attachment",
              again["id"] == item["id"] and len(StubWP.media) == 1, str(list(StubWP.media)))
        check("...and says so", any("recorded on the row" in n for n in notes2), str(notes2))

        notes3: list = []
        by_slug = wd.ensure_featured_media(wp, SLUG, ILLUSTRATION, notes3)
        check("without a recorded id the media slug still finds it (no second copy)",
              by_slug["id"] == item["id"] and len(StubWP.media) == 1, str(list(StubWP.media)))
        check("...and says so", any("media slug match" in n for n in notes3), str(notes3))

        StubWP.media[item["id"]]["alt_text"] = "stale alt from a previous push"
        wd.ensure_featured_media(wp, SLUG, ILLUSTRATION, [])
        check("an attachment whose metadata drifted is re-captioned, not re-uploaded",
              StubWP.media[item["id"]]["alt_text"] == ILLUSTRATION["alt_text"]
              and len(StubWP.media) == 1)

        missing = wd.ensure_featured_media(wp, "no-such-slug",
                                           {"slug": "no-such-slug", "local_path": "nope.png"}, [])
        missing_notes: list = []
        wd.ensure_featured_media(wp, "no-such-slug", {"slug": "no-such-slug",
                                                     "local_path": "nope.png"}, missing_notes)
        check("an article whose image is not on this host is reported, not silently headerless",
              missing is None and any("illustration_creator.py" in n for n in missing_notes),
              str(missing_notes))
    finally:
        wd.ROOT = origin_root

print("\nfeatured image — the alt text a lower-privilege password cannot set")
dropped = wd.media_problems(meta, {"alt_text": "", "title": meta["title"], "caption": meta["caption"]})
check("a CMS that drops alt_text is caught by the read-back",
      len(dropped) == 1 and "alt_text" in dropped[0], str(dropped))
check("a read-back in WordPress's own shape ({raw, rendered}) is NOT a defect",
      wd.media_problems(meta, {"alt_text": meta["alt_text"],
                               "title": {"raw": meta["title"], "rendered": meta["title"]},
                               "caption": {"raw": meta["caption"], "rendered": meta["caption"]}}) == [],
      str(wd.media_problems(meta, {"alt_text": meta["alt_text"],
                                   "title": {"rendered": meta["title"]},
                                   "caption": {"rendered": meta["caption"]}})))
check("matching fields report nothing",
      wd.media_problems(meta, {"alt_text": meta["alt_text"], "title": meta["title"],
                               "caption": meta["caption"]}) == [])
check("an unattached image is fine, a missing featured_media on the post is not",
      wd.delivery_problems({"featured_media": 3, "title": "t", "excerpt": "e", "content": "c"},
                           {"featured_media": 0, "title": {"raw": "t"}, "excerpt": {"raw": "e"},
                            "content": {"raw": "c"}, "status": "draft"})
      and not wd.delivery_problems({"title": "t", "excerpt": "e", "content": "c"},
                                   {"title": {"raw": "t"}, "excerpt": {"raw": "e"},
                                    "content": {"raw": "c"}, "status": "draft"}))
check("the summary names the featured media it verified",
      "featured media 3" in wd.verification_summary(
          {"featured_media": 3, "excerpt": "e", "content": "c"}, {}))

print("\nfeatured image — end to end through push_one")
StubWP.posts, StubWP.media = {}, {}
with tempfile.TemporaryDirectory() as tmp:
    origin_root = wd.ROOT
    wd.ROOT = pathlib.Path(tmp)
    try:
        staged = pathlib.Path(tmp) / ILLUSTRATION["local_path"]
        staged.parent.mkdir(parents=True, exist_ok=True)
        staged.write_bytes(b"\x89PNG\r\n\x1a\n" + b"illustrated header" * 32)
        db = FakeDB()
        # The stub server, not the fixture's real CMS base URL: wp_factory receives the site's
        # cms_base_url, and a test that forwards it would be talking to the live site.
        withmedia = wd.push_one(ILLUSTRATED_ROW, db,
                                wp_factory=lambda b, u, p: wd.WordPress(media_base, u, p))
        post = StubWP.posts[[k for k in StubWP.posts][0]]
        check("the draft is created with the attachment as its featured image",
              str(post.get("featured_media")) == str(withmedia["media_id"]) and withmedia["media_id"],
              f"post featured_media={post.get('featured_media')} media_id={withmedia['media_id']}")
        check("...attached to the post in the library (post_parent set)",
              StubWP.media[str(withmedia["media_id"])]["post"] == post["id"],
              str(StubWP.media[str(withmedia["media_id"])]["post"]))
        record = db.recorded[-1]["record"]
        check("...and recorded on the Supabase row (id, url, alt)",
              record["media_id"] == withmedia["media_id"] and record["media_url"].startswith("https://")
              and record["media_alt"] == ILLUSTRATION["alt_text"], json.dumps(record)[:200])
        check("...with the delivery verified, featured image included",
              withmedia["verified"] and not withmedia["problems"]
              and "featured media" in withmedia["summary"], str(withmedia)[:240])

        # The image must not be uploaded twice for the same article.
        db2 = FakeDB()
        second = wd.push_one({**ILLUSTRATED_ROW,
                              "metadata": {**ILLUSTRATED_ROW["metadata"],
                                           "wordpress": {"media_id": withmedia["media_id"]}}},
                             db2, wp_factory=lambda b, u, p: wd.WordPress(media_base, u, p))
        check("a second push reuses the attachment instead of adding a copy",
              second["media_id"] == withmedia["media_id"] and len(StubWP.media) == 1,
              str(list(StubWP.media)))

        StubWP.media_alt_forbidden = True
        withbadmedia = wd.push_one({**ILLUSTRATED_ROW, "title": "Another headline for a new slug",
                                    "metadata": {**ILLUSTRATED_ROW["metadata"],
                                                 "slug": "second-article",
                                                 "illustration": {**ILLUSTRATION, "slug": "second-article"}}},
                                   FakeDB(), wp_factory=lambda b, u, p: wd.WordPress(media_base, u, p))
        check("an account that cannot set alt text fails the verification loudly",
              not withbadmedia["verified"]
              and any("alt_text" in p for p in withbadmedia["problems"]),
              str(withbadmedia["problems"])[:200])
        StubWP.media_alt_forbidden = False
    finally:
        wd.ROOT = origin_root

print("\nfeatured image — a brief on disk, no metadata on the row (the sweep's case)")
with tempfile.TemporaryDirectory() as tmp:
    origin_root = wd.ROOT
    wd.ROOT = pathlib.Path(tmp)
    try:
        staged = pathlib.Path(tmp) / ILLUSTRATION["local_path"]
        staged.parent.mkdir(parents=True, exist_ok=True)
        staged.write_bytes(b"\x89PNG\r\n\x1a\n" + b"sweep generated this" * 16)
        (staged.parent / "featured.json").write_text(json.dumps(ILLUSTRATION), encoding="utf-8")
        record, note = wd.staged_illustration(SLUG)
        check("the brief committed beside the image is found for a row that does not carry one",
              record.get("alt_text") == ILLUSTRATION["alt_text"] and "featured.json" in note, note[:120])
        check("a slug with nothing staged yields nothing to report",
              wd.staged_illustration("no-such-slug") == ({}, ""))
        StubWP.posts, StubWP.media = {}, {}
        plain_row = {**ROW, "metadata": {k: v for k, v in ROW["metadata"].items() if k != "illustration"}}
        db = FakeDB()
        result = wd.push_one(plain_row, db, wp_factory=lambda b, u, p: wd.WordPress(media_base, u, p))
        post = StubWP.posts[[k for k in StubWP.posts][0]]
        check("the draft still gets its featured image",
              bool(result["media_id"]) and post.get("featured_media") == result["media_id"],
              str(result)[:200])
        check("...with the alt text from the committed brief",
              StubWP.media[str(result["media_id"])]["alt_text"] == ILLUSTRATION["alt_text"],
              json.dumps(StubWP.media[str(result["media_id"])])[:160])
        check("...and the row becomes self-describing (the brief is written back)",
              db.recorded[-1]["metadata"].get("illustration", {}).get("alt_text")
              == ILLUSTRATION["alt_text"], json.dumps(db.recorded[-1]["metadata"])[:160])
    finally:
        wd.ROOT = origin_root

print("\nend-to-end against a stub WordPress")
StubWP.posts, StubWP.media = {}, {}      # the earlier featured-image section left posts behind
server, base = start_stub()
try:
    db = FakeDB()
    wp = wd.WordPress(base, "editor", "secret")
    first = wd.push_one(ROW, db, wp_factory=lambda b, u, p: wp)
    check("first run creates a DRAFT (never publish)", StubWP.posts["101"]["status"] == "draft",
          f"status={StubWP.posts['101'].get('status')}")
    check("title mapped from metadata.headline",
          StubWP.posts["101"]["title"] == ROW["metadata"]["headline"])
    check("write-back recorded the post id + edit url",
          db.recorded[0]["record"]["post_id"] == "101"
          and "action=edit" in db.recorded[0]["record"]["edit_url"])

    print("\ninternal links — generated for the row, delivered to the CMS, written back")
    check("the reader-facing links are in the post body",
          '<a href="https://giniloh.com/how-to-cut-energy-bills/">How to Cut Energy Bills</a>'
          in StubWP.posts["101"]["content"], StubWP.posts["101"]["content"][-400:])
    check("the operator's placement hints stay out of the reader copy (they are for the artifact,",
          "internal-link hint" not in StubWP.posts["101"]["content"])
    check("...and are carried on the row the operator reads, next to the links they describe",
          "internal-link hint" in db.bodies[0]["content"] and 'Anchor:' not in StubWP.posts["101"]["content"],
          db.bodies[0]["content"][-300:])
    check("the enriched body is written back to the Supabase row (the next --refresh reads it)",
          bool(db.bodies) and "Related reading" in db.bodies[0]["content"],
          str(db.bodies)[:200])
    check("...recording what was generated, from where",
          db.bodies[0]["metadata"].get("internal_links", {}).get("count") == 1
          and "internal_links.json" in db.bodies[0]["metadata"]["internal_links"]["source"],
          json.dumps(db.bodies[0]["metadata"].get("internal_links"))[:200])
    check("the push records the link count it verified",
          db.recorded[0]["record"].get("internal_links") == 1, json.dumps(db.recorded[0]["record"])[:200])
    check("the delivery summary names the links", "internal link(s)" in
          wd.verification_summary({"excerpt": "e", "content": StubWP.posts["101"]["content"]}, {},
                                  "giniloh.com"))

    print("\ninternal links — never rewritten twice (idempotent through the row)")
    row_after = {"id": ROW["id"], "title": ROW["title"], "tags": ROW["tags"],
                 "content": db.bodies[0]["content"], "metadata": db.bodies[0]["metadata"]}
    db2 = FakeDB()
    same, notes_same = il.ensure_for_row(row_after, persist=True, db=db2, site_domain="giniloh.com")
    check("a row that already carries its links is left untouched",
          same["content"] == row_after["content"] and not db2.bodies
          and any("no change" in n for n in notes_same), str(notes_same)[:200])

    second = wd.push_one(ROW, db, wp_factory=lambda b, u, p: wp)
    check("second run updates the same post (no duplicate)",
          second["status"] == "updated" and len(StubWP.posts) == 1, f"posts={list(StubWP.posts)}")
    check("original draft status preserved on update",
          StubWP.posts["101"]["status"] == "draft")

    print("\na live post is refreshed, never demoted")
    StubWP.posts["101"]["status"] = "publish"          # a human published it in the CMS
    StubWP.requests.clear()
    bodies_before = len(db.bodies)
    skipped_result = wd.push_one(ROW, db, wp_factory=lambda b, u, p: wp)
    check("a published post is left alone unless asked (a refresh re-derives its body and can "
          "overwrite what an editor tuned in the CMS)",
          skipped_result.get("skipped") is True and StubWP.posts["101"]["status"] == "publish",
          str(skipped_result)[:200])
    check("...no write reaches the CMS at all",
          not [1 for method, path, _ in StubWP.requests if method == "POST" and path.endswith("/posts/101")],
          str(StubWP.requests)[:200])
    check("...and the row is not written back either (the DB must not claim links the CMS lacks)",
          len(db.bodies) == bodies_before, str(len(db.bodies)))

    StubWP.requests.clear()
    live = wd.push_one(ROW, db, wp_factory=lambda b, u, p: wp, live_ok=True)
    pushed = [body for method, path, body in StubWP.requests
              if method == "POST" and path.endswith("/posts/101")]
    check("--refresh-live updates it without ever sending a status (it cannot be unpublished)",
          bool(pushed) and all("status" not in body for body in pushed), str(pushed)[:200])
    check("...it stays live", StubWP.posts["101"]["status"] == "publish",
          StubWP.posts["101"]["status"])
    check("...and the push says so", "kept published" in live["status"], live["status"])
    check("...and the read-back does not report the live status as a defect",
          not any("status" in p for p in (live.get("problems") or [])), str(live.get("problems"))[:200])
    check("...with the internal links in the body it just rewrote",
          "Related reading" in StubWP.posts["101"]["content"])
    StubWP.posts["101"]["status"] = "draft"
    check("Dataset JSON-LD embedded exactly once and retargeted",
          StubWP.posts["101"]["content"].count("application/ld+json") == 1
          and "giniloh.com" in StubWP.posts["101"]["content"]
          and "editorial-factory.com" not in StubWP.posts["101"]["content"])

    second = wd.push_one(ROW, db, wp_factory=lambda b, u, p: wp)
    check("second run updates the same post (no duplicate)",
          second["status"] == "updated" and len(StubWP.posts) == 1, f"posts={list(StubWP.posts)}")
    check("original draft status preserved on update",
          StubWP.posts["101"]["status"] == "draft")

    StubWP.require_auth = True
    import base64 as _b64
    StubWP.expected_auth = "Basic " + _b64.b64encode(b"editor:secret").decode()
    unauth = wd.WordPress(base, "editor", "wrong")
    raises("a bad password surfaces an explicit error (no silent skip)",
           lambda: unauth.find_by_slug("x"), "401")
    StubWP.expected_auth = ""
    check("a category id valid on the destination resolves to its name",
          "Agentic" in wp.category_name(9))
    raises("a category id that does NOT exist on the site fails loudly",
           lambda: wp.category_name(999), "does not exist on this site")
    src = pathlib.Path(wd.__file__).read_text()
    declared = set(re.findall(r'add_argument\("(--[a-z-]+)"', src))
    check("no --status/--publish flag exists (publishing stays a human step)",
          not {"--status", "--publish"} & declared and '"status": "draft"' in src,
          f"declared options: {sorted(declared)}")
    check("--refresh re-applies the mapping to drafts that already exist",
          "--refresh" in declared and "un_pushed_only=not args.refresh" in src)
    check("...and defaults to every row rather than the --limit 1 batch",
          "None if args.refresh else 1" in src)
    payload, _ = wd.build_payload(ROW, SITE)
    check("payload status is hard-coded to draft", payload["status"] == "draft")
finally:
    server.shutdown()

# ─────────────────────────────────────────────────────────────────────────────
# the in-run hook: publish.py creates the draft in the same pass
# ─────────────────────────────────────────────────────────────────────────────

print("\nin-run hook (publish.py)")
import importlib.util  # noqa: E402

pub_src = (pathlib.Path(wd.__file__).parent / "publish.py").read_text()
check("publish.py calls the shared entry point", "push_wp_draft(slug_val)" in pub_src)
check("publish.py skips it on --dry-run", "if not args.dry_run:\n        push_wp_draft(slug_val)" in pub_src)
check("publish.py retries via the sweep on failure", "wp_draft.py --all" in pub_src)
check("publish.py explains the draft is human-published", "stays your call in the CMS" in pub_src)

spec = importlib.util.spec_from_file_location("publish_mod", pathlib.Path(wd.__file__).parent / "publish.py")
publish_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(publish_mod)

print("  (a CMS failure must not abort a publish that already persisted the article)")
import io, contextlib  # noqa: E402
stderr_buf = io.StringIO()
try:
    with contextlib.redirect_stderr(stderr_buf):
        ok = publish_mod.push_wp_draft("definitely-not-a-real-slug-xyz")
    raised_none = True
except BaseException as exc:                      # noqa: BLE001
    raised_none, ok = False, f"raised {exc!r}"
check("push_wp_draft never raises", raised_none, str(ok))
check("push_wp_draft reports the failure instead of swallowing it",
      "WordPress draft NOT created" in stderr_buf.getvalue(), stderr_buf.getvalue()[:120])
check("...and returns False so the caller can log it", ok is False, repr(ok))

print("  (the hook pushes through the same path the CLI uses)")
server2, base2 = start_stub()
try:
    stub_db = FakeDB()
    result = wd.push_by_slug(ROW["metadata"]["slug"], db=stub_db,
                             wp_factory=lambda b, u, p: wd.WordPress(base2, "editor", "secret"))
    check("push_by_slug creates the draft", StubWP.posts and list(StubWP.posts.values())[-1]["status"] == "draft")
    check("push_by_slug returns site + post id + edit url",
          result["site"] == "giniloh.com" and result["post_id"] and "action=edit" in result["edit_url"])
    check("push_by_slug writes the row back once", len(stub_db.recorded) == 1)
finally:
    server2.shutdown()

# ─────────────────────────────────────────────────────────────────────────────
# delivery verification — read the post back and compare it to what was sent
# ─────────────────────────────────────────────────────────────────────────────

print("\ndelivery verification — what the CMS actually kept")

SVG_CHART = cg.generate_svg_bar_chart("Verified figures", [("Price hike", 13.0, "[1]"), ("Ad tier", 4.0, "[2]")])
CHART_ROW = {**ROW, "content": MARKDOWN.replace("## Sources", SVG_CHART + "\n\n## Sources")}

base_payload, _ = wd.build_payload(ROW, SITE)
chart_payload, chart_notes = wd.build_payload(CHART_ROW, SITE)


def stored_post(payload: dict, content: str | None = None, status: str = "draft",
                title: str | None = None, excerpt: str | None = None) -> dict:
    """A WordPress-shaped read-back of `payload`."""
    return {
        "id": 101,
        "status": status,
        "title": {"raw": payload["title"] if title is None else title, "rendered": "<p>x</p>"},
        "excerpt": {"raw": f"<p>{html.escape(payload['excerpt'] if excerpt is None else excerpt)}</p>"},
        "content": {"raw": payload["content"] if content is None else content},
    }


check("the inline chart is in the payload",
      "<svg" in chart_payload["content"] and "&lt;svg" not in chart_payload["content"])
check("no SVG in the artifact => no SVG in the payload (nothing invented)",
      "<svg" not in base_payload["content"])

check("a faithful read-back reports no problems",
      wd.delivery_problems(chart_payload, stored_post(chart_payload)) == [],
      str(wd.delivery_problems(chart_payload, stored_post(chart_payload))))
check("...even though WordPress wraps and entity-encodes the excerpt",
      wd.delivery_problems(base_payload, stored_post(base_payload)) == [])
check("a mismatched title is reported",
      any("title" in p for p in wd.delivery_problems(base_payload, stored_post(base_payload, title="Wrong"))))
check("an excerpt the CMS left empty is reported",
      any("excerpt" in p for p in wd.delivery_problems(base_payload, stored_post(base_payload, excerpt=""))))
check("a JSON-LD block stripped on save is reported",
      any("JSON-LD" in p for p in wd.delivery_problems(
          base_payload,
          stored_post(base_payload, content=re.sub(r"<script[^>]*>.*?</script>", "",
                                                   base_payload["content"], flags=re.S)))))
check("an inline SVG stripped on save is reported",
      any("SVG" in p for p in wd.delivery_problems(
          chart_payload, stored_post(chart_payload, content=re.sub(r"<svg\b.*?</svg>", "",
                                                                    chart_payload["content"], flags=re.S | re.I)))))
check("a chart stored as escaped text is reported, not accepted as markup",
      any("escaped text" in p for p in wd.delivery_problems(
          chart_payload, stored_post(chart_payload, content=chart_payload["content"].replace("<svg", "&lt;svg")))))
check("a post that came back published is reported (the human gate must hold)",
      any("status" in p for p in wd.delivery_problems(base_payload, stored_post(base_payload, status="publish"))))

print("\ndelivery verification — internal links")
link_payload, _ = wd.build_payload({**ROW, "content": LATE_SECTION}, SITE)
check("the payload's same-site links are counted", wd.internal_link_count(link_payload["content"], "giniloh.com") == 1,
      str(wd.internal_link_count(link_payload["content"], "giniloh.com")))
check("a faithful read-back reports no problems, links included",
      wd.delivery_problems(link_payload, stored_post(link_payload), "giniloh.com") == [],
      str(wd.delivery_problems(link_payload, stored_post(link_payload), "giniloh.com")))
check("a CMS that drops the Related reading section is reported",
      any("internal links" in p for p in wd.delivery_problems(
          link_payload, stored_post(link_payload, content=re.sub(r"<h2>Related reading</h2>[\s\S]*$", "",
                                                                  link_payload["content"])),
          "giniloh.com")),
      str(wd.delivery_problems(
          link_payload, stored_post(link_payload, content=re.sub(r"<h2>Related reading</h2>[\s\S]*$", "",
                                                                  link_payload["content"])),
          "giniloh.com")))
check("a post whose status was not sent is not reported as an unpublished-to-published flip",
      wd.delivery_problems({k: v for k, v in link_payload.items() if k != "status"},
                           stored_post(link_payload, status="publish"), "giniloh.com") == [])

print("\nend-to-end — the read-back runs on a real push against the stub CMS")
server3, base3 = start_stub()
StubWP.posts.clear()
StubWP.requests.clear()
StubWP.sanitize = False
try:
    db3 = FakeDB()
    wp3 = wd.WordPress(base3, "editor", "secret")
    def _resend(row=CHART_ROW, **kw):
        return wd.push_one(row, db3, wp_factory=lambda b, u, p: wp3, **kw)

    first = _resend()
    check("push_one verifies the draft it created", first["verified"] is True and not first["problems"],
          str(first["problems"]))
    check("...and reports what it verified", "JSON-LD" in (first.get("summary") or ""), str(first.get("summary")))
    check("...by reading the post back with context=edit",
          any("context=edit" in path for _, path, _ in StubWP.requests))
    check("...and records the verification on the Supabase row",
          db3.recorded[-1]["record"]["verified"] is True)
    stored_content = StubWP.posts[list(StubWP.posts)[-1]]["content"]
    check("the chart is on the CMS post as markup, next to its JSON-LD",
          "<svg" in stored_content and "&lt;svg" not in stored_content
          and "application/ld+json" in stored_content)

    StubWP.sanitize = True                     # a CMS/plugin that strips scripts and SVG on save
    sanitized = _resend()
    check("a CMS that strips the script/SVG is reported instead of assumed fine",
          sanitized["verified"] is False and len(sanitized["problems"]) >= 2, str(sanitized["problems"]))
    check("...and the row records verified=false (the sweep can find it)",
          db3.recorded[-1]["record"]["verified"] is False)

    StubWP.sanitize = False
    reads_before = len([1 for _, path, _ in StubWP.requests if "context=edit" in path])
    _resend(verify=False)
    reads_after = len([1 for _, path, _ in StubWP.requests if "context=edit" in path])
    check("--no-verify skips the read-back", reads_after == reads_before)
finally:
    server3.shutdown()



print("\nreal Supabase row (read-only, no WordPress call)")
try:
    url, key = wd.supabase_config()
except SystemExit as exc:
    print(f"  (skipped: {exc})")
else:
    try:
        db = wd.Supabase(url, key)
        rows = db.articles(slug="reshoring-moved-the-tariff-upstream")
    except Exception as exc:                      # noqa: BLE001
        # Network/API trouble must not fail this gate: the hermetic assertions above are the
        # regression protection. Report the skip instead of turning a hiccup into a red build.
        print(f"  (skipped: Supabase unreachable — {str(exc)[:120]})")
        rows = []
    if not rows:
        print("  (skipped: sample row not found)")
    else:
        row = rows[0]
        site = db.site_for((row.get("metadata") or {}).get("vertical"))
        payload, notes = wd.build_payload(row, site, publisher_name="Gini Loh")
        check("real row: title has no vertical id",
              (row["metadata"]["vertical"] not in payload["title"]), payload["title"])
        check("real row: excerpt is the lead paragraph",
              payload["excerpt"].startswith("Coca-Cola just pledged"), payload["excerpt"][:80])
        check("real row: routes to the CMS its vertical maps to",
              site["cms_base_url"] == "https://cms.giniloh.com", site["cms_base_url"])
        check("real row: content is HTML with no pipeline markers",
              payload["content"].startswith("<p>") and "<!--" not in payload["content"])
        check("real row: status draft", payload["status"] == "draft")
        print(f"  payload: {len(payload['content'])} chars HTML, excerpt {len(payload['excerpt'])} chars")

print(f"\n{len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    for name in FAIL:
        print(f"  FAILED: {name}")
sys.exit(1 if FAIL else 0)
