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


def test_module_is_importable_from_the_repo_root():
    """The suite runs from the repo root; the module must not need a sys.path shim."""
    assert pathlib.Path(__file__).resolve().parent.parent.name == "editorial-factory"
