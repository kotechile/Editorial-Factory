---
title: "Your Jira Bill Rose 10%: Memory Rose Six Times"
vertical: enterprise_build_vs_buy
persona: eng_leader
one_big_thing: "In the fortnight of 1–13 October 2026 the bought option raised its base price 3–10% and put its AI behind meters, while the inputs to the built option repriced faster and with no grandfathering — so build-vs-buy is now a choice between two cost curves, not two prices."
date: 2026-10-14
slug: flat-price-was-the-hedge
synthesis: true
sources:
  - https://blog.ovhcloud.com/en/posts/dedicated-servers-pricing-update-h2-2026/
  - https://www.atlassian.com/resources/usage
---

<!-- lead -->
Atlassian's Jira and Confluence cloud list prices rose 3% to 10% on 13 October [1][2]. Twelve days earlier, on 1 October, OVHcloud raised prices on dedicated servers that were already running, and gave the reason in its first paragraph: the memory inside costs six times what it did a year ago [3]. One of OVHcloud's own worked examples renews 41.2% higher [3].

One of those increases is the price of buying software. The other is the price of building your own.

<!-- tension -->

## The big picture:

A subscription was never only a way to bill. It was a hedge. The vendor bought the inputs and carried the risk when their cost moved. In return, the buyer got one number to budget against.

OVHcloud says as much while ending its own version of the idea. "When a customer puts two prices side by side, they are comparing two numbers, not two scopes" [7].

What strikes me is how fast the flat part shrank.

Atlassian is the clearest case. Its plan pages now list how many automated steps each tier includes, per user, per month: 400 on Standard, 750 on Premium, 1,000 on Enterprise [1]. Its AI layer, Rovo, is billed per credit, at one cent each [1]. A support request that an agent closes is billed per result [1].

Microsoft is moving the same way. From 1 December, new Microsoft 365 Copilot Business licences bought through a Cloud Solution Provider (a reseller that bills you for Microsoft) arrive with pay-as-you-go billing already on [6]. That date was pulled forward from an earlier plan for 2 November [6]. The meter is the default, not an option.

The other leg is stranger. OVHcloud spared nothing a customer already runs. From 1 October, its new rates apply to live servers at the next renewal [3]. The company says why: DDR5 memory costs six times what it did a year ago, and storage is following [3][7].

TrendForce, a memory research house, sees no relief soon. It expects memory contract prices up another 10% to 15% this quarter, and flash storage up 15% to 20% [5]. Enterprise solid-state drives are the only group where the rise is speeding up [5].

## By the numbers

- **3% to 10% — Atlassian's list rise:** from 13 October, on new purchases, renewals and upgrades. Standard and Premium plans above 5,000 seats take the top step [2].
- **41.2% — One renewal:** OVHcloud's own example. An Advance server with 128 gigabytes of memory and four solid-state drives moves from €204.99 to €289.49 at renewal [3].
- **Six times — DDR5:** OVHcloud's account of the memory chip inside its servers, a year on. It is the reason the firm gives for raising prices on machines already in service [3][7].
- **10% to 15% — Memory, next quarter:** TrendForce's forecast for the quarter now under way, with flash storage up 15% to 20% and enterprise drives faster still [5].

<!-- tactical-insight -->

## What I'd watch:

The teams closest to this are reading contracts, not price lists. Four places I'd look.

- **The allowance, not the rate.** A meter is only a price once you know the free volume behind it. Atlassian pools allowances at the company level and bills only above them [1]. The overshoot is the number to model, and nobody has data for it yet.
- **The renewal clock.** A price change lands on the date it reaches the invoice, and those dates differ. OVHcloud's rise arrives at renewal, not on 1 October [3]. Atlassian honours a quote taken before 13 October until it expires, so a signed renewal is a real gain [2].
- **The buying-power gap.** OVHcloud charges 127% more for memory on a new order, in the median case, but 20% or 40% on a machine already installed [3]. The vendor bought that chip last year. The invoice carries the old cost forward.
- **The one-off option.** Some operators read the same price list and went the other way, to their own hardware, on the argument that the memory tax is paid once [4]. I take that as an argument about risk, not about price.

What I'm watching next is the overshoot, not the list price. The first quarter of meter data settles whether October was a repricing or a re-scoping.

<!-- nuanced-takeaway -->

## The catch

The largest figure here, 41.2%, is one vendor's worked example on one setup [3]. OVHcloud applied it only to recent machines built on the newest memory, and says older generations keep their prices [3]. My read: the direction is clear and the size is not.

The Atlassian figures come from its partners, who publish the firm's price tables, because Atlassian renders its own price pages in the browser [2]. A single menu figure is one example, not a rate.

TrendForce's numbers are a forecast, and forecasts of a shortage have been wrong in both directions before [5]. None of this argues that code got dearer to write. AI did make writing it cheaper. It argues that the bills which arrive after the code ships did not come down with it.

<!-- tldr -->

## At a glance

- **The Big Shift:** Both sides of the build-vs-buy call repriced in one fortnight. Atlassian raised cloud list prices 3% to 10% on 13 October and moves its AI features to meters on 3 December [1][2]. OVHcloud raised rates on dedicated servers already in service from 1 October — 41.2% at renewal on one of its own examples [3].
- **Why It Matters:** A flat subscription was a hedge against input costs. October shrank the flat part and raised the base, while the inputs behind the alternative, memory and storage, kept climbing [3][5][7]. A licence now sits beside a build as two cost curves, and only one of them is capped by a contract.
- **What I'd Watch:** How the meters behave once billed, and how long the contracts signed before October can be stretched.
  - **The allowance behind each meter:** Atlassian pools usage allowances at the company level and bills only above them, so the overshoot is the number that matters [1].
  - **The renewal date on server contracts:** OVHcloud's rise takes effect at renewal, which spreads the hit over time rather than landing it on one day [3].
  - **The gap between new and installed hardware:** memory costs a new order 127% more in the median case and an installed machine 20% to 40% — the clearest sign that buying power, not the price list, decides this [3].
- **The Catch:** The 41.2% figure is one vendor's example on one setup, and it applies only to the newest memory generation [3]. The Atlassian figures come from partner copies of its price tables [2], and the memory numbers are forecasts [5].

<!-- internal-links -->

## Sources
[1] Atlassian, "Usage-based pricing" — https://www.atlassian.com/resources/usage
[2] Adaptavist, "Atlassian Cloud price updates, effective October 2026" (28 August 2026) — https://www.adaptavist.com/blog/atlassian-price-updates-effective-october-2026
[3] OVHcloud, "Dedicated servers: price change in the second half of 2026" (Octave Klaba) — https://blog.ovhcloud.com/en/posts/dedicated-servers-pricing-update-h2-2026/
[4] Hacker News, "Tell HN: OVH price increase for dedicated servers" (2 October 2026) — https://news.ycombinator.com/item?id=49931175
[5] TrendForce, "AI Server Demand Sustains Memory Contract Price Increases in 4Q26" (30 September 2026) — https://www.trendforce.com/presscenter/news/20260930-13258.html
[6] Microsoft, "October 2026 announcements", Partner Center (1 October 2026) — https://learn.microsoft.com/en-us/partner-center/announcements/2026-october
[7] OVHcloud, "Public Cloud: the end of all-inclusive pricing" — https://us.ovhcloud.com/resources/blog/public-cloud-the-end-of-all-inclusive-pricing/

## Gate report
lead: PASS — opens on the 13 October rise and the 1 October renewal, no preamble.
tension: PASS — '## The big picture:' names the shift (the flat price as a hedge), carries a first-person cue, and holds a '## By the numbers' section with four bullets.
tactical-insight: PASS — '## What I'd watch:' with four bullets, observer voice, no instructions to the reader.
nuanced-takeaway: PASS — '## The catch' states the sample and provenance limits and closes on substance.
tldr: PASS — four-part schema under '## At a glance' with sub-bullet definitions.
