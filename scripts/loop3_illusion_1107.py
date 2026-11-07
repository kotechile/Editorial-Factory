#!/usr/bin/env python3
"""Per-draft Loop 3 driver for your-512x384-cameras-10x-illusion (skills/claude_humanizer.md §7).

Frontier = deepseek-v4-pro via scripts/frontier_llm.py, reasoning pass off (`thinking=False`),
900 s socket, detached run, log /tmp/loop3_illusion.log.
"""
import pathlib, sys

sys.path.insert(0, "/root/editorial-factory/scripts")
import humanize_loop3 as hl
import frontier_llm as fl

ROOT = pathlib.Path("/root/editorial-factory")
draft = ROOT / "context/drafts/2026-11-07_your-512x384-cameras-10x-illusion_draft.md"
out = ROOT / "context/drafts/2026-11-07_your-512x384-cameras-10x-illusion_final.md"


def call_frontier_long(prompt):
    return fl.chat(prompt, max_tokens=16000, temperature=0.7, timeout=900, thinking=False)


hl.call_gemini = call_frontier_long
result = hl.humanize_single_draft(draft.read_text(), out)
print("WROTE", out, "exists=", out.exists())
