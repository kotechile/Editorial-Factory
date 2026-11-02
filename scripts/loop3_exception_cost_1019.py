#!/usr/bin/env python3
"""Per-draft Loop 3 driver (evergreen 2026-10-19 sales_order_service_level_otif).

Rebinds humanize_loop3.call_gemini to a 900s socket timeout per skills/claude_humanizer.md §7:
the module default is 240s and a ~1,000-word draft on the DeepSeek frontier can exceed it,
aborting attempt 1 fatally and leaving no _final.md.
"""
import json, sys, pathlib, urllib.request

sys.path.insert(0, "/root/editorial-factory/scripts")
import humanize_loop3 as hl

ROOT = pathlib.Path("/root/editorial-factory")
draft = ROOT / sys.argv[1]
out = draft.with_name(draft.name.replace("_draft.md", "_final.md"))


def call_gemini_long(prompt):
    """DeepSeek frontier with this draft's wider socket timeout (was a Gemini rebind)."""
    return hl.call_frontier(prompt, timeout=900)


hl.call_gemini = call_gemini_long
text = draft.read_text()
result = hl.humanize_single_draft(text, out)
print("WROTE", out, "exists=", out.exists())
