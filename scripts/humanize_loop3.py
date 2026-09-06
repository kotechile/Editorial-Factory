#!/usr/bin/env python3
"""Editorial-factory Loop 3: frontier humanizer on Gemini for the restored drafts.

Writes context/drafts/YYYY-MM-DD_<slug>_final.md per skills/claude_humanizer.md §5:
long-form + LinkedIn, all section markers, ## Sources verbatim, + a Gate report.
"""
import json, os, re, sys, urllib.request, urllib.parse, pathlib

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
- Keep the TL;DR as the structured <!-- tldr --> field, exactly 3 scannable bullet items starting with "-". Never write a prose "in conclusion / key takeaways" paragraph. Do NOT compose a TOC (render-time only).

VOICE RULES:
- Vary sentence length; short declaratives next to longer causal sentences.
- Prefer concrete nouns and named actors over abstractions.
- One idea per paragraph; kill any sentence that does not earn its place.
- Tighten cadence and rhythm; remove any mechanical parallelism.

OUTPUT FORMAT (strict):
1) The full rewritten article, beginning with the frontmatter, then each section in order with its marker, then "## Sources" (the original source list VERBATIM), then the <!-- linkedin --> variant.
2) Then a section starting exactly "## Gate report" listing, one per line, each section's gate verdict: lead / tension / tactical-insight / nuanced-takeaway / tldr as "PASS — <short reason>" or "FAIL — <reason>".

Now rewrite the following draft:"""

def call_gemini(prompt):
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": 6000, "temperature": 0.7},
    }
    req = urllib.request.Request(URL, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        j = json.loads(r.read().decode())
    txt = j["candidates"][0]["content"]["parts"][0]["text"]
    return txt

def extract_sources(draft):
    m = re.search(r"## Sources\s*\n(.*?)(?=\n<!-- linkedin -->|\Z)", draft, re.S)
    return m.group(1).strip() if m else ""

for path in sorted(DRAFTS.glob("2026-09-*.md")):
    if "_final" in path.name:
        continue
    draft = path.read_text()
    out_name = path.name.replace("_draft.md", "_final.md")
    out = DRAFTS / out_name
    if out.exists():
        print(f"skip (exists): {out_name}")
        continue
    prompt = RULES + "\n\n" + draft
    try:
        result = call_gemini(prompt)
        # Extract only the article+gate portion (Gemini sometimes wraps in fences)
    except Exception as e:
        print(f"ERROR {path.name}: {e}")
        continue
    result = re.sub(r"^```[a-zA-Z]*\s*", "", result.strip())
    result = re.sub(r"\s*```$", "", result).strip()
    # sanity: citations preserved from the draft
    srcs_draft = extract_sources(draft)
    srcs_ok = all(s in result for s in [l.strip() for l in srcs_draft.splitlines() if l.strip()][:3])
    out.write_text(result + "\n")
    print(f"WROTE {out_name}  (sources_check={'ok' if srcs_ok else 'MISSING'}) gate_included={'## Gate report' in result}")
