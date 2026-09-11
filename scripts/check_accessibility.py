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


def body_of(path):
    t = pathlib.Path(path).read_text()
    t = re.sub(r"^---\n.*?\n---\n", "", t, flags=re.S)          # frontmatter
    t = re.sub(r"#{1,3}\s*Sources.*", "", t, flags=re.S)        # sources -> end
    t = re.sub(r"<!--\s*linkedin\s*-->.*", "", t, flags=re.S)   # linkedin variant
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)               # HTML section markers
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
    cands = re.findall(r"\b([A-Z][A-Z&]{1,7})\b", text)
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
    2. Paragraph sentence count: max 3 sentences per paragraph.
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
        if len(sents) > 3:
            long_paras += 1
    if long_paras > 0:
        warns.append(f"Smart Brevity: {long_paras} paragraph(s) > 3 sentences (aim for 1-3 max)")

    # 3. Context signposts
    signpost_patterns = [
        r"\*\*Why it matters:\*\*", r"\*\*The big picture:\*\*", r"\*\*By the numbers:\*\*",
        r"\*\*What to do:\*\*", r"\*\*The playbook:\*\*", r"\*\*The catch:\*\*",
        r"\*\*Between the lines:\*\*", r"\*\*Yes, but:\*\*", r"\*\*Go deeper:\*\*", r"\*\*What's next:\*\*"
    ]
    has_signposts = any(re.search(pat, raw_text, re.I) for pat in signpost_patterns)
    if not has_signposts:
        warns.append("Smart Brevity: no bold context signposts found (**Why it matters:**, **The big picture:**, etc.)")

    return warns


def measure(path, target=TARGET, floor=FLOOR):
    """Return a structured diagnosis of the article's accessibility. Safe to call from other
    scripts (the Loop 3 humanizers) so they can read the exact FAIL reasons and retry."""
    raw = pathlib.Path(path).read_text()
    text = body_of(path)
    score, w, s, long_rate = flesch(text)
    undef = undefined_acronyms(text)
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
    if jarg:
        warns.append("jargon to gloss/replace: " + ", ".join(jarg))

    # Smart Brevity structural check
    sb_warns = check_smart_brevity(raw, text)
    warns.extend(sb_warns)

    # Keyword-stuffing guard (topic-agnostic: reads the article's own primary_keyword).
    kw, kw_count = _keyword_density(path, text)
    if kw:
        if kw_count >= 4:
            fails.append(f"keyword stuffing: '{kw}' appears {kw_count}x in body (max 3)")
        elif kw_count >= 2:
            warns.append(f"keyword density high: '{kw}' appears {kw_count}x in body")

    return {
        "file": pathlib.Path(path).name,
        "flesch": score, "target": target, "floor": floor,
        "words": w, "sents": s, "long_word": long_rate,
        "undefined_acronyms": undef, "jargon": jarg,
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


def check(path, target=TARGET, floor=FLOOR):
    m = measure(path, target, floor)
    print(f"== {m['file']}")
    print(f"   Flesch={m['flesch']} (target {m['target']}, floor {m['floor']})  words={m['words']}  sents={m['sents']}  long-word={m['long_word']}%")
    if m["undefined_acronyms"]:
        print(f"   undefined acronyms: {', '.join(m['undefined_acronyms'])}")
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
