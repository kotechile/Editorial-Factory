#!/usr/bin/env python3
"""Derive the assets a destination needs from an article artifact: SEO metadata + a chart.

Both are **derived from the artifact's own text** — never invented. The generator's drafting stage
is an LLM and it does not reliably emit `meta_title` / `meta_description`, and the news path emits no
visual at all, so the destinations (the CMS excerpt, the frontends' `<meta name="description">`, the
reader's page) end up with whatever the last writer happened to leave behind. This module makes both
deterministic, idempotent and testable, and reports every decision (including "no chart, and why").

Two halves:

  metadata   `meta_title` / `meta_description`, from the headline and the lead paragraph, only when
             the artifact does not already carry them (a keyword-aware value written by the drafting
             stage always wins). Provenance is recorded in `meta_title_source` /
             `meta_description_source` so a derived value is never mistaken for a researched one.

  chart      An inline SVG bar chart of the percentages the article's own `**By the numbers:**`
             section states. Charted only when the figures are a real, single-unit series:

               - only the numbers section is read, never the prose of the article;
               - only figures carrying `%` (a 0-100 axis is then a true comparison — money, counts
                 and multipliers never share it);
               - a bullet whose own sentence contains a second percentage is skipped: that figure is
                 being *compared* to another one, not stated as a series point;
               - at least two points, at most five; fewer than two emits no chart at all, and says so.

             There is deliberately no placeholder fallback. A chart is the most quotable part of an
             article; a bar that exists only so a visual exists is an invented figure.

CLI:
  python3 scripts/article_assets.py context/drafts/foo_final.md            # report only
  python3 scripts/article_assets.py context/drafts/foo_final.md --apply    # write in place
  python3 scripts/article_assets.py --check published/*.md                 # exit 1 if anything is missing
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import chart_generator as cg  # noqa: E402

META_TITLE_MAX = 60
META_DESC_TARGET = 158          # characters; the WordPress excerpt / <meta name="description"> budget
META_DESC_MIN = 110             # below this a description is a fragment, not a description
CHART_MAX_POINTS = 5
CHART_MIN_POINTS = 2            # fewer than two points is not a series
CHART_SUBTITLE = "Figures as stated in this article's own numbers section (verified figures, %)"

_NUMBERS_HEADING = re.compile(r"^\*\*By the numbers:\*\*\s*$", re.M)
_BULLET = re.compile(r"^\s*[-*]\s+(.*)$")
_BOLD_LEAD = re.compile(r"^\*\*(?P<lead>.+?)\*\*\s*:?\s*(?P<rest>.*)$", re.S)
_PCT = re.compile(r"(\d+(?:[.,]\d+)?)\s*%")
_SECTION_BREAK = re.compile(r"^(#{1,6}\s|\s*<!--|\s*\|)")


# ─────────────────────────────────────────────────────────────────────────────
# artifact parsing (frontmatter + the numbers section)
# ─────────────────────────────────────────────────────────────────────────────

def split_frontmatter(md: str) -> tuple[dict[str, str], str]:
    """The artifact's frontmatter as raw strings, plus the body. Mirrors publish.py's parser."""
    fm: dict[str, str] = {}
    body = md
    if md.startswith("---"):
        parts = md.split("---", 2)
        if len(parts) >= 3:
            body = parts[2].lstrip("\n")
            for line in parts[1].strip().splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, body


def numbers_block(body: str) -> str:
    """The `**By the numbers:**` bullet block, or "" when the article has none."""
    match = _NUMBERS_HEADING.search(body)
    if not match:
        return ""
    lines: list[str] = []
    for line in body[match.end():].splitlines():
        stripped = line.strip()
        if stripped and not _BULLET.match(line) and _SECTION_BREAK.match(stripped):
            break
        lines.append(line)
    return "\n".join(lines).strip("\n")


def _bullets(block: str) -> list[str]:
    return [m.group(1).strip() for line in block.splitlines() if (m := _BULLET.match(line))]


def clean_metric_label(figure: str, rest: str) -> str:
    """Derive a concise, human-readable metric label for charts.

    Prefers structured titles, strips conversational lead-ins ('The price jump for...',
    'The leap in the...'), normalizes agency/corporate acronyms (e.g. 'United Parcel Service (UPS)'
    -> 'UPS'), and trims trailing subordinate clauses so the chart displays a clean metric name
    rather than a truncated sentence fragment.

    Every candidate is bounded by `chart_generator.LABEL_MAX` — the widest label that clears the
    bars — so the renderer never has to shorten this output. A label longer than the ceiling that
    still reads as a name is cut on a word boundary instead of being handed back for ellipsis.
    """
    # 0. Check if metric name is embedded in the bold figure itself: e.g. "13% — Ad-free Disney+ & Hulu"
    for sep in [" — ", " – ", " - "]:
        if sep in figure:
            for p in figure.split(sep):
                if "%" not in p and len(p.strip(" :—-")) >= 3:
                    cand = p.strip(" :—-")
                    if len(cand) <= cg.LABEL_MAX:
                        return cand

    text = rest.strip()
    # 1. Bold metric title: **Metric Name**: description or **Metric Name** — description
    bold_m = re.match(r"^\*\*(.+?)\*\*\s*:?\s*(.*)$", text)
    if bold_m:
        cand = bold_m.group(1).strip(" :—-")
        if 3 <= len(cand) <= cg.LABEL_MAX:
            return cand

    # 2. Separator like ' — ', ' – ', ' - '
    for sep in [" — ", " – ", " - "]:
        if sep in text:
            cand = text.split(sep)[0].strip(" :—-")
            cand = re.sub(r"\[\d+\]", "", cand).strip()
            if 3 <= len(cand) <= cg.LABEL_MAX:
                return cand

    # 3. Clean citations and trailing punctuation early
    text = re.sub(r"\[\d+\]", "", text).strip(" ,;:—.-/")

    # 4. Check if figure carries a descriptive metric noun (e.g. '88% price jump', '40% routed', '5.9% rate hike')
    fig_clean = re.sub(r"[\$€£]?\s*[\d.,]+(?:\s*(?:to|–|-|\/|vs\.?|and)\s*[\$€£]?[\d.,]+)?\s*[%xX×\+]?", "", figure, flags=re.I)
    fig_clean = re.sub(r"[\d.,\s%xX×\+\$€£/–—:-]+", " ", fig_clean).strip()
    non_num_fig = " ".join([w for w in fig_clean.split() if w.lower() not in ("to", "vs", "and", "or", "a", "an", "the", "per")])

    if non_num_fig and len(non_num_fig) >= 3:
        subj_m = re.match(r"^([A-Z][a-zA-Z0-9\+\s]+?)(?:\s+(?:started|began|rose|fell|jumped|dropped|hit|costs|priced|was|is|are|were|grew|surged|on|in|at)\b|[,;:])", text)
        if subj_m:
            subj = subj_m.group(1).strip()
            subj = re.sub(r"\s+fuel$", "", subj, flags=re.I)
            if 2 <= len(subj) <= 20 and subj.lower() not in non_num_fig.lower():
                combined = f"{subj} {non_num_fig}".strip()
                if len(combined) <= cg.LABEL_MAX:
                    return combined[0].upper() + combined[1:]
        if len(non_num_fig) <= cg.LABEL_MAX:
            return non_num_fig[0].upper() + non_num_fig[1:]

    # 5. Strip common conversational filler prefixes
    filler_re = r"^(?:the\s+)?(?:tiny\s+|huge\s+|massive\s+|slight\s+|modest\s+|strict\s+|record\s+)?(?:price\s+jump|price\s+hike|leap|jump|surge|spike|rise|climb|gain|increase|growth|drop|fall|cut|reduction|decline|slump|rate|share|slice|size|fee|cost|number|amount)\s+(?:for\s+(?:both\s+|the\s+)?|in\s+(?:the\s+)?|of\s+(?:the\s+)?|to\s+(?:the\s+)?|on\s+(?:the\s+)?|that\s+)"
    stripped = re.sub(filler_re, "", text, flags=re.I).strip(" ,;:—.-/")

    filler_re2 = r"^(?:the\s+)?(?:year-over-year\s+|yoy\s+)?(?:growth|increase|drop)\s+(?:for\s+(?:both\s+|the\s+)?|in\s+(?:the\s+)?|of\s+(?:the\s+)?)"
    stripped = re.sub(filler_re2, "", stripped, flags=re.I).strip(" ,;:—.-/")

    filler_re3 = r"^(?:the\s+)?(?:tiny\s+|huge\s+|massive\s+|slight\s+|modest\s+)?(?:rate\s+that|rate\s+prices\s+outpaced|share\s+of|rate\s+of)\s+"
    stripped = re.sub(filler_re3, "", stripped, flags=re.I).strip(" ,;:—.-/")

    # Normalize entity acronyms: 'United Parcel Service (UPS)' -> 'UPS'
    stripped = re.sub(r"\b(?:[A-Z][a-z0-9]+\s+){1,5}\(([A-Z0-9]{2,8})\)", r"\1", stripped)
    stripped = re.sub(r"\bUnited Parcel Service\b", "UPS", stripped)
    stripped = re.sub(r"\bUnited States Postal Service\b", "USPS", stripped)
    stripped = re.sub(r"\bFederal Express\b", "FedEx", stripped)

    # 6. Cut at clause boundaries or narrative timing markers
    _MONTH_PAT = r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)"
    clause_pat = rf"[,;.]|\s+(?:taking|hitting|reaching|costing|which|down from|compared to|fell to|dropped to|rose to|cut to|to\s+[\$0-9]|on\s+{_MONTH_PAT}|on\s+\d+|before\b|after\b|since\b|during\b)"
    clause = re.split(clause_pat, stripped, flags=re.I)[0].strip()

    # Clean action verbs like 'dropped', 'cut', 'claims'
    cleaned = re.sub(r"\b(?:dropped|cut|slashed|claims)\b", "", clause, flags=re.I).strip(" ,;:—.-/")

    if len(cleaned) > 28 and " for " in cleaned.lower():
        cleaned = re.split(r"\s+for\s+", cleaned, flags=re.I)[0].strip()

    res = cleaned if len(cleaned) >= 3 else clause
    if not res:
        res = figure

    # Strip dangling trailing prepositions/conjunctions
    dangling = re.compile(r"\s+(?:to|for|in|of|and|or|by|with|at|the|a|an)\s*$", flags=re.I)
    while dangling.search(res):
        res = dangling.sub("", res).strip(" ,;:—.-/")

    res = re.sub(r"\s+", " ", res).strip()

    if len(res) <= cg.LABEL_MAX:
        return res[0].upper() + res[1:] if len(res) > 1 else res.upper()

    cut = res[:cg.LABEL_MAX - 2].rsplit(" ", 1)[0].rstrip(" ,;:-")
    return (cut or res[:cg.LABEL_MAX - 2]).strip()



def chart_series(body: str) -> tuple[list[tuple[str, float, str]], str]:
    """(items, notes) — the series the numbers section states, and what was left out and why.

    The points are returned even when there are too few to chart (the ≥2 rule lives in
    `inject_chart`), because a caller reporting "0 chartable points" when the artifact has one is
    just as misleading as inventing the second.
    """
    block = numbers_block(body)
    if not block:
        return [], "no `**By the numbers:**` section — nothing to chart"
    items: list[tuple[str, float, str]] = []
    skipped: list[str] = []
    for bullet in _bullets(block):
        lead = _BOLD_LEAD.match(bullet)
        if not lead:
            skipped.append(f"no bold figure: {bullet[:40]}")
            continue
        figure, rest = lead.group("lead"), lead.group("rest")
        fig_pct = _PCT.search(figure)
        if not fig_pct:
            skipped.append(f"not a percentage: {figure[:24]}")
            continue
        if _PCT.search(rest):                       # a second % in the same sentence = a comparison
            skipped.append(f"states a second figure, so it is a comparison not a series point: {figure}")
            continue
        value = float(fig_pct.group(1).replace(",", "."))
        if value > 100:
            # A rate above 100% is growth over a base, not a share of one; plotting it on the same
            # 0-100 axis as the shares beside it is a wrong comparison dressed as a chart.
            skipped.append(f"above 100%, so it is a growth rate not a share: {figure}")
            continue
        label = clean_metric_label(figure, rest)
        citations = " ".join(re.findall(r"\[\d+\]", rest or ""))
        items.append((label, value, citations))

    if len(items) < 2:
        return items, (f"{len(items)} chartable percentage point(s) in the numbers section "
                       f"({'; '.join(skipped[:3]) or 'no bullets'}) — emitting none rather than "
                       f"inventing a series")
    return items[:CHART_MAX_POINTS], ("skipped: " + "; ".join(skipped) if skipped else "")


def inject_chart(md: str, subtitle: str = CHART_SUBTITLE, force: bool = False,
                 title: str | None = None) -> tuple[str, str]:
    """(markdown, note). Idempotent: an artifact that already carries an <svg> is left alone.

    `title` is the caller's headline for the chart. It is only consulted when the markdown carries
    no frontmatter — see `_chart_title` for why that case is real.
    """
    if re.search(r"<svg\b", md, re.I):
        if not force:
            return md, "chart already present — left alone"
        md = re.sub(r"\s*<svg[\s\S]*?</svg>\s*", "\n\n", md)


    series, notes = chart_series(md)
    if len(series) < CHART_MIN_POINTS:
        return md, f"no chart: {notes}"

    chart_title = _chart_title(md, title)
    svg = cg.generate_svg_bar_chart(chart_title, series, subtitle=subtitle)

    match = _NUMBERS_HEADING.search(md)
    if not match:
        return md, f"no chart: {notes}"
    # Insert after the numbers bullet block, so the chart sits with the figures it charts.
    end = match.end()
    for line in md[match.end():].splitlines(keepends=True):
        if line.strip() and not _BULLET.match(line) and _SECTION_BREAK.match(line.strip()):
            break
        end += len(line)
    out = md[:end].rstrip("\n") + "\n\n" + svg + "\n\n" + md[end:].lstrip("\n")
    return out, (f"chart added: {len(series)} point(s) — {', '.join(l for l, _, _ in series)}"
                 + (f" | {notes}" if notes else ""))


def _chart_title(md: str, title: str | None = None) -> str:
    """The chart's headline: the artifact's own, else the caller's, else the body's first H1.

    The fallbacks are not hypothetical. `publish.apply_derived_assets` splits the frontmatter off
    BEFORE it injects the chart, so on the pipeline's own path the markdown has no frontmatter at
    all — which is how a chart titled "Verified figures" (a generic caption about nothing) reached
    the CMS on every article generated that way. A caller that holds the artifact's headline passes
    it in; a caller that does not gets the body's own top heading.
    """
    fm, body = split_frontmatter(md)
    for candidate in (fm.get("meta_title"), fm.get("title"), title):
        if (candidate or "").strip():
            return str(candidate).strip()
    heading = re.search(r"^#\s+(.+?)\s*$", body, re.M)
    return heading.group(1).strip() if heading else "Verified figures"


# ─────────────────────────────────────────────────────────────────────────────
# SEO metadata
# ─────────────────────────────────────────────────────────────────────────────

def _lead_paragraph(body: str) -> str:
    """The article's first real paragraph — the same source the CMS excerpt falls back to."""
    for block in re.sub(r"^---.*?---", "", body, flags=re.S).split("\n"):
        text = block.strip()
        if not text or text.startswith(("#", "|", ">", "-", "*", "```", "<!--")):
            continue
        text = re.sub(r"\[([^\]]+)\]\([^)\s]+\)", r"\1", text)
        text = re.sub(r"\[\d+\]", "", text)          # inline [1] citation markers
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"[*`_]", "", text)
        text = re.sub(r"\s+([.,;:])", r"\1", text)   # a marker removed mid-sentence leaves " ."
        text = re.sub(r"\s+", " ", text).strip()
        if len(text.split()) >= 8:
            return text
    return ""


def _trim_words(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[:limit].rsplit(" ", 1)[0].rstrip(" ,;:—-") + "…"


def derive_meta_description(body: str, target: int = META_DESC_TARGET) -> str:
    """A description built from the article's own lead paragraph, trimmed on a word boundary.

    Whole sentences are preferred over a mid-clause cut, because this string becomes the CMS excerpt
    and the frontends' `<meta name="description">`: a truncated fragment reads as broken metadata,
    while one or two complete lead sentences read as a summary. Only when the first sentence alone
    overruns the budget is it trimmed on a word boundary.
    """
    lead = _lead_paragraph(body)
    if not lead:
        return ""
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", lead) if s.strip()]
    if not sentences:
        return ""
    if len(sentences[0]) > target:
        return _trim_words(sentences[0], target)
    out = sentences[0]
    for sentence in sentences[1:]:
        if len(out) + 1 + len(sentence) > target:
            break
        out = f"{out} {sentence}"
    return out


def ensure_seo_metadata(fm: dict[str, str], body: str) -> tuple[dict[str, str], list[str]]:
    """Fill meta_title / meta_description + provenance. A value the artifact already carries wins."""
    notes: list[str] = []
    title = (fm.get("title") or "").strip()
    if not (fm.get("meta_title") or "").strip() and title:
        fm["meta_title"] = _trim_words(title, META_TITLE_MAX)
        fm["meta_title_source"] = "derived_from_title"
        notes.append(f"meta_title derived from the title ({len(fm['meta_title'])} chars)")
    if not (fm.get("meta_description") or "").strip():
        desc = derive_meta_description(body)
        if desc:
            fm["meta_description"] = desc
            fm["meta_description_source"] = "derived_from_lead"
            notes.append(f"meta_description derived from the lead paragraph ({len(desc)} chars)")
        else:
            notes.append("no meta_description could be derived: no lead paragraph found")
    return fm, notes


# ─────────────────────────────────────────────────────────────────────────────
# whole-artifact pass (what the publish path calls)
# ─────────────────────────────────────────────────────────────────────────────

def ensure_assets(md: str, chart: bool = True, force_chart: bool = False,
                  title: str | None = None) -> tuple[str, list[str]]:
    """Enrich an artifact: frontmatter SEO fields + an inline chart. Returns (markdown, notes).

    `title` is the chart's headline, for a body that carries no frontmatter of its own (the shape
    the CMS row holds, and the shape `publish.apply_derived_assets` passes down). Ignored when the
    markdown has a frontmatter title of its own.
    """
    fm, body = split_frontmatter(md)
    fm, notes = ensure_seo_metadata(fm, body)
    md = _reemit_frontmatter(fm, body, md)
    if chart:
        md, note = inject_chart(md, force=force_chart, title=title)
        notes.append(note)
    return md, notes


def _reemit_frontmatter(fm: dict[str, str], body: str, md: str) -> str:
    """The document with ONLY the keys this pass added appended to its frontmatter.

    The frontmatter is YAML and `split_frontmatter` is a line-based `key: value` reader: it knows
    nothing about lists, nested mappings, comments or block scalars. Rebuilding the block from that
    dict therefore DESTROYED a real artifact's `sources:` list — `sources: ""` plus a broken
    `- https: "//…"` line (three artifacts, the first time this CLI was pointed at the whole
    corpus) — and flipped the quoting of every key the pipeline had written quoted, so a run that
    changed nothing reported every file as rewritten. So the block is preserved LINE FOR LINE and
    only genuinely new keys are appended; nothing this pass did not add is re-serialised.
    """
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n*", md, re.S)
    if not match:
        return md
    block = match.group(1)
    present = {line.split(":", 1)[0].strip() for line in block.splitlines() if ":" in line}
    additions = [(key, value) for key, value in fm.items() if key not in present]
    if not additions:
        return md                      # nothing derived: the artifact is returned byte-identical
    lines = block.rstrip("\n").splitlines()
    for key, value in additions:
        lines.append(f'{key}: "{value}"' if not re.fullmatch(r"[\w.+-]+", str(value))
                     else f"{key}: {value}")
    return "---\n" + "\n".join(lines) + "\n---\n\n" + body.lstrip("\n")


# ─────────────────────────────────────────────────────────────────────────────
# CLI — report (default) or write in place
# ─────────────────────────────────────────────────────────────────────────────

def _report(path: pathlib.Path) -> tuple[bool, list[str]]:
    md = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(md)
    notes: list[str] = []
    complete = True
    if not (fm.get("meta_title") or "").strip():
        complete = False
        notes.append("meta_title: MISSING")
    if not (fm.get("meta_description") or "").strip():
        complete = False
        notes.append("meta_description: MISSING")
    series, reason = chart_series(md)
    if re.search(r"<svg\b", md, re.I):
        notes.append("chart: present")
    elif len(series) >= CHART_MIN_POINTS:
        complete = False
        notes.append(f"chart: CHARTABLE ({len(series)} points) but not embedded")
    else:
        notes.append(f"chart: n/a — {reason}")
    return complete, notes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("files", nargs="*", help="article markdown files")
    parser.add_argument("--apply", action="store_true", help="write the assets into the files")
    parser.add_argument("--force-chart", action="store_true", help="regenerate chart even if <svg> exists")
    parser.add_argument("--title", default=None,
                        help="the chart's headline for a body with no frontmatter of its own "
                             "(the shape a CMS row holds); ignored when the file carries a title")
    parser.add_argument("--check", action="store_true", help="exit 1 when an asset is missing")
    args = parser.parse_args()

    if not args.files:
        parser.error("pass at least one markdown file")

    incomplete = 0
    for raw in args.files:
        path = pathlib.Path(raw)
        text = path.read_text(encoding="utf-8")
        check_only = args.check and not args.apply
        if not check_only and args.apply:
            enriched, notes = ensure_assets(text, force_chart=args.force_chart, title=args.title)
            if enriched != text:
                path.write_text(enriched, encoding="utf-8")
            print(f"  {path.name}")
            for n in notes:
                print(f"    - {n}")
            print(f"    - {'written' if enriched != text else 'already complete (no change)'}")
        else:
            complete, notes = _report(path)
            incomplete += 0 if complete else 1
            print(f"  {path.name}")
            for n in notes:
                print(f"    - {n}")

    if args.check and incomplete:
        print(f"\nFAIL: {incomplete} artifact(s) missing derived SEO metadata or an available chart")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
