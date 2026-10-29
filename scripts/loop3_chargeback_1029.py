#!/usr/bin/env python3
"""Loop 3 driver for the 2026-10-29 enterprise_ai_finops evergreen draft (chargeback).

`skills/claude_humanizer.md` §7: a ~1,000-word rewrite on the frontier needs a socket
timeout well above the module default (240s); this driver keeps `humanize_path.py`'s
behaviour (frontmatter normalisation, accessibility retry loop, source/marker/length
checks) and only widens the timeout, so the attempt trail prints.
"""
import functools
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import humanizer_tools as ht  # noqa: E402

_orig_call = ht.call_gemini
ht.call_gemini = functools.partial(_orig_call, timeout=900)

draft = "context/drafts/2026-10-29_your-chargeback-misses-40-of-the-bill_draft.md"
sys.argv = ["humanize_path.py", draft]
code = compile((ROOT / "scripts" / "humanize_path.py").read_text(), "humanize_path.py", "exec")
exec(code, {"__name__": "__main__"})
