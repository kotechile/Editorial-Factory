#!/usr/bin/env python3
"""Per-draft Loop 3 driver (2026-10-23 resilient_home_assets 745 MW) with a 900s socket timeout (skills/claude_humanizer.md §7)."""
import json, sys, pathlib, urllib.request

sys.path.insert(0, "/root/editorial-factory/scripts")
import humanize_loop3 as hl

ROOT = pathlib.Path("/root/editorial-factory")
draft = ROOT / sys.argv[1]
out = draft.with_name(draft.name.replace("_draft.md", "_final.md"))


def call_gemini_long(prompt):
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"maxOutputTokens": 24000, "temperature": 0.7},
    }
    req = urllib.request.Request(hl.URL, data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=900) as r:
        j = json.loads(r.read().decode())
    c = j["candidates"][0]
    print("finish:", c.get("finishReason"), "usage:", j.get("usageMetadata"), flush=True)
    return c["content"]["parts"][0]["text"]


hl.call_gemini = call_gemini_long
text = draft.read_text()
hl.humanize_single_draft(text, out)
print("WROTE", out, "exists=", out.exists(), flush=True)
