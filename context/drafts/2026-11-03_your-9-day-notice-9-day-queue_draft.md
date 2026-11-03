---
title: Your 9-Day Notice, 9-Day Queue
vertical: control_tower_exception_orchestration
kind: news
persona: supply_chain_architect
one_big_thing: "A strike warning is only worth the retrieval cycle it has to work through: a nine-day notice cannot move a rail-destined box that was already nine days old when the notice arrived."
date: 2026-11-03
slug: your-9-day-notice-9-day-queue
synthesis: true
sources:
  - https://gcaptain.com/strike-threat-at-los-angeles-long-beach-ports-delayed-as-union-and-employers-extend-talks/
  - https://www.freightwaves.com/news/backlog-grows-as-35000-containers-await-rail-service-at-la-long-beach
meta_title: Your 9-Day Notice, 9-Day Queue
meta_description: A 250-person watchmen dispute at eight Los Angeles and Long Beach gates arrived with nine days of notice, in front of a rail queue already nine days deep.
---

<!-- lead -->
At 5 p.m. Pacific on Wednesday, about 250 watchmen with the International Longshore and Warehouse Union (ILWU) Local 26 could stop work at eight container terminals in Los Angeles and Long Beach [1][2]. The warning behind that walkout was dated 23 October, and it gave the trade nine days, because its first deadline was 1 November [1]. On 26 October, 10,562 import containers at those same ports had already been sitting on the terminal for at least nine days, waiting for a train [4]. The warning and the wait are the same length, so the boxes a stoppage would hurt most were already past the point where a warning helps.

<!-- tension -->

## One gate, 250 people

The Pacific Maritime Association, which bargains for the terminal employers, says the watchmen are about 2% of the ILWU workforce at the two ports. It also says they work the gates at terminals that handle 85% of Long Beach's cargo and a third of Los Angeles' [3]. Longshore crews and marine clerks hold a separate coastwide contract and are not party to this dispute, yet they are not expected to cross a Local 26 picket line [3]. My read is that this is the cleanest exception a tower will ever see on paper: dated, bounded, with a named facility list and a federal mediator at the table. The exposure still comes out at all of the flow through the eight terminals named, because a gate is one shared function rather than a share of one.

## The queue the notice leaves out

On 26 October, 35,688 import containers were waiting for on-dock rail across the two ports, and 10,562 of them had been on the terminal nine days or longer [4]. The pile is not spread evenly. At Los Angeles, 8,133 of 19,626 rail-bound boxes were past nine days, or 41.4%, against 15.1% at Long Beach [4]. Those counts are a snapshot of inventory taken from the ports' daily rail reports, not an average wait, and the report says a box in the pile is not always late [4]. One harbor, two terminals, and a wait that is nearly three times as common on one side. What the count does show is that a large block of cargo was already deeper into its stay than the notice window is long.

Volume is not the whole story. Both ports set monthly records in September, and barely half of vessel arrivals were on time at 50.6%, with the average late arrival running 6.65 days [6][7]. That is long enough that a missed rail connection is the ordinary outcome rather than the exception. Dwell followed, at 7.19 days for rail containers in September [5]. Rail is the slow half of the gateway, and it is the half a stoppage would freeze first.

## What nine days of notice buys

The 23 October notice set its first deadline for 1 November, nine days out [1]. The extension signed on 30 October moved that to 5 p.m. Pacific on 4 November, twelve days out [2]. A container that reached nine days on 26 October reaches eighteen on 4 November if nothing moves it, and a gate stoppage moves nothing. The number that decides what the notice is worth is the retrieval cycle: how long a box takes to leave the terminal and come back. A deadline says when the gate closes. It says nothing about whether the box can reach the gate by then. In September that ran 7.19 days by rail and 3.18 days by local truck [5]. A truck-destined box can be pulled and returned inside the window with room to spare. A rail-destined box cannot, and no notice changes the speed of a train.

## By the numbers

- **10,562 containers — rail queue past nine days:** of 35,688 boxes awaiting on-dock trains at Los Angeles and Long Beach on 26 October, counted as individual containers rather than as twenty-foot equivalent units [4].
- **41.4% — Los Angeles long-wait share:** 8,133 of 19,626 rail-bound containers past nine days at Los Angeles, against 15.1% at Long Beach [4].
- **7.19 days — September rail dwell:** against 3.18 days for local truck, the gap between a box a shipper can still retrieve inside the window and one it cannot [5].

<!-- tactical-insight -->

## What operators are doing

The employer association and the local are still bargaining, with the Federal Mediation and Conciliation Service helping, and both ports' chief executives urged a settlement on Friday [2]. The Masters, Mates and Pilots union has told members at affected berths to expect guidance as the deadline nears [1]. On the cargo side, C.H. Robinson's October market note named Southern California intermodal railcar shortages as a constraint and reported truck-destined containers moving close to normal [4]. I keep returning to that split: the mode with the shorter cycle is the one still moving.

The cost of a workaround has also moved in the shipper's favour. Drewry's World Container Index fell 3% to $4,429 per 40-foot container on 29 October, and Shanghai to Los Angeles fell 6% to $7,514 [8]. The National Retail Federation expects import volumes to ease from 2.25 million twenty-foot equivalent units in October to 2.0 million in November [6]. A diversion booked now is cheaper than one booked at the peak, and a queue that has stopped filling is easier to draw down. Both advantages depend on gates that stay open long enough to use them.

A stoppage also starts a billing clock that outlasts it. Demurrage and detention invoices carry their own filing and dispute windows, and [the two 30-day clocks on a late container's bill](/demurrage-invoice-30-day-clocks/) decide whether the charge that lands a month from now stands at all.

<!-- nuanced-takeaway -->

## The catch

The threat may fade before it lands. No walkout had been called, the extension runs to 4 November, and the two sides have been trading extensions since the previous agreement expired in July 2025 [2][3]. The cargo shares are the employer association's own figures, produced in a dispute about pay, and no port authority has published an independent measure of what those eight terminals carry. The queue count is a point in time, not an average wait. 

Both ports also moved record volumes in September without the congestion that broke them in 2021, which is the best argument that the system has more slack than the queue implies. 

What I cannot verify from outside is what happens to event feeds during a gate stop. A tower built on carrier events records a gate-in when a truck enters and a gate-out when it leaves, and a closed gate produces neither. Silence is the one input most exception rules were never written to escalate on, which is why the depth of the queue matters more than the countdown.

<!-- tldr -->

## At a glance

**The shift:** A 250-person dispute at eight Los Angeles and Long Beach gates now sits in front of a 35,688-box rail queue.
**The number:** 10,562 rail-bound containers were nine days old on 26 October, the original notice window.
**The risk:** Nine days of warning cannot move a box on a 7.19-day rail cycle.

## Sources

[1] Mike Schuler, "Strike Threat Looms at Eight Los Angeles, Long Beach Port Terminals," gCaptain, 2026-10-27 — https://gcaptain.com/strike-threat-looms-at-eight-los-angeles-long-beach-port-terminals/
[2] Mike Schuler, "Strike Threat at Los Angeles, Long Beach Ports Delayed as Union and Employers Extend Talks," gCaptain, 2026-10-30 — https://gcaptain.com/strike-threat-at-los-angeles-long-beach-ports-delayed-as-union-and-employers-extend-talks/
[3] Stuart Chirls, "Strike threat by port security workers at Los Angeles–Long Beach," FreightWaves, 2026-10-28 — https://www.freightwaves.com/news/strike-threat-by-port-security-workers-at-los-angeles-long-beach
[4] Stuart Chirls, "Backlog grows as 35,000 containers await rail service at LA–Long Beach," FreightWaves, 2026-10-28 — https://www.freightwaves.com/news/backlog-grows-as-35000-containers-await-rail-service-at-la-long-beach
[5] Pacific Merchant Shipping Association, "San Pedro Bay Ports Container Dwell Times for September 2026," 2026-10-15 — https://www.pmsaship.com/maritime-insights-blog/san-pedro-bay-ports-container-dwell-times-for-september-2026
[6] Mike Schuler, "Southern California Ports Shatter Cargo Records as Imports Surge," gCaptain, 2026-10-16 — https://gcaptain.com/southern-california-ports-shatter-cargo-records-as-imports-surge/
[7] Sea-Intelligence, "Global Schedule Reliability Records a Marginal Gain in September" (GLP issue 182), 2026-10-28 — https://www.sea-intelligence.com/press-room/415-global-schedule-reliability-records-a-marginal-gain-in-september
[8] ShipUniverse, "Drewry Container Rates Fall 3% to $4,429 as U.S. Trade Routes Reverse Their Rally," 2026-10-29 — https://www.shipuniverse.com/news/drewry-container-rates-fall-3-to-4429-as-u-s-trade-routes-reverse-their-rally
