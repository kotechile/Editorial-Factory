# Verified Brief: control_tower_exception_orchestration — 2026-11-17

Primary documents fetched and quoted: Sea-Intelligence press release 419 (the correction, 2026-11-07),
Sea-Intelligence press release 415 (issue 182, released 2026-10-28), the Shipzil FedEx monitoring page
(snapshot 2026-11-15, 21:35 UTC), and project44's Hormuz Week 34 dataset page.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | A — correction | Sea-Intelligence disclosed that a subset of vessel arrivals had been double counted in its aggregated alliance schedule-reliability figures | VERIFIED | https://www.sea-intelligence.com/press-room/419-glp-correction | "the release of the latest Global Liner Performance (GLP) report on October 27th, 2026" … "an error in which a small subset of vessel arrivals had been double counted in the calculation of aggregated alliance schedule reliability figures" |
| 2 | A — correction | The error dates to April 2015 and survived eleven years, including unnoticed by the alliance carriers that receive the raw data | VERIFIED | https://www.sea-intelligence.com/press-room/419-glp-correction | "This error dates back to the first alliance section in the April 2015 GLP report and went unnoticed for 11 years, both by our team and by alliance carriers receiving copies of the underlying raw data" |
| 3 | A — correction | Only the alliance aggregates were affected; carrier and trade scores were not | VERIFIED | https://www.sea-intelligence.com/press-room/419-glp-correction | "The error does not impact any carrier or trade scores, only the aggregated alliance scores." |
| 4 | A — correction | Mechanism: alliance scores were weighted averages across trades without correcting for calls that sit in two destination regions / two trade lanes | VERIFIED | https://www.sea-intelligence.com/press-room/419-glp-correction | "aggregate East-West alliance scores were calculated as weighted averages of schedule reliability across individual trades, without correcting for a small number of vessel calls in destination regions appearing on two separate trade lanes" |
| 5 | A — correction | Worked example: the New York call on a Shanghai–Algeciras–New York service lands on both Asia–North America East Coast and Transatlantic Westbound | VERIFIED | https://www.sea-intelligence.com/press-room/419-glp-correction | "on a service calling at Shanghai, Algeciras, and New York, the New York call would appear on both the Asia–North America East Coast and Transatlantic Westbound trade lanes, resulting in double counting" |
| 6 | A — correction | 461 calls affected, 2.28% of all alliance calls between February 2025 and September 2026; calls removed and the October report republished | VERIFIED | https://www.sea-intelligence.com/press-room/419-glp-correction | "Since the launch of the current alliance networks in February 2025 (incl. treating MSC as an alliance), 461 calls were affected, representing 2.28% of all alliance calls in February 2025 to September 2026. The affected calls have been removed from the GLP database, and we have republished the October 2026 report." |
| 7 | A — correction | The correction reverses the August/September 2026 alliance ranking | VERIFIED | https://www.sea-intelligence.com/press-room/419-glp-correction | previously: "MSC was the most reliable carrier alliance with schedule reliability of 68.9%, followed by Gemini with 68.4%, and Ocean Alliance with 44.8%"; corrected: "Gemini was the most reliable carrier alliance with schedule reliability of 70.4%, followed by MSC with 69.5%, and Ocean Alliance with 44.9%" |
| 8 | A — correction | The publisher characterises the impact as minimal | VERIFIED | https://www.sea-intelligence.com/press-room/419-glp-correction | "The correction has had minimal impact on overall alliance scores and trends, as illustrated in Figure 1, with differences barely discernible in most months. The only notable change is in August/September 2026" |
| 9 | B — benchmark level | September 2026 global schedule reliability 50.6%, +0.9 points M/M, after an aggregate −14.8 points from a 64.5% peak in May | VERIFIED | https://www.sea-intelligence.com/press-room/415-global-schedule-reliability-records-a-marginal-gain-in-september | "Schedule reliability improved by 0.9 percentage points M/M in September 2026 to 50.6%. The marginal improvement comes after three consecutive M/M drops, with an aggregate drop of ‑14.8 percentage points, from a peak of 64.5% in May." |
| 10 | B — benchmark level | Average delay of late vessel arrivals 6.65 days in September, −0.30 days M/M, the second-highest for the month | VERIFIED | https://www.sea-intelligence.com/press-room/415-global-schedule-reliability-records-a-marginal-gain-in-september | "The average delay of late vessel arrivals also improved, decreasing by ‑0.30 days M/M to 6.65 days. Despite this improvement, the average delay for late vessel arrivals in September 2026 is the second‑highest figure for the month." |
| 11 | B — benchmark level | Issue 182 covers 34 trade lanes and more than 60 carriers; Premier Alliance was the least reliable alliance at 41.5% | VERIFIED | https://www.sea-intelligence.com/press-room/415-global-schedule-reliability-records-a-marginal-gain-in-september | "covers schedule reliability across 34 different trade lanes and 60+ carriers"; "Premier Alliance was the least reliable carrier alliance with schedule reliability of 41.5%" |
| 12 | C — live feed | 162 carrier-affecting incidents recorded across four platforms run by three companies; 90% reported by only one company | VERIFIED | https://shipzil.com/carrier/fedex | "Across 162 carrier-affecting incidents recorded here, 90% were reported by only one company, so a problem on a single platform usually means that platform's FedEx integration rather than FedEx itself" |
| 13 | C — live feed | 47 of the 162 incidents (29%) had their carrier inferred from the incident title rather than a tagged component | VERIFIED | https://shipzil.com/carrier/fedex | "Of the 162 carrier-affecting incidents behind these figures, 47 (29%) had their carriers inferred from the incident title rather than a component the platform tagged." |
| 14 | C — live feed | Reported 90-day uptime across the four platforms ranges from 99.97% to 95.68%; incident counts in that window differ 2 / 10 / 5 / 1 | VERIFIED | https://shipzil.com/carrier/fedex | "EasyPost 99.97% 2 incidents · 1 measured / Shippo worst 95.68% 10 incidents · 6 measured / ShipStation 99.40% 5 incidents · 2 measured / ShipEngine 99.24% 1 incident · 1 measured" |
| 15 | C — live feed | Total incidents recorded per platform: Shippo 82, EasyPost 44, ShipEngine 25, ShipStation 11 — the page's own note that reporting less looks better | VERIFIED | https://shipzil.com/carrier/fedex | "a platform that reports less looks better here: Shippo 82, EasyPost 44, ShipEngine 25, ShipStation 11 incidents recorded respectively" |
| 16 | C — live feed | The figures are reported uptime, not measured uptime, and averaging across platforms flatters the result | VERIFIED | https://shipzil.com/carrier/fedex | "Either way this is uptime as reported by the platforms, not independently measured: there may be outages nobody reported." … "averaging mixes different integrations and improves the number every time a platform is added" |
| 17 | D — baseline | project44 measures transshipment dwell against a stated pre-conflict baseline (5 January – 23 February) and reports +12% to +59% across six ports | VERIFIED | https://www.project44.com/supply-chain-insights/hormuz-week-34-impact-on-ocean-freight-eases-but-diversions-and-port-dwell-remain-above-pre-conflict-levels/ | "At six key ports, TSP dwell over the last four weeks (Sep 28 to Oct 25) is above its pre-conflict baseline (Jan 5 to Feb 23), from 12% higher at Port Said to 59% higher at Hambantota and Mundra." |
| 18 | D — baseline | Named port pairs: Hambantota 17.4 vs 11.0 days; Mundra 10.6 vs 6.7; Singapore 7.6 vs 6.4 | VERIFIED | https://www.project44.com/supply-chain-insights/hormuz-week-34-impact-on-ocean-freight-eases-but-diversions-and-port-dwell-remain-above-pre-conflict-levels/ | "Hambantota: 17.4 days versus 11.0 (+59%)" · "Mundra: 10.6 days versus 6.7 (+59%)" · "Singapore: 7.6 days versus 6.4 (+20%)" |
| 19 | D — baseline | Jebel Ali export dwell averages 26.8 days across the conflict against 8.5 pre-conflict | VERIFIED | https://www.project44.com/supply-chain-insights/hormuz-week-34-impact-on-ocean-freight-eases-but-diversions-and-port-dwell-remain-above-pre-conflict-levels/ | "At Jebel Ali it averages 26.8 days across the conflict versus 8.5 days pre-conflict (+215%)" |
| 20 | A — derived | Point swings: Gemini +2.0, MSC +0.6, Ocean +0.1; the published MSC lead of 0.5 points became a Gemini lead of 0.9, a 1.4-point reversal — 2.8x the margin that had decided the ranking | DERIVED | desk arithmetic on rows 7 and 8 | 68.9 − 68.4 = 0.5; 70.4 − 68.4 = 2.0; 69.5 − 68.9 = 0.6; 70.4 − 69.5 = 0.9; 0.5 + 0.9 = 1.4; 1.4 ÷ 0.5 = 2.8 |

## Binding rulings for the drafter

1. **This is not a synthesis.** The angle brief carries `Angle Type: Single-Signal`; the draft must
   NOT set `synthesis: true` and must not put two anchor URLs under `sources:`. Shipzil's monitor is
   corroboration for the same failure class in the live feed, not a second thesis.
2. **Rows 9–11 are context only.** The level of reliability (50.6%) is not the argument — it may
   appear once, to date the report the correction concerns, and never as a trend claim about the
   market. This vertical published the reliability *level* on 2026-10-13; that piece is a retread
   risk and must not be re-argued.
3. **Print the publisher's own characterisation of the impact (row 8).** "Minimal impact … barely
   discernible in most months" is the sentences that keep this article honest; an article that
   implies the whole benchmark was wrong is over-claiming and fails review.
4. **Only the aggregates moved.** Rows 3 and 7 are binding together: the carrier-level numbers a
   shipper negotiates against were never affected, and the article must say so. The affected layer
   is the alliance aggregate.
5. **Shipzil's numbers are reported, not measured (row 16).** Every uptime figure must carry
   "reported"; never write "measured". The 162-incident total covers a period the page does not
   state — do not present it as a 90-day count; the 90-day count is the 2 / 10 / 5 / 1 series.
6. **The 1.4-point reversal is desk arithmetic (row 20)** and must be labelled as this desk's own
   subtraction, never as a published finding.
7. **project44's baseline is the positive example (rows 17–19)**, not a news signal: it shows what a
   disclosed denominator looks like, and it may contribute exactly one figure.
8. **No hands-on claim, no vendor recommendation.** This desk has no tower, no carrier contract and
   no platform relationship; the piece describes counting rules and reports what the sources do.

## Removal log
- Descartes' OpsForce design statement (false exceptions removed by an agent) — REMOVED on
  freshness: its write-up is 2026-01-30, outside the window. Not cited in the draft.
- FourKites' Magic Quadrant withdrawal — REMOVED: 2025-02-24.
- Samsara Agent Studio's 7x adoption — REMOVED: 2026-10-13.
- No claim was removed for lack of a source; two were removed on date.
