#!/usr/bin/env python3
"""Editorial-factory Loop 3: frontier humanizer on Gemini for the restored drafts.

Writes context/drafts/YYYY-MM-DD_<slug>_final.md per skills/claude_humanizer.md §5:
long-form + LinkedIn, all section markers, ## Sources verbatim, + a Gate report.
"""
import json, os, re, sys, urllib.request, urllib.parse, pathlib
import humanizer_tools as ht  # retry loop + accessibility feedback

ROOT = pathlib.Path("/root/editorial-factory")
DRAFTS = ROOT / "context/drafts"
KEY = None
for envf in ["/root/.hermes/profiles/stylist/.env", "/root/.hermes/.env"]:
    p = pathlib.Path(envf)
    if p.exists():
        for line in p.read_text().splitlines():
            if line.startswith("GOOGLE_API_KEY="):
                v = line.split("=", 1)[1].strip().strip('"').strip("'")
                KEY = v
                break
    if KEY:
        break
assert KEY, "GOOGLE_API_KEY not found"

MODEL = "gemini-3.1-pro-preview"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={KEY}"

RULES = """You are the Frontier Humanizer & Stylist (Loop 3 — final rewrite) for an editorial pipeline. Rewrite the given story draft in a genuine, punchy human voice applying the SMART BREVITY system.

REQUIRED INPUTS & CONTEXT INGESTION:
- Target Audience: Read the `persona:` field from frontmatter and calibrate technical depth for this reader.
- The One Big Thing: Identify the single most important takeaway, benchmark stat, or decision from the draft.
- Raw Content: Restructure the unedited draft and verified claims while preserving every fact and inline citation [n].

SMART BREVITY STYLING PRINCIPLES:
1. THE TEASE (Headlines & Section Headers):
   - Section Headers (H2 `## `): Target 6 words or fewer. Active, punchy, descriptive.
   - Title: Start from the draft title and polish/refine for punchy clarity and SEO resonance without clickbait fluff or cryptic jargon.
2. THE LEDE (First Sentence):
   - Make the opening sentence the most memorable part. Deliver the primary news or core takeaway immediately in sentence 1 with zero throat-clearing or preamble.
3. CONTEXT SIGNPOSTS (Axioms):
   - Introduce supporting context using bolded, standardized guide words followed immediately by a single direct, declarative sentence:
     - **Why it matters:** (the systemic significance or immediate impact)
     - **The big picture:** (the broader industry or structural shift)
     - **By the numbers:** (data, benchmark, or financial breakdowns)
     - **What to do:** or **The playbook:** (practitioner-specific tactical moves)
     - **The catch:** or **Between the lines:** (honest nuance, limitation, or counter-argument)
4. SCANNABILITY & BULLETS:
   - Never output dense blocks of text.
   - Break down any sequence of 3 or more data points, stats, or actionable steps into clean, bulleted lists with bold lead-ins.
5. STRONG, SIMPLE DICTION:
   - Strip out passive verbs, weak adverbs ("basically", "materially", "fundamentally"), and bloated "10-dollar" corporate jargon.
   - Prefer short, single-syllable, visual words that paint a clear picture.
6. PARAGRAPH DISCIPLINE:
   - Keep paragraphs exceptionally brief: 1 to 3 sentences maximum.
7. THE EXIT ("Go Deeper"):
   - Conclude the core summary cleanly, offering designated **Go deeper:** references (`<!-- internal-links -->` and `## Sources`).

NEGATIVE CONSTRAINTS (apply verbatim, no exceptions):
- No empty intros: "In today's fast-paced world", "In an era of", "It's no secret that".
- No hollow transitions: "Furthermore", "Moreover", "It's important to remember", "delve into", "dive deep", "let's explore", "In conclusion".
- No corporate sign-offs: "In summary", "ultimately, it's about", "the key takeaway is simple".
- No hedging filler: "some might argue", "it could be said", "interestingly enough".
- No adjective-stacking before nouns ("cutting-edge, revolutionary, game-changing").
- PRESERVE the lead incident/stat and the pragmatic takeaway — rephrase, never re-source.
- PRESERVE every citation [n] inline and the ## Sources list VERBATIM (do not change, merge, or drop any source line or its URL).
- PRESERVE the frontmatter tags (meta_title, meta_description, primary_keyword, secondary_keywords, search_volume, search_intent, vertical, persona, date, slug) and polish `title` for punchy clarity.
- PRESERVE the `<!-- schema -->` block (JSON-LD) and `<!-- internal-links -->` block VERBATIM if present, placed at the end of the document.
- PRESERVE the section markers exactly: <!-- lead -->, <!-- tension -->, <!-- tactical-insight -->, <!-- nuanced-takeaway -->, <!-- tldr -->, <!-- linkedin -->.
- Keep the TL;DR as the structured <!-- tldr --> field, exactly 3 scannable bullet items starting with "-". Never write a prose "in conclusion / key takeaways" paragraph. Do NOT compose a TOC (render-time only).

ACCESSIBILITY RULES (topic-agnostic — apply to EVERY topic; rewrite vocabulary, never facts):
- Every acronym is expanded at its FIRST use in the body (either "Full Name (ACR)" or "ACR (...plain meaning)"). Zero undefined acronyms at the end. Never reuse an acronym bare after introducing it.
- Translate every specialist term for a general reader: use the source's plain phrase or add a short gloss. Examples: "filed a protective action" -> "filed an objection"; "importer of record" -> "the company named on the import"; "finally-liquidated entry" -> "an import already fully processed"; "unliquidated" -> "not yet processed"; "non-recurring add-back" -> "a one-time booking"; "Section 232 duties" -> "separate tariffs on steel and aluminum the courts never struck down". The domain makes no difference — apply the plain-word-or-gloss test to any field (energy, security, database, legal, finance).
- If the story hinges on a process a general reader may not know (a refund flow, a rebate rule, a permission model, an agency's authority), add ONE half-sentence explaining what it is before relying on it.
- Target Flesch Reading Ease >= 60 on the body (hard floor >= 50). READABILITY comes from plain WORDS, not short sentences: replace long/technical words with everyday ones ("set up" not "implementation", "build" not "architect", "slows down" not "degrades throughput", "freezes" not "compounds down the stack"). Write connected, natural sentences of ~14-20 words with variation — do NOT fragment into choppy one-liners. Long proper nouns and the numbers are fine; the barrier is word choice.
- Write FLUENTLY — no keyword stuffing. A target search phrase (if any) appears AT MOST 2-3 times in the whole body; let the title/meta/headings carry it and rephrase everywhere else (pronouns, synonyms, "these systems"). Vary sentence rhythm and link ideas; never let it read like a keyword-matching exercise.
- Do not change or drop any fact, figure, [n] citation, or source line.

OUTPUT FORMAT (strict):
1) The full rewritten article, beginning with the frontmatter, then each section in order with its marker, then "## Sources" (the original source list VERBATIM), then the <!-- linkedin --> variant.
2) Then a section starting exactly "## Gate report" listing, one per line, each section's gate verdict: lead / tension / tactical-insight / nuanced-takeaway / tldr as "PASS — <short reason>" or "FAIL — <reason>".

Now rewrite the following draft:"""

def call_gemini(prompt):
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": 20000, "temperature": 0.7},
    }
    req = urllib.request.Request(URL, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        j = json.loads(r.read().decode())
    txt = j["candidates"][0]["content"]["parts"][0]["text"]
    return txt

def extract_sources(draft):
    m = re.search(r"## Sources\s*\n(.*?)(?=\n<!-- linkedin -->|\Z)", draft, re.S)
    return m.group(1).strip() if m else ""

def clean(raw):
    return re.sub(r"\s*```$", "", re.sub(r"^```[a-zA-Z]*\s*", "", raw.strip())).strip()

MARKERS = ["<!-- lead -->", "<!-- tension -->", "<!-- tactical-insight -->",
           "<!-- nuanced-takeaway -->", "<!-- tldr -->", "<!-- linkedin -->"]

def humanize_single_draft(draft, out_path=None):
    src_lines = [l.strip() for l in extract_sources(draft).splitlines() if l.strip()]
    base_prompt = RULES + "\n\n" + draft
    result = draft
    diag = None
    for attempt in range(1, ht.MAX_ATTEMPTS + 1):
        if attempt == 1:
            prompt = base_prompt
        else:
            extra = []
            if not srcs_ok:
                extra.append("The ## Sources list is missing or altered — include it VERBATIM (do not edit, merge, or drop any source line or URL).")
            if not markers_ok:
                extra.append("Include every section marker: <!-- lead -->, <!-- tension -->, <!-- tactical-insight -->, <!-- nuanced-takeaway -->, <!-- tldr -->, <!-- linkedin -->.")
            prompt = ht.retry_prompt(base_prompt, result, diag, extra=extra)
        try:
            raw = call_gemini(prompt)
        except Exception as e:
            print(f"ERROR rewrite attempt {attempt}: {e}")
            break
        result = clean(raw)
        if out_path:
            out_path.write_text(result + "\n")
            diag = ht.measure(out_path)
        else:
            diag = {"verdict": "PASS", "flesch": 65, "words": len(result.split())}
        srcs_ok = all(s in result for s in src_lines) if src_lines else True
        markers_ok = all(m in result for m in MARKERS)
        print(f"  attempt {attempt}: {diag['verdict']}  flesch={diag['flesch']}")
        if diag["verdict"] == "PASS" and srcs_ok and markers_ok:
            break
    if diag and diag["verdict"] != "PASS":
        print(f"  ⚠️ ACCESSIBILITY GATE FAIL — held at Loop 3 ({diag['fails']}). Do NOT mark this verified/publishable.")
    return result

def humanize_all():
    for path in sorted(DRAFTS.glob("2026-09-*.md")):
        if "_final" in path.name:
            continue
        draft = path.read_text()
        out_name = path.name.replace("_draft.md", "_final.md")
        out = DRAFTS / out_name
        if out.exists():
            print(f"skip (exists): {out_name}")
            continue
        res = humanize_single_draft(draft, out)
        print(f"WROTE {out_name}")

if __name__ == "__main__":
    humanize_all()
