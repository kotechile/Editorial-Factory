#!/usr/bin/env python3
"""Per-draft Loop 3 driver with a 600s socket timeout (skills/claude_humanizer.md §7).

`humanize_one.py` and `humanize_loop3.call_gemini` both hard-code a 240s socket timeout; a
~1,000-word draft on the DeepSeek frontier can exceed it and abort attempt 1 fatally.
This rebinds the module-level call_gemini to the same call with a longer timeout.
"""
import json, sys, pathlib, urllib.request

sys.path.insert(0, "/root/editorial-factory/scripts")
import humanize_loop3 as hl

ROOT = pathlib.Path("/root/editorial-factory")
draft = ROOT / sys.argv[1]
out = draft.with_name(draft.name.replace("_draft.md", "_final.md"))


def call_gemini_long(prompt):
    """DeepSeek frontier with this draft's wider socket timeout (was a Gemini rebind)."""
    return hl.call_frontier(prompt, timeout=600)


hl.call_gemini = call_gemini_long
text = draft.read_text()
result = hl.humanize_single_draft(text, out)
print("WROTE", out, "exists=", out.exists())
