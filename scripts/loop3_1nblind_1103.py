#!/usr/bin/env python3
"""Per-draft Loop 3 driver (900 s socket rebind) for your-plant-was-1n-and-blind (skills/claude_humanizer.md §7)."""
import sys, pathlib

sys.path.insert(0, "/root/editorial-factory/scripts")
import humanize_loop3 as hl

ROOT = pathlib.Path("/root/editorial-factory")
draft = ROOT / "context/drafts/2026-11-03_your-plant-was-1n-and-blind_draft.md"
out = ROOT / "context/drafts/2026-11-03_your-plant-was-1n-and-blind_final.md"


def call_frontier_long(prompt):
    return hl.call_frontier(prompt, timeout=900)


hl.call_gemini = call_frontier_long
text = draft.read_text()
result = hl.humanize_single_draft(text, out)
print("WROTE", out, "exists=", out.exists())
