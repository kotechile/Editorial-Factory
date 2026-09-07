#!/usr/bin/env python3
"""Loop 3 frontier humanizer for an arbitrary draft (Gemini frontier), per skills/claude_humanizer.md."""
import json, re, sys, pathlib, urllib.request

ROOT = pathlib.Path("/root/editorial-factory")
draft_rel = sys.argv[1] if len(sys.argv) > 1 else "context/drafts/2026-09-07_ieepa-refund-wave-hits-earnings_draft.md"

KEY = None
for envf in ["/root/.hermes/profiles/stylist/.env", "/root/.hermes/.env"]:
    p = pathlib.Path(envf)
    if p.exists():
        for line in p.read_text().splitlines():
            if line.startswith("GOOGLE_API_KEY="):
                KEY = line.split("=", 1)[1].strip().strip('"').strip("'")
                break
    if KEY:
        break
assert KEY, "GOOGLE_API_KEY not found"

MODEL = "gemini-3.1-pro-preview"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={KEY}"

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
- Keep the TL;DR as the structured <!-- tldr --> field, exactly 3 scannable bullet items starting with "-". Never write a prose "in conclusion / key takeaways" paragraph. Do NOT compose a TOC.

SECTION GATES (each section must pass its own gate):
- <!-- lead -->: opens with a concrete incident or figure in the first 2 sentences; does NOT open like a definition or "the world is changing". HIGHEST PRIORITY.
- <!-- tension -->: names what shifted and who it hurts/helps; not vague "the industry is evolving".
- <!-- tactical-insight -->: one specific, doable move for the persona; not generic advice like "invest in AI".
- <!-- nuanced-takeaway -->: an honest limitation or counter-argument; not a hollow hedge or a cheerlead.
- <!-- tldr -->: exactly 3 scannable bullets; does not read like a summary paragraph.

VOICE RULES:
- Vary sentence length; short declaratives next to longer causal sentences.
- Prefer concrete nouns and named actors over abstractions.
- One idea per paragraph; kill any sentence that does not earn its place.
- Tighten cadence and rhythm; remove mechanical parallelism.

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

body = {"contents": [{"parts": [{"text": RULES + "\n\n" + draft}]}],
        "generationConfig": {"maxOutputTokens": 7000, "temperature": 0.7}}
req = urllib.request.Request(URL, data=json.dumps(body).encode(),
                             headers={"Content-Type": "application/json"})
with urllib.request.urlopen(req, timeout=240) as r:
    j = json.loads(r.read().decode())
result = j["candidates"][0]["content"]["parts"][0]["text"]

result = re.sub(r"^```[a-zA-Z]*\s*", "", result.strip())
result = re.sub(r"\s*```$", "", result).strip()

srcs_draft = extract_sources(draft)
srcs_ok = all(s in result for s in [l.strip() for l in srcs_draft.splitlines() if l.strip()])
out_path.write_text(result + "\n")
print(f"WROTE {out_path.name}  sources_check={'ok' if srcs_ok else 'MISSING'} gate_included={'## Gate report' in result} markers_ok={all(m in result for m in ['<!-- lead -->','<!-- tension -->','<!-- tactical-insight -->','<!-- nuanced-takeaway -->','<!-- tldr -->','<!-- linkedin -->'])}")
