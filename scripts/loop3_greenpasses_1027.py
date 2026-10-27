#!/usr/bin/env python3
"""Per-draft Loop 3 driver with a 900s socket timeout (skills/claude_humanizer.md §7).

`humanize_loop3.call_gemini` hard-codes a 240s socket timeout and a ~1,200-word draft on
gemini-3.1-pro-preview can exceed it, aborting attempt 1 fatally (no _final.md). This rebinds the
module-level call_gemini to the same body with a longer timeout and leaves the marker/source/length
checks and the accessibility retry loop untouched.
"""
import json, sys, pathlib, urllib.request

sys.path.insert(0, "/root/editorial-factory/scripts")
import humanize_loop3 as hl

ROOT = pathlib.Path("/root/editorial-factory")
draft = ROOT / sys.argv[1]
out = draft.with_name(draft.name.replace("_draft.md", "_final.md"))


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
