#!/usr/bin/env python3
"""One-off Loop 3 humanizer for a single draft (Gemini frontier), per skills/claude_humanizer.md."""
import re, sys, pathlib
import humanizer_tools as ht  # retry loop + accessibility feedback + frontier call

ROOT = pathlib.Path("/root/editorial-factory")
draft_rel = sys.argv[1] if len(sys.argv) > 1 else "context/drafts/2026-09-07_anthropic-multiagent-turf-war_draft.md"

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
- PRESERVE the section markers exactly: <!-- lead -->, <!-- tension -->, <!-- tactical-insight -->, <!-- nuanced-takeaway -->, <!-- tldr -->, <!-- linkedin -->.
- PRESERVE the `<!-- schema -->` JSON-LD and `<!-- internal-links -->` blocks verbatim at the document end (do not remove or rewrite them).
- Keep the TL;DR as the structured <!-- tldr --> field, exactly 3 scannable bullet items starting with "-". Never write a prose "in conclusion / key takeaways" paragraph. Do NOT compose a TOC.

SECTION GATES (each section must pass its own gate):
- <!-- lead -->: delivers the core news/stat immediately in sentence 1; no throat-clearing or preamble. HIGHEST PRIORITY.
- <!-- tension -->: frames the shift with a context signpost (**The big picture:** or **Why it matters:**); names who it hurts/helps.
- <!-- tactical-insight -->: practitioner moves structured with clean bullets and bold lead-ins for 3+ items; doable for the persona.
- <!-- nuanced-takeaway -->: honest limitation / counter-argument with a signpost (**The catch:** or **Between the lines:**).
- <!-- tldr -->: exactly 3 scannable bullets; does not read like a summary paragraph.

ACCESSIBILITY RULES (topic-agnostic — apply to EVERY topic; rewrite vocabulary, never facts):
- Every acronym is expanded at its FIRST use in the body (either "Full Name (ACR)" or "ACR (...plain meaning)"). Zero undefined acronyms at the end. Never reuse an acronym bare after introducing it.
- Translate every specialist term for a general reader: use the source's plain phrase or add a short gloss.
- If the story hinges on a process a general reader may not know, add ONE half-sentence explaining what it is before relying on it.
- Target Flesch Reading Ease >= 60 on the body (hard floor >= 50). READABILITY comes from plain WORDS, not short sentences: replace long/technical words with everyday ones. Write connected, natural sentences of ~14-20 words with variation — do NOT fragment into choppy one-liners.
- Write FLUENTLY — no keyword stuffing. A target search phrase (if any) appears AT MOST 2-3 times in the whole body.
- Do not change or drop any fact, figure, [n] citation, or source line.

OUTPUT FORMAT (strict):
1) The full rewritten article, beginning with the frontmatter, then each section in order with its marker, then "## Sources" (the original source list VERBATIM), then the <!-- linkedin --> variant.
2) Then a section starting exactly "## Gate report" listing, one per line, each section's gate verdict: lead / tension / tactical-insight / nuanced-takeaway / tldr as "PASS — <short reason>" or "FAIL — <reason>".

Now rewrite the following draft:"""

draft_path = ROOT / draft_rel
out_path = draft_path.with_name(draft_path.name.replace("_draft.md", "_final.md"))
draft = draft_path.read_text()

def extract_sources(d):
    m = re.search(r"## Sources\s*\n(.*?)(?=\n<!-- linkedin -->|\Z)", d, re.S)
    return m.group(1).strip() if m else ""

def clean(raw):
    return re.sub(r"\s*```$", "", re.sub(r"^```[a-zA-Z]*\s*", "", raw.strip())).strip()

src_lines = [l.strip() for l in extract_sources(draft).splitlines() if l.strip()]
base_prompt = RULES + "\n\n" + draft
MARKERS = ["<!-- lead -->", "<!-- tension -->", "<!-- tactical-insight -->",
           "<!-- nuanced-takeaway -->", "<!-- tldr -->", "<!-- linkedin -->"]
result, diag, srcs_ok, markers_ok = None, None, False, False
attempts = 0
for attempt in range(1, ht.MAX_ATTEMPTS + 1):
    attempts = attempt
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
        raw = ht.call_gemini(prompt)
    except Exception as e:
        print(f"ERROR attempt {attempt}: {e}")
        break
    result = clean(raw)
    out_path.write_text(result + "\n")
    srcs_ok = all(s in result for s in src_lines)
    markers_ok = all(m in result for m in MARKERS)
    diag = ht.measure(out_path)
    print(f"attempt {attempt}: VERDICT {diag['verdict']}  flesch={diag['flesch']}  words={diag['words']}  "
          f"sources={'ok' if srcs_ok else 'MISSING'}  markers={'ok' if markers_ok else 'FAIL'}")
    if diag["verdict"] == "PASS" and srcs_ok and markers_ok:
        break

note = diag["verdict"] if diag else "UNKNOWN"
print(f"WROTE {out_path.name}  final_verdict={note}  attempts={attempts}  "
      f"sources={'ok' if srcs_ok else 'MISSING'}")
if diag and diag["verdict"] != "PASS":
    sys.exit(1)  # held at Loop 3 (per claude_humanizer.md §7) — never ship a dense/partial piece
