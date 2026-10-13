#!/usr/bin/env python3
"""Per-draft Loop 3 driver (evergreen) — humanize_one.py logic with a 480s frontier timeout.

Skills/claude_humanizer.md §7: a ~2,000-word rewrite on gemini-3.1-pro-preview has aborted at
240s (the module default), and humanize_loop3.call_gemini keeps its own hard-coded timeout, so a
per-draft driver must rebind it. Same applies to humanizer_tools.call_gemini.
"""
import re, sys, pathlib

sys.path.insert(0, "/root/editorial-factory/scripts")
import humanizer_tools as ht

_orig_call = ht.call_gemini
ht.call_gemini = lambda prompt, **kw: _orig_call(prompt, timeout=480, **kw)

ROOT = pathlib.Path("/root/editorial-factory")
draft_rel = sys.argv[1]
RULES = """You are the Frontier Humanizer & Stylist (Loop 3 — final rewrite) for an editorial pipeline. Rewrite the given story draft in a genuine, punchy human voice applying the SMART BREVITY system.

REQUIRED INPUTS & CONTEXT INGESTION:
- Target Audience: Read the `persona:` field from frontmatter and calibrate technical depth for this reader.
- The One Big Thing: Identify the single most important takeaway, benchmark stat, or decision from the draft.
- Raw Content: Restructure the unedited draft and verified claims while preserving every fact and inline citation [n].

SMART BREVITY STYLING PRINCIPLES:
1. THE TEASE (Headlines & Section Headers):
   - Section Headers (H2 `## `): Target 6 words or fewer. Active, punchy, descriptive.
   - Title: Keep the draft's title unless you can beat it without breaking the house headline standard
     (skills/story_draft.md): core headline <= 6 words, whole title <= 10 words and <= 60 chars, never
     open on 'The/A/An', keep a curiosity-gap or loss-aversion hook, anchor on a figure the article
     states, and call the reader out. It must promise nothing the article does not deliver in its first
     paragraph. Do not lengthen the title.
2. THE LEDE (First Sentence):
   - Make the opening sentence the most memorable part. Deliver the primary news or core takeaway immediately in sentence 1 with zero throat-clearing or preamble.
3. CONTEXT SIGNPOSTS & MANDATORY H2 HEADERS:
   - Use standardized H2 headers (`## `) to structure the core sections cleanly for readers and Table of Contents generators.
   - FORMATTING REQUIREMENT: Every H2 header MUST stand on its own separate line, preceded by an empty blank line and followed by an empty blank line:
     - `## The big picture:` (in <!-- tension -->)
     - `## By the numbers` (MANDATORY quantitative section presenting 2–4 verified figures in bold bullets pairing the figure with a concise metric title)
     - `## What I'd watch:` (in <!-- tactical-insight -->, reporting what operators closest to the story are doing)
     - `## The catch` (in <!-- nuanced-takeaway -->, presenting the honest limitation, tradeoff, or counter-argument)
     - `## At a glance` (in <!-- tldr -->, the 4-part Smart Brevity executive summary)
4. SCANNABILITY & BULLETS:
   - Never output dense blocks of text. Break down any sequence of 3 or more data points or moves into clean bullets with bold lead-ins.
   - By the numbers format: `- **<Figure> — <Metric Title>:** <Clear explanation> [Citation]`.
5. STRONG, SIMPLE DICTION:
   - Strip out passive verbs, weak adverbs, and bloated corporate jargon. Prefer short, everyday words that paint a clear picture.
6. PARAGRAPH DISCIPLINE:
   - Keep paragraphs exceptionally brief: 1 to 3 sentences maximum (the accessibility gate warns above 3).
7. THE EXIT ("Go Deeper"): conclude cleanly with the `<!-- internal-links -->` placeholder and `## Sources`.

NEGATIVE CONSTRAINTS (apply verbatim, no exceptions):
- No empty intros: "In today's fast-paced world", "In an era of", "It's no secret that".
- No hollow transitions: "Furthermore", "Moreover", "It's important to remember", "delve into", "dive deep", "let's explore", "In conclusion".
- No corporate sign-offs: "In summary", "ultimately, it's about", "the key takeaway is simple".
- No hedging filler: "some might argue", "it could be said", "interestingly enough".
- No adjective-stacking before nouns ("cutting-edge, revolutionary, game-changing").
- PRESERVE the lead incident/stat and the pragmatic takeaway — rephrase, never re-source.
- PRESERVE every citation [n] inline and the ## Sources list VERBATIM (do not change, merge, or drop any source line or its URL).
- PRESERVE the frontmatter keys exactly: title, vertical, persona, one_big_thing, date, slug, archetype, evergreen. The keys `archetype: evergreen` and `evergreen: true` MUST survive verbatim — this is an evergreen-track article. Polish `title` only as allowed above.
- PRESERVE the section markers exactly: <!-- lead -->, <!-- tension -->, <!-- tactical-insight -->, <!-- nuanced-takeaway -->, <!-- tldr -->.
- PRESERVE the opening and closing `---` YAML delimiters around the frontmatter exactly — do NOT wrap the frontmatter in triple-backtick code fences.
- PRESERVE the `<!-- internal-links -->` placeholder block verbatim (the persistence pass fills it).
- Format the TL;DR as the structured <!-- tldr --> field opening with an H2 header '## At a glance', strictly following this 4-part Smart Brevity schema:
  ## At a glance
  1) "- **The Big Shift:** <1-2 plain-English sentences explaining what happened and what the article is about>"
  2) "- **Why It Matters:** <1-2 sentences stating the economic, architectural, or industry impact and who is affected>"
  3) "- **What I'd Watch:** <what the writer is watching next, and why it matters>" followed by indented sub-bullets:
     "  - **<Move Name>:** <1-line plain-English definition explaining what it does and why>"
  4) "- **The Catch:** <trade-offs, caveats, realistic constraints>"
  Never write a prose "in conclusion / key takeaways" paragraph. Do NOT compose a TOC.

SECTION GATES (each section must pass its own gate):
- <!-- lead -->: delivers the core news/stat immediately in sentence 1; no throat-clearing. HIGHEST PRIORITY.
- <!-- tension -->: frames the shift with '## The big picture:' and includes the '## By the numbers' section; names who it hurts/helps.
- <!-- tactical-insight -->: what the people closest to the story are doing and what the writer expects next, structured with clean bullets for 3+ items; observations, never instructions to the reader.
- <!-- nuanced-takeaway -->: honest limitation / counter-argument with '## The catch'.
- <!-- tldr -->: opens with '## At a glance'; follows the 4-part schema in plain English.

ACCESSIBILITY RULES (topic-agnostic — apply to EVERY topic; rewrite vocabulary, never facts):
- Every acronym is expanded at its FIRST use in the body ("Full Name (ACR)" or "ACR (...plain meaning)"). Zero undefined acronyms at the end.
- Translate every specialist term for a general reader, or add a short gloss.
- Target Flesch Reading Ease >= 60 on the body (hard floor >= 50). Readability comes from plain WORDS: replace long/technical words with everyday ones, and keep sentences around 14-20 words with variation. This draft sits at 57.8 — lift it, do not let it drop.
- Write FLUENTLY — no keyword stuffing.
- Do not change or drop any fact, figure, [n] citation, or source line.
- NEVER invent an expansion for a proper noun. METR is glossed in the draft as "a nonprofit that studies AI risks" — keep that gloss, do not invent a full legal name.
- Do not add any figure, name, date or quantity that is not already in the draft.

OUTPUT FORMAT (strict):
1) The full rewritten article, beginning with the frontmatter, then each section in order with its marker, then "## Sources" (the original source list VERBATIM). Write nothing after that but the `## Gate report`.
2) Then a section starting exactly "## Gate report" listing, one per line, each section's gate verdict: lead / tension / tactical-insight / nuanced-takeaway / tldr as "PASS — <short reason>".
"""

RULES += "\n" + ht.LONGFORM_VOICE_RULES

draft_path = ROOT / draft_rel
out_path = draft_path.with_name(draft_path.name.replace("_draft.md", "_final.md"))
draft = draft_path.read_text()


def extract_sources(d):
    m = re.search(r"## Sources\s*\n(.*?)(?=\n<!-- linkedin -->|\n## Gate report|\Z)", d, re.S)
    return m.group(1).strip() if m else ""


def clean(raw):
    return re.sub(r"\s*```$", "", re.sub(r"^```[a-zA-Z]*\s*", "", raw.strip())).strip()


src_lines = [l.strip() for l in extract_sources(draft).splitlines() if l.strip()]
base_prompt = RULES + "\n\n" + draft
MARKERS = ["<!-- lead -->", "<!-- tension -->", "<!-- tactical-insight -->",
           "<!-- nuanced-takeaway -->", "<!-- tldr -->"]
result, diag, srcs_ok, markers_ok, len_ok, flags_ok = None, None, False, False, False, False
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
            extra.append("The article body is too short (under %d words). Restore depth from the draft — restate the tactical moves and the tension in full, using only already-verified figures. Never invent new claims or numbers." % ht.MIN_BODY_WORDS)
        if not flags_ok:
            extra.append("The frontmatter must keep `archetype: evergreen` and `evergreen: true` exactly.")
        prompt = ht.retry_prompt(base_prompt, result, diag, extra=extra)
    try:
        raw = ht.call_gemini(prompt)
    except Exception as e:
        print(f"ERROR attempt {attempt}: {e}", flush=True)
        break
    result = ht.normalize_frontmatter(clean(raw))
    out_path.write_text(result + "\n")
    srcs_ok = all(s in result for s in src_lines)
    markers_ok = all(m in result for m in MARKERS)
    flags_ok = "archetype: evergreen" in result and "evergreen: true" in result
    diag = ht.measure(out_path)
    len_ok = diag.get("words", 0) >= ht.MIN_BODY_WORDS
    print(f"attempt {attempt}: VERDICT {diag['verdict']}  flesch={diag['flesch']}  words={diag['words']}  "
          f"sources={'ok' if srcs_ok else 'MISSING'}  markers={'ok' if markers_ok else 'FAIL'}  "
          f"evergreen_flags={'ok' if flags_ok else 'MISSING'}  length={'ok' if len_ok else 'SHORT'}", flush=True)
    if diag["verdict"] == "PASS" and srcs_ok and markers_ok and len_ok and flags_ok:
        break

print(f"WROTE {out_path.name}  final_verdict={diag['verdict'] if diag else 'UNKNOWN'}  attempts={attempts}  "
      f"sources={'ok' if srcs_ok else 'MISSING'}  evergreen_flags={'ok' if flags_ok else 'MISSING'}  "
      f"length={'ok' if len_ok else 'SHORT'}", flush=True)
if diag and diag["verdict"] != "PASS":
    sys.exit(1)
