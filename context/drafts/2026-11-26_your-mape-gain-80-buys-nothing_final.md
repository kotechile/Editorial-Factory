---
title: Your MAPE Gain: 80% Buys Nothing
vertical: demand_sensing_advanced_sop
kind: evergreen
archetype: evergreen
evergreen: true
persona: ops_leader
one_big_thing: "80% of forecast-accuracy improvements changed no reorder decision at all, so a promised MAPE point is not cash until you price it against your own carrying cost."
date: 2026-11-26
slug: your-mape-gain-80-buys-nothing
image_path: "context/assets/illustrations/your-mape-gain-80-buys-nothing/featured.jpg"
image_style: "long_lens_industry"
image_model: "flux"
image_alt: "80% Of Forecast Gains Buy Nothing. Pallet racks of shrink-wrapped stock stacked to the ceiling in a warehouse aisle, hard skylight raking"
image_caption: "80% Of Forecast Gains Buy Nothing: A MAPE point pays only where it shifts an order — price it against your holding cost."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
A vendor promises two points of MAPE (mean absolute percentage error — the average size of your forecast miss), and the reflex is to price them against the license fee. That price is wrong. The reason is not opinion. A study replayed 9.4 million real order decisions on the M5 Walmart forecast data and found 80% of forecast gains bought nothing — no changed order, no saved cash [1]. A score point pays only where it shifts an order you can name.

<!-- tldr -->
## At a glance
This article is for supply-chain and S&OP (sales and operations planning) leaders weighing a forecast-accuracy purchase. Its finding: most accuracy gains change no order call at all, so price the point against decision impact and your own holding cost, not the scorecard.

<!-- tension -->
## The conversion rate nobody quotes
Why does a better forecast so often buy nothing? The chain runs score to buffer to dollars. Forecast error feeds safety stock — the buffer held to cover forecast misses. That buffer only moves money when a smaller error lets you hold less of it. The 2024 economics study tested exactly that step on the M5 Walmart forecasting dataset: about 130 rival forecast sets, each pushed through a live order process rather than scored on error alone [1]. The result is blunt. Better forecasts paid off in only 12.6% of cases — about one order in eight [2]. I read that figure twice before accepting what it implies: seven gains in eight never touch a purchase order. Field results carry the same shape. One consumer-goods planner cut forecast error from 24% to 21% using live retail sales data and released $8.5M of stock. The money came from changed order sizes, not from the score. A score is a cause with a payout rate. The payout, not the score, is what you are buying.

## By the numbers
- **80% of accuracy gains:** Changed no order call and no money outcome in the M5 test [1].
- **12.6% of cases:** Paid off when the forecast improved — about 1 in 8 [2].
- **$8.5M released:** The stock one planner trimmed after a 3-point error cut changed order sizes.

<!-- tactical-insight -->
## Price the point before you sign
What I find hard to square is that buyers still price a license off a scorecard, when every pricing input sits in their own systems. The teams that turn a score into cash run three numbers. First, they set a holding-cost rate — the yearly cost of keeping stock. The standard rule is 15% to 25% of stock value, and some firms run to 55% [4]. That rate is what converts a smaller buffer into dollars. Second, they check the promised buffer cut against their own safety-stock formula. A vendor-typical result is 8% to 15% less buffer for a 5-point MAPE cut on mid-volume items; a pitch far above that band should be asked which order rule it changed [5]. Third, they ask for the decision layer, not the scorecard. The strongest model tests now push each forecast through a stock simulator and price it on holding cost and fill rate. A 2026 study graded seven forecast methods that way on the M5 data [3]. So ask for one thing before you sign: the vendor's own simulation of your order book. A vendor who cannot model the effect on your orders is selling a number with no payout rate.

<!-- nuanced-takeaway -->
## The catch
Even a paying gain pays dirty. The same M5 study — the 9.4 million-case Walmart forecast replay — found better forecasts made the money result worse in 7.3% of cases, and the wins shrank by roughly 28% once those losses were netted in [2]. Level matters too. A MAPE quoted on monthly total demand hides the SKU (stock-keeping unit) weekly error that the safety-stock formula consumes, so a two-point total gain can leave every buffer untouched [5]. My reading, held loosely: the aggregation trap bites more often than the backfire, because nobody checks the level a score is quoted at. Price the point at your own holding-cost rate — [inventory carrying cost runs 20–30% a year, not the 7% borrowing rate most models load](/inventory-carrying-cost-rate/) — demand a decision-impact estimate, and treat any score number without a payout story as marketing.

## Sources
- [1] Johann Robette / Demand-Planning.net, "Forecasting Fallacy Exposed: The Economics Behind Accuracy", 19 Aug 2024 — https://demand-planning.com/2024/08/19/forecasting-fallacy-exposed-the-economics-behind-accuracy
- [2] Johann Robette / Demand-Planning.net, "Forecasting Fallacy Exposed: The Economics Behind Accuracy", 19 Aug 2024 — https://demand-planning.com/2024/08/19/forecasting-fallacy-exposed-the-economics-behind-accuracy
- [3] Swata Marik, Swayamjit Saha, Garga Chatterjee, "Beyond Accuracy: Evaluating Forecasting Models by Multi-Echelon Inventory Cost" (arXiv:2603.16815), 17 Mar 2026 — https://arxiv.org/abs/2603.16815
- [4] APICS Princeton-Ocean Chapter (ASCM partner), "Cost of Carrying Inventory – Yes it costs money" — https://apicsprsjorg.starchapter.com/blog/id/6
- [5] Horizon Solutions, "Forecast Accuracy: MAPE, WMAPE, MAD and RMSE Explained", 10 Nov 2026 — https://www.horizonsolutions.ai/supply-chain-planning/forecast-accuracy
