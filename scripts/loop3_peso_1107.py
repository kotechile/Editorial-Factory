#!/usr/bin/env python3
"""Per-draft Loop 3 driver for 2026-11-07_your-peso-upside-is-priced (skills/claude_humanizer.md §7).

Frontier = deepseek-v4-pro via scripts/frontier_llm.py, reasoning pass off (`thinking=False`),
900 s socket, log /tmp/loop3_peso.log.
"""
import pathlib, sys

sys.path.insert(0, "/root/editorial-factory/scripts")
import humanize_loop3 as hl
import frontier_llm as fl

ROOT = pathlib.Path("/root/editorial-factory")
draft = ROOT / "context/drafts/2026-11-07_your-peso-upside-is-priced_draft.md"
out = ROOT / "context/drafts/2026-11-07_your-peso-upside-is-priced_final.md"


def call_frontier_long(prompt):
    return fl.chat(prompt, max_tokens=16000, temperature=0.7, timeout=900, thinking=False)


hl.call_gemini = call_frontier_long
result = hl.humanize_single_draft(draft.read_text(), out)
print("WROTE", out, "exists=", out.exists())
