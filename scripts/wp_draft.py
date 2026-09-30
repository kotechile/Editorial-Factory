#!/usr/bin/env python3
"""Push a generated article from Supabase into its vertical's WordPress CMS as a DRAFT.

The pipeline writes each article to public.articles (content = markdown, with the editorial
fields in the `metadata` jsonb). Delivery to a site is manual today, and the field mapping
lives in the operator's head — which is how an article titled "AI Price Volatility: The $250k
Upkeep Tax" reached giniloh.com with the raw vertical id as its H1, og:title and
Article.headline. This script makes that mapping explicit and testable.

Contract with the destinations (cms.<domain>, routed per vertical by public.vertical_sites):

  title    <- metadata.headline (fallback: title).  NEVER the vertical id — asserted below.
  slug     <- metadata.slug, used as the idempotency key (re-runs update, never duplicate).
  excerpt  <- metadata.seo.meta_description, else the article's lead paragraph. This is what
              the Astro frontends render as <meta name="description">. Trimmed on a word
              boundary, never mid-word.
  content  <- the markdown body rendered to HTML: pipeline section markers removed, the
              internal `<!-- linkedin -->` variant and `## Gate report` dropped, tables and
              blockquotes rendered as real elements.
  schema   <- ONLY the `Dataset` node of metadata.seo.schema, appended as a JSON-LD script.
              The frontends already emit Article + BreadcrumbList + FAQPage from the post
              itself, so re-sending those would duplicate nodes. No Dataset node => nothing
              is emitted (never invented).
  status   <- always "draft". There is no flag to publish: the founder's approval gate stays
              on the draft -> publish flip, which is a human action in the CMS.

Write-back: metadata.wordpress = {post_id, edit_url, link, status, site, pushed_at} on the
same row, so the next run can update rather than duplicate, and so GSC data can later be
joined back to the row.

Usage:
  python3 scripts/wp_draft.py --slug reshoring-moved-the-tariff-upstream --dry-run
  python3 scripts/wp_draft.py --slug mcp-skills-extension                  # creates a draft
  python3 scripts/wp_draft.py --all --limit 5                              # every un-pushed row

Credentials (env or ./.env), keyed by the destination domain:
  WP_GINILOH_USER / WP_GINILOH_APP_PASSWORD
  WP_WELLROOST_USER / WP_WELLROOST_APP_PASSWORD
Create the password in the CMS: Users -> Profile -> Application Passwords (core, 5.6+).
"""

from __future__ import annotations

import argparse
import html
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parent.parent
ARTICLES_TABLE = "articles"
SITES_TABLE = "vertical_sites"
EXCERPT_TARGET = 165          # characters, before the word-boundary trim
WORDPRESS = "wordpress"


# ─────────────────────────────────────────────────────────────────────────────
# config
# ─────────────────────────────────────────────────────────────────────────────

def load_env() -> None:
    """Read ./.env without overriding anything already exported."""
    env_file = ROOT / ".env"
    if not env_file.exists():
        return
    for raw in env_file.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def supabase_config() -> tuple[str, str]:
    load_env()
    url = os.environ.get("SUPABASE_URL", "").rstrip("/")
    key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")
    if not url or not key:
        sys.exit("FAIL: SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY must be set (env or ./.env)")
    return url, key


def credentials_for(site_domain: str) -> tuple[str, str]:
    """WP_USER / WP_APP_PASSWORD for a site, keyed by its domain label.

    giniloh.com -> WP_GINILOH_USER / WP_GINILOH_APP_PASSWORD
    wellroost.com -> WP_WELLROOST_USER / WP_WELLROOST_APP_PASSWORD
    WP_USER / WP_APP_PASSWORD act as a single-site fallback.
    """
    label = site_domain.split(".")[0].upper()
    full = re.sub(r"[^A-Z0-9]", "_", site_domain.upper())
    user = (os.environ.get(f"WP_{label}_USER") or os.environ.get(f"WP_{full}_USER")
            or os.environ.get("WP_USER", ""))
    password = (os.environ.get(f"WP_{label}_APP_PASSWORD") or os.environ.get(f"WP_{full}_APP_PASSWORD")
                or os.environ.get("WP_APP_PASSWORD", ""))
    if not user or not password:
        sys.exit(
            f"FAIL: no WordPress credentials for {site_domain}.\n"
            f"      Set WP_{label}_USER and WP_{label}_APP_PASSWORD in the environment or ./.env.\n"
            f"      Create the password in the CMS: Users -> Profile -> Application Passwords."
        )
    return user, password


# ─────────────────────────────────────────────────────────────────────────────
# Supabase reads/writes
# ─────────────────────────────────────────────────────────────────────────────

class Supabase:
    def __init__(self, url: str, key: str):
        self.url, self.key = url, key

    def _call(self, method: str, path: str, body=None, extra_headers=None):
        headers = {"apikey": self.key, "Authorization": f"Bearer {self.key}",
                   "Accept": "application/json"}
        data = None
        if body is not None:
            data = json.dumps(body).encode()
            headers["Content-Type"] = "application/json"
        if extra_headers:
            headers.update(extra_headers)
        req = urllib.request.Request(f"{self.url}/rest/v1/{path}", data=data,
                                     headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=45) as response:
                raw = response.read().decode("utf-8", "replace")
                return response.status, (json.loads(raw) if raw.strip() else None)
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")[:300]
            raise RuntimeError(f"Supabase {method} {path} -> HTTP {exc.code}: {detail}") from None

    def articles(self, slug: str | None = None, un_pushed_only: bool = False,
                 limit: int | None = None) -> list[dict]:
        """Rows from public.articles. The editorial fields live in the metadata jsonb."""
        fields = "id,title,content,source_url,tags,metadata,created_at"
        if slug:
            path = f"{ARTICLES_TABLE}?select={fields}&metadata->>slug=eq.{urllib.parse.quote(slug)}"
        else:
            path = f"{ARTICLES_TABLE}?select={fields}&order=created_at.desc"
        _, rows = self._call("GET", path)
        rows = rows or []
        if un_pushed_only:
            rows = [r for r in rows if not ((r.get("metadata") or {}).get(WORDPRESS) or {}).get("post_id")]
        if limit is not None:
            # `limit is not None`, not truthiness: limit=0 means "none" (a deliberate no-op probe),
            # and treating it as falsy returned EVERY row instead — which turned a no-op test run
            # into a full backfill. None means unlimited.
            rows = rows[:max(0, limit)]
        return rows

    def site_for(self, vertical: str) -> dict:
        """Resolve the destination CMS for a vertical. Fails closed — never guesses a site."""
        _, rows = self._call(
            "GET", f"{SITES_TABLE}?select=vertical_id,cms_base_url,site_domain,frontend_url,active"
                       f"&vertical_id=eq.{urllib.parse.quote(vertical)}")
        rows = rows or []
        if not rows:
            raise RuntimeError(
                f"no destination in public.{SITES_TABLE} for vertical '{vertical}' — "
                f"add a row (supabase/migrations/0003_vertical_sites.sql) rather than guessing a site")
        site = rows[0]
        if site.get("active") is False:
            raise RuntimeError(f"vertical '{vertical}' is routed to {site['site_domain']} but marked active=false")
        return site

    def record_push(self, row_id: str, metadata: dict, record: dict) -> None:
        """Merge metadata.wordpress into the row's metadata jsonb (no new columns needed)."""
        merged = dict(metadata or {})
        merged[WORDPRESS] = record
        self._call("PATCH", f"{ARTICLES_TABLE}?id=eq.{row_id}", {"metadata": merged},
                   {"Prefer": "return=minimal"})


# ─────────────────────────────────────────────────────────────────────────────
# markdown -> HTML (the destinations store HTML in post_content)
# ─────────────────────────────────────────────────────────────────────────────

def reader_markdown(markdown: str) -> str:
    """Strip frontmatter and the pipeline's internal sections — the same cuts the site's
    readerBody() makes, so the CMS holds what a reader is meant to see."""
    body = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", markdown or "", flags=re.S)
    body = body.split("<!-- linkedin -->")[0]
    body = re.split(r"^##\s+Gate report\s*$", body, flags=re.M)[0]
    body = re.sub(r"^\s*<!--\s*(lead|tension|tactical-insight|nuanced-takeaway|tldr|quick-cite|schema|internal-links)\s*-->\s*$",
                  "", body, flags=re.M)
    return body.strip()


def _linkify_bare_urls(text: str) -> str:
    """Turn bare URLs into links, leaving any href already produced by the [text](url) pass alone.

    The pipeline's Sources sections cite bare URLs ("[1] Fortune — https://fortune.com/…"), so
    without this the destination post ships plain-text citations instead of links.
    """
    parts = re.split(r"(<a\s[^>]*>.*?</a>)", text, flags=re.S)
    for index, part in enumerate(parts):
        if part.startswith("<a "):
            continue

        def repl(match: re.Match) -> str:
            url, trail = match.group(1), ""
            while url and url[-1] in ".,;":
                trail, url = url[-1] + trail, url[:-1]
            return f'<a href="{url}">{url}</a>{trail}'

        parts[index] = re.sub(r"(?<![\"'=/>])(https?://[^\s<>\")]+)", repl, part)
    return "".join(parts)


def _inline(text: str) -> str:
    out = html.escape(text, quote=False)
    out = re.sub(r"`([^`]+)`", r"<code>\1</code>", out)
    out = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", out)
    out = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", out)
    out = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', out)
    return _linkify_bare_urls(out)


def md_to_html(markdown: str) -> str:
    """Render the reader-facing markdown to HTML.

    Handles the constructs the pipeline actually emits: headings, paragraphs, nested-ish
    bullet lists, ordered lists, blockquotes (the Quick-Cite cards), pipe tables (the
    citation-hub benchmark matrix) and fenced code. Deliberately small: an unknown line
    becomes a paragraph rather than being dropped.
    """
    lines = reader_markdown(markdown).split("\n")
    out: list[str] = []
    para: list[str] = []
    list_items: list[str] = []
    list_tag = ""
    quote: list[str] = []
    table: list[list[str]] = []
    fence: list[str] = []
    in_fence = False

    def flush_para():
        if para:
            out.append(f"<p>{' '.join(para)}</p>")
            para.clear()

    def flush_list():
        nonlocal list_tag
        if list_items:
            out.append(f"<{list_tag}>{''.join(list_items)}</{list_tag}>")
            list_items.clear()
            list_tag = ""

    def flush_quote():
        if quote:
            out.append(f"<blockquote><p>{' '.join(quote)}</p></blockquote>")
            quote.clear()

    def flush_table():
        if not table:
            return
        head, *body_rows = table
        out.append("<table><thead><tr>" + "".join(f"<th>{c}</th>" for c in head) + "</tr></thead><tbody>")
        for r in body_rows:
            out.append("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>")
        out.append("</tbody></table>")
        table.clear()

    def flush_all():
        flush_para(); flush_list(); flush_quote(); flush_table()

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("```"):
            if in_fence:
                out.append("<pre><code>" + html.escape("\n".join(fence)) + "</code></pre>")
                fence.clear(); in_fence = False
            else:
                flush_all(); in_fence = True
            continue
        if in_fence:
            fence.append(line)
            continue

        if re.match(r"^\|.*\|$", stripped):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                continue                       # separator row
            if not table:
                flush_para(); flush_list(); flush_quote()
            table.append([_inline(c) for c in cells])
            continue
        if table:
            flush_table()

        if not stripped:
            flush_all()
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if heading:
            flush_all()
            level = len(heading.group(1))
            out.append(f"<h{level}>{_inline(heading.group(2))}</h{level}>")
            continue

        bullet = re.match(r"^[-*]\s+(.*)$", stripped)
        ordered = re.match(r"^\d+[.)]\s+(.*)$", stripped)
        if bullet or ordered:
            flush_para(); flush_quote()
            tag = "ul" if bullet else "ol"
            if list_tag and list_tag != tag:
                flush_list()
            list_tag = tag
            list_items.append(f"<li>{_inline((bullet or ordered).group(1))}</li>")
            continue

        if stripped.startswith(">"):
            flush_para(); flush_list()
            quote.append(_inline(stripped.lstrip(">").strip()))
            continue

        if re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", stripped):
            flush_all()
            out.append("<hr>")
            continue

        para.append(_inline(stripped))

    flush_all()
    if fence:
        out.append("<pre><code>" + html.escape("\n".join(fence)) + "</code></pre>")
    return "\n".join(out)


# ─────────────────────────────────────────────────────────────────────────────
# field mapping
# ─────────────────────────────────────────────────────────────────────────────

def lead_paragraph(markdown: str) -> str:
    """First real paragraph of the article — the destination's established excerpt source."""
    for block in reader_markdown(markdown).split("\n"):
        text = block.strip()
        if not text or text.startswith(("#", "|", ">", "-", "*", "```")):
            continue
        text = re.sub(r"\[([^\]]+)\]\([^)\s]+\)", r"\1", text)
        text = re.sub(r"[*`_]", "", text)
        if len(text.split()) >= 8:
            return text
    return ""


def make_excerpt(row: dict, limit: int = EXCERPT_TARGET) -> str:
    """meta_description when the pipeline wrote one, else the lead paragraph.

    Always trimmed on a word boundary: the budget this feeds is a <meta name="description">
    tag, and a mid-word cut ("...contrasted with vendor cl...") is what the generator ships.
    """
    seo = (row.get("metadata") or {}).get("seo") or {}
    text = (seo.get("meta_description") or "").strip() or lead_paragraph(row.get("content") or "")
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0].rstrip(" ,;:—-") + "…"


def make_title(row: dict) -> str:
    """The article's real headline. Asserted to not contain the vertical id — the exact defect
    found live on giniloh.com ('enterprise_build_vs_buy: The $250k AI Upkeep Tax')."""
    metadata = row.get("metadata") or {}
    title = (metadata.get("headline") or row.get("title") or "").strip()
    if not title:
        raise RuntimeError("article has no headline/title — refusing to push an untitled draft")
    vertical = (metadata.get("vertical") or (row.get("tags") or [None])[0] or "")
    if vertical and vertical.lower() in title.lower():
        raise RuntimeError(
            f"refusing to push: the vertical id '{vertical}' appears in the title '{title}'. "
            f"That is the live defect this script exists to prevent.")
    return title


def extract_dataset_node(schema) -> dict | None:
    """The frontends already emit Article + BreadcrumbList + FAQPage, so only the Dataset node
    is worth sending on. Anything else would duplicate nodes on the page."""
    if not schema:
        return None
    nodes = schema.get("@graph") if isinstance(schema, dict) else schema
    if isinstance(nodes, dict):
        nodes = [nodes]
    for node in nodes or []:
        if isinstance(node, dict) and str(node.get("@type", "")).lower() == "dataset":
            return node
    return None


def retarget_publisher(node: dict, site: dict, publisher_name: str | None) -> tuple[dict, list[str]]:
    """Point creator/publisher at the site the article is actually published on.

    The generator hard-codes `editorial-factory.com`, which does not resolve (verified), so a
    pasted schema asserts a publisher that does not exist. The destination is known here, so
    it is rewritten — and reported, never done silently.
    """
    notes: list[str] = []
    node = json.loads(json.dumps(node))
    for key in ("creator", "publisher"):
        value = node.get(key)
        if not isinstance(value, dict):
            continue
        url = str(value.get("url") or "")
        if not url or "editorial-factory.com" in url:
            value["url"] = site["frontend_url"]
            notes.append(f"schema {key}.url -> {site['frontend_url']} (was '{url or 'unset'}')")
        if publisher_name:
            value["name"] = publisher_name
        name = str(value.get("name") or "")
        if "editorial factory" in name.lower():
            value["name"] = publisher_name or site["site_domain"]
            notes.append(f"schema {key}.name -> '{value['name']}' (was '{name}')")
    return node, notes


def build_payload(row: dict, site: dict, publisher_name: str | None = None) -> tuple[dict, list[str]]:
    """The exact WordPress post payload, plus a list of mapping notes for the operator."""
    metadata = row.get("metadata") or {}
    notes: list[str] = []
    content_html = md_to_html(row.get("content") or "")

    dataset, schema_notes = retarget_publisher(
        extract_dataset_node((metadata.get("seo") or {}).get("schema")) or {}, site, publisher_name)
    notes += schema_notes
    if dataset:
        content_html += (
            '\n<script type="application/ld+json">'
            + json.dumps(dataset, separators=(",", ":")) + "</script>")
    else:
        notes.append("no Dataset node in metadata.seo.schema — sent no JSON-LD (frontends emit Article/FAQPage)")

    payload = {
        "title": make_title(row),
        "slug": metadata.get("slug"),
        "excerpt": make_excerpt(row),
        "content": content_html,
        "status": "draft",              # hard-coded: publishing is a human decision in the CMS
        "comment_status": "closed",
        "ping_status": "closed",
    }
    if not payload["slug"]:
        raise RuntimeError("article has no metadata.slug — it is the idempotency key")
    return payload, notes


# ─────────────────────────────────────────────────────────────────────────────
# WordPress REST client
# ─────────────────────────────────────────────────────────────────────────────

class WordPress:
    def __init__(self, base_url: str, user: str, password: str, timeout: int = 60):
        self.base = base_url.rstrip("/")
        self.auth = "Basic " + __import__("base64").b64encode(f"{user}:{password}".encode()).decode()
        self.timeout = timeout

    def _call(self, method: str, path: str, body=None):
        url = f"{self.base}/wp-json/wp/v2/{path}"
        data = json.dumps(body).encode() if body is not None else None
        headers = {"Authorization": self.auth, "Accept": "application/json"}
        if data:
            headers["Content-Type"] = "application/json"
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                raw = response.read().decode("utf-8", "replace")
                return response.status, (json.loads(raw) if raw.strip() else None)
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")[:400]
            raise RuntimeError(f"WordPress {method} {path} -> HTTP {exc.code}: {detail}") from None

    def find_by_slug(self, slug: str) -> dict | None:
        """status=any includes drafts, so a re-run finds the draft it created before.

        `status=any` needs edit_posts on the account: an Author/Editor Application Password
        works, a lower-privilege one returns `rest_forbidden_status`, which is a credentials
        problem rather than a request problem — say so instead of echoing the raw 400.
        """
        try:
            _, posts = self._call("GET", f"posts?slug={urllib.parse.quote(slug)}&status=any&_fields=id,status,link,slug")
        except RuntimeError as exc:
            if "rest_forbidden_status" in str(exc) or "Status is forbidden" in str(exc):
                raise RuntimeError(
                    f"{self.base}: the account cannot read drafts via the REST API "
                    f"(WordPress requires the Author role or higher for `status=any`). "
                    f"Use an Application Password from an Author/Editor account. Raw: {exc}") from None
            raise
        return (posts or [None])[0]

    def upsert(self, payload: dict) -> tuple[dict, str]:
        existing = self.find_by_slug(payload["slug"])
        if existing:
            _, post = self._call("POST", f"posts/{existing['id']}", payload)
            return post, "updated"
        _, post = self._call("POST", "posts", payload)
        return post, "created"


# ─────────────────────────────────────────────────────────────────────────────
# driver
# ─────────────────────────────────────────────────────────────────────────────

def push_one(row: dict, db, *, dry_run: bool = False, publisher_name: str | None = None,
             wp_factory=None) -> dict:
    metadata = row.get("metadata") or {}
    vertical = metadata.get("vertical") or (row.get("tags") or [""])[0]
    if not vertical:
        raise RuntimeError(f"row {row.get('id')} has no vertical — cannot route it to a site")
    site = db.site_for(vertical)
    payload, notes = build_payload(row, site, publisher_name)

    print(f"\n  article : {payload['title']}")
    print(f"  slug    : {payload['slug']}   (idempotency key)")
    print(f"  vertical: {vertical}  ->  {site['site_domain']}  ({site['cms_base_url']})")
    print(f"  excerpt : {len(payload['excerpt'])} chars | {payload['excerpt'][:72]}…")
    print(f"  content : {len(payload['content'])} chars HTML | status={payload['status']}")
    for note in notes:
        print(f"  note    : {note}")

    if dry_run:
        print("  DRY RUN — nothing sent. Payload:")
        print(json.dumps({**payload, "content": payload["content"][:400] + "…"}, indent=2)[:1600])
        return {"status": "dry-run", "site": site["site_domain"], "payload": payload}

    user, password = credentials_for(site["site_domain"])
    wp = (wp_factory or (lambda base, u, p: WordPress(base, u, p)))(site["cms_base_url"], user, password)
    post, action = wp.upsert(payload)
    print(f"  {action}: post {post.get('id')} ({post.get('status')}) {post.get('link')}")

    record = {
        "post_id": post.get("id"),
        "status": post.get("status"),
        "link": post.get("link"),
        "edit_url": f"{site['cms_base_url']}/wp-admin/post.php?post={post.get('id')}&action=edit",
        "site": site["site_domain"],
        "pushed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "pushed_by": "scripts/wp_draft.py",
    }
    db.record_push(row["id"], metadata, record)
    print(f"  recorded metadata.{WORDPRESS} on the Supabase row ({row['id']})")
    return {"status": action, "site": site["site_domain"], "post_id": post.get("id"),
            "edit_url": record["edit_url"]}


def push_by_slug(slug: str, *, dry_run: bool = False, publisher_name: str | None = None,
                 wp_factory=None, db=None) -> dict:
    """Push one article by its Supabase slug. The single entry point used by both this CLI and
    scripts/publish.py, so the in-run hook and a manual re-run share one code path."""
    db = db or Supabase(*supabase_config())
    rows = db.articles(slug=slug)
    if not rows:
        raise RuntimeError(f"no row in public.{ARTICLES_TABLE} with metadata.slug '{slug}'")
    return push_one(rows[0], db, dry_run=dry_run, publisher_name=publisher_name, wp_factory=wp_factory)


def main() -> int:
    parser = argparse.ArgumentParser(description="Push generated articles to their vertical's WordPress CMS as drafts")
    parser.add_argument("--slug", help="Article slug (metadata->>slug)")
    parser.add_argument("--all", action="store_true", help="Every row with no metadata.wordpress.post_id yet")
    parser.add_argument("--limit", type=int, default=1, help="Max articles to push in one run (default 1)")
    parser.add_argument("--dry-run", action="store_true", help="Print the payload without contacting WordPress")
    parser.add_argument("--publisher-name", default=None,
                        help="Organization name to write into the Dataset schema (default: the site domain)")
    args = parser.parse_args()

    if not args.slug and not args.all:
        parser.error("pass --slug <slug> or --all")

    db = Supabase(*supabase_config())

    if args.slug:
        try:
            push_by_slug(args.slug, dry_run=args.dry_run, publisher_name=args.publisher_name, db=db)
        except Exception as exc:                       # rule 6: surface it, never a silent skip
            print(f"\n  FAILED {args.slug}: {exc}", file=sys.stderr)
            return 1
        print("\npushed: 1/1 | drafts only — publishing stays a human step in the CMS")
        return 0

    rows = db.articles(un_pushed_only=True, limit=args.limit)
    if not rows:
        print("Nothing to push (every row already has a draft in its CMS).")
        return 0

    failures = 0
    for row in rows:
        try:
            push_one(row, db, dry_run=args.dry_run, publisher_name=args.publisher_name)
        except Exception as exc:                       # rule 6: surface it, never a silent skip
            failures += 1
            print(f"\n  FAILED {row.get('title')}: {exc}", file=sys.stderr)

    print(f"\npushed: {len(rows) - failures}/{len(rows)} | drafts only — publishing stays a human step in the CMS")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
