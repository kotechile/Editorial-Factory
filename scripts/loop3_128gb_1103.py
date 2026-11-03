#!/usr/bin/env python3
"""Per-draft Loop 3 driver (900 s socket rebind) for your-128gb-laptop-2319-memory-bill (skills/claude_humanizer.md §7).

DeepSeek bills reasoning tokens inside max_tokens, so a long rewrite can come back with
finish_reason=length at the module default of 20,000. Raise the budget here and retry once with a
tightening suffix rather than dying on attempt 1 (see skills/llm-api-calls).
"""
import sys, pathlib

sys.path.insert(0, "/root/editorial-factory/scripts")
import humanize_loop3 as hl
import humanizer_tools as ht
import frontier_llm

ROOT = pathlib.Path("/root/editorial-factory")
draft = ROOT / "context/drafts/2026-11-03_your-128gb-laptop-2319-memory-bill_draft.md"
out = ROOT / "context/drafts/2026-11-03_your-128gb-laptop-2319-memory-bill_final.md"

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
