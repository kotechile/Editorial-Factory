#!/usr/bin/env python3
"""Topic-agnostic accessibility gate for editorial-factory articles.

Used by verify.sh and the Loop 3 humanizers. Computes the readability and
accessibility of a final/draft article body on ANY topic:

  1. Flesch Reading Ease on the article body (frontmatter, "## Sources", and the
     "<!-- linkedin -->" variant are all excluded — they are not reader-facing prose).
  2. Undefined acronyms: an ALL-CAPS token (2-8 letters) whose first body use is NOT
     accompanied by an expanded definition, i.e. no "Expanded Form (ACR)" anywhere.
  3. Jargon-density advisory (non-fatal): cross-domain gating phrases + long-word rate.

measure(path) returns a dict {verdict, flesch, undefined_acronyms, jargon, warnings, fails, ...}
so the Loop 3 humanizers can read the exact reasons and feed them back for a retry.

CLI: exit 0 = PASS, exit 1 = FAIL (Flesch below floor OR an undefined specialist acronym).
    python3 check_accessibility.py [--target 60] [--floor 50] [--json] <draft.md ...>
"""
import json
import re
import sys
import pathlib

# Config (overridable via CLI).
TARGET = 60.0  # advisory: aim here for "plain English" (broader audience)
FLOOR = 50.0   # hard-fail below this (difficult / specialist reading level)

# Sentence-rhythm floor (advisory). A body of short declaratives scores well on Flesch and reads
# like a list of one-liners; these thresholds are what the Loop 3 retry prompt uses to ask for
# joined sentences instead of more splitting.
RHYTHM_MEAN_MIN = 14.5    # mean words per sentence, below which the body reads as choppy
RHYTHM_SHORT_MAX = 20.0   # % of sentences at RHYTHM_SHORT_WORDS or fewer
RHYTHM_SHORT_WORDS = 8

# Figure load (advisory). A piece can clear Flesch 60 and still be unreadable because every prose
# sentence is a step in a chain of arithmetic: measured on the 269 published artifacts, the median
# share of prose sentences carrying a figure was 41%, and 95 of them sat above 45% (worst: 89%).
# That is the "the numbers are right but the text does not flow" failure the owner reports, and
# Flesch cannot see it: numbers are short, low-syllable words, so a derivation dump SCORES WELL.
# Prose only — the "By the numbers" bullets are where figures belong and are excluded.
FIGURE_DENSITY_MAX = 45.0  # % of prose sentences carrying a figure

# Acronyms that are universally understood and do not need a definition for a general reader.
# Everything else, if left undefined at first use, is a FAIL. This is what makes the gate
# topic-agnostic: any new domain acronym must be spelled out once.
COMMON = {
    "US", "UK", "EU", "AI", "CEO", "CFO", "COO", "CTO", "GDP", "EPS", "IT", "TV", "PC",
    "OK", "ID", "R&D", "FBI", "CIA", "NASA", "NFL", "Q1", "Q2", "Q3", "Q4", "vs", "etc",
}

# Well-known names written in caps that are NOT acronyms (brands/programs). Kept small;
# the mixed/lowercase test in undefined_acronyms removes most of these generically.
NOT_ACRONYM = {
    "ENERGY", "STAR",
    # SQL / code keywords that appear in caps but are not abbreviations
    "SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "ALTER", "FROM", "WHERE",
    "JOIN", "AND", "OR", "NOT", "NULL", "TRUE", "FALSE", "TABLE", "INTO", "VALUES", "SET",
    "GROUP", "ORDER", "DISTINCT", "HAVING", "UNION", "WHEN", "THEN", "ELSE", "WITH", "AS",
    "RETURN", "BREAK", "CONTINUE", "CLASS", "STATIC", "PUBLIC", "PRIVATE", "VOID",
}

# Cross-domain gating phrases (advisory only — never hard-fails). These recur across
# finance / legal / customs / trade / tech writing and tend to block a general reader.
# They are a hint to the humanizer to find a plain equivalent or add a gloss.
GATING = sorted({
    "non-recurring", "add-back", "non-GAAP", "gross margin", "pass-through",
    "protective action", "importers of record", "of record", "reconciliation entry",
    "unliquidated", "finally-liquidated", "statute of limitations", "fiscal Q3",
    "fiscal Q4", "fiscal-third-quarter", "YTD", "run rate", "revenue recognition",
    "Section 232", "Section 301", "cost of sales", "cost of goods sold",
    "SELECT", "INSERT", "UPDATE", "DELETE",  # code keywords in prose — jargon for a general reader
})


# ── specialist shorthand and metric terms (HARD fail) ────────────────────────────────────────
# The acronym rule above sees only ALL-CAPS tokens, so a reader-hostile token like "F1", "p95" or
# "R@10" is invisible to it: one capital letter and a digit is not a word the regex can call an
# acronym, and it is not expanded anywhere either. Observed 2026-11-03 on
# your-dedupe-cut-f1-by-74: the title and body both lean on "F1" and "dedupe pass", neither is
# explained, and every gate passed — Flesch 61, no undefined acronyms, jargon list silent.
#
# Membership rule: a term earns a place here only when a general reader cannot follow the sentence
# without knowing it AND the word has no ordinary-English reading that would make a gloss noise.
# "recall", "token" and "latency" fail the second test (product recall, token gesture, latency is
# everyday), so they stay advisory rather than holding a publish.
SPECIALIST = {
    "F1": r"\bF-?1\b",
    "dedupe": r"\bdedup(?:e|es|ed|ing|lication)\b",
    "classifier": r"\bclassifiers?\b",
    "test set": r"\b(?:test|evaluation|eval)\s+sets?\b",
    "synthetic data": r"\bsynthetic\s+(?:data|sets?)\b",
    "cosine similarity": r"\bcosine similarity\b",
    "embedding": r"\bembeddings?\b",
    "KV cache": r"\bKV[-\s]cache\b",
    "fine-tuning": r"\bfine-?tun(?:e|es|ed|ing)\b",
    "precision/recall": r"\bprecision\b[^.]{0,40}\brecall\b|\brecall\b[^.]{0,40}\bprecision\b",
    "percentile": r"\bp(?:50|75|90|95|99|999)\b",
}

# What counts as an explanation attached to a term. Deliberately STRUCTURAL, not a vocabulary of
# definitional verbs: "F1 — a single score that balances…" and "dedupe, which removes near-copies
# before the model sees them" both carry a clause a reader can use, and neither is going to contain
# the word "means". A parenthetical, an em-dash clause or a comma appositive of four words or more is
# the gloss; anything shorter is a label, not an explanation.
_GLOSS_AFTER = (
    re.compile(r"\((?:[^()]{15,})\)"),
    re.compile(r"[—–]\s*[^—–.;]{20,}"),
    re.compile(r",\s*(?:a|an|the|which|or)\s+[^.;:—–]{25,}"),
)


def _prose_sentences(text):
    """Reader-facing sentences with headings removed.

    A heading is not a place a gloss can live ("## The dedupe trap"), so a term whose first
    appearance is in an H2 must still be explained in the prose underneath it.
    """
    prose = "\n".join(l for l in text.splitlines() if not l.lstrip().startswith("#"))
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+", prose) if x.strip()]


def is_glossed(pattern, sentences):
    """True when the FIRST use of the term sits in a sentence that explains it.

    Only the first use is judged, and only its OWN sentence: once a reader has the explanation,
    later bare uses are the point of having explained it. A next-sentence fallback was tried and
    removed — it passed "…a dedupe pass: every diversity score rose" because the FOLLOWING sentence
    happened to contain an unrelated em-dash clause.
    """
    rx = re.compile(pattern, re.I)
    for sentence in sentences:
        m = rx.search(sentence)
        if not m:
            continue
        return any(g.search(sentence[m.end():]) for g in _GLOSS_AFTER)
    return True  # term absent from the body


def unglossed_terms(text):
    """Specialist terms used without a plain-English explanation at first use."""
    sentences = _prose_sentences(text)
    return sorted(t for t, pat in SPECIALIST.items() if not is_glossed(pat, sentences))


def body_of(path):
    t = pathlib.Path(path).read_text()
    t = re.sub(r"^---\n.*?\n---\n", "", t, flags=re.S)          # frontmatter
    t = re.sub(r"#{1,3}\s*Sources.*", "", t, flags=re.S)        # sources -> end
    t = re.sub(r"#{1,3}\s*Related reading.*", "", t, flags=re.S)  # the internal-link block the
    #   persistence pass injects AFTER Loop 3 rewrote and measured the body. It is link titles, not
    #   the article's prose, and counting it dragged 21 of 70 published artifacts under the floor
    #   (spanning ~5 points) while the per-run gate — which measures the body it actually rewrote —
    #   had passed them. Measuring it here made the desk's own floor unreproducible.
    t = re.sub(r"<!--\s*linkedin\s*-->.*", "", t, flags=re.S)   # linkedin variant
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)               # HTML section markers
    t = re.sub(r"```.*?```", " ", t, flags=re.S)                # code blocks & mermaid diagrams
    t = re.sub(r"<svg.*?</svg>", " ", t, flags=re.S)            # embedded SVG charts
    return t


def flesch(text):
    sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    words = re.findall(r"[A-Za-z][A-Za-z'\-]*", text)
    if not words:
        return None, 0, 0, 0
    syl = lambda w: max(1, len(re.findall(r"[aeiouyAEIOU]+", w)))
    w = len(words)
    s = max(1, len(sents))
    syl_total = sum(syl(x) for x in words)
    score = 206.835 - 1.015 * (w / s) - 84.6 * (syl_total / w)
    long_words = sum(1 for x in words if len(x) > 6)
    return round(score, 1), w, s, round(100.0 * long_words / w, 1)


def is_defined(acr, text):
    """True if the acronym is expanded anywhere, in either order:
    'Expanded Form (ACR)' or 'ACR (Expanded Form / phrase)'. Both are common
    conventions and both make the term followable by a general reader.
    Also accepts a trailing gloss inside the same parens — 'Full Name (ACR — gloss)'
    or 'ACR (— gloss)' — which the frontier model favors (e.g. 'Total Cost of
    Ownership (TCO—the full lifetime price of a part)')."""
    p = re.escape(acr)
    # "Expanded Form (ACR)" and "Expanded Form (ACR — gloss)": the text before the
    # paren carries the expansion; anything after the acronym inside the parens is
    # an optional plain-English gloss.
    order_a = re.compile(r"[A-Za-z][A-Za-z0-9 \-]{2,90}\(\s*" + p + r"[^)]*\)")
    # "ACR (Expanded Form / phrase)" and "ACR (— gloss)": the paren directly follows
    # the acronym and carries at least one word of explanation.
    order_b = re.compile(r"\b" + p + r"\b\s*\([^)]*[A-Za-z][^)]*\)")
    return bool(order_a.search(text) or order_b.search(text))


def _used_as_word(acr, text):
    """True if the all-caps token is also used as an ordinary word (any mixed/lower
    capitalization, e.g. 'select' vs 'SELECT'). Such a token is emphasis or a code
    keyword, not a specialist abbreviation."""
    for m in re.finditer(r"\b[A-Za-z]{1,12}\b", text):
        tok = m.group(0)
        if tok.upper() == acr and tok != acr:
            return True
    return False


def undefined_acronyms(text):
    bad = set()
    # Mixed letter+digit tokens (A2A, M2M) are invisible to an all-caps regex, and one of them — the
    # Agent-to-Agent protocol — shipped unexpanded through every gate on 2026-11-07 while the piece
    # read it as a bare "A2A" from the second section on. Only the letter-digit-letter shape is taken
    # (A2A), never a product code (H100, A100, GPT4): a part number is not an abbreviation and
    # demanding an expansion for it holds legitimate hardware copy.
    cands = re.findall(r"\b([A-Z][A-Z&]{1,7})\b", text)
    cands += re.findall(r"\b([A-Z]+[0-9]+[A-Z]+)\b", text)
    roman = re.compile(r"^[IVXLCDM]+$")  # Phase II / Phase III / etc. — ordinals, not acronyms
    for acr in set(cands):
        if len(acr) < 2:
            continue
        if acr in COMMON or acr in NOT_ACRONYM or acr.isdigit() or roman.match(acr):
            continue
        if _used_as_word(acr, text):
            continue
        if not is_defined(acr, text):
            bad.add(acr)
    return sorted(bad)


def jargon_hits(text):
    low = text.lower()
    return [g for g in GATING if g.lower() in low]


def check_smart_brevity(raw_text, body_text):
    """Diagnose Smart Brevity compliance (advisory):
    1. H2/H3 headers target <= 6 words.
    2. Paragraph sentence count: 3-5 sentences per paragraph, warn above 6.
       (Owner decision 2026-10-26: the old 1-3 cap was producing choppy, shallow prose —
       relaxing the paragraph to 3-6 sentences while keeping sentences at 15-19 words
       measured +20% length, +6 Flesch points on the same article.)
    3. Standardized context signposts: **Why it matters:**, **The big picture:**, etc.
    """
    warns = []
    # 1. H2/H3 header length
    headers = re.findall(r"^#{2,3}\s+(.+)$", raw_text, re.M)
    long_headers = []
    for h in headers:
        clean_h = h.strip()
        if clean_h.lower().startswith("sources") or clean_h.lower().startswith("gate report"):
            continue
        words = clean_h.split()
        if len(words) > 6:
            long_headers.append(f"'{clean_h}' ({len(words)}w)")
    if long_headers:
        warns.append("Smart Brevity: header > 6 words: " + "; ".join(long_headers[:2]))

    # 2. Paragraph sentence counts
    paras = [p.strip() for p in re.split(r"\n\s*\n", body_text) if p.strip()]
    long_paras = 0
    for p in paras:
        if p.startswith("#") or p.startswith("-") or p.startswith("*") or p.startswith(">") or p.startswith("```"):
            continue
        sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", p) if s.strip()]
        if len(sents) > 6:
            long_paras += 1
    if long_paras > 0:
        warns.append(f"Smart Brevity: {long_paras} paragraph(s) > 6 sentences (aim for 3-5, max 6)")

    # 3. Section headers, and the figures block. The old rule demanded the four fixed signposts
    #    ("The big picture:", "By the numbers", "What I'd watch:", "The catch") on every article, and
    #    a mandatory bold-stat block on every article. That is what made the corpus read like a deck:
    #    owner, 2026-11-03 — "less smart brevity in favour of an interesting, easy to read story".
    #    A section header is now any H2 the article writes for itself; the markers, not the words,
    #    are what the pipeline needs.
    signpost_patterns = [
        r"^##\s+\S",                                                   # any H2, narrative included
        r"\*\*Why it matters:\*\*", r"\*\*The big picture:\*\*", r"\*\*By the numbers:\*\*",
        r"\*\*Where this bites:\*\*", r"\*\*What I(?:'d| would) watch:\*\*",
        r"\*\*The catch:\*\*", r"\*\*Between the lines:\*\*", r"\*\*Yes, but:\*\*",
        r"\*\*Go deeper:\*\*", r"\*\*What's next:\*\*",
    ]
    has_signposts = any(re.search(pat, raw_text, re.I | re.M) for pat in signpost_patterns)
    if not has_signposts:
        warns.append("Smart Brevity: no section headers found — give each section an H2, in words "
                     "this article would use")

    # The figures block stays a house section (owner, 2026-11-03: relaxing it to optional removed it
    # from the page and the reader lost the block he scans). Small, though: 2-3 bullets carrying the
    # figures the prose does not state again — never the old 4-bullet recap of the body.
    if not re.search(r"(?:##\s*By the numbers|\*\*By the numbers:\*\*)", raw_text, re.I):
        warns.append("Smart Brevity: missing the '## By the numbers' block — 2-3 bullets, the figures "
                     "the prose does not restate")
    else:
        block = re.search(r"##\s*By the numbers(.*?)(?=\n#{1,3}\s|\Z)", raw_text, re.I | re.S)
        bullets = len(re.findall(r"^\s*[-*]\s", block.group(1), re.M)) if block else 0
        if bullets > 3:
            warns.append(f"Smart Brevity: the numbers block carries {bullets} bullets (keep 2-3 — the "
                         f"prose already states the rest)")

    return warns


def rhythm(text):
    """Sentence rhythm: mean length and the share of very short sentences.

    Advisory only — this is the *other* direction of the readability gate. Flesch rewards shorter
    sentences, so a pipeline that chases the score ratchets toward staccato and every mechanical
    check still passes (2026-10-22 audit: published corpus at 14.0 words/sentence with ~18% of
    sentences at 8 words or fewer, drafts already that short before Loop 3 touched them). The
    remedy the model is given is to JOIN adjacent short sentences, never to pad them longer.
    """
    sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    lens = [len(s.split()) for s in sents]
    if not lens:
        return None, None
    mean = round(sum(lens) / len(lens), 1)
    short = round(100.0 * sum(1 for x in lens if x <= RHYTHM_SHORT_WORDS) / len(lens), 1)
    return mean, short


def figure_load(text):
    """Share of PROSE sentences that carry a figure, and the prose sentence count.

    Prose = paragraphs that are not a bullet, heading, quote, table or image. The mandatory
    "By the numbers" block is bullets, so it is not counted — figures belong there. What this
    measures is the rest: paragraphs whose every sentence is another step of a derivation.
    Returns (pct, n) or (None, 0) when the body has no prose.
    """
    sents = []
    for para in re.split(r"\n\s*\n", text):
        p = para.strip()
        if not p or p[0] in "#-*>|!":
            continue
        sents += [s.strip() for s in re.split(r"(?<=[.!?])\s+", p) if len(s.split()) > 3]
    if not sents:
        return None, 0
    carrying = sum(1 for s in sents if re.search(r"\d", s))
    return round(100.0 * carrying / len(sents), 1), len(sents)


def measure(path, target=TARGET, floor=FLOOR):
    """Return a structured diagnosis of the article's accessibility. Safe to call from other
    scripts (the Loop 3 humanizers) so they can read the exact FAIL reasons and retry."""
    raw = pathlib.Path(path).read_text()
    text = body_of(path)
    score, w, s, long_rate = flesch(text)
    undef = undefined_acronyms(text)
    unglossed = unglossed_terms(text)
    jarg = jargon_hits(text)

    fails, warns = [], []
    if score is None:
        fails.append("empty body")
    else:
        if score < floor:
            fails.append(f"Flesch {score} < floor {floor}")
        elif score < target:
            warns.append(f"Flesch {score} below target {target} (still readable; tighten jargon)")
        if long_rate and long_rate > 35:
            warns.append(f"long-word rate {long_rate}% > 35% (plain-english pass recommended)")
    if undef:
        fails.append("undefined acronym(s): " + ", ".join(undef))
    if unglossed:
        # Hard fail, not advisory: a reader who does not know the term cannot read the sentence. The
        # message names the fix so the Loop 3 retry prompt hands it straight back to the model.
        fails.append("unglossed specialist term(s): " + ", ".join(unglossed)
                     + " — explain each in plain words at first use (em-dash clause or parenthesis)")
    if jarg:
        warns.append("jargon to gloss/replace: " + ", ".join(jarg))

    # Smart Brevity structural check
    sb_warns = check_smart_brevity(raw, text)
    warns.extend(sb_warns)

    # Sentence rhythm (advisory): the direction Flesch alone never measures.
    mean_len, short_pct = rhythm(text)
    if mean_len is not None and mean_len < RHYTHM_MEAN_MIN:
        warns.append(f"rhythm: sentences average {mean_len} words (floor {RHYTHM_MEAN_MIN}) — "
                     f"join adjacent short sentences")
    if short_pct is not None and short_pct > RHYTHM_SHORT_MAX:
        warns.append(f"rhythm: {short_pct}% of sentences are {RHYTHM_SHORT_WORDS} words or fewer "
                     f"(cap {RHYTHM_SHORT_MAX}%) — the body reads as a run of one-liners")

    # Figure load (advisory): the same failure in the other direction. Flesch rewards digits, so a
    # derivation chain scores well while reading like a worksheet — the arithmetic is right and the
    # reader stops following. The remedy is a sentence without a number, not a smaller figure.
    fig_pct, fig_n = figure_load(text)
    if fig_pct is not None and fig_pct > FIGURE_DENSITY_MAX:
        warns.append(f"figure load: {fig_pct}% of prose sentences carry a figure "
                     f"(cap {FIGURE_DENSITY_MAX}%) — give the meaning its own sentence without a number")

    # Keyword-stuffing guard (topic-agnostic: reads the article's own primary_keyword).
    kw, kw_count = _keyword_density(path, text)
    if kw:
        if kw_count >= 4:
            fails.append(f"keyword stuffing: '{kw}' appears {kw_count}x in body (max 3)")
        elif kw_count >= 2:
            warns.append(f"keyword density high: '{kw}' appears {kw_count}x in body")

    # Title contains primary_keyword check (SEO mandatory requirement)
    title_ok, kw_val, title_val = check_title_keyword(raw)
    if not title_ok:
        fails.append(f"title missing SEO keyword: title '{title_val}' must contain primary_keyword '{kw_val}'")

    return {
        "file": pathlib.Path(path).name,
        "flesch": score, "target": target, "floor": floor,
        "words": w, "sents": s, "long_word": long_rate,
        "sentence_mean": mean_len, "short_sent_pct": short_pct,
        "figure_pct": fig_pct, "figure_sents": fig_n,
        "undefined_acronyms": undef, "unglossed_terms": unglossed, "jargon": jarg,
        "primary_keyword": kw, "keyword_count": kw_count,
        "warnings": warns, "fails": fails,
        "verdict": "PASS" if not fails else "FAIL",
    }


def _keyword_density(path, body_text):
    """Return (primary_keyword, occurrences_in_body) from the article's own frontmatter, so the
    gate can flag keyword stuffing on ANY topic without a hardcoded keyword list."""
    raw = pathlib.Path(path).read_text()
    m = re.search(r"primary_keyword:\s*[\"']?([^\"'\n]+)", raw)
    if not m:
        return None, 0
    kw = m.group(1).strip()
    low = body_text.lower()
    # normalize: count phrase occurrences ignoring case
    count = len(re.findall(re.escape(kw.lower()), low))
    return kw, count


def check_title_keyword(raw_text):
    """Verify that when primary_keyword is declared in frontmatter, title contains the keyword."""
    m_kw = re.search(r"primary_keyword:\s*[\"']?([^\"'\n]+)", raw_text)
    if not m_kw:
        return True, None, None
    kw = m_kw.group(1).strip()
    if not kw:
        return True, None, None
    m_title = re.search(r"title:\s*[\"']?([^\"'\n]+)", raw_text)
    if not m_title:
        return False, kw, ""
    title = m_title.group(1).strip()

    def norm(s):
        s = s.lower().replace("-", " ")
        s = re.sub(r"[^a-z0-9\s]", "", s)
        return " ".join(s.split())

    n_kw = norm(kw)
    n_title = norm(title)
    if not n_kw:
        return True, kw, title

    # Exact normalized substring match
    if n_kw in n_title:
        return True, kw, title

    # All words in order with flexible spacing / prepositions
    kw_words = n_kw.split()
    if kw_words:
        pattern = r"\b" + r"\b.*\b".join(re.escape(w) for w in kw_words) + r"\b"
        if re.search(pattern, n_title):
            return True, kw, title

        # Stem simple trailing 's' if not matched
        stem = lambda w: w[:-1] if w.endswith("s") and len(w) > 3 else w
        kw_stems = [stem(w) for w in kw_words]
        stem_pattern = r"\b" + r"[a-z]*\b.*\b".join(re.escape(w) for w in kw_stems) + r"[a-z]*\b"
        if re.search(stem_pattern, n_title):
            return True, kw, title

    return False, kw, title


def check(path, target=TARGET, floor=FLOOR):
    m = measure(path, target, floor)
    print(f"== {m['file']}")
    print(f"   Flesch={m['flesch']} (target {m['target']}, floor {m['floor']})  words={m['words']}  sents={m['sents']}  long-word={m['long_word']}%")
    if m["undefined_acronyms"]:
        print(f"   undefined acronyms: {', '.join(m['undefined_acronyms'])}")
    if m["unglossed_terms"]:
        print(f"   unglossed terms: {', '.join(m['unglossed_terms'])}")
    if m["jargon"]:
        print(f"   jargon (advisory): {', '.join(m['jargon'])}")
    for wmsg in m["warnings"]:
        print(f"   WARNING: {wmsg}")
    for f in m["fails"]:
        print(f"   FAIL: {f}")
    print(f"   VERDICT: {m['verdict']}")
    return m["verdict"] == "PASS"


def main(argv):
    target, floor, paths, want_json = TARGET, FLOOR, [], False
    it = iter(argv)
    for tok in it:
        if tok == "--target":
            target = float(next(it))
        elif tok == "--floor":
            floor = float(next(it))
        elif tok == "--json":
            want_json = True
        else:
            paths.append(tok)
    if not paths:
        print("usage: check_accessibility.py [--target N] [--floor N] [--json] <draft.md ...>")
        return 2
    ok = True
    for p in paths:
        m = measure(p, target, floor)
        if want_json:
            print(json.dumps(m))
        else:
            print("\n".join(_render(m)))
        ok = ok and m["verdict"] == "PASS"
    return 0 if ok else 1


def _render(m):
    lines = [f"== {m['file']}",
             f"   Flesch={m['flesch']} (target {m['target']}, floor {m['floor']})  words={m['words']}  sents={m['sents']}  long-word={m['long_word']}%"]
    if m["undefined_acronyms"]:
        lines.append(f"   undefined acronyms: {', '.join(m['undefined_acronyms'])}")
    if m["unglossed_terms"]:
        lines.append(f"   unglossed terms: {', '.join(m['unglossed_terms'])}")
    if m["jargon"]:
        lines.append(f"   jargon (advisory): {', '.join(m['jargon'])}")
    for wmsg in m["warnings"]:
        lines.append(f"   WARNING: {wmsg}")
    for f in m["fails"]:
        lines.append(f"   FAIL: {f}")
    lines.append(f"   VERDICT: {m['verdict']}")
    return lines


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
