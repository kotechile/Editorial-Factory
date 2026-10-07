---
title: "The Price of a GPU-Hour Is Now Set by Memory, Not Compute"
vertical: gpu_hardware
persona: infra_engineer
one_big_thing: "Memory, not compute, now sets the price of rented AI compute. As HBM supply stays tight and memory prices climb (TrendForce now expects 2027 HBM to cost 121% more than 2026), cloud providers are passing it straight into the hourly rate — so renting the newest accelerator no longer buys the cheapest unit of work, and the 'wait a generation for cheaper compute' rule has stopped holding."
date: 2026-10-07
slug: gpu-hour-price-set-by-memory
synthesis: true
sources:
  - https://www.trendforce.com/presscenter/news/20260929-13255.html
  - https://nebius.com/prices
---

<!-- lead -->
On October 1, 2026, the cloud provider Nebius raised its on-demand rate for an Nvidia H100 from $3.85 to $4.50 an hour [3]. It raised the newer B200 from $7.15 to $8.50. Neither chip got faster.

Two days earlier, the research house TrendForce raised its 2027 forecast for the high-bandwidth memory (HBM) inside those chips to a 121% jump over this year's prices [1]. The part did not change. Its memory did, and the bill moved.

<!-- tension -->

## The big picture:

For a decade, the plan for AI compute was to wait. Each new graphics processing unit (GPU) delivered more work per dollar, so the next generation was the cheaper place to run. That plan is now in doubt, and the reason is not the compute — it is the memory.

I keep coming back to how the two price signals line up. The memory market says prices keep climbing. TrendForce expects 2027 high-bandwidth memory to cost 121% more than 2026. It also projects that fourth-quarter contract prices for ordinary dynamic random-access memory (DRAM) will rise another 10% to 15% [1][2]. The rental market is where that lands for anyone paying by the hour.

The clearest sign of the squeeze is what chipmakers are weighing as a fix. TrendForce reports that GPU and custom-chip makers are considering putting *less* memory in each part — 8-high stacks instead of 12-high [1]. The reason is not falling demand; it is short supply and rising system costs. That "saving" still costs more per gigabit. The smaller stack carries a 10% to 20% higher price per bit [1]. When the answer to a shortage is to use less and pay more per unit, the scarce input is setting the price.

## By the numbers

- **121% — HBM price jump:** TrendForce now expects the blended price of high-bandwidth memory to rise 121% year over year in 2027, on supply constraints and a richer mix of the newest HBM4 grade [1].
- **17% to 21% — Nebius GPU rate hike:** Effective October 1, 2026, the provider raised H100 to $4.50, H200 to $5.40, B200 to $8.50 and B300 to $9.50 per GPU-hour, up roughly 17% to 21% [3].
- **$8.55 vs $14.24 — the same B200:** An independent price tracker puts the median on-demand B200 at $8.55 an hour at dedicated GPU clouds and $14.24 at the big hyperscalers, a 67% gap for the identical part [5].
- **10% to 15% — DRAM contracts:** TrendForce projects conventional DRAM contract prices to climb another 10% to 15% in the fourth quarter, with server memory still undersupplied [2].

<!-- tactical-insight -->

## What I'd watch:

What strikes me is that the price of the newest chip is now set by how much memory it carries, not by how much math it does. The index that tracks rental rates put a B200 at $8.01 an hour in late September [4]. It reported that the chip now costs 21% more per unit of compute than the older H100. That reverses June, when it was 18% cheaper, according to the SemiAnalysis GPU pricing index as reported [4].

I'd watch three things from here:

- **The compute-adjusted flip:** whether providers keep charging a premium for newer, memory-heavy parts even when they are the worse buy per unit of work [4]. The hourly sticker is no longer a proxy for value.
- **The provider spread:** the same B200 runs $8.55 an hour at dedicated clouds and $14.24 at hyperscalers [5]. That gap, not the chip, is where a budget can still be moved.
- **The workaround:** operators leaning on quantized weights, smaller models, and older silicon to dodge the premium. Whether that shows up as longer H100 bookings is the signal I'd want next.

<!-- nuanced-takeaway -->

## The catch

The 121% figure is a 2027 forecast, not a signed contract, and TrendForce built it on a supply picture that could ease [1]. The rate increase is one provider's, and the compute-adjusted inversion rests on a paywalled index that reaches the public only secondhand [4].

My read is that the direction is firmer than the magnitude. The markup landed while the chips were unchanged, which tells you the cost is in the memory, not the silicon. What I could be wrong about is timing. HBM is sold on annual contracts, so the repricing arrives in lumps. A buyer who locked in 2026 capacity may not feel this until the renewal.

I'd also want to know what "cheaper per token" even means once the hourly rate stops falling. If the savings have to come from serving more tokens per chip, the pressure moves to software — batching, quantization, and serving engines — not to the hardware roadmap.

<!-- tldr -->

## At a glance

- **The Big Shift:** Cloud providers are raising GPU rental prices because memory, not compute, is now the scarce input. Nebius lifted its hourly rates 17% to 21% on October 1, as TrendForce raised its 2027 high-bandwidth memory forecast to a 121% increase [1][3].
- **Why It Matters:** The decade-long rule that each new GPU generation is cheaper per unit of work has stopped holding. Teams renting compute by the hour now pay more for the newest silicon, and memory-heavy parts carry a premium even when they are the worse value.
- **What I'd Watch:** Whether the pricing holds and where teams can still save:
  - **The compute-adjusted flip:** the newest chips costing more per unit of work than the older ones, which flips the usual upgrade math.
  - **The provider spread:** the same B200 priced about 67% higher at hyperscalers than at dedicated clouds — the gap to shop.
  - **The workaround:** quantized models, smaller models, and older silicon used to sidestep the memory premium.
- **The Catch:** The headline memory number is a 2027 forecast, the rate hike is one provider's, and the inversion rests on a paywalled index; HBM's annual contracts mean the repricing lands unevenly.

## Sources
[1] TrendForce, "HBM Supply Constraints Persist, 2027 Price Outlook Revised Upward with Blended ASP Forecast to Rise 121% YoY," press release, 29 September 2026 (https://www.trendforce.com/presscenter/news/20260929-13255.html)
[2] TrendForce, "AI Server Demand Sustains Memory Contract Price Increases in 4Q26, While Consumer-Side Pressure Persists," press release, 30 September 2026 (https://www.trendforce.com/presscenter/news/20260930-13258.html)
[3] Nebius, "NVIDIA GPU Pricing," rate card effective 1 October 2026 (https://nebius.com/prices)
[4] SemiAnalysis GPU Pricing Index, September 2026, as reported (https://gpu-index.semianalysis.com/)
[5] getdeploying.com, "GPU Rental Price Trends," week of 5 October 2026 (https://getdeploying.com/gpu-price-trends)
