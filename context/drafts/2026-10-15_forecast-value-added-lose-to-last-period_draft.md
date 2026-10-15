---
title: "Forecast Value Added: 52% Lose to Last Period"
vertical: demand_sensing_advanced_sop
persona: ops_leader
one_big_thing: "Score every layer of the planning process — the baseline, the edits, the consensus pass and any demand-sensing tool — against a naive test at the lag the plan is frozen, keep only the layers whose value added is positive, and tie any gain in accuracy to stock or cash before renewing the spend."
date: 2026-10-15
slug: forecast-value-added-lose-to-last-period
archetype: evergreen
evergreen: true
---

<!-- lead -->
In a study of more than 300,000 forecasts, 52% lose to a random walk — the plainest test there is, because it just carries last period's value forward unchanged [3]. That is the number I would put in front of a planning team about to renew a demand-sensing budget, because the question is not how clever the extra layer is. It is whether the layer's value added is positive.

<!-- tension -->

## The big picture:

A planning stack is a pile of layers. There is a model's baseline, then sales input, then the team's consensus pass, then a sensing tool that re-forecasts inside the month. Each layer is sold on accuracy, and few are ever scored against the layer below them.

What strikes me is how plain the missing test is. Forecast value added (FVA) is the change in error that one step of the process brings, set against a test forecast [3]. The usual test is the dumbest one around — last period's value, or the same week a year ago — and when a step's error is worse than that, the step took value out rather than adding it.

Scoring steps is rare work. In a survey of 661 planners, published in May 2026, 16% did not track forecast error at all [5]. Another 51% said they sometimes go ahead with a forecast they know is bad, because nothing better exists [5].

## By the numbers

- **52% — Worse than a random walk:** In a study of more than 300,000 forecasts, reported in a practitioner account of Gilliland's *Business Forecasting*, 52% did worse than carrying the last value forward [3].
- **147,000 — Forecasts pooled in one review:** Edits to the model's number helped only just over half of stock keeping units (SKUs) across six datasets, and edits that pushed the number up were the ones most likely to hurt [1].
- **60,000 — Forecasts from four supply-chain firms:** Edits raised accuracy on average at three of the four firms. The big edits helped. The small ones often did not [2].
- **13.8 points — A consensus layer that lost:** In a worked case cited from Gilliland's 2010 book, a consensus forecast lost to its test in 11 of 13 weeks, with an average error of 13.8 points [4].

<!-- tactical-insight -->

## What I'd watch:

The part I keep circling is what changes once a team scores its own process. The moves I have been watching all sit downstream of that one number.

- **The lag that counts:** A score only counts at the lag where the plan is frozen. For the baseline that is months out. For a sensing layer it is the nearest one to four weeks, the point where decisions are made [6].
- **The direction of the edit:** Edits that push a number up are the ones most likely to make it worse. A sales team raising the number is not proof of a better number [1].
- **The size of the edit:** Small tidy-up edits damage accuracy most often, and big ones tend to help. Most override rules let the wrong kind through [2].
- **The tether to real money:** A packaged-goods brand cut its 30-day forecast error, measured as mean absolute percentage error (MAPE), from 24% to 21% with a machine-learning sensing tool, and released $8.5M of finished-goods stock [7]. A gain that does not turn into stock or cash is not a business result [4].
- **The sensing layer's own test:** Every layer, sensing included, has to beat the layer beneath it, or it adds cost and complexity for nothing [6].

<!-- nuanced-takeaway -->

## The catch:

My read is that value added is a check-up, not a ruling. Four limits matter.

- The tool has its own critics, and their point is about money. A forecast can be 40% more accurate while the firm makes 75% less profit overall [4].
- One bad read is not an order to retire a step. The cited advice on a consensus pass that lost 11 of 13 weeks was to find out why it behaves that way, not to shut it down [4].
- The studies measure three different things on three different samples: 52% of forecasts losing to a random walk, just over half of SKUs helped by edits, three of four firms helped. As one number, they mislead.
- A good read does not insure you against a demand shock. It prices the error a better forecast can take out, and nothing more.

<!-- tldr -->

## At a glance

- **The Big Shift:** Planning teams now run several forecast layers, and forecast value added — the change in error one layer contributes against a naive test — is the check that shows which layers earn their keep.
- **Why It Matters:** In a study of more than 300,000 forecasts, 52% were worse than carrying last period's value forward. A layer that cannot beat that is cost and complexity rather than accuracy, and one brand's 3-point error cut freed $8.5M of stock [7].
- **What I'd Watch:** How teams score their own process, and what they do with the answer.
  - **The frozen lag:** Scoring only counts at the point the plan was locked, where the call was made [6].
  - **Edit direction and size:** Small edits and upward edits are the two that most often damage accuracy [1][2].
  - **The dollar tether:** Whether a gain in points turns into stock or cash, or only into a better-looking dashboard [4].
- **The Catch:** Value added is a check-up with limits. Accuracy is not profit, one poor quarter is not proof, and a better forecast does not take demand risk away.

## Sources

[1] Fildes, Goodwin & De Baets, "Forecast value added in demand planning", International Journal of Forecasting 41(2):649–669 (2025) — https://ideas.repec.org/a/eee/intfor/v41y2025i2p649-669.html (retrieved 2026-10-15)
[2] Fildes, Goodwin, Lawrence & Nikolopoulos, "Effective forecasting and judgmental adjustments: an empirical evaluation and strategies for improvement in supply-chain planning", International Journal of Forecasting 25(1):3–23 (2009) — https://research.manchester.ac.uk/en/publications/effective-forecasting-and-judgmental-adjustments-an-empirical-eva (retrieved 2026-10-15)
[3] Gibbons, "How To Use Forecast Value Added Analysis", Demand Planning / Institute of Business Forecasting (2018-02-12), reporting Steve Morlidge's study of more than 300,000 forecasts as cited in Gilliland, Tashman & Sglavo, *Business Forecasting: Practical Problems and Solutions* — https://demand-planning.com/2018/02/12/what-is-forecast-value-added-analysis (retrieved 2026-10-15)
[4] Lokad, "Forecast Value Added" (reference page, reviewed Q2 2024; cites Gilliland, 2010) — https://www.lokad.com/forecast-value-added (retrieved 2026-10-15)
[5] DOSS, "Shelf Life Stress: What's Keeping Inventory Teams up at Night in 2026?" (research report dated 18 May 2026; 661 respondents) — https://www.doss.com/research/top-inventory-stressors-affecting-teams (retrieved 2026-10-15)
[6] Infomineo, "Demand Sensing vs Demand Forecasting: How to Run Both Without Making Your Plan Worse" (2026-09-21) — https://infomineo.com/services/data-analytics/demand-sensing-vs-demand-forecasting-how-to-run-both-without-making-your-plan-worse (retrieved 2026-10-15)
[7] Field notes — context/growth_os/customer-truth.md §`demand_sensing_advanced_sop` Anecdote 1: a consumer packaged goods brand cut 30-day forecast MAPE from 24% to 21% with machine-learning demand sensing and permanently trimmed $8.5M of excess finished-goods inventory.
