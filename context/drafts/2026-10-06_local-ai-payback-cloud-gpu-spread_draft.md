---
title: "Your Local AI Rig Just Tripled, and the Cloud Split Three Ways"
vertical: workstation_compute_economics
persona: infra_engineer
one_big_thing: "The build-vs-rent break-even for AI compute stopped being one number in September 2026: local hardware repriced up on the memory crunch while the cloud GPU price split into a roughly three-times provider spread, so any payback figure is only honest if it names the cloud row it used."
date: 2026-10-06
slug: local-ai-payback-cloud-gpu-spread
synthesis: true
sources:
  - https://www.tomshardware.com/pc-components/gpus/nvidias-rtx-5090-vanishes-from-online-retail-in-the-us-third-party-sellers-now-demand-as-much-as-usd9-500-for-nvidias-fastest-gpu
  - https://getdeploying.com/gpu-price-trends
---

<!-- lead -->
The graphics processing unit (GPU) that local-AI builders actually buy has gone vertical. In the two weeks to September 14, first-party stock of Nvidia's RTX 5090 "almost completely evaporated" from United States online retail, and what remains sells on third-party marketplaces for $6,500 to $9,500 — against a $1,999 launch price, Tom's Hardware's tracker reports [1]. In the same fortnight, the cloud H100 you would rent instead quoted a median of $3.39 an hour, but a hyperscaler rate of $7.89 for identical silicon [4].

<!-- tension -->

## The big picture:

The build-versus-rent decision for AI compute moved on both sides at once, and both moves trace to the same cause.

What changed on the hardware side is memory. Micron's chief executive told investors on September 30 that dynamic random-access memory (DRAM) contract prices rose by a high-teens percentage in the quarter, and that supply and demand will be "much tighter in calendar 2027 and 2028 than they were in 2026" [2]. TrendForce expects conventional DRAM contracts to climb another 10% to 15% this quarter [3]. The RTX 5090 carries 32 gigabytes of fast GDDR7 memory; when memory gets scarce, the cards built around it get scarce too.

What changed on the cloud side is that "the cloud GPU price" stopped being a single number. Across 41 providers tracked by getdeploying.com, the median on-demand H100 rents for $3.39 an hour — but hyperscalers charge about 105% more than dedicated GPU clouds for the same card, $7.89 against $3.85 [4]. For an H200, the gap widens to 141% [4]. A separate audit reading seven providers' own pricing pages on September 18 found the same class of H100 spanning $1.99 to roughly $6 an hour, and put it flatly: "a three-times spread for the same silicon is normal here" [5].

My read: because both sides trace back to the same memory squeeze, "just rent instead" is not the clean escape from local hardware inflation it looks like. Hyperscaler capacity is priced against the same scarce supply. The escape hatch, if there is one, sits at the cheap end of the rental market — the part a team never sees if it budgets against the Amazon Web Services (AWS) row.

## By the numbers

- **$6,395 to $9,500 — RTX 5090 street price:** Third-party only, against a $1,999 launch price; the June median was $4,299 and the early-September low was $5,199 [1].
- **105% — hyperscaler H100 premium:** $7.89 an hour on AWS, Azure and Google Cloud versus $3.85 on dedicated GPU clouds; for an H200 the gap is 141% [4].
- **$1.99 to ~$6 — the H100 spread:** Cheapest buyable H100 per hour up to a dedicated provider's derived rate, read from the providers' own pages on September 18 [5].
- **2028 — Micron's horizon:** The memory maker says conditions tighten further in 2027 and 2028, with more than 75% of 2027 output already committed [2].

<!-- tactical-insight -->

## What I'd watch:

The teams closest to this are re-running their build-versus-rent models, and I keep coming back to which cloud row they put in the denominator.

- **The denominator problem:** A payback figure computed against a $7.89-an-hour hyperscaler rate says "buy locally"; the same figure against a $1.99-an-hour preemptible rate says "keep renting" [4][5]. The hardware did not change — the benchmark row did.
- **The commitment ladder:** Reservations run about 28% below on-demand for a year and 49% for three; spot sits near half of on-demand but can be reclaimed at short notice [4]. That ladder moves the break-even more than any single GPU swap.
- **The egress line:** Two providers can quote the same hourly rate and still differ by five figures a year once egress and idle storage are counted [5]. I want to see more teams model that before declaring a winner on the headline rate.
- **The memory clock:** Micron says relief is not coming before 2028, and TrendForce still sees contract prices rising this quarter [2][3]. Anyone treating this autumn's GPU prices as a passing spike is betting against both suppliers.

<!-- nuanced-takeaway -->

## The catch

I could be wrong to read a routing problem where others see a plain shortage. The RTX 5090's price is partly a scalper story — Tom's Hardware found the surviving listings are third-party, several with poor seller ratings, and one Micro Center store still had cards near $4,299 [1]. That is a retail-inventory failure, not a pure cost of silicon.

The honest limit is that the two trends run on different clocks. GPU street prices can snap back when stock returns; the memory contract prices Micron and TrendForce describe sit inside multi-year supply agreements that will not. And the cloud spread is not a falling price — the same tracker shows H100 rental rates up 14% over the year [4]. Cheap capacity exists; it is not getting cheaper.

The part I keep circling is the "months to payback" number that anchors every build-versus-rent slide. It is only as good as the cloud row behind it, and that row now varies by a factor of three for the same chip. The decision did not get harder because the hardware got worse. It got harder because the reference price stopped being one thing.

<!-- tldr -->

## At a glance

- **The Big Shift:** The GPU local-AI builders buy, the RTX 5090, trades at roughly three times its launch price on third-party marketplaces, while the cloud H100 it competes against quoted a $3.39-an-hour median but a $7.89-an-hour hyperscaler rate in the same fortnight.
- **Why It Matters:** The build-versus-rent break-even now depends on which cloud row you compare against. The same hardware looks like a bargain or a waste depending on a provider choice the buying guides never name.
- **What I'd Watch:**
  - **The denominator:** Which cloud rate goes into the payback model — a hyperscaler row or a cheaper dedicated-cloud one.
  - **The commitment ladder:** Reserved pricing (about 28% off for a year) and spot pricing (near half), which move the break-even more than a GPU swap.
  - **The egress bill:** Providers with identical hourly rates that still differ by five figures a year on data transfer and idle storage.
- **The Catch:** The RTX 5090 spike is partly a retail-inventory and scalper effect that can reverse, and cloud rental rates are still up 14% year-over-year — cheap capacity exists, but it is not getting cheaper.

## Sources
[1] Tom's Hardware, "Nvidia's RTX 5090 vanishes from online retail in the US — third-party sellers now demand as much as $9,500" (2026-09-14). https://www.tomshardware.com/pc-components/gpus/nvidias-rtx-5090-vanishes-from-online-retail-in-the-us-third-party-sellers-now-demand-as-much-as-usd9-500-for-nvidias-fastest-gpu
[2] CIO, "Memory squeeze set to tighten through 2028, Micron says" (2026-10-01). https://www.cio.com/article/4229625/memory-squeeze-set-to-tighten-through-2028-micron-says.html
[3] TrendForce, "AI Server Demand Sustains Memory Contract Price Increases in 4Q26" (2026-09-30). https://www.trendforce.com/presscenter/news/20260930-13258.html
[4] getdeploying.com, "GPU Price Trends (2026)" (week of 2026-09-28). https://getdeploying.com/gpu-price-trends
[5] Deepak Gupta, "Top 7 GPU Cloud and AI Compute Providers 2026" (2026-09-18). https://guptadeepak.com/tools/top-7-gpu-cloud-ai-compute-providers-2026

<!-- linkedin -->
I've been watching the price of the GPU that local-AI teams actually buy, and the number that stopped me was the cloud row next to it.

In the two weeks to September 14, first-party stock of Nvidia's RTX 5090 almost completely evaporated from US online retail. What's left sells on third-party marketplaces for $6,395 to $9,500, against a $1,999 launch price. The cause is memory: Micron's chief said on September 30 that supply will be tighter in 2027 and 2028 than in 2026.

Here's what I keep coming back to. The cloud H100 you'd rent instead quoted a median of $3.39 an hour in the same fortnight — but hyperscalers charge about 105% more than dedicated GPU clouds for the identical card: $7.89 versus $3.85. One audit found the same class of H100 spanning $1.99 to about $6 an hour and called a three-times spread "normal."

My read: the build-versus-rent break-even isn't one number anymore. It's a routing problem. A payback figure computed against the AWS row says buy locally; the same figure against a preemptible neocloud row says keep renting. The hardware didn't change — the benchmark row did.

What I'm watching next is whether teams start naming the cloud rate behind their payback slide. Curious whether others are re-running their models against the cheaper rows.

## Gate report
lead: PASS — Concrete price collision in sentence one, no preamble.
tension: PASS — `## The big picture:` names the shared cause (memory) and who it helps/hurts; `## By the numbers` carries four sourced figures.
tactical-insight: PASS — `## What I'd watch:` reports what operators are modelling; observer cues, no commands.
nuanced-takeaway: PASS — `## The catch` states the scalper caveat and the differing timelines with a first-person cue.
tldr: PASS — Four-part Smart Brevity schema with nested sub-bullets under `## At a glance`.
