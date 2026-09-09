#!/usr/bin/env python3
"""One-off Loop 3 humanizer for a single draft (Gemini frontier), per skills/claude_humanizer.md."""
import re, sys, pathlib
import humanizer_tools as ht  # retry loop + accessibility feedback + frontier call

ROOT = pathlib.Path("/root/editorial-factory")
draft_rel = sys.argv[1] if len(sys.argv) > 1 else "context/drafts/2026-09-07_anthropic-multiagent-turf-war_draft.md"

RULES = """You are the Frontier Humanizer (Loop 3 — final rewrite) for an editorial pipeline. Rewrite the given story draft in a genuine human editorial voice.

NEGATIVE CONSTRAINTS (apply verbatim, no exceptions):
- No empty intros: "In today's fast-paced world", "In an era of", "It's no secret that".
- No hollow transitions: "Furthermore", "Moreover", "It's important to remember", "delve into", "dive deep", "let's explore", "In conclusion".
- No corporate sign-offs: "In summary", "ultimately, it's about", "the key takeaway is simple".
- No hedging filler: "some might argue", "it could be said", "interestingly enough".
- No adjective-stacking before nouns ("cutting-edge, revolutionary, game-changing").
- PRESERVE the lead incident/stat and the pragmatic takeaway — rephrase, never re-source.
- PRESERVE every citation [n] inline and the ## Sources list VERBATIM (do not change, merge, or drop any source line or its URL).
- PRESERVE the frontmatter (title/vertical/persona/date/slug) unchanged.
- PRESERVE the section markers exactly: <!-- lead -->, <!-- tension -->, <!-- tactical-insight -->, <!-- nuanced-takeaway -->, <!-- tldr -->, <!-- linkedin -->.
- PRESERVE the `<!-- schema -->` JSON-LD and `<!-- internal-links -->` blocks verbatim at the document end (do not remove or rewrite them).
- Keep the TL;DR as the structured <!-- tldr --> field, exactly 3 scannable bullet items starting with "-". Never write a prose "in conclusion / key takeaways" paragraph. Do NOT compose a TOC.

VOICE RULES:
- Vary sentence length; short declaratives next to longer causal sentences.
- Prefer concrete nouns and named actors over abstractions.
- One idea per paragraph; kill any sentence that does not earn its place.
- Tighten cadence and rhythm; remove mechanical parallelism.

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
