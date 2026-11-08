#!/usr/bin/env python3
"""Per-draft Loop 3 driver (900 s socket rebind) for the corded snow machine review
(skills/claude_humanizer.md §7). DeepSeek bills reasoning tokens inside max_tokens, so raise
the budget and retry once on truncation instead of dying on attempt 1."""
import sys, pathlib

sys.path.insert(0, "/root/editorial-factory/scripts")
import humanize_loop3 as hl
import humanizer_tools as ht
import frontier_llm

ROOT = pathlib.Path("/root/editorial-factory")
draft = ROOT / "context/drafts/2026-11-08_your-150-snow-shovels-6-inch-trap_draft.md"
out = ROOT / "context/drafts/2026-11-08_your-150-snow-shovels-6-inch-trap_final.md"

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
