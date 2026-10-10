# Evergreen Brief: supplier_risk_reshoring_decision — 2026-10-10
**Archetype:** evergreen
**Vertical:** supplier_risk_reshoring_decision
**Persona:** ops_leader
**Decision the reader is facing:** Whether to reshore/nearshore a component to "escape" its import duty — or first net out the drawback already recoverable (up to 99%) on whatever share of the output is exported or destroyed, before crediting the move with a duty saving it does not really create.
**Durability:** The mechanism is statutory, not cyclical: drawback's 99% refund cap and the export-or-destroy trigger sit in 19 U.S.C. 1313 and 19 CFR Part 190, and the statute has not changed the 99% figure since the TFTEA modernization that took effect in 2018. The only time-bound part of the argument is *which* duty programs are eligible as of October 2026 (Section 232 and some IEEPA duties are carved out while Section 301 is generally in), and that is stated as-of in the body so a reader can re-check it; the decision rule — net the recoverable duty out of the reshoring case before crediting the move with a saving — does not expire.
**De-dup:** 2026-10-03_total-landed-cost-china-vs-mexico and 2026-10-10_nearshoring-doesnt-move-the-trade-case (this vertical's two most recent published articles) and the earlier 2026-10-03_supplier_risk_reshoring_decision_evergreen_brief — all three treat duty as a *cost you pay* (a landed-cost comparison and a trade-case read). This is the opposite side of the same line item: a *recovery* you can claim, and the reason the duty line in a reshoring model is smaller than it looks. Different thesis, different evidence, no retread.
**Thesis:** A reshoring business case that credits the move with "escaping" import duty is overstating the saving — drawback refunds up to 99% of the duties, taxes and fees paid on any imported input that is later exported or destroyed, substitution lets a duty-paid import be matched to an export of the same 8-digit HTS subheading for up to five years, and the real duty exposure is only the domestic-consumption share; so the durable reasons to reshore are lead time, concentration risk and currency, not the tariff line.

**Lead:** From the vertical's own `primary_angles` (angle 1: "quantifying geopolitical tariff and lead-time risks of single-source offshore manufacturing vs nearshoring unit costs" and angle 2: "total landed cost tlc calculator factoring tariffs…"), `context/growth_os/founder-voice.md` §3 `supplier_risk_reshoring_decision` ("Total Landed Cost (TLC) Transparency" — duty and fees are a line the nearshoring model carries, never nets), and `context/growth_os/customer-truth.md` Anecdote 1 (a casting quoted at $18/unit that landed at $24.80) and Anecdote 6 (a mid-sized importer hit with a retroactive $1.2M duty bill after an HTS reclassification) — i.e. importers who model duty as an unavoidable cost. GSC striking-distance is a bonus signal only and the per-vertical export (`context/gsc_performance.json`, last synced 2026-09-08) holds no supplier-risk query with meaningful impressions, so the topic is sourced from the vertical's durable beat, not an invented idea.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | eCFR — 19 CFR Part 190 (Modernized Drawback), current as of 2026-10-10 | https://www.ecfr.gov/current/title-19/chapter-I/part-190 | 2026-10-10 | 99 percent — the amount of drawback allowable "will not exceed 99 percent of the amount of duties, taxes, and fees paid" on the imported merchandise, on export or destruction under CBP supervision | measured (regulation) |
| 2 | Cornell LII — 19 U.S.C. § 1313 (Drawback and refunds), current as of 2026-10-10 | https://www.law.cornell.edu/uscode/text/19/1313 | 2026-10-10 | 99 percent — the refund is "equal to 99 percent of the duties, taxes, and fees paid on the imported merchandise"; substitution drawback matches a duty-paid import to an exported/destroyed article of the same 8-digit HTS subheading within five years | measured (statute) |
| 3 | U.S. Customs and Border Protection — "Drawback" program page | https://www.cbp.gov/trade/programs-administration/entry-summary/drawback-overview | 2026-10-10 | 1313 — drawback is the refund of duties, certain internal revenue taxes and fees "collected upon the importation of goods and refunded when the merchandise is exported or destroyed"; authority is 19 U.S.C. 1313 / 19 CFR 190, and Section 301/201 duties are claimable (filer must report both the Chapter 99 and the 1–97 HTS numbers) | measured (agency) |
| 4 | Borderless — "Duty drawback in 2026: what you can (and can't) recover" (last reviewed June 2026) | https://borderless.us/blog/duty-drawback-2026 | 2026-10-10 | 232 — recovery is program-by-program: "Section 232 (steel/aluminum/copper) and certain IEEPA-based duties are generally excluded from drawback", so "up to 99%" is real but not universal | vendor claim |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Duty drawback as a set-off against the reshoring business case: net the 99% recoverable duty out before crediting the move with a saving | 9 | 9 | 9 | 9 | 9.0 | **winner** |
| Dual-sourcing overhead vs. risk: split POs and lose the volume tier, or stay single-source | 8 | 8 | 6 | 8 | 7.5 | dropped — the load-bearing discount-loss figure (5–10%) is the founder's own estimate; no fetchable measured primary |
| Disruption resilience matrix / 45-day cash survival curve | 8 | 7 | 5 | 7 | 6.9 | dropped — the survival-curve anchors are customer-truth anecdotes, not fetchable primaries; re-run when a measured disruption-cost dataset lands |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=4 fetched=4 sources=4 hosts=4 decision="sha1:f90f058e06" dedup="matched a prior artifact: 2026-10-03_total-landed-cost-china" window_days=180 checked_at=2026-10-10T18:03:34+00:00 -->
<!-- evergreen-gate:end -->
