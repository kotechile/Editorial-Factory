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
meta_description: "Most of your stock-keeping units (SKUs) fail the 1.32 cut, because real sales happen less often than a planner expects."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/skus-fail-the-1-32-cut/featured.jpg"
image_style: "component_assembly"
image_model: "nanobanana"
image_alt: "Your SKUs Fail The 1.32 Cut. A four-quadrant modular sorting tray with irregular metal parts resting on a concrete surface."
image_caption: "Your SKUs Fail The 1.32 Cut: The limits of demand sensing for unpredictable items."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Most of your stock-keeping units (SKUs) fail the 1.32 cut, because real sales happen less often than a planner expects. In Walmart's M5 data, just 1,994 of 28,903 weekly item-and-store series sit in the smooth group where an accuracy goal actually works [1]. The other 26,909, which is 28,903 minus 1,994, fall outside it. Two numbers put them there: the average demand interval (ADI), which counts the time between sales, and the squared coefficient of variation (CV²) of the sale sizes [1]. The exact cut-offs are 1.32 for ADI and 0.49 for CV² [1].

<!-- tension -->

## The big picture:

The grid these two numbers build holds four distinct groups, and it was never meant to tell a supply chain team which SKUs need a forecast [1][3]. Researchers made it to pick between two math models, Croston's and the Syntetos-Boylan approximation (SBA), by checking their errors on real sales [3]. A forecasting expert notes the line between lumpy and erratic items exists only because of how those two models scored [3]. A later paper found the split should be curved, and the whole plan assumes ADI and CV² stay flat over time [3].

That last guess breaks down fast in a live catalog. Sales either fade into more zeroes or grow into fewer, so a SKU marked as intermittent last year can turn lumpy this year if nobody checks it [3]. What I take from the review is a much narrower use than picking models. The grid shows exactly which items an accuracy goal can grab, and a public test of 28,903 series finds that grip is weak [1].

That test is the M5 study, and its result goes against normal industry habits. The ranking of forecasting models barely moves between the four groups, whether you check sharpness or raw stock costs [1]. The lumpy and sparse groups carry the highest costs overall [1]. Picking a model by group is close to guessing. Asking whether to score a group at all is a different question, and this grid answers it.

## By the numbers

- **36% — Lumpy parts share:** A 403-part sample splits into 92 smooth, 97 erratic, 67 intermittent and 147 lumpy items, and the page says no forecasting tool will give that last group a reliable number [2].
- **21,111 — Intermittent M5 series:** Another 4,987 sit in the lumpy group, meaning the sparse majority is intermittent and the group no forecast fits is the minority [1].
- **146% — Low-volume weighted error:** An old forecast scored at this mean absolute percentage error (MAPE), showing what a percent metric does to an item that mostly reports zero [4].
- **1.40 against 1.17 — Sparse series spread:** Simple exponential smoothing hit 1.27, Croston hit 1.40, and the SBA hit 1.33 units a week. The real average was 1.17 on an item that sold in four of twelve weeks [4].

<!-- tactical-insight -->

## What I'd watch:

My read is that this shift lands in the next budget talk, not in a software test. Four specific moves are worth watching as teams adjust.

- **The catalog's cell counts:** A team that runs ADI and CV² over two years of history learns exactly what share of its SKUs can be graded. Where the lumpy share is large, the limit on any demand sensing buy is set before the renewal meeting [1][2].
- **The sparse tail metric:** Percent error cannot be figured out in a week with zero sales. The reported number shifts to absolute error or raw fill rate for those hard groups [2][4].
- **The tail service price:** Moving one part from 90% to 95% service is cheap, but doing it for another costs a lot. The tail gets priced item by item instead of against one broad goal [5].
- **The intermittent cell method:** A two-parameter rate estimate is the stated default for sparse items, with the SBA fix at half the smoothing constant. It can overshoot on items that sell in most periods [4].

<!-- nuanced-takeaway -->

## The catch

My sense is that the core math is solid but the printed examples are not universal. The M5 data tracks weekly grocery sales from single stores, so an item that sells in a minority of weeks is intermittent by definition, which is exactly why the smooth group is so small there [1]. A manufacturer's parts catalog splits quite differently, carrying a far larger smooth share [2]. Quote the sample, not the slogan.

The borders themselves are academic hand-me-downs. Researchers tuned them to split two models by their error rates, not to mark the strict edge of what a planner can know [3]. The critique that they assume steady sales is entirely right [3]. A planning team can move these lines for its own catalog and lose only the chance to compare notes with outside peers.

The final warning is strictly about the sources. Two of the five pages sell forecasting tools, so their numbers show exactly what their writers want a planner to try [4][5]. What a team actually controls is the record behind the reorder point, which has to be right before any rule runs on it. The desk's own [inventory record accuracy calculator](/tools/inventory-record-accuracy/) is the primary check for that.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Ops Leaders: Why 60.7% of Stock Hides Costs" -> /slow-movers-hold-your-stock/ [same site (aichieve.net); same category; topical overlap: skus, stock-keeping, units] Link "Ops Leaders: Why 60.7% of Stock Hides Costs" in the section where the article touches skus, stock-keeping, units. -->
<!-- internal-link hint: "63.6% OTIF: Your Hidden Quantity Gap" -> /your-hidden-quantity-gap/ [same site (aichieve.net); same category; topical overlap: units] Link "63.6% OTIF: Your Hidden Quantity Gap" in the section where the article touches units. -->
<!-- internal-link hint: "Dock Overtime: Your Real 14-Hour Cost" -> /hour-14-recovery-wall/ [same site (aichieve.net); same category; topical overlap: real] Link "Dock Overtime: Your Real 14-Hour Cost" in the section where the article touches real. -->
## Related reading

- [Ops Leaders: Why 60.7% of Stock Hides Costs](/slow-movers-hold-your-stock/) — more on Supply Chain & Operations
- [63.6% OTIF: Your Hidden Quantity Gap](/your-hidden-quantity-gap/) — more on Supply Chain & Operations
- [Dock Overtime: Your Real 14-Hour Cost](/hour-14-recovery-wall/) — more on Supply Chain & Operations
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Demand planners are moving from trying to forecast every SKU better to deciding which SKUs can be forecast at all. The main tool is two ratios: how often an item sells, and how much each sale size shifts.
- **Why It Matters:** Every accuracy goal, planner override and sensing licence tied to an unscorable item is spent on a number that will never move. The stock rule that would have covered that item goes unpriced.
- **What I'd Watch:** how quickly the segment pass reaches the budget talk, and what it changes when it does.
  - **Cell counts:** the share of a catalog landing in each of the four demand patterns, because it sets the limit on accuracy work.
  - **Metric swap:** moving sparse items off percent error and onto absolute error or fill rate.
  - **Service pricing:** costing the service goal per item on the sparse tail instead of applying one broad number to everything.
- **The Catch:** the printed borders were tuned for a narrow model test and assume sales habits stay put, so the first pass is a starting map rather than a final ruling.

## Sources
[1] Wang, Kang & Petropoulos — "Combining Probabilistic Forecasts of Intermittent Demand", arXiv:2304.03092v4 — https://arxiv.org/html/2304.03092v4
[2] frepple — "Demand classification" — https://frepple.com/blog/demand-classification
[3] Kourentzes — "Intermittent demand classifications: is that what you need?", OpenForecast, 16 July 2024 — https://openforecast.org/2024/07/16/intermittent-demand-classifications-is-that-what-you-need
[4] Hausner — "Intermittent demand forecasting: Croston's method, SBA, TSB and the long tail", Demand Forecast, 5 October 2026 — https://demandforecast.ai/blog/intermittent-demand-forecasting
[5] ToolsGroup — "Intermittent Demand Forecasting" — https://www.toolsgroup.com/blog/intermittent-demand-forecasting-explained
