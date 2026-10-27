#!/usr/bin/env python3
"""Per-draft Loop 3 driver (900s socket rebind) for your-miss-costs-9x-the-chargeback (skills/claude_humanizer.md §7)."""
import json, sys, pathlib, urllib.request

sys.path.insert(0, "/root/editorial-factory/scripts")
import humanize_loop3 as hl

ROOT = pathlib.Path("/root/editorial-factory")
draft = ROOT / "context/drafts/2026-10-27_your-miss-costs-9x-the-chargeback_draft.md"
out = ROOT / "context/drafts/2026-10-27_your-miss-costs-9x-the-chargeback_final.md"


def call_gemini_long(prompt):
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": 20000, "temperature": 0.7},
    }
    req = urllib.request.Request(hl.URL, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=900) as r:
        j = json.loads(r.read().decode())
    return j["candidates"][0]["content"]["parts"][0]["text"]


hl.call_gemini = call_gemini_long
text = draft.read_text()
result = hl.humanize_single_draft(text, out)
print("WROTE", out, "exists=", out.exists())
