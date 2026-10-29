---
title: Your SKUs Fail The 1.32 Cut
vertical: demand_sensing_advanced_sop
persona: ops_leader
one_big_thing: "Score every SKU on its average demand interval and the squared coefficient of variation, then stop buying forecast accuracy for the cells that cannot carry it and cover them with stock instead."
date: 2026-10-29
slug: skus-fail-the-1-32-cut
archetype: evergreen
evergreen: true
---

<!-- lead -->
Your stock-keeping units (SKUs) fail the 1.32 cut more often than they pass it, because real demand is sparser than the planning calendar assumes. In Walmart's M5 dataset, 1,994 of 28,903 weekly item-and-store series sit in the smooth cell, the only cell where an accuracy target means much [1]. The other 26,909, which is 28,903 minus 1,994, fall outside it. Two numbers put them there: the average demand interval (ADI), which counts the periods between non-zero sales, and the squared coefficient of variation (CV²) of the sale sizes [1]. The cut-offs are 1.32 for ADI and 0.49 for CV² [1].

<!-- tension -->

## The big picture:

The grid those numbers build has four cells. It was never designed to tell a planning team which SKUs deserve a forecast [1][3]. It was built to pick between two methods, Croston's and the Syntetos-Boylan approximation (SBA), by comparing their errors on real series [3]. A forecasting academic's account of it is blunt. The line between the lumpy and erratic cells exists because of how those two methods scored [3]. A later paper found the split should be non-linear, and the whole scheme assumes ADI and CV² hold still over time [3].

That last assumption breaks in a live catalog. Demand either fades into more zeroes or builds into fewer, so a SKU filed as intermittent last year can be lumpy this year with nobody re-scoring it [3]. What I take from the critique is a narrower use than picking methods. The grid says which series an accuracy target can grip, and the largest public test of it says that grip is thin.

That test is the study above, and its result runs against the usual use. The ranking of methods barely moves between the four cells, in sharpness or in inventory cost [1]. The lumpy and sparse groups carry the higher costs [1]. Picking a method by cell is close to guessing. Asking whether to score a cell at all is a different question, and the grid answers it.

## By the numbers

- **36% — lumpy share of a parts catalog:** a 403-part sample splits 92 smooth, 97 erratic, 67 intermittent and 147 lumpy. The page calls that last pattern unforecastable "no matter which forecasting tools you use" [2].
- **21,111 — intermittent series in the M5 test:** the other 4,987 sit in the lumpy cell. The sparse majority is intermittent, and the group no forecast fits is the minority [1].
- **146% — a low-volume portfolio's weighted error:** an incumbent forecast scored at that mean absolute percentage error (MAPE). That is what a percent metric does to a series that mostly reports zero [4].
- **1.40 against 1.17 — one sparse series, four methods:** simple exponential smoothing ended at 1.27, Croston at 1.40, SBA at 1.33 and one more method at 1.23 units a week. The actual average was 1.17, on a series that sold in four of twelve weeks [4].

<!-- tactical-insight -->

## What I'd watch:

My read is that this lands in the next budgeting round, not in a software trial. Four things are worth watching.

- **The catalog's own cell counts:** a team that runs ADI and CV² over two years of history learns what share of its SKUs can be graded. Where the lumpy share is large, the ceiling on any sensing purchase is set before the renewal meeting [1][2].
- **The metric on the sparse tail:** percent error cannot be computed in a week with no demand. The reported number shifts to absolute error or fill rate for those cells [2][4].
- **The price of service on that tail:** moving one part from 90% to 95% service is cheap, and doing it for another is expensive. The tail gets costed item by item instead of against one blanket target [5].
- **The method inside the intermittent cell:** a two-parameter rate estimate is the published default for sparse items, with the SBA correction at half the smoothing constant. It can overshoot on items that sell in most weeks [4].

<!-- nuanced-takeaway -->

## The catch

My sense is that the arithmetic is sturdy and the examples are not universal. M5 is weekly grocery data from single stores, so a series that sells in a minority of weeks is intermittent by definition. That is why the smooth cell is small there [1]. A parts catalog for machines splits differently, with a far larger smooth share [2]. Quote the sample, not the slogan.

The boundaries themselves are hand-me-downs. They were tuned to separate two methods by their error, not to mark the edge of what a planner can know [3]. The critique that they assume stable demand is correct [3]. A team can move them for its own catalog and lose only the ability to compare notes with its peers.

The last caveat is about the sources. Two of the five pages sell forecasting software, so their numbers describe what their authors want a planner to try [4][5]. What a team controls is the record behind the reorder point, which has to be right before any policy runs on it. The desk's own [inventory record accuracy calculator](/tools/inventory-record-accuracy/) is the check for that.

<!-- tldr -->

## At a glance

- **The Big Shift:** Demand planners are moving from "forecast every SKU better" to "decide which SKUs can be forecast at all". The tool is two ratios: how often a series sells, and how much each sale size varies.
- **Why It Matters:** Every accuracy target, override hour and sensing licence tied to a series that cannot be scored is spent on a number that will not move. The stock policy that would have covered that series goes unpriced.
- **What I'd Watch:** how quickly the segment pass reaches the budget talk, and what it changes when it does.
  - **Cell counts:** the share of a catalog landing in each of the four demand patterns, because it sets the ceiling on accuracy work.
  - **Metric swap:** moving sparse series off percent error and onto absolute error or fill rate.
  - **Service pricing:** costing the service target per item on the sparse tail instead of applying one number to everything.
- **The Catch:** the published boundaries were tuned for a method comparison and assume demand behaviour stays put, so the pass is a starting map, not a verdict.

## Sources
[1] Wang, Kang & Petropoulos — "Combining Probabilistic Forecasts of Intermittent Demand", arXiv:2304.03092v4 — https://arxiv.org/html/2304.03092v4
[2] frepple — "Demand classification" — https://frepple.com/blog/demand-classification
[3] Kourentzes — "Intermittent demand classifications: is that what you need?", OpenForecast, 16 July 2024 — https://openforecast.org/2024/07/16/intermittent-demand-classifications-is-that-what-you-need
[4] Hausner — "Intermittent demand forecasting: Croston's method, SBA, TSB and the long tail", Demand Forecast, 5 October 2026 — https://demandforecast.ai/blog/intermittent-demand-forecasting
[5] ToolsGroup — "Intermittent Demand Forecasting" — https://www.toolsgroup.com/blog/intermittent-demand-forecasting-explained
