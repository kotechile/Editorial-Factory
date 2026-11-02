#!/usr/bin/env python3
"""Per-draft Loop 3 driver (900s socket rebind) for kroger-direct-buy-retires-its-own-fine (skills/claude_humanizer.md §7)."""
import sys, pathlib

sys.path.insert(0, "/root/editorial-factory/scripts")
import humanize_loop3 as hl

ROOT = pathlib.Path("/root/editorial-factory")
draft = ROOT / "context/drafts/2026-11-02_kroger-direct-buy-retires-its-own-fine_draft.md"
out = ROOT / "context/drafts/2026-11-02_kroger-direct-buy-retires-its-own-fine_final.md"


def call_frontier_long(prompt):
    """DeepSeek frontier with this draft's wider socket timeout."""
    return hl.call_frontier(prompt, timeout=900)


hl.call_gemini = call_frontier_long
text = draft.read_text()
result = hl.humanize_single_draft(text, out)
print("WROTE", out, "exists=", out.exists())
