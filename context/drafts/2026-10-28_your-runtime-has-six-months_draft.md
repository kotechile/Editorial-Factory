---
title: "Your Runtime: The 6-Month Exit Gap"
vertical: enterprise_build_vs_buy
persona: eng_leader
one_big_thing: "October 2026 drew the build-versus-buy line for developer tooling at the layer, not the licence: Cloudflare is retiring and giving away the runtime beneath its platform margin, while Anthropic rebuilt its source-control layer because no vendor sold the shape a 30,000-merge-a-day workload needed — so the question for an engineering leader is which layer a purchase sits in, and whether the team could produce the replacement at all."
date: 2026-10-28
slug: your-runtime-has-six-months
synthesis: true
sources:
  - https://www.anthropic.com/engineering/redesigning-source-control
  - https://deno.com/blog/cloudflare
---

<!-- lead -->

Your hosted runtime has six months to leave. Deno Deploy runs until about April 2027 and then shuts down, and the Deno runtime itself gets one more year of security fixes before its own authors end development [1]. Four days later, Anthropic described the mirror image of that trade. It spent five months and seven engineers building a source-control system of its own, then moved its main repo off git [2]. One notice hands a buyer an exit date. The other shows what an exit costs when the buyer has to build it.

Both stories are about layers, not products. Cloudflare earns its money in the network and platform above a JavaScript runtime, so the runtime can be given away. Anthropic's problem sat in a layer nobody sells, so the company had to make it.

<!-- tension -->

## The big picture:

Cloudflare is blunt about where the money is. It says workerd, the runtime behind its Workers platform, "is open source. This is not a parallel implementation, it's the same code we run in production." It then adds that "being open source and giving people an escape hatch is good business" [3]. The plan merges celld, an open-source build released in August 2026, back into workerd. Self-hosting the same programming model becomes a first-class supported path [3]. Deno's paying customers get six months and a push onto Workers [1].

Put those two facts side by side and the purchase changes shape. A vendor that gives away a runtime is telling you the runtime is not the product. A customer who bought at that layer is being handed a successor that belongs to the layer above it. What strikes me is that neither notice discusses licence fees. Both are about who can make the next version of a layer, and on what timetable.

Anthropic's half of the same fortnight shows the other edge. Merges into its main repo went from about 2,500 code changes a day in May 2026 to over 30,000 a day by September [2]. Main-branch history is almost 100 gigabytes (GB), and a compressed working copy is over 25 GB [2]. Continuous integration (CI) alone does about 25 million code checkouts a day. Fetch each one in full and the traffic passes 600 petabytes (PB) daily [2].

Git is free, and none of that mattered until the workload changed shape. The company ran several hundred internal mirrors to carry the load before it built its own system [2]. The fix was not one tool either. Review, code search, access control for source code and CI changes shipped with it, because a layer is a set of neighbours [2].

## By the numbers

- **30,000 a day — Merges into one repo:** up from roughly 2,500 a day in May 2026, as agent-written code swamped the checkout path [2].
- **25 million — Code checkouts a day:** the CI load that would mean more than 600 PB of git traffic daily if every job fetched the whole repo [2].
- **200 times — Smaller footprint:** processor and memory use for the new system against the several hundred mirrors it ran at peak, plus a 25% capacity win in CI [2].
- **Six months — Hosting exit:** Deno Deploy's shutdown window, against one year of monthly patches for the runtime itself [1].

<!-- tactical-insight -->

## What I'd watch:

I keep coming back to the gap between the two notices. Each one is half of a renewal conversation. The vendor's half is a roadmap call. The buyer's half is a production question, and only one of the two sides usually has a plan for it.

- **Where the seller's margin sits:** Cloudflare gives away the runtime and sells the network, the data layer and the platform around it, so the runtime's shutdown costs it nothing it wants to keep [3].
- **Whether the exit is open or shut:** workerd is open source and can be self-hosted, which is the very property Cloudflare markets as the reason to sign. A closed runtime that is dropped leaves customers with nothing to run [3].
- **How long a replacement takes:** seven engineers and five months covered Anthropic's rewrite, its review tooling, search and access control together. That pace leaned on an internal token budget the company says no other business would realistically match [2].
- **What the notice really promises:** paying Deno Deploy customers get help moving to Workers, and the package registry keeps running as its systems move to Cloudflare [1][4].

The CI line is where this stops being abstract. [The math of running that layer yourself](/your-ci-bill-232-hours/) turns on how busy it is, not on the sticker price.

<!-- nuanced-takeaway -->

## The catch

Anthropic spends its closing section arguing against the obvious read of its own post. The system "is by no means a suitable replacement for git for general use", it says, and the ideas only make sense for truly enormous repos [2]. It adds that every company facing this alone "would be an inefficient use of engineering resources" [2].

My read is that the post is a warning dressed as an engineering diary. The build was partly research, because Anthropic says it does this kind of internal work in part to test what its models can do [2]. That is not a budget line most leaders can copy. Where I've landed is that the two notices describe one decision from opposite ends. The honest form of it is not build or buy. It is which layer you are buying, and whether you can make a successor before the seller stops.

<!-- tldr -->

## At a glance

- **The Big Shift:** Deno's team joined Cloudflare on 2026-10-09, with Deno Deploy closing after six months and the runtime patched for one more year. Four days later, Anthropic said it had replaced git in five months because agent-written code pushed merges past 30,000 a day.
- **Why It Matters:** A vendor now competes at the layer above the tool it sells you. A purchase can be solid and still have a short future, and a build can be justified and still be the wrong copy for anyone outside that scale.
- **What I'd Watch:** How the two halves of a renewal conversation line up, since the vendor owns the roadmap and the buyer owns whether a replacement exists.
  - **Layer margin:** Whether the seller's profit sits above or below the thing being bought, which predicts what gets given away and what gets charged for.
  - **Exit freshness:** Whether the runtime is open source and self-hostable today, which decides if a shutdown is an inconvenience or a rebuild.
  - **Replacement capacity:** How many engineers and months a successor would take, measured against the length of the notice.
- **The Catch:** Anthropic says its system suits only enormous repos, that building one per company would waste engineering effort, and that its internal token budget is unlike any other business. The build marks a ceiling, not a recipe.

## Sources

[1] Deno, "Deno is joining Cloudflare", 2026-10-09 — https://deno.com/blog/cloudflare
[2] Anthropic, "Redesigning source control at Anthropic", 2026-10-13 — https://www.anthropic.com/engineering/redesigning-source-control
[3] Cloudflare, "Deno is joining Cloudflare", 2026-10-09 — https://blog.cloudflare.com/deno-joins-cloudflare
[4] The New Stack, "Cloudflare acquires Node.js creator's startup that copied its serverless playbook", 2026-10-09 — https://thenewstack.io/cloudflare-acquires-deno-ryan-dahl
