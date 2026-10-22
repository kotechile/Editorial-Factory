#!/usr/bin/env python3
"""Loop 3 driver for the 2026-10-22 expat_cross_border_relocation evergreen draft
(`your-130000-cap-burns-the-credit`).

`skills/claude_humanizer.md` §7: a per-draft driver with a wide socket timeout, because the
frontier is a thinking model and the module's own 240s bound aborts long rewrites mid-generation.
Everything else in `humanize_one.py` (frontmatter normalisation, the accessibility retry loop,
the source / marker / length checks) stays exactly as written, so the attempt trail prints.
"""
import functools
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import humanizer_tools as ht  # noqa: E402

_orig_call = ht.call_gemini
ht.call_gemini = functools.partial(_orig_call, timeout=900)

draft = "context/drafts/2026-10-22_your-130000-cap-burns-the-credit_draft.md"
sys.argv = ["humanize_one.py", draft]
code = compile((ROOT / "scripts" / "humanize_one.py").read_text(), "humanize_one.py", "exec")
exec(code, {"__name__": "__main__"})
