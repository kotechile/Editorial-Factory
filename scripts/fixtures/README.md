# Sync fixtures

Each file here is a signals-file-format fixture for `scripts/synthesize_topics.py`, and every row
(including every URL) is copied verbatim from a committed `context/recon_proposals/*_signals.md`
run. `python3 scripts/synthesize_topics.py --check-fixtures` (wired into `scripts/verify.sh` §8)
fails the build if a fixture cites a source that the committed recon files do not contain — the
point being that the helper, its demo and its tests may never introduce a citation of their own.

| Fixture | Case | Expected |
|---|---|---|
| `synthesis_positive_home_signals.md` | FAIR Plan rate hike ⨂ hardening discounts | 1+ pair, `insurance_withdrawal_x_asset_resilience` |
| `synthesis_positive_chain_signals.md` | rail consolidation ⨂ reshoring capex | 1+ pair, `freight_chokepoint_x_nearshoring` |
| `synthesis_negative_carrier_scope_signals.md` | ocean `carrier` ⨂ claims `mitigation` | 0 pairs (vertical scoping) |
| `synthesis_negative_port_boundary_signals.md` | "ports" ⨂ `supplier`, `multi-carrier` | 0 pairs (word boundary) |
| `synthesis_negative_weak_token_signals.md` | only `cost` shared; bare-domain URLs | 0 pairs (weak tokens + no https) |
