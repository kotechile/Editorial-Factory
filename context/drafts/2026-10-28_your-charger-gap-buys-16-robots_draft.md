---
title: "Your Charger Gap Buys 16 Robots"
vertical: warehouse_automation_robotics_capex
persona: ops_leader
one_big_thing: "Battery recovery is a fleet-sizing input: the robot's loaded runtime against your shift length decides how many machines you actually need, and covering that gap with extra robots instead of a reachable charger is the most expensive way to solve it."
date: 2026-10-28
slug: your-charger-gap-buys-16-robots
archetype: evergreen
evergreen: true
---

<!-- lead -->

The robot on the quote works 6 hours 45 minutes at maximum payload. Your shift runs eight hours [1]. The 75 minutes in between decide what the capital request really buys. A fleet that cannot charge mid-shift has to cover that gap with machines. Your charger gap buys 16 robots per 100 that mostly stand still. Put a charger on the robot's route and the line disappears.

<!-- tension -->

## The big picture:

The ratios this industry trades come from model runs. One of the papers behind them says the battery was never modelled at all: "for this work we assume the battery capacity to be infinite" [7]. That is fine for studying routing and pod assignment. It is a poor basis for sizing a fleet you will pay for.

The research on this beat treats charging as a first-order variable. Zou, Xu, Gong and De Koster modelled a robotic fulfilment system with charging and swapping built as queues. Their finding is blunt: "ignoring the battery recovery will underestimate the number of robots required and the system cost for more than 15%" [3][4]. A 2024 study went further into policy. It weighed fast and slow charging against battery wear, and worked out the charger count that meets a throughput target at the lowest cost [8].

The data sheets publish the inputs those models need. A 1,350-kilogram machine runs 6 hours 45 minutes at maximum payload, and 9 hours 50 minutes empty [1]. Its charging ratio is 1:12, so ten minutes on a charger returns two hours of work [1]. A 250-kilogram model runs 13 hours loaded, against 17 hours 30 minutes empty [2]. Set the first pair against a shift and the gap is small. 75 minutes of work needs about six minutes of charging.

That is the whole difference between a charger on the route and a charger in the corner. One costs six minutes a shift. The other costs machines, because a robot that cannot top up has to be replaced by one that can.

What I keep circling is that two details on those pages matter more than the headline numbers. The summary block quotes the empty robot, and the detail block gives the loaded figure [1][2]. Payload is what shortens the day: 13 hours on the light machine, 6 hours 45 minutes on the heavy one. A fleet sized on the brochure line is sized on a robot carrying nothing.

The power bill is the smallest line in the case, which matters before anyone sells you an efficiency story. A 7.2-kilowatt Level 2 charger needs its own 40-Amp circuit under Article 625 of the National Electric Code [5]. Commercial power averaged 13.41 cents a unit in 2025 [6]. Six minutes of charging is about 0.75 kWh, or ten cents a robot-day and roughly 26 dollars a robot-year. Against a machine, that is noise. Against sixteen machines you did not need, it is the argument.

## By the numbers

- **15% — fleet under-count:** skipping battery recovery under-counts the robots required and the system cost by more than 15% [3][4].
- **4.88% — swapping's ceiling:** swapping beats plug-in charging by up to 4.88% on retrieval time, at a generally higher yearly cost [3][4].
- **3,000 cycles — pack rating:** the lowest full charging-cycle rating on both machines [1][2]. That is about 20,250 hours of loaded work: near 9.7 years on one shift, 4.9 on two, 3.3 on three.
- **7.2 kW — the charger:** a Level 2 unit with its own 40-Amp circuit puts the power near ten cents a robot-day [5][6].

<!-- tactical-insight -->

## What I'd watch:

My read is that the buyers who get this right are not smarter about batteries. They ask for a different page of the data sheet. Loaded runtime, charging ratio and cycle rating are all published, and none of the three appears on the sheet that reaches finance.

- **Which figure the vendor quotes first:** the summary block is the empty-robot number on both pages I checked [1][2]. The loaded one sits a click down, and the distance is the whole shift.
- **Whether the charger sits on the route or at the wall:** a charger the robot passes during normal work turns a 75-minute deficit into six minutes. A charger in a back corner turns it into detour time, paid for with machines.
- **What the charging policy does to throughput time:** Zou's results put the recovery policy among the variables that move throughput time, with inductive charging performing best in their tests [3]. That is a software setting and a floorplan choice, not a purchase order.
- **Whether the pack is in the schedule:** the cycle rating is the only published number that dates the asset. It is missing from most capital models on this beat, and a two-shift building owns the same robot for a far smaller share of its rated life.
- **Whether the ratio you were given counted charging at all:** the robots-per-station guidance traces back to model runs that assumed an infinite battery [7]. That does not make the ratio wrong. It means charging is an addition to it, not something it already absorbed.

If you want the sizing logic the station applies, the rule in [the pick-station model](/pick-station-sets-robot-count/) is the other half of this figure. That piece sets how many robots a station can keep busy. This one sets how many are free to be kept busy.

<!-- nuanced-takeaway -->

## The catch

My read, held loosely: the main study here is a queueing model, and its "more than 15%" comes from its own settings, not from your building. Read it as a direction and a size, not as a law you hand to a controller. The shift sum in this piece is a separate quantity that lands nearby: 75 minutes of an eight-hour shift is 15.6%. The two must never be added, averaged, or presented as one finding.

The data sheets carry their own limits. Both robots are transport machines from one vendor, not the pod-carrying robots inside a grid [1][2]. A data sheet is not a benchmark of your fleet. The cycle rating has no published statement of how deep a cycle runs, so the hours above rest on an assumption I am stating: one full cycle equals one pack's worth of loaded runtime. Change that assumption and the years move.

Two costs sit outside the sum. A charger on the route needs a 40-Amp circuit and floor space, which is site work with its own lead time [5]. And the 13.41-cent figure is a national commercial average [6]. It leaves out the demand charges and time-of-use rates a building actually pays, which barely matters here because the power line is small either way. What is not small is buying machines to cover a charging gap that a siting decision could have closed.

<!-- tldr -->

## At a glance

- **The Big Shift:** fleet sizing is moving from a ratio a vendor supplies to an uptime count an operator can check. The published duty cycle of a battery-powered robot is now specific enough to set against a shift.
- **Why It Matters:** the gap between a reachable charger and a distant one is a double-digit share of the fleet. The machines bought to cover it are capital that never earns throughput.
- **What I'd Watch:**
  - **Loaded runtime:** the run time published against maximum payload, not the empty-robot figure in the summary, because payload shortens the working day.
  - **Charging ratio:** minutes of charging needed to return an hour of runtime, which decides whether charging on the route is practical.
  - **Cycle rating:** the pack's rated full-charge count, the one published number that puts the asset's life on a calendar.
  - **Recovery policy:** whether charging is prioritised or dedicated, and where chargers sit relative to the robots' normal paths.
- **The Catch:** the fleet penalty comes from a queueing model whose settings are not yours. The cycle rating has no published depth, and a charger on the route is still site work with a circuit to install.

## Sources

[1] MiR1350 specifications, Mobile Industrial Robots — https://mobile-industrial-robots.com/products/robots/mir1350/specifications
[2] MiR250 specifications, Mobile Industrial Robots — https://mobile-industrial-robots.com/products/robots/mir250/specifications
[3] Zou, Xu, Gong & De Koster, "Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system", European Journal of Operational Research 267(2):733-753 (2018), abstract record on RePEc — https://ideas.repec.org/a/eee/ejores/v267y2018i2p733-753.html
[4] Same study, abstract record on Erasmus University Rotterdam (Pure) — https://pure.eur.nl/en/publications/evaluating-battery-charging-and-swapping-strategies-in-a-robotic-
[5] U.S. Department of Energy, Alternative Fuels Data Center, "Electricity Stations" — https://www.afdc.energy.gov/fuels/electricity-stations
[6] U.S. Energy Information Administration, "Prices and factors affecting prices" — https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php
[7] Xie, "From Simulation to Real-World Robotic Mobile Fulfillment Systems" (arXiv:1810.03643v1, 2018) — https://arxiv.org/html/1810.03643v1
[8] Chen, Gong, Chen & Wang, "Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse", European Journal of Operational Research 312(1):164-181 (2024), abstract record on RePEc — https://ideas.repec.org/a/eee/ejores/v312y2024i1p164-181.html
