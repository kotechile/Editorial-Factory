---
title: "Your GPU Landlord: 80% Won't Survive"
vertical: enterprise_tech_leadership
persona: eng_leader
one_big_thing: "A multi-year AI compute commitment is a credit decision, not a procurement one: Gartner's own sums say the firms renting out GPU capacity cannot earn their cost of capital, so the buyer's real exposure is the seller's balance sheet."
date: 2026-10-20
slug: your-gpu-landlord-80-wont-survive
---

<!-- lead -->
Your GPU landlord probably won't survive the decade as an independent company. Gartner now puts the number at more than 80% of neocloud providers — the firms that rent out graphics processing unit (GPU) capacity — ceasing independent operations by 2030 [1]. The firms selling rented compute need $8.5 trillion of revenue by 2030 to cover what they have promised to build, and Gartner thinks the market can pay no more than $3.6 trillion [1].

<!-- tension -->

## The big picture:

I keep coming back to one line in the Gartner note. It changes what a per-hour GPU rate is. It is not a price; it is a share of someone else's capital structure [1].

The sums are simple. Owners need $8.5 trillion of revenue by 2030. That has to cover the build they have announced, the interest on it, and a 12% return on invested capital (ROIC), Gartner's own minimum for the money [1]. Revenue that can be traced to AI data centers comes to no more than $3.6 trillion, which leaves a gap of about $4.9 trillion [1].

The clock makes it worse. Gartner does not see that 12% return before the end of 2032, and it puts more than $4 trillion of asset value at risk of a write-down through 2032 [1].

The cause sits in the hardware. Spending on AI-optimized infrastructure as a service (IaaS) grows from $66 billion in 2027 to $174 billion in 2030. Gartner's own analyst calls that too low for most sellers to earn back their spend before "the current generation of AI semiconductors is replaced" [1]. The chip turns over faster than the gear pays for itself.

Two things moved this month. On 12 October, the heads of Broadcom and Intel told a conference in Singapore that money, not silicon, is now the limit. "What I think might be the biggest constraint is capital," said Hock Tan of Broadcom [3].

Lip-Bu Tan of Intel put the rest plainly: "in the longer run, people want to see the ROI" [3]. Neither man is neutral, and both still expect demand to beat supply through 2029 [3].

Input prices are rising too. Gartner's PC data for the third quarter shows shipments down 22.4% to 55.4 million units. Memory chip costs rose fivefold from a year earlier in the second quarter, and PC makers passed the rise on [4].

Then comes the counter-current, out the day before Gartner's note. IDC (International Data Corporation) ran a study paid for by the Open Compute Project (OCP) Foundation, and lifted its 2029 forecast for OCP-recognized gear to about $800 billion [2]. That is roughly 2.7 times the $295 billion it had forecast for the same year a year earlier.

By 2030 the figure reaches $892 billion, about 51% of the gear categories studied, and about $628 billion of it is AI-related [2].

My read: those two notes describe the same rack from opposite ends. The gear is turning into a catalogue item, growing about 42% a year [2]. The business of renting it out cannot cover its cost of capital [1].

## By the numbers

- **$8.5 trillion — Revenue the owners need:** In total by 2030, to cover the build they have announced, the interest on it and a 12% ROIC [1].
- **$3.6 trillion — Revenue the market can pay:** Gartner's cap on AI revenue that can be traced to data centers, a gap of about $4.9 trillion [1].
- **80% — Operators that lose independence:** Neocloud providers Gartner expects to cease independent operations by 2030, under cost pressure and thin margins [1].
- **2.7x — Open-gear forecast:** IDC's 2029 figure for OCP-recognized equipment, up to about $800 billion from $295 billion a year earlier [2].

<!-- tactical-insight -->

## What I'd watch:

What strikes me is how little of this shows up on a rate card. A buyer comparing dollars per GPU-hour is looking at a number that already assumes the seller's financing works out [1].

- **Who holds the risk:** The note puts the write-down risk on whoever owns the gear. A long deal moves that risk to the buyer only if the deal says so, which makes the exit terms the part worth reading [1].
- **The shape of the merge:** "Cease independent operations" covers being bought as well as being shut. Which one it turns out to be decides whether a deal survives on its terms [1].
- **Open racks outside hyperscale:** OCP frames its next phase around enterprise, regional and edge sites, not just the largest campuses [2]. If that holds, the gear gets easier to buy without a rental deal.
- **Capex guidance this month:** The hyperscalers report in the last week of October. Gartner's forecast holds only if they keep spending at the current pace, so that guidance is the test [1].

<!-- nuanced-takeaway -->

## The catch

The honest limit is that this is a forecast about planned spend, not a loss anyone has booked. Gartner's words are "could be exposed to impairment," and only if sellers keep spending at the current pace [1]. Hyperscalers have other revenue that can carry a weak return for years, and the note says so [1].

I could be wrong about what this means for a buyer. Renting still hands the leftover risk to someone else, and the seller's problem is not automatically the buyer's.

Kevin Goldsmith makes that point in a recent essay on build versus buy. AI "collapsed the first cost of building, the cost of making something," he writes, while "the cost of having made it" did not move [5]. His end point is the same question turned on hardware: "what you are willing to own" [5].

The part I keep circling is the gap in horizons. An engineering leader plans two to three years out. The write-down question runs to 2032. Between those dates sits a deal, and its terms decide who eats the gap.

<!-- tldr -->

## At a glance

- **The Big Shift:** Gartner says more than 80% of neocloud providers will cease independent operations by 2030, because the owners of AI data centers need $8.5 trillion of revenue by 2030 and the market can pay no more than $3.6 trillion [1].
- **Why It Matters:** A rented GPU-hour is priced on a seller's financing, so the buyer's exposure is that seller's balance sheet as much as the rate. In the same week, IDC raised its open-gear forecast 2.7 times, which is the other way to buy the same rack [1][2].
- **What I'd Watch:** How the risk gets split between seller and buyer as the weaker operators are bought or shut [1].
  - **Exit terms:** Whether long deals start carrying the right to move or leave early, which decides who holds the gear when a seller changes hands [1].
  - **The shape of the merge:** Being bought keeps a deal alive; being shut does not [1].
  - **Open racks outside hyperscale:** Whether OCP-recognized gear keeps taking share in enterprise and regional sites, which is what makes owning the hardware a real option [2].
- **The Catch:** The impairment figure is a conditional forecast, not a booked loss, and bigger hyperscalers can carry a weak return for years [1]. Renting still moves the leftover risk off the buyer's books, which is why the call turns on what the buyer is willing to own [5].

## Sources

[1] Gartner, "Gartner Says Over $3.5 Trillion of AI Infrastructure Spending Could Be Exposed to Impairment by the End of 2030," October 14, 2026 — https://www.gartner.com/en/newsroom/press-releases/2026-10-14-gartner-says-over-us-dollars-three-and-a-half-trillion-of-artificial-intelligence-infrastructure-spending-could-be-exposed-to-impairment-by-the-end-of-2030
[2] IDC and the Open Compute Project Foundation, "IDC Raises 2029 Forecast for OCP-Recognized Infrastructure Spending by 2.7x to $800 Billion," October 13, 2026 — https://www.prnewswire.co.uk/news-releases/idc-raises-2029-forecast-for-ocp-recognized-infrastructure-spending-by-2-7x-to-800-billion-302906503.html
[3] Quartz, "Intel and Broadcom CEOs warn capital may bottleneck AI growth," October 12, 2026 — https://qz.com/intel-broadcom-ceos-capital-constraint-ai-growth-101226
[4] Gartner, "Gartner Says Worldwide PC Shipments Declined 22.4% in Third Quarter of 2026 As Component Cost Inflation Raised ASPs," October 12, 2026 — https://www.gartner.com/en/newsroom/press-releases/2026-10-12-gartner-says-worldwide-pc-shipments-declined-22-point-4-percent-in-third-quarter-of-2026-as-component-cost-inflation-raised-asps
[5] Kevin Goldsmith, "Build vs Buy When Building Just Got Cheap," October 16, 2026 — https://kevingoldsmith.substack.com/p/build-vs-buy-when-building-just-got
