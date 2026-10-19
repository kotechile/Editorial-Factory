#!/usr/bin/env python3
"""Loop 3 driver for the 2026-10-19 agentic_ai EVERGREEN draft (answer-field-first-costs-38-points).

`skills/claude_humanizer.md` §7: humanize_loop3's own call_gemini carries a hard-coded 240 s
socket timeout that aborts a long draft on its first attempt, and a 900 s rebind converged a
rewrite the shorter timeouts aborted (learned 2026-10-19). This driver rebinds the module-level
`call_gemini` to a 900 s socket timeout and calls `humanize_single_draft()` directly (never
`humanize_all()` — it is month-locked to 2026-09). Every other behaviour (frontmatter
normalisation, accessibility retry loop, source / marker / length checks) is unchanged.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import humanizer_tools as ht  # noqa: E402
import humanize_loop3 as hl  # noqa: E402


def call_gemini_wide(prompt):
    return ht.call_gemini(prompt, timeout=900)


hl.call_gemini = call_gemini_wide

slug = "answer-field-first-costs-38-points"
draft_path = ROOT / "context" / "drafts" / f"2026-10-19_{slug}_draft.md"
final_path = ROOT / "context" / "drafts" / f"2026-10-19_{slug}_final.md"

print("pre-flight:", flush=True)
print(ht.call_gemini("Reply with the single word OK.", max_tokens=200, timeout=120).strip()[:80], flush=True)

hl.humanize_single_draft(draft_path.read_text(), final_path)
print("EXISTS:", final_path.exists(), final_path.stat().st_size if final_path.exists() else 0, flush=True)
