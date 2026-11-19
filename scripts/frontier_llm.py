"""The editorial factory's frontier transport — OpenRouter, GLM, or DeepSeek.

One place that knows how to reach the frontier, so the Loop 3 humanizer, the article reviewer
and the art director all move together:

Supported providers:
  * OpenRouter (OPENROUTER_API_KEY) — route to GLM 5.3, Claude 3.5 Sonnet, GPT-4o, etc.
  * GLM / Zhipu AI (GLM_API_KEY / ZHIPU_API_KEY) — direct BigModel API
  * DeepSeek (DEEPSEEK_API_KEY) — default direct DeepSeek v4 pro

Provider override: FRONTIER_PROVIDER (openrouter | glm | deepseek)
Model override:    FRONTIER_MODEL / TEXT_MODEL
Endpoint override: FRONTIER_BASE_URL
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

# Default fallback values for backward-compatibility with imports
DEFAULT_DEEPSEEK_TEXT = "deepseek-v4-pro"
DEFAULT_DEEPSEEK_VISION = "deepseek-flash"
DEFAULT_DEEPSEEK_URL = "https://api.deepseek.com/v1/chat/completions"

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_OPENROUTER_TEXT = "z-hipu/glm-4-plus"
DEFAULT_OPENROUTER_VISION = "google/gemini-flash-1.5"

GLM_URL = "https://open.bigmodel.cn/api/paas/v4/chat/completions"
DEFAULT_GLM_TEXT = "glm-4-plus"
DEFAULT_GLM_VISION = "glm-4v-plus"

TEXT_MODEL = os.environ.get("FRONTIER_MODEL") or os.environ.get("TEXT_MODEL") or DEFAULT_DEEPSEEK_TEXT
VISION_MODEL = os.environ.get("VISION_MODEL") or DEFAULT_DEEPSEEK_VISION
BASE_URL = os.environ.get("FRONTIER_BASE_URL") or DEFAULT_DEEPSEEK_URL
MAX_TOKENS = 32000
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
    str(ROOT / ".env"),
    os.path.expanduser("~/.hermes/profiles/stylist/.env"),
    os.path.expanduser("~/.hermes/profiles/simon/.env"),
    os.path.expanduser("~/.hermes/.env"),
    os.path.expanduser("~/.editorial-factory.env"),
    "/root/.hermes/profiles/stylist/.env",
    "/root/.hermes/profiles/simon/.env",
    "/root/.hermes/.env",
    "/root/editorial-factory/.env",
)


class FrontierError(RuntimeError):
    """The frontier could not be reached or returned nothing usable."""


def _read_env_val(key_name: str) -> str:
    val = os.environ.get(key_name) or ""
    if val:
        return val.strip()
    for envf in _ENV_FILES:
        p = pathlib.Path(envf)
        if not p.exists():
            continue
        try:
            for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
                if line.startswith(f"{key_name}="):
                    val = line.split("=", 1)[1].strip().strip('"').strip("'")
                    if val:
                        return val
        except Exception:
            continue
    return ""


def active_provider() -> str:
    """Return active provider: 'openrouter', 'glm', or 'deepseek'."""
    prov = (os.environ.get("FRONTIER_PROVIDER") or "").strip().lower()
    if prov:
        return prov
    if _read_env_val("OPENROUTER_API_KEY") or _read_env_val("OPENROUTER_KEY"):
        return "openrouter"
    if _read_env_val("GLM_API_KEY") or _read_env_val("ZHIPU_API_KEY"):
        return "glm"
    if _read_env_val("DEEPSEEK_API_KEY"):
        return "deepseek"
    return "openrouter" if _read_env_val("OPENROUTER_API_KEY") else "deepseek"


def key(provider: str | None = None) -> str:
    """Resolve API key for active provider (or explicit provider)."""
    prov = provider or active_provider()
    if prov == "openrouter":
        val = (_read_env_val("OPENROUTER_API_KEY") or _read_env_val("OPENROUTER_KEY")
               or _read_env_val("FRONTIER_API_KEY"))
        if val:
            return val
        raise FrontierError("OPENROUTER_API_KEY not found (env or .env files)")
    elif prov == "glm":
        val = (_read_env_val("GLM_API_KEY") or _read_env_val("ZHIPU_API_KEY")
               or _read_env_val("FRONTIER_API_KEY"))
        if val:
            return val
        raise FrontierError("GLM_API_KEY / ZHIPU_API_KEY not found (env or .env files)")
    else:  # deepseek
        val = _read_env_val("DEEPSEEK_API_KEY") or _read_env_val("FRONTIER_API_KEY")
        if val:
            return val
        raise FrontierError("DEEPSEEK_API_KEY not found (env or a profile .env)")


def endpoint(provider: str | None = None) -> str:
    custom = os.environ.get("FRONTIER_BASE_URL")
    if custom:
        return custom
    prov = provider or active_provider()
    if prov == "openrouter":
        return os.environ.get("OPENROUTER_BASE_URL") or OPENROUTER_URL
    elif prov == "glm":
        return os.environ.get("GLM_BASE_URL") or GLM_URL
    return os.environ.get("DEEPSEEK_BASE_URL") or BASE_URL


def default_text_model(provider: str | None = None) -> str:
    custom = (os.environ.get("REVIEW_MODEL")
              or os.environ.get("EDITORIAL_MODEL")
              or os.environ.get("OPENROUTER_MODEL")
              or os.environ.get("FRONTIER_MODEL")
              or os.environ.get("TEXT_MODEL"))
    if custom:
        return custom
    prov = provider or active_provider()
    if prov == "openrouter":
        return DEFAULT_OPENROUTER_TEXT
    elif prov == "glm":
        return os.environ.get("GLM_MODEL") or DEFAULT_GLM_TEXT
    return DEFAULT_DEEPSEEK_TEXT


def default_vision_model(provider: str | None = None) -> str:
    custom = os.environ.get("VISION_MODEL")
    if custom:
        return custom
    prov = provider or active_provider()
    if prov == "openrouter":
        return os.environ.get("OPENROUTER_VISION_MODEL") or DEFAULT_OPENROUTER_VISION
    elif prov == "glm":
        return os.environ.get("GLM_VISION_MODEL") or DEFAULT_GLM_VISION
    return DEFAULT_DEEPSEEK_VISION


def _request_headers(provider: str | None = None) -> dict[str, str]:
    prov = provider or active_provider()
    h = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + key(prov),
    }
    if prov == "openrouter":
        h["HTTP-Referer"] = os.environ.get("OPENROUTER_REFERER", "https://editorial-factory.local")
        h["X-Title"] = os.environ.get("OPENROUTER_TITLE", "editorial-factory")
    return h


def _post(body: dict, timeout: int, provider: str | None = None) -> dict:
    prov = provider or active_provider()
    url = endpoint(prov)
    headers = _request_headers(prov)
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode(),
        headers=headers,
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as exc:
        raise FrontierError(f"frontier ({prov}) call failed: HTTP {exc.code} — "
                            f"{exc.read().decode('utf-8', 'replace')[:300]}") from None
    except Exception as exc:  # noqa: BLE001 — surface, never swallow
        raise FrontierError(f"frontier ({prov}) call failed: {exc}") from None


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


def chat(prompt: str, *, model: str = "", max_tokens: int = MAX_TOKENS,
         temperature: float = 0.7, timeout: int = 240, json_mode: bool = False,
         thinking: bool | None = None, stage: str = "", provider: str | None = None,
         reasoning_effort: str | None = None) -> str:
    """One frontier completion. `json_mode` asks for a bare JSON object.

    `thinking=False` turns the model's reasoning pass off on DeepSeek. The reasoning tokens are
    billed inside `max_tokens` and are unbounded in practice: a full Loop 3 rewrite prompt
    (humanizer RULES + a ~1,200-word draft) burned 8,000, then 20,000, then 32,000 completion
    tokens entirely on reasoning and returned an empty `content` with `finish_reason=length`
    (2026-11-04). The same call with `thinking={"type": "disabled"}` answers normally.
    Note: `thinking` is only passed to DeepSeek endpoints (OpenRouter/GLM reject unknown fields).

    `reasoning_effort`: For GLM-5.3 / OpenAI reasoning models routed through OpenRouter, Novita,
    or DeepInfra, accepts 'low', 'medium', or 'high' (default configurable via REASONING_EFFORT).
    """
    prov = provider or active_provider()
    chosen_model = model or default_text_model(prov)
    body = {
        "model": chosen_model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": temperature,
        "stream": False,
    }
    effort = reasoning_effort or os.environ.get("REASONING_EFFORT")
    if effort:
        body["reasoning_effort"] = effort
        if prov == "openrouter":
            body["reasoning"] = {"effort": effort}
    if thinking is False and prov == "deepseek":
        body["thinking"] = {"type": "disabled"}
    if json_mode:
        body["response_format"] = {"type": "json_object"}
    payload = _post(body, timeout, provider=prov)
    _log_usage(payload, chosen_model, "chat", stage)
    return _text(payload)


def vision(image: bytes, prompt: str, *, model: str = "",
           max_tokens: int = VISION_MAX_TOKENS, temperature: float = 0.1,
           timeout: int = 120, json_mode: bool = False, stage: str = "",
           provider: str | None = None) -> str:
    """One frontier completion with the picture inline (downscaled: the checker needs the subject,
    not the grain)."""
    from PIL import Image

    prov = provider or active_provider()
    chosen_model = model or default_vision_model(prov)

    img = Image.open(io.BytesIO(image)).convert("RGB")
    if img.width > 1200:
        img = img.resize((1200, round(img.height * 1200 / img.width)), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=85)
    data_uri = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    body = {
        "model": chosen_model,
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
    payload = _post(body, timeout, provider=prov)
    _log_usage(payload, chosen_model, "vision", stage)
    return _text(payload)
