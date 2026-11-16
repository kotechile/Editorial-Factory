"""The editorial factory's frontier transport — DeepSeek (replaced Gemini 3.1 Pro, 2026-11-02).

One place that knows how to reach the frontier, so the Loop 3 humanizer, the article reviewer
and the art director all move together:

  * ``TEXT_MODEL = deepseek-v4-pro``   — the frontier rewrite / review / art-director brief
  * ``VISION_MODEL = deepseek-flash``  — the picture-desk checker (DeepSeek's vision-capable model;
                                          ``deepseek-v4-pro`` is text-only and returns empty content
                                          when handed an image)

DeepSeek reasons before it answers and bills those reasoning tokens inside ``max_tokens``, so the
budgets here are deliberately large (a full ~1,200-word rewrite needs > 8k with headroom).

Key resolution order: ``DEEPSEEK_API_KEY`` in the environment, then the profile .env files that
already hold the fleet's key. Resolved per call, never at import, so offline tests import cleanly.
"""
from __future__ import annotations

import base64
import io
import json
import os
import pathlib
import time
import urllib.error
import urllib.request

TEXT_MODEL = "deepseek-v4-pro"
VISION_MODEL = "deepseek-flash"
BASE_URL = "https://api.deepseek.com/v1/chat/completions"
MAX_TOKENS = 32000   # 20k truncated thinking-model rewrites outright (finish_reason=length)
VISION_MAX_TOKENS = 1024

# Every in-pipeline call is metered into context/cost_ledger.jsonl. Before this existed the desk
# could not see a single one of its own pro-tier calls: Hermes records session usage, not the
# subprocess calls a pipeline makes (article_reviewer, the art director, publish_gate's rewrite).
# Prices mirror the fleet's own estimator (see `scripts/cost_report.py`): a cache HIT is 50x
# cheaper than a miss, which is why the ledger records the two separately.
ROOT = pathlib.Path(__file__).resolve().parent.parent
LEDGER = ROOT / "context" / "cost_ledger.jsonl"
PRICE_IN_MISS = 0.15 / 1e6     # per token
PRICE_IN_HIT = 0.0030 / 1e6
PRICE_OUT = 0.60 / 1e6


def _log_usage(payload: dict, model: str, kind: str, stage: str = "") -> None:
    """Append one usage row to the cost ledger. Never raises: metering must not break a call."""
    try:
        u = payload.get("usage") or {}
        hit = int(u.get("prompt_cache_hit_tokens") or 0)
        miss = int(u.get("prompt_cache_miss_tokens") or 0)
        if not miss and u.get("prompt_tokens"):
            miss = max(0, int(u["prompt_tokens"]) - hit)
        out = int(u.get("completion_tokens") or 0)
        reasoning = int(((u.get("completion_tokens_details") or {}).get("reasoning_tokens")) or 0)
        row = {
            "ts": round(time.time(), 3),
            "stage": stage or os.environ.get("PIPELINE_STAGE", ""),
            "kind": kind,
            "model": model,
            "prompt": int(u.get("prompt_tokens") or 0),
            "hit": hit,
            "miss": miss,
            "out": out,
            "reasoning": reasoning,
            "usd": round(miss * PRICE_IN_MISS + hit * PRICE_IN_HIT + out * PRICE_OUT, 6),
        }
        LEDGER.parent.mkdir(parents=True, exist_ok=True)
        with open(LEDGER, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(row) + "\n")
    except Exception:                                        # noqa: BLE001 — metering is best-effort
        pass


_ENV_FILES = (
    "/root/.hermes/profiles/stylist/.env",
    "/root/.hermes/profiles/simon/.env",
    "/root/.hermes/.env",
    "/root/editorial-factory/.env",
)


class FrontierError(RuntimeError):
    """The frontier could not be reached or returned nothing usable."""


def key() -> str:
    """The DeepSeek API key: environment first, then the profile/repo .env files."""
    value = os.environ.get("DEEPSEEK_API_KEY") or ""
    if value:
        return value.strip()
    for envf in _ENV_FILES:
        p = pathlib.Path(envf)
        if not p.exists():
            continue
        for line in p.read_text().splitlines():
            if line.startswith("DEEPSEEK_API_KEY="):
                value = line.split("=", 1)[1].strip().strip('"').strip("'")
                if value:
                    return value
    raise FrontierError("DEEPSEEK_API_KEY not found (env or a profile .env)")


def _post(body: dict, timeout: int) -> dict:
    req = urllib.request.Request(
        BASE_URL,
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json",
                 "Authorization": "Bearer " + key()},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as exc:
        raise FrontierError(f"frontier call failed: HTTP {exc.code} — "
                            f"{exc.read().decode('utf-8', 'replace')[:300]}") from None
    except Exception as exc:  # noqa: BLE001 — surface, never swallow
        raise FrontierError(f"frontier call failed: {exc}") from None


def _text(payload: dict) -> str:
    choices = payload.get("choices") or []
    if not choices:
        raise FrontierError(f"frontier returned no choices: {json.dumps(payload)[:300]}")
    choice = choices[0]
    text = (choice.get("message") or {}).get("content") or ""
    text = text.strip()
    finish = choice.get("finish_reason")
    if not text:
        raise FrontierError(f"frontier returned no text (finish_reason={finish})")
    if finish == "length":
        raise FrontierError("frontier output truncated (finish_reason=length); raise max_tokens")
    return text


def chat(prompt: str, *, model: str = TEXT_MODEL, max_tokens: int = MAX_TOKENS,
         temperature: float = 0.7, timeout: int = 240, json_mode: bool = False,
         thinking: bool | None = None, stage: str = "") -> str:
    """One frontier completion. `json_mode` asks for a bare JSON object.

    `thinking=False` turns the model's reasoning pass off for this call. The reasoning tokens are
    billed inside `max_tokens` and are unbounded in practice: a full Loop 3 rewrite prompt
    (humanizer RULES + a ~1,200-word draft) burned 8,000, then 20,000, then 32,000 completion
    tokens entirely on reasoning and returned an empty `content` with `finish_reason=length`
    (2026-11-04). The same call with `thinking={"type": "disabled"}` answers normally, so a caller
    that needs the text back from a long structured prompt passes `thinking=False`.
    """
    body = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": temperature,
        "stream": False,
    }
    if thinking is False:
        body["thinking"] = {"type": "disabled"}
    if json_mode:
        body["response_format"] = {"type": "json_object"}
    payload = _post(body, timeout)
    _log_usage(payload, model, "chat", stage)
    return _text(payload)


def vision(image: bytes, prompt: str, *, model: str = VISION_MODEL,
           max_tokens: int = VISION_MAX_TOKENS, temperature: float = 0.1,
           timeout: int = 120, json_mode: bool = False, stage: str = "") -> str:
    """One frontier completion with the picture inline (downscaled: the checker needs the subject,
    not the grain)."""
    from PIL import Image

    img = Image.open(io.BytesIO(image)).convert("RGB")
    if img.width > 1200:
        img = img.resize((1200, round(img.height * 1200 / img.width)), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=85)
    data_uri = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    body = {
        "model": model,
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": data_uri}},
        ]}],
        "max_tokens": max_tokens,
        "temperature": temperature,
        "stream": False,
    }
    if json_mode:
        body["response_format"] = {"type": "json_object"}
    payload = _post(body, timeout)
    _log_usage(payload, model, "vision", stage)
    return _text(payload)
