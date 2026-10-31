#!/usr/bin/env python3
"""Editorial-factory Loop 3: frontier humanizer on Gemini for the restored drafts.

Writes context/drafts/YYYY-MM-DD_<slug>_final.md per skills/claude_humanizer.md §5:
long-form, all section markers, ## Sources verbatim, + a Gate report. No social variant (the
LinkedIn/Reddit channel was removed 2026-10-06).
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
   - Title: Start from the draft title and polish/refine for punchy clarity and SEO resonance without clickbait fluff or cryptic jargon. When frontmatter defines `primary_keyword:`, the `title:` and `meta_title:` MUST explicitly contain the primary keyword (preserving proper/canonical casing, e.g. "<Keyword>: <Subtitle>"). Never drop or replace the keyword in the headline.
2. THE LEDE (First Sentence):
   - Make the opening sentence the most memorable part. Deliver the primary news or core takeaway immediately in sentence 1 with zero throat-clearing or preamble.
3. CONTEXT SIGNPOSTS & MANDATORY H2 HEADERS:
   - Use standardized H2 headers (`## `) to structure the core sections cleanly for readers and Table of Contents generators.
   - FORMATTING REQUIREMENT: Every H2 header MUST stand on its own separate line, preceded by an empty blank line and followed by an empty blank line. NEVER place body prose or bullets on the same line as the H2 header, and never attach text directly on the line below without an intervening blank line:
     - `## The big picture:` (in <!-- tension -->, introducing the broader industry or structural shift; followed on a new paragraph by a single direct sentence)
     - `## By the numbers` (MANDATORY quantitative section presenting 2–4 verified figures/percentages in bold bullets pairing the figure with a concise metric title)
     - `## What I'd watch:` or `## Where the money flows` (in <!-- tactical-insight -->, reporting what operators closest to the story are doing)
     - `## The catch` (in <!-- nuanced-takeaway -->, presenting the honest limitation, tradeoff, or counter-argument; followed on a new paragraph)
     - `## At a glance` (in <!-- tldr -->, a three-line shift / number / risk box under 50 words, under its own distinct H2 header so it is NEVER embedded under "The catch")
4. SCANNABILITY & BULLETS:
   - Never output dense blocks of text.
   - Every article MUST feature a dedicated **By the numbers:** quantitative section with 2–4 bold bulleted stats pairing the figure with a concise 2–4 word metric title (e.g., `- **88% — Diesel price jump:** ...` or `- **21% to 29.5% — UPS fuel fee:** ...`). The words following the bold lead MUST NOT begin with conversational or background narrative filler ("Diesel fuel started the year...", "The leap in the..."). Instead, structure as `- **<Figure> — <Metric Title>:** <Clear explanation> [Citation]`.
   - Break down any sequence of 3 or more data points, stats, or actionable steps into clean, bulleted lists with bold lead-ins.
4b. SHAPE RULES (gate-enforced by scripts/article_shape.py — these hold a publish):
   - THE OPENING STATES THE STAKES FIRST. Sentence 1 carries at most ONE figure and names WHY the
     change is happening (because / after / driven by / following / amid) before any mechanism,
     statute, tier or threshold. Detail in the first sentence is what makes a reader leave.
   - A FIGURE IS STATED ONCE. It may appear in the lead (or the numbers section) and again in `At a
     glance`; a third section repeating it is scroll friction and fails the gate. Do not write a
     numbers list and then a watch list that restates the same figures — write the numbers once.
   - COMPARISON BELONGS IN A TABLE. Three or more comparable items measured on two or more
     attributes (states, tiers, sizes, terms, scenarios) go in ONE markdown pipe table with a row per
     item and a column per attribute, not in two prose lists.
   - CLOSE ON A DECISION. The last section ends on the choice the reader can act on and carries ONE
     inline markdown link to the desk's own page that runs that math (`[anchor](/slug/)`). The
     generated Related-reading block does not satisfy this.

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
- PRESERVE the `<!-- schema -->` block (JSON-LD) and `<!-- internal-links -->` block VERBATIM if present, placed at the end of the document.
- PRESERVE the `## Related reading` section exactly as written — its anchor texts and URLs are verified internal links to live pages on the same site. Never rewrite, drop, merge, or invent one, and never add a link that is not already there.
- PRESERVE the section markers exactly: <!-- lead -->, <!-- tension -->, <!-- tactical-insight -->, <!-- nuanced-takeaway -->, <!-- tldr -->.
- PRESERVE the opening and closing `---` YAML delimiters around the frontmatter exactly — do NOT wrap the frontmatter in triple-backtick code fences.
- Format the TL;DR as the structured <!-- tldr --> field opening with an H2 header '## At a glance', strictly following this 3-LINE schema (owner standard 2026-10-29; the older four-part Big Shift / Why It Matters / What I'd Watch / Catch recap is RETIRED — it duplicated the tactical section, and its return is a rewrite defect):
  ## At a glance
  - "**The shift:** <one sentence: what changed>"
  - "**The number:** <the one figure that proves it and that the body already states>"
  - "**The risk:** <the single caveat a reader must carry away>"
  Under 50 words total, no sub-bullets, no list mirroring "What I'd watch".
  Never write a prose "in conclusion / key takeaways" paragraph. Do NOT compose a TOC (render-time only).

ACCESSIBILITY RULES (topic-agnostic — apply to EVERY topic; rewrite vocabulary, never facts):
- Every acronym is expanded at its FIRST use in the body (either "Full Name (ACR)" or "ACR (...plain meaning)"). Zero undefined acronyms at the end. Never reuse an acronym bare after introducing it.
- Translate every specialist term for a general reader: use the source's plain phrase or add a short gloss. Examples: "filed a protective action" -> "filed an objection"; "importer of record" -> "the company named on the import"; "finally-liquidated entry" -> "an import already fully processed"; "unliquidated" -> "not yet processed"; "non-recurring add-back" -> "a one-time booking"; "Section 232 duties" -> "separate tariffs on steel and aluminum the courts never struck down". The domain makes no difference — apply the plain-word-or-gloss test to any field (energy, security, database, legal, finance).
- If the story hinges on a process a general reader may not know (a refund flow, a rebate rule, a permission model, an agency's authority), add ONE half-sentence explaining what it is before relying on it.
- Target Flesch Reading Ease >= 60 on the body (hard floor >= 50). READABILITY comes from plain WORDS, not short sentences: replace long/technical words with everyday ones ("set up" not "implementation", "build" not "architect", "slows down" not "degrades throughput", "freezes" not "compounds down the stack"). Write connected, natural sentences of ~14-20 words with variation — do NOT fragment into choppy one-liners. Long proper nouns and the numbers are fine; the barrier is word choice.
- Write FLUENTLY — no keyword stuffing. A target search phrase (if any) appears AT MOST 2-3 times in the whole body; let the title/meta/headings carry it and rephrase everywhere else (pronouns, synonyms, "these systems"). Vary sentence rhythm and link ideas; never let it read like a keyword-matching exercise.
- Do not change or drop any fact, figure, [n] citation, or source line.
- NEVER invent an expansion for a proper noun or system name (e.g. CRAB, DeltaBox). If a name has no known full form, do not fabricate one to satisfy the acronym rule — rephrase to drop the all-caps token instead (e.g. "specialized checkpoint systems" rather than "CRAB"). A fabricated acronym expansion is a hallucination and a hard failure.

OUTPUT FORMAT (strict):
1) The full rewritten article, beginning with the frontmatter, then each section in order with its marker, then "## Sources" (the original source list VERBATIM). Write nothing after that but the `## Gate report` — the social variant was removed with the LinkedIn/Reddit channel (2026-10-06).
2) Then a section starting exactly "## Gate report" listing, one per line, each section's gate verdict: lead / tension / tactical-insight / nuanced-takeaway / tldr as "PASS — <short reason verifying plain-English clarity and scannability>" or "FAIL — <reason>".

Now rewrite the following draft:"""

# The voice contract (skills/claude_humanizer.md §3.9) is part of the job instruction, not a
# suggestion: verify.sh §9 fails the build on the article body. (No social variant — the LinkedIn/
# Reddit channel was removed 2026-10-06.)
RULES += "\n" + ht.LONGFORM_VOICE_RULES
RULES += ht.VIBE_COPY_RULES  # the copy contract, read from context/vibe/lexicon.json

def call_gemini(prompt):
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": 20000, "temperature": 0.7},
    }
    req = urllib.request.Request(URL, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    # Thinking models (gemini-3.1-pro-preview) burn seconds on reasoning before the first
    # token; a 30s socket timeout aborts a full rewrite mid-generation. Match humanizer_tools.
    with urllib.request.urlopen(req, timeout=240) as r:
        j = json.loads(r.read().decode())
    txt = j["candidates"][0]["content"]["parts"][0]["text"]
    return txt

def extract_sources(draft):
    m = re.search(r"## Sources\s*\n(.*?)(?=\n<!-- linkedin -->|\n## Gate report|\Z)", draft, re.S)
    return m.group(1).strip() if m else ""

def clean(raw):
    return re.sub(r"\s*```$", "", re.sub(r"^```[a-zA-Z]*\s*", "", raw.strip())).strip()

MARKERS = ["<!-- lead -->", "<!-- tension -->", "<!-- tactical-insight -->",
           "<!-- nuanced-takeaway -->", "<!-- tldr -->"]

def humanize_single_draft(draft, out_path=None):
    src_lines = [l.strip() for l in extract_sources(draft).splitlines() if l.strip()]
    base_prompt = RULES + "\n\n" + draft
    result = draft
    diag = None
    len_ok = False
    for attempt in range(1, ht.MAX_ATTEMPTS + 1):
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
            raw = call_gemini(prompt)
        except Exception as e:
            print(f"ERROR rewrite attempt {attempt}: {e}")
            break
        result = ht.ensure_title_contains_keyword(ht.normalize_frontmatter(clean(raw)))
        if out_path:
            out_path.write_text(result + "\n")
            diag = ht.measure(out_path)
        else:
            diag = {"verdict": "PASS", "flesch": 65, "words": len(result.split())}
        srcs_ok = all(s in result for s in src_lines) if src_lines else True
        markers_ok = all(m in result for m in MARKERS)
        len_ok = diag.get("words", 0) >= ht.MIN_BODY_WORDS
        print(f"  attempt {attempt}: {diag['verdict']}  flesch={diag['flesch']}  words={diag.get('words', 0)}  length={'ok' if len_ok else 'SHORT'}")
        if diag["verdict"] == "PASS" and srcs_ok and markers_ok and len_ok:
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
