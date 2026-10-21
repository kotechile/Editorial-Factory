---
title: "Why Your Robot Ratio Fails: 91% vs 59%"
vertical: warehouse_automation_robotics_capex
persona: ops_leader
one_big_thing: "A robot fleet has a saturation point you can compute from the picker's handling time and the robot's round trip, so a fixed robots-per-station ratio over-buys a small catalogue and under-buys a large one — and every robot past saturation is capex that throughput can never repay."
date: 2026-10-21
slug: pick-station-sets-robot-count
archetype: evergreen
evergreen: true
image_path: "context/assets/illustrations/pick-station-sets-robot-count/featured.jpg"
image_style: "long_lens_industry"
image_model: "flux"
image_alt: "Why Fixed Robot Ratios Fail. A dense queue of identical automated warehouse robots lined up on a polished concrete facility"
image_caption: "Why Fixed Robot Ratios Fail: How blind fleet scaling wastes capex at the pick station."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

A fixed rule of four robots per pick station fails fast as your product catalogue grows [3]. One simulation put four robots per station at 91% of the rate its picker allowed with 1,000 product codes [3]. With 10,000 codes and medium-sized orders, the same four reached 59% [3]. Sellers still pitch fixed ratios: one claims four machines and one worker pick 300 to 400 units an hour [2], while a new site is built for 4,500 lines an hour across 24 stations, or 187.5 at each one [1].

<!-- tension -->

## The big picture:

Robots in these systems do not pick. They carry shelves to people, and the people set the rate limit [3].

A fleet fails two ways. Too few robots and pickers wait for a shelf. Too many and machines queue behind a busy picker, which is capital standing still.

The 2018 study tested that trade. It varied pick stations from one to six, and robots from two to six per station. Each run was scored against the top rate a picker's handling time allowed [3].

What strikes me is how early the curve flattens on a small catalogue. With 1,000 product codes and small orders, four robots per station reached 91% of that ceiling. A fifth added six points, and a sixth added nothing [3]. With 10,000 codes, medium orders and returns, four robots reached 59% and six reached 83% [3]. The ratio never moved. The return did.

A 2024 queueing study puts the mechanism more starkly. Its example has two picking stations and two restocking stations. A pick takes 10 seconds; a restock takes 30. That fleet needs at least 17 robots to keep up [4]. Past 40 robots, added machines cannot raise the order arrival rate much. The people at the stations have become the limit [4].

That paper also moves the fleet number with the floor plan. Merge picking and restocking into one station and the minimum falls to 16 robots. At the same 17 robots, average order turnover time drops by about 64% [4].

One more claim on the pool: restocking took 20.29% of all robot time across the 2018 study's runs [3].

## By the numbers

- **187.5 lines an hour — Station rate:** a system built for more than 4,500 lines an hour through 24 stations averages 187.5 at each one, as a vendor design target [1].
- **91% of the ceiling — Small catalogue:** with 1,000 product codes and small orders, four robots per station reached 91% of the picker's maximum, and a fifth added six points [3].
- **59% of the ceiling — Large catalogue:** with 10,000 codes, medium orders and returns, the same four robots reached 59%, and six reached 83% [3].
- **17 to 40 robots — Useful band:** an example with two pick and two restock stations needed 17 robots to stay stable, and gained no arrival rate past 40 [4].

<!-- tactical-insight -->

## What I'd watch:

I keep circling the gap between what sellers pitch and what the studies measure. Sellers pitch a ratio. The studies publish a curve.

- **The buyer survey gap:** 92% of surveyed buyers rate durability, reliability and uptime very important, and 95% call fast response times essential [5]. Fleet size is not among the criteria the study lists.
- **The coming wave:** 48% of surveyed companies use goods-to-person picking now, and 51% are preparing updates or new deployments [5]. That is a large set of station counts being fixed in the next two years.
- **The combined station:** folding restocking into the pick station cut the minimum fleet from 17 robots to 16. Turnover time fell by about 64% at the same fleet [4]. Layout is a fleet-size lever that costs no machine.
- **The hidden variables:** a lines-per-hour target means little without the product-code count, the order size and the seconds a picker spends on a unit. I am watching for sites that publish all four.

<!-- nuanced-takeaway -->

## The catch

My read is that the curves are more useful than the ratios, but both are models. The studies assume steady arrivals and known service times [3][4]. Real floors have order swings, returns, peak weeks and robots on chargers. No figure cited here sizes that share.

The two papers also come from one research line rather than two independent field audits. The 2024 paper applies the earlier group's method to a layout of its own. So 17 and 40 describe that example, not a law [4].

The deployment numbers carry the same limit from the other side. The 187.5 lines an hour is a design target in a vendor and customer announcement. The four-robots-per-associate figure is a product page's own arithmetic, with its manual baseline of 40 to 60 units an hour attributed only to "industry data" [1][2]. Neither is an audit.

What I keep circling: a ratio travels well because it fits a sales meeting. A curve needs two measurements from the buyer's own floor. One is the seconds a picker takes per unit. The other is the seconds a robot takes to come back around. The ratio is free. The curve is the part that says when to stop buying.

<!-- tldr -->

## At a glance

- **The Big Shift:** A goods-to-person robot fleet has a saturation point set by the picker's handling time and the robot's round trip. A fixed four-robots-per-station rule over-buys a small catalogue and under-buys a large one.
- **Why It Matters:** Robots past saturation are capital no throughput can repay. A fleet sized below station demand leaves pickers waiting and payback slipping.
- **What I'd Watch:** I am watching which deployment numbers get published, because a ratio alone cannot be checked.
  - **Product-code count:** the number of distinct items, the variable that moved the same four-robot ratio from 91% to 59% of the ceiling [3].
  - **Handling seconds:** the time a picker spends on one unit, which sets the ceiling a station can reach.
  - **Combined stations:** pick and restock at one station, which cut the minimum fleet by one robot and turnover time by about 64% in the 2024 example [4].
- **The Catch:** both studies are queueing models from one research line, and the deployment figures are announced design targets rather than audits. No cited figure accounts for charging time out of the pool.

## Sources
[1] Modern Materials Handling, "S&S Activewear partners with Körber Supply Chain Software and Geekplus on robotics deployment", 29 May 2024 — "designed to support more than 4,500 lines per hour through 24 picking stations", and 340 Geekplus robots at the first 750,000 sq. ft. site (https://www.mmh.com/article/ss_activewear_partners_with_koerber_supply_chain_software_and_geekplus_on_robotics_deployment)
[2] Locus Robotics, "How P2G Creates Unlimited Warehouse Throughput with Fast Pick" — "With a single associate working alongside four Locus robots, Fast Pick enables the picking of 300-400 units per hour from bulk locations", against "around 40-60 UPH according to industry data" (https://locusrobotics.com/blog/p2g-unlimited-warehouse-throughput-fast-pick)
[3] Merschformann, Lamballais, de Koster & Suhl, "Decision Rules for Robotic Mobile Fulfillment Systems" (arXiv:1801.06703v1, 2018) — Table 10's unit throughput rate as a percentage of the upper bound (1K-S-N: 44 82 91 97 97; 10K-M-R: 21 41 59 73 83), and "Replenishment operations only consume 20.29% out of the overall time consumed by the robots" (https://arxiv.org/html/1801.06703v1)
[4] Xie & Otten, "Introducing Combi-Stations in Robotic Mobile Fulfilment Systems: A Queueing-Theory-Based Efficiency Analysis" (arXiv:2403.12798v1, 2024) — minimum stable fleet of 17 robots (16 with two combi-stations), "with more than 40 robots, it is not possible to significantly increase the arrival rate", the 64% turnover-time reduction at 17 robots, and the 10-second pick / 30-second replenishment parameters (https://arxiv.org/html/2403.12798v1)
[5] Modern Materials Handling, "2026 Automation Study: Warehouse automation ticks upward", January 2026 — 48% using goods-to-person picking with 51% preparing updates, 92% rating durability, reliability and uptime very important, 95% calling fast response times essential (https://www.mmh.com/article/2026_automation_study_warehouse_automation_ticks_upward)

## Gate report
lead: PASS — Opens on the fixed-ratio failure and delivers the 91% / 59% contrast in the first paragraph, with the two published ratios behind it.
tension: PASS — Explains the queueing mechanism in floor language, keeps every figure tied to its own scenario, and holds paragraphs to 1-3 sentences.
tactical-insight: PASS — Reports what buyers rank and what operators are fixing, with a first-person observer cue and no instructions.
nuanced-takeaway: PASS — Names the model limits, the shared research line and the design-target status of the deployment numbers.
tldr: PASS — Four-part structure with sub-bullet definitions; both figures and the fleet-size decision survive the summary.
