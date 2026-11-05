#!/usr/bin/env python3
"""Per-draft Loop 3 driver for your-port-clears-35688-boxes-dont (skills/claude_humanizer.md §7).

DeepSeek bills reasoning tokens inside max_tokens, so a long rewrite can come back with
finish_reason=length at the module default (observed on this draft's attempt 1). Raise the
budget here and retry once with a tightening suffix rather than dying on attempt 1.
"""
import sys, pathlib

sys.path.insert(0, "/root/editorial-factory/scripts")
import humanize_loop3 as hl
import humanizer_tools as ht
import frontier_llm

ROOT = pathlib.Path("/root/editorial-factory")
draft = ROOT / "context/drafts/2026-11-05_your-port-clears-35688-boxes-dont_draft.md"
out = ROOT / "context/drafts/2026-11-05_your-port-clears-35688-boxes-dont_final.md"

TIGHTEN = ("\n\nReturn ONLY the rewritten article (frontmatter, marked sections, ## Sources, "
           "## Gate report). No preamble, no commentary, no repeated draft.")


def call_frontier_long(prompt):
    try:
        return ht.call_frontier(prompt, max_tokens=32000, timeout=900)
    except frontier_llm.FrontierError as exc:
        if "truncated" not in str(exc):
            raise
        print("RETRY after truncation, tighter prompt", flush=True)
        return ht.call_frontier(prompt + TIGHTEN, max_tokens=32000, timeout=900)


hl.call_gemini = call_frontier_long
text = draft.read_text()
result = hl.humanize_single_draft(text, out)
print("WROTE", out, "exists=", out.exists())
