#!/usr/bin/env python3
"""The Vibe Marketing lexicon, re-checked at the publish gate.

The copy contract lives in ONE data file (`context/vibe/lexicon.json`, vendored from the
vibe-marketing spec). This module applies the half a machine can settle to an article body:
forbidden AI-isms, throat-clearing openers, and the exception mask that keeps real domain terms
("test harness", "EmPOWER", "landscape design", "leverage ratio") from tripping it.

Two rules keep it honest:
  * it scores the READER-FACING body only (`check_accessibility.body_of`), never frontmatter or the
    Sources list;
  * it grandfathers by artifact date — `enforced_from` in the lexicon — so a standard that lands
    today scores old work but never rewrites or holds it.

Failures are returned as strings in the same shape as `publish_gate.text_failures`; notes are
returned separately so a caller can report grandfathered hits without failing them.
"""
from __future__ import annotations

import json
import pathlib
import re

LEXICON_PATH = pathlib.Path(__file__).resolve().parent.parent / "context" / "vibe" / "lexicon.json"
_DATE = re.compile(r"(\d{4}-\d{2}-\d{2})")


def _lexicon() -> dict:
    try:
        return json.loads(LEXICON_PATH.read_text())
    except FileNotFoundError:
        return {}


def enforced_from() -> str:
    """The first artifact date the lexicon holds to. Missing lexicon => enforce nothing new."""
    return _lexicon().get("enforced_from", "9999-12-31")


def artifact_date(path: pathlib.Path | str, text: str | None = None) -> str | None:
    """The artifact's own date: the filename stamp first, then a frontmatter `date:`."""
    m = _DATE.search(pathlib.Path(path).name)
    if m:
        return m.group(1)
    if text:
        m = re.search(r"^date:\s*['\"]?(\d{4}-\d{2}-\d{2})", text, re.M)
        if m:
            return m.group(1)
    return None


def _mask(text: str, exceptions: list[str]) -> str:
    for pattern in exceptions:
        text = re.sub(pattern, lambda m: " " * len(m.group(0)), text)
    return text


def _sentences(text: str) -> list[str]:
    """Reader sentences, in reading order.

    Blockquotes are other people's words; the contract governs the writer's prose. Headings are
    structure (the headline gate owns the title), so a heading never counts as an opening line —
    without this, `## At a glance` glued itself to the next sentence and hid a "Welcome to…".
    """
    out: list[str] = []
    para: list[str] = []

    def flush() -> None:
        if para:
            joined = re.sub(r"\s+", " ", " ".join(para)).strip()
            out.extend(s.strip() for s in re.split(r"(?<=[.!?])\s+", joined) if s.strip())
            para.clear()

    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith(">"):
            flush()
            continue
        if re.match(r"^#{1,6}\s", s) or s.startswith("<!--"):
            flush()
            continue
        if re.match(r"^([-*+]|\d+\.)\s+", s):
            flush()
            s = re.sub(r"^([-*+]|\d+\.)\s+", "", s)
        para.append(s.replace("**", "").replace("__", ""))
    flush()
    return out


def check(text: str, *, path: pathlib.Path | str = "artifact.md") -> tuple[list[str], list[str]]:
    """(failures, notes). Failures hold the article; notes are grandfathered or advisory.

    An artifact dated before `enforced_from` has every hit demoted to a note.
    """
    lex = _lexicon()
    if not lex:
        return [], [f"vibe lexicon missing at {LEXICON_PATH}"]
    body = _mask(text, lex.get("exceptions", []))
    date = artifact_date(path, text)
    grandfathered = bool(date and date < enforced_from())

    hits: list[str] = []
    for rule in lex.get("banned", []):
        m = re.search(rule["pattern"], body, re.I)
        if m:
            hits.append(f"vibe: '{m.group(0).strip()}' — {rule.get('label', rule['id'])}")

    openers = [(rule, re.compile(rule["pattern"], re.I)) for rule in lex.get("openers", [])]
    for sentence in _sentences(body):
        for rule, rx in openers:
            if rx.search(sentence):
                hits.append(f"vibe: opener '{sentence[:60]}…' — {rule.get('label', rule['id'])}")
                break

    if not hits:
        return [], []
    if grandfathered:
        return [], [f"{h} (grandfathered: {date} < {enforced_from()})" for h in hits]
    return hits, []
