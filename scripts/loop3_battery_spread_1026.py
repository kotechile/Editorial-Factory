#!/usr/bin/env python3
"""Loop 3 driver for the 2026-10-26 home_equity_tco evergreen draft (your-battery-payback-0-or-38).

`skills/claude_humanizer.md` §7: humanize_loop3/humanize_one's own 240 s socket timeout aborts a long
rewrite on its first attempt, and a cron "foreground" call over the tool cap is promoted to a
background process. This driver keeps every other behaviour of `humanize_one.py` (frontmatter
normalisation, the accessibility retry loop, the source / marker / length checks) and only widens the
socket timeout, so the per-attempt trail prints to the log.
"""
import functools
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import humanizer_tools as ht  # noqa: E402

_orig_call = ht.call_gemini
ht.call_gemini = functools.partial(_orig_call, timeout=900)

draft = "context/drafts/2026-10-26_your-battery-payback-0-or-38_draft.md"
sys.argv = ["humanize_one.py", draft]
code = compile((ROOT / "scripts" / "humanize_one.py").read_text(), "humanize_one.py", "exec")
exec(code, {"__name__": "__main__"})
