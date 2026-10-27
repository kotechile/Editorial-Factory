---
title: "Why Your ETA Misses 27 Hours"
vertical: control_tower_exception_orchestration
persona: supply_chain_architect
one_big_thing: "Arrival-prediction error is a share of the voyage, not a fixed number of hours — measured at 2.21 hours on legs under a day, 6.89 at 24 to 72 hours, 11.97 at three to seven days and 26.92 beyond a week — so an exception threshold written in flat hours is slack on short lanes and tight on long ones, and the alert window belongs as a share of remaining transit time."
date: 2026-10-27
slug: your-eta-misses-27-hours
archetype: evergreen
evergreen: true
---

<!-- lead -->
A commercial ship-tracking feed refreshes a vessel every 25 seconds [3]. Yet the best published model of a vessel's estimated time of arrival (ETA) misses the real arrival by 26.92 hours on average on a voyage leg longer than a week [1]. Call it 27 hours, and your tower should read it as a floor rather than a rival's benchmark, because the study runs on the same Automatic Identification System (AIS) records a vendor's product would buy. The error is not the pipe. It is the math of forecasting a distance still to run, which is why it grows with the length of the leg.

<!-- tension -->

## The big picture:

What strikes me first is how little of this error belongs to the ship. A control tower takes positions, speeds and port calls, and turns them into one number: when this box arrives. That number is a forecast over the remaining voyage, so every hour of uncertainty left in the route lands inside it. The paper that models the problem most carefully measures the forecast per duration band, and the bands are the argument [1].

On legs under a day, the strongest of the models tested, its own included, averages 2.21 hours of absolute error [1]. At 24 to 72 hours the figure is 6.89 hours, at three to seven days it is 11.97 hours, and beyond a week it reaches 26.92 hours [1]. In percentage terms the same table runs from 22.5% down to 10.9%, so the estimate stays at roughly a tenth to a fifth of the voyage at every length [1]. That last number is the one an architect can actually use.

A second study reaches the same shape by a different method. Its graph of historical vessel travel places only 69.1% of the voyage paths it models within 20% of the actual arrival time on its first held-out set, and 62.1% on a second external set [2]. Two independent teams, two different models, and the tolerance that survives both is roughly a fifth of the remaining voyage.

Meanwhile the tracking layer sells precision rather than accuracy. The vendor behind one large AIS network reports 13,000+ receivers, more than 300,000 vessels tracked daily, an average message frequency of 25 seconds and an average data latency of about 5 seconds [3]. All of that is true, and all of it describes the bottom of the stack. A position that arrives five seconds late is still a position; the arrival forecast built on top of it can be a day out.

## By the numbers

- **62.1% — within 20% of the arrival:** On a second external test set the graph model placed 62.1% of voyage paths inside a fifth of the actual arrival time, against 69.1% on its own held-out set [2].
- **13,000+ receivers — behind the feed:** The AIS network the vendor sells reports 13,000-plus receivers and more than 300,000 vessels tracked daily, with an average message frequency of 25 seconds [3].
- **$39.58 an hour — the manual re-check:** Logisticians earned a median $82,320 a year, or $39.58 an hour, in 2025, which is the rate at which a fifteen-minute arrival check is billed [4].

<!-- tactical-insight -->

## What I'd watch:

The architects I would trust here are not buying sharper predictions. They are re-sizing the alert window around the error they cannot remove. A twelve-hour threshold looks sensible until it is placed at both ends of the ladder. On a six-hour drayage leg it exceeds the whole voyage, so it never fires. On a two-week ocean leg it sits under half the measured error, so it fires on noise.

The shape that fits the data is a window expressed as a share of remaining transit time, with an absolute floor for short legs. The two studies bracket that share loosely, and a tenth to a fifth of the voyage is where the measured percentage error sits [1][2]. On a 100-hour leg that is a window of ten to twenty hours, which is also the smallest shift a planner can still respond to.

Then price the fallback honestly. Where the model sits inside the window, someone still re-checks the arrival by hand, and at the 2025 median wage for logisticians that check runs to $9.90 for fifteen minutes of work [4]. A threshold tuned so tightly that every long lane triggers a daily re-check is a labour bill disguised as an alert setting.

What I keep coming back to is that a control tower's prediction only pays when there is time left to act on it. The measured error is a bound on that time, not a detail of the estimator.

<!-- nuanced-takeaway -->

## The catch

My read is that this ladder is a shape and a floor, not a league table of products. The bands come from research models fed 2021 AIS records [1], and a commercial vendor's estimate may well be better on a mature lane and worse on a thin one. What survives any re-measurement is the direction: error rises with the horizon, so a fixed-hour threshold cannot be right across a fleet's whole lane mix.

The percentage tolerance also buys less than it appears to. A window of a fifth of the voyage is 80 hours on a 400-hour leg, which means the tower cannot promise early warning there at all; it can only promise an honest one. Early signal on a long ocean lane has to come from something other than the arrival estimate, such as berth windows and terminal queues that move before the ship does.

The second study's headline reads badly in both directions. Being within 20% is a permissive test, and a model can clear it on most trajectories while still missing the one voyage that decides a quarter [2]. The error quoted throughout is also a mean, so half the voyages beat it and half do worse, and the tail is where the chargebacks live.

None of this shrinks the tower's other blind spots. The exception no arrival model sees, a load handed to a fake carrier at the dock, is the reminder that [a control tower's own blind spots](/control-tower-silent-exception/) do not close when the arrival estimate gets better.

<!-- tldr -->

## At a glance

- **The Big Shift:** Arrival prediction is sold as a precision product, but the error behind it behaves like a percentage of the voyage rather than a fixed count of hours. The best published models miss a leg longer than a week by roughly a day on average.
- **Why It Matters:** Every exception rule in a control tower is a claim about how wrong its arrival estimate can be. A flat-hour threshold is slack on short lanes and tight on long ones, which turns the alert queue into noise on exactly the lanes where a miss costs most.
- **What I'd Watch:**
  - **The window's unit:** size the alert as a share of remaining transit instead of a flat hour count, so a drayage leg and a two-week ocean leg obey one rule.
  - **The fallback's price:** every alert a planner cannot trust becomes a manual re-check, and that labour is a real line item at the median logistician wage.
  - **The response time left:** a prediction is worth only what the remaining time allows, so watch how long dispatching, rerouting and customer notification actually take.
- **The Catch:** The bands come from research models on older tracking records, the percentage tolerance is generous, and a mean error means half the voyages are worse than the number the tower quotes.

<!-- internal-links -->

## Sources

[1] Nairui Liu, Fang He, Xindi Tang, Yineng Wang, "Beyond the Next Port: A Multi-Task Transformer for Forecasting Future Voyage Segment Durations" (arXiv:2601.08013v2, 17 May 2026), duration-band error table and §1 — https://arxiv.org/html/2601.08013v2
[2] Neofytos Dimitriou, "Historical Knowledge Graphs for Global Maritime Estimated Time of Arrival" (arXiv:2605.18408v1, 18 May 2026), abstract and held-out test results — https://arxiv.org/html/2605.18408v1
[3] Kpler AIS, "Global ship tracking" (vendor product page, figures as retrieved 2026-10-27) — https://spire.com/maritime/
[4] O*NET OnLine, "13-1081.00 - Logisticians", median wages (2025) — https://www.onetonline.org/link/summary/13-1081.00
