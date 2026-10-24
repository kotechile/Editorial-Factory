#!/usr/bin/env python3
"""Brief the scene, never the concept — and keep the scene in the site's own world.

The owner's example is the fixture: a wall-mounted home battery in a garage is a photograph; "a home
battery for energy independence, futuristic, high-tech, glowing, 8k, cinematic, masterpiece" is a
category wrapped in quality claims, and it comes back as plastic.
"""
from __future__ import annotations

import pytest

from scripts import scene_brief as scene

GOOD_HOME = (
    "A wall-mounted home battery in a garage, its status ring lit, beside a coiled charging cable on "
    "a concrete floor. Editorial photograph, 35mm, soft directional daylight from the left, warm "
    "neutral palette of bone white, graphite and deep pine green, shallow depth of field, fine film "
    "grain, no people, no faces, no hands, no text, no lettering, no signage, no logos."
)
BAD_CATEGORY = ("A home battery for energy independence, futuristic, high-tech, glowing, 8k, "
                "cinematic, masterpiece.")


def test_the_owners_good_brief_passes_untouched():
    """The example from the brief must clear the gate as written, or the gate is wrong."""
    assert scene.problems(GOOD_HOME, site="wellroost.com",
                          subject="a wall-mounted home battery in a garage") == []


def test_the_owners_bad_brief_is_refused_for_every_reason_it_deserves():
    problems = " | ".join(scene.problems(BAD_CATEGORY, site="wellroost.com",
                                         subject="a home battery"))
    assert "quality" in problems          # 8k / futuristic / masterpiece
    assert "place" in problems            # no garage, no kitchen, no wall
    assert "light" in problems
    assert "palette" in problems


def test_a_quality_claim_alone_is_enough_to_refuse():
    prompt = ("A wall-mounted home battery in a garage, light from the left, bone white and "
              "graphite palette, photorealistic 8k masterpiece.")
    assert any("quality" in p for p in scene.problems(prompt, site="wellroost.com",
                                                      subject="a home battery in a garage"))


def test_a_prompt_set_in_another_sites_world_is_refused():
    prompt = ("A wall-mounted home battery in a data hall, light from the left, bone white and "
              "graphite palette, 35mm, fine grain.")
    problems = " | ".join(scene.problems(prompt, site="wellroost.com",
                                         subject="a wall-mounted home battery"))
    assert "data hall" in problems and "not wellroost.com's world" in problems


def test_the_same_prompt_is_fine_on_the_site_whose_world_it_is():
    prompt = ("A GPU blade in a rack row, light from above, graphite and copper palette, 85mm, "
              "fine film grain.")
    assert scene.problems(prompt, site="aichieve.net", subject="a GPU blade in a rack row") == []


def test_the_light_must_have_a_direction_or_a_quality():
    prompt = ("A wall-mounted home battery in a garage, bone white and graphite palette, 35mm, "
              "fine grain.")
    assert any("light" in p for p in scene.problems(prompt, site="wellroost.com",
                                                    subject="a home battery in a garage"))


def test_the_palette_must_be_named():
    prompt = ("A wall-mounted home battery in a garage, soft daylight from the left, 35mm, "
              "fine grain.")
    assert any("palette" in p for p in scene.problems(prompt, site="wellroost.com",
                                                      subject="a home battery in a garage"))


def test_the_prompt_must_show_the_articles_own_object():
    prompt = ("A tidy garage, soft daylight from the left, bone white and graphite palette, 35mm, "
              "fine grain.")
    assert any("article's own object" in p for p in scene.problems(
        prompt, site="wellroost.com", subject="a wall-mounted home battery"))


@pytest.mark.parametrize("vertical,site", [
    ("resilient_home_assets", "wellroost.com"),
    ("home_infrastructure_lifecycle_tco", "wellroost.com"),
    ("gpu_hardware", "aichieve.net"),
    ("career_velocity_equity_engineering", "giniloh.com"),
])
def test_a_vertical_maps_to_its_reader_site(vertical, site):
    assert scene.site_for_vertical(vertical) == site


def test_every_site_world_is_a_real_world():
    for site, world in scene.SITES.items():
        assert len(world["places"]) >= 8, site
        assert len(world["palette"]) >= 5, site
        assert world["label"], site


def test_the_directors_brief_names_the_sites_own_places():
    block = scene.guidance("wellroost.com")
    assert "wellroost.com" in block and "garage" in block and "kitchen" in block
    assert "data hall" not in block.split("never:")[0]
