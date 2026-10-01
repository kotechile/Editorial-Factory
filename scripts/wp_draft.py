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


def supabase_get(path: str, quiet: bool = False) -> list[dict] | None:
    """Best-effort PostgREST GET — returns None rather than exiting.

    For optional reads (the site list behind the internal-link index) where an unreachable database
    should degrade to a documented fallback instead of killing the run. Use Supabase() directly when
    a miss has to fail loudly. `quiet` suppresses the warning for an attempt that is expected to fail,
    e.g. asking for a column an unapplied migration has not added yet.
    """
    try:
        _, rows = Supabase(*supabase_config())._call("GET", path)
        return rows or []
    except Exception as exc:                                   # noqa: BLE001 - optional read
        if not quiet:
            print(f"[supabase] optional read failed ({path}): {exc}", file=sys.stderr)
        return None


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
        """Resolve the destination CMS for a vertical. Fails closed — never guesses a site.

        Selects `*` rather than a column list so an added column (wp_category_id) is picked up the
        moment the migration is applied — and so a push does not break on a database that has not
        been migrated yet.
        """
        _, rows = self._call(
            "GET", f"{SITES_TABLE}?select=*&vertical_id=eq.{urllib.parse.quote(vertical)}")
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
    body = re.sub(r"^\s*<!--.*?-->\s*$", "", body, flags=re.M)
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


_RAW_SVG = re.compile(r"<svg\b[^>]*>.*?</svg>", re.S | re.I)
_RAW_UNSAFE = re.compile(r"<script\b|\son[a-z]+\s*=", re.I)


def _stash_raw_blocks(markdown: str) -> tuple[str, dict[str, str]]:
    """Lift generated inline SVG out of the markdown so the reader gets a chart, not its markup.

    This renderer escapes HTML, which is correct for prose but turned the hub's chart into a wall of
    `&lt;svg …` text on the page — the chart only ever existed as a visual in the source file.
    Stashing the block also protects the `<!-- Row n -->` comments inside the SVG from being read as
    markdown comment lines and dropped. A block carrying a script tag or an event handler is
    discarded rather than passed through.
    """
    blocks: dict[str, str] = {}

    def stash(match: "re.Match[str]") -> str:
        block = match.group(0)
        if _RAW_UNSAFE.search(block):
            return ""
        key = f"RAWBLOCK{len(blocks)}TOKEN"
        blocks[key] = block
        return f"\n\n{key}\n\n"

    return _RAW_SVG.sub(stash, markdown), blocks


def md_to_html(markdown: str) -> str:
    """Render the reader-facing markdown to HTML.

    Handles the constructs the pipeline actually emits: headings, paragraphs, nested-ish
    bullet lists, ordered lists, blockquotes (the Quick-Cite cards), pipe tables (the
    citation-hub benchmark matrix) and fenced code. Deliberately small: an unknown line
    becomes a paragraph rather than being dropped. Generated inline SVG passes through as markup.
    """
    markdown, raw_blocks = _stash_raw_blocks(markdown)
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

        if stripped in raw_blocks:
            flush_all()
            out.append(raw_blocks[stripped])
            continue

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
    tag, and a mid-word cut ("...contrasted with vendor cl…") is what the generator ships.
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


def _resolve_placeholders(value, mapping: dict, notes: list[str], path: str):
    """Recursively substitute {{TOKEN}} placeholders and report every substitution."""
    if isinstance(value, dict):
        return {k: _resolve_placeholders(v, mapping, notes, f"{path}.{k}") for k, v in value.items()}
    if isinstance(value, list):
        return [_resolve_placeholders(v, mapping, notes, f"{path}[{i}]") for i, v in enumerate(value)]
    if isinstance(value, str):
        for token, replacement in mapping.items():
            if token in value:
                value = value.replace(token, replacement)
                notes.append(f"{path}: {token} -> {replacement}")
        if "editorial-factory.com" in value:      # legacy artifact from an older generator run
            value = value.replace("https://editorial-factory.com", mapping["{{SITE_URL}}"])
            notes.append(f"{path}: editorial-factory.com (does not resolve) -> {mapping['{{SITE_URL}}']}")
        if "editorial factory" in value.lower():
            value = re.sub(r"editorial factory[^\"']*", mapping["{{PUBLISHER_NAME}}"], value, flags=re.I)
            notes.append(f"{path}: 'Editorial Factory…' -> {mapping['{{PUBLISHER_NAME}}']}")
    return value


def retarget_publisher(node: dict, site: dict, publisher_name: str | None,
                       author_name: str | None = None) -> tuple[dict, list[str]]:
    """Point the schema's identity at the site the article is actually published on.

    The generator emits placeholders ({{SITE_URL}}, {{PUBLISHER_NAME}}, {{AUTHOR_NAME}}) because the
    destination is chosen here, not there; older artifacts instead hard-code
    `editorial-factory.com`, which does not resolve (verified), and the internal approval handle as
    the public author. Either way the value is rewritten — and reported, never done silently. A
    placeholder with no value supplied is DROPPED rather than published literally: a consumer
    reading `{{AUTHOR_NAME}}` as an author name is worse than no author node.
    """
    notes: list[str] = []
    node = json.loads(json.dumps(node))
    if author_name:
        mapping = {"{{SITE_URL}}": site["frontend_url"],
                   "{{PUBLISHER_NAME}}": publisher_name or site["site_domain"],
                   "{{AUTHOR_NAME}}": author_name}
    else:
        mapping = {"{{SITE_URL}}": site["frontend_url"],
                   "{{PUBLISHER_NAME}}": publisher_name or site["site_domain"]}
        for key in ("author", "creator", "publisher"):
            value = node.get(key)
            if isinstance(value, dict) and str(value.get("name") or "").strip() == "{{AUTHOR_NAME}}":
                node.pop(key, None)
                notes.append(f"schema {key} dropped: generator placeholder with no --author-name supplied")

    node = _resolve_placeholders(node, mapping, notes, "schema")
    return node, notes


def build_payload(row: dict, site: dict, publisher_name: str | None = None,
                  author_name: str | None = None) -> tuple[dict, list[str]]:
    """The exact WordPress post payload, plus a list of mapping notes for the operator."""
    metadata = row.get("metadata") or {}
    notes: list[str] = []
    content_html = md_to_html(row.get("content") or "")

    dataset, schema_notes = retarget_publisher(
        extract_dataset_node((metadata.get("seo") or {}).get("schema")) or {}, site, publisher_name,
        author_name)
    notes += schema_notes
    if dataset:
        content_html += (
            '\n<script type="application/ld+json">'
            + json.dumps(dataset, separators=(",", ":")) + "</script>")
    else:
        notes.append("no Dataset node in metadata.seo.schema — sent no JSON-LD. The frontends emit "
                     "Article/BreadcrumbList/FAQPage themselves, so this is only a defect when the "
                     "generator produced a node it did not capture (scripts/publish.py reports that)")

    seo = metadata.get("seo") or {}
    if not (seo.get("meta_description") or "").strip():
        notes.append("no metadata.seo.meta_description — the excerpt fell back to the article's lead "
                     "paragraph. Run scripts/article_assets.py on the artifact (publish.py does it "
                     "automatically) to generate and store one")
    if re.search(r"<svg\b", content_html, re.I) is None:
        notes.append("no inline SVG in the content — nothing to transfer (the artifact carries no chart)")

    payload = {
        "title": make_title(row),
        "slug": metadata.get("slug"),
        "excerpt": make_excerpt(row),
        "content": content_html,
        "status": "draft",              # hard-coded: publishing is a human decision in the CMS
        "comment_status": "closed",
        "ping_status": "closed",
    }
    # Category. Every published post on both sites carries one, so a draft that lands in
    # WordPress's default (Uncategorized) leaves work for the operator and, if missed, a post that
    # never appears on a category page. The id is per-site, so it is routed per vertical in
    # public.vertical_sites (migrations/0004) — never guessed from the vertical name here.
    category_id = site.get("wp_category_id")
    if category_id:
        payload["categories"] = [int(category_id)]
        notes.append(f"category {int(category_id)} (from {SITES_TABLE}.wp_category_id)")
    else:
        notes.append(f"no {SITES_TABLE}.wp_category_id for this vertical — WordPress will file the "
                     f"draft under its default category; set one before publishing")
    if not payload["slug"]:
        raise RuntimeError("article has no metadata.slug — it is the idempotency key")
    return payload, notes


# ─────────────────────────────────────────────────────────────────────────────
# delivery verification (read the post back, compare to what was sent)
# ─────────────────────────────────────────────────────────────────────────────

_LD_SCRIPT = re.compile(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', re.S | re.I)


def _plain_text(value) -> str:
    """Reader-visible text of a CMS field: unescaped, tags dropped, whitespace collapsed.

    A CMS read-back is not the string that was written — WordPress entity-encodes punctuation
    (`&#8217;`) and wraps `excerpt` in `<p>…</p>` — so a raw comparison reports a failure on a
    perfectly good push.
    """
    text = html.unescape(str(value or ""))
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _ld_blocks(content: str) -> list:
    out = []
    for raw in _LD_SCRIPT.findall(content or ""):
        try:
            out.append(json.loads(raw))
        except Exception:                          # noqa: BLE001 - an unparsable block is a defect
            out.append({"__unparsable__": raw[:120]})
    return out


def delivery_problems(payload: dict, post: dict) -> list[str]:
    """Compare a post read back from the CMS against the payload that was sent. [] means it landed.

    This is the half that a push-only connector cannot see: the CMS is free to sanitize, truncate,
    re-encode or drop anything in the body, and a 201 response proves only that the request was
    accepted. Run it after every real push and report the result instead of assuming it.
    """
    problems: list[str] = []
    sent_content = payload.get("content") or ""
    stored_content = ((post.get("content") or {}).get("raw")
                      or (post.get("content") or {}).get("rendered") or "")
    stored_post_id = post.get("id")

    if _plain_text(((post.get("title") or {}).get("raw") or (post.get("title") or {}).get("rendered"))) \
            != _plain_text(payload.get("title")):
        problems.append(f"title: sent {payload.get('title')!r}, CMS holds "
                        f"{_plain_text(((post.get('title') or {}).get('raw')))[:80]!r}")

    stored_excerpt = _plain_text((post.get("excerpt") or {}).get("raw")
                                 or (post.get("excerpt") or {}).get("rendered"))
    sent_excerpt = _plain_text(payload.get("excerpt"))
    if stored_excerpt and sent_excerpt and stored_excerpt[:80] != sent_excerpt[:80]:
        problems.append(f"excerpt: sent {sent_excerpt[:60]!r}, CMS holds {stored_excerpt[:60]!r}")
    elif sent_excerpt and not stored_excerpt:
        problems.append("excerpt: empty on the CMS — the frontends' <meta name=\"description\"> is blank")

    sent_ld, stored_ld = _ld_blocks(sent_content), _ld_blocks(stored_content)
    if len(stored_ld) != len(sent_ld):
        problems.append(f"JSON-LD: sent {len(sent_ld)} block(s), CMS holds {len(stored_ld)} — "
                        f"a <script type=application/ld+json> block was dropped or added")
    else:
        for index, (sent_node, stored_node) in enumerate(zip(sent_ld, stored_ld)):
            if json.dumps(sent_node, sort_keys=True) != json.dumps(stored_node, sort_keys=True):
                problems.append(f"JSON-LD block {index + 1} differs from what was sent")

    sent_svg = len(re.findall(r"<svg\b", sent_content, re.I))
    stored_svg = len(re.findall(r"<svg\b", stored_content, re.I))
    if sent_svg != stored_svg:
        problems.append(f"inline SVG: sent {sent_svg} chart(s), CMS holds {stored_svg}")
    if sent_svg and re.search(r"&lt;svg", stored_content, re.I):
        problems.append("inline SVG: the chart was stored as escaped text (&lt;svg), not as markup")
    if sent_content.strip() and not stored_content.strip():
        problems.append("content: the CMS holds an empty body")

    if stored_post_id and str(post.get("status") or "") not in ("draft", "pending", "private", ""):
        problems.append(f"status: the post came back {post.get('status')!r}, not draft — "
                        f"publishing must stay a human step in the CMS")
    return problems


def verification_summary(payload: dict, post: dict) -> str:
    """A one-line description of what a successful read-back verified."""
    content = payload.get("content") or ""
    return (f"title, {len(_plain_text(payload.get('excerpt')))}-char excerpt, "
            f"{len(_ld_blocks(content))} JSON-LD block(s), "
            f"{len(re.findall(r'<svg', content, re.I))} inline SVG(s), "
            f"{len(content)} chars of body")


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

    def category_name(self, category_id: int) -> str:
        """The category's name on THIS site, or an explicit failure.

        Category ids are per-site — giniloh #4 is "Money & Wealth", wellroost #4 is "Energy &
        Efficiency" — so a value routed for one site and pushed to the other would silently misfile
        the post. Validating here turns that into a loud error instead.
        """
        try:
            _, category = self._call("GET", f"categories/{int(category_id)}?_fields=id,name")
        except RuntimeError as exc:
            raise RuntimeError(
                f"{self.base}: category {category_id} does not exist on this site — check "
                f"public.vertical_sites.wp_category_id for the vertical's own domain ({exc})") from None
        return str((category or {}).get("name") or "")

    def read_back(self, post_id) -> dict:
        """The post as the CMS actually holds it — raw fields, drafts included.

        `context=edit` is what returns `content.raw`; the default `view` context returns rendered
        HTML, where the read-back cannot tell an injected script tag from a stripped one.
        """
        _, post = self._call("GET", f"posts/{int(post_id)}?context=edit")
        return post or {}

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
             author_name: str | None = None, wp_factory=None, verify: bool = True) -> dict:
    metadata = row.get("metadata") or {}
    vertical = metadata.get("vertical") or (row.get("tags") or [""])[0]
    if not vertical:
        raise RuntimeError(f"row {row.get('id')} has no vertical — cannot route it to a site")
    site = db.site_for(vertical)
    payload, notes = build_payload(row, site, publisher_name, author_name)

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
    if payload.get("categories"):
        category_id = payload["categories"][0]
        print(f"  category: {category_id} — {html.unescape(wp.category_name(category_id))} "
              f"(validated on {site['site_domain']})")
    post, action = wp.upsert(payload)
    print(f"  {action}: post {post.get('id')} ({post.get('status')}) {post.get('link')}")

    # Read the post back. A 201 says the request was accepted, not that the CMS kept what was sent:
    # sanitizers, plugins and editors are all free to strip a <script> or an inline <svg> on save,
    # which is exactly the failure a push-only connector cannot see. Reported, never assumed.
    problems: list[str] = []
    summary = ""
    if verify:
        try:
            stored = wp.read_back(post.get("id"))
            problems = delivery_problems(payload, stored)
            if problems:
                print("  DELIVERY VERIFICATION FAILED — the CMS does not hold what was sent:")
                for problem in problems:
                    print(f"    - {problem}")
            else:
                summary = verification_summary(payload, stored)
                print(f"  delivery verified on {site['site_domain']}: {summary}")
        except Exception as exc:                    # noqa: BLE001 - surface, never swallow (rule 6)
            problems = [f"could not read the post back to verify delivery: {exc}"]
            print(f"  DELIVERY VERIFICATION FAILED — {problems[0]}")

    record = {
        "post_id": post.get("id"),
        "status": post.get("status"),
        "link": post.get("link"),
        "edit_url": f"{site['cms_base_url']}/wp-admin/post.php?post={post.get('id')}&action=edit",
        "site": site["site_domain"],
        "pushed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "pushed_by": "scripts/wp_draft.py",
        "verified": not problems,
    }
    db.record_push(row["id"], metadata, record)
    print(f"  recorded metadata.{WORDPRESS} on the Supabase row ({row['id']})")
    return {"status": action, "site": site["site_domain"], "post_id": post.get("id"),
            "edit_url": record["edit_url"], "verified": not problems, "problems": problems,
            "summary": summary}


def push_by_slug(slug: str, *, dry_run: bool = False, publisher_name: str | None = None,
                 author_name: str | None = None, wp_factory=None, db=None,
                 verify: bool = True) -> dict:
    """Push one article by its Supabase slug. The single entry point used by both this CLI and
    scripts/publish.py, so the in-run hook and a manual re-run share one code path."""
    db = db or Supabase(*supabase_config())
    rows = db.articles(slug=slug)
    if not rows:
        raise RuntimeError(f"no row in public.{ARTICLES_TABLE} with metadata.slug '{slug}'")
    return push_one(rows[0], db, dry_run=dry_run, publisher_name=publisher_name,
                    author_name=author_name, wp_factory=wp_factory, verify=verify)


def main() -> int:
    parser = argparse.ArgumentParser(description="Push generated articles to their vertical's WordPress CMS as drafts")
    parser.add_argument("--slug", help="Article slug (metadata->>slug)")
    parser.add_argument("--all", action="store_true", help="Every row with no metadata.wordpress.post_id yet")
    parser.add_argument("--limit", type=int, default=1, help="Max articles to push in one run (default 1)")
    parser.add_argument("--dry-run", action="store_true", help="Print the payload without contacting WordPress")
    parser.add_argument("--no-verify", action="store_true",
                        help="Skip the post-push read-back (default: read the post back and compare "
                             "what the CMS stored against what was sent)")
    parser.add_argument("--publisher-name", default=None,
                        help="Organization name for the schema (default: the destination site domain)")
    parser.add_argument("--author-name", default=None,
                        help="Byline for the schema's author node. Omitted = the author node is "
                             "dropped rather than publishing the generator's {{AUTHOR_NAME}} token")
    args = parser.parse_args()

    if not args.slug and not args.all:
        parser.error("pass --slug <slug> or --all")

    db = Supabase(*supabase_config())

    if args.slug:
        try:
            result = push_by_slug(args.slug, dry_run=args.dry_run, publisher_name=args.publisher_name,
                                  author_name=args.author_name, db=db, verify=not args.no_verify)
        except Exception as exc:                       # rule 6: surface it, never a silent skip
            print(f"\n  FAILED {args.slug}: {exc}", file=sys.stderr)
            return 1
        if result.get("problems"):
            print("\n  the draft exists, but the CMS does not hold what was sent (see above) — "
                  "fix the mapping and re-run; the slug is the idempotency key, so this updates "
                  "the same post rather than duplicating it", file=sys.stderr)
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
            result = push_one(row, db, dry_run=args.dry_run, publisher_name=args.publisher_name,
                              author_name=args.author_name, verify=not args.no_verify)
            if result.get("problems"):
                failures += 1
        except Exception as exc:                       # rule 6: surface it, never a silent skip
            failures += 1
            print(f"\n  FAILED {row.get('title')}: {exc}", file=sys.stderr)

    print(f"\npushed: {len(rows) - failures}/{len(rows)} | drafts only — publishing stays a human step in the CMS")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
