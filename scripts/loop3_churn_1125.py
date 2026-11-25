#!/usr/bin/env python3
"""Loop 3 driver for the 2026-11-25 warehouse evergreen draft (turnover-cost thesis)."""
import functools
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import humanizer_tools as ht  # noqa: E402

_orig_call = ht.call_gemini
ht.call_gemini = functools.partial(_orig_call, timeout=480)

draft = "context/drafts/2026-11-25_your-labor-line-replaces-40-percent_draft.md"
sys.argv = ["humanize_one.py", draft]
code = compile((ROOT / "scripts" / "humanize_one.py").read_text(), "humanize_one.py", "exec")
exec(code, {"__name__": "__main__"})
