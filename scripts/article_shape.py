#!/usr/bin/env python3
"""The desk's article-shape standard — the rules a reader-facing piece has to keep, on any vertical.

These came out of a reader-side critique of a live article (2026-10-24) that no gate could see: the
opening spent three statutory clocks before it named the stakes, two sections repeated the same six
figures, and nothing in the body tied the story to a decision the reader could act on. Each of those
is a shape, not a subject — so the checks below take no vertical, no category and no vocabulary from
one story. They read the artifact's own structure.

Enforced from `enforced_from` in context/article_shape.json; older artifacts are reported only.

    python3 scripts/article_shape.py --report published/*.md
    python3 scripts/article_shape.py --check published/2026-10-24_x.md
"""
from __future__ import annotations

import argparse
import datetime
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "context" / "article_shape.json"

DEFAULT_REGISTRY = {
    "version": 1,
    "enforced_from": "2026-10-24",
    "why": "Reader-side review, 2026-10-24: an opening that spent its first sentences on statutory "
           "detail, two sections repeating the same figures, and no tie to a decision the reader "
           "could act on. Shape rules apply to every vertical.",
    # A figure may set up the story and be summarised in the tldr. Beyond that it is repetition.
    "max_body_sections_per_figure": 2,
    # The conclusion has to land somewhere the reader can go: one inline link inside the body
    # (the generated Related-reading block does not count — every article has one).
    "min_body_inline_links": 1,
    "advisory": {
        "max_figures_in_first_sentence": 1,
        "require_why_clause": True,
        "suggest_table_at_shared_figures": 3,
    },
}

MARKERS = ("lead", "tension", "tactical-insight", "nuanced-takeaway", "tldr")
_MARKER_RE = re.compile(r"<!--\s*(lead|tension|tactical-insight|nuanced-takeaway|tldr)\s*-->")
_NUMBER = r"\d[\d,\.]*"
_UNITS = {
    "percent": r"(?:%|percent|per cent)",
    "days": r"(?:days?|day\b)",
    "months": r"(?:months?)",
    "years": r"(?:years?)",
    "weeks": r"(?:weeks?)",
    "hours": r"(?:hours?)",
    "money": r"(?:\$|usd|dollars?)",
}
_FIGURE_RES = [
    (name, re.compile(rf"(?<![\w.]){_NUMBER}[\s-]*{unit}\b", re.I)) for name, unit in _UNITS.items()
]
_MONEY_RE = re.compile(rf"\$\s?{_NUMBER}(?:\s?(?:million|billion|thousand|k|m|bn)\b)?", re.I)
_LINK_RE = re.compile(r"\[[^\]]+\]\((/[^)\s]+)\)")


def _registry() -> dict:
    try:
        data = json.loads(REGISTRY.read_text())
    except (OSError, json.JSONDecodeError):
        return dict(DEFAULT_REGISTRY)
    merged = {**DEFAULT_REGISTRY, **{k: v for k, v in data.items() if k in DEFAULT_REGISTRY}}
    merged["advisory"] = {**DEFAULT_REGISTRY["advisory"], **(data.get("advisory") or {})}
    return merged


def article_date(text: str, path: pathlib.Path | None = None) -> str:
    """The artifact's own date, from the frontmatter or the filename prefix."""
    match = re.search(r'^date:\s*"?([0-9]{4}-[0-9]{2}-[0-9]{2})', text, re.M)
    if match:
        return match.group(1)
    if path is not None:
        match = re.match(r"([0-9]{4}-[0-9]{2}-[0-9]{2})", path.name)
        if match:
            return match.group(1)
    return ""


def enforced_for(date: str, registry: dict | None = None) -> bool:
    """Only artifacts dated on/after the standard are held; the corpus before it is grandfathered."""
    start = (registry or _registry()).get("enforced_from") or "9999-12-31"
    return bool(date) and date >= start


def _strip_sources(text: str) -> str:
    return re.split(r"^##\s*Sources", text, flags=re.M | re.I)[0]


def sections(text: str) -> dict[str, str]:
    """The five reader-facing sections, by marker. Anything before the first marker is ignored."""
    body = _strip_sources(text)
    marks = list(_MARKER_RE.finditer(body))
    out: dict[str, str] = {}
    for i, match in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(body)
        out[match.group(1)] = body[match.end():end]
    return out


def figures(text: str) -> set[str]:
    """Normalised figures (value + unit family). `120 days` and `120-day` are the same figure."""
    found: set[str] = set()
    for name, pattern in _FIGURE_RES:
        for match in pattern.finditer(text):
            value = re.sub(r"[,\s]", "", match.group(0))
            value = re.sub(_UNITS[name], "", value, flags=re.I).strip("-\u2014. ")
            if value:
                found.add(f"{value}:{name}")
    for match in _MONEY_RE.finditer(text):
        value = re.sub(r"[\s,]", "", match.group(0)).lower()
        found.add(f"{value}:money")
    return found


def _first_sentence(text: str) -> str:
    flat = re.sub(r"\s+", " ", re.sub(r"\[[0-9]+\]", "", text)).strip()
    match = re.match(r"(.+?[.!?])(?:\s|$)", flat)
    return match.group(1) if match else flat


def _why_clause(text: str) -> bool:
    """A cause or an actor before the detail: because/as/since/after/due to/driven by/following."""
    flat = re.sub(r"\s+", " ", text[:600]).lower()
    return bool(re.search(r"\b(because|as|since|after|due to|driven by|following|amid|while|"
                          r"when|as soon as)\b", flat))


def problems(text: str, *, registry: dict | None = None) -> dict:
    """{"fails": [...], "advisories": [...], "held": bool} for one artifact."""
    reg = registry or _registry()
    held = enforced_for(article_date(text), reg)
    parts = sections(text)
    fails: list[str] = []
    advisories: list[str] = []

    # 1. A figure is stated once, where it earns its place. The lead may set it up and the tldr may
    #    summarise it; a third body section repeating it is scroll friction, not emphasis.
    limit = int(reg.get("max_body_sections_per_figure", 2))
    body_keys = [k for k in MARKERS if k not in ("tldr",) and k in parts]
    counts: dict[str, list[str]] = {}
    for key in body_keys:
        for figure in figures(parts[key]):
            counts.setdefault(figure, []).append(key)
    for figure, where in sorted(counts.items()):
        if len(where) > limit:
            fails.append(f"figure {figure.replace(':', ' ')} is restated in {len(where)} sections "
                         f"({', '.join(where)}) — state it once, where it earns its place")
    shared = None
    for i, first in enumerate(body_keys):
        for second in body_keys[i + 1:]:
            common = figures(parts[first]) & figures(parts[second])
            if len(common) >= int(reg["advisory"].get("suggest_table_at_shared_figures", 3)):
                shared = (first, second, sorted(common))
    if shared:
        first, second, common = shared
        advisories.append(
            f"'{first}' and '{second}' share {len(common)} figures ({', '.join(common[:4])}) — "
            f"consider one comparison table instead of two prose lists")

    # 2. The opening states the stakes before the mechanism: one figure at most in the first
    #    sentence, and a cause inside the first two sentences (advisory — a rule that cannot see
    #    paraphrase must not score).
    lead = parts.get("lead", "")
    if lead:
        first = _first_sentence(lead)
        if len(figures(first)) > int(reg["advisory"].get("max_figures_in_first_sentence", 1)):
            advisories.append(f"the opening sentence carries {len(figures(first))} figures — lead "
                              f"with the stakes and move the numbers into the body")
        if reg["advisory"].get("require_why_clause") and not _why_clause(lead):
            advisories.append("the opening never says WHY the change is happening (because / after / "
                              "driven by / following) — a reader cannot weigh a rule without it")

    # 3. The conclusion lands somewhere the reader can act. The generated Related-reading list does
    #    not count: every article has one, so it proves nothing.
    body_only = _MARKER_RE.sub("", _strip_sources(text))
    body_only = re.split(r"<!--\s*internal-links", body_only)[0]
    links = [m.group(1) for m in _LINK_RE.finditer(body_only)]
    if len(links) < int(reg.get("min_body_inline_links", 1)):
        fails.append(f"the body carries no inline internal link — close on the decision the reader "
                     f"can act on and link it (the generated Related-reading block does not count)")

    return {"fails": fails, "advisories": advisories, "held": held}


def failures(path: pathlib.Path, *, registry: dict | None = None) -> list[str]:
    """The gate's view: only what may HOLD a publish (grandfathered artifacts never fail)."""
    path = pathlib.Path(path)
    try:
        text = path.read_text()
    except OSError:
        return []
    report = problems(text, registry=registry)
    if not report["held"]:
        return []
    return report["fails"]


def main() -> int:
    parser = argparse.ArgumentParser(description="The desk's article-shape standard.")
    parser.add_argument("files", nargs="*", help="artifacts to check")
    parser.add_argument("--report", action="store_true", help="one line per artifact, never fails")
    parser.add_argument("--check", action="store_true", help="exit 1 when a HELD artifact fails")
    args = parser.parse_args()
    if not args.files:
        parser.error("pass at least one artifact")
    bad = 0
    for name in args.files:
        path = pathlib.Path(name)
        report = problems(path.read_text())
        state = "HELD" if report["held"] else "legacy"
        fails, advisories = report["fails"], report["advisories"]
        if fails and report["held"]:
            bad += 1
        print(f"[{'FAIL' if fails and report['held'] else 'ok  '}] {path.name} ({state})")
        for failure in fails:
            print(f"        - {failure}")
        for advisory in advisories:
            print(f"        ~ {advisory}")
    return 1 if (args.check and bad) else 0


if __name__ == "__main__":
    raise SystemExit(main())
