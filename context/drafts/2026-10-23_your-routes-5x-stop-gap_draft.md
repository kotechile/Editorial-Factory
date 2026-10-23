---
title: "Your Route's 5x Stop Gap: Density Beats Routing"
vertical: last_mile_routing_fleet_carbon
persona: supply_chain_architect
one_big_thing: "A routing engine can only re-order the stops it is handed: the routes in the published Amazon last-mile corpus carry 50 to 250 stops, a 5x spread, and the measured route-time lever is driver knowledge of dense districts (35.8%), which is a network-design decision no router touches."
date: 2026-10-23
slug: your-routes-5x-stop-gap
archetype: evergreen
evergreen: true
meta_title: "Your Route's 5x Stop Gap: Density Beats Routing"
meta_description: "One route in the published last-mile corpus carries 50 stops, another 250. The 5x spread is a district decision, and the measured density lever is worth 35.8% of route time."
---

<!-- lead -->
Your route's 5x stop gap sits in the one input your routing engine never gets to choose. The routes in the last-mile corpus Amazon released for its routing research challenge each carry a set of 50 to 250 stops [1], a 5x spread in what a single van-day is asked to contain. Density beats routing the moment that spread exists, because a router can only re-order the list it is handed.

<!-- tension -->

## The big picture:

My read starts with how that corpus was graded. Of the 6,112 executed routes, the challenge graders rated 2,718 high quality, 3,292 medium and 102 low [2]. The stop order a driver actually ran was not reliably the good one, and a better algorithm does not fix a stop list that was thin, spread out or split across two postcodes.

What decides the list is local knowledge of dense areas. A 2026 review in the European Transport Research Review credits Raghavan and Zhang with a finding: using drivers' experience in dense areas cut route time by 35.8% on average [3]. The same passage says what a district should look like — sized to the daily workload, tight enough to cut travel, and touching so neighbouring routes do not overlap [3].

That is a different job from routing. A router improves the order of stops inside one route. It cannot merge two half-empty districts, hand a driver the same streets for a second month, or push a stop set past a depot boundary. The 2026 article says as much itself: route quality "is not defined solely by its duration or cost", but by street layout, local rules and customers that a solver struggles to model [4].

The spread is also older than this year's software pitch. The corpus behind it covers 9,184 historical routes that Amazon drivers ran in 2018, in five United States cities [5]. The band and the grading describe real operations, not a release note.

Then there is the hour. Light truck drivers' median wage as of the 2025 survey was $21.57 an hour, or $44,860 a year [6], and 72% of them report a typical work week of more than 40 hours [7]. Doing that math honestly: a 150-stop route at 18 stops per driver-hour takes 8.33 hours, and at 22 stops per driver-hour it takes 6.82 hours. The 1.52 hours saved, at $21.57, is $32.68 a van-day.

<!-- By the numbers -->

## By the numbers

- **50 to 250 stops — What one route holds:** The band in the published corpus, across 6,112 training routes and 3,052 test routes — a 5x spread in the work one van is asked to absorb [1].
- **2,718 of 6,112 — Executed routes rated high quality:** The graders marked 2,718 high, 3,292 medium and 102 low, so the order a driver ran was often not the good one [2].
- **35.8% — Route time from dense-area knowledge:** The average cut in route time credited to drivers' experience in dense areas, as the 2026 review reports it [3].
- **$21.57 an hour — The van-hour's price:** The 2025 median wage for light truck drivers, with 72% reporting a typical week of more than 40 hours [6][7].

<!-- tactical-insight -->

## What I'd watch:

The people closest to this argument are not comparing routers. They are arguing about boundaries, and I think they are arguing about the right thing.

- **The stop count, before the order:** A route carrying 50 stops and a route carrying 250 are two different products with two different cost bases [1]. I'd want that count on the table before anyone benchmarks an algorithm.
- **The grade on the route drivers ran:** The corpus graded the order drivers actually ran [2]. A network that only counts planned miles never learns whether its good plan survived the day.
- **Local knowledge as an asset:** The 35.8% is about drivers who know their dense areas [3]. A re-draw that rotates everyone through new streets trades one gain for another, and the review's own caveat is that uncertain demand and local knowledge have to be balanced [3].
- **The habit of pricing hours:** One field note we hold has a 140-van regional parcel carrier lifting stops per driver-hour from 18 to 22 on dynamic routing, with fleet miles down 16% and 1,800 gallons a week less fuel, a 5.4x return on the licence [8]. The stop gain carried that case; the miles were the side effect.
- **The length of the week:** With 72% of light truck drivers already past 40 hours [7], an hour saved is often an hour of overtime removed rather than an hour of slack.

<!-- nuanced-takeaway -->

## The catch

I would not put the 35.8% on a slide without its owner. It is Raghavan and Zhang's finding, reported inside a 2026 review, and so far as the pages I read show, it was not measured again by the paper that cites it [3].

The corpus is 2018 work in five cities [5]. The 50-to-250 band says what those routes carried, not what a route should carry, and it is not a target to hit. A dense district that lifts stops per driver-hour can still add minutes at each door, and a route that saves an hour can hand that hour back as unpaid waiting.

The wage is a median from a survey [6], not a loaded cost. Benefits, vans, depots and managers sit outside it, which makes the $32.68 a floor on the hour's value rather than the whole bill.

What survives all of that is narrow, and I think durable: the stop set is a decision, the order is a by-product, and a district drawn badly cannot be routed back into shape.

<!-- tldr -->

## At a glance

- **The Big Shift:** The published last-mile route corpus shows each route carrying 50 to 250 stops — a 5x spread — and the measured route-time lever is driver knowledge of dense districts, at 35.8% on average, not the order of the list.
- **Why It Matters:** A routing engine re-orders the stops it is handed. If the stop set is thin, spread out or freshly rotated, the software is working on a decision it was never given, and the van-hours that decision costs are priced at $21.57 an hour.
- **What I'd Watch:** Whether networks settle districts before they shop for routers.
  - **The stop count per route:** The number of drops one van-day carries, which sets the cost base before any algorithm runs.
  - **The grade on the route drivers ran:** Whether the order they ran was a good one, which is what the corpus graded and what planned-mile reporting hides.
  - **The knowledge cost of a re-draw:** What a driver loses in local familiarity when districts move, since dense-area experience is the measured lever.
  - **The over-40 week:** The share of drivers already past 40 hours, because a saved hour lands on overtime rather than slack.
- **The Catch:** The 35.8% is a cited finding inside a 2026 review, the corpus describes 2018 routes in five cities, and the band is a description rather than a target. The wage is a median, so the $32.68 a van-day understates the true cost of the hour.

## Sources

[1] Li, He and Zhang — "Learning from Drivers to Tackle the Amazon Last Mile Routing Research Challenge" (arXiv:2205.04001v2; 6,112 training and 3,052 evaluation routes; each route contains a set of 50 to 250 stops) — https://arxiv.org/html/2205.04001v2
[2] Same source — quality grading of the executed sequences: "Out of the 6,112 actual sequences, 2,718 are of high quality, 3,292 are medium, and 102 are low" — https://arxiv.org/html/2205.04001v2
[3] European Transport Research Review (2026) — "A decision tree-based algorithm for the Amazon last-mile routing research challenge" (Raghavan & Zhang's 35.8% average route-time reduction from driver experience in dense areas; district balance, compactness and contiguity; the demand-uncertainty and familiarity trade-off) — https://link.springer.com/article/10.1186/s12544-026-00795-4
[4] Same source — "The quality of a route is not defined solely by its duration or cost, but by a multitude of additional factors related to geography, infrastructure, and customers" — https://link.springer.com/article/10.1186/s12544-026-00795-4
[5] Same source — the data set covers 9,184 historical routes performed by Amazon drivers in 2018 — https://link.springer.com/article/10.1186/s12544-026-00795-4
[6] O*NET OnLine, United States Department of Labor — 53-3033.00 Light Truck Drivers (median wages 2025: $21.57 hourly, $44,860 annual) — https://onetonline.org/link/summary/53-3033.00
[7] Same source — Duration of Typical Work Week: 72% responded "More than 40 hours" — https://onetonline.org/link/summary/53-3033.00
[8] Editorial-Factory field notes, last_mile_routing_fleet_carbon Anecdote 1 (internal) — context/growth_os/customer-truth.md
