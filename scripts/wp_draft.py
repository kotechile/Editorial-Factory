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
              blockquotes rendered as real elements. An artifact that reached the row with no
              internal links has them generated here, before the body is rendered
              (scripts/internal_links.py) — the reader-facing `## Related reading` section and the
              operator's placement hints — and the enriched body is written back to the row so the
              database and the CMS never disagree. Nothing is invented: if no live page on the
              destination site scores for the topic, the section is absent and the gap is reported.
  schema   <- ONLY the `Dataset` node of metadata.seo.schema, appended as a JSON-LD script.
              The frontends already emit Article + BreadcrumbList + FAQPage from the post
              itself, so re-sending those would duplicate nodes. No Dataset node => nothing
              is emitted (never invented).
  status   <- always "draft" for a post this connector creates or updates. There is no flag to
              publish: the founder's approval gate stays on the draft -> publish flip, which is a
              human action in the CMS. The one exception is an existing post that a human already
              published — a refresh sends no status for it at all, so it stays live rather than
              being demoted back to draft (verified: post 401 was published, and `--refresh` used
              to send status=draft for every row).

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
LINK_LINKS_MAX = 3            # reader-facing internal links per article (internal_links.MAX_LINKS)
LIVE_POST_NOTE = "live post kept published"    # upsert()'s action for an already-published post
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

    def update_body(self, row_id: str, content: str, metadata: dict) -> None:
        """Write an enriched body back onto the row, in ONE write with its metadata.

        The connector pushes the row's own `content`, so a pass that enriched only the file on disk
        (or only the payload) would be invisible to the next run: `--refresh` re-reads this row and
        would push the unlinked body again. Content and metadata go together so the row can never
        say it has links the CMS does not hold.
        """
        self._call("PATCH", f"{ARTICLES_TABLE}?id=eq.{row_id}",
                   {"content": content, "metadata": dict(metadata or {})}, {"Prefer": "return=minimal"})


# ─────────────────────────────────────────────────────────────────────────────
# markdown -> HTML (the destinations store HTML in post_content)
# ─────────────────────────────────────────────────────────────────────────────

def reader_markdown(markdown: str) -> str:
    """Strip frontmatter and the pipeline's internal sections — the same cuts the site's
    readerBody() makes, so the CMS holds what a reader is meant to see.

    The non-reader blocks (the `<!-- linkedin -->` social variant, the machine `<!-- schema -->`)
    are dropped as BOUNDED regions — the marker up to the next marker — not by truncating
    everything after them. Truncating silently deleted whatever the artifact wrote later in the
    file, and the internal-link block legitimately sits at the end in some artifacts (verified on
    published/2026-09-21_mcp-skills-extension.md, where it was dropped for exactly that reason).
    """
    body = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", markdown or "", flags=re.S)
    for marker in ("<!-- linkedin -->", "<!-- schema -->"):
        body = _drop_marker_block(body, marker)
    body = re.split(r"^##\s+Gate report\s*$", body, flags=re.M)[0]
    body = re.sub(r"^\s*<!--.*?-->\s*$", "", body, flags=re.M)
    return body.strip()


def _drop_marker_block(text: str, marker: str) -> str:
    """Remove one non-reader block: `marker` through the line before the next marker (or EOF)."""
    index = text.find(marker)
    if index == -1:
        return text
    start = index + len(marker)
    following = re.search(r"^[ \t]*<!--", text[start:], re.M)
    end = start + following.start() if following else len(text)
    return text[:index] + text[end:]


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
    # A previous push recorded the featured image's attachment id. Sending it keeps a --refresh or a
    # dry run honest about what the post will carry; push_one replaces it with the id it resolves.
    recorded_media = (metadata.get(WORDPRESS) or {}).get("media_id")
    if recorded_media:
        try:
            payload["featured_media"] = int(recorded_media)
            notes.append(f"featured media {int(recorded_media)} (recorded by a previous push)")
        except (TypeError, ValueError):
            notes.append(f"metadata.{WORDPRESS}.media_id is not a number ({recorded_media!r}) — "
                         f"re-uploading the image rather than sending an id the CMS cannot accept")
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


def internal_link_count(content: str, site_domain: str) -> int:
    """Links in a rendered body that point at the article's own site — the reader-visible internal
    links. Counted on the rendered HTML because that is what the reader and a crawler see."""
    if not site_domain:
        return 0
    host = re.escape(site_domain.split("/")[0].strip().lower())
    return len(re.findall(r'href=["\']https?://(?:www\.)?' + host + r'(?=[/"\':])', content or "", re.I))


def delivery_problems(payload: dict, post: dict, site_domain: str | None = None) -> list[str]:
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

    # Internal links are the one part of the body whose absence is invisible in a diff of lengths:
    # a sanitizer, an editor or a plugin can drop the Related reading section on save, and the post
    # still looks complete. Compare the reader-visible same-site link count. (Zero on both sides is
    # not a delivery failure — it is a content gap, reported by scripts/internal_links.py, which
    # refuses to invent a link to fill it.)
    if site_domain:
        sent_links = internal_link_count(sent_content, site_domain)
        stored_links = internal_link_count(stored_content, site_domain)
        if sent_links != stored_links:
            problems.append(f"internal links: sent {sent_links} link(s) to {site_domain}, CMS holds "
                            f"{stored_links} — the reader would get {stored_links}")

    sent_status = payload.get("status")
    if stored_post_id and sent_status and str(post.get("status") or "") not in (
            "draft", "pending", "private", ""):
        problems.append(f"status: the post came back {post.get('status')!r}, not draft — "
                        f"publishing must stay a human step in the CMS")

    # The featured image is a separate object; a post whose featured_media came back 0 (or dropped)
    # renders with no header at all, which no post-field comparison would catch.
    sent_media = payload.get("featured_media")
    if sent_media:
        stored_media = post.get("featured_media")
        if str(stored_media or "") != str(sent_media):
            problems.append(f"featured image: sent media {sent_media}, CMS holds {stored_media!r} — "
                            f"the post would render without its header")
    return problems


def verification_summary(payload: dict, post: dict, site_domain: str | None = None) -> str:
    """A one-line description of what a successful read-back verified."""
    content = payload.get("content") or ""
    featured = f", featured media {payload['featured_media']}" if payload.get("featured_media") else ""
    links = f", {internal_link_count(content, site_domain)} internal link(s)" if site_domain else ""
    return (f"title, {len(_plain_text(payload.get('excerpt')))}-char excerpt, "
            f"{len(_ld_blocks(content))} JSON-LD block(s), "
            f"{len(re.findall(r'<svg', content, re.I))} inline SVG(s), "
            f"{len(content)} chars of body{links}{featured}")


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

    def upsert(self, payload: dict, existing: dict | None = None) -> tuple[dict, str]:
        existing = existing if existing is not None else self.find_by_slug(payload["slug"])
        if existing:
            if str(existing.get("status") or "") == "publish":
                # A published post is a published post: refreshing its body must not send
                # status=draft, which would take a live article off the site (the approval gate was
                # already passed by a human — this is not a second flip, and it is not an unpublish).
                live = {k: v for k, v in payload.items() if k != "status"}
                _, post = self._call("POST", f"posts/{existing['id']}", live)
                return post or {}, f"updated ({LIVE_POST_NOTE})"
            _, post = self._call("POST", f"posts/{existing['id']}", payload)
            return post, "updated"
        _, post = self._call("POST", "posts", payload)
        return post, "created"

    # ── media library (the featured image's home) ────────────────────────────
    #
    # The featured image is not sent in the post body: WordPress stores it as an attachment and the
    # post carries its id in `featured_media`. So a push is two writes (media, then post) and the
    # image's public URL only exists after the first one — which is why the id is recorded in
    # metadata.wordpress and reused on every later push instead of re-uploading the same bytes.

    def media(self, media_id) -> dict | None:
        """One attachment by id, or None when the CMS no longer holds it (deleted in wp-admin)."""
        try:
            _, item = self._call("GET", f"media/{int(media_id)}?_fields=id,slug,source_url,alt_text,"
                                        f"caption,title,post,media_type,mime_type")
        except RuntimeError as exc:
            if "HTTP 404" in str(exc) or "rest_post_invalid_id" in str(exc):
                return None
            raise
        return item or None

    def find_media(self, slug: str) -> dict | None:
        """The attachment whose slug matches — `slug` here is the media slug, not the post slug.

        WordPress derives an attachment's slug from its filename, so `<article-slug>-featured` is a
        stable idempotency key for the image across pushes.
        """
        _, items = self._call("GET", f"media?slug={urllib.parse.quote(slug)}&per_page=1"
                                     f"&_fields=id,slug,source_url,alt_text,caption,title,post")
        return (items or [None])[0]

    def upload_media(self, filename: str, blob: bytes, content_type: str,
                     meta: dict | None = None) -> dict:
        """Upload one image as an attachment. WordPress needs the binary as the raw body."""
        url = f"{self.base}/wp-json/wp/v2/media"
        headers = {"Authorization": self.auth,
                   "Content-Type": content_type or "application/octet-stream",
                   "Content-Disposition": f'attachment; filename="{filename}"',
                   "Accept": "application/json"}
        req = urllib.request.Request(url, data=blob, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                created = json.loads(response.read().decode("utf-8", "replace") or "{}")
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")[:400]
            raise RuntimeError(f"WordPress POST media ({filename}, {len(blob)} bytes) -> "
                               f"HTTP {exc.code}: {detail}") from None
        if meta:
            created = {**created, **(self.update_media(created.get("id"), meta) or {})}
        return created

    def update_media(self, media_id, meta: dict) -> dict | None:
        """Set the attachment's alt text / caption / title. Idempotent: a no-op change is a POST."""
        if not media_id:
            return None
        _, item = self._call("POST", f"media/{int(media_id)}", meta)
        return item or None


# ─────────────────────────────────────────────────────────────────────────────
# featured image — scripts/illustration_creator.py stages it, this uploads it
# ─────────────────────────────────────────────────────────────────────────────

MEDIA_TYPES = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp"}


def illustration_record(row: dict) -> dict:
    """The art direction recorded on the row (metadata.illustration); {} for articles illustrated
    before this step existed."""
    return ((row.get("metadata") or {}).get("illustration") or {})


def staged_illustration(slug: str) -> tuple[dict, str]:
    """(record, note) — the brief committed beside the image, for a row that does not carry one.

    `metadata.illustration` is written by the persistence pass, so an article illustrated *after* it
    was published (the sweep in scripts/cron-wp-drafts.sh generates images for artifacts that have
    none) has a brief on disk and nothing on its row. Without this lookup the sweep would generate an
    image and then push the draft without it — the exact silent outcome the step exists to prevent.
    The note is returned so the push says which source it used.
    """
    if not slug:
        return {}, ""
    path = ROOT / "context" / "assets" / "illustrations" / slug / "featured.json"
    if not path.is_file():
        return {}, ""
    try:
        record = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return {}, f"staged brief at {path} is unreadable ({exc}) — pushing without a featured image"
    return record, f"the brief committed at context/assets/illustrations/{slug}/featured.json " \
                   f"(the row carries no metadata.illustration)"


def illustration_file(record: dict) -> pathlib.Path | None:
    """The staged image on THIS host, or None.

    The binary is deliberately not committed (see .gitignore): the CMS media library is the image's
    canonical home, and the staged file is only the upload's source. So a push that cannot find the
    file has to say so — pushing the post without a featured image and without a word is exactly the
    silent degradation the third surgical rule forbids.
    """
    candidates = []
    if record.get("local_path"):
        candidates.append(ROOT / str(record["local_path"]))
    slug = str(record.get("slug") or "")
    if slug:
        candidates += sorted((ROOT / "context" / "assets" / "illustrations" / slug).glob("featured.*"))
    for path in candidates:
        if path.is_file() and path.suffix.lower() in MEDIA_TYPES:
            return path
    return None


def media_meta(record: dict, slug: str) -> dict:
    """The attachment's CMS fields: the reader-facing alt/caption plus how the image was made."""
    credit = record.get("credit") or ""
    provenance = " · ".join(str(x) for x in (record.get("style_label"), record.get("model")) if x)
    description = f"{credit} ({provenance})" if credit and provenance else (credit or provenance)
    return {"title": record.get("title") or f"{slug} featured image",
            "alt_text": record.get("alt_text") or "",
            "caption": record.get("caption") or "",
            "description": description}


def ensure_featured_media(wp, slug: str, record: dict, notes: list, *, path=None,
                          recorded_id=None) -> dict | None:
    """Upload or re-find the article's featured image and make sure the CMS carries its metadata.

    Idempotency is the media SLUG (`<article-slug>-featured`, derived from the filename WordPress
    stores), backed by the id recorded in metadata.wordpress — so a re-push reuses the attachment
    instead of adding a second copy of the same bytes to the library, which is what happens when a
    connector simply posts the file again.
    """
    path = path or illustration_file(record)
    if path is None:
        notes.append(f"no featured image staged for {slug} "
                     f"(looked for {record.get('local_path') or 'context/assets/illustrations/' + slug}) "
                     f"— run `python3 scripts/illustration_creator.py <artifact> --apply` on this host; "
                     f"pushing the draft without one")
        return None
    filename = f"{slug}-featured{path.suffix.lower()}"
    media_slug = pathlib.Path(filename).stem
    meta = media_meta(record, slug)

    item = wp.media(recorded_id) if recorded_id else None
    action = "reused (the id recorded on the row)"
    if item is None:
        item = wp.find_media(media_slug)
        action = "reused (media slug match)"
    if item is None:
        item = wp.upload_media(filename, path.read_bytes(), MEDIA_TYPES[path.suffix.lower()])
        action = "uploaded"
    if not item or not item.get("id"):
        raise RuntimeError(f"WordPress returned no attachment id for {filename}")
    stale = {k: v for k, v in meta.items() if _field_text(item.get(k)) != _field_text(v)}
    if stale:
        item = {**item, **(wp.update_media(item.get("id"), stale) or {})}
        action += f" + set {', '.join(sorted(stale))}"
    notes.append(f"featured image {action}: media {item.get('id')} ({filename}, "
                 f"{path.stat().st_size // 1024} KB, {path.stat().st_size} bytes)")
    return item


def _field_text(value) -> str:
    """A CMS text field as reader-visible text, whether it came back as a string or as the
    `{raw, rendered}` object WordPress returns for `title`/`caption` on media and posts.

    Comparing the raw value against what was sent is the false positive this avoids: a correct
    push reads back as `{'rendered': 'Macro plastic resin pellets'}` and would be reported as
    'the CMS does not hold what was sent' on every single push.
    """
    if isinstance(value, dict):
        value = value.get("raw") or value.get("rendered") or ""
    return _plain_text(value)


def media_problems(expected: dict, item: dict) -> list[str]:
    """Compare the attachment fields that were sent against what the CMS holds.

    Alt text is the one that matters most: it is what a screen reader announces, and WordPress
    silently drops an `alt_text` a lower-privilege application password is not allowed to set.
    """
    problems: list[str] = []
    for field in ("alt_text", "title", "caption"):
        sent = _field_text(expected.get(field))
        if not sent:
            continue
        if _field_text((item or {}).get(field)) != sent:
            problems.append(f"media {field}: sent {sent[:60]!r}, CMS holds "
                            f"{_field_text((item or {}).get(field))[:60]!r}")
    return problems


# ─────────────────────────────────────────────────────────────────────────────
# driver
# ─────────────────────────────────────────────────────────────────────────────

def push_one(row: dict, db, *, dry_run: bool = False, publisher_name: str | None = None,
             author_name: str | None = None, wp_factory=None, verify: bool = True,
             live_ok: bool = False) -> dict:
    metadata = row.get("metadata") or {}
    vertical = metadata.get("vertical") or (row.get("tags") or [""])[0]
    if not vertical:
        raise RuntimeError(f"row {row.get('id')} has no vertical — cannot route it to a site")
    site = db.site_for(vertical)
    slug = (metadata.get("slug") or "").strip()

    # Two things are needed before this run can decide to enrich the row's body: the WordPress client
    # and the record of what the CMS already holds for this slug. A post a human already published is
    # not a draft, and a refresh re-derives title/excerpt/body from the row — so rewriting a live
    # article is an explicit decision (--refresh-live), never a side effect of the routine sweep.
    wp = None
    existing = None
    if not dry_run:
        user, password = credentials_for(site["site_domain"])
        wp = (wp_factory or (lambda base, u, p: WordPress(base, u, p)))(site["cms_base_url"], user, password)
        existing = wp.find_by_slug(slug) if slug else None
        if existing and str(existing.get("status") or "") == "publish" and not live_ok:
            print(f"\n  skipped: {site['site_domain']} holds '{slug}' as a PUBLISHED post "
                  f"({existing.get('id')}) — a refresh re-derives its body from the row and can "
                  f"overwrite what an editor tuned; pass --refresh-live to update it deliberately")
            return {"status": "skipped (live post)", "site": site["site_domain"],
                    "post_id": existing.get("id"), "verified": None, "problems": [], "skipped": True,
                    "edit_url": f"{site['cms_base_url']}/wp-admin/post.php?post={existing.get('id')}"
                                f"&action=edit"}

    # Internal links first: they are part of the body that goes to the CMS, and the row this run
    # pushes is the one the next run reads (scripts/internal_links.py). Best-effort — an article
    # with no links is a worse article, an article that never reached the CMS is a missing one.
    links_notes: list[str] = []
    try:
        import internal_links as il
        row, links_notes = il.ensure_for_row(
            row, persist=not dry_run, db=db, max_links=LINK_LINKS_MAX,
            site_domain=site.get("site_domain"))
    except Exception as exc:                       # noqa: BLE001 - surface, never swallow (rule 6)
        links_notes = [f"internal links NOT generated: {exc}"]
        print(f"  internal links NOT generated: {exc}", file=sys.stderr)

    metadata = row.get("metadata") or {}          # re-read: the links pass rewrote it
    payload, notes = build_payload(row, site, publisher_name, author_name)
    notes = links_notes + notes

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

    # The featured image goes up BEFORE the post: the payload carries the attachment id and
    # WordPress will not accept one that does not exist yet. A failure here is reported and the
    # draft is still pushed — an article with no featured image is recoverable by the next sweep,
    # an article that never reached the CMS is not.
    illustration = illustration_record(row)
    if not illustration:
        illustration, staged_note = staged_illustration(payload["slug"])
        if staged_note:
            notes.append(staged_note)
            print(f"  featured: {staged_note}")
    recorded_media = (metadata.get(WORDPRESS) or {}).get("media_id")
    media = None
    media_failure = ""
    media_expected: dict = {}
    if illustration or recorded_media:
        try:
            media = ensure_featured_media(wp, payload["slug"], illustration, notes,
                                          recorded_id=recorded_media)
        except Exception as exc:                       # noqa: BLE001 - surface, never swallow (rule 6)
            media_failure = str(exc)
            notes.append(f"featured image FAILED: {media_failure}")
            print(f"  featured image FAILED: {media_failure}", file=sys.stderr)
        if media:
            payload["featured_media"] = media.get("id")
            media_expected = media_meta(illustration, payload["slug"])
            print(f"  featured: media {media.get('id')} — {media.get('source_url') or 'no url returned'}")

    if payload.get("categories"):
        category_id = payload["categories"][0]
        print(f"  category: {category_id} — {html.unescape(wp.category_name(category_id))} "
              f"(validated on {site['site_domain']})")
    post, action = wp.upsert(payload, existing=existing)
    # For an existing LIVE post the status was deliberately not sent (see upsert), so what was sent
    # is the payload minus its status — compare the read-back against that, not against the draft
    # intent we started from.
    sent_payload = ({k: v for k, v in payload.items() if k != "status"}
                    if LIVE_POST_NOTE in action else payload)
    print(f"  {action}: post {post.get('id')} ({post.get('status')}) {post.get('link')}")

    # Attach the image to the post in the library (post_parent), so an editor looking at the article
    # finds its header image filed under it rather than loose in the media list.
    if media and str(media.get("post") or "") != str(post.get("id")):
        try:
            wp.update_media(media.get("id"), {"post": post.get("id")})
        except Exception as exc:                       # noqa: BLE001 - reported, never fatal
            print(f"  featured image not attached to the post in the library: {exc}", file=sys.stderr)

    # Read the post back. A 201 says the request was accepted, not that the CMS kept what was sent:
    # sanitizers, plugins and editors are all free to strip a <script> or an inline <svg> on save,
    # which is exactly the failure a push-only connector cannot see. Reported, never assumed.
    problems: list[str] = [media_failure] if media_failure else []
    summary = ""
    if verify:
        try:
            stored = wp.read_back(post.get("id"))
            problems += delivery_problems(sent_payload, stored, site["site_domain"])
            if media:
                stored_media = wp.media(media.get("id")) or {}
                problems += media_problems(media_expected, stored_media)
            if problems:
                print("  DELIVERY VERIFICATION FAILED — the CMS does not hold what was sent:")
                for problem in problems:
                    print(f"    - {problem}")
            else:
                summary = verification_summary(sent_payload, stored, site["site_domain"])
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
        "internal_links": internal_link_count(payload["content"], site["site_domain"]),
        "verified": not problems,
    }
    if media:
        # Recorded so the next push reuses this attachment (no duplicate bytes in the library) and
        # so the image can be found again by hand from the Supabase row alone.
        record.update({"featured_media": payload.get("featured_media"),
                       "media_id": media.get("id"),
                       "media_url": media.get("source_url"),
                       "media_alt": media_expected.get("alt_text")})
    if illustration and not illustration_record(row):
        # The brief came from disk (the sweep generated this image after the article was published),
        # so write it onto the row now: from here on the row is self-describing and the next push
        # reads it from Supabase like any other. Same field the persistence pass maintains.
        metadata = {**metadata, "illustration": illustration}
    db.record_push(row["id"], metadata, record)
    print(f"  recorded metadata.{WORDPRESS} on the Supabase row ({row['id']})")
    return {"status": action, "site": site["site_domain"], "post_id": post.get("id"),
            "edit_url": record["edit_url"], "verified": not problems, "problems": problems,
            "media_id": record.get("media_id"), "summary": summary}


def push_by_slug(slug: str, *, dry_run: bool = False, publisher_name: str | None = None,
                 author_name: str | None = None, wp_factory=None, db=None,
                 verify: bool = True, live_ok: bool = False) -> dict:
    """Push one article by its Supabase slug. The single entry point used by both this CLI and
    scripts/publish.py, so the in-run hook and a manual re-run share one code path."""
    db = db or Supabase(*supabase_config())
    rows = db.articles(slug=slug)
    if not rows:
        raise RuntimeError(f"no row in public.{ARTICLES_TABLE} with metadata.slug '{slug}'")
    return push_one(rows[0], db, dry_run=dry_run, publisher_name=publisher_name,
                    author_name=author_name, wp_factory=wp_factory, verify=verify, live_ok=live_ok)


def main() -> int:
    parser = argparse.ArgumentParser(description="Push generated articles to their vertical's WordPress CMS as drafts")
    parser.add_argument("--slug", help="Article slug (metadata->>slug)")
    parser.add_argument("--all", action="store_true", help="Every row with no metadata.wordpress.post_id yet")
    parser.add_argument("--refresh", action="store_true",
                        help="Every row, pushed or not: re-apply the current mapping (category, "
                             "excerpt, chart, JSON-LD, internal links) to the drafts that already "
                             "exist. Updates the same post per slug — use after a routing or content "
                             "change")
    parser.add_argument("--refresh-live", action="store_true",
                        help="With --refresh/--slug: also update posts that are already PUBLISHED "
                             "(their status is never sent, so they stay live). Off by default: a "
                             "refresh re-derives the body from the row and can overwrite what an "
                             "editor tuned in the CMS")
    parser.add_argument("--limit", type=int, default=None,
                        help="Max articles to push in one run (default 1, or all with --refresh)")
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

    if not args.slug and not args.all and not args.refresh:
        parser.error("pass --slug <slug>, --all or --refresh")

    limit = args.limit if args.limit is not None else (None if args.refresh else 1)
    db = Supabase(*supabase_config())

    if args.slug:
        try:
            result = push_by_slug(args.slug, dry_run=args.dry_run, publisher_name=args.publisher_name,
                                  author_name=args.author_name, db=db, verify=not args.no_verify,
                                  live_ok=args.refresh_live)
        except Exception as exc:                       # rule 6: surface it, never a silent skip
            print(f"\n  FAILED {args.slug}: {exc}", file=sys.stderr)
            return 1
        if result.get("problems"):
            print("\n  the draft exists, but the CMS does not hold what was sent (see above) — "
                  "fix the mapping and re-run; the slug is the idempotency key, so this updates "
                  "the same post rather than duplicating it", file=sys.stderr)
            return 1
        if result.get("skipped"):
            return 0
        print("\npushed: 1/1 | drafts only — publishing stays a human step in the CMS")
        return 0

    rows = db.articles(un_pushed_only=not args.refresh, limit=limit)
    if not rows:
        print("Nothing to push (every row already has a draft in its CMS)."
              if not args.refresh else "No rows to refresh.")
        return 0

    failures = 0
    skipped = 0
    for row in rows:
        try:
            result = push_one(row, db, dry_run=args.dry_run, publisher_name=args.publisher_name,
                              author_name=args.author_name, verify=not args.no_verify,
                              live_ok=args.refresh_live)
            if result.get("skipped"):
                skipped += 1
            elif result.get("problems"):
                failures += 1
        except Exception as exc:                       # rule 6: surface it, never a silent skip
            failures += 1
            print(f"\n  FAILED {row.get('title')}: {exc}", file=sys.stderr)

    tail = f" | {skipped} live post(s) left alone (--refresh-live to update them)" if skipped else ""
    print(f"\npushed: {len(rows) - failures - skipped}/{len(rows)} | drafts only — publishing stays a "
          f"human step in the CMS{tail}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
