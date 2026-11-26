# Evergreen Brief: enterprise_ai_finops — 2026-11-26
**Archetype:** evergreen
**Vertical:** enterprise_ai_finops
**Persona:** enterprise_cai
**Decision the reader is facing:** The CIO runs 10+ GenAI proofs of concept a year and must decide, before renewal season, which pilots earn production compute budget — and which get killed on a written scorecard rather than on demo enthusiasm. The decision bites at every quarterly budget gate, when a pilot team asks for scale funding on the strength of a demo nobody has priced.
**Durability:** The abandonment arithmetic (95% of pilots delivering no measurable return; 42% of companies scrapping most initiatives) is a structural feature of how enterprises fund demos vs. production, and the graduation mechanics — a written scorecard with a dated payback threshold — do not expire. Figures are current as of the sources' own dates: the MIT NANDA finding as of the August 2025 report, the Census BTOS adoption figures as of the December 2025–May 2026 collection window, and the O*NET labor anchor as of the 2025 median-wage table.
**De-dup:** `2026-11-12_enterprise_ai_finops_evergreen_brief` is this vertical's nearest prior evergreen artifact and it argues context-length price tiers, not pilot graduation; `2026-11-05_enterprise_ai_finops_evergreen_brief` argued billable-unit definitions and `2026-10-29_enterprise_ai_finops_evergreen_brief` argued chargeback identifiers — none touches the PoC scorecard. Cross-vertical, `2026-11-17_your-approval-gate-kills-20` (enterprise_tech_leadership) argued meter-vs-gate funding control and `2026-11-03_your-ai-roi-28-rising-28-stalled` argued that ROI percentages are definitions; both named and read — this piece is checked-and-dropped against their mechanisms: it does not re-argue funding control or ROI definition, it supplies the graduation artifact (the scorecard's five questions and the 5× threshold) those pieces named as missing.
**Thesis:** Pilots do not die because the model fails the demo — 95% of GenAI implementations fall short while the models keep improving — they die because nothing written down decides whether a demo graduates, and the fix is a one-page scorecard with a dated payback threshold (5× labor-hour payback at measured wages) and a bias for deterministic high-throughput work over open-ended chat.

**Lead:** §2's field-friction lead — `context/growth_os/customer-truth.md` Anecdote 3 (the pilot-to-production graveyard: 11 PoCs in 12 months, $1.8M in licenses and consulting, one survivor, the 5× labor-hour payback scorecard) — crossed with `founder-voice.md` §3's "pilot-to-production graveyard and PoC audit scorecards" angle and the persona's CRW unit-economics want.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Fortune, "MIT report: 95% of generative AI pilots at companies are failing" (MIT NANDA, The GenAI Divide: State of AI in Business 2025) | https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo | 2026-11-26 | 95% of the companies in the MIT dataset fall short: "But for 95% of companies in the dataset, generative AI implementation is falling short," and "The 95% failure rate for enterprise AI solutions represents the clearest manifestation of the GenAI Divide" — while the models themselves are not the constraint ("Not the quality of the AI models, but the 'learning gap'"). | measured |
| 2 | U.S. Census Bureau, America Counts: "Large Firms With at Least 20 Employees Biggest AI Users" (BTOS) | https://www.census.gov/library/stories/2026/05/ai-use-businesses.html | 2026-11-26 | 17% to 20% is where overall U.S. business AI usage hovered from December 2025 to May 2026, with 20% to 23% expecting to use AI in the next six months — adoption is real and broad, so the bottleneck is not access but conversion to value. | measured |
| 3 | O*NET OnLine, Summary Report for Paralegals and Legal Assistants (23-2011.00) | https://www.onetonline.org/link/summary/23-2011.00 | 2026-11-26 | $30.24 hourly / $62,890 annual is the 2025 median paralegal wage — the measured labor anchor for the scorecard's payback arithmetic: a review step a human does at market wage is what the 5× labor-hour threshold is priced against. | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The PoC graduation scorecard: what written criteria (and what payback threshold) separate a pilot that earns production compute from the graveyard | 9 | 9 | 8 | 9 | 8.9 | **winner** |
| Token cost attribution by business unit (tag-before-request) | 8 | 8 | 7 | 8 | 7.7 | dropped — already argued by 2026-10-29 chargeback piece |
| Prompt prefix caching layout stability | 8 | 8 | 6 | 8 | 7.6 | dropped — 2026-10-27 cache piece owns this mechanism |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=3 fetched=3 sources=3 hosts=3 decision="sha1:7d0975986c" dedup="matched a prior artifact: 2026-11-12_enterprise_ai_finops_ev" window_days=180 checked_at=2026-11-26T18:05:17+00:00 -->
<!-- evergreen-gate:end -->
