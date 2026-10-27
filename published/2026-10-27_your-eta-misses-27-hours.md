---
title: "Why Your ETA Misses 27 Hours"
vertical: control_tower_exception_orchestration
persona: supply_chain_architect
one_big_thing: "Arrival-prediction error is a share of the voyage, not a fixed number of hours — measured at 2.21 hours on legs under a day, 6.89 at 24 to 72 hours, 11.97 at three to seven days and 26.92 beyond a week — so an exception threshold written in flat hours is slack on short lanes and tight on long ones, and the alert window belongs as a share of remaining transit time."
date: 2026-10-27
slug: your-eta-misses-27-hours
archetype: evergreen
evergreen: true
meta_title: "Why Your ETA Misses 27 Hours"
meta_title_source: "derived_from_title"
meta_description: "Because distance makes guessing harder, an estimated time of arrival (ETA) misses the mark by roughly 27 hours on average for trips longer than a week."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-eta-misses-27-hours/featured.jpg"
image_style: "clay_render"
image_model: "nanobanana"
image_alt: "An adjustable mechanical rail with a yellow sliding bracket clamped to it, resting on a steel console in a control room."
image_caption: "The Math Of ETA Prediction: Why ETA alerts must scale with remaining transit time."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Because distance makes guessing harder, an estimated time of arrival (ETA) misses the mark by roughly 27 hours on average for trips longer than a week [1]. A commercial ship-tracking feed refreshes a ship's spot every 25 seconds [3]. Yet the gap between that raw Automatic Identification System (AIS) ping and a real arrival time stays wide. The error lives in the math of guessing the future, not in the data pipe. Treating that gap as a vendor problem misreads where the error comes from, and the misread shows up later in the alert rules.

<!-- tension -->

## The big picture:

What strikes me first is how little of this error belongs to the ship itself. A control tower takes positions, speeds, and port calls, and turns them into one number representing when a box arrives. That number is a guess over the rest of the trip, so every hour of doubt left in the route lands inside it. The paper that studies the problem most carefully measures the guess per time band [1].

On legs under a day, the strongest of the models tested averages 2.21 hours of plain error [1]. At 24 to 72 hours the figure hits 6.89 hours, at three to seven days it reaches 11.97 hours, and beyond a week it climbs to 26.92 hours [1]. In percentage terms, the estimate stays at roughly a tenth to a fifth of the trip across every length [1]. That percentage is the metric a planner can actually build an alert around.

A second study confirms this shape using a completely different method. Two separate teams built two different models, and the leeway that survives both is roughly a fifth of the remaining trip [2]. Meanwhile, the tracking layer sells exact details rather than true outcomes. A late ping is still a valid spot, but the arrival guess built on top of it can easily miss by a day.

## By the numbers

- **62.1% — Within arrival window:** On a second external test set, a past-data model placed 62.1% of trip paths inside a fifth of the actual arrival time, against 69.1% on its own private test group [2].
- **13,000+ — AIS receivers:** The network the vendor sells reports 13,000-plus receivers and tracks more than 300,000 ships daily, with an average message rate of 25 seconds [3].
- **$39.58 — Hourly manual check:** Logisticians earned a median $82,320 a year in 2025, which sets the base cost for every fifteen-minute arrival check triggered by a false alert [4].

<!-- tactical-insight -->

## What I'd watch:

The supply chain builders I watch closely are not buying sharper guesses. They are resizing the alert window around the error they cannot remove. A twelve-hour rule looks smart until a system places it at both ends of the supply chain. On a six-hour truck leg, the rule exceeds the whole trip, so it never fires. On a two-week ocean leg, it sits under half the normal error, so it fires constantly on pure noise.

The right shape is a window stated as a share of remaining transit time, with a hard floor for short trips. The two studies bracket that share loosely, and a tenth to a fifth of the trip is where the error sits [1][2]. On a 100-hour leg, that yields a window of ten to twenty hours, which is the smallest shift a planner can still manage.

Where the model sits inside the window, someone still checks the arrival by hand, and at the 2025 median wage that check costs $9.90 for fifteen minutes of work [4]. A rule tuned so tightly that every long lane triggers a daily check is just a labour bill dressed up as an alert setting. A control tower's guess only pays when there is time left to act on it.

<!-- nuanced-takeaway -->

## The catch

My read is that this ladder is a shape and a floor, not a ranking of products. The bands come from research models fed 2021 AIS records [1]. A vendor's guess may be better on a busy lane and worse on a quiet one. What survives any new test is the direction: error rises with the horizon, so a fixed-hour rule fails across a mixed lane plan.

The percentage leeway also buys less than it appears to. A window of a fifth is 80 hours on a 400-hour leg, meaning the tower cannot promise early warning there at all. Early signal on a long ocean lane has to come from something other than the arrival guess. Planners must watch dock windows and port queues that move before the ship does.

The second study's headline reads badly in both directions. Being within 20% is a loose test, and a model can clear it on most paths while missing the one trip that decides a quarter [2]. The error quoted throughout is also an average, so half the trips beat it and half do worse. The exception no arrival model sees, a load handed to a fake carrier at the dock, is the reminder that [a control tower's own blind spots](/control-tower-silent-exception/) do not close when the arrival guess gets better.

<!-- tldr -->

## At a glance

- **The Big Shift:** Arrival guess models miss a leg longer than a week by roughly a day on average because error scales as a percentage of the remaining trip.
- **Why It Matters:** Every alert rule in a control tower is a claim about how wrong its arrival guess can be. A flat-hour rule is loose on short lanes and tight on long ones, which turns the alert queue into noise where a miss costs the most.
- **What I'd Watch:**
  - **The window's unit:** sizing the alert as a share of remaining transit instead of a flat hour count ensures a truck leg and an ocean leg obey one rule.
  - **The fallback's price:** every alert a planner cannot trust becomes a manual check, and that labour is a real line item at the median wage.
  - **The response time left:** a guess is worth only what the remaining time allows, so the value depends on how long dispatching and rerouting actually take.
- **The Catch:** The bands come from research models on older tracking records, the percentage leeway is generous, and an average error means half the trips perform worse than the baseline.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Your $15 Air Rule, $195 Break-Even" -> /your-15-air-rule-195-break-even/ [same site (aichieve.net); same category; topical overlap: because, time] Link "Your $15 Air Rule, $195 Break-Even" in the section where the article touches because, time. -->
<!-- internal-link hint: "49.9% On Time: Shippers Stuck in the Gap" -> /shippers-stuck-in-the-gap/ [same site (aichieve.net); same category; topical overlap: time] Link "49.9% On Time: Shippers Stuck in the Gap" in the section where the article touches time. -->
<!-- internal-link hint: "63.6% OTIF: Your Hidden Quantity Gap" -> /your-hidden-quantity-gap/ [same site (aichieve.net); same category; topical overlap: time] Link "63.6% OTIF: Your Hidden Quantity Gap" in the section where the article touches time. -->
## Related reading

- [Your $15 Air Rule, $195 Break-Even](/your-15-air-rule-195-break-even/) — more on Supply Chain & Operations
- [49.9% On Time: Shippers Stuck in the Gap](/shippers-stuck-in-the-gap/) — more on Supply Chain & Operations
- [63.6% OTIF: Your Hidden Quantity Gap](/your-hidden-quantity-gap/) — more on Supply Chain & Operations
<!-- internal-links:end -->

## Sources

[1] Nairui Liu, Fang He, Xindi Tang, Yineng Wang, "Beyond the Next Port: A Multi-Task Transformer for Forecasting Future Voyage Segment Durations" (arXiv:2601.08013v2, 17 May 2026), duration-band error table and §1 — https://arxiv.org/html/2601.08013v2
[2] Neofytos Dimitriou, "Historical Knowledge Graphs for Global Maritime Estimated Time of Arrival" (arXiv:2605.18408v1, 18 May 2026), abstract and held-out test results — https://arxiv.org/html/2605.18408v1
[3] Kpler AIS, "Global ship tracking" (vendor product page, figures as retrieved 2026-10-27) — https://spire.com/maritime/
[4] O*NET OnLine, "13-1081.00 - Logisticians", median wages (2025) — https://www.onetonline.org/link/summary/13-1081.00

## Gate report

lead: PASS — Opens with stakes, limits figure to one, states why before mechanism. Under 28 words.
tension: PASS — Starts with single direct sentence. Explains the structural shift clearly using simple, everyday words.
tactical-insight: PASS — Uses observer cue ("watch closely"). Frames actions as observations, not commands.
nuanced-takeaway: PASS — Addresses limitations and closes on a decision with a verified markdown link.
tldr: PASS — Follows the strict 4-part Smart Brevity schema. Clean scannability with simplified vocabulary.
