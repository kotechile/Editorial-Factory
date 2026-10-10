#!/usr/bin/env python3
"""Publishing engine for the Editorial Factory.

Handles:
1. Parsing approved draft markdown (frontmatter, sections, sources).
2. Unconditional persistence to `published/YYYY-MM-DD_<slug>.md`.
3. Logging to `context/published_log.md` with the reader URL and any external URLs.
4. Persistence to Supabase (articles, sources, live URLs) when configured.
5. The art-directed featured image and the derived SEO assets (`scripts/article_assets.py`).
6. Automatic WordPress post creation in the destination CMS for the article's vertical
   (scripts/wp_draft.py) with status 'publish' so the article is live immediately.

There is no outbound social distribution step: the LinkedIn and Reddit channels were removed
by the owner (2026-10-06). The reader sites (giniloh.com / wellroost.com, fed by the CMS) are
the destination.

Usage:
  python3 scripts/publish.py context/drafts/YYYY-MM-DD_<slug>_final.md --article-url "https://site.com/post"
  python3 scripts/publish.py --interactive context/drafts/YYYY-MM-DD_<slug>_final.md
  python3 scripts/publish.py --dry-run context/drafts/YYYY-MM-DD_<slug>_final.md
"""

import argparse
import datetime
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO_ROOT, "scripts"))
import article_assets  # noqa: E402  (derived SEO metadata + charts, artifact-local)
import illustration_creator  # noqa: E402  (art-directed featured image + its metadata)

_SCHEMA_MARKER = re.compile(r"<!--\s*schema\s*-->(.*)", re.S | re.IGNORECASE)


def _schema_block(body: str) -> tuple[dict | None, str, tuple[int, int] | None]:
    """Locate the artifact's JSON-LD block: (schema, note, (start, end) of the whole block).

    Both of the generator's styles are accepted — a ```json fence and a bare object — because a
    fenced-only pattern silently dropped a real block: the mcp-skills-extension artifact carries an
    unfenced JSON-LD object after the marker (published/2026-09-21_mcp-skills-extension.md:79) and
    its Supabase row has no `metadata.seo.schema` at all, so nothing reached the CMS. A marker with
    no JSON after it (the marker is written even when the block is not — see
    published/2026-09-24_maskills-*.md) is reported rather than swallowed, and a block that does not
    parse is reported rather than replaced: an invented node is worse than no node.
    """
    match = _SCHEMA_MARKER.search(body or "")
    if not match:
        return None, "no `<!-- schema -->` block in the artifact — nothing captured (never invented)", None

    rest = match.group(1)
    lead = len(rest) - len(rest.lstrip())
    text_start = match.start(1) + lead
    body_from_text = rest[lead:]

    fenced = re.match(r"```(?:json)?\s*(.*?)\s*```", body_from_text, re.S)
    if fenced:
        candidate, block_end = fenced.group(1), text_start + fenced.end()
    elif body_from_text.startswith("{"):
        # Brace-match the object so trailing prose / gate-report lines are not dragged into the parse.
        depth, end, in_str, escaped = 0, None, False, False
        for index, char in enumerate(body_from_text):
            if in_str:
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == '"':
                    in_str = False
                continue
            if char == '"':
                in_str = True
            elif char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    end = index + 1
                    break
        if end is None:
            return None, "schema marker found but its JSON object never closes — nothing captured", None
        candidate, block_end = body_from_text[:end], text_start + end
    else:
        following = (body_from_text.strip().splitlines() or ["(end of file)"])[0][:60]
        return None, (f"schema marker present but no JSON-LD block follows (next line: {following!r}) "
                      f"— a marker alone is not schema, nothing captured"), None

    try:
        parsed = json.loads(candidate)
    except Exception as exc:                       # noqa: BLE001 - reported, never substituted
        return None, f"schema block did not parse as JSON ({exc}) — nothing captured (never invented)", None
    if not isinstance(parsed, dict):
        return None, f"schema block parsed to {type(parsed).__name__}, not an object — ignored", None

    nodes = parsed.get("@graph") if isinstance(parsed.get("@graph"), list) else [parsed]
    types = ", ".join(str(node.get("@type")) for node in nodes if isinstance(node, dict))
    return parsed, f"schema JSON-LD captured ({types or 'no @type'})", (match.start(), block_end)


def extract_schema_json(body: str) -> tuple[dict | None, str]:
    """The JSON-LD graph the artifact carries, as (schema, note)."""
    schema, note, _ = _schema_block(body)
    return schema, note


def strip_schema_block(body: str) -> str:
    """Drop the machine-readable schema block from the reader-facing body (fenced OR bare).

    The reader must never receive the JSON-LD as prose: only a fenced block used to be stripped, so
    a bare object — the style the SEO machine writes — would have shipped as visible text on the
    reader page.
    """
    _schema, _note, span = _schema_block(body)
    if not span:
        return body
    return (body[:span[0]] + body[span[1]:]).strip()


def apply_derived_assets(content: str) -> tuple[str, list[str]]:
    """Add the derived SEO metadata (frontmatter) and an inline chart (body) to an artifact.

    The drafting stage is an LLM: it emits `meta_title` / `meta_description` only on the SEO path,
    and never emits a visual. Both are DERIVED from the artifact's own text here (the headline, the
    lead paragraph, the `**By the numbers:**` percentages) so every destination gets them without a
    research step that could invent anything. Idempotent — a value or a chart already present wins,
    including the drafting stage's own. Every decision is reported, never applied silently.
    """
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n*", content, re.S)
    fm_text, body = (match.group(1), content[match.end():]) if match else ("", content)

    existing = {}
    for line in fm_text.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            existing[key.strip()] = value.strip().strip('"').strip("'")

    enriched, notes = article_assets.ensure_seo_metadata(dict(existing), body)
    additions = {k: v for k, v in enriched.items() if k not in existing}
    # The chart is injected into the BODY, which is the frontmatter-less half of the artifact — so
    # the artifact's own headline has to be handed over explicitly. Without it `_chart_title` found
    # no title and captioned every pipeline-generated chart "Verified figures" (a heading that
    # describes nothing), and that caption is what reached the CMS.
    chart_title = enriched.get("meta_title") or enriched.get("title") or existing.get("title")
    body, chart_note = article_assets.inject_chart(body, title=chart_title)
    notes.append(chart_note)

    fm_lines = fm_text.rstrip("\n")
    for key, value in additions.items():
        fm_lines += f'\n{key}: "{str(value).replace(chr(34), chr(92) + chr(34))}"'
    rebuilt = f"---\n{fm_lines}\n---\n\n{body.lstrip(chr(10))}" if match else body

    if rebuilt == content:
        return content, [f"{note} (already present)" for note in notes]
    return rebuilt, notes


def parse_bool_env(var_name: str, default: bool = False) -> bool:
    val = os.environ.get(var_name, "").strip().lower()
    if not val:
        return default
    return val in ("1", "true", "yes", "on", "enable", "enabled")


def apply_illustration(content: str, enabled: bool = True, *, pinned_style: str | None = None,
                       pinned_model: str | None = None) -> tuple[str, list[str], dict | None]:
    """Commission the article's featured image and its metadata (scripts/illustration_creator.py).

    Runs inside the persistence pass because the image is part of what is persisted: the artifact
    carries the image fields, the Supabase row carries metadata.illustration, and the CMS push
    uploads it. It is idempotent by content — an article whose text is unchanged re-uses the image
    it already has. A failure is reported and the article still publishes: a missing header image
    is recoverable by the host sweep (`scripts/cron-wp-drafts.sh` re-runs this before pushing),
    whereas an article held back for it is not.
    """
    if not enabled:
        return content, ["featured image: skipped (dry-run, --no-illustration, or "
                         "ILLUSTRATION_ENABLED=false)"], None
    # The asset directory is keyed by the BARE slug — the same one the published filename and the
    # Supabase row use — so a frontmatter slug that still carries its date prefix cannot file the
    # image under a slug nothing else knows.
    header = dict(re.findall(r"^(slug|date):[ \t]*\"?([^\"\n]+?)\"?[ \t]*$", content, re.M))
    bare_slug = normalize_slug(header.get("slug"), header.get("date")) or None
    try:
        content, notes, meta = illustration_creator.ensure_illustration(
            content, slug=bare_slug,
            pinned_style=pinned_style, pinned_model=pinned_model)
        if bare_slug:
            try:
                import illustration_overlay
                ov = illustration_overlay.apply_to_slug(bare_slug, article_md=content)
                anchor = ov.get("placement", {}).get("anchor") or ov.get("anchor") or "placed"
                notes.append(f"typography overlay applied ({anchor})")
                side = illustration_creator.read_sidecar(bare_slug)
                if side:
                    content = illustration_creator._write_frontmatter(content, illustration_creator.frontmatter_fields(side))
                    meta = illustration_creator.supabase_metadata(side)
            except Exception as ov_err:
                notes.append(f"typography overlay note: {ov_err}")
        return content, notes, meta
    except Exception as exc:                            # noqa: BLE001 - surfaced, never swallowed
        return content, [f"featured image FAILED: {exc} — publishing without one; re-run "
                         f"`python3 scripts/illustration_creator.py <artifact> --apply`"], None


def apply_internal_links(content: str, enabled: bool = True) -> tuple[str, list[str]]:
    """Fill the artifact's reader-facing internal links (scripts/internal_links.py).

    Runs in the persistence pass, next to the derived metadata and the chart, because the links are
    part of what is persisted: the published file, the Supabase row's `content` and the CMS draft
    must carry the same body. Nothing here is invented — the candidates are the pages that are
    actually live on the destination site (each frontend's sitemap decides that, not an HTTP 200,
    because both Astro fronts answer 200 with the homepage for an unknown URL). When no page
    qualifies the section is absent and the reason is printed.

    Idempotent by construction (the generated block is delimited and replaced in place), and a
    failure is reported rather than fatal: an article without internal links is a worse article,
    an article that never got persisted is a missing one.
    """
    if not enabled:
        return content, ["internal links: skipped (dry-run or --no-links)"]
    header = dict(re.findall(r"^(vertical|title):[ \t]*\"?([^\"\n]+?)\"?[ \t]*$", content, re.M))
    try:
        import internal_links as il
        enriched, notes, _links = il.enrich(content, vertical=header.get("vertical", ""))
        return enriched, notes
    except Exception as exc:                            # noqa: BLE001 - surfaced, never swallowed
        return content, [f"internal links FAILED: {exc} — publishing without them; re-run "
                         f"`python3 scripts/internal_links.py <artifact> --apply`"]


def parse_draft(file_path: str, illustrate: bool = True, pinned_style: str | None = None,
                pinned_model: str | None = None, links: bool = True):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Derived assets first: the frontmatter's meta_title/meta_description and the inline chart are
    # filled from the artifact's own text (scripts/article_assets.py) before anything reads them, so
    # the published file, the Supabase row and the CMS draft all carry one version. Idempotent and
    # reported — see apply_derived_assets.
    content, asset_notes = apply_derived_assets(content)
    for note in asset_notes:
        print(f"  [assets] {note}")

    # Then the internal links — reader-facing body, derived from the sites' real live corpus
    # (scripts/internal_links.py) rather than left to the drafting stage, which is an LLM with no
    # list of live pages (verified: every artifact it produced carried an empty block and every CMS
    # draft reached the reader with zero internal links, while the hand-written back catalogue
    # carried 2-10 each).
    content, links_notes = apply_internal_links(content, links)
    for note in links_notes:
        print(f"  [links] {note}")

    # Then the visual: art direction + generation, from the same text (scripts/illustration_creator.py).
    content, image_notes, illustration_meta = apply_illustration(
        content, illustrate, pinned_style=pinned_style, pinned_model=pinned_model)
    for note in image_notes:
        print(f"  [image] {note}")

    # Parse YAML frontmatter if present
    frontmatter = {}
    body_content = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            body_content = parts[2].strip()
            for line in fm_text.strip().splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    frontmatter[k.strip()] = v.strip().strip('"').strip("'")

    # Extract headline/title
    title = frontmatter.get("title")
    if not title:
        title_match = re.search(r"^#\s+(.+)$", body_content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else os.path.basename(file_path)

    slug = frontmatter.get("slug")
    if not slug:
        base = os.path.basename(file_path).replace("_final.md", "").replace("_draft.md", "").replace(".md", "")
        # Strip leading date if present (YYYY-MM-DD_)
        slug = re.sub(r"^\d{4}-\d{2}-\d{2}_", "", base)

    vertical = frontmatter.get("vertical", "general")
    persona = frontmatter.get("persona", "general")
    date_str = frontmatter.get("date", datetime.date.today().isoformat())
    article_url = frontmatter.get("article_url", "")
    promo_url = frontmatter.get("promo_url", "")
    promo_label = frontmatter.get("promo_label", "")

    # Everything before the `<!-- linkedin -->` marker is the article. That marker held the
    # authored social variant, which nothing produces or posts any more (the LinkedIn/Reddit
    # channels were removed by the owner on 2026-10-06); artifacts written before that still
    # carry it, and it is the desk's internal copy, so it is cut here the same way the
    # `## Gate report` below is — never into the reader's copy, never into a row.
    linkedin_marker = re.search(r"<!--\s*linkedin\s*-->", body_content, re.IGNORECASE)
    body_article = (body_content[:linkedin_marker.start()] if linkedin_marker else body_content).strip()

    # Cleanly strip machine-readable schema, internal-links hints, and gate reports from body_article
    body_article = strip_schema_block(body_article)
    # Operator-facing HTML comments (section markers, internal-link placement hints) are machinery.
    # The reader-facing `## Related reading` links are article body and must survive this.
    body_article = re.sub(r"^\s*<!--.*?-->\s*$", "", body_article, flags=re.M).strip()
    body_article = re.sub(r"##\s*Gate report[\s\S]*$", "", body_article, flags=re.IGNORECASE).strip()

    # Extract Sources
    sources = []
    sources_match = re.search(r"## Sources\s*(.+)", body_article, re.DOTALL | re.IGNORECASE)
    if sources_match:
        sources_text = sources_match.group(1).strip()
        for s in re.finditer(r"\[(\d+)\]\s*([^\[\n]+)", sources_text):
            sources.append({"index": int(s.group(1)), "citation": s.group(2).strip()})

    # Extract SEO fields from frontmatter
    primary_keyword = frontmatter.get("primary_keyword", "")
    secondary_raw = frontmatter.get("secondary_keywords", "")
    secondary_keywords = []
    if secondary_raw:
        if secondary_raw.startswith("[") and secondary_raw.endswith("]"):
            try:
                secondary_keywords = json.loads(secondary_raw)
            except Exception:
                secondary_keywords = [k.strip().strip('"').strip("'") for k in secondary_raw[1:-1].split(",") if k.strip()]
        else:
            secondary_keywords = [k.strip().strip('"').strip("'") for k in secondary_raw.split(",") if k.strip()]

    search_volume = None
    if frontmatter.get("search_volume"):
        try:
            search_volume = int(frontmatter.get("search_volume"))
        except Exception:
            search_volume = frontmatter.get("search_volume")

    search_intent = frontmatter.get("search_intent", "")
    kd = None
    if frontmatter.get("keyword_difficulty") or frontmatter.get("kd"):
        try:
            kd = float(frontmatter.get("keyword_difficulty") or frontmatter.get("kd"))
        except Exception:
            kd = frontmatter.get("keyword_difficulty") or frontmatter.get("kd")

    cpc = None
    if frontmatter.get("cpc"):
        try:
            cpc = float(frontmatter.get("cpc"))
        except Exception:
            cpc = frontmatter.get("cpc")

    gsc_impressions = None
    if frontmatter.get("gsc_impressions"):
        try:
            gsc_impressions = int(frontmatter.get("gsc_impressions"))
        except Exception:
            gsc_impressions = frontmatter.get("gsc_impressions")

    meta_title = frontmatter.get("meta_title", "")
    meta_desc = frontmatter.get("meta_description", "")

    # Extract JSON-LD schema if present (fenced or bare — see extract_schema_json).
    schema_json, schema_note = extract_schema_json(body_content)
    print(f"  [schema] {schema_note}")

    status = "published" if "/published/" in os.path.abspath(file_path) else "draft"

    return {
        "title": title,
        "slug": slug,
        "vertical": vertical,
        "persona": persona,
        "date": date_str,
        "status": status,
        "file_path": str(file_path),
        "article_url": article_url,
        "promo_url": promo_url,
        "promo_label": promo_label,
        "primary_keyword": primary_keyword,
        "secondary_keywords": secondary_keywords,
        "search_volume": search_volume,
        "search_intent": search_intent,
        "keyword_difficulty": kd,
        "cpc": cpc,
        "gsc_impressions": gsc_impressions,
        "meta_title": meta_title,
        "meta_title_source": frontmatter.get("meta_title_source", ""),
        "meta_description": meta_desc,
        "meta_description_source": frontmatter.get("meta_description_source", ""),
        "schema": schema_json,
        "illustration": illustration_meta,
        "body_md": body_article,
        "sources": sources,
        "full_content": content,
    }


_COLUMNS_CACHE = None


def _articles_live_columns(supabase_url: str, service_key: str):
    """Return the set of column names currently present on public.articles.

    Probes live table via select=* (fast path) or candidate columns via PostgREST
    Cached per process. Returns None on total failure so callers fall back to
    metadata-only persistence safely.
    """
    global _COLUMNS_CACHE
    if _COLUMNS_CACHE is not None:
        return _COLUMNS_CACHE
    base = supabase_url.rstrip("/") + "/rest/v1/articles"
    # Fast path: 1 request
    try:
        req = urllib.request.Request(
            f"{base}?select=*&limit=1",
            headers={"apikey": service_key, "Authorization": f"Bearer {service_key}",
                     "Accept": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
                _COLUMNS_CACHE = set(data[0].keys())
                return _COLUMNS_CACHE
    except Exception:
        pass

    candidates = ["slug", "vertical", "headline", "body_md", "content", "title",
                  "source_url", "sources", "tags", "status", "live_urls", "metadata"]
    found = set()
    try:
        for col in candidates:
            req = urllib.request.Request(
                f"{base}?select={urllib.parse.quote(col)}&limit=1",
                headers={"apikey": service_key, "Authorization": f"Bearer {service_key}",
                         "Accept": "application/json"},
            )
            try:
                with urllib.request.urlopen(req, timeout=5) as resp:
                    found.add(col)
            except urllib.error.HTTPError as e:
                if e.code != 400:
                    raise
    except Exception as e:
        print(f"  [Supabase] Column introspection failed ({e}); using metadata-only.")
        return None
    _COLUMNS_CACHE = found
    return found


def sync_to_supabase(data: dict, live_urls: dict):
    """Persist an article to the shared factory-core Supabase 'public.articles' table.

    Writes to the rich columns (slug, vertical, headline, body_md, sources, status,
    live_urls, ...) when they exist on the table, and always keeps the editorial
    fields in the 'metadata' jsonb so the row is fully described regardless of schema.
    Idempotent on metadata->>'slug' — re-running does not create duplicates.
    """
    supabase_url = os.environ.get("SUPABASE_URL", "").rstrip("/")
    service_key = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")
    if not supabase_url or not service_key:
        print("  [Supabase] SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY not set. Skipping DB sync.")
        return False

    # First source URL (grounded citation) -> source_url column.
    source_url = ""
    for s in sorted(data.get("sources") or [], key=lambda x: x.get("index", 0)):
        m = re.search(r"https?://\S+", str(s.get("citation", "")))
        if m:
            source_url = m.group(0)
            break

    seo_metadata = {
        "primary_keyword": data.get("primary_keyword"),
        "secondary_keywords": data.get("secondary_keywords") or [],
        "search_volume": data.get("search_volume"),
        "search_intent": data.get("search_intent"),
        "keyword_difficulty": data.get("keyword_difficulty"),
        "cpc": data.get("cpc"),
        "gsc_impressions": data.get("gsc_impressions"),
        "meta_title": data.get("meta_title"),
        "meta_title_source": data.get("meta_title_source"),
        "meta_description": data.get("meta_description"),
        "meta_description_source": data.get("meta_description_source"),
        "schema": data.get("schema"),
    }
    # Clean empty values for clean JSON. The emptiness test is value-based, not None-based: an empty
    # list is falsy but not None, so `v is not None and v != ""` wrote `seo: {secondary_keywords: []}`
    # onto 10 of the 11 published rows — a `seo` object that looked populated and carried nothing.
    clean_seo = {k: v for k, v in seo_metadata.items() if v not in (None, "", [], {})}

    status = data.get("status") or ("published" if "/published/" in str(data.get("file_path", "")) else "draft")
    targets = ["published/"] if status == "published" else ["context/drafts/"]

    metadata = {
        "slug": data.get("slug"),
        "vertical": data.get("vertical"),
        "headline": data.get("title"),
        "sources": data.get("sources") or [],
        "status": status,
        "targets": targets,
        "live_urls": live_urls or {},
        "article_url": (data.get("article_url") or live_urls.get("article_url", "")) or None,
        "promo_url": (data.get("promo_url") or live_urls.get("promo_url", "")) or None,
    }
    if clean_seo:
        metadata["seo"] = clean_seo
    # The featured image's brief (scripts/illustration_creator.py): the CMS push reads the staged
    # image's path and the alt text/caption/credit from here, and it is the record of what the desk
    # decided and what it spent.
    if data.get("illustration"):
        metadata["illustration"] = data["illustration"]

    full = {
        "slug": data.get("slug"),
        "vertical": data.get("vertical"),
        "headline": data.get("title"),
        "body_md": data.get("body_md") or "",
        "content": data.get("body_md") or "",
        "title": data.get("title"),
        "source_url": source_url or None,
        "sources": data.get("sources") or [],
        "tags": [data.get("vertical")] if data.get("vertical") else [],
        "status": status,
        "live_urls": live_urls or {},
        "primary_keyword": data.get("primary_keyword") or None,
        "secondary_keywords": data.get("secondary_keywords") or [],
        "search_volume": data.get("search_volume"),
        "search_intent": data.get("search_intent") or None,
        "meta_title": data.get("meta_title") or None,
        "meta_description": data.get("meta_description") or None,
        "seo_metadata": clean_seo if clean_seo else None,
        "metadata": metadata,
    }

    base = f"{supabase_url}/rest/v1/articles"
    headers = {
        "apikey": service_key,
        "Authorization": f"Bearer {service_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Prefer": "return=representation",
    }

    # Keep only columns the live table actually has; put the rest in metadata.
    live_cols = _articles_live_columns(supabase_url, service_key)
    if live_cols is not None:
        payload = {k: v for k, v in full.items() if k in live_cols}
        if "metadata" in live_cols:
            payload.setdefault("metadata", metadata)
    else:
        payload = {"title": full["title"], "content": full["content"],
                   "source_url": full["source_url"], "tags": full["tags"],
                   "metadata": metadata}

    slug = data.get("slug") or ""
    slug_q = urllib.parse.quote(slug)
    # Idempotency: look up an existing row by metadata->>'slug'.
    try:
        req = urllib.request.Request(
            f"{base}?metadata->>slug=eq.{slug_q}&select=id&limit=1",
            headers={"apikey": service_key, "Authorization": f"Bearer {service_key}",
                     "Accept": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=20) as resp:
            existing = json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"  [Supabase] Could not query existing article: {e}")
        existing = []

    try:
        if existing:
            rid = existing[0]["id"]
            update = dict(payload)
            update["updated_at"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
            if "metadata" not in update:
                update["metadata"] = metadata
            req = urllib.request.Request(
                f"{base}?id=eq.{rid}",
                data=json.dumps(update).encode("utf-8"),
                headers={**headers, "Prefer": "return=representation"},
                method="PATCH",
            )
            label = f"updated {rid}"
        else:
            req = urllib.request.Request(base, data=json.dumps(payload).encode("utf-8"),
                                         headers=headers, method="POST")
            label = "inserted"
        with urllib.request.urlopen(req, timeout=20) as resp:
            body = resp.read().decode("utf-8")
            article_id = None
            try:
                rows = json.loads(body)
                if isinstance(rows, list) and rows:
                    article_id = rows[0].get("id")
            except Exception:
                article_id = None
            print(f"  [Supabase] {label} article '{slug}' (HTTP {resp.status}, id={article_id or 'n/a'})")
            return True
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        print(f"  [Supabase] Warning: Upsert failed (HTTP {e.code}): {err_body}")
        return False
    except Exception as e:
        print(f"  [Supabase] Warning: Could not connect to Supabase: {e}")
        return False


def push_wp_draft(slug: str) -> bool:
    """Create the article's draft in the CMS its vertical maps to (public.vertical_sites).

    Runs in the persistence pass, not behind the approval gate: a draft is invisible to readers
    (the Astro frontends render published posts only) and the gate stays on the CMS's
    draft -> publish flip, which is a human action. Idempotent by slug, so re-publishing an
    article updates its existing draft instead of creating a second one.

    Best-effort by design: a CMS that is down or an
    unconfigured credential must not roll back a publish that already persisted the article to
    published/, the log and Supabase. A failed push leaves the row without metadata.wordpress,
    which is exactly what `scripts/wp_draft.py --all` selects for on the next sweep.
    """
    try:
        import importlib.util

        path = os.path.join(REPO_ROOT, "scripts", "wp_draft.py")
        spec = importlib.util.spec_from_file_location("wp_draft", path)
        if spec is None or spec.loader is None:
            print(f"! WordPress draft skipped: cannot load {path}")
            return False
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        result = module.push_by_slug(slug)
        print(f"✓ WordPress post {result['status']}: post {result['post_id']} on {result['site']} "
              f"— {result['edit_url']}")
        if result.get("problems"):
            print("! the post exists but the CMS does not hold what was sent:", file=sys.stderr)
            for problem in result["problems"]:
                print(f"!   - {problem}", file=sys.stderr)
            print("!   fix the mapping and re-run: python3 scripts/wp_draft.py --all", file=sys.stderr)
        else:
            print(f"  (verified on the CMS: {result.get('summary') or 'title, excerpt, JSON-LD, inline SVG'})")
        print("  (published live on WordPress)")
        return True
    except Exception as exc:  # network, credentials, routing, CMS — never fail the publish
        print(f"! WordPress draft NOT created: {exc}", file=sys.stderr)
        print("!   retry later with: python3 scripts/wp_draft.py --all", file=sys.stderr)
        return False


def auto_deploy_push(slug: str) -> bool:
    """Commit pending factory changes and push to origin/<current-branch> so the GitHub->Coolify
    build redeploys automatically. Best-effort: warns and skips on any git failure rather than
    failing the publish. Returns True if a push was issued."""
    try:
        add = subprocess.run(["git", "add", "-A"], cwd=REPO_ROOT, capture_output=True, text=True)
        if add.returncode != 0:
            print(f"  [Auto-deploy] git add failed: {add.stderr.strip()}")
            return False
        status = subprocess.run(["git", "status", "--porcelain"], cwd=REPO_ROOT, capture_output=True, text=True)
        if not status.stdout.strip():
            print("  [Auto-deploy] no changes to commit; nothing to push.")
            return True
        who = subprocess.run(["git", "config", "user.email"], cwd=REPO_ROOT, capture_output=True, text=True)
        if not who.stdout.strip():
            print("  [Auto-deploy] git user.email not set; skipping push (deploy manually).")
            return False
        subprocess.run(["git", "commit", "-m", f"publish: {slug} (auto-deploy)", "--no-verify"],
                       cwd=REPO_ROOT, capture_output=True, text=True)
        branch = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=REPO_ROOT,
                                capture_output=True, text=True)
        branch = (branch.stdout or "main").strip()
        push = subprocess.run(["git", "push", "origin", branch], cwd=REPO_ROOT,
                              capture_output=True, text=True)
        if push.returncode != 0:
            print(f"  [Auto-deploy] git push failed: {push.stderr.strip()}")
            return False
        print(f"  [Auto-deploy] committed and pushed to origin/{branch} -> redeploy triggered.")
        return True
    except Exception as e:
        print(f"  [Auto-deploy] skipped: {e}")
        return False


LOG_COLUMNS = "| Date | Vertical | Slug | Headline | Reader URL | Distribution |"
LOG_DIVIDER = "|---|---|---|---|---|---|"

ENV_FILE = os.path.join(REPO_ROOT, ".env")


def load_env():
    """Populate os.environ from the repo .env (same precedence rule as site/server.mjs:
    real environment wins). Without this the Supabase upsert silently no-ops when the
    publisher is run from a plain shell — which is exactly how it is documented to run."""
    if not os.path.exists(ENV_FILE):
        return
    try:
        with open(ENV_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                key = key.strip()
                if key and not os.environ.get(key):
                    os.environ[key] = value.strip().strip('"').strip("'")
    except Exception as exc:  # never fail the publish over a malformed .env
        print(f"! Could not parse {ENV_FILE}: {exc}")


def normalize_slug(raw_slug, date_val):
    """Return a bare slug: some drafts carry '<date>_<slug>' in frontmatter, which used to
    produce 'published/<date>_<date>_<slug>.md' (and a doubled reader URL)."""
    slug = str(raw_slug or "").strip()
    if date_val and slug.startswith(f"{date_val}_"):
        slug = slug[len(date_val) + 1:]
    return re.sub(r"^\d{4}-\d{2}-\d{2}_", "", slug).strip()


def record_publish(log_path, values):
    """Insert one row at the end of the published-articles table (the file's first table).

    Keeps the log a faithful record of `published/*.md`: same six columns, rows added in place
    instead of appended at EOF (the file also carries an 'Awaiting approval' table that must not
    be polluted by published rows).
    """
    row = "| " + " | ".join(str(v) for v in values) + " |"
    if not os.path.exists(log_path) or os.path.getsize(log_path) == 0:
        with open(log_path, "w", encoding="utf-8") as f:
            f.write(f"# Published Log\n\n{LOG_COLUMNS}\n{LOG_DIVIDER}\n{row}\n")
        return

    with open(log_path, "r", encoding="utf-8") as f:
        lines = f.read().split("\n")

    table_start = next((i for i, line in enumerate(lines) if line.strip().startswith("|")), None)
    if table_start is None:
        lines += ["", LOG_COLUMNS, LOG_DIVIDER, row]
    else:
        last = table_start
        i = table_start
        while i < len(lines) and lines[i].strip().startswith("|"):
            last = i
            i += 1
        # Idempotent by slug: re-publishing an artifact (a corrected internal-links block, a
        # regenerated visual, a fixed body) has to UPDATE its row, never add a second one. The log's
        # invariant is one row per file in `published/`, so a duplicate makes it a false count.
        # (learned 2026-10-07: a re-run after an internal_links.py fix appended an identical row.)
        slug = str(values[2]) if len(values) > 2 else ""
        existing = next((j for j in range(table_start, last + 1)
                         if slug and f"| {slug} |" in lines[j]), None)
        if existing is not None:
            lines[existing] = row
        else:
            lines.insert(last + 1, row)

    with open(log_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    load_env()
    parser = argparse.ArgumentParser(description="Publish an article and embed external illustrated article & tool promo URLs")
    parser.add_argument("draft_file", help="Path to final draft markdown file")
    parser.add_argument("-a", "--article-url", default=None, help="Final URL where the article (with illustrations) is published (e.g. PressFlow/Ghost/blog)")
    parser.add_argument("-p", "--promo-url", default=None, help="URL for an external tool to promote (e.g. from Software Factory)")
    parser.add_argument("--promo-label", default=None, help="Custom label for the promo tool link (e.g. '🛠️ Try the tool:')")
    parser.add_argument("-i", "--interactive", action="store_true", help="Prompt interactively for article URL and promo tool URL")
    parser.add_argument("--dry-run", action="store_true", help="Parse and show what would be published without side effects")
    parser.add_argument("--no-deploy", action="store_true", default=False, help="Skip the auto commit+push (deploy) after publishing")
    parser.add_argument("--no-illustration", action="store_true", default=False,
                        help="Skip the featured-image pass (scripts/illustration_creator.py). Default: "
                             "art-direct + generate one header image unless ILLUSTRATION_ENABLED=false")
    parser.add_argument("--illustration-style", default=None,
                        help="Pin the treatment for this article (see STYLES in scripts/illustration_creator.py)")
    parser.add_argument("--illustration-model", default=None,
                        help="Pin the image model: flux or nanobanana")
    args = parser.parse_args()

    if not os.path.exists(args.draft_file):
        print(f"Error: file not found: {args.draft_file}", file=sys.stderr)
        return 1

    # A dry run must not spend image credits, so the featured-image pass is skipped there and said so.
    illustrate = (not args.no_illustration and not args.dry_run
                  and parse_bool_env("ILLUSTRATION_ENABLED", default=True))
    data = parse_draft(args.draft_file, illustrate=illustrate,
                       pinned_style=args.illustration_style, pinned_model=args.illustration_model,
                       links=not args.dry_run)
    date_val = data["date"]
    slug_val = normalize_slug(data["slug"], date_val)
    data["slug"] = slug_val  # keep the Supabase row / log consistent with the published filename
    pub_filename = f"{date_val}_{slug_val}.md"
    pub_path = os.path.join(REPO_ROOT, "published", pub_filename)
    log_path = os.path.join(REPO_ROOT, "context", "published_log.md")

    # Resolve URLs with precedence: CLI flag > Interactive > Frontmatter > Env variable fallback
    article_url = args.article_url or data["article_url"]
    promo_url = args.promo_url or data["promo_url"]
    promo_label = args.promo_label or data["promo_label"] or os.environ.get("DEFAULT_PROMO_LABEL", "🛠️ Try the live tool:")

    # Fallback to default base URL from env if available
    if not article_url:
        base_url = os.environ.get("DEFAULT_ARTICLE_BASE_URL", "").rstrip("/")
        if base_url:
            article_url = f"{base_url}/{slug_val}"

    if not promo_url:
        promo_url = os.environ.get("DEFAULT_PROMO_URL", "").strip()

    # Interactive prompt if requested and fields are empty
    if args.interactive:
        print("\n--- Interactive Link Setup ---")
        prompt_art = input(f"Enter final illustrated article URL [{article_url}]: ").strip()
        if prompt_art:
            article_url = prompt_art
        prompt_prm = input(f"Enter tool promo URL [{promo_url}]: ").strip()
        if prompt_prm:
            promo_url = prompt_prm
        if promo_url:
            prompt_lbl = input(f"Enter promo label [{promo_label}]: ").strip()
            if prompt_lbl:
                promo_label = prompt_lbl
        print("------------------------------\n")

    print("=" * 75)
    print(f"PUBLISHING PIPELINE: {data['title']}")
    print("=" * 75)
    print(f"Vertical:        {data['vertical']}")
    print(f"Slug:            {slug_val}")
    print(f"Target file:     published/{pub_filename}")
    print(f"Article URL:     {article_url or '(None - local reader only)'}")
    print(f"Promo Tool URL:  {promo_url or '(None)'}")

    if args.dry_run:
        print("\n[DRY RUN] Actions that would be performed:")
        print(f" 1. Write long-form markdown to {pub_path}")
        print(f" 2. Append entry to {log_path}")
        print(f" 3. Upsert row to Supabase articles table")
        print(f" 4. Create the CMS draft for the article's vertical (scripts/wp_draft.py)")
        print(f" 5. Refresh context/sitemap.json from published/")
        return 0

    # 1. Unconditional Persistence: write to published/
    os.makedirs(os.path.join(REPO_ROOT, "published"), exist_ok=True)
    with open(pub_path, "w", encoding="utf-8") as f:
        f.write(data["full_content"])
    print(f"✓ Saved article to published/{pub_filename}")

    # 3. Record the publish in published_log.md.
    #    The log is a *record of* published/*.md (six columns, first table in the file);
    #    the filesystem stays the source of truth, so a row is written only after the
    #    file exists on disk.
    reader_base = os.environ.get("PRESSFLOW_READER_BASE_URL", "https://pressflow.aichieve.net/published").rstrip("/")
    reader_url = f"{reader_base}/{pub_filename}"
    links = []
    if article_url:
        links.append(f"[article]({article_url})")
    if promo_url:
        links.append(f"[tool]({promo_url})")
    distribution = " · ".join(links) if links else "reader site only"

    record_publish(log_path, [date_val, data["vertical"], slug_val, data["title"], reader_url, distribution])
    print("✓ Recorded row in context/published_log.md")

    # 4. Upsert to Supabase
    #    `live_urls` carries where else the article lives (article_url / promo_url). It used to
    #    also carry the LinkedIn post URL; that channel was removed on 2026-10-06 and the removal
    #    deleted this dict's construction here by accident, leaving the call below referencing an
    #    undefined name — a NameError that aborted the pass AFTER the log row was written, silently
    #    skipping the Supabase row, the CMS draft and the sitemap refresh for every publish since.
    live_urls = {}
    if article_url:
        live_urls["article_url"] = article_url
    if promo_url:
        live_urls["promo_url"] = promo_url
    sync_to_supabase(data, live_urls)

    # 4a. Create the article's draft in the destination CMS (scripts/wp_draft.py) — in this same
    #     pass, so no manual step is needed. Persistence, not distribution: the draft is invisible
    #     to readers and the approval gate stays on the CMS's draft -> publish flip. Best-effort;
    #     a failure is surfaced here and re-tried by the scheduled `wp_draft.py --all` sweep.
    if not args.dry_run:
        push_wp_draft(slug_val)
    else:
        print("  [WordPress draft] skipped (dry-run).")

    # 4b. Refresh the derived surfaces in the same pass. context/sitemap.json is derived from
    #     published/*.md (it feeds the SEO tab + Growth OS loops) and verify.sh §7.5 fails closed on
    #     drift, so a persistence pass that skipped it shipped a stale index and a red gate.
    try:
        sm = subprocess.run([sys.executable, os.path.join(REPO_ROOT, "scripts", "sitemap_sync.py")],
                            cwd=REPO_ROOT, capture_output=True, text=True)
        if sm.returncode == 0:
            print("✓ Refreshed context/sitemap.json from published/")
        else:
            print(f"! sitemap_sync.py failed: {(sm.stderr or sm.stdout).strip()[:200]}", file=sys.stderr)
    except Exception as e:  # never fail the publish on a derived-surface refresh
        print(f"! sitemap_sync.py could not run: {e}", file=sys.stderr)

    # 5. Auto-deploy: commit + push so the GitHub->Coolify build redeploys automatically.
    if not args.dry_run and parse_bool_env("AUTO_PUBLISH_DEPLOY", default=True) and not args.no_deploy:
        auto_deploy_push(slug_val)
    else:
        print("  [Auto-deploy] skipped (dry-run, --no-deploy, or AUTO_PUBLISH_DEPLOY=false).")

    print("\n✓ Publishing process completed successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
