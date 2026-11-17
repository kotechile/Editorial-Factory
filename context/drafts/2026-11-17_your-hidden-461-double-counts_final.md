---
title: "Your Hidden 461 Double Counts"
vertical: control_tower_exception_orchestration
kind: news
persona: supply_chain_architect
one_big_thing: "The alliance on-time figure most ocean scorecards are cut from counted 461 ship calls on two lanes at once from April 2015 onward, and fixing it reversed which alliance ranked most reliable — so the audit that pays is on the base of the count, not on the threshold you tune against it."
date: 2026-11-17
slug: your-hidden-461-double-counts
image_path: "context/assets/illustrations/your-hidden-461-double-counts/featured.jpg"
image_style: "long_lens_industry"
image_model: "flux"
image_alt: "The 461 Double Counts. Unbranded container ship reflected in dock water at a quay under low sunrise"
image_caption: "The 461 Double Counts: A hidden 461-call double count reversed which alliance ranked most reliable."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
On 7 November, Sea-Intelligence told subscribers that 461 ship calls had been counted twice in its alliance figures, and that the double count had sat hidden since April 2015 [1]. The rebuilt benchmark now puts Gemini ahead of the Mediterranean Shipping Company (MSC) for August and September [1]. Your carrier scorecard is cut from the same number, so what moved it was a counting rule, not a ship.

<!-- tldr -->
## At a glance

- **The shift:** the alliance on-time benchmark behind most ocean scorecards was rebuilt after an eleven-year double count.
- **The number:** 461 ship calls, 2.28% of alliance calls since February 2025.
- **The risk:** a ranking you acted on reversed on a margin thinner than the flaw that caused it.

<!-- tension -->
## The same ship, counted again

Issue 182 of the Global Liner Performance report came out on 28 October [2]. It put September on-time arrivals at 50.6%, after a 14.8-point fall from May's 64.5% peak, and late ships ran 6.65 days behind [2]. Ten days later, the publisher took part of it back [1].

The alliance figures, it turned out, were averages of the lane-by-lane scores. They never fixed the calls that land on two lanes at once [1]. A ship calling Shanghai, Algeciras and New York has its New York call counted on both the Asia–North America lane and the transatlantic lane [1]. That call goes into the average twice, so one ship becomes two counts. Across the networks that opened in February 2025, 461 calls were hit, or 2.28% of all alliance calls through September [1]. Scores for a single carrier or a single lane were left as they were [1].

That is the one layer a shipper cannot rebuild. You can test a single carrier's score against your own tender data. You can also argue about a run of late ships, carrier by carrier. The alliance number is an average over 34 lanes and more than 60 carriers, and only the research house holds the calls behind it [2]. A flaw inside it cannot be seen from outside.

I read the publisher's two sentences three times before I believed the reversal. The gap that set the ranking was 0.5 points, and the fix moved Gemini up 2.0 and MSC up 0.6, a 1.4-point swing this desk worked out from those two published sentences [1]. The ranking flipped on a margin smaller than the error that caused it.

## By the numbers

- **461 ship calls:** the calls counted on two lanes, 2.28% of all alliance calls since February 2025 [1].
- **0.5 points:** the gap between MSC and Gemini that the fix reversed [1].
- **6.65 days:** how far late ships ran behind in September, the second-highest for that month [2].

<!-- tactical-insight -->
## What the live feed does

Shipzil watches one carrier through four shipping platforms run by three companies [3]. Of the 162 incidents it has logged, 90% were reported by one company alone, so a lone report points at that platform's link to the carrier, not at the carrier [3]. Its own note says a platform that reports less looks better, and the totals run from 82 incidents down to 11 [3]. Its uptime figures are, in its words, "as reported by the platforms, not independently measured" [3]. Those are claims filed by the party being measured, not measurements of it. The same caveat applies to every uptime figure a platform hands your tower.

Two things on that page change how I read an exception queue. First, 47 of the 162 incidents, or 29%, had their carrier guessed from the title, because no part of the platform was tagged [3]. Second, over 90 days one platform logged 2 incidents and another logged 10, against reported uptime of 99.97% and 95.68% [3]. Buy the second feed and you will see more exceptions, then decide the network got worse. That is a reporting habit being read as a fact about freight. The party being counted is also the party filing the report, and the report is what the tower reads.

Three questions are worth asking of any count before a threshold is tuned to it. Does each shipment have one key on every lane you report it on? Is the count made by a party you also pay? Does the base of the count move without saying so? project44 shows the third done right. It says transshipment dwell, the days a box waits at a port to change ship, is measured against 5 January to 23 February, then reports six ports 12% to 59% above that line [4].

<!-- nuanced-takeaway -->
## The catch

What I find hard to square is how small the damage was. Sea-Intelligence calls the impact "minimal", with differences "barely discernible in most months", and that is fair: one ranking moved and the rest of the chart held [1]. That does not make the benchmark broken. What it does show is a call that rested on a margin thinner than a flaw nobody could see. That is a different question from whether the number was high or low. The same shape sits under every exception rate your tower pages on.

There is also a limit to what you can do from outside a vendor's pipeline. You cannot audit an average you cannot see. You can ask whether the count can be rebuilt from your own records, and whether anyone has tried. That is where a record becomes proof rather than a claim: the retention behind [your exception log](/your-exception-log-owes-5-years/) decides whether you can rebuild last quarter's count when a carrier disputes it.

## Sources

- [1] Sea-Intelligence, "Correction to October 2026 schedule reliability report", 7 November 2026 — https://www.sea-intelligence.com/press-room/419-glp-correction
- [2] Sea-Intelligence, "Global Schedule Reliability Records a Marginal Gain in September" (GLP issue 182), 28 October 2026 — https://www.sea-intelligence.com/press-room/415-global-schedule-reliability-records-a-marginal-gain-in-september
- [3] Shipzil, "Is FedEx API down?" — cross-platform monitoring snapshot, 15 November 2026, 21:35 UTC — https://shipzil.com/carrier/fedex
- [4] project44, "Hormuz Week 34: Impact on ocean freight eases, but diversions and port dwell remain above pre-conflict levels", data window 28 September – 25 October 2026 — https://www.project44.com/supply-chain-insights/hormuz-week-34-impact-on-ocean-freight-eases-but-diversions-and-port-dwell-remain-above-pre-conflict-levels/
