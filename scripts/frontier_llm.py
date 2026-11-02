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
import urllib.error
import urllib.request

TEXT_MODEL = "deepseek-v4-pro"
VISION_MODEL = "deepseek-flash"
BASE_URL = "https://api.deepseek.com/v1/chat/completions"
MAX_TOKENS = 20000
VISION_MAX_TOKENS = 1024

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
         temperature: float = 0.7, timeout: int = 240, json_mode: bool = False) -> str:
    """One frontier completion. `json_mode` asks for a bare JSON object."""
    body = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": temperature,
        "stream": False,
    }
    if json_mode:
        body["response_format"] = {"type": "json_object"}
    return _text(_post(body, timeout))


def vision(image: bytes, prompt: str, *, model: str = VISION_MODEL,
           max_tokens: int = VISION_MAX_TOKENS, temperature: float = 0.1,
           timeout: int = 120, json_mode: bool = False) -> str:
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
    return _text(_post(body, timeout))
