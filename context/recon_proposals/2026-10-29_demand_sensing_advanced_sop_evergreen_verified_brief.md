# Verified Brief: demand_sensing_advanced_sop — 2026-10-29 (evergreen)

Source of the topic: `context/recon_proposals/2026-10-29_demand_sensing_advanced_sop_evergreen_brief.md`
(evergreen gate PASS, 5 rows / 5 hosts, 2026-10-29T20:18:36Z). All five gate rows were re-fetched below and
their verbatim cells re-extracted from the retrieved body — not copied from the brief. Two claims that the
draft needs sit on the same pages but were read by eye outside a gate row, and are recorded here as such:
the frepple page's own conclusion (row 6) and its worked ADI example (row 8).

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | The grid and its boundaries | Demand is classified into four patterns — smooth, erratic, lumpy, intermittent — on average demand interval (ADI) and the squared coefficient of variation of demand sizes (CV²), with critical values of 1.32 and 0.49 | VERIFIED | https://arxiv.org/html/2304.03092v4 | "Following the categorization proposed by Syntetos et al. (2005), intermittent demand is classified into four patterns based on the average demand interval (ADI) and the square of the coefficient of variation (CV2), denoted as “smooth”, “erratic”, “lumpy”, and “intermittent”. The critical values of segmentation are 1.32 for ADI and 0.49 for CV2." |
| 2 | How a real catalogue splits (large sample) | Among 28,903 series, the four cells hold 1,994 smooth, 811 erratic, 4,987 lumpy and 21,111 intermittent | VERIFIED | https://arxiv.org/html/2304.03092v4 | "Among the 28903 time series, the series numbers of the four patterns are 1994, 811, 4987, and 21111." |
| 3 | The sample is Walmart's M5 data | The experiment uses 28,903 Walmart SKUs | VERIFIED | https://arxiv.org/html/2304.03092v4 | "Subsequently, we consider 28,903 SKUs of Walmart in our experiments." |
| 4 | The finding that kills method-selection | Method rankings barely change across the four demand patterns, and cost is higher in the lumpy and intermittent cells | VERIFIED | https://arxiv.org/html/2304.03092v4 | "First, the trade-off relationship between forecasting and inventory exists in all four demand patterns. Second, the rankings of methods exhibit minimal variation across different demand patterns, whether in terms of sharpness or inventory. Third, the intermittent category has the lowest sharpness scores among the four demand patterns, while we see higher costs in the lumpy and intermittent groups." |
| 5 | How a parts catalogue splits (second, different population) | A 403-part sample splits 92 smooth (23%), 97 erratic (24%), 67 intermittent (17%) and 147 lumpy (36%) | VERIFIED (vendor's own sample; undated) | https://frepple.com/blog/demand-classification | "Smooth 92 23% Erratic 97 24% Intermittent 67 17% Lumpy 147 36%" |
| 6 | The page's own conclusion | On that distribution the company should manage safety stock and service levels rather than chase forecast accuracy | VERIFIED (vendor claim; read by eye outside the gate row) | https://frepple.com/blog/demand-classification | "In the above example, 23% of the products have a smooth demand history profile, meaning that they should be easy to forecast. 40% of them are either erratic or intermittent and forecasting them is already more difficult. For the remaining 36%, the lumpy ones, we won’t reach an accurate forecast. With this distribution pattern, we can conclude that the management of this company should focus on the safety stock and service levels to cover for the variable nature of their demand rather than aiming at improving the forecast accuracy." |
| 7 | The lumpy cell is refused, and accuracy is the wrong metric outside smooth | The lumpy pattern is called unforecastable, and forecast accuracy is not a reliable performance metric outside the smooth cell | VERIFIED (vendor claim) | https://frepple.com/blog/demand-classification | "It is actually impossible to produce a reliable forecast, no matter which forecasting tools you use. This particular type of demand pattern is unforecastable." / "For all but the smooth demand profile, forecast accuracy is not a reliable performance metric." |
| 8 | The worked classification arithmetic | A sample with demands 1.71 periods apart, average quantity 10.57 and standard deviation 6.43 is an intermittent pattern (CV² ≈ 0.37, below 0.49, ADI above 1.32) | VERIFIED (vendor claim; the CV² is computed here from the page's own two inputs) | https://frepple.com/blog/demand-classification | "We can say that, in our data sample, a demand occurs on average every 1.71 periods." / "In our sample, the average quantity is 10.57, while the standard deviation is 6.43." / "This is an intermittent demand pattern." |
| 9 | The boundary's provenance, and its limits | The 1.32 / 0.49 cut-offs come from comparing Croston and SBA; the split should be non-linear; the classes assume stable ADI and CV, and classification must serve a purpose | VERIFIED (academic critique, dated 2024-07-16) | https://openforecast.org/2024/07/16/intermittent-demand-classifications-is-that-what-you-need | "They compared MSE performance of Croston (1972) and SBA (Syntetos & Boylan, 2005) forecasting methods, creating four categories of intermittent demand with ADI=1.32 and CV²=0.49 as cut-off values" / "Kostenko & Hyndman (2006) found that the split between Croston and SBA does not form four distinct areas – the cut-off should be non-linear." / "These classifications were designed for conventional intermittent demand (e.g., spare parts) assuming stable ADI and CV over time. But what if demand builds up (fewer zeroes, higher volume) or slows down? In such cases, SBC, KH, and PK would be inappropriate. Moreover, classification should serve a purpose." |
| 10 | Why percentage error fails on sparse series | An incumbent forecast on a low-volume portfolio ran at a weighted MAPE of 146%, and MAPE cannot be computed where demand is zero | VERIFIED (vendor claim, dated 2026-10-05) | https://demandforecast.ai/blog/intermittent-demand-forecasting | "Our 2026 forecast accuracy report includes a portfolio whose incumbent forecast started at a weighted MAPE of 146%." / "MAPE fails first. It divides the error by actual demand, and in 8 of our 12 weeks actual demand is zero." |
| 11 | The worked sparse series | A 12-week series selling in four weeks (ADI 3.0, CV² 0.10) averages 1.17 units a week; the four methods end at 1.27, 1.40, 1.33 and 1.23 | VERIFIED (vendor claim; illustrative arithmetic) | https://demandforecast.ai/blog/intermittent-demand-forecasting | "Take one SKU with 12 weeks of demand: 0, 3, 0, 0, 5, 0, 0, 0, 2, 0, 4, 0. That’s 14 units, or 1.17 a week. It sold in 4 of 12 weeks, so ADI = 12 ÷ 4 = 3.0. The four sale sizes average 3.5 with a CV² of 0.10. High ADI, low CV²: the intermittent quadrant." / "Simple exponential smoothing 1.27 +9% … Croston 1.40 +20% … SBA 1.33 +14% … TSB 1.23 +5%" |
| 12 | The correction term, and its caution | SBA multiplies Croston's forecast by (1 − alpha ÷ 2), a 5% trim at alpha 0.1 — and the correction can overshoot on items that sell in most periods | VERIFIED (vendor claim, dated 2026-10-05) | https://demandforecast.ai/blog/intermittent-demand-forecasting | "SBA (the Syntetos-Boylan Approximation) multiplies Croston’s forecast by (1 − alpha ÷ 2). At an alpha of 0.1 that’s a 5% reduction, so our 1.40 becomes 1.33." / "Teunter and Sani add a caution: the correction can overshoot and leave a negative bias on items that sell in most periods, so keep SBA for SKUs that are sparse to begin with." |
| 13 | What replaces the accuracy target | For a sparse item, fit a count distribution to the forecast rate and set the reorder point from it, because lead-time demand is not normal | VERIFIED (vendor claim, dated 2026-10-05) | https://demandforecast.ai/blog/intermittent-demand-forecasting | "Safety stock needs the same care. The textbook safety stock formula assumes demand is roughly normal, and lead-time demand for a sparse item isn’t. Fit a count distribution such as Poisson or negative binomial to the forecast rate, or resample from the SKU’s own history, and set the reorder point from that." |
| 14 | The service-level lever is item-specific | The cost of moving from 90% to 95% service differs by part | VERIFIED (vendor claim; undated) | https://www.toolsgroup.com/blog/intermittent-demand-forecasting-explained | "The service-level curve reveals the inventory cost of incremental availability. Moving from 90% to 95% service may be economical for one part and extremely expensive for another." |
| 15 | Where the work goes instead | The decision is per SKU, on intermittency, lumpiness, lifecycle and the decision being supported — and demand history is only one input | VERIFIED (vendor claim; qualitative — quoted in prose, no figure, so NOT a gate row) | https://www.toolsgroup.com/blog/intermittent-demand-forecasting-explained | "No single method is best for every SKU. In intermittent demand forecasting, model choice should reflect intermittency, lumpiness, lifecycle, and the decision being supported." / "Historical demand is only one input." |

## Discrepancies and flags recorded for the drafter
- **Two catalogues, two very different splits — never blend them.** Row 2 is 28,903 weekly Walmart M5 series
  (6.9% smooth); row 5 is a 403-part manufacturer-style sample (23% smooth, 36% lumpy). The populations
  differ, so the article names each sample with its size and never writes "most SKUs" or "half your
  catalogues" as though one number covered both.
- **The M5 counts are weekly, grocery-store, item-by-store series**, which is why so many fall in the
  intermittent cell: a series that sells in a minority of weeks is intermittent by construction. Say that
  when quoting the 6.9%, so the reader can see why a manufacturer's catalogue looks different.
- **Row 4 is the article's spine and its direction must not flip.** The paper finds that *method rankings
  barely vary* across the four cells. Any sentence where the classifier picks a winning forecasting method
  contradicts row 4, and row 9 already explains why the grid was built for exactly that purpose it does
  not deliver.
- **Rows 5–8, 10–15 are vendor pages.** None is a measured study. Rows 6, 7, 13 and 14 are the vendor's own
  opinion or advice, quoted as such; the article attributes each to its publisher rather than presenting
  them as findings. Row 11's four forecasts are a worked arithmetic example on one synthetic 12-week series,
  not an accuracy benchmark.
- **Row 8's CV² is computed here, not printed by the page**: (6.43 ÷ 10.57)² = 0.370. The page states the
  class ("intermittent demand pattern"); the 0.37 must be shown as arithmetic in the sentence so a reader
  can reproduce it.
- **Row 9 is a critique, not a refutation of the method.** Kourentzes says the grid is theoretically
  imprecise and assumes stability; he does not say the four cells are useless. The article may not claim
  that the grid has been disproved or withdrawn.
- Nothing was removed for want of a source. The one candidate row dropped this run was a consultancy
  "worked scenario" whose page states its figures are hypothetical and prints two different reorder points
  (11 units, then 16 units) for the same item — an internally inconsistent source is not a citation.

## Arithmetic checked before drafting
- 1,994 ÷ 28,903 = 6.90% of the M5 series in the smooth cell; 28,903 − 1,994 = 26,909, i.e. 93.1% outside it.
  State both from the two cited counts, and say "of the 28,903 weekly series in that dataset".
- 4,987 lumpy ÷ 28,903 = 17.3%; 21,111 intermittent ÷ 28,903 = 73.0%. The lumpy cell is the smaller of the two
  sparse cells, so the article must not call lumpy "the bulk of the catalogue" — on this sample the bulk is
  intermittent.
- Row 5: 92 + 97 + 67 + 147 = 403 parts; smooth 22.8%, erratic 24.1%, intermittent 16.6%, lumpy 36.5%.
- Row 8: 6.43 ÷ 10.57 = 0.6083; squared = 0.370. ADI 1.71 ≥ 1.32 with CV² 0.37 < 0.49 = intermittent cell.
- Row 11: four sale weeks (3, 5, 2, 4) average 3.5 units; 14 ÷ 12 = 1.17 units a week; the SBA trim at
  alpha 0.1 is 1.40 × (1 − 0.05) = 1.33. Do not restate the +9%/+20%/+14%/+5% column as accuracy scores.
- Row 12's trim is alpha ÷ 2 = 0.05 at alpha 0.1 — a 5% cut in the forecast level, not a 5-point accuracy gain.
