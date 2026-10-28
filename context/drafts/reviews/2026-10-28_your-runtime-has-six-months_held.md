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

Your hosted code engine has six months to leave. Deno Deploy runs until about April 2027 and then shuts down, while the base code itself gets one more year of security fixes before its authors end development [1]. Four days later, Anthropic described the exact opposite trade. The firm spent five months and seven engineers building an internal version control system before moving its main repo off git [2]. One notice hands a buyer an exit date, while the other shows what an exit costs when a team must build the successor.

Both stories are about software layers. Cloudflare earns money in the network and platform above a JavaScript environment, so the base code can be given away. The AI lab faced a problem in a layer nobody sells, so the team had to make it.

<!-- tension -->

## The big picture:

Cloudflare is blunt about where the money sits. It says workerd, the code behind its Workers platform, is open source and is the exact same code it runs in live environments [3]. The transition plan merges an open-source build released in August 2026 back into the main project, making self-hosted setups a supported path [3]. Paying Deno Deploy customers receive six months of service and a push onto Workers [1]. I read the two notices as a single lesson on vendor margins. A seller that gives away a tool is telling you the tool is not the product, while a customer who bought at that layer is handed a successor belonging to the network layer above it.

Anthropic shows the other edge of the same problem. Merges into its main repo went from about 2,500 code changes a day in May 2026 to over 30,000 a day by September [2]. Main-branch history is almost 100 Gigabytes (GB), and a compressed working copy is over 25 GB [2]. Continuous Integration (CI) alone does about 25 million code checkouts a day, and fetching each one in full means the traffic passes 600 Petabytes (PB) daily [2].

Git is free, and none of that mattered until the workload changed shape and forced the firm to run several hundred internal mirrors to carry the load before it built its own custom system [2]. The fix required more than one tool, as review, code search, and access control shipped with the new system, because a software layer is a set of neighbours [2].

## By the numbers

- **30,000 a day — Merges into one repo:** up from roughly 2,500 a day in May 2026, as agent-written code swamped the checkout path [2].
- **25 million — Code checkouts a day:** the CI load that would mean more than 600 PB of git traffic daily if every job fetched the whole repo [2].
- **200 times — Smaller footprint:** processor and memory use for the new system against the several hundred mirrors it ran at peak, plus a 25% capacity win in CI [2].
- **Six months — Hosting exit:** Deno Deploy's shutdown window, against one year of monthly patches for the runtime itself [1].

<!-- tactical-insight -->

## What I'd watch:

What I am watching is how quickly a buyer can build an escape hatch when a vendor exits. Each notice represents half of a renewal conversation. The vendor owns the roadmap call, while the buyer owns the live environment question, and only one of the two sides usually has a plan for the transition.

- **Where the seller margin sits:** Cloudflare gives away the base code and sells the network, the data layer and the platform around it, meaning the shutdown costs the vendor nothing it wants to keep [3].
- **Whether the exit is open or shut:** the base code is open source and can be self-hosted, which is the very property the vendor markets as a reason to sign [3]. A closed tool that is dropped leaves customers with nothing to run.
- **How long a replacement takes:** seven engineers and five months covered the internal rewrite, review tooling, search and access control together. That pace leaned on an internal token budget the firm says no other business would realistically match [2].
- **What the notice promises:** paying Deno Deploy customers get help moving to Workers, and the JavaScript Registry (JSR) keeps operating as its infrastructure moves to Cloudflare [1][4].

The build path is where this stops being abstract, because [the math of running that layer yourself](/your-ci-bill-232-hours/) turns on how busy it is, not on the sticker price.

<!-- nuanced-takeaway -->

## The catch

Anthropic spends its closing section arguing against the obvious read of its own post. The system is not a suitable replacement for git for general use, it says, and the ideas only make sense for truly enormous repos [2]. It adds that every company facing this alone would be an inefficient use of engineering resources [2].

I see the post as a warning dressed as an engineering diary. The custom build was partly research, because the lab says it does this kind of internal work to test what its models can do [2]. That is not a budget line most leaders can copy, so the two notices describe one decision from opposite ends. The honest form of the problem is not build or buy. It is which software layer you are buying, and whether you can make a successor before the seller stops.

<!-- tldr -->

## At a glance

- **The Big Shift:** Deno's team joined Cloudflare on 2026-10-09, with Deno Deploy closing after six months and the runtime patched for one more year. Four days later, Anthropic said it had replaced git in five months because agent-written code pushed merges past 30,000 a day.
- **Why It Matters:** A vendor now competes at the layer above the tool it sells you. A purchase can be solid and still have a short future, and a custom build can be justified while remaining the wrong choice for anyone outside that scale.
- **What I'd Watch:** How the two halves of a renewal conversation line up, since the vendor owns the roadmap and the buyer owns whether a replacement exists.
  - **Layer margin:** Whether the seller profit sits above or below the thing being bought, which predicts what gets given away and what gets charged for.
  - **Exit freshness:** Whether the base code is open source and self-hostable today, which decides if a shutdown is an inconvenience or a rebuild.
  - **Replacement capacity:** How many engineers and months a successor would take, measured against the length of the notice.
- **The Catch:** Anthropic says its system suits only enormous repos, that building one per company would waste engineering effort, and that its internal token budget is unlike any other business. The build marks a ceiling, not a recipe.

## Sources
[1] Deno, "Deno is joining Cloudflare", 2026-10-09 — https://deno.com/blog/cloudflare
[2] Anthropic, "Redesigning source control at Anthropic", 2026-10-13 — https://www.anthropic.com/engineering/redesigning-source-control
[3] Cloudflare, "Deno is joining Cloudflare", 2026-10-09 — https://blog.cloudflare.com/deno-joins-cloudflare
[4] The New Stack, "Cloudflare acquires Node.js creator's startup that copied its serverless playbook", 2026-10-09 — https://thenewstack.io/cloudflare-acquires-deno-ryan-dahl
