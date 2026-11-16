#!/usr/bin/env python3
"""One-off Loop 3 humanizer for a single draft (Gemini frontier), per skills/claude_humanizer.md."""
import re, sys, pathlib
import humanizer_tools as ht  # retry loop + accessibility feedback + frontier call

ROOT = pathlib.Path("/root/editorial-factory")
draft_rel = sys.argv[1] if len(sys.argv) > 1 else "context/drafts/2026-09-07_anthropic-multiagent-turf-war_draft.md"

import humanize_loop3 as hl  # noqa: E402  (the pipeline's one RULES source)

# ONE RULES source. This driver used to carry its own 14 KB copy of the rewrite contract; the two
# copies drifted (the second one still asked for a self-graded "## Gate report", which the reviewer
# strips, and it lacked the 4a/4b law). It now uses humanize_loop3.RULES and adds only the block
# that is specific to this driver: the per-section gate list.
SECTION_GATES = """SECTION GATES (each section must pass its own gate):
- <!-- lead -->: delivers the core news/stat immediately in sentence 1; no throat-clearing or preamble. HIGHEST PRIORITY.
- <!-- tension -->: the section that says what changed and who it lands on. Give it an H2 in this article's own words (the house label '## The big picture:' is a fallback). A '## By the numbers' block is optional — carry the figures in the sentences that use them unless the piece is genuinely a table of numbers.
- <!-- tactical-insight -->: what the people closest to the story are doing and what the writer expects next, structured with clean bullets and bold lead-ins for 3+ items; observations, never instructions to the reader.
- <!-- nuanced-takeaway -->: honest limitation / counter-argument with '## The catch' H2 header.
- <!-- tldr -->: opens with '## At a glance' H2 header; follows the three-line schema (**The shift**, **The number**, **The risk**) under 50 words with no sub-bullets and no recap of the tactical section; plain, accessible English without unexplained buzzwords.

"""

RULES = hl.RULES.replace("Now rewrite the following draft:",
                         SECTION_GATES + "Now rewrite the following draft:")

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
    result = ht.normalize_frontmatter(clean(raw))
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
