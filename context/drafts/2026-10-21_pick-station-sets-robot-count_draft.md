---
title: "Why Your Robot Ratio Fails: 91% vs 59%"
vertical: warehouse_automation_robotics_capex
persona: ops_leader
one_big_thing: "A robot fleet has a saturation point you can compute from the picker's handling time and the robot's round trip, so a fixed robots-per-station ratio over-buys a small catalogue and under-buys a large one — and every robot past saturation is capex that throughput can never repay."
date: 2026-10-21
slug: pick-station-sets-robot-count
archetype: evergreen
evergreen: true
---

<!-- lead -->

A robotic picking system announced for a 750,000-square-foot site is designed to move more than 4,500 lines an hour through 24 pick stations, which averages 187.5 lines an hour at each station [1]. One robot vendor says a single associate working with four of its machines picks 300 to 400 units an hour [2]. Set both figures beside the one published simulation that varied the ratio, and the gap opens fast: at 1,000 product codes, four robots per station reached 91% of the ceiling its pickers set; at 10,000 codes, the same four reached 59% [3].

<!-- tension -->

## The big picture:

Robots in these systems do not pick. They carry a shelf of stock to a person, wait while that person takes items off it, and carry it back [3]. The person's hands set the maximum output of the station. The robots only decide how often a fresh shelf arrives.

So the fleet has two failure modes. Too few robots and the picker stands idle, waiting for a shelf. Too many and the robots queue for a picker who is already busy, which is capex sitting still.

The 2018 study tested that trade directly. It varied stations from one to six and robots from two to six per station, and scored each run against the best rate the picker's handling time would allow [3]. The pattern held across every catalogue it tried.

What strikes me is how early the curve flattens on a small catalogue. With 1,000 product codes, four robots per station reached 91% of the ceiling, a fifth added six points, and a sixth added nothing [3]. With 10,000 codes and medium-sized orders, four robots reached 59% and six reached 83% [3]. The ratio never changed. The return did.

A 2024 queueing study puts the same mechanism in starker terms. In an example with two picking stations and two replenishment stations, where a pick takes 10 seconds and a replenishment 30, a fleet needs at least 17 robots just to keep up [4]. Past 40 robots, adding more cannot meaningfully raise the arrival rate, because the people at the stations have become the limit [4].

That paper also shows the station layout moving the fleet number. Merge picking and replenishment into one combined station and the minimum falls to 16 robots, while average order turnover time at the same 17 robots drops by about 64% [4]. Same floor, same pickers, fewer machines needed to feed them.

One more tax on the pool: replenishment consumed 20.29% of overall robot time across that study's runs [3]. Robots spend a fifth of their day hauling stock back out, not just serving pickers.

## By the numbers

- **187.5 lines an hour — station rate:** a PopPick system designed for more than 4,500 lines an hour through 24 picking stations averages 187.5 lines at each station, a vendor design target rather than an audited figure [1].
- **91% of the ceiling — small catalogue:** with 1,000 product codes and small orders, four robots per pick station reached 91% of the maximum its picker allowed, and a fifth robot added six points [3].
- **59% of the ceiling — large catalogue:** with 10,000 product codes and medium orders, the same four robots per station reached 59%, and six reached 83% [3].
- **17 to 40 robots — the useful band:** a two-picking-station example needed 17 robots to be stable and stopped gaining arrival rate past 40 [4].

<!-- tactical-insight -->

## What I'd watch:

I have been reading these two studies beside the vendor numbers, and the thing that keeps standing out is which figure each side publishes. Vendors publish ratios. The studies publish curves.

- **The buyer survey behind the ratios:** 92% of surveyed buyers rate durability, reliability and uptime very important, and 95% call fast response times essential, up from 83% a year earlier [5]. Those are the reasons a fleet gets bought. None of them is a fleet size.
- **The adoption wave about to test it:** 48% of surveyed companies use goods-to-person picking now, and 51% are preparing updates or new deployments [5]. That is a lot of station counts being fixed in the next two years.
- **The combined station:** folding replenishment into the pick station cut the minimum stable fleet from 17 robots to 16 and turnover time by about 64% at the same fleet size [4]. Layout is a fleet-size lever that costs no robot.
- **The unpublished numbers:** a picks-per-hour figure at a station means little without the product-code count, the order size and the seconds a picker spends on a unit. I am watching for deployments that publish all four together, because that is the only version a buyer can check against their own floor.

<!-- nuanced-takeaway -->

## The catch

My read is that the curves are more useful than the ratios, but they are still models. Both studies assume steady arrivals and known service times. Real floors have order-size swings, returns, seasonal peaks and a share of robots sitting on chargers, which no cited figure here sizes.

The two studies also come from one research line, not two independent field audits. The 2024 paper applies the earlier group's approximation method to a layout of its own, so the 17-robot and 40-robot figures describe that example, not a general law [4]. Read them as the shape of the curve, never as a fleet size.

The deployment numbers have the same limit from the other side. The 187.5 lines an hour is a design target in a vendor and customer announcement, and the four-robots-per-associate claim is a product page's own arithmetic, with its manual baseline of 40 to 60 units an hour attributed only to "industry data" [1][2]. Neither is an audit.

What I keep circling back to: a ratio travels because it is easy to repeat in a sales meeting. A curve requires two measurements from the buyer's own floor, the seconds a picker takes per unit and the seconds a robot takes to come back around. The ratio is free. The curve is the part that tells you when to stop buying.

<!-- tldr -->

## At a glance

- **The Big Shift:** Robot fleets in goods-to-person warehouses have a saturation point that depends on the picker's handling time and the robot's round trip, so a fixed four-robots-per-station rule over-buys a small catalogue and under-buys a large one.
- **Why It Matters:** Every robot past saturation is capital that no throughput can repay, while a fleet sized below the station's demand leaves pickers waiting and payback slipping.
- **What I'd Watch:** I am watching which deployment numbers get published, because the ratio alone cannot be checked.
  - **Product-code count:** how many distinct items the catalogue holds, the variable that moved the same four-robot ratio from 91% to 59% of the ceiling.
  - **Station handling seconds:** the time a picker spends on one unit, which sets the ceiling a station can reach.
  - **Combined stations:** pick and replenish at one station, which cut the minimum stable fleet by one robot and turnover time by about 64% in the 2024 example.
- **The Catch:** both studies are queueing models from one research line, the deployment figures are announced design targets rather than audits, and no cited number here accounts for charging time out of the pool.

## Sources
[1] Modern Materials Handling, "S&S Activewear partners with Körber Supply Chain Software and Geekplus on robotics deployment", 29 May 2024 — "designed to support more than 4,500 lines per hour through 24 picking stations", and 340 Geekplus robots at the first 750,000 sq. ft. site (https://www.mmh.com/article/ss_activewear_partners_with_koerber_supply_chain_software_and_geekplus_on_robotics_deployment)
[2] Locus Robotics, "How P2G Creates Unlimited Warehouse Throughput with Fast Pick" — "With a single associate working alongside four Locus robots, Fast Pick enables the picking of 300-400 units per hour from bulk locations", against "around 40-60 UPH according to industry data" (https://locusrobotics.com/blog/p2g-unlimited-warehouse-throughput-fast-pick)
[3] Merschformann, Lamballais, de Koster & Suhl, "Decision Rules for Robotic Mobile Fulfillment Systems" (arXiv:1801.06703v1, 2018) — Table 10's unit throughput rate as a percentage of the upper bound (1K-S-N: 44 82 91 97 97; 10K-M-R: 21 41 59 73 83), and "Replenishment operations only consume 20.29% out of the overall time consumed by the robots" (https://arxiv.org/html/1801.06703v1)
[4] Xie & Otten, "Introducing Combi-Stations in Robotic Mobile Fulfilment Systems: A Queueing-Theory-Based Efficiency Analysis" (arXiv:2403.12798v1, 2024) — minimum stable fleet of 17 robots (16 with two combi-stations), "with more than 40 robots, it is not possible to significantly increase the arrival rate", the 64% turnover-time reduction at 17 robots, and the 10-second pick / 30-second replenishment parameters (https://arxiv.org/html/2403.12798v1)
[5] Modern Materials Handling, "2026 Automation Study: Warehouse automation ticks upward", January 2026 — 48% using goods-to-person picking with 51% preparing updates, 92% rating durability, reliability and uptime very important, 95% calling fast response times essential (https://www.mmh.com/article/2026_automation_study_warehouse_automation_ticks_upward)
