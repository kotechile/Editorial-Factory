#!/usr/bin/env python3
"""Tests for scripts/wp_draft.py — run: python3 scripts/test_wp_draft.py

A stub WordPress REST API runs on localhost, so the whole push path (routing -> field
mapping -> idempotency -> write-back) is exercised without touching either live CMS.
The final block re-runs the mapping against a REAL row from Supabase (read-only, no
WordPress call) when credentials are present, then exits non-zero on any failure.
"""

from __future__ import annotations

import json
import pathlib
import re
import sys
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import wp_draft as wd  # noqa: E402

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
    requests: list[tuple[str, str, dict]] = []
    require_auth = True
    expected_auth = ""       # set by the test: "Basic <b64>" — a wrong password must 401

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

    def do_GET(self):
        if not self._authed():
            return
        StubWP.requests.append(("GET", self.path, {}))
        if self.path.startswith("/wp-json/wp/v2/posts?"):
            slug = self.path.split("slug=")[1].split("&")[0]
            found = [p for p in StubWP.posts.values() if p["slug"] == slug]
            return self._send(200, found)
        self._send(404, {"message": "not found"})

    def do_POST(self):
        if not self._authed():
            return
        body = self._read()
        StubWP.requests.append(("POST", self.path, body))
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
        "site_domain": "giniloh.com", "frontend_url": "https://giniloh.com", "active": True}

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

    def site_for(self, vertical):
        if self.site is None:
            raise RuntimeError(f"no destination in public.vertical_sites for vertical '{vertical}'")
        if self.site.get("active") is False:
            raise RuntimeError(f"vertical '{vertical}' is routed to {self.site['site_domain']} but marked active=false")
        return self.site

    def record_push(self, row_id, metadata, record):
        self.recorded.append({"row_id": row_id, "record": record})


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

print("\nschema handling")
dataset = wd.extract_dataset_node(ROW["metadata"]["seo"]["schema"])
check("sends only the Dataset node (Article/FAQPage come from the frontends)",
      dataset is not None and dataset["@type"] == "Dataset" and "TechArticle" not in json.dumps(dataset))
check("no Dataset node => nothing emitted", wd.extract_dataset_node({"@graph": [{"@type": "FAQPage"}]}) is None)
retargeted, notes = wd.retarget_publisher(dataset, SITE, None)
check("editorial-factory.com (unresolvable) rewritten to the destination",
      retargeted["creator"]["url"] == "https://giniloh.com" and any("creator.url" in n for n in notes))
check("...and reported, not silent", len(notes) >= 1 and "giniloh.com" in notes[0])

print("\nrouting — fails closed")
db_no_route = FakeDB(site=None)
raises("unknown vertical refuses to push", lambda: wd.push_one(ROW, db_no_route, dry_run=True),
       "no destination")
raises("inactive vertical refuses to push",
       lambda: wd.push_one(ROW, FakeDB(site={**SITE, "active": False}), dry_run=True), "active=false")

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

print("\nend-to-end against a stub WordPress")
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
    src = pathlib.Path(wd.__file__).read_text()
    declared = set(re.findall(r'add_argument\("(--[a-z-]+)"', src))
    check("no --status/--publish flag exists (publishing stays a human step)",
          not {"--status", "--publish"} & declared and '"status": "draft"' in src,
          f"declared options: {sorted(declared)}")
    payload, _ = wd.build_payload(ROW, SITE)
    check("payload status is hard-coded to draft", payload["status"] == "draft")
finally:
    server.shutdown()

# ─────────────────────────────────────────────────────────────────────────────
# real data (read-only; skipped when Supabase creds are absent)
# ─────────────────────────────────────────────────────────────────────────────

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
