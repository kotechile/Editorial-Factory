#!/usr/bin/env python3
"""Loop 3 driver for the 2026-10-15 agentic_ai evergreen draft.

`skills/claude_humanizer.md` §7: humanize_loop3's own socket timeout (240s) aborts a
~1,000-word rewrite on its first attempt. This driver keeps every other behaviour of
`humanize_one.py` (frontmatter normalisation, the accessibility retry loop, the source /
marker / length checks) and only widens the socket timeout, so the attempt trail prints.
"""
import functools
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import humanizer_tools as ht  # noqa: E402

_orig_call = ht.call_gemini
ht.call_gemini = functools.partial(_orig_call, timeout=480)

draft = "context/drafts/2026-10-15_agent-loop-bound-not-a-budget_draft.md"
sys.argv = ["humanize_one.py", draft]
code = compile((ROOT / "scripts" / "humanize_one.py").read_text(), "humanize_one.py", "exec")
exec(code, {"__name__": "__main__"})
