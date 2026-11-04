"""Per-draft Loop 3 driver for 2026-11-04 / gpu_hardware / 18x-lpddr-isnt-18tbs.

Article reviewer (whole-document rewrite + review_audit gate) with a transport-level retry:
the first call runs the frontier as configured; if it truncates or returns no text (the
2026-11-04 reasoning-exhaustion class), the same prompt is retried with thinking disabled.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_llm  # noqa: E402
import article_reviewer as ar  # noqa: E402

DRAFT = ROOT / "context/drafts/2026-11-04_18x-lpddr-isnt-18tbs_draft.md"
BRIEF = ROOT / "context/recon_proposals/2026-11-04_gpu_hardware_verified_brief.md"


def call_model(prompt, *, model=ar.MODEL, timeout=ar.TIMEOUT,
               max_tokens=ar.MAX_TOKENS, temperature=0.7):
    try:
        return frontier_llm.chat(prompt, model=model, max_tokens=max_tokens,
                                 temperature=temperature, timeout=timeout)
    except Exception as exc:  # truncation / empty answer -> one no-thinking retry
        print(f"[driver] first call failed ({exc}); retrying with thinking disabled", flush=True)
        return frontier_llm.chat(prompt, model=model, max_tokens=max_tokens,
                                 temperature=temperature, timeout=timeout, thinking=False)


ar.call_model = call_model

result = ar.review(DRAFT, brief_path=BRIEF, attempts=2, keep_attempts=True)
print("RESULT", {k: v for k, v in result.items() if k not in ("text",)}, flush=True)
print("WROTE", DRAFT.with_name(DRAFT.name.replace("_draft.md", "_final.md")), flush=True)
