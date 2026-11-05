#!/usr/bin/env python3
"""Per-draft Loop 3 driver with a 900s socket timeout (skills/claude_humanizer.md §7).

Reasoning tokens count inside `max_tokens` on DeepSeek, so the rewrite rebinds the transport to
`thinking=False`: without it the model burned the whole 20k budget on the reasoning pass and
returned empty content with finish_reason=length (2026-11-05).
"""
import sys, pathlib

sys.path.insert(0, "/root/editorial-factory/scripts")
import humanize_loop3 as hl
import frontier_llm

ROOT = pathlib.Path("/root/editorial-factory")
draft = ROOT / sys.argv[1]
out = draft.with_name(draft.name.replace("_draft.md", "_final.md"))


def call_frontier_long(prompt):
    return frontier_llm.chat(prompt, timeout=900, max_tokens=frontier_llm.MAX_TOKENS,
                             temperature=0.7, thinking=False)


hl.call_gemini = call_frontier_long
text = draft.read_text()
hl.humanize_single_draft(text, out)
print("WROTE", out, "exists=", out.exists())
