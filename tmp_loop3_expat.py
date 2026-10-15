#!/usr/bin/env python3
"""Loop 3 driver for one draft (evergreen, expat) — 480s socket timeout per skills/claude_humanizer.md §7."""
import sys, pathlib, urllib.request, json
sys.path.insert(0, 'scripts')
import humanize_loop3 as hl

_orig = hl.call_gemini


def call_gemini(prompt):
    body = {"contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"maxOutputTokens": 20000, "temperature": 0.7}}
    req = urllib.request.Request(hl.URL, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=480) as r:
        j = json.loads(r.read().decode())
    return j["candidates"][0]["content"]["parts"][0]["text"]


hl.call_gemini = call_gemini

D = pathlib.Path('/root/editorial-factory/context/drafts/2026-10-15_three-forms-cost-more-than-tax_draft.md')
OUT = pathlib.Path('/root/editorial-factory/context/drafts/2026-10-15_three-forms-cost-more-than-tax_final.md')
res = hl.humanize_single_draft(D.read_text(), OUT)
print("FINAL WRITTEN:", OUT.exists(), OUT.stat().st_size if OUT.exists() else 0)
