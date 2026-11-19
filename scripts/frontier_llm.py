"""The editorial factory's model transport — OpenRouter, GLM 5.3 family (since 2026-11-19).

One place that knows how to reach every model tier, so the Loop 3 humanizer, the article
reviewer, the headline re-cut and the art director all move together:

  * ``TEXT_MODEL = z-ai/glm-5.3``        — FINAL REVIEW & REWRITE / ART DIRECTION (frontier).
                                            Pinned to Decart's fp4 endpoint (``decart/fp4``);
                                            text-only, so it never sees a picture.
  * ``FLASH_MODEL = z-ai/glm-5.3-flash`` — RADAR, VIRALITY JUDGE, FACT-CHECK, FIRST DRAFT,
                                            HEADLINE OPTIMIZATION, and the visual QA pass.
                                            Pinned to Relace's fp4 endpoint (``relace/fp4``);
                                            it is multimodal (text/image/video in), which is why
                                            it — not the text-only frontier — checks the artwork.
                                            (Specced as ``wafer/us`` 2026-11-19, moved to Relace
                                            the same day: Wafer answered 429 "temporarily
                                            rate-limited upstream" on ~8 of 10 real calls.)
  * ``VISION_MODEL`` is ``FLASH_MODEL`` under its historic name.

Routing is a hard pin, per the owner's 2026-11-19 spec: the request body carries
``provider: {only: [<endpoint tag>], allow_fallbacks: false}``. If the pinned endpoint is
unavailable the call fails loudly instead of silently landing on a reseller with different
quantization or pricing. GLM-5.3's reasoning pass bills inside ``max_tokens``; ``thinking=False``
asks OpenRouter to disable it for long structured rewrites.

Key resolution order: ``OPENROUTER_API_KEY`` in the environment, then the profile/repo .env
files that hold the fleet's key. Resolved per call, never at import, so offline tests import
cleanly.
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

TEXT_MODEL = os.environ.get("FRONTIER_MODEL") or "z-ai/glm-5.3"
FLASH_MODEL = os.environ.get("FRONTIER_FLASH_MODEL") or "z-ai/glm-5.3-flash"
VISION_MODEL = FLASH_MODEL
# One env override for the whole transport (a provider experiment must not need a code edit);
# unset = OpenRouter's chat-completions route, which is what the pins are written against.
BASE_URL = os.environ.get("FRONTIER_BASE_URL") or "https://openrouter.ai/api/v1/chat/completions"
MAX_TOKENS = 32000   # GLM reasons before it answers and bills that inside max_tokens
VISION_MAX_TOKENS = 1024

# Endpoint pins (OpenRouter endpoint tags, as published by /api/v1/models/<id>/endpoints).
PROVIDER_PINS = {
    TEXT_MODEL: "decart/fp4",
    FLASH_MODEL: "relace/fp4",
}
# Relace serves the flash model for text but not for image input — OpenRouter narrows the pool to
# vision-capable endpoints and answers 404 when the pinned one is absent (probed 2026-11-19).
# The picture desk therefore pins separately, to an fp4 endpoint that does serve images.
VISION_PIN = "open-inference/fp4"

# Every in-pipeline call is metered into context/cost_ledger.jsonl. Before this existed the desk
# could not see a single one of its own frontier calls: Hermes records session usage, not the
# subprocess calls a pipeline makes (article_reviewer, the art director, publish_gate's rewrite).
# Prices are per model, per token, as listed by OpenRouter for the pinned endpoint.
ROOT = pathlib.Path(__file__).resolve().parent.parent
LEDGER = ROOT / "context" / "cost_ledger.jsonl"
PRICES = {
    TEXT_MODEL:  {"in": 0.56 / 1e6,    "cached": 0.10 / 1e6,    "out": 1.81 / 1e6},
    FLASH_MODEL: {"in": 0.0399 / 1e6,  "cached": 0.03 / 1e6,    "out": 0.0784 / 1e6},
}
# Back-compat for scripts/cost_report.py, which imports these three names. They describe the
# cheap tier — the volume tier — and every ledger row records its own model's price anyway.
PRICE_IN_MISS = PRICES[FLASH_MODEL]["in"]
PRICE_IN_HIT = PRICES[FLASH_MODEL]["cached"]
PRICE_OUT = PRICES[FLASH_MODEL]["out"]


def price_for(model: str) -> dict:
    """Per-token prices for *model*; unknown ids are priced as the cheap tier."""
    return PRICES.get(model, PRICES[FLASH_MODEL])


def _log_usage(payload: dict, model: str, kind: str, stage: str = "") -> None:
    """Append one usage row to the cost ledger. Never raises: metering must not break a call."""
    try:
        u = payload.get("usage") or {}
        details = u.get("prompt_tokens_details") or {}
        hit = int(details.get("cached_tokens") or u.get("prompt_cache_hit_tokens") or 0)
        miss = int(u.get("prompt_cache_miss_tokens") or 0)
        if not miss and u.get("prompt_tokens"):
            miss = max(0, int(u["prompt_tokens"]) - hit)
        out = int(u.get("completion_tokens") or 0)
        reasoning = int(((u.get("completion_tokens_details") or {}).get("reasoning_tokens")) or 0)
        price = price_for(model)
        row = {
            "ts": round(time.time(), 3),
            "stage": stage or os.environ.get("PIPELINE_STAGE", ""),
            "kind": kind,
            "model": model,
            "provider": payload.get("provider", ""),
            "prompt": int(u.get("prompt_tokens") or 0),
            "hit": hit,
            "miss": miss,
            "out": out,
            "reasoning": reasoning,
            "usd": round(miss * price["in"] + hit * price["cached"] + out * price["out"], 6),
        }
        LEDGER.parent.mkdir(parents=True, exist_ok=True)
        with open(LEDGER, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(row) + "\n")
    except Exception:                                        # noqa: BLE001 — metering is best-effort
        pass


_ENV_FILES = (
    "/root/.hermes/.env",
    "/root/.hermes/profiles/stylist/.env",
    "/root/.hermes/profiles/simon/.env",
    "/root/editorial-factory/.env",
)


class FrontierError(RuntimeError):
    """The model endpoint could not be reached or returned nothing usable."""


def key() -> str:
    """The OpenRouter API key: environment first, then the profile/repo .env files."""
    value = os.environ.get("OPENROUTER_API_KEY") or ""
    if value:
        return value.strip()
    for envf in _ENV_FILES:
        p = pathlib.Path(envf)
        if not p.exists():
            continue
        for line in p.read_text().splitlines():
            if line.startswith("OPENROUTER_API_KEY="):
                value = line.split("=", 1)[1].strip().strip('"').strip("'")
                if value:
                    return value
    raise FrontierError("OPENROUTER_API_KEY not found (env or a profile .env)")


def _provider_body(model: str, kind: str = "chat") -> dict | None:
    """The OpenRouter routing object: hard-pin the model's endpoint, no silent fallback."""
    tag = VISION_PIN if kind == "vision" and model == VISION_MODEL else PROVIDER_PINS.get(model)
    if not tag:
        return None
    return {"only": [tag], "allow_fallbacks": False}


def _post(body: dict, timeout: int, attempts: int = 4) -> dict:
    """POST with a bounded retry on the failures the pinned endpoints actually raise.

    OpenRouter answers a throttled upstream endpoint with HTTP 429 ("temporarily rate-limited
    upstream") — measured at ~4-of-5 on `wafer/us` during a burst on 2026-11-19 — and the
    pipeline has no supervisor to retry a failed stage. Retry 429/5xx and transport blips with
    backoff; anything else (400 mandatory-reasoning, 401, 404 pin) is a real defect and raises
    on the first attempt.
    """
    last = None
    for i in range(attempts):
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
            detail = exc.read().decode("utf-8", "replace")[:300]
            last = f"HTTP {exc.code} — {detail}"
            if exc.code not in (429, 500, 502, 503, 504) or i == attempts - 1:
                raise FrontierError(f"frontier call failed: {last}") from None
        except Exception as exc:  # noqa: BLE001 — surface, never swallow
            last = str(exc)
            if i == attempts - 1:
                raise FrontierError(f"frontier call failed: {last}") from None
        time.sleep(min(2 * (2 ** i), 20))
    raise FrontierError(f"frontier call failed: {last}")


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
    """One completion. `json_mode` asks for a bare JSON object.

    `thinking=False` asks for the cheapest reasoning pass the endpoint allows (OpenRouter
    ``reasoning: {effort: "low"}``). It cannot ask for NO reasoning: both pinned GLM-5.3
    endpoints answer ``400 Reasoning is mandatory for this endpoint and cannot be disabled``,
    so "off" is not a state this model family has (probed 2026-11-19). Low effort still keeps
    the pass small enough that a long structured rewrite fits the completion ceiling, which is
    the property the DeepSeek-era `thinking: disabled` bought.
    """
    body = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": temperature,
        "stream": False,
    }
    if thinking is False:
        body["reasoning"] = {"effort": "low"}
    if json_mode:
        body["response_format"] = {"type": "json_object"}
    routing = _provider_body(model)
    if routing:
        body["provider"] = routing
    payload = _post(body, timeout)
    _log_usage(payload, model, "chat", stage)
    return _text(payload)


def vision(image: bytes, prompt: str, *, model: str = VISION_MODEL,
           max_tokens: int = VISION_MAX_TOKENS, temperature: float = 0.1,
           timeout: int = 120, json_mode: bool = False, stage: str = "") -> str:
    """One completion with the picture inline (downscaled: the checker needs the subject,
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
    routing = _provider_body(model, kind="vision")
    if routing:
        body["provider"] = routing
    payload = _post(body, timeout)
    _log_usage(payload, model, "vision", stage)
    return _text(payload)
