#!/usr/bin/env python3
"""Per-draft Loop 3 driver (900s socket rebind) for your-60-fast-lane-is-blind (skills/claude_humanizer.md §7)."""
import json, sys, pathlib, urllib.request

sys.path.insert(0, "/root/editorial-factory/scripts")
import humanize_loop3 as hl

ROOT = pathlib.Path("/root/editorial-factory")
draft = ROOT / "context/drafts/2026-10-27_your-60-fast-lane-is-blind_draft.md"
out = ROOT / "context/drafts/2026-10-27_your-60-fast-lane-is-blind_final.md"


def call_gemini_long(prompt):
    """DeepSeek frontier with this draft's wider socket timeout (was a Gemini rebind)."""
    return hl.call_frontier(prompt, timeout=900)


hl.call_gemini = call_gemini_long
text = draft.read_text()
result = hl.humanize_single_draft(text, out)
print("WROTE", out, "exists=", out.exists())
