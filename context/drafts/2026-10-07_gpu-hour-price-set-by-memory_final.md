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
Cloud provider Nebius raised its hourly rate for an Nvidia H100 chip from $3.85 to $4.50 on October 1, 2026, while pushing the newer B200 to $8.50 [3]. The chips did not get faster, but their memory now costs much more. Two days prior, TrendForce raised its 2027 forecast for high-bandwidth memory (HBM) to a 121% jump over this year's prices [1].

<!-- tension -->

## The big picture:

For a decade, the plan for artificial intelligence (AI) compute was to wait. Each new graphics processing unit (GPU) did more work per dollar, making the next version a cheaper place to run. That rule just broke, and the reason is the memory.

I keep coming back to how the two price signals line up. The memory market says prices will keep climbing. TrendForce expects 2027 HBM to cost 121% more than 2026 [1]. 

TrendForce also expects standard dynamic random-access memory (DRAM) prices to rise another 10% to 15% late this year [2]. The rental market absorbs this hit for anyone paying by the hour.

The clearest sign of the squeeze is what chipmakers might do next. Builders are thinking about putting less memory in each part, using 8-high memory stacks instead of 12-high [1]. This "saving" still costs 10% to 20% more per gigabit [1]. 

When the fix for a shortage is to use less and pay more per unit, the scarce part sets the price.

## By the numbers

- **121% — HBM price jump:** TrendForce expects the blended price of high-bandwidth memory to rise 121% next year due to tight supply and a shift to the newest HBM4 grade [1].
- **17% to 21% — Nebius rate hike:** The cloud provider raised H100 rates to $4.50, H200 to $5.40, B200 to $8.50, and B300 to $9.50 per GPU-hour on October 1, 2026 [3].
- **$8.55 vs $14.24 — B200 spread:** An independent tracker puts the median on-demand B200 at $8.55 an hour at dedicated GPU clouds and $14.24 at large hyperscalers [5].
- **10% to 15% — DRAM contracts:** TrendForce expects standard DRAM contract prices to climb another 10% to 15% in the fourth quarter [2].

<!-- tactical-insight -->

## What I'd watch:

What strikes me is that the price of the newest chip relies entirely on how much memory it holds, not how much math it does. A September index tracking rental rates put the B200 at $8.01 an hour [4]. It reported the chip now costs 21% more per unit of compute than the older H100 [4]. 

That reverses a June trend when the B200 was 18% cheaper [4]. 

I'd watch three things from here:

- **The compute-adjusted flip:** Cloud providers keeping a premium on newer, memory-heavy parts even when they are a worse buy per unit of work [4].
- **The provider spread:** The massive 67% price gap between dedicated clouds and hyperscalers for the exact same B200 [5].
- **The workaround:** Operators leaning on quantized weights (using smaller math formats to save space), smaller models, and older chips to dodge the premium.

<!-- nuanced-takeaway -->

## The catch

The 121% figure is a 2027 forecast, not a signed contract. TrendForce built it on a supply picture that could ease up [1]. 

My read is that the trend is firmer than the exact number. The markup landed while the chips stayed the same, proving the cost lives in the memory. I could be wrong about the timing, though. 

HBM sells on annual contracts, so the price hikes hit the market in lumps. Buyers with locked 2026 capacity will not feel this until they renew.

I'd also want to know what "cheaper per token" means once the hourly rate stops falling. If savings must come from serving more tokens per chip, the pressure moves entirely to software. Batching, quantization, and serving engines will matter more than the hardware roadmap.

<!-- tldr -->

## At a glance

- **The Big Shift:** Cloud providers are raising GPU rental prices because memory, not compute, is now the scarce part. Nebius lifted its hourly rates 17% to 21% on October 1, 2026, as TrendForce raised its 2027 high-bandwidth memory forecast to a 121% jump [1][3].
- **Why It Matters:** The decade-long rule that each new GPU is cheaper per unit of work has stopped holding. Teams renting compute by the hour now pay more for the newest chips, and memory-heavy parts carry a premium even when they are a worse deal.
- **What I'd Watch:**
  - **The compute-adjusted flip:** The newest chips costing more per unit of work than older ones, which flips the usual upgrade math.
  - **The provider spread:** The same B200 priced about 67% higher at hyperscalers than at dedicated clouds — the gap to shop.
  - **The workaround:** Quantized models, smaller models, and older chips used to sidestep the memory premium.
- **The Catch:** The headline memory number is a 2027 forecast, the rate hike is one provider's, and the inversion rests on a paywalled index; HBM's annual contracts mean the price hikes land unevenly.

## Sources
[1] TrendForce, "HBM Supply Constraints Persist, 2027 Price Outlook Revised Upward with Blended ASP Forecast to Rise 121% YoY," press release, 29 September 2026 (https://www.trendforce.com/presscenter/news/20260929-13255.html)
[2] TrendForce, "AI Server Demand Sustains Memory Contract Price Increases in 4Q26, While Consumer-Side Pressure Persists," press release, 30 September 2026 (https://www.trendforce.com/presscenter/news/20260930-13258.html)
[3] Nebius, "NVIDIA GPU Pricing," rate card effective 1 October 2026 (https://nebius.com/prices)
[4] SemiAnalysis GPU Pricing Index, September 2026, as reported (https://gpu-index.semianalysis.com/)
[5] getdeploying.com, "GPU Rental Price Trends," week of 5 October 2026 (https://getdeploying.com/gpu-price-trends)

## Gate report
- lead: PASS — Directly states the core news (Nebius raising rates and TrendForce forecasting a 121% memory price jump) in the opening sentence, using plain language.
- tension: PASS — Explains the structural shift from cheap compute to expensive memory with simple vocabulary and strict paragraph lengths (1-3 sentences).
- tactical-insight: PASS — Highlights what operators are doing (quantization, watching provider spreads) using clear, bulleted observations rather than prescriptive commands.
- nuanced-takeaway: PASS — Acknowledges the limitations of the data (forecasts, annual contracts) while maintaining a first-person analytical perspective ("My read is...") and simple sentence structures.
- tldr: PASS — Distinctly separated into the mandatory 4-part Smart Brevity format, accurately summarizing the article in highly readable plain English.
