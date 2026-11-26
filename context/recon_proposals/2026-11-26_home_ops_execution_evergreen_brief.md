# Evergreen Brief: home_ops_execution — 2026-11-26
**Archetype:** evergreen
**Vertical:** home_ops_execution
**Persona:** pro_homeowner
**Decision the reader is facing:** When the contractor hands over this year's renewal sheet, whether to sign the annual HVAC maintenance plan, what price is fair for it, and which clauses make it worth more than booking tune-ups yourself.
**Durability:** The plan-vs-à-la-carte math is structural: a service agreement is prepaid labor with a discount kicker, and that structure does not move. Figures are dated — the price bands are as of January 30, 2026 (Fixr's stated update date) and retrieved 2026-11-26 from This Old House; technician wage data is median wages (2025) from O*NET. In 12 months the bands may drift a few percent; the decision rule (what the plan must include, what the repair discount must be worth) does not.
**De-dup:** `2026-10-29_11-degrees-kills-the-compressor-quote` is this vertical's nearest prior artifact — that piece argues the diagnostic delta-T you take yourself before calling a tech; it never prices the ongoing service contract. Cross-corpus grep for maintenance/service contracts (`grep -rli "maintenance plan\|service contract" published/`) hits only `2026-11-11_your-71-margin-is-your-exit-bill`, `2026-10-28_100000-totes-skip-the-cost`, `2026-10-31_your-mower-pays-back-in-24-years-or-09` and `2026-10-06_demurrage-invoice-30-day-clocks` — none of them HVAC plan-purchase economics. The retainage/lien/bond/permit evergreens argue contract law, not service-plan pricing.
**Thesis:** An annual HVAC maintenance agreement is prepaid labor priced between two verified anchors — a one-off tune-up running $75–$200 (This Old House) against a $275 national average visit (Fixr) — so the plan only pays if what you are prepaying (two clean visits, priority scheduling, waived fees, a repair discount) is worth more than the ~$75–$150 the agreement costs, and the article's job is to give the reader the arithmetic and the clause checklist to decide.

**Lead:** The vertical's own `primary_angles` ("annual preventative maintenance vendor contracts") and founder-voice §3 pillar "The Enterprise Home Ops Playbook" (standardized, scheduled vendor service contracts that eliminate emergency failures); customer-truth Anecdote 3 (the $7,500 compressor quote) supplies the failure the plan is supposed to prevent. GSC striking-distance file for this vertical returned 0 candidates, so demand data is not a lead — and per §2 it never vetoes.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Fixr — How Much Does HVAC Maintenance Cost? [2026 Data] (updated January 30, 2026) | https://www.fixr.com/costs/hvac-maintenance | 2026-11-26 | $275 is the average cost of a one-off HVAC maintenance visit, with most services ranging $150–$350 | measured |
| 2 | This Old House — How Much Does HVAC Maintenance Cost? | https://www.thisoldhouse.com/heating-cooling/reviews/hvac-maintenance-cost | 2026-11-26 | $75–$200 flat fee for an annual HVAC tune-up visit (page: "costs homeowners an average of $75–$200") | measured |
| 3 | This Old House — same page, agreement-plan pricing | https://www.thisoldhouse.com/heating-cooling/reviews/hvac-maintenance-cost | 2026-11-26 | $75–$150 — annual maintenance agreement plans' average cost (bi-annual $150–$300); same page: a home warranty needs proof of regular maintenance before covering HVAC repair, and agreements carry priority scheduling, reduced fees, repair discounts | measured |
| 4 | Fixr — HVAC maintenance cost table (same page, task pricing) | https://www.fixr.com/costs/hvac-maintenance | 2026-11-26 | $100–$350 for a standalone coil cleaning, $10–$50 per filter, $75–$150 hourly labor — labor is nearly all of the maintenance bill | measured |
| 5 | O*NET OnLine — 49-9021.00 Heating and Air Conditioning Mechanics and Installers | https://www.onetonline.org/link/summary/49-9021.00 | 2026-11-26 | $29.33 hourly, $61,010 annual — median wages (2025) for HVAC service technicians | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Whether to sign the contractor's annual HVAC maintenance plan — price anchors, clause checklist, payback math | 9 | 9 | 9 | 8 | 8.9 | **winner** |
| Sewer-scope cadence as part of an annual PM contract | 8 | 9 | 5 | 7 | 7.4 | dropped — no fetchable primary cost anchor; scope-price pages 403/wall the verifier |
| Refrigerant-phaseout service-contract riders (R-410A) | 6 | 4 | 6 | 7 | 5.7 | dropped — value expires with the phase-out clock; a news-track topic, not evergreen |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=5 fetched=5 sources=3 hosts=3 decision="sha1:96d40822e8" dedup="matched a prior artifact: 2026-10-29_11-degrees-kills-the-co" window_days=180 checked_at=2026-11-26T19:04:29+00:00 -->
<!-- evergreen-gate:end -->
