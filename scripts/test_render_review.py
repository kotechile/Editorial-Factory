#!/usr/bin/env python3
"""The picture-desk check: does the finished RENDER match the article?

The mechanical gates (brief vocabulary, treatment rotation, byte hashes) prove the file, never the
picture. On 2026-10-24 the owner found headers that were not accurate to their articles, and nothing
in the pipeline could see it — `depicts_real_brand` is a judgement on the brief text, not on the
pixels. These cases pin the reviewer's verdict contract and the render gate it feeds.
"""
from __future__ import annotations

import io
import json
import pathlib
import random
from types import SimpleNamespace

import pytest
from PIL import Image, ImageDraw

from scripts import illustration_creator as ic

ARTICLE = """---
title: Roof Straps Do Not Stop Ember Rain
slug: roof-straps-do-not-stop-ember-rain
one_big_thing: A roof strap fixes the deck to the frame, not the vent to the deck, so an ember enters where the deck was never sealed.
vertical: resilient_home_assets
---

A hurricane strap holds the roof structure down. It does nothing about the ember that enters
through a ridge vent at 2 a.m.

## The strap is not the seal

The test is the vent, not the strap.

## Sources

[1] Example, https://example.com/vent
"""

PROMPT = ("Extreme close-up macro photograph of a weathered galvanised tie strap crossing a ridge "
          "tile on a roof deck, 100mm macro lens with a shallow focal plane, hard low-angle "
          "afternoon light raking from the left across the oxidised metal, bone white and slate "
          "grey palette, asymmetric composition with the strap off-centre.")

BRIEF = {
    "style_id": "editorial_macro", "rationale": "The story turns on one physical joint and the "
    "gap beside it, so a macro of the strap and the unsealed deck carries the thesis.",
    "cue": "an ember enters where the deck was never sealed",
    "subject": "a weathered tie strap crossing a ridge tile on a roof deck",
    "composition": "extreme asymmetry, the strap off-centre and low in frame",
    "model": "flux", "prompt": PROMPT, "negative_prompt": ic.DEFAULT_NEGATIVE,
    "aspect_ratio": "16:9", "resolution": "1K",
    "alt_text": "A weathered metal tie strap crossing a ridge tile on a timber roof deck in low sun.",
    "caption": "The strap holds the deck; the vent beside it is what lets the ember in.",
    "title": "Tie strap across a ridge tile",
    "credit": "Illustration: Editorial-Factory Intelligence Unit",
    "depicts_real_brand": False,
}


def make_brief() -> ic.Brief:
    return ic.validate_brief(BRIEF, ARTICLE, allowed=ic.allowed_styles([]))


def render(seed: int = 1, size=(1344, 768)) -> bytes:
    """A real JPEG: the reviewer downscales it before the call, so the bytes must open."""
    random.seed(seed)
    img = Image.new("RGB", size, (96 - seed, 82 + seed * 3 % 60, 66 + seed * 5 % 60))
    draw = ImageDraw.Draw(img)
    left = (size[0] // 4 + seed * 37) % (size[0] // 2)
    draw.rectangle([left, 0, left + size[0] // 6, size[1]], fill=(210 - seed * 9 % 50, 204, 190))
    draw.line([0, (size[1] // 3 + seed * 11) % size[1], size[0], (size[1] // 2 + seed * 13) % size[1]],
              fill=(40, 36, 32), width=12)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=88)
    return buf.getvalue()


def verdict(**over) -> str:
    payload = {"depicts": "a metal strap crossing a pale ridge tile on a dark timber deck",
               "legible_text": "", "on_topic": True, "confidence": 0.86,
               "reason": "the frame shows the strap and the deck it crosses"}
    payload.update(over)
    return json.dumps(payload)


# ─────────────────────────────────────────────────────────────────────────────
# the prompt the checker sees
# ─────────────────────────────────────────────────────────────────────────────

def test_the_checker_sees_the_article_and_the_frame_that_was_ordered():
    prompt = ic.review_prompt(ARTICLE, make_brief())
    assert "Roof Straps Do Not Stop Ember Rain" in prompt
    assert "an ember enters where the deck was never sealed" in prompt
    assert "a weathered tie strap crossing a ridge tile" in prompt
    assert "fail" in prompt.lower() or "fail a frame" in prompt.lower()


# ─────────────────────────────────────────────────────────────────────────────
# the verdict contract
# ─────────────────────────────────────────────────────────────────────────────

def test_an_on_topic_frame_with_no_lettering_passes():
    result = ic.review_render(render(), ARTICLE, make_brief(), vision=lambda *a, **k: verdict())
    assert result["ok"] is True and result["problems"] == []
    assert result["depicts"].startswith("a metal strap")


def test_a_frame_about_another_story_is_refused_with_the_checkers_words():
    result = ic.review_render(render(), ARTICLE, make_brief(), vision=lambda *a, **k: verdict(
        on_topic=False, depicts="a glass office tower at night",
        reason="a corporate skyline has nothing to do with roof vents"))
    assert result["ok"] is False
    assert "does not depict this article" in result["problems"][0]
    assert "glass office tower" in result["problems"][0]


@pytest.mark.parametrize("text", ["STRUCTURAL ROOFING CERTIFICATE", "2026", "KINETIC"])
def test_legible_lettering_in_the_render_is_a_defect(text):
    result = ic.review_render(render(), ARTICLE, make_brief(),
                              vision=lambda *a, **k: verdict(legible_text=text))
    assert result["ok"] is False
    assert "legible lettering" in result["problems"][0]


@pytest.mark.parametrize("text", ["", "none", "None.", "no text", "N/A"])
def test_the_checker_saying_there_is_no_text_is_not_a_defect(text):
    result = ic.review_render(render(), ARTICLE, make_brief(),
                              vision=lambda *a, **k: verdict(legible_text=text))
    assert result["ok"] is True


def test_a_checker_outage_does_not_block_the_publish_but_says_it_was_not_checked():
    def down(*a, **k):
        raise ic.IllustrationError("render review failed: HTTP 503 — overloaded")
    result = ic.review_render(render(), ARTICLE, make_brief(), vision=down)
    assert result["ok"] is True and result["skipped"] is True
    assert "not checked" in result["reason"]


# ─────────────────────────────────────────────────────────────────────────────
# the gate in ensure_illustration: a rejected picture re-commissions, never ships
# ─────────────────────────────────────────────────────────────────────────────

class StubClient:
    """Two renders: the first is wrong, the second is right (or both are wrong)."""

    def __init__(self, renders):
        self.renders = list(renders)
        self.calls = 0

    def generate(self, brief, *, notes=None, **kwargs):
        image = self.renders[min(self.calls, len(self.renders) - 1)]
        self.calls += 1
        return ic.Generation(image=image, ext="jpg", content_type="image/jpeg",
                             task_id=f"task{self.calls}", credits=1.0, cost_ms=10,
                             source_url="https://example.test/render.jpg", request={})


def director(*answers):
    """An LLM that returns the given briefs in order (a re-commission is a new call)."""
    queue = list(answers)

    def call(prompt, **kwargs):
        return json.dumps(queue.pop(0) if queue else BRIEF)
    return call


def test_a_rejected_render_is_re_commissioned_and_the_second_one_ships(tmp_path):
    good = render(seed=2)
    client = StubClient([render(seed=1), good])
    calls = {"n": 0}

    def vision(image, prompt, **kwargs):
        calls["n"] += 1
        return verdict(on_topic=False, reason="wrong roof type") if calls["n"] == 1 else verdict()

    md, notes, meta = ic.ensure_illustration(
        ARTICLE, root=tmp_path, client=client, llm=director(BRIEF, BRIEF), vision=vision)

    assert client.calls == 2                     # the second reading was commissioned
    assert meta["review"]["ok"] is True
    assert any("rejected" in note for note in notes)
    assert (tmp_path / meta["local_path"]).is_file()


def test_two_rejected_renders_publish_without_a_header_rather_than_a_wrong_one(tmp_path):
    client = StubClient([render(seed=1), render(seed=3)])

    with pytest.raises(ic.IllustrationError, match="WITHOUT a header"):
        ic.ensure_illustration(ARTICLE, root=tmp_path, client=client,
                               llm=director(BRIEF, BRIEF),
                               vision=lambda *a, **k: verdict(on_topic=False,
                                                              reason="not this story"))
    assert client.calls == 2
    assert not (tmp_path / "context" / "assets" / "illustrations").exists()


def test_a_render_already_used_by_another_article_is_refused(tmp_path):
    """Uniqueness is checked on the pristine render, and a repeat is a templating tell."""
    from scripts import image_delivery as delivery
    shared = render(seed=4)
    other = tmp_path / "context" / "assets" / "illustrations" / "someone-else"
    other.mkdir(parents=True)
    (other / "featured.base.jpg").write_bytes(delivery.normalize(shared).blob)
    (other / "featured.json").write_text(json.dumps({"slug": "someone-else"}))

    client = StubClient([shared, render(seed=9)])
    md, notes, meta = ic.ensure_illustration(ARTICLE, root=tmp_path, client=client,
                                             llm=director(BRIEF, BRIEF),
                                             vision=lambda *a, **k: verdict())
    assert client.calls == 2
    assert any("already runs on 'someone-else'" in note for note in notes)
