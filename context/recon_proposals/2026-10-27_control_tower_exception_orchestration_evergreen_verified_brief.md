# Verified Brief: control_tower_exception_orchestration — 2026-10-27 (evergreen)
**Companion to:** `2026-10-27_control_tower_exception_orchestration_evergreen_brief.md` (evergreen gate PASS, marker rows=4 fetched=4 sources=4 hosts=3, dedup `2026-10-13_shippers-stuck-in-the-gap`)
**Article:** `published/2026-10-27_your-eta-misses-27-hours.md` — "Why Your ETA Misses 27 Hours"

## Claim table

| # | Claim as written | Source | Verbatim / evidence | Status |
|---|---|---|---|---|
| 1 | 2.21 hours mean absolute error on voyage legs under 24 hours | [1] arXiv 2601.08013v2 | "In short segments ( < 24 h), it reduces MAE from 2.24 h to 2.21 h ( 1.34% relatively) and MAPE from 23.45% to 22.51%" | VERIFIED |
| 2 | 6.89 hours at 24 to 72 hours | [1] | "For segments with average sailing durations 24–72 h, MAE drops from 7.16 h to 6.89 h" | VERIFIED |
| 3 | 11.97 hours at three to seven days | [1] | "For segments with average sailing durations 72–168 h … MAE reduced from 12.42 h to 11.97 h" | VERIFIED |
| 4 | 26.92 hours beyond a week | [1] | "In long segments (168–504 h), the proposed model achieves a reduction of MAE from 27.05 h to 26.92 h" | VERIFIED |
| 5 | Percentage error runs from 22.5% down to 10.9% across the bands | [1] | MAPE per bin: 22.51% (<24 h), 16.18% (24–72 h), 11.50% (72–168 h), 10.94% (168–504 h) | VERIFIED |
| 6 | 69.1% of trajectories within 20% of actual arrival time, first held-out set | [2] arXiv 2605.18408v1 | "with 69.1 % of trajectories within 20 % of actual arrival time" | VERIFIED |
| 7 | 62.1% on a second external test set | [2] | "On a second external test set, median RMSE is 27.36 min … with 62.1 % of trajectories within 20 %" | VERIFIED |
| 8 | The graph holds 5,433 nodes and 12,334 edges (context only, not in body) | [2] | "the resulting global graph comprises 5,433 geohash-3 nodes and 12,334 edges" | VERIFIED |
| 9 | 13,000+ AIS receivers; 300,000+ vessels tracked daily | [3] spire.com/maritime | "More than 300,000 Vessels tracked daily 13,000+ AIS receivers 25 sec Average message frequency 5 sec average data latency" | VERIFIED (vendor claim) |
| 10 | Average message frequency 25 seconds | [3] | "25 sec Average message frequency" | VERIFIED (vendor claim) |
| 11 | Average data latency about 5 seconds (carried in prose) | [3] | "5 sec average data latency" | VERIFIED (vendor claim) |
| 12 | Median hourly wage $39.58, annual $82,320, logisticians (2025) | [4] O*NET 13-1081.00 | "Median wages (2025) $39.58 hourly, $82,320 annual" | VERIFIED |
| 13 | A fifteen-minute manual arrival check costs $9.90 | derived from [4] | 39.58 × 0.25 = 9.895 | COMPUTED |
| 14 | A tenth-to-a-fifth window is ten to twenty hours on a 100-hour leg | derived from [1][2] | 100 × 0.10 = 10 h; 100 × 0.20 = 20 h | COMPUTED |
| 15 | A fifth of a 400-hour leg is 80 hours | derived | 400 × 0.20 = 80 h | COMPUTED |
| 16 | The bands come from research models fed 2021 AIS records | [1] | The paper's evaluation quarters against "2021 sailing records" and 2021 record counts in its segment tables | FLAGGED — the study's own window, stated in the body, never generalised to a vendor's live data |
| 17 | The measured percentage error makes a share-of-voyage window the right shape, and 10–20% the right share | author's derivation from [1][2] | The sources state per-bin MAPE and a 20% tolerance; neither recommends a threshold design | FLAGGED — written as the author's reading, not the papers' recommendation |
| 18 | A 62.1%/69.1% result can still miss the voyage that matters | [2] | "within 20%" is the study's own permissive test | FLAGGED — an argument about tails, not a measured failure count |
| 19 | The vendor's five-second latency is the feed's, not the estimate's freshness | [3] | The page reports "average data latency", with no ETA metric on it | FLAGGED — the body uses it only as evidence about the bottom of the stack |

**Tally:** 19 rows — 12 VERIFIED (three of them labelled vendor claims), 3 COMPUTED with endpoints shown, 4 FLAGGED with the reason. 0 REMOVED. No hands-on claim of any kind; the pipeline ran no hardware and tested nothing.

## Rulings carried into the prose
- The four band figures are one study's table and are attributed to it; the body never calls them a vendor benchmark or an industry average.
- 20% is the second study's *test tolerance*, not a recommendation; the article's rule is labelled as the author's derivation.
- The wage prices a manual re-check only; no per-alert volume or per-lane bill is invented anywhere.
- Means, not distributions: the body says half the voyages beat the quoted error and half do worse.
