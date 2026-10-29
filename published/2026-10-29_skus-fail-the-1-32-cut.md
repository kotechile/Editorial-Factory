---
title: Your SKUs Fail The 1.32 Cut
vertical: demand_sensing_advanced_sop
persona: ops_leader
one_big_thing: "Score every SKU on its average demand interval and the squared coefficient of variation, then stop buying forecast accuracy for the cells that cannot carry it and cover them with stock instead."
date: 2026-10-29
slug: skus-fail-the-1-32-cut
archetype: evergreen
evergreen: true
meta_title: "Your SKUs Fail The 1.32 Cut"
meta_title_source: "derived_from_title"
meta_description: "Most stock-keeping units fail the 1.32 cut, because real sales happen less often than a planner expects."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/skus-fail-the-1-32-cut/featured.jpg"
image_style: "component_assembly"
image_model: "nanobanana"
image_alt: "Your SKUs Fail The 1.32 Cut. A four-quadrant modular sorting tray with irregular metal parts resting on a concrete surface."
image_caption: "Your SKUs Fail The 1.32 Cut: The limits of demand sensing for unpredictable items."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Most of a catalogue cannot carry an accuracy target, and no model change fixes that, because the items do not sell often enough to score. The limit is a sorting rule few teams have looked up. Score each stock-keeping unit (SKU) on two measures. The first is the average demand interval (ADI), the gap between sales; the second is the squared coefficient of variation of sale sizes (CV²). Most items then land outside the one group where a target means anything: in Walmart's M5 dataset, just 1,994 of 28,903 weekly item-and-store series (about 7%) sit in the smooth group [1]. The other 26,909 fail the 1.32 cut on ADI or the 0.49 cut on CV², because their sales arrive too rarely to score.

<!-- tension -->
My read starts with the sample sizes, because the two catalogues in this story split in opposite directions.

## The big picture

The grid behind those numbers comes from the Syntetos-Boylan-Croston (SBC) framework, which sorts demand into four cells. Smooth items sell in most periods with steady sale sizes. Erratic items sell in most periods but the sizes swing. Intermittent items sell rarely with steady sizes, and lumpy items sell rarely and swing too. An item with ADI below 1.32 and CV² below 0.49 is smooth; push either measure past its cut and it moves into another cell. On the M5 sample the cells hold 1,994 smooth, 811 erratic, 4,987 lumpy and 21,111 intermittent series [1].

The grid was never built to tell a supply team which SKUs deserve a forecast. Nikolaos Kourentzes traced where the two cuts came from. They came from comparing the errors of Croston's method with the Syntetos-Boylan approximation (SBA). So the line between lumpy and erratic marks where one method beat the other [3]. It does not mark where a planner's knowledge runs out. Kostenko and Hyndman later found the true split is not a straight line, and the cells assume ADI and CV² hold still over time [3].

That last guess breaks in a live catalogue. Sales build up (fewer zero weeks, larger orders) or fade (more zeros). A SKU called intermittent last year can be lumpy this year with nobody rechecking it [3].

The Wang, Kang and Petropoulos study is where the grid earns its keep, and its result cuts against normal practice. The ranking of methods barely moves between the four cells, on sharpness or on stock cost. The lumpy and intermittent cells carry the highest costs overall [1]. Choosing a method by cell is close to guessing. Asking whether a cell can be scored at all is a different question, and the grid answers that one.

## By the numbers

- **93% — The share accuracy cannot govern:** 26,909 of the 28,903 weekly M5 series fall outside the smooth cell. An accuracy target reaches one item in fourteen, and stock rules cover the rest [1].
- **73% — Sparse, but predictable:** 21,111 series are intermittent, where a sale's size is steady even if its timing is not; only 4,987 are lumpy [1][2]. The bulk of an unscorable catalogue is not the hopeless cell, so a blanket "we cannot forecast this" verdict over-reaches.
- **146% — Weighted error under MAPE:** one portfolio's incumbent forecast scored a weighted mean absolute percentage error (MAPE) of 146% [4]. The metric divides by actual demand, and actual demand is zero in most weeks. Read the figure as a verdict on the metric, not on the planner.
- **1.40 against 1.17 — Croston against reality:** a 12-week series sold in four weeks and averaged 1.17 units a week. Exponential smoothing landed at 1.27, Croston at 1.40 and the SBA at 1.33 [4]. Method choice moves the number by a fifth, which is why teams argue about it, and the item still needs a stock rule rather than a sharper score.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 172" style="background:#0f172a; border-radius:8px; font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,sans-serif; margin:16px 0; max-width:100%; height:auto;">
  <text x="20" y="36" fill="#f8fafc" font-size="16" font-weight="600">Your SKUs Fail The 1.32 Cut</text>
  <text x="20" y="52" fill="#94a3b8" font-size="12">Figures as stated in this article&#x27;s own numbers section (verified figures, %)</text>
  <!-- Row 1 -->
  <text x="20" y="84" fill="#e2e8f0" font-size="13" font-weight="500">The share accuracy cannot govern</text>
  <rect x="240" y="70" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="70" width="279" height="18" rx="4" fill="#818cf8"/>
  <text x="529" y="84" fill="#f1f5f9" font-size="13" font-weight="600">93%</text>
  <text x="583" y="84" fill="#64748b" font-size="11">([1])</text>
  <!-- Row 2 -->
  <text x="20" y="132" fill="#e2e8f0" font-size="13" font-weight="500">Sparse, but predictable</text>
  <rect x="240" y="118" width="300" height="18" rx="4" fill="#1e293b"/>
  <rect x="240" y="118" width="219" height="18" rx="4" fill="#818cf8"/>
  <text x="469" y="132" fill="#f1f5f9" font-size="13" font-weight="600">73%</text>
  <text x="523" y="132" fill="#64748b" font-size="11">([1] [2])</text>
</svg>

<!-- tactical-insight -->

## What I'd watch

My sense is that this is a budgeting question before it is a modelling question, and four items carry the money.

- **Catalog segmentation audit:** the first pass runs ADI and CV² over two years of item history. It counts the SKUs that can be scored at all. Where the smooth share is small, the limit on any demand sensing renewal is set before the vendor meeting [1][2].
- **Metric swap on sparse items:** percent error gives way to absolute error or fill rate for the intermittent and lumpy cells. A percentage built on zero demand cannot be improved by any forecast, however good [2][4].
- **Service-level pricing by item:** moving one part from 90% to 95% service is cheap, while moving the whole tail is not. The tail gets priced item by item instead of against one service target [5].
- **Method defaults for intermittent items:** Croston's method with the SBA correction is the stated default for sparse items. It multiplies the forecast by one minus half the smoothing constant, and it can overshoot on items that sell in most periods [4].

<!-- nuanced-takeaway -->

## The catch

My sense is that the maths holds up but the samples do not travel. The M5 figures come from weekly grocery sales in single stores. There, an item that sells in most weeks is rare by design, which is why only 7% land in the smooth cell [1]. A manufacturer's parts catalogue splits the other way: on a 403-part sample, 92 parts are smooth and 147, or 36%, are lumpy [2]. Quote each sample with its size, never one share as though it covered every catalogue.

The borders were fitted to a model test. Kourentzes' review of where they came from is the best part of the critique. The cut sits where Croston's error crossed the SBA's, not where a planner stops knowing [3]. The cells also assume ADI and CV² hold still. A team can move those lines for its own catalogue and lose only the ability to compare notes with outside peers.

Two of the five sources sell forecasting tools, so their numbers show what their writers want a planner to try [4][5]. What a team controls is the record behind the reorder point, since no stock rule and no model beats the demand history it reads. That record is worth measuring before any algorithm is tuned, and our [inventory record accuracy calculator](/tools/inventory-record-accuracy/) reports the gap between recorded stock and the physical count.

<!-- tldr -->

## At a glance

**The shift:** accuracy spend moves off the SKUs that cannot be scored and onto stock rules that can cover them.
**The number:** 93% of a 28,903-series sample sits outside the cell where accuracy targets work.
**The risk:** the boundaries were tuned to pick between two methods, not to grade a catalogue.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Ops Leaders: Why 60.7% of Stock Hides Costs" -> /slow-movers-hold-your-stock/ [same site (aichieve.net); same category; topical overlap: skus, stock-keeping, units] Link "Ops Leaders: Why 60.7% of Stock Hides Costs" in the section where the article touches skus, stock-keeping, units. -->
<!-- internal-link hint: "63.6% OTIF: Your Hidden Quantity Gap" -> /your-hidden-quantity-gap/ [same site (aichieve.net); same category; topical overlap: units] Link "63.6% OTIF: Your Hidden Quantity Gap" in the section where the article touches units. -->
<!-- internal-link hint: "Dock Overtime: Your Real 14-Hour Cost" -> /hour-14-recovery-wall/ [same site (aichieve.net); same category; topical overlap: real] Link "Dock Overtime: Your Real 14-Hour Cost" in the section where the article touches real. -->
## Related reading

- [$200,000 Robots: Your Seller Won't Stay](/your-seller-wont-stay/) — more on Supply Chain & Operations
- [Ops Leaders: Why 60.7% of Stock Hides Costs](/slow-movers-hold-your-stock/) — more on Supply Chain & Operations
- [Your 60% Drop Isn't the Model](/your-60-drop-isnt-the-model/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

## Sources
[1] Wang, Kang & Petropoulos — "Combining Probabilistic Forecasts of Intermittent Demand", arXiv:2304.03092v4 — https://arxiv.org/html/2304.03092v4
[2] frepple — "Demand classification" — https://frepple.com/blog/demand-classification
[3] Kourentzes — "Intermittent demand classifications: is that what you need?", OpenForecast, 16 July 2024 — https://openforecast.org/2024/07/16/intermittent-demand-classifications-is-that-what-you-need
[4] Hausner — "Intermittent demand forecasting: Croston's method, SBA, TSB and the long tail", Demand Forecast, 5 October 2026 — https://demandforecast.ai/blog/intermittent-demand-forecasting
[5] ToolsGroup — "Intermittent Demand Forecasting" — https://www.toolsgroup.com/blog/intermittent-demand-forecasting-explained
