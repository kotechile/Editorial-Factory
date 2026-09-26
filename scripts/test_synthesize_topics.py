#!/usr/bin/env python3
"""
scripts/test_synthesize_topics.py — regression suite for the pairing helper.

Run directly (`python3 scripts/test_synthesize_topics.py`) or via `scripts/verify.sh` §8.

The cases encode the defects the helper was rewritten to remove, so that they cannot come back:
constant gate-clearing scores, single-token substring collisions across domains (`carrier`,
`port`), canned theses stamped onto unrelated signals, and fabricated demo citations.
"""

import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import synthesize_topics as st  # noqa: E402

FIXTURES = HERE / "fixtures"
CANNED_HEADLINES = [
    "The Uninsurable Suburb",
    "Would Lower Frontier Model Prices Drive",
    "Kill Open-Loop Autonomous Agents",
    "The Power Wall Tipping Point",
    "The Working Capital Paradox",
    "Digital Nomad Tax Trap",
    "Subsidies Actually Lower Homeowner Bills",
]
FABRICATED_DEMO_STRINGS = [
    "68% of enterprise",
    "github.blog/news-insights/enterprise-software-report-2026",
    "pricing-trends",
]


def run(argv):
    """Invoke main() in-process and capture stdout."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(io.StringIO()):
        code = st.main(argv)
    return code, buf.getvalue()


def json_pairs(fixture, vertical, extra=()):
    code, out = run(["--signals", str(FIXTURES / fixture), "--vertical", vertical,
                     "--format", "json", *extra])
    assert code == 0, f"helper exited {code}"
    return json.loads(out)["pairs"]


def signals(fixture):
    return st.parse_signals_markdown((FIXTURES / fixture).read_text(encoding="utf-8"))


class TokensAndMatching(unittest.TestCase):
    def test_word_boundary_prevents_substring_collisions(self):
        port = st._token_pattern("port")
        self.assertIsNone(port.search("san pedro bay ports"))
        self.assertIsNone(port.search("support"))
        self.assertIsNotNone(port.search("port of long beach"))
        carrier = st._token_pattern("carrier")
        self.assertIsNotNone(carrier.search("ltl carrier-fit now material"))
        self.assertIsNone(carrier.search("carriers and safety groups"))

    def test_pattern_is_scoped_to_registry_verticals(self):
        leg_a = {"title": "Insurer premium spike", "claim": "insurance premium up 29%",
                 "angle": "underwriting", "url": "https://a.example/x", "id": "1",
                 "date": "2026-09-01", "intensity": "80"}
        leg_b = {"title": "Roof hardening codes", "claim": "roof hardening discount 16%",
                 "angle": "building code", "url": "https://b.example/y", "id": "2",
                 "date": "2026-09-02", "intensity": "80"}
        self.assertIsNotNone(st.match_pattern(leg_a, leg_b, "resilient_home_assets"))
        self.assertIsNone(st.match_pattern(leg_a, leg_b, "supply_chain"))

    def test_weak_tokens_never_form_a_match(self):
        leg_a = {"title": "API cost pressure", "claim": "cost and price moves", "angle": "cost",
                 "url": "https://a.example/x", "id": "1", "date": "2026-09-01", "intensity": "80"}
        leg_b = {"title": "SaaS price review", "claim": "platform budget", "angle": "price",
                 "url": "https://b.example/y", "id": "2", "date": "2026-09-02", "intensity": "80"}
        self.assertIsNone(st.match_pattern(leg_a, leg_b, "agentic_ai"))


class FixtureCases(unittest.TestCase):
    def test_positive_home_pair(self):
        pairs = json_pairs("synthesis_positive_home_signals.md", "resilient_home_assets")
        self.assertEqual(len(pairs), 1, pairs)
        pair = pairs[0]
        self.assertEqual(pair["pattern_id"], "insurance_withdrawal_x_asset_resilience")
        self.assertEqual(pair["signals"], ["1", "2"])
        self.assertTrue(all(st.is_https(u) for u in pair["anchor_urls"]))
        self.assertLessEqual(pair["emergence_heuristic"], 1.0)
        self.assertGreater(pair["emergence_heuristic"], 0.0)

    def test_positive_chain_pair(self):
        pairs = json_pairs("synthesis_positive_chain_signals.md", "supply_chain")
        self.assertTrue(pairs, "expected at least one chain pair")
        self.assertIn("freight_chokepoint_x_nearshoring", {p["pattern_id"] for p in pairs})
        self.assertIn(["1", "3"], [p["signals"] for p in pairs])

    def test_negative_carrier_scope(self):
        self.assertEqual(json_pairs("synthesis_negative_carrier_scope_signals.md", "supply_chain"), [])

    def test_negative_port_boundary(self):
        self.assertEqual(json_pairs("synthesis_negative_port_boundary_signals.md",
                                    "last_mile_routing_fleet_carbon"), [])

    def test_negative_weak_token_rows_are_not_citable(self):
        rows = signals("synthesis_negative_weak_token_signals.md")
        self.assertFalse(any(st.is_https(r["url"]) for r in rows),
                         "fixture rows must stay non-https — that is part of the case")
        self.assertEqual(json_pairs("synthesis_negative_weak_token_signals.md",
                                    "expat_cross_border_relocation"), [])

    def test_heuristic_is_content_derived_not_constant(self):
        home = json_pairs("synthesis_positive_home_signals.md", "resilient_home_assets")[0]
        chain = json_pairs("synthesis_positive_chain_signals.md", "supply_chain")[0]
        self.assertNotEqual(home["emergence_heuristic"], chain["emergence_heuristic"])


class Gates(unittest.TestCase):
    def test_window_override_rejects_everything_out_of_window(self):
        self.assertEqual(json_pairs("synthesis_positive_home_signals.md", "resilient_home_assets",
                                    extra=("--window-start", "2026-11-01",
                                           "--window-end", "2026-12-01")), [])

    def test_leg_outside_window_kills_the_pair(self):
        self.assertEqual(json_pairs("synthesis_positive_home_signals.md", "resilient_home_assets",
                                    extra=("--window-start", "2026-09-20",
                                           "--window-end", "2026-09-25")), [])

    def test_intensity_floor_is_enforced(self):
        body = ("# Signals: agentic_ai — 2026-09-20\n\n**Window:** 2026-08-21 → 2026-09-20\n\n"
                "| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |\n"
                "|---|--------|-----------|------|--------------|-------|-----------|\n"
                "| 1 | Frontier token pricing reset | https://a.example/x | 2026-09-10 | per-token rate card moved | unit economics | 55 |\n"
                "| 2 | Team moves agent loops in-house | https://b.example/y | 2026-09-11 | in-house developer platform | self-hosted | 88 |\n")
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "2026-09-20_agentic_ai_signals.md"
            path.write_text(body, encoding="utf-8")
            code, out = run(["--signals", str(path), "--format", "json", "--show-rejected"])
            self.assertEqual(code, 0)
            payload = json.loads(out)
            self.assertEqual(payload["pairs"], [])
            self.assertTrue(any("intensity<60" in r["reason"] for r in payload["rejected"]), out)

    def test_no_output_ever_carries_a_gate_score_or_canned_headline(self):
        for fixture, vertical in [("synthesis_positive_home_signals.md", "resilient_home_assets"),
                                  ("synthesis_positive_chain_signals.md", "supply_chain"),
                                  ("synthesis_negative_carrier_scope_signals.md", "supply_chain"),
                                  ("synthesis_negative_port_boundary_signals.md", "last_mile_routing_fleet_carbon"),
                                  ("synthesis_negative_weak_token_signals.md", "expat_cross_border_relocation")]:
            code, out = run(["--signals", str(FIXTURES / fixture), "--vertical", vertical])
            self.assertEqual(code, 0)
            self.assertNotIn("Composite", out)
            for headline in CANNED_HEADLINES:
                self.assertNotIn(headline, out)

    def test_demo_is_grounded_in_a_committed_source(self):
        code, out = run(["--demo"])
        self.assertEqual(code, 0)
        self.assertIn("kqed.org", out)
        for fabricated in FABRICATED_DEMO_STRINGS:
            self.assertNotIn(fabricated, out)

    def test_write_guard_protects_judge_artifacts_and_drafts(self):
        self.assertIsNotNone(st.validate_out_path(Path("/tmp/x_angle_brief.md")))
        self.assertIsNotNone(st.validate_out_path(Path("/tmp/x_verified_brief.md")))
        self.assertIsNotNone(st.validate_out_path(st.REPO_ROOT / "context" / "drafts" / "a.md"))
        with tempfile.TemporaryDirectory() as tmp:
            fresh = Path(tmp) / "pairs.md"
            self.assertIsNone(st.validate_out_path(fresh))
            fresh.write_text("x", encoding="utf-8")
            self.assertIsNotNone(st.validate_out_path(fresh))
            self.assertIsNone(st.validate_out_path(fresh, force=True))

    def test_build_checks_are_clean(self):
        self.assertEqual(st.check_fixtures(), [])
        self.assertEqual(st.check_briefs(), [])

    def test_json_contract(self):
        code, out = run(["--signals", str(FIXTURES / "synthesis_positive_home_signals.md"),
                         "--vertical", "resilient_home_assets", "--format", "json",
                         "--show-rejected"])
        payload = json.loads(out)
        for key in ("vertical", "persona", "window", "rows", "pairs", "rejected", "note"):
            self.assertIn(key, payload)
        self.assertIn("advisory", payload["note"].lower())
        self.assertNotIn("Composite", out)

    def test_unknown_vertical_warns_rather_than_faking_a_persona(self):
        code, out = run(["--signals", str(FIXTURES / "synthesis_positive_home_signals.md"),
                         "--vertical", "not_a_registry_vertical", "--format", "json"])
        self.assertEqual(code, 0)
        payload = json.loads(out)
        self.assertIsNone(payload["persona"])
        self.assertEqual(payload["pairs"], [])  # no scoping → no pattern may fire


if __name__ == "__main__":
    unittest.main(verbosity=2)
