#!/usr/bin/env python3
"""What the accessibility floor actually measures.

The floor is about the article's prose. Three machine-written blocks sit in every published artifact
and none of them is prose the writer chose: the frontmatter, the `## Sources` list, and the
`## Related reading` block the persistence pass injects after Loop 3 already measured and passed the
body. Counting the last one put 21 of 70 published artifacts under the floor while the per-run gate
said PASS — the desk's own floor has to be reproducible from the artifact.
"""
from __future__ import annotations

import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import check_accessibility as ca  # noqa: E402

ARTICLE = """---
title: A Short Headline
primary_keyword: tco
---

## The setup

The plan is simple. You size the bank for the loads. Then you test it.

## Related reading

- [A Very Long And Complicated Internal Link Title](https://example.com/some-long-slug/) — more on Stuff
- [Another Considerably Overwritten Editorial Link Title](https://example.com/other-slug/) — more on Stuff

## Sources

1. A source that is long and lexically dense with considerable terminology.
"""


def test_machine_written_blocks_are_not_counted_as_prose(tmp_path):
    path = tmp_path / "a.md"
    path.write_text(ARTICLE)
    body = ca.body_of(str(path))
    assert "A Short Headline" not in body          # frontmatter
    assert "Related reading" not in body           # injected after the rewrite
    assert "A Very Long And Complicated" not in body
    assert "Sources" not in body
    assert "The plan is simple." in body           # the prose survives


def test_the_prose_alone_is_what_passes_or_fails(tmp_path):
    path = tmp_path / "a.md"
    path.write_text(ARTICLE)
    assert ca.measure(str(path))["flesch"] > 60     # short sentences, short words


def test_dense_prose_still_fails(tmp_path):
    """The floor must still bite: excluding the blocks cannot rescue a genuinely dense body."""
    dense = ARTICLE.replace(
        "The plan is simple. You size the bank for the loads. Then you test it.",
        "Notwithstanding the considerable methodological complexity inherent in contemporary "
        "battery-sizing methodologies, practitioners invariably underestimate the consequences "
        "of uninterrupted critical-load requirements during extended infrastructural outages.")
    path = tmp_path / "b.md"
    path.write_text(dense)
    assert ca.measure(str(path))["flesch"] < 50


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))
