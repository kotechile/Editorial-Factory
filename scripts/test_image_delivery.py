#!/usr/bin/env python3
"""The delivery standard, pinned: aspect, width, weight, format, filename, alt text, uniqueness.

Each case here is a rule the owner set on 2026-10-24 because the corpus broke it in production:
161 of 182 staged images were under 1600px wide, 89 were over 400KB, 78 were PNG, 16 were baseline
JPEG — and nothing in the pipeline looked at any of it.
"""
from __future__ import annotations

import io
import json
import pathlib
import random

import pytest
from PIL import Image, ImageDraw, ImageFilter

from scripts import image_delivery as delivery


def _photo(size=(1344, 768), seed=1, noise: int = 0) -> Image.Image:
    """A structured image with photographic local correlation (flat colour compresses to nothing;
    per-pixel random noise is incompressible and no real render looks like it). `noise` raises the
    entropy so a case can exercise the weight ladder."""
    random.seed(seed)
    w, h = size
    base = Image.new("RGB", (max(1, w // 8), max(1, h // 8)))
    pixels = base.load()
    for y in range(base.height):
        for x in range(base.width):
            value = (x * 3 + y * 2) % 200
            pixels[x, y] = (value + 30, (value * 2) % 180, 90)
    img = base.resize(size, Image.BICUBIC)
    draw = ImageDraw.Draw(img)
    for _ in range(14):
        x, y = random.randint(0, w - 1), random.randint(0, h - 1)
        radius = random.randint(40, 220)
        draw.ellipse([x - radius, y - radius, x + radius, y + radius],
                     fill=(random.randint(20, 240), random.randint(20, 240),
                           random.randint(20, 240)))
    img = img.filter(ImageFilter.GaussianBlur(1.2))
    if noise:
        grain = Image.effect_noise(size, noise).convert("RGB")
        img = Image.blend(img, grain, 0.18)
    return img


def _blob(img: Image.Image, fmt="JPEG", quality=95, **kwargs) -> bytes:
    buf = io.BytesIO()
    img.save(buf, format=fmt, quality=quality, **kwargs)
    return buf.getvalue()


# ─────────────────────────────────────────────────────────────────────────────
# the master
# ─────────────────────────────────────────────────────────────────────────────

def test_a_render_is_converted_to_the_exact_delivery_master():
    out = delivery.normalize(_blob(_photo()))
    assert (out.width, out.height) == (2400, 1350)
    assert out.aspect == pytest.approx(16 / 9, abs=1e-4)
    assert out.bytes <= delivery.MAX_BYTES
    with Image.open(io.BytesIO(out.blob)) as check:
        assert check.format == "JPEG"
        assert check.info.get("progressive")
        assert check.size == (2400, 1350)


def test_a_square_render_is_centre_cropped_not_squashed():
    out = delivery.normalize(_blob(_photo((1024, 1024))))
    assert (out.width, out.height) == (2400, 1350)


def test_a_wide_render_loses_the_edges_not_the_geometry():
    out = delivery.normalize(_blob(_photo((1600, 700))))
    with Image.open(io.BytesIO(out.blob)) as check:
        assert check.size == (2400, 1350)


def test_the_weight_budget_steps_quality_down_instead_of_shipping_over_it():
    busy = _blob(_photo((2400, 1350), seed=7, noise=30))
    assert len(busy) > delivery.MAX_BYTES          # the render itself is over budget
    out = delivery.normalize(busy)
    assert out.bytes <= delivery.MAX_BYTES
    assert out.quality < delivery.QUALITIES[0]


def test_a_source_too_small_to_reach_the_floor_is_refused_not_blown_up():
    with pytest.raises(delivery.DeliveryError, match="cannot reach"):
        delivery.normalize(_blob(_photo((900, 506))))


# ─────────────────────────────────────────────────────────────────────────────
# the measurable rules
# ─────────────────────────────────────────────────────────────────────────────

def test_a_conforming_file_has_no_problems(tmp_path):
    path = tmp_path / "ok.jpg"
    path.write_bytes(delivery.normalize(_blob(_photo())).blob)
    assert delivery.check_file(path) == []


def test_each_rule_failure_is_named(tmp_path):
    png = tmp_path / "shot.png"
    png.write_bytes(_blob(_photo(), fmt="PNG"))
    problems = " ".join(delivery.check_file(png))
    assert "not JPEG" in problems

    narrow = tmp_path / "narrow.jpg"
    narrow.write_bytes(_blob(_photo((1200, 675))))
    assert "1600px floor" in " ".join(delivery.check_file(narrow))

    wide = tmp_path / "wide.jpg"
    wide.write_bytes(_blob(_photo((1600, 1000))))
    assert "aspect" in " ".join(delivery.check_file(wide))

    baseline = tmp_path / "baseline.jpg"
    baseline.write_bytes(_blob(_photo((2400, 1350)), progressive=False))
    assert "progressive" in " ".join(delivery.check_file(baseline))


def test_the_weight_rule_is_a_hard_ceiling(tmp_path):
    heavy = tmp_path / "heavy.jpg"
    heavy.write_bytes(_blob(_photo((2400, 1350), seed=11, noise=30), quality=100))
    assert heavy.stat().st_size > delivery.MAX_BYTES
    assert "budget" in " ".join(delivery.check_file(heavy))


# ─────────────────────────────────────────────────────────────────────────────
# alt text
# ─────────────────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("alt", [
    "A weathered roof bracket fixed to a ridge tile.",
    "An unbranded electric van charging on a wet suburban driveway at dusk, warm window light "
    "behind it and a dark street beyond.",
])
def test_a_good_alt_text_passes(alt):
    assert delivery.alt_problems(alt, "Roof bracket", "The article headline") == []


def test_alt_text_under_the_floor_is_refused():
    problems = delivery.alt_problems("A roof bracket.", "x", "")
    assert problems and "40-140" in problems[0]


def test_alt_text_over_the_ceiling_is_refused():
    problems = delivery.alt_problems("a" * 141, "x", "")
    assert problems and "40-140" in problems[0]


@pytest.mark.parametrize("alt,title", [
    ("A weathered roof bracket fixed to a ridge tile.",
     "A weathered roof bracket fixed to a ridge tile."),
    ("A weathered roof bracket fixed to a ridge tile",
     "A weathered roof bracket, fixed to a ridge tile!"),
])
def test_alt_text_may_not_restate_the_title(alt, title):
    assert any("repeats the title" in p for p in delivery.alt_problems(alt, title))


def test_alt_text_may_not_restate_the_ARTICLE_headline():
    alt = "Why your 49 percent discount is not all roof"
    assert any("repeats the title" in p
               for p in delivery.alt_problems(alt, "media label", alt.title()))


# ─────────────────────────────────────────────────────────────────────────────
# filename
# ─────────────────────────────────────────────────────────────────────────────

@pytest.mark.parametrize("slug,expected", [
    ("your-49-discount-isnt-all-roof", "your-49-discount-isnt-all-roof-featured.jpg"),
    ("Your 49 Discount", "your-49-discount-featured.jpg"),
    ("Weird__Slug!!", "weird-slug-featured.jpg"),
])
def test_the_media_filename_is_lowercase_slug_featured_jpg(slug, expected):
    assert delivery.media_filename(slug) == expected


# ─────────────────────────────────────────────────────────────────────────────
# uniqueness
# ─────────────────────────────────────────────────────────────────────────────

def test_the_same_picture_re_encoded_is_a_duplicate():
    original = _photo(seed=3)
    a = _blob(original, quality=95)
    b = _blob(original.resize((1600, 915)), quality=60)
    assert delivery.hamming(delivery.dhash(a), delivery.dhash(b)) <= delivery.DUPLICATE_HAMMING


def test_different_pictures_are_not_duplicates():
    a = delivery.dhash(_photo(seed=1))
    b = delivery.dhash(_photo(seed=200))
    assert delivery.hamming(a, b) > delivery.DUPLICATE_HAMMING


def test_a_repeat_across_two_articles_is_caught_by_the_corpus(tmp_path):
    root = tmp_path
    directory = root / "context" / "assets" / "illustrations" / "first-article"
    directory.mkdir(parents=True)
    render = delivery.normalize(_blob(_photo(seed=5))).blob
    (directory / "featured.base.jpg").write_bytes(render)
    (directory / "featured.json").write_text(json.dumps({"slug": "first-article"}))

    again = _blob(Image.open(io.BytesIO(render)).resize((1600, 900)), quality=70)
    duplicate = delivery.find_duplicate(again, "second-article", root=root)
    assert duplicate and duplicate["slug"] == "first-article"

    fresh = _blob(_photo(seed=99))
    assert delivery.find_duplicate(fresh, "second-article", root=root) is None


def test_an_article_may_reuse_its_own_picture(tmp_path):
    root = tmp_path
    directory = root / "context" / "assets" / "illustrations" / "my-article"
    directory.mkdir(parents=True)
    render = delivery.normalize(_blob(_photo(seed=8))).blob
    (directory / "featured.base.jpg").write_bytes(render)
    (directory / "featured.json").write_text(json.dumps({"slug": "my-article"}))
    assert delivery.find_duplicate(render, "my-article", root=root) is None


# ─────────────────────────────────────────────────────────────────────────────
# the audit
# ─────────────────────────────────────────────────────────────────────────────

def test_the_audit_separates_legacy_assets_from_standard_breaches(tmp_path):
    root = tmp_path
    base = root / "context" / "assets" / "illustrations"

    legacy = base / "old-post"
    legacy.mkdir(parents=True)
    (legacy / "featured.png").write_bytes(_blob(_photo((1344, 768)), fmt="PNG"))
    (legacy / "featured.json").write_text(json.dumps(
        {"slug": "old-post", "alt_text": "An old header", "title": "Old"}))

    good = base / "new-post"
    good.mkdir(parents=True)
    (good / "featured.jpg").write_bytes(delivery.normalize(_blob(_photo(seed=21))).blob)
    (good / "featured.json").write_text(json.dumps(
        {"slug": "new-post", "delivery": {"standard": delivery.STANDARD_VERSION},
         "alt_text": "A weathered steel bracket bolted to a ridge tile in hard afternoon light",
         "title": "Ridge bracket"}))

    report = delivery.audit(root)
    slugs = {row["slug"]: row for row in report["problems"]}
    assert "old-post" in slugs and slugs["old-post"]["legacy"] is True
    assert "new-post" not in slugs
