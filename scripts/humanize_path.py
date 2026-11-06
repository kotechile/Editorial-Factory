#!/usr/bin/env python3
"""Loop 3 frontier humanizer for an arbitrary draft (Gemini frontier), per skills/claude_humanizer.md."""
import re, sys, pathlib
import humanizer_tools as ht  # retry loop + accessibility feedback + frontier call

ROOT = pathlib.Path("/root/editorial-factory")
draft_rel = sys.argv[1] if len(sys.argv) > 1 else "context/drafts/2026-09-07_ieepa-refund-wave-hits-earnings_draft.md"

RULES = """You are the Frontier Humanizer & Stylist (Loop 3 — final rewrite) for an editorial pipeline. Rewrite the given story draft in a genuine, punchy human voice applying the SMART BREVITY system.

REQUIRED INPUTS & CONTEXT INGESTION:
- Target Audience: Read the `persona:` field from frontmatter and calibrate technical depth for this reader.
- The One Big Thing: Identify the single most important takeaway, benchmark stat, or decision from the draft.
- Raw Content: Restructure the unedited draft and verified claims while preserving every fact and inline citation [n].

SMART BREVITY STYLING PRINCIPLES:
1. THE TEASE (Headlines & Section Headers):
   - Section Headers (H2 `## `): Target 6 words or fewer. Active, punchy, descriptive.
   - Title: Start from the draft title and re-cut it to the house headline standard (see
     `skills/story_draft.md`): core headline <= 6 words, whole title <= 10 words and <= 60 chars,
     never open on 'The/A/An', keep a curiosity-gap or loss-aversion hook, anchor on a figure the
     article states, and name the reader. It must promise nothing the article does not deliver in its
     first paragraph. Anything over 10 words is not a headline — cut it, do not soften it. When frontmatter defines `primary_keyword:`, the `title:` and `meta_title:` MUST explicitly contain the primary keyword (preserving proper/canonical casing, e.g. "<Keyword>: <Subtitle>"). Never drop or replace the keyword in the headline.
2. THE LEDE (First Sentence):
   - Make the opening sentence the most memorable part. Deliver the primary news or core takeaway immediately in sentence 1 with zero throat-clearing or preamble.
3. SECTION HEADERS — A STORY, NOT A DECK:
   - Use standardized H2 headers (`## `) to structure the core sections cleanly for readers and Table of Contents generators.
   - FORMATTING REQUIREMENT: Every H2 header MUST stand on its own separate line, preceded by an empty blank line and followed by an empty blank line. NEVER place body prose or bullets on the same line as the H2 header, and never attach text directly on the line below without an intervening blank line:
   - THE ORDER IS PART OF THE CONTRACT (owner, 2026-11-06): `<!-- lead -->` → `<!-- tldr -->` → `<!-- tension -->` → `<!-- tactical-insight -->` → `<!-- nuanced-takeaway -->`. If the draft you were handed carries the summary at the foot of the piece, MOVE IT — the executive summary is the second thing the reader sees.
     - `## At a glance` (in <!-- tldr -->, DIRECTLY under the lede: a three-line shift / number / risk box under 50 words, under its own distinct H2 header so it is NEVER embedded under "The catch")
     - `## The big picture:` (in <!-- tension -->, the timeline stated ONCE in strict order — initial event → initial deadline → current extension — then the broader structural shift; followed on a new paragraph by a single direct sentence)
     - `## By the numbers` (REQUIRED section, but small, and placed AFTER the mechanism is explained: 2–3 bold bullets, ONE metric per bullet, one sentence, 25 words or fewer — `- **85% of Long Beach cargo:** one clause saying what it counts [3]`. Never a four-bullet recap, never two statistics in one lead-in.)
     - `## What I'd watch:` or `## Where the money flows` (in <!-- tactical-insight -->, reporting what operators closest to the story are doing)
     - `## The catch` (in <!-- nuanced-takeaway -->, presenting the honest limitation, tradeoff, or counter-argument; self-contained — no rule or concept that appears for the first time in the closing paragraph; followed on a new paragraph)
4. SCANNABILITY & BULLETS:
   - Never output dense blocks of text.
   - STORY FIRST. The reader is following an argument, not scanning a deck: a section of three bullets usually wants to be three sentences. Bullets are for a real list (3+ comparable items), and a bold figure lead-in (`- **88% — Diesel price jump:** ...`) belongs only where the figure is the point of the line.
   - The fixed house labels are a fallback, not a requirement: write each section header in this article's own words — what the section actually argues. An article that opens on "The big picture:", lists "What I'd watch:" and closes on "The catch" reads like the template it is.
   - Break down any sequence of 3 or more data points, stats, or actionable steps into clean, bulleted lists with bold lead-ins.
4a. READABILITY LAW (owner, 2026-11-06 — the desk's critic checks these, and three of them hold the push):
   - NO RIDDLE SYNTAX. Never trade clarity for a clever parallel or an abstract noun chain: "a gate is one shared function rather than a share of one" and "deeper into its stay than the window is long" are banned. Write subject -> active verb -> concrete object, with the consequence in the same sentence: "A walkout by 2% of the workforce still freezes 100% of the cargo at those eight terminals, because you cannot run a terminal with a closed gate." Three prepositional phrases in a row ("the fee on the rate for the box in the yard at the gate") is the signature of the defect.
   - STATE THE TIMELINE ONCE, in paragraph 2: initial event -> initial deadline -> current extension. After that refer to the operational window ("the 12-day window"), never re-explain the calendar, and never open a paragraph on a relative day ("At 5 p.m. on Wednesday") before the calendar date is established.
   - KEEP DOMAIN TERMS EXACT and gloss them in place: terminal dwell time is how long an import box sits on the dock, never "a round-trip retrieval cycle". Use the source's own method name, not a picture of it.
   - NO COLD CONCEPT IN THE CLOSING: the last paragraph may not introduce a rule, a billing mechanism or a technical concept the body never explained; if it must, carry a 5-10 word inline bridge ("under federal demurrage billing rules, the two 30-day dispute clocks...").
   - ONE CITATION TAG PER SENTENCE (consolidate to the most primary source) and `## Sources` as a vertical list ("1. <publisher> - <url>"), never a run-on paragraph.
5. STRONG, SIMPLE DICTION:
   - Strip out passive verbs, weak adverbs ("basically", "materially", "fundamentally"), and bloated "10-dollar" corporate jargon.
   - Prefer short, single-syllable, visual words that paint a clear picture.
6. PARAGRAPH DISCIPLINE & SENTENCE RHYTHM:
   - Keep paragraphs to 3-5 sentences, never more than 6. Depth comes from sentences per paragraph, not from longer sentences: one idea may run to five sentences, but never split a single thought across two paragraphs.
   - Write CONNECTED sentences, roughly 14-22 words with real variation. One sentence may carry a cause and its consequence ("X, so Y" / "X: Y"), which is what keeps the prose from reading like a list.
   - At most ONE sentence of 8 words or fewer per paragraph, and never a run of short declaratives. A claim and the consequence that follows it belong in the same sentence unless each needs its own emphasis.
   - Never shorten a sentence to raise the Flesch score: the lever is plain WORDS. Shortening scores the same and reads worse.
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
- PRESERVE the frontmatter tags (meta_title, meta_description, primary_keyword, secondary_keywords, search_volume, search_intent, keyword_data_source, secondary_keywords_source, vertical, persona, date, slug) and polish `title` for punchy clarity. When `primary_keyword` is defined in frontmatter, `title` and `meta_title` MUST explicitly contain the primary keyword. Never omit the target keyword from the title.
- PRESERVE the `<!-- schema -->` JSON-LD and `<!-- internal-links -->` blocks verbatim at the document end (do not remove or rewrite them).
- PRESERVE the `## Related reading` section exactly as written — its anchor texts and URLs are verified internal links to live pages on the same site. Never rewrite, drop, merge, or invent one, and never add a link that is not already there.
- PRESERVE the section markers exactly: <!-- lead -->, <!-- tension -->, <!-- tactical-insight -->, <!-- nuanced-takeaway -->, <!-- tldr -->.
- PRESERVE the opening and closing `---` YAML delimiters around the frontmatter exactly — do NOT wrap the frontmatter in triple-backtick code fences.
- Format the TL;DR as the structured <!-- tldr --> field opening with an H2 header '## At a glance', strictly following this 3-LINE schema (owner standard 2026-10-29; the four-part Big Shift / Why It Matters / What I'd Watch / Catch recap is RETIRED — rebuilding it is a rewrite defect):
  ## At a glance
  - "**The shift:** <one sentence: what changed>"
  - "**The number:** <the one figure that proves it and that the body already states>"
  - "**The risk:** <the single caveat a reader must carry away>"
  Under 50 words total, no sub-bullets, no list mirroring "What I'd watch".
  Never write a prose "in conclusion / key takeaways" paragraph. Do NOT compose a TOC.

SECTION GATES (each section must pass its own gate):
- <!-- lead -->: delivers the core news/stat immediately in sentence 1; no throat-clearing or preamble. HIGHEST PRIORITY.
- <!-- tension -->: the section that says what changed and who it lands on. Give it an H2 in this article's own words (the house label '## The big picture:' is a fallback). A '## By the numbers' block is optional — carry the figures in the sentences that use them unless the piece is genuinely a table of numbers.
- <!-- tactical-insight -->: what the people closest to the story are doing and what the writer expects next, structured with clean bullets and bold lead-ins for 3+ items; observations, never instructions to the reader.
- <!-- nuanced-takeaway -->: honest limitation / counter-argument with '## The catch' H2 header.
- <!-- tldr -->: opens with '## At a glance' H2 header; follows the three-line schema (**The shift**, **The number**, **The risk**) under 50 words with no sub-bullets and no recap of the tactical section; plain, accessible English without unexplained buzzwords.

ACCESSIBILITY RULES (topic-agnostic — apply to EVERY topic; rewrite vocabulary, never facts):
- Every acronym is expanded at its FIRST use in the body (either "Full Name (ACR)" or "ACR (...plain meaning)"). Zero undefined acronyms at the end. Never reuse an acronym bare after introducing it.
- Translate every specialist term for a general reader: use the source's plain phrase or add a short gloss.
- If the story hinges on a process a general reader may not know, add ONE half-sentence explaining what it is before relying on it.
- Target Flesch Reading Ease >= 60 on the body (hard floor >= 50). READABILITY comes from plain WORDS, not short sentences: replace long/technical words with everyday ones. Write connected, natural sentences of ~14-20 words with variation — do NOT fragment into choppy one-liners.
- Write FLUENTLY — no keyword stuffing. A target search phrase (if any) appears AT MOST 2-3 times in the whole body.
- Do not change or drop any fact, figure, [n] citation, or source line.
- NEVER invent an expansion for a proper noun or system name (e.g. CRAB, DeltaBox). If a name has no known full form, do not fabricate one to satisfy the acronym rule — rephrase to drop the all-caps token instead (e.g. "specialized checkpoint systems" rather than "CRAB"). A fabricated acronym expansion is a hallucination and a hard failure.

OUTPUT FORMAT (strict):
1) The full rewritten article, beginning with the frontmatter, then the sections IN THIS ORDER with their markers — <!-- lead -->, <!-- tldr --> (## At a glance, directly under the lede), <!-- tension -->, <!-- tactical-insight -->, <!-- nuanced-takeaway --> — then "## Sources" (the original source list VERBATIM, as a vertical list, one entry per line). Write nothing after that but the `## Gate report` — the social variant was removed with the LinkedIn/Reddit channel (2026-10-06).
2) Then a section starting exactly "## Gate report" listing, one per line, each section's gate verdict: lead / tension / tactical-insight / nuanced-takeaway / tldr as "PASS — <short reason verifying plain-English clarity and scannability>" or "FAIL — <reason>".

Now rewrite the following draft:"""

# The voice contract (skills/claude_humanizer.md §3.9) is part of the job instruction, not a
# suggestion: verify.sh §9 fails the build on the article body. (No social variant — the LinkedIn/
# Reddit channel was removed 2026-10-06.)
RULES += "\n" + ht.LONGFORM_VOICE_RULES
RULES += ht.VIBE_COPY_RULES  # the copy contract, read from context/vibe/lexicon.json

draft_path = ROOT / draft_rel
out_path = draft_path.with_name(draft_path.name.replace("_draft.md", "_final.md"))
draft = draft_path.read_text()

def extract_sources(d):
    m = re.search(r"## Sources\s*\n(.*?)(?=\n<!-- linkedin -->|\n## Gate report|\Z)", d, re.S)
    return m.group(1).strip() if m else ""

def clean(raw):
    return re.sub(r"\s*```$", "", re.sub(r"^```[a-zA-Z]*\s*", "", raw.strip())).strip()

srcs_draft = extract_sources(draft)
src_lines = [l.strip() for l in srcs_draft.splitlines() if l.strip()]
base_prompt = RULES + "\n\n" + draft
MARKERS = ["<!-- lead -->", "<!-- tension -->", "<!-- tactical-insight -->",
           "<!-- nuanced-takeaway -->", "<!-- tldr -->"]

result, diag, srcs_ok, markers_ok, len_ok = None, None, False, False, False
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
            extra.append("Include every section marker: <!-- lead -->, <!-- tension -->, <!-- tactical-insight -->, <!-- nuanced-takeaway -->, <!-- tldr -->.")
        if not len_ok:
            extra.append("The article body is too short (under %d words). Restore depth from the verified brief — restate the tactical moves and the tension in full, using only already-verified figures. Never invent new claims or numbers." % ht.MIN_BODY_WORDS)
        prompt = ht.retry_prompt(base_prompt, result, diag, extra=extra)
    try:
        raw = ht.call_gemini(prompt)
    except Exception as e:
        print(f"ERROR attempt {attempt}: {e}")
        break
    result = ht.ensure_title_contains_keyword(ht.normalize_frontmatter(clean(raw)))
    out_path.write_text(result + "\n")
    srcs_ok = all(s in result for s in src_lines)
    markers_ok = all(m in result for m in MARKERS)
    diag = ht.measure(out_path)
    len_ok = diag.get("words", 0) >= ht.MIN_BODY_WORDS
    print(f"attempt {attempt}: VERDICT {diag['verdict']}  flesch={diag['flesch']}  words={diag['words']}  "
          f"sources={'ok' if srcs_ok else 'MISSING'}  markers={'ok' if markers_ok else 'FAIL'}  length={'ok' if len_ok else 'SHORT'}")
    if diag["verdict"] == "PASS" and srcs_ok and markers_ok and len_ok:
        break

note = diag["verdict"] if diag else "UNKNOWN"
print(f"WROTE {out_path.name}  final_verdict={note}  attempts={attempts}  "
      f"sources={'ok' if srcs_ok else 'MISSING'}  length={'ok' if len_ok else 'SHORT'}")
if diag and diag["verdict"] != "PASS":
    sys.exit(1)  # held at Loop 3 (per claude_humanizer.md §7) — never ship a dense/partial piece
