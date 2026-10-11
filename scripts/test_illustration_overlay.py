#!/usr/bin/env python3
"""Head casing rules for the reader-facing alt/caption.

The header copy comes back uppercased ('SPACEX STAGGERED LOCKUP'), so title-casing it is where
brand and product names get mangled into something the article never wrote ('Spacex', 'Iphone').
These pin the three inputs that decide a token's case: the article's own spelling, the acronym
list, and plain title case.
"""
from __future__ import annotations

import pathlib

import pytest

from scripts.illustration_overlay import sentence_case, source_spelling

ARTICLE = (
    "SpaceX workers get their next chance to sell today. The iPhone order book and the eBay "
    "listing are not the point; an AI model reading CPU/MCP traffic is. Next.js and macOS too."
)


@pytest.mark.parametrize("raw, expected", [
    ("SPACEX STAGGERED LOCKUP", "SpaceX Staggered Lockup"),
    ("THE IPHONE ORDER BOOK", "The iPhone Order Book"),
    ("EBAY LISTING RESET", "eBay Listing Reset"),
    ("THE ELECTRIC FREIGHT GAP", "The Electric Freight Gap"),
])
def test_article_spelling_wins(raw, expected):
    """A word the article spells with an internal capital keeps that spelling."""
    assert sentence_case(raw, ARTICLE) == expected


@pytest.mark.parametrize("raw, expected", [
    ("AI SPEND HITS A WALL", "AI Spend Hits A Wall"),
    ("GPU COST PER TOKEN", "GPU Cost Per Token"),
    ("KV CACHE REUSE", "KV Cache Reuse"),
])
def test_acronyms_stay_upper(raw, expected):
    assert sentence_case(raw, "no acronym is spelled here") == expected


def test_all_caps_non_acronym_is_title_cased():
    assert sentence_case("STAGGERED LOCKUP") == "Staggered Lockup"


def test_source_is_optional_and_never_needed():
    """No article text (a dry path, a caller that passes nothing) must not raise or mangle."""
    assert sentence_case("SPACEX LOCKUP") == "Spacex Lockup"
    assert sentence_case("SPACEX LOCKUP", "") == "Spacex Lockup"


@pytest.mark.parametrize("word, source", [
    ("lockup", ARTICLE),          # lowercase in the article: not a spelling to preserve
    ("spacx", ARTICLE),           # absent from the article
    ("", ARTICLE),                # nothing to look up
    ("IPO", ""),                  # no source at all
])
def test_source_spelling_declines(word, source):
    assert source_spelling(word, source) is None


def test_source_spelling_finds_the_canonical_form():
    assert source_spelling("spacex", ARTICLE) == "SpaceX"
    assert source_spelling("macos", ARTICLE) == "macOS"


@pytest.mark.parametrize("raw, expected", [
    ("UP-NS RAIL MERGER ADVANCES", "UP-NS Rail Merger Advances"),   # a hyphenated initialism the
    ("THE AI-COST MANDATE", "The AI-Cost Mandate"),                  # director already set right
])
def test_hyphenated_initialisms_keep_their_caps(raw, expected):
    """`.title()` turned 'UP-NS' into 'Up-Ns' — a name neither the article nor the ticker uses."""
    assert sentence_case(raw) == expected


def test_long_hyphenated_words_are_still_title_cased():
    assert sentence_case("STATE-OF-THE-ART RIG") == "State-Of-The-Art Rig"


def test_anchor_can_be_forced_and_validates():
    from PIL import Image
    from scripts.illustration_overlay import plan
    img = Image.new("RGB", (1000, 500), "white")
    auto = plan(img)
    forced = plan(img, "bottom-right")
    assert auto["anchor"] == "top-left" and not auto.get("forced")
    assert forced["anchor"] == "bottom-right" and forced["forced"] is True
    assert forced["x"] > auto["x"] and forced["y"] > auto["y"]
    with pytest.raises(ValueError):
        plan(img, "middle")


# --- placement against the subject -------------------------------------------------------------------
#
# The defect these pin: the old probe scored edge energy, so a SMOOTH subject — the document on a desk,
# the slab of metal — looked like the emptiest region in the frame and the type was laid on top of it.
# These frames are built the way that failure appeared in the corpus.

COPY = {"kicker": "RESHORING MATH // DUTY REFUNDS", "title": "DUTY DRAWBACK MATH",
        "hook": "Why unrecovered duty refunds skew reshoring math"}


def _ground_with_a_document():
    """A bright document on a dark textured desk, the real failing frame.

    The document sits over the block's default origin (top-left, inset): that is where the desk's
    design puts the type, and where the old edge-energy probe put it too — the smooth document scored
    as the *emptiest* region in the frame while the desk's grain scored as busy.
    """
    import random
    from PIL import Image, ImageDraw
    img = Image.new("RGB", (1344, 768), (58, 46, 38))
    d = ImageDraw.Draw(img)
    rnd = random.Random(7)
    for _ in range(6000):                       # grain: edge energy the old probe punished
        x, y = rnd.randrange(1344), rnd.randrange(768)
        g = rnd.randint(20, 40)
        d.point((x, y), fill=(58 + g, 46 + g, 38 + g))
    d.rectangle([0, 0, 900, 500], fill=(238, 234, 226))         # the document, smooth and bright
    return img


def _layout_of(img):
    from PIL import ImageDraw
    from scripts.illustration_overlay import _layout, SAFE_W
    pad = int(img.size[0] * 0.045)
    column = int(img.size[0] * SAFE_W) - pad * 2
    spans, ink, total = _layout(ImageDraw.Draw(img), COPY, img.size[1], column)
    return ink, (column + pad, total), pad


def test_the_subject_map_ranks_the_smooth_subject_over_the_grainy_ground():
    """The inversion that shipped the defect: bright document vs dark desk."""
    from scripts.illustration_overlay import _subject_map
    img = _ground_with_a_document()
    smap = _subject_map(img)
    sh, sw = smap.shape
    doc = smap[int(120 / 768 * sh):int(400 / 768 * sh), int(150 / 1344 * sw):int(800 / 1344 * sw)]
    desk = smap[int(600 / 768 * sh):int(740 / 768 * sh), int(200 / 1344 * sw):int(1200 / 1344 * sw)]
    assert doc.mean() > 0.6, doc.mean()          # the document is subject
    assert desk.mean() < 0.15, desk.mean()       # the grain is not


def test_type_is_placed_off_the_subject_not_on_it():
    from scripts.illustration_overlay import plan, _subject_map, _spot_cost
    img = _ground_with_a_document()
    ink, box, pad = _layout_of(img)
    smap = _subject_map(img)
    default = (int(img.size[0] * 0.02) + pad, int(img.size[1] * 0.02) + int(img.size[1] * 0.035))
    old_cost = _spot_cost(smap, ink, img.size, default, box[0], box[1], pad)[0]
    p = plan(img, None, rects=ink, box=box, pad=pad)
    assert old_cost > 0.5, old_cost                  # the design's own spot is on the document
    assert p["subject"] < 0.15, p                    # and the chosen spot is not
    assert p["moved"] is True
    assert p["y"] > 450 or p["x"] > 900, p           # clear of the document, not merely less bad


def test_blank_frame_keeps_the_design_default_and_does_not_drift():
    from PIL import Image
    from scripts.illustration_overlay import plan
    img = Image.new("RGB", (1344, 768), "white")
    ink, box, pad = _layout_of(img)
    p = plan(img, None, rects=ink, box=box, pad=pad)
    assert p["moved"] is False and p["subject"] < 0.05, p
    assert (p["x"], p["y"]) == (pad, int(768 * 0.055))     # the design's own gutter, unchanged


def test_a_nearly_empty_frame_keeps_the_design_inset():
    """Every cost within noise of zero: the block must not drift for a gain no eye can see."""
    import random
    from PIL import Image, ImageDraw
    from scripts.illustration_overlay import plan
    img = Image.new("RGB", (1344, 768), (58, 46, 38))
    d = ImageDraw.Draw(img)
    rnd = random.Random(3)
    for _ in range(9000):                       # grain, no subject
        x, y = rnd.randrange(1344), rnd.randrange(768)
        g = rnd.randint(14, 34)
        d.point((x, y), fill=(58 + g, 46 + g, 38 + g))
    ink, box, pad = _layout_of(img)
    p = plan(img, None, rects=ink, box=box, pad=pad)
    assert p["moved"] is False, p
    assert (p["x"], p["y"]) == (pad, int(768 * 0.055)), p


def test_the_block_stays_inside_the_frame_at_every_anchor():
    from scripts.illustration_overlay import plan
    img = _ground_with_a_document()
    ink, box, pad = _layout_of(img)
    column = box[0] - pad
    for anchor in ("top-left", "top-right", "bottom-left", "bottom-right"):
        p = plan(img, anchor, rects=ink, box=box, pad=pad)
        assert p["forced"] is True and p["anchor"] == anchor
        # The feathered panel is what has to fit: it spans pad/2 either side of the type's column.
        assert p["x"] - pad // 2 >= 0 and p["x"] + column + pad // 2 <= img.size[0], p
        assert 0 <= p["y"] and p["y"] + box[1] <= img.size[1], p


def test_a_frame_with_no_free_space_reports_it_instead_of_pretending():
    """Every spot carries art: the block takes the freest one and says the render must be re-done."""
    from PIL import Image, ImageDraw
    from scripts.illustration_overlay import plan, SUBJECT_TIGHT
    img = Image.new("RGB", (1344, 768), (58, 46, 38))
    d = ImageDraw.Draw(img)
    d.rectangle([70, 70, 1290, 700], fill=(238, 234, 226))   # a bright subject filling the interior:
    ink, box, pad = _layout_of(img)                          # no block of this size can miss it
    p = plan(img, None, rects=ink, box=box, pad=pad)
    assert p["subject"] >= SUBJECT_TIGHT, p
    assert "re-commission" in p["note"]


def test_the_composite_records_where_the_type_landed(tmp_path):
    """The sidecar's own number: one article, end to end, no credits."""
    from scripts.illustration_overlay import composite
    img = _ground_with_a_document()
    src = tmp_path / "featured.png"
    img.save(src)
    out = tmp_path / "typed.png"
    place = composite(src, out, COPY)
    assert out.exists()
    assert place["size"] == img.size[:2]        # under 1920px: delivery size untouched
    assert place["ink_subject"] < 0.15, place
    assert {"subject", "ink_subject", "spike", "anchor"} <= set(place)
    assert place["block"][1] < img.size[1]      # the block is on the frame


def test_module_is_importable_from_the_repo_root():
    """The suite runs from the repo root; the module must not need a sys.path shim."""
    assert pathlib.Path(__file__).resolve().parent.parent.name == "editorial-factory"
