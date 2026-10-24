#!/usr/bin/env python3
"""Reader-facing internal links for an artifact, from the sites' real live corpus.

The drafting skill asks for 2-3 contextual links under `<!-- internal-links -->`, and nothing ever
filled it: the drafting stage is an LLM with no list of live pages, so the block arrived empty on
every artifact and every CMS draft reached the reader with zero internal links (verified by reading
all 12 back — 0 same-site anchors in each) while the hand-written back catalogue carried 2-10 each.
The candidate corpus and the scorer already existed (scripts/build_internal_link_index.py,
growth_os.generate_internal_link_map) but were wired only into the keyword path
(scripts/seo_machine.py), never into the path that actually publishes.

This module is the deterministic fill, and it is the one owner of the block's shape:

  * `## Related reading` — real markdown links, so they reach the CMS post as `<a href>`. Article
    body, not an operator note: a link only does something for a reader or a crawler once it lands
    in the post.
  * operator placement hints as HTML comments — never reader-visible, stripped by every renderer.

Rules that decide whether the reader gets a useful link or a broken one:

  * the destination is resolved from the artifact's vertical (public.vertical_sites). No vertical =>
    no links: a link to the other site is a cross-site link, not an internal one, and guessing
    "the main site" is how content gets mis-routed. Says so rather than generating anything.
  * stamped ONCE, for every front that will serve the article (learned 2026-10-15). One shared CMS
    serves several fronts that pull different category subsets of it, so a body written for one site is
    read on another: an absolute `https://giniloh.com/...` anchor is internal on giniloh.com and a
    cross-site link on aichieve.net, and no front rewrites it. A link is therefore stamped as the
    site-relative path (`/slug/`) it resolves to on EVERY front that serves the article, and dropped
    when the fronts disagree about the path (giniloh's `/calculators/x/` vs aichieve's `/tools/x/`) or
    when it is not live on all of them. A link that 404s or leaves the site is worse than no link.
  * same-site, live-on-the-frontend-sitemap, never the article itself (its own slug is excluded here
    as well, so refreshing an already-published article cannot link it to itself), never a mere
    domain match — all enforced by the scorer.
  * never invented: when nothing qualifies there is no `## Related reading` section at all, and the
    gap is stated in the notes.
  * idempotent: the generated block is delimited by `<!-- internal-links:start/end -->`, so a re-run
    replaces it exactly instead of stacking a second list, and a link that has since gone stale (its
    target dropped out of the sitemap) is removed rather than left rotting in the post.
  * placement: the block belongs under the marker; when the marker is missing it is inserted before
    `<!-- tldr -->`, else `<!-- linkedin -->`, else `## Sources`, else at the end of the body.

CLI:
  python3 scripts/internal_links.py context/drafts/foo_final.md            # report, write nothing
  python3 scripts/internal_links.py context/drafts/foo_final.md --apply    # write in place
  python3 scripts/internal_links.py --check context/drafts/*.md published/*.md
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys
import urllib.parse
from datetime import datetime, timezone

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

ROOT = pathlib.Path(__file__).resolve().parent.parent
MARKER = "<!-- internal-links -->"
BLOCK_START = ("<!-- internal-links:start — generated from context/internal_links.json by "
               "scripts/internal_links.py; edits between these markers are overwritten -->")
BLOCK_END = "<!-- internal-links:end -->"
MAX_LINKS = 3

_BLOCK_RE = re.compile(r"[ \t]*" + re.escape(BLOCK_START) + r".*?" + re.escape(BLOCK_END) + r"[ \t]*\n?",
                       re.S)
_FM_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.S)
_BARE_RELATED_RE = re.compile(r"(?:\n|^)##\s*Related reading\s*\n+(?:[ \t]*[-*+]\s+\[[^\]]+\]\([^)]+\)[^\n]*\n*)+", re.M)
# Absolute OR site-relative, because a stamped link is a relative path (`/slug/`) — a reader-facing
# link only has to resolve on the front that serves the post, and reading one back must not depend on
# the form it was written in (a relative-only block would read as "0 links", which the CLI and
# `--check` would report as an article that reaches readers with no internal link at all).
_LIST_ITEM = re.compile(r"^-\s+\[(?P<anchor>[^\]]+)\]\((?P<url>(?:https?://|/)[^)\s]+)\)"
                        r"(?:\s+—\s+(?P<reason>.*))?$")
_COMMENT_LINE = re.compile(r"^[ \t]*<!--.*?-->[ \t]*$\n?", re.M)
# A line that is only link material: a markdown link, a bare URL, or a site-relative path. Used to
# recognise the drafting stage's own attempt at the block, so leftovers are removed WITHOUT touching
# prose — the marker's region can otherwise hold reader content (verified: on
# published/2026-09-25_ca-fair-plan-rate-hike-hardening-exit.md the marker sits inline on
# "**Go deeper:**", and everything up to the next heading is the article's Key Takeaways block).
_LINK_ONLY_LINE = re.compile(
    r"^[ \t]*(?:[-*+]\s+)?(?:\[[^\]]*\]\((?:https?://|/)[^)\s]+\)|https?://\S+|/[a-z0-9][\w\-/]*/?)[.,;]?[ \t]*$",
    re.I)


# ─────────────────────────────────────────────────────────────────────────────
# rendering — the only place the block's shape is defined
# ─────────────────────────────────────────────────────────────────────────────

_ACRONYM_RE = re.compile(r"\b[A-Z]{2,}\b")


def _reader_safe_category(category: str) -> str:
    """The category label is reader-facing copy, so it must survive the accessibility gate.

    A destination CMS category like `AI Stack & Tool TCO` echoes a bare all-caps token into the
    article, and `check_accessibility.py` then reads the PUBLISHED artifact as an undefined-acronym
    FAIL even though the `_final.md` the humanizer passed was clean (learned 2026-10-06). Editing
    the article body to compensate is the wrong fix, and inventing an expansion for a token the
    destination site owns is a hallucination — so the label is dropped. Same for a trailing colon.
    """
    category = (category or "").strip().rstrip(":").strip()
    if not category or _ACRONYM_RE.search(category):
        return ""
    return category


def href_of(link) -> str:
    """The URL to stamp in the body: the relative path when one was stamped, else the absolute URL.

    Only links that arrived with corpus metadata (`sites_live`) are stamped; a caller that passes its
    own links keeps the URLs it chose."""
    return link.get("href") or link.get("url", "")


def render_related_reading(links) -> str:
    """The reader-facing section: real anchors, on the same site, verified live.

    Empty when no link qualified — an empty heading is worse than no section. Callers (and the
    regression suite) rely on that: `== ""` means "the article ships with no Related reading".
    """
    links = [l for l in (links or []) if l.get("url") and l.get("anchor_text")]
    if not links:
        return ""
    lines = ["## Related reading", ""]
    for link in links:
        category = _reader_safe_category(link.get("category"))
        reason = "calculator" if link.get("kind") == "calculator" else (
            f"more on {category}" if category else "")
        lines.append(f"- [{link['anchor_text']}]({href_of(link)})" + (f" — {reason}" if reason else ""))
    return "\n".join(lines)


def render_link_hints(links) -> str:
    """Placement hints for the operator, as HTML comments so they never reach a reader."""
    lines = [f"<!-- internal-link hint: \"{l.get('anchor_text')}\" -> {href_of(l)} "
             f"[{l.get('why', '')}] {l.get('suggested_placement', '')} -->"
             for l in (links or []) if l.get("url")]
    return "\n".join(lines) or ("<!-- internal-link hint: none — no live page on this site scored "
                               "for this topic -->")


def render_block(links) -> str:
    """The delimited block written under the marker. Always delimited, even with no links, so a
    stale block from an earlier run is replaced rather than left behind."""
    parts = [BLOCK_START, render_link_hints(links)]
    related = render_related_reading(links)
    if related:
        parts.append(related)
    parts.append(BLOCK_END)
    return "\n".join(parts)


def read_links(markdown: str) -> list[dict]:
    """The links the generated block currently carries. [] when there is no block (or no links).

    Reads our own delimited block, falling back to the marker's region so a block written by an
    older revision (before the delimiters existed) is still visible.
    """
    text = markdown or ""
    block = _BLOCK_RE.search(text)
    if block:
        region = block.group(0)
    else:
        marker = text.find(MARKER)
        if marker == -1:
            return []
        start = marker + len(MARKER)
        region = text[start:_next_boundary(text, start)]
    out = []
    for line in region.splitlines():
        match = _LIST_ITEM.match(line.strip())
        if match:
            out.append({"anchor_text": match.group("anchor"), "url": match.group("url"),
                        "reason": (match.group("reason") or "").strip()})
    return out


# ─────────────────────────────────────────────────────────────────────────────
# placement
# ─────────────────────────────────────────────────────────────────────────────

def _split_frontmatter(markdown: str) -> tuple[str, str]:
    match = _FM_RE.match(markdown or "")
    return (markdown[:match.end()], markdown[match.end():]) if match else ("", markdown or "")


def _next_boundary(text: str, start: int) -> int:
    """Index of the next standalone pipeline marker or heading after `start`, else len(text)."""
    hits = [m.start() for m in (re.search(r"^[ \t]*<!--", text[start:], re.M),
                                re.search(r"^#{1,6}\s", text[start:], re.M)) if m]
    return start + min(hits) if hits else len(text)


def _insertion_point(body: str) -> tuple[int, str]:
    """Where the marker goes when the artifact has none. Order matters: the block must sit before
    `<!-- linkedin -->`, because everything after that marker is the internal social variant."""
    for pattern, label in ((r"^[ \t]*<!--\s*tldr\s*-->", "before <!-- tldr -->"),
                           (r"^[ \t]*<!--\s*linkedin\s*-->", "before <!-- linkedin -->"),
                           (r"^[ \t]*<!--\s*schema\s*-->", "before <!-- schema -->"),
                           (r"^##\s+Sources\s*$", "before ## Sources")):
        match = re.search(pattern, body, re.M)
        if match:
            return match.start(), label
    return len(body.rstrip("\n")) + 1 if body.strip() else 0, "at the end of the body"


def _lead_paragraph(body: str) -> str:
    """First real paragraph — the article's own summary of what it is about."""
    for raw in _COMMENT_LINE.sub("", body or "").splitlines():
        text = raw.strip()
        if not text or text.startswith(("#", "|", ">", "-", "*", "```", "!")):
            continue
        text = re.sub(r"\[([^\]]+)\]\([^)\s]+\)", r"\1", text)
        text = re.sub(r"[*`_]", "", text).strip()
        if len(text.split()) >= 6:
            return text
    return ""


def topic_for(title: str, body: str) -> str:
    """What the link scorer matches against: the headline, plus the lead's first sentence.

    The headline alone is the tightest summary, but the corpus is scored on the target page's
    title/excerpt/categories, so one more sentence of real subject matter measurably improves which
    pages qualify. Barely more than the title is used on purpose — a long topic string would let a
    single incidental shared word qualify an unrelated page.
    """
    title = " ".join(str(title or "").split())
    lead = _lead_paragraph(body)
    sentence = re.split(r"(?<=[.!?])\s+", lead)[0].strip() if lead else ""
    topic = f"{title}. {sentence}".strip(" .") if sentence else title
    return topic[:240]


# ─────────────────────────────────────────────────────────────────────────────
# the render set — which fronts will serve this article, and what form a link takes
# ─────────────────────────────────────────────────────────────────────────────

def renderers_for(links) -> list[str]:
    """The fronts that will serve this article — as the SCORER resolved them, carried on the links.

    Deliberately not computed here. Working out the render set needs the article's routing row, and the
    only code that may touch routing is the scorer, which already holds it: routing goes through
    `wp_draft.supabase_config()`, which EXITS THE PROCESS when the Supabase credentials are absent —
    an `except Exception` cannot catch that, so a link pass that reached for it would kill a publish
    instead of degrading. `generate_internal_link_map` resolves the set (the fronts publishing the
    article's category hub) and stamps it on every link it returns.

    Returns [] when nothing carries a render set — a caller's own links, or a corpus with no hub data —
    and the caller then stamps nothing rather than guessing.
    """
    for link in links or []:
        serve = link.get("serve")
        if serve:
            return [d for d in serve if d]
    return []


def stamp_links(links, renderers, site_domain=None) -> tuple[list[dict], list[str]]:
    """Stamp each link in the form that is internal on every front that serves the article.

    Returns (kept_links, notes). Kept links carry `href`, the relative path; a link is dropped, with a
    note, when it is not live on every renderer or when the renderers publish it at different paths. A
    link with no corpus metadata (a caller's own list) is passed through untouched.
    """
    renderers = [d for d in (renderers or []) if d]
    if not renderers:
        # The fronts that will serve this article could not be resolved (no index, no routing row, or
        # an index built before the fronts owned the corpus). Nothing is dropped and nothing is
        # restamped: the links keep the form the corpus gave them. This is the one degradation that
        # must not be destructive — `publish.apply_internal_links` calls this without a site_domain,
        # so guessing an empty render set here would strip every link from every article it touches.
        return list(links or []), ["the fronts that serve this article could not be resolved — links "
                                   "left in the form the corpus gave them (nothing was stamped)"]
    kept: list[dict] = []
    dropped_absent: list[str] = []
    dropped_divergent: list[str] = []
    for link in links or []:
        live = link.get("sites_live") or {}
        if not live:
            kept.append(link)
            continue
        paths = [live.get(d) for d in renderers]
        if any(p is None for p in paths):
            missing = [d for d, p in zip(renderers, paths) if p is None] or ["?"]
            dropped_absent.append(f"{link.get('anchor_text')!r} (not live on {', '.join(missing)})")
            continue
        if len(set(paths)) != 1:
            where = ", ".join(f"{d}:{p}" for d, p in zip(renderers, paths))
            dropped_divergent.append(f"{link.get('anchor_text')!r} ({where})")
            continue
        kept.append({**link, "href": paths[0]})

    notes = []
    if renderers:
        notes.append(f"links stamped for {len(renderers)} front(s) that serve this article: "
                     f"{', '.join(renderers)} — a relative path is internal on each of them")
    if dropped_absent:
        notes.append(f"dropped {len(dropped_absent)} candidate(s) that are not live on every front "
                     f"serving this article: " + "; ".join(dropped_absent[:3]))
    if dropped_divergent:
        notes.append(f"dropped {len(dropped_divergent)} candidate(s) the fronts publish at different "
                     f"paths (a relative path cannot be right on both): " + "; ".join(dropped_divergent[:3]))
    return kept, notes


# ─────────────────────────────────────────────────────────────────────────────
# link resolution — the one seam between this module and the corpus
# ─────────────────────────────────────────────────────────────────────────────

def resolve_links(topic: str, vertical: str | None, max_links: int = MAX_LINKS,
                  exclude_slugs=(), category_id=None) -> list[dict]:
    """Propose links for the destination site of `vertical`, from the live corpus.

    The single seam: everything above is pure (no network, no clock) and the regression suite
    replaces this one function.
    """
    import growth_os as gos
    return gos.generate_internal_link_map(topic, vertical, max_links=max_links,
                                          exclude_slugs=tuple(exclude_slugs),
                                          category_id=category_id)


def _links_note(links, vertical, topic) -> str:
    if not links:
        return (f"no internal link generated for '{topic[:60]}' on {vertical}: no live page on the "
                f"destination site scored for this topic (nothing is invented to fill the gap)")
    return (f"{len(links)} internal link(s) for {vertical}: "
            + "; ".join(f"\"{l['anchor_text']}\" -> {l['url']} ({l.get('why', '')})" for l in links))


def same_site(url: str, domain: str) -> bool:
    """Is `url` on `domain`? The scorer already prefers the destination site, but a routing lookup
    that degraded (an unreachable database) leaves it without a destination to filter on — so the
    final list is checked here too. A link to the other site is not an internal link."""
    host = (urllib.parse.urlparse(url or "").hostname or "").lower()
    want = (domain or "").strip().lower().lstrip(".")
    return bool(host and want) and (host == want or host.endswith("." + want))


# ─────────────────────────────────────────────────────────────────────────────
# the artifact pass
# ─────────────────────────────────────────────────────────────────────────────

def enrich(markdown: str, *, vertical: str | None = None, topic: str | None = None,
           links=None, exclude_slugs=(), max_links: int = MAX_LINKS,
           site_domain: str | None = None, category_id=None) -> tuple[str, list[str], list[dict]]:
    """Fill the artifact's internal links. Returns (markdown, notes, links_used).

    Idempotent: a previously generated block is replaced by the freshly scored one (same delimiters),
    so re-running after a corpus change updates the links instead of appending a second list, and a
    link whose target is no longer live disappears. Every decision is reported, never silent.
    """
    notes: list[str] = []
    frontmatter, body = _split_frontmatter(markdown or "")
    previous = _BLOCK_RE.search(body)
    had_delimited = previous is not None
    if had_delimited:
        body = _BLOCK_RE.sub("", body)
    if _BARE_RELATED_RE.search(body):
        body = _BARE_RELATED_RE.sub("\n", body)

    title = _frontmatter_title(frontmatter) or _first_heading(body)
    if links is None:
        if not vertical:
            links = []
            notes.append("no vertical on the artifact — the destination site cannot be resolved, so "
                         "no internal link was generated (a link to another site is not an internal "
                         "link, and guessing one mis-routes content)")
        else:
            links = resolve_links(topic or topic_for(title, body), vertical, max_links,
                                  exclude_slugs, category_id=category_id) or []
    links = list(links)
    if links:
        links, stamp_notes = stamp_links(links, renderers_for(links), site_domain)
        notes += stamp_notes
    if site_domain:
        off_site = [l for l in links if not same_site(l.get("url", ""), site_domain)]
        if off_site:
            notes.append(f"dropped {len(off_site)} candidate(s) not on {site_domain}: "
                         + ", ".join(l.get("url", "") for l in off_site[:3])
                         + " (a link to another site is not an internal link)")
        links = [l for l in links if same_site(l.get("url", ""), site_domain)]

    block = render_block(links)
    previous_text = previous.group(0).strip() if previous else ""
    if block.strip() == previous_text:
        notes.append(f"the block is already up to date ({len(links)} link(s)) — nothing rewritten")
    elif previous:
        notes.append(f"replaced the previously generated block "
                     f"({len(read_links(previous.group(0)))} link(s) -> {len(links)})")

    if MARKER in body:
        start = body.index(MARKER) + len(MARKER)
        if not had_delimited:
            # First run. The marker's region may hold the drafting stage's own attempt at the block.
            # Remove it ONLY when every line of it is link material — the region can equally hold
            # reader copy (the marker is sometimes written inline, e.g. "**Go deeper:** <!--
            # internal-links -->" directly above the Key Takeaways block), and deleting that would
            # silently shorten the article in the CMS.
            end = _next_boundary(body, start)
            leftover = body[start:end]
            lines = [line for line in leftover.splitlines() if line.strip()]
            if lines and all(_LINK_ONLY_LINE.match(line) for line in lines):
                notes.append(f"dropped {len(lines)} line(s) of leftover link material under the "
                             f"marker ({lines[0].strip()[:60]!r})")
                body = body[:start] + body[end:]
            elif lines:
                notes.append(f"left {len(lines)} existing line(s) under the marker alone — they are "
                             f"not link material (the block is added below them, so the operator can "
                             f"prune a duplicate by hand)")
        tail = body[start:].lstrip("\n")
        body = f"{body[:start]}\n\n{block}\n\n{tail}" if tail else f"{body[:start]}\n\n{block}\n"
        where = "under <!-- internal-links -->"
    else:
        index, where = _insertion_point(body)
        tail = body[index:].lstrip("\n")
        body = f"{body[:index].rstrip()}\n\n{MARKER}\n\n{block}\n\n{tail}".rstrip() + "\n"
        notes.append(f"inserted <!-- internal-links --> {where} (the artifact carried no marker)")

    notes.append(_links_note(links, vertical or "?", topic or title))
    notes.append(f"block written {where}")
    return frontmatter + body.strip("\n") + "\n", notes, links


def _frontmatter_title(frontmatter: str) -> str:
    match = re.search(r'^title:[ \t]*"?([^"\n]+?)"?[ \t]*$', frontmatter or "", re.M)
    return match.group(1).strip() if match else ""


def _first_heading(body: str) -> str:
    match = re.search(r"^#{1,6}\s+(.+)$", body or "", re.M)
    return match.group(1).strip() if match else ""


# ─────────────────────────────────────────────────────────────────────────────
# the source-row pass (what the connector and the persistence pass call)
# ─────────────────────────────────────────────────────────────────────────────

def topic_from_row(metadata: dict, content: str) -> str:
    """Topic for a Supabase article row: its headline, plus the lead's first sentence."""
    metadata = metadata or {}
    title = metadata.get("headline") or metadata.get("title") or ""
    for key in ("primary_keyword", "keyword"):
        if (metadata.get(key) or "").strip():
            title = f"{metadata[key]} {title}"
            break
    return topic_for(title, content)


def ensure_for_row(row: dict, *, persist: bool = True, db=None, links=None,
                   max_links: int = MAX_LINKS, site_domain: str | None = None) -> tuple[dict, list[str]]:
    """Fill an article row's internal links and (optionally) write them back.

    The row is what the connector pushes, so this is where the links have to land: enriching only
    the file on disk would be invisible to the CMS, and enriching only the payload would be lost by
    the next `--refresh` (which re-reads the row's own content). Content + metadata are written in
    one PATCH so the row and the CMS never disagree, and `metadata.internal_links` records what was
    generated, from where, and when.
    """
    metadata = row.get("metadata") or {}
    content = row.get("content") or ""
    vertical = metadata.get("vertical") or (row.get("tags") or [None])[0]
    slug = (metadata.get("slug") or "").strip()
    existing = read_links(content)

    enriched, notes, used = enrich(
        content, vertical=vertical, topic=topic_from_row(metadata, content), links=links,
        exclude_slugs=(slug,) if slug else (), max_links=max_links, site_domain=site_domain,
        # The post's own category (an editor's override) decides which hub it links to.
        category_id=(metadata.get("wordpress") or {}).get("category_id"))

    if enriched == content:
        notes.append(f"no change: the block already holds {len(existing)} link(s)")
        return row, notes

    record = {"count": len(used),
              "urls": [l.get("url") for l in used],
              "anchors": [l.get("anchor_text") for l in used],
              "source": "context/internal_links.json",
              "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
              "generated_by": "scripts/internal_links.py"}
    updated = {**row, "content": enriched, "metadata": {**metadata, "internal_links": record}}
    if persist and db is not None:
        db.update_body(row["id"], enriched, updated["metadata"])
        notes.append(f"wrote the links back to the Supabase row ({row['id']}) so the DB and the CMS "
                     f"hold the same body")
    elif not persist:
        notes.append("not written back (dry-run)")
    return updated, notes


# ─────────────────────────────────────────────────────────────────────────────
# CLI — report (default) or write in place
# ─────────────────────────────────────────────────────────────────────────────

def _vertical_of(text: str) -> str:
    match = re.search(r'^vertical:[ \t]*"?([^"\n]+?)"?[ \t]*$', text, re.M)
    return match.group(1).strip() if match else ""


def _report(path: pathlib.Path) -> tuple[bool, list[str]]:
    text = path.read_text(encoding="utf-8")
    links = read_links(text)
    has_marker = MARKER in text
    notes = []
    complete = bool(links) and has_marker
    if not has_marker:
        notes.append("marker: MISSING (<!-- internal-links -->)")
    notes.append(f"links in the artifact: {len(links)}"
                 + ("" if links else " — a reader gets no internal link from this article"))
    for link in links:
        notes.append(f"  {link['anchor_text']} -> {link['url']}")
    return complete, notes


def _artifact_slug(path: pathlib.Path) -> str:
    """The slug of the artifact a CLI path names (`2026-10-10_my-slug.md` -> `my-slug`).

    The CLI is also how an artifact that is ALREADY live gets re-enriched, and by then the article
    is itself a candidate in `context/internal_links.json` — so the exclusion `ensure_for_row` passes
    (the row's own slug) has to be passed here too, or the re-run links the post to itself.
    """
    stem = path.name[:-3] if path.name.lower().endswith(".md") else path.name
    return stem[11:] if re.match(r"\d{4}-\d{2}-\d{2}_", stem) else stem


def main() -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").splitlines()[0])
    parser.add_argument("files", nargs="*", help="article markdown files")
    parser.add_argument("--apply", action="store_true", help="write the links into the files")
    parser.add_argument("--check", action="store_true",
                        help="exit 1 when an artifact would reach a destination without any link")
    args = parser.parse_args()
    if not args.files:
        parser.error("pass at least one markdown file")

    incomplete = 0
    for raw in args.files:
        path = pathlib.Path(raw)
        text = path.read_text(encoding="utf-8")
        print(f"  {path.name}")
        if args.apply:
            enriched, notes, links = enrich(text, vertical=_vertical_of(text),
                                            exclude_slugs=(_artifact_slug(path),))
            if enriched != text:
                path.write_text(enriched, encoding="utf-8")
            for note in notes:
                print(f"    - {note}")
            print(f"    - {'written' if enriched != text else 'already up to date (no change)'}")
        else:
            complete, notes = _report(path)
            incomplete += 0 if complete else 1
            for note in notes:
                print(f"    - {note}")
    if args.check and incomplete:
        print(f"FAIL: {incomplete} artifact(s) reach a destination with no internal link")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
