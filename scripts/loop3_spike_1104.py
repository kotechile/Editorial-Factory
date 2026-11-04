#!/usr/bin/env python3
"""Per-draft Loop 3 driver for your-10-minute-spike-bills-an-hour (skills/claude_humanizer.md §7).

2026-11-04: the default driver died twice with `frontier returned no text (finish_reason=length)` —
the reasoning pass spent 8k, then 32k completion tokens entirely on `reasoning_content` and returned
an empty body for this prompt (humanizer RULES + a 1,166-word draft). The transport now takes
`thinking=False`, which the provider answers normally, so the rewrite runs with the reasoning pass
off and a 900 s socket.
"""
import pathlib, sys

sys.path.insert(0, "/root/editorial-factory/scripts")
import humanize_loop3 as hl
import humanizer_tools as ht
import frontier_llm as fl

ROOT = pathlib.Path("/root/editorial-factory")
draft = ROOT / "context/drafts/2026-11-04_your-10-minute-spike-bills-an-hour_draft.md"
out = ROOT / "context/drafts/2026-11-04_your-10-minute-spike-bills-an-hour_final.md"


def call_frontier_long(prompt):
    """DeepSeek frontier, reasoning pass off, 900 s socket."""
    return fl.chat(prompt, max_tokens=16000, temperature=0.7, timeout=900, thinking=False)


hl.call_gemini = call_frontier_long
result = hl.humanize_single_draft(draft.read_text(), out)
print("WROTE", out, "exists=", out.exists())
