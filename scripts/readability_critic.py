#!/usr/bin/env python3
"""The reader-side critic — the four checks a piece gets before it is final.

Why this exists (owner, 2026-11-06): the writer stage can clear every existing gate and still
produce copy that is *hard to read* — sentences that parse on the second pass, a timeline explained
three times, bullets carrying two competing statistics, and a closing paragraph that names a rule
the reader has never been told about. None of that is a Flesch problem (the rhythm is fine, the
citations resolve), so nothing held it.

The standard is `skills/story_draft.md` §2-§4 and `skills/claude_humanizer.md` §3.11-§3.13:

  1. STRUCTURE  — At a glance sits immediately below the lede, not at the foot of the piece, and the
                  five marked sections run lead → tldr → tension → tactical → catch.
  2. BULLETS    — one metric per bullet, one sentence, 25 words or fewer, in At a glance and
                  By the numbers.
  3. CITATIONS  — at most one [n] tag per sentence, and `## Sources` as a vertical list.
  4. PROSE      — the read-twice test (three prepositional phrases in a row, abstract symmetry
                  "more X than Y is Z"), a timeline stated once, and no cold late-stage concept in
                  the closing paragraph.

1-3 are deterministic and HOLD a publish (a wrong order or a two-statistic bullet is not a matter
of taste). 4 is advisory: a rule that cannot see paraphrase must not hold a piece, so its findings
are printed for the rewrite and the reviewer, never used to reject. Artifacts dated before
`enforced_from` are grandfathered — reported, never held (house convention, owner 2026-10-10).

    python3 scripts/readability_critic.py --check published/x.md
    python3 scripts/readability_critic.py --report published/*.md
    python3 scripts/readability_critic.py --json context/drafts/x_final.md
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "context" / "readability_critic.json"

DEFAULT_REGISTRY = {
    "version": 1,
    "enforced_from": "2026-11-06",
    "why": "Owner report 2026-11-06: the articles are hard to read. Riddle syntax, a timeline "
           "explained more than once, bullets packing two statistics, and closings that name a rule "
           "the body never introduced. Structure, bullet and citation rules hold the push; prose "
           "findings are advisory and go back through the rewrite.",
    # Which classes may hold a publish. The prose classes stay advisory: they are heuristics over
    # grammar, and a heuristic that cannot see paraphrase must never reject an article.
    "hold": ["structure", "bullets", "citations"],
    "at_a_glance_max_words": 50,
    "bullet_max_words": 25,
    "max_citations_per_sentence": 1,
}

MARKER_ORDER = ("lead", "tldr", "tension", "tactical-insight", "nuanced-takeaway")
LABELS = ("The shift", "The number", "The risk")
_MARKER_RE = re.compile(r"<!--\s*(lead|tension|tactical-insight|nuanced-takeaway|tldr)\s*-->", re.I)
_FM_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.S)
_CITE_RE = re.compile(r"\[(\d+)\]")
_BULLET_RE = re.compile(r"^[ \t]*[-*][ \t]+(.+)$", re.M)

_PREPS = frozenset({"in", "on", "at", "for", "from", "with", "by", "under", "over", "through",
                    "against", "between", "across", "within", "without", "during", "into", "onto",
                    "upon", "of", "to", "per", "about", "than", "like", "via", "among", "around",
                    "behind", "beyond"})
_MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September",
           "October", "November", "December")
_MONTH_RE = re.compile(r"\b(" + "|".join(m[:3] for m in _MONTHS) + r")[a-z]*\.?\s+(\d{1,2})\b")
_DAY_MONTH_RE = re.compile(r"\b(\d{1,2})\s+(" + "|".join(m[:3] for m in _MONTHS) + r")[a-z]*\b",
                           re.I)
_ISO_RE = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
_WEEKDAY_RE = re.compile(r"^\W{0,3}(?:at\s+\d{1,2}(?::\d{2})?\s*(?:a\.?m\.?|p\.?m\.?)?\s*(?:on\s+)?)?"
                         r"(?:mon|tues|wednes|thurs|fri|satur|sun)day\b", re.I)


# ------------------------------------------------------------------------------- registry

def _registry() -> dict:
    try:
        data = json.loads(REGISTRY.read_text())
    except (OSError, json.JSONDecodeError):
        return dict(DEFAULT_REGISTRY)
    merged = {**DEFAULT_REGISTRY, **{k: v for k, v in data.items() if k in DEFAULT_REGISTRY}}
    return merged


def article_date(text: str, path: pathlib.Path | None = None) -> str:
    match = re.search(r'^date:\s*"?([0-9]{4}-[0-9]{2}-[0-9]{2})', text, re.M)
    if match:
        return match.group(1)
    if path is not None:
        match = re.match(r"([0-9]{4}-[0-9]{2}-[0-9]{2})", pathlib.Path(path).name)
        if match:
            return match.group(1)
    return ""


def enforced_for(date: str, registry: dict | None = None) -> bool:
    start = (registry or _registry()).get("enforced_from") or "9999-12-31"
    return bool(date) and date >= start


# ------------------------------------------------------------------------------- text shapes

def raw_body(text: str) -> str:
    """The body with its section markers intact, and the machine blocks removed."""
    body = _FM_RE.sub("", text)
    body = re.sub(r"<svg\b.*?</svg>", "", body, flags=re.S | re.I)
    body = re.split(r"^##\s*Related reading\s*$", body, flags=re.M | re.I)[0]
    return re.split(r"^##\s*Sources\s*$", body, flags=re.M | re.I)[0]


def body_of(text: str) -> str:
    """Reader-facing prose: no frontmatter, sources, Related-reading block, SVG, or machine
    comments (`internal-link hint`, block delimiters) — those inflate a word count and are not
    prose a reader ever sees."""
    return re.sub(r"<!--.*?-->", "", raw_body(text), flags=re.S)


def sections(text: str) -> list[tuple[str, str]]:
    """[(marker, section_text)] in document order — the order itself is what check 1 reads."""
    body = raw_body(text)
    marks = list(_MARKER_RE.finditer(body))
    out = []
    for i, match in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(body)
        out.append((match.group(1).lower(), body[match.end():end]))
    return out


def section_map(text: str) -> dict[str, str]:
    """First occurrence wins, so a duplicated marker cannot hide behind a later one."""
    out: dict[str, str] = {}
    for name, chunk in sections(text):
        out.setdefault(name, chunk)
    return out


def sentences(text: str) -> list[str]:
    prose = "\n".join(line for line in text.splitlines() if not line.lstrip().startswith("#"))
    flat = re.sub(r"\s+", " ", re.sub(r"<!--.*?-->", "", prose)).strip()
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", flat) if s.strip()]


def _strip_markup(s: str) -> str:
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", s)
    return re.sub(r"[*_`>#]", "", s).strip()


# ------------------------------------------------------------------------------- 1. structure

def structure_findings(text: str, reg: dict) -> list[str]:
    fails: list[str] = []
    order = [name for name, _ in sections(text)]
    if not order:
        return ["no section markers found — the five marked sections are lead / tldr / tension / "
                "tactical-insight / nuanced-takeaway"]
    missing = [m for m in MARKER_ORDER if m not in order]
    if missing:
        fails.append("missing section marker(s): " + ", ".join(f"<!-- {m} -->" for m in missing))

    seen = [m for m in order if m in MARKER_ORDER]
    if seen != [m for m in MARKER_ORDER if m in seen]:
        fails.append("sections are out of order (" + " → ".join(seen) + ") — the reader needs the "
                     "executive summary immediately below the lede: lead → tldr → tension → "
                     "tactical-insight → nuanced-takeaway")

    if "tldr" in order and order.index("tldr") > 1:
        fails.append(f"'At a glance' sits at position {order.index('tldr') + 1} of the body — it "
                     f"belongs immediately under the lede, before the chronology")

    glance = section_map(text).get("tldr", "")
    if glance:
        clean = re.sub(r"<!--.*?-->", "", glance, flags=re.S)
        lacking = [label for label in LABELS if label.lower() not in clean.lower()]
        if lacking:
            fails.append("'At a glance' is missing its line(s): " + ", ".join(lacking)
                         + " — three lines: The shift / The number / The risk")
        words = len(_strip_markup(re.sub(r"^#+.*$", "", clean, flags=re.M)).split())
        limit = int(reg.get("at_a_glance_max_words", 50))
        if words > limit:
            fails.append(f"'At a glance' runs {words} words (cap {limit}) — it is a box, not a "
                         f"second summary")
    return fails


# ------------------------------------------------------------------------------- 2. bullets

def _bullet_lead_and_body(line: str) -> tuple[str, str]:
    """Split `- **<figure> — <label>:** <sentence>` into its bold lead-in and its sentence."""
    match = re.match(r"\*\*(.+?)\*\*(.*)$", line.strip())
    if match:
        return match.group(1), match.group(2)
    return "", line


def bullets_findings(text: str, reg: dict) -> list[str]:
    """One metric per bullet, one sentence, ≤25 words — in the two scanned blocks."""
    fails: list[str] = []
    limit = int(reg.get("bullet_max_words", 25))
    parts = section_map(text)
    blocks = [("At a glance", parts.get("tldr", ""))]
    numbers = re.search(r"^##\s*By the numbers\s*$(.*?)(?=^#{1,3}\s|\Z)", body_of(text),
                        re.M | re.S | re.I)
    if numbers:
        blocks.append(("By the numbers", numbers.group(1)))
    for label, block in blocks:
        for raw in _BULLET_RE.findall(block or ""):
            line = _strip_markup(raw)
            words = len(line.split())
            if words > limit:
                fails.append(f"{label} bullet is {words} words (max {limit}): "
                             f"\"{_short(line)}\"")
            body_text = re.sub(r"^\*\*.+?\*\*", "", raw)
            if len(re.findall(r"[.!?](?:\s|$)", body_text.strip())) > 1:
                fails.append(f"{label} bullet carries more than one sentence: "
                             f"\"{_short(line)}\"")
            lead, _ = _bullet_lead_and_body(raw)
            figures = re.findall(r"\d[\d,\.]*\s*(?:%|percent|x\b|bn\b|m\b|k\b)?", lead)
            if len(figures) > 1:
                fails.append(f"{label} bullet packs {len(figures)} figures into one lead-in "
                             f"(one metric per bullet): \"{_short(lead or line)}\"")
    return fails


def _short(s: str, n: int = 90) -> str:
    flat = re.sub(r"\s+", " ", s).strip()
    return flat if len(flat) <= n else flat[: n - 1].rstrip() + "…"


# ------------------------------------------------------------------------------- 3. citations

def citation_findings(text: str, reg: dict) -> list[str]:
    fails: list[str] = []
    limit = int(reg.get("max_citations_per_sentence", 1))
    for sentence in sentences(body_of(text)):
        tags = _CITE_RE.findall(sentence)
        if len(tags) > limit:
            fails.append(f"{len(tags)} citation tags in one sentence "
                         f"({', '.join('[' + t + ']' for t in tags)}) — keep the primary source: "
                         f"\"{_short(sentence)}\"")
    block = re.split(r"^##\s*Sources\s*$", text, flags=re.M | re.I)
    if len(block) < 2:
        return fails
    footer = block[1]
    entries = len(re.findall(r"^[ \t]*(?:\[\d+\]|\d+[.)])\s+\S", footer, re.M))
    if entries < 2 and len(_CITE_RE.findall(footer)) >= 2:
        fails.append("`## Sources` is a run-on paragraph — render it as a vertical list "
                     "(`1. <name> — <url>` on its own line)")
    return fails


# ------------------------------------------------------------------------------- 4. prose

def read_twice_findings(text: str) -> list[str]:
    """Sentences that do not parse on the first read: stacked prepositional phrases, or the
    abstract symmetry of \"more X than Y is Z\" / \"a gate is one function rather than a share\"."""
    out: list[str] = []
    breakers = {",", ";", ":", "—", "–", "and", "but", "not", "or", "yet", "so"}
    for sentence in sentences(text):
        words = re.findall(r"[A-Za-z][A-Za-z'-]*|[,;:—–]", sentence)
        groups: list[list[int]] = []
        for i, word in enumerate(words):
            if word.lower() not in _PREPS:
                continue
            if groups:
                prev = groups[-1][-1]
                between = [w.lower() for w in words[prev + 1:i]]
                # A stacked chain modifies one head ("on the rate for the box in the yard"); parallel
                # phrases separated by a comma or a conjunction are not the defect.
                joined = (i - prev) <= 3 and not any(b in breakers for b in between)
                if joined:
                    groups[-1].append(i)
                    continue
            groups.append([i])
        run = max((len(g) for g in groups), default=0)
        if run >= 3:
            out.append(f"{run} prepositional phrases in a row — \"{_short(sentence)}\"")
        if re.search(r"\b(?:more|less|deeper|longer|shorter|higher|lower|bigger|smaller|faster|"
                     r"slower|wider|tighter)\s+[^.]{0,40}\bthan\b[^.]{0,40}\b(?:is|are|was|were)\b",
                     sentence, re.I):
            out.append(f"abstract comparison (\"more X than Y is Z\") — say it as subject → verb → "
                       f"object: \"{_short(sentence)}\"")
        elif re.search(r"\b(?:is|are|was|were)\s+(?:a|an|the|one)\b[^.]{0,60}\brather than\b",
                       sentence, re.I):
            out.append(f"abstract symmetry (\"X is one Y rather than a Z\") — name the concrete "
                       f"consequence instead: \"{_short(sentence)}\"")
    return out


def timeline_findings(text: str) -> list[str]:
    """The calendar is established once, in the opening. After that: the operational window."""
    out: list[str] = []
    body = body_of(text)
    order = sections(text)
    per_section: dict[str, list[str]] = {}
    for name, chunk in order:
        if name == "tldr":
            # The glance box summarises the piece; the timeline is set in the body sections.
            continue
        # A heading may name the date (it is a signpost); it is not a second explanation.
        chunk = "\n".join(line for line in chunk.splitlines() if not line.lstrip().startswith("#"))
        found = [f"{m.group(1).title()} {int(m.group(2))}" for m in _MONTH_RE.finditer(chunk)]
        found += [f"{m.group(2).title()} {int(m.group(1))}" for m in _DAY_MONTH_RE.finditer(chunk)]
        found += [m.group(0) for m in _ISO_RE.finditer(chunk)]
        per_section[name] = found
    seen_once: dict[str, list[str]] = {}
    totals: dict[str, int] = {}
    for name, found in per_section.items():
        for date in found:
            totals[date] = totals.get(date, 0) + 1
            if name not in seen_once.setdefault(date, []):
                seen_once[date].append(name)
    for date, where in sorted(seen_once.items()):
        if len(where) > 1:
            out.append(f"the date {date} is explained in {len(where)} sections "
                       f"({', '.join(where)}) — set the timeline once in the opening, then refer "
                       f"to the operational window")
        elif totals.get(date, 0) > 1:
            out.append(f"the date {date} is stated {totals[date]} times — set the timeline once in "
                       f"the opening, then refer to the operational window")
    # An ambiguous relative day before the calendar exists.
    first_absolute = min((m.start() for m in _MONTH_RE.finditer(body)), default=None)
    for para in re.split(r"\n\s*\n", body):
        p = para.strip()
        if not p or p.startswith(("#", "-", "*", ">", "|")):
            continue
        if _WEEKDAY_RE.match(p):
            at = body.find(p[:40])
            if first_absolute is None or at < first_absolute:
                out.append(f"a paragraph opens on an ambiguous relative day before any calendar "
                           f"date: \"{_short(p)}\"")
            break
    return out


_STOP = {"the", "a", "an", "of", "and", "for", "with", "from", "that", "this", "these", "those",
         "its", "their", "his", "her", "was", "were", "has", "have", "had", "have", "not", "but",
         "you", "your", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
         "ten", "than", "then", "when", "what", "which", "who", "how", "why", "all", "any"}


def closing_findings(text: str) -> list[str]:
    """No cold concept in the last paragraph: an orphan reference is a rule, a clock or a link the
    body never introduced."""
    out: list[str] = []
    body = body_of(text)
    paras = [p.strip() for p in re.split(r"\n\s*\n", body)
             if p.strip() and not p.strip().startswith(("#", "-", "*", ">", "|", "<"))]
    if not paras:
        return out
    closing = paras[-1]
    earlier = body[: body.rfind(closing)].lower()
    for match in re.finditer(r"\bthe\s+((?:[a-z0-9][\w'-]*\s+){0,3}[a-z0-9][\w'-]*)", closing, re.I):
        phrase = match.group(1).strip()
        if not re.search(r"\d", phrase):
            continue
        content = [w for w in re.findall(r"[a-z][\w'-]*", phrase.lower())
                   if w not in _STOP and len(w) > 3]
        if not content:
            continue
        # The head noun (the last significant word) is what a reader must already hold.
        if content[-1] not in earlier:
            out.append(f"the closing paragraph names \"the {phrase}\" and no earlier sentence "
                       f"introduces it — add a 5-10 word inline bridge")
    for match in re.finditer(r"\b(?:this|these|those)\s+([a-z][\w'-]*)", closing, re.I):
        noun = match.group(1).lower()
        if noun not in _STOP and noun not in earlier:
            out.append(f"the closing paragraph says \"{match.group(0)}\" with no antecedent — "
                       f"name the thing again")
    return out


# ------------------------------------------------------------------------------- api

def findings(text: str, *, registry: dict | None = None) -> dict:
    """{"fails": [...], "advisories": [...], "held": bool, "by_class": {...}}."""
    reg = registry or _registry()
    held = enforced_for(article_date(text), reg)
    hold = set(reg.get("hold") or [])
    by_class = {
        "structure": structure_findings(text, reg),
        "bullets": bullets_findings(text, reg),
        "citations": citation_findings(text, reg),
        "read_twice": read_twice_findings(body_of(text)),
        "timeline": timeline_findings(text),
        "closing": closing_findings(text),
    }
    fails: list[str] = []
    advisories: list[str] = []
    for name, items in by_class.items():
        if name in hold:
            fails += [f"{name}: {i}" for i in items]
        else:
            advisories += [f"{name}: {i}" for i in items]
    return {"fails": fails, "advisories": advisories, "held": held, "by_class": by_class}


def failures(path: pathlib.Path, *, registry: dict | None = None) -> list[str]:
    """The publish gate's view: only what may HOLD a push; grandfathered artifacts never fail."""
    path = pathlib.Path(path)
    try:
        text = path.read_text()
    except OSError:
        return []
    return failures_for_text(text, registry=registry)


def failures_for_text(text: str, *, registry: dict | None = None) -> list[str]:
    """Same rule, for text a caller already holds — no temp file needed."""
    report = findings(text, registry=registry)
    return report["fails"] if report["held"] else []


def advisories(path: pathlib.Path, *, registry: dict | None = None) -> list[str]:
    try:
        text = pathlib.Path(path).read_text()
    except OSError:
        return []
    report = findings(text, registry=registry)
    return report["advisories"] if report["held"] else []


def main() -> int:
    parser = argparse.ArgumentParser(description="The reader-side critic (structure, bullets, "
                                                 "citations, prose).")
    parser.add_argument("files", nargs="*", help="artifacts to read")
    parser.add_argument("--check", action="store_true", help="exit 1 when a HELD artifact fails")
    parser.add_argument("--report", action="store_true", help="one line per artifact, never fails")
    parser.add_argument("--json", action="store_true", help="machine-readable report")
    args = parser.parse_args()
    if not args.files:
        parser.error("pass at least one artifact")
    bad = 0
    payload = []
    for name in args.files:
        path = pathlib.Path(name)
        text = path.read_text()
        report = findings(text)
        payload.append({"file": str(path), **report})
        if args.json:
            continue
        state = "HELD" if report["held"] else "legacy"
        print(f"[{'FAIL' if report['fails'] and report['held'] else 'ok  '}] {path.name} ({state})")
        for failure in report["fails"]:
            print(f"        - {failure}")
        for advisory in report["advisories"]:
            print(f"        ~ {advisory}")
        if report["fails"] and report["held"]:
            bad += 1
    if args.json:
        print(json.dumps(payload, indent=2))
    return 1 if (args.check and bad) else 0


if __name__ == "__main__":
    raise SystemExit(main())
