#!/usr/bin/env python3
"""The reviewer's mechanical contract: did the rewrite keep the facts, and did it read better?

Why this file exists
--------------------
Loop 3 replaces a whole article with one model call, so a bad rewrite *is* the published artifact.
The rules that stop that were prose: `skills/claude_humanizer.md` §7 carries 25+ hand-audited
pitfall classes ("a share-of-a-base figure is the first casualty of compaction", "audit each
figure's unit noun", "audit derived intervals"), and every one of them is a manual diff after the
fact. Measured over the 216 committed draft/final pairs, the classes recur at the rate of human
attention — 128/216 rewrites dropped at least one figure — and the prose quality the pass exists to
improve moved the wrong way: sentence-length variance fell in 159/216, filler density rose in
108/216. `check_accessibility.py` cannot see either: it gates Flesch and acronyms and advises on the
*mean* sentence length and the share of very short sentences, all of which a body of uniformly
15-word sentences satisfies.

So this module is the part of the review that is not a judgement call:

  * `ledger()`  — what may not move: figures (with the sentence each sits in), `[n]` citations,
                  quoted strings, `## Sources` lines.
  * `audit()`   — hard failures (a figure lost, a figure invented, a citation dropped, a quote or
                  source line altered, a marker missing, a body under the floor, leaked
                  deliberation, a self-graded gate report left in the artifact) and flow numbers
                  (rhythm variance, staccato rate, filler/hedge/abstraction density, repetition,
                  restatement, section-opener sameness, boilerplate observer cues).
  * `score()`   — order two candidate rewrites, so a retry loop keeps the best attempt, not the last.
  * `feedback()` — the exact lines to hand back to the model: the missing figure *and the draft
                  sentence it came from*, the rhythm delta, the repeated phrases.

Subject-agnostic by construction: it reads the artifact's own numbers and the artifact's own prose.
No vertical, no vocabulary, no network.

    python3 scripts/review_audit.py --draft context/drafts/x_draft.md --final context/drafts/x_final.md
    python3 scripts/review_audit.py --draft A --final B --brief context/recon_proposals/x_verified_brief.md
    python3 scripts/review_audit.py --draft A --final B --json
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import statistics
import sys

MIN_BODY_WORDS = 500

# ------------------------------------------------------------------------------------- text shape

_FRONTMATTER = re.compile(r"^---\s*\n.*?\n---\s*\n", re.S)
_MARKER = re.compile(r"<!--\s*(lead|tension|tactical-insight|nuanced-takeaway|tldr)\s*-->", re.I)
_SOURCES = re.compile(r"^##\s*Sources\s*$", re.M | re.I)
_GATE_REPORT = re.compile(r"^##\s*Gate report\s*$", re.M | re.I)
_ISO_DATE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
_URL = re.compile(r"https?://\S+")

MARKERS = ("lead", "tension", "tactical-insight", "nuanced-takeaway", "tldr")

# Phrases that name the task instead of doing it (the monologue failure), plus template slots.
LEAK_PATTERNS = (
    r"\bthe user (?:wants|asks|wanted|provided)\b",
    r"\blet me (?:analy[sz]e|think|re-?read|rewrite)\b",
    r"\bI need to\b",
    r"\bmy job is\b",
    r"\bthe instructions? (?:say|says)\b",
    r"\bthat seems like the best approach\b",
    r"\[(?:table|3 bolded bullets|n bolded bullets)\b",
    r"\bSection \d+ header\b",
    r"\.\.\. content\.\.\.",
)

# The observer cue is required by the voice gate as a *kind* (any first-person observation). These
# four phrasings became the desk's default and now appear in 29-56 artifacts each, which is the
# clearest sign a reader gets that one template wrote the corpus.
BOILERPLATE_CUES = (
    "the part i keep circling",
    "the catch my read is that",
    "what strikes me here is",
    "what i'd watch i am watching",
    "my read is that",
    "what i'd watch next",
)

FILLER = ("really", "actually", "clearly", "essentially", "basically", "significantly",
          "incredibly", "remarkably", "importantly", "notably", "substantially", "fundamentally",
          "ultimately", "interestingly", "simply", "very", "quite", "truly", "honestly")
HEDGE = ("may", "might", "could", "possibly", "arguably", "seems", "appears", "perhaps",
         "some might", "it could be said", "tends to", "potentially", "likely", "somewhat")
ABSTRACT = ("leverage", "utilize", "utilise", "optimize", "optimise", "streamline", "robust",
            "holistic", "paradigm", "synergy", "ecosystem", "landscape", "framework", "capability",
            "alignment", "initiative", "impactful", "transformative", "nuanced", "multifaceted")

SCALES = {"k": 1e3, "thousand": 1e3, "m": 1e6, "million": 1e6, "bn": 1e9, "b": 1e9,
          "billion": 1e9, "t": 1e12, "trillion": 1e12}

_FIGURE = re.compile(
    r"(?<![\w.])(?P<cur>\$)?(?P<num>\d[\d,]*(?:\.\d+)?)\s?"
    r"(?P<scale>trillion|billion|million|thousand|bn|k|m|b|t)\b"
    r"|(?<![\w.])(?P<cur2>\$)?(?P<num2>\d[\d,]*(?:\.\d+)?)\s?(?P<pct>%)?",
    re.I,
)


def body(text: str) -> str:
    """Reader-facing prose only: no frontmatter, sources, related links, comments or headings."""
    t = _FRONTMATTER.sub("", text or "")
    t = _SOURCES.split(t)[0]
    t = _GATE_REPORT.split(t)[0]
    t = re.sub(r"<!--[\s\S]*?-->", " ", t)
    return t


def prose_paragraphs(text: str) -> list[str]:
    """Paragraphs of running prose (bullets, headings and tables are shape, not prose)."""
    out = []
    for block in re.split(r"\n\s*\n", body(text)):
        b = block.strip()
        if not b or b.startswith(("#", "-", "*", "|", "<", ">", "!", "`")):
            continue
        if re.fullmatch(r"[-*_]{3,}", b):
            continue
        out.append(b)
    return out


def sentences(text: str) -> list[str]:
    """Sentences from running prose only — bullets and headings excluded from rhythm."""
    prose = " ".join(prose_paragraphs(text))
    parts = re.split(r"(?<=[.!?])[\"'”’]?\s+", prose)
    return [p.strip() for p in parts if len(p.split()) >= 2]


def sections(text: str) -> dict[str, str]:
    """Body keyed by section marker."""
    t = _FRONTMATTER.sub("", text or "")
    parts = _MARKER.split(t)
    out: dict[str, str] = {}
    for i in range(1, len(parts), 2):
        out[parts[i].lower()] = parts[i + 1] or ""
    return out


# --------------------------------------------------------------------------------------- figures

def _clean_number(raw: str) -> str:
    return raw.replace(",", "").strip()


def _load_bearing(num: str, pct: bool, cur: bool) -> bool:
    """A decimal, a percentage, a money amount or a count >= 13 is a measurement.

    Small integers (a list length, "5 of 7") are prose furniture; a year is a date, not a claim.
    """
    if pct or cur or "." in num:
        return True
    try:
        value = float(num)
    except ValueError:
        return False
    if value.is_integer() and 1900 <= value <= 2100:
        return False
    return value >= 13


def figures(text: str, *, with_context: bool = False) -> dict[str, dict]:
    """Measured figures in `text`, keyed by a stable id, with value and the sentence they sit in.

    `$1,175`, `1175` and `$1175` are one figure; `22,269` and `22269` are one; `13.41` stays exact.
    Scale words fold into the value (`2.084T` -> 2.084e12) and the raw decimal is kept as an alias.
    """
    clean = _URL.sub(" ", _ISO_DATE.sub(" ", text or ""))
    out: dict[str, dict] = {}
    for m in _FIGURE.finditer(clean):
        num = _clean_number(m.group("num") or m.group("num2") or "")
        if not num:
            continue
        pct = bool(m.group("pct"))
        cur = bool(m.group("cur") or m.group("cur2"))
        scale = (m.group("scale") or "").lower()
        mult = SCALES.get(scale, 1.0)
        try:
            value = float(num) * mult
        except ValueError:
            continue
        if not _load_bearing(num, pct, cur or bool(scale)):
            continue
        key = f"{num}{scale}{'%' if pct else ''}"
        entry = out.setdefault(key, {"key": key, "num": num, "value": value, "pct": pct,
                                     "money": cur, "scale": scale, "hits": 0, "context": ""})
        entry["hits"] += 1
        if with_context and not entry["context"]:
            entry["context"] = _sentence_around(clean, m.start(), m.end())
    return out


def _sentence_around(text: str, start: int, end: int, limit: int = 260) -> str:
    """The sentence a figure sits in, for feedback that quotes the claim.

    Boundaries are punctuation *followed by whitespace*, so a decimal ("6.89") never splits its own
    sentence — the first version cut every context at the point, which made the retry feedback
    read "the figure is 6." and told the model less than the number did.
    """
    left = max(text.rfind(sep, 0, start) for sep in (". ", "! ", "? ", "\n"))
    left = 0 if left < 0 else left + 2
    rights = [i for i in (text.find(sep, end) for sep in (". ", "! ", "? ", "\n")) if i != -1]
    right = min(rights) + 1 if rights else len(text)
    return re.sub(r"\s+", " ", text[left:right]).strip()[:limit]


def _present(fig: dict, other: dict[str, dict]) -> str:
    """How `fig` survives in `other`: '' (lost), 'exact', or 'rounded'."""
    if fig["key"] in other:
        return "exact"
    for cand in other.values():
        if cand["key"] == fig["key"]:
            return "exact"
        if fig["value"] and abs(cand["value"] - fig["value"]) <= max(
                0.5, abs(fig["value"]) * 0.01):
            return "rounded"
    return ""


# ---------------------------------------------------------------------------------------- quotes

def quotes(text: str) -> list[str]:
    """Quoted spans of four or more words — a source's words are content, not style."""
    out = []
    for m in re.finditer(r"[\"“]([^\"”]{20,400})[\"”]", body(text)):
        span = m.group(1).strip()
        if len(span.split()) >= 4:
            out.append(re.sub(r"\s+", " ", span))
    return out


def source_lines(text: str) -> list[str]:
    m = re.search(r"^##\s*Sources\s*$", text or "", re.M | re.I)
    if not m:
        return []
    tail = text[m.end():]
    tail = _GATE_REPORT.split(tail)[0]
    return [re.sub(r"\s+", " ", ln).strip() for ln in tail.splitlines() if ln.strip()]


# ----------------------------------------------------------------------------------- flow metrics

def _density(words: list[str], lexicon: tuple[str, ...]) -> float:
    flat = [w.lower().strip(".,;:!?") for w in words]
    hits = sum(1 for w in flat if w in lexicon)
    return round(1000.0 * hits / max(len(flat), 1), 2)


def _phrases(text: str) -> list[tuple[str, ...]]:
    ws = re.findall(r"[a-z']+", body(text).lower())
    return [tuple(ws[i:i + 5]) for i in range(len(ws) - 4)]


def rhythm(text: str) -> dict:
    sents = sentences(text)
    lens = [len(s.split()) for s in sents]
    if not lens:
        return {"sentences": 0, "mean": 0.0, "sd": 0.0, "short_pct": 0.0}
    return {
        "sentences": len(lens),
        "mean": round(statistics.mean(lens), 1),
        "sd": round(statistics.pstdev(lens), 1),
        "short_pct": round(100.0 * sum(1 for n in lens if n <= 8) / len(lens), 1),
    }


def rhythm_health(text: str) -> float:
    """0..1: does the prose have a human sentence rhythm, not just a healthy average?

    Raw variance alone is gameable — one 50-word run-on beside three short sentences scores a wide
    spread and reads terribly. So the score is the product of three honest conditions: the spread is
    real (sd >= ~4 and growing), the average sits where connected prose sits (13-24 words), and the
    tail is not pathological (few sentences past 40 words). It is a shape, not a target to hit: a
    rewrite is compared against its own draft, never against an absolute ideal.
    """
    sents = sentences(text)
    lens = [len(s.split()) for s in sents]
    if len(lens) < 4:
        return 0.0
    mean = statistics.mean(lens)
    sd = statistics.pstdev(lens)
    long_share = sum(1 for n in lens if n > 40) / len(lens)
    spread = max(0.0, min(1.0, (sd - 3.0) / 4.5))
    centre = max(0.0, 1.0 - abs(mean - 18.0) / 14.0)
    tail = max(0.0, 1.0 - long_share / 0.2)
    return round(spread * centre * tail, 3)


def paragraph_shape(text: str) -> dict:
    paras = prose_paragraphs(text)
    counts = [len(sentences(p)) for p in paras] if paras else []
    staccato = sum(1 for p in paras
                   if sentences(p) and all(len(s.split()) <= 10 for s in sentences(p)))
    return {"paragraphs": len(paras),
            "mean_sentences": round(statistics.mean(counts), 1) if counts else 0.0,
            "staccato_share": round(100.0 * staccato / max(len(paras), 1), 1)}


def repetition(text: str) -> dict:
    grams = _phrases(text)
    seen: dict[tuple[str, ...], int] = {}
    for g in grams:
        seen[g] = seen.get(g, 0) + 1
    # A repeated gram that is only stopwords or only one content word is ordinary English.
    stop = {"the", "a", "an", "of", "to", "and", "in", "is", "it", "that", "for", "on", "as",
            "at", "by", "with", "be", "this", "from", "or", "are", "was", "but", "not"}
    repeats = {g: c for g, c in seen.items()
               if c >= 3 and len([w for w in g if w not in stop]) >= 2}
    return {"repeated_5grams": len(repeats),
            "worst": sorted(((" ".join(g), c) for g, c in repeats.items()),
                            key=lambda x: -x[1])[:5]}


def duplicate_sentences(text: str, min_words: int = 8) -> dict:
    """Sentences repeated word-for-word — a stutter no writer leaves in a finished piece.

    The 2026-10-27 reviewer output carried the same 27-word sentence in the tension and the
    tactical section, which is what "restating instead of developing" looks like mechanically.
    """
    import collections
    seen: collections.Counter = collections.Counter()
    for s in sentences(text):
        key = re.sub(r"\s+", " ", s).strip().lower()
        if len(key.split()) >= min_words:
            seen[key] += 1
    dupes = {s: c for s, c in seen.items() if c > 1}
    return {"count": len(dupes), "examples": [s[:140] for s in list(dupes)[:3]]}


def section_openers(text: str) -> dict:
    """First four words of each section's opening paragraph — identical openers read as a template."""
    openers = []
    for name in MARKERS:
        s = sections(text).get(name, "")
        paras = prose_paragraphs(s)
        if paras:
            openers.append((name, " ".join(paras[0].split()[:4]).lower().strip(",:")))
    dupes = {w for _, w in openers if sum(1 for _, x in openers if x == w) > 1} if openers else set()
    return {"openers": openers, "duplicate_openers": sorted(dupes)}


_THESIS_STOP = {"the", "a", "an", "of", "to", "and", "in", "is", "it", "that", "for", "on", "as",
                "at", "by", "with", "be", "this", "from", "or", "are", "was", "but", "not", "its",
                "their", "they", "you", "your", "we", "our", "has", "have", "had", "will", "than",
                "so", "if", "then", "there", "which", "what", "when", "how", "who", "more", "less"}


def _content_words(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z]{4,}", text.lower()) if w not in _THESIS_STOP}


def restatement(text: str) -> dict:
    """How many sections restate the article's own thesis (the lead's core claim), beyond two.

    A reader experiences this as one idea said five times: the same failure as a repeated figure,
    one level up. The threshold is 2 because the lead states the claim and the glance card summarises
    it — a third section restating it is repetition, not development.
    """
    lead = sections(text).get("lead", "") or body(text)
    first = sentences(lead)[0] if sentences(lead) else ""
    thesis = _content_words(first)
    if len(thesis) < 3:
        return {"sections_restating": 0, "restating": []}
    hits = []
    for name in MARKERS:
        s = sections(text).get(name, "")
        if not s:
            continue
        words = _content_words(s)
        if thesis and len(thesis & words) / len(thesis) >= 0.75:
            hits.append(name)
    return {"sections_restating": len(hits), "restating": hits}


# Mirrors site/social_voice.mjs OBSERVER_CUES (the node gate verify.sh §9 runs). Three kinds: an
# observation the writer made, an opinion labelled as one, or attention named as attention. Keeping a
# copy here lets the reviewer hold its own output offline; if the JS patterns change, change these.
OBSERVER_CUE_RES = (
    # Any first-person verb — see site/social_voice.mjs: a closed verb list failed honest prose.
    re.compile(r"\bI(?:'ve|'m|'d|'ll)\b|\bI\s+[a-z']", re.I),
    re.compile(r"\b(?:my read|my take|my sense|my view|where I(?:'ve| have) landed|"
               r"what I take from|I could be wrong)\b", re.I),
    re.compile(r"\b(?:what I(?:'m| am) watching|what strikes me|the bit that stuck with me|"
               r"the thing I(?:'d| would) want|curious (?:how|what|whether|if))\b", re.I),
)

INTERPRETING = ("tension", "tactical-insight", "nuanced-takeaway")


def observer_cues(text: str) -> dict:
    """Which interpreting sections carry a first-person cue — the §3.9 voice contract, offline."""
    secs = sections(text)
    missing, present = [], []
    for name in INTERPRETING:
        body = re.sub(r"<!--[\s\S]*?-->", " ", secs.get(name, "") or "")
        if not body.strip():
            continue  # an absent section is the schema's business, not the voice gate's
        if any(r.search(body) for r in OBSERVER_CUE_RES):
            present.append(name)
        else:
            missing.append(name)
    return {"missing": missing, "present": present}


def cue_boilerplate(text: str) -> dict:
    low = body(text).lower()
    hits = [c for c in BOILERPLATE_CUES if c in low]
    return {"boilerplate_cues": hits, "count": len(hits)}


def leaked(text: str) -> dict:
    prose = body(text)
    hits = [p for p in LEAK_PATTERNS if re.search(p, prose, re.I)]
    gate_report = bool(_GATE_REPORT.search(text or ""))
    return {"patterns": hits, "gate_report": gate_report}


def flow(text: str) -> dict:
    words = re.findall(r"[A-Za-z']+", body(text))
    return {
        "words": len(words),
        "rhythm": rhythm(text),
        "rhythm_health": rhythm_health(text),
        "paragraphs": paragraph_shape(text),
        "repetition": repetition(text),
        "duplicates": duplicate_sentences(text),
        "openers": section_openers(text),
        "restatement": restatement(text),
        "cues": cue_boilerplate(text),
        "filler": _density(words, FILLER),
        "hedge": _density(words, HEDGE),
        "abstraction": _density(words, ABSTRACT),
    }


# ---------------------------------------------------------------------------------------- ledger

def ledger(draft: str, brief: str = "") -> dict:
    """Everything a rewrite must keep, taken from the draft (and the verified brief as authorised)."""
    return {
        "figures": figures(body(draft), with_context=True),
        "authorised": figures(brief or ""),
        "citations": _citation_counts(draft),
        "quotes": quotes(draft),
        "sources": source_lines(draft),
        "markers": [m for m in MARKERS if re.search(rf"<!--\s*{m}\s*-->", draft, re.I)],
    }


def _citation_counts(text: str) -> dict[str, int]:
    out: dict[str, int] = {}
    for m in re.finditer(r"\[(\d{1,2})\]", text or ""):
        out[m.group(1)] = out.get(m.group(1), 0) + 1
    return out


# ------------------------------------------------------------------------------------------ audit

def audit(draft: str, final: str, brief: str = "", *, min_words: int | None = None) -> dict:
    """Compare a rewrite to its draft. Returns {"hard": [...], "advisories": [...], "flow": {...}}.

    `min_words` is the publishable-length floor (default `MIN_BODY_WORDS`); a caller auditing a
    fixture passes 0 rather than inflating the fixture into a fake article.
    """
    led = ledger(draft, brief)
    hard: list[str] = []
    adv: list[str] = []

    f_figs = figures(body(final))
    for key, fig in led["figures"].items():
        how = _present(fig, f_figs)
        if how:
            continue
        hard.append(f"figure lost: {key} — the draft sentence: \"{fig['context'][:220]}\"")

    for key, fig in f_figs.items():
        if _present(fig, led["figures"]):
            continue
        if _present(fig, led["authorised"]):
            continue
        adv.append(f"figure not in the draft or the brief: {key} — confirm it is the source's own")

    f_cites = _citation_counts(final)
    for n, count in led["citations"].items():
        if n not in f_cites:
            hard.append(f"citation [{n}] dropped (the draft cited it {count}×)")
    for n in f_cites:
        if n not in led["citations"]:
            hard.append(f"citation [{n}] invented — the draft has no such source marker")

    f_body = body(final).lower()
    for q in led["quotes"]:
        if q.lower() not in f_body and q.lower() not in body(draft).lower():
            hard.append(f"quoted source text altered: \"{q[:120]}\"")

    f_src = " ".join(source_lines(final))
    for line in led["sources"]:
        url = _URL.search(line)
        token = url.group(0) if url else line[:60]
        if token and token not in f_src:
            hard.append(f"source line altered or dropped: {token}")

    for m in led["markers"]:
        if not re.search(rf"<!--\s*{m}\s*-->", final, re.I):
            hard.append(f"section marker <!-- {m} --> dropped")

    words = len(re.findall(r"[A-Za-z']+", body(final)))
    floor = MIN_BODY_WORDS if min_words is None else min_words
    if floor and words < floor:
        hard.append(f"body is {words} words, under the {floor}-word floor")

    dupes = duplicate_sentences(final)
    for example in dupes["examples"]:
        hard.append(f"a sentence is repeated verbatim: \"{example}\" — say it once, develop it "
                    f"where it belongs")

    cues = observer_cues(final)
    for name in cues["missing"]:
        where = re.sub(r"\s+", " ", prose_paragraphs(sections(final).get(name, ""))[0])[:150] \
            if prose_paragraphs(sections(final).get(name, "")) else "(the section is empty)"
        hard.append(f"<!-- {name} --> carries no first-person sentence — it currently opens "
                    f"\"{where}…\". The body is one person commenting, so this section needs one "
                    f"observation, labelled opinion or attention cue in the writer's own words")

    leak = leaked(final)
    if leak["patterns"]:
        hard.append(f"leaked deliberation: {', '.join(leak['patterns'])}")
    if leak["gate_report"]:
        hard.append("the artifact carries a self-graded `## Gate report` — that is the model "
                    "grading itself, not a gate; strip it into the review report")

    d_flow, f_flow = flow(draft), flow(final)
    dsd, fsd = d_flow["rhythm"]["sd"], f_flow["rhythm"]["sd"]
    reg: list[str] = []

    def regression(msg: str) -> None:
        """A flow change that made the piece worse than its own draft — fixed before shipping."""
        adv.append(msg)
        reg.append(msg)

    if dsd and fsd < dsd * 0.85:
        regression(f"rhythm flattened: sentence-length sd {dsd} -> {fsd} "
                   f"(kept {100 * fsd / dsd:.0f}% of the draft's variance)")
    if d_flow["rhythm_health"] and f_flow["rhythm_health"] < d_flow["rhythm_health"] - 0.05:
        regression(f"rhythm health fell {d_flow['rhythm_health']} -> {f_flow['rhythm_health']} "
                   f"(mean {d_flow['rhythm']['mean']} -> {f_flow['rhythm']['mean']} words, "
                   f"sd {dsd} -> {fsd}) — vary sentence length and break any run-on past 40 words")
    if f_flow["filler"] > d_flow["filler"] + 0.25:
        regression(f"filler density rose: {d_flow['filler']} -> {f_flow['filler']} per 1,000 words")
    if f_flow["hedge"] > d_flow["hedge"] + 0.25:
        regression(f"hedge density rose: {d_flow['hedge']} -> {f_flow['hedge']} per 1,000 words")
    if f_flow["repetition"]["repeated_5grams"] > max(3, d_flow["repetition"]["repeated_5grams"]):
        regression(f"repetition rose: {d_flow['repetition']['repeated_5grams']} -> "
                   f"{f_flow['repetition']['repeated_5grams']} repeated 5-grams")
    if f_flow["restatement"]["sections_restating"] > 2:
        regression("the through-line is restated in "
                   f"{f_flow['restatement']['sections_restating']} sections "
                   f"({', '.join(f_flow['restatement']['restating'])}) — develop it, do not repeat it")
    if f_flow["cues"]["count"]:
        regression("boilerplate observer cue(s): " + ", ".join(f_flow["cues"]["boilerplate_cues"]))
    if f_flow["openers"]["duplicate_openers"]:
        regression("sections open with the same words: "
                   + ", ".join(f_flow["openers"]["duplicate_openers"]))
    if f_flow["paragraphs"]["staccato_share"] > 20:
        regression(f"{f_flow['paragraphs']['staccato_share']}% of paragraphs are all short "
                   f"declaratives — that reads as a list, not an argument")

    return {
        "ok": not hard,
        "hard": hard,
        "advisories": adv,
        "regressions": reg,
        "flow": f_flow,
        "draft_flow": d_flow,
        "cues": cues,
        "ledger": {"figures": len(led["figures"]), "citations": len(led["citations"]),
                   "quotes": len(led["quotes"]), "sources": len(led["sources"])},
    }


def score(result: dict) -> tuple:
    """Order candidate rewrites: no hard failures first, then a better flow delta."""
    f, d = result["flow"], result["draft_flow"]
    gain = 0.0
    gain += 8.0 * (f["rhythm_health"] - d["rhythm_health"])
    gain += 1.0 * (d["filler"] - f["filler"])
    gain += 0.6 * (d["hedge"] - f["hedge"])
    gain -= 0.4 * f["repetition"]["repeated_5grams"]
    gain -= 0.8 * f["cues"]["count"]
    gain -= 1.0 * max(0, f["restatement"]["sections_restating"] - 2)
    gain -= 0.5 * f["paragraphs"]["staccato_share"] / 10
    return (len(result["hard"]) == 0, -len(result["hard"]), round(gain, 2))


def feedback(result: dict) -> list[str]:
    """The retry lines: what failed, and the draft's own sentence that carries the lost fact."""
    lines = []
    for h in result["hard"]:
        lines.append(f"- FAIL {h}")
    for a in result["advisories"]:
        lines.append(f"- FIX  {a}")
    return lines


# -------------------------------------------------------------------------------------------- cli

def main() -> int:
    ap = argparse.ArgumentParser(description="Audit a rewrite against its draft")
    ap.add_argument("--draft", required=True)
    ap.add_argument("--final", required=True)
    ap.add_argument("--brief", default="")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    draft = pathlib.Path(args.draft).read_text(encoding="utf-8")
    final = pathlib.Path(args.final).read_text(encoding="utf-8")
    brief = pathlib.Path(args.brief).read_text(encoding="utf-8") if args.brief else ""
    result = audit(draft, final, brief)
    if args.json:
        print(json.dumps(result, indent=2))
        return 0 if result["ok"] else 1

    f, d = result["flow"], result["draft_flow"]
    print(f"review audit: {pathlib.Path(args.final).name}")
    print(f"  words {d['words']} -> {f['words']}   "
          f"rhythm sd {d['rhythm']['sd']} -> {f['rhythm']['sd']} (mean "
          f"{d['rhythm']['mean']} -> {f['rhythm']['mean']})   short% "
          f"{d['rhythm']['short_pct']} -> {f['rhythm']['short_pct']}")
    print(f"  filler {d['filler']} -> {f['filler']}   hedge {d['hedge']} -> {f['hedge']}   "
          f"abstraction {d['abstraction']} -> {f['abstraction']}")
    print(f"  repeated 5-grams {d['repetition']['repeated_5grams']} -> "
          f"{f['repetition']['repeated_5grams']}   restated sections "
          f"{d['restatement']['sections_restating']} -> {f['restatement']['sections_restating']}")
    print(f"  ledger: {result['ledger']}")
    for h in result["hard"]:
        print(f"  FAIL {h}")
    for a in result["advisories"]:
        print(f"  ~    {a}")
    print("  => " + ("PASS" if result["ok"] else "FAIL"))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
