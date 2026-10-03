#!/usr/bin/env python3
"""
scripts/test_evergreen_gate.py — regression suite for the evergreen evidence floor.

Wired into `scripts/verify.sh`. The rules themselves are pinned by
`evergreen_gate.py --self-test` (offline, stubbed fetch — no network, no credits); this suite adds
the file-level contract that verify.sh depends on: where briefs are discovered, and that a brief
whose table no longer matches its marker reads as STALE rather than shipping.

Nothing here touches the network or the working tree (temp dirs only).
"""

import io
import contextlib
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import evergreen_gate as eg  # noqa: E402

REPO = HERE.parent


def sample_brief(rows=3, marker_rows=None):
    lines = [
        "# Evergreen Brief: home_ops_execution — 2026-10-08",
        "**Archetype:** evergreen",
        "**Vertical:** home_ops_execution",
        "**Persona:** pro_homeowner",
        "**Decision the reader is facing:** Whether to hold retainage on a remodel milestone or "
        "release it on a signed unconditional lien waiver.",
        "**Durability:** Figures are as of the 2026 statute book and do not expire; the caps are "
        "restated annually.",
        "**De-dup:** 2026-10-01_home_ops_execution_angle_brief (different thesis: code-cycle timing)",
        "**Thesis:** The retainage cap changes who carries the cash-flow risk on a residential "
        "remodel.",
        "",
        "| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |",
        "|---|---|---|---|---|---|",
    ]
    for i in range(1, rows + 1):
        lines.append(f"| {i} | source {i} | https://example{i}.org/page | 2026-10-08 | {i}00 "
                     f"| measured |")
    text = "\n".join(lines) + "\n"
    if marker_rows is not None:
        marker = eg.render_marker([{"url": f"https://example{i}.org/page", "verified": True}
                                   for i in range(1, marker_rows + 1)],
                                  "2026-10-08T00:00:00+00:00", "decision", "2026-10-01_brief")
        text = text + "\n## Gate result\n\n" + marker + "\n"
    return text


class RulesArePinned(unittest.TestCase):
    def test_the_gate_self_test_passes(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = eg.self_test()
        self.assertEqual(rc, 0, "the evergreen rules self-test failed:\n" + buf.getvalue())

    def test_the_floor_constants_are_what_the_skill_documents(self):
        # skills/evergreen_topics.md quotes these; a silent change would make the SOP a lie
        self.assertEqual(eg.MIN_SOURCES, 3)
        self.assertEqual(eg.MIN_HOSTS, 2)
        self.assertEqual(eg.DEDUP_WINDOW_DAYS, 180)


class Parsing(unittest.TestCase):
    def test_fields_and_rows_are_extracted(self):
        parsed = eg.parse_brief(sample_brief(rows=3))
        self.assertEqual(parsed["errors"], [])
        self.assertEqual(len(parsed["rows"]), 3)
        self.assertEqual(parsed["rows"][0]["url"], "https://example1.org/page")
        self.assertEqual(parsed["fields"]["Persona"], "pro_homeowner")

    def test_missing_fields_are_reported(self):
        parsed = eg.parse_brief(sample_brief(rows=3).replace("**Persona:** pro_homeowner\n", ""))
        self.assertTrue(any("Persona" in e for e in parsed["errors"]), parsed["errors"])

    def test_a_hosts_vary_helper(self):
        self.assertEqual(eg.host_of("https://www.example.com/a/b"), "example.com")


class MarkerFreshness(unittest.TestCase):
    def test_a_matching_marker_is_fresh(self):
        fresh, why = eg.marker_state(sample_brief(rows=3, marker_rows=3), 3)
        self.assertTrue(fresh, why)

    def test_an_edited_table_reads_as_stale(self):
        fresh, why = eg.marker_state(sample_brief(rows=3, marker_rows=3), 4)
        self.assertFalse(fresh)
        self.assertIn("stale", why)

    def test_a_brief_with_no_marker_is_not_seeded(self):
        fresh, why = eg.marker_state(sample_brief(rows=3), 3)
        self.assertFalse(fresh)
        self.assertEqual(why, "not seeded")


class ArtifactCheck(unittest.TestCase):
    """check_artifacts() is what verify.sh runs daily, so its discovery + verdicts are pinned."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self._saved = eg.REPO
        eg.REPO = Path(self._tmp.name)
        (eg.REPO / "context" / "recon_proposals").mkdir(parents=True)

    def tearDown(self):
        eg.REPO = self._saved
        self._tmp.cleanup()

    def _write(self, name, text):
        path = eg.REPO / "context" / "recon_proposals" / name
        path.write_text(text, encoding="utf-8")
        return path

    def test_no_briefs_is_a_pass(self):
        self.assertEqual(eg.check_artifacts(no_network=True), 0)

    def test_a_fresh_brief_passes(self):
        self._write("2026-10-08_home_ops_execution_evergreen_brief.md",
                    sample_brief(rows=3, marker_rows=3))
        self.assertEqual(eg.check_artifacts(no_network=True), 0)

    def test_a_stale_brief_fails(self):
        self._write("2026-10-08_home_ops_execution_evergreen_brief.md",
                    sample_brief(rows=4, marker_rows=3))
        self.assertEqual(eg.check_artifacts(no_network=True), 1)

    def test_an_unseeded_brief_fails(self):
        self._write("2026-10-08_home_ops_execution_evergreen_brief.md", sample_brief(rows=3))
        self.assertEqual(eg.check_artifacts(no_network=True), 1)

    def test_only_evergreen_briefs_are_discovered(self):
        # the news pipeline's artifacts must never be swept into this gate
        self._write("2026-10-08_home_ops_execution_signals.md", "not a brief")
        self._write("2026-10-08_home_ops_execution_angle_brief.md", "not a brief either")
        self.assertEqual(eg.check_artifacts(no_network=True), 0)

    def test_a_committed_brief_must_pass_the_floor_not_just_have_a_marker(self):
        # marker fresh, but only one evidence row -> the floor fails on the full run
        self._write("2026-10-08_home_ops_execution_evergreen_brief.md",
                    sample_brief(rows=1, marker_rows=1))

        def fetch(url):
            return {"status": "fetched", "http": "200", "text": "100 measured", "sha256": "x"}

        saved = eg.chd.fetch_source
        eg.chd.fetch_source = fetch
        try:
            self.assertEqual(eg.check_artifacts(no_network=False), 1)
        finally:
            eg.chd.fetch_source = saved


if __name__ == "__main__":
    unittest.main(verbosity=2)
