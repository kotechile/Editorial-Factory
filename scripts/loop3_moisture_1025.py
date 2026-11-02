#!/usr/bin/env python3
"""Per-draft Loop 3 driver (2026-10-25 home_diagnostics_tech / review track: moisture meters) with a
900s socket timeout (skills/claude_humanizer.md §7)."""
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
hl.humanize_single_draft(text, out)
print("WROTE", out, "exists=", out.exists(), flush=True)
