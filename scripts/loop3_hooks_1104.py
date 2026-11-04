#!/usr/bin/env python3
"""Per-draft Loop 3 driver for your-2-silent-agent-hooks (skills/claude_humanizer.md §7).

Follows the 2026-11-04 transport fix: frontier_llm.chat(thinking=False) with a 900 s socket and a
16k output budget, because the reasoning pass can consume the whole ceiling and return no text.
"""
import pathlib, sys

sys.path.insert(0, "/root/editorial-factory/scripts")
import humanize_loop3 as hl
import frontier_llm as fl

ROOT = pathlib.Path("/root/editorial-factory")
draft = ROOT / "context/drafts/2026-11-04_your-2-silent-agent-hooks_draft.md"
out = ROOT / "context/drafts/2026-11-04_your-2-silent-agent-hooks_final.md"


def call_frontier_long(prompt):
    return fl.chat(prompt, max_tokens=16000, temperature=0.7, timeout=900, thinking=False)


hl.call_gemini = call_frontier_long
result = hl.humanize_single_draft(draft.read_text(), out)
print("WROTE", out, "exists=", out.exists())
