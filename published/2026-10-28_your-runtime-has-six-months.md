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
meta_title: "Your Runtime: The 6-Month Exit Gap"
meta_title_source: "derived_from_title"
meta_description: "Your hosted runtime has six months to leave. Deno Deploy runs until about April 2027 and then shuts down, while the runtime itself gets one more year of…"
meta_description_source: "derived_from_lead"
---

<!-- lead -->

Your hosted runtime has six months to leave. Deno Deploy runs until about April 2027 and then shuts down, while the runtime itself gets one more year of security fixes before its authors end development [1]. Four days later, Anthropic described the opposite trade. It spent five months and seven engineers building a source-control system of its own, then moved its main repo off git [2]. One notice hands a buyer an exit date; the other shows what an exit costs when the team must build the successor. That gap between the two clocks is the whole decision.

Both stories are about layers, not products. Cloudflare competes on the network and platform above a JavaScript runtime, so the runtime can be given away. Anthropic's problem sat in a layer nobody sells, so the company had to make it.

<!-- tension -->

## The big picture:

Cloudflare is blunt about where the money is. It says workerd, the runtime behind its Workers platform, is open source and is the same code it runs in production [3]. The plan merges celld, an open-source build released in August 2026, back into workerd, so running that model on your own machines becomes a path the vendor backs [3]. Paying Deno Deploy customers get six months of service and a push onto Workers [1].

I read the two notices as one lesson about margins. A seller that gives away a tool is saying the tool is not the product. A buyer who paid at that layer is handed the next one from the layer above.

Anthropic shows the other edge of the same problem. Merges into its main repo went from about 2,500 code changes a day in May 2026 to over 30,000 a day by September [2]. Main-branch history is almost 100 gigabytes (GB), and a compressed working copy is over 25 GB [2]. Continuous integration (CI) alone does about 25 million code checkouts a day, and fetching each one in full means the traffic passes 600 petabytes (PB) daily [2].

Git is free, and none of that mattered until the workload changed shape. The firm ran several hundred in-house mirrors to carry the load before it built its own system [2]. The fix was never one tool. Review, code search and access rules shipped with it, because a layer is a set of neighbours [2].

## By the numbers

- **30,000 a day — Merges into one repo:** up from roughly 2,500 a day in May 2026, as agent-written code swamped the checkout path [2].
- **25 million — Code checkouts a day:** the CI load that would mean more than 600 PB of git traffic daily if every job fetched the whole repo [2].
- **200 times — Smaller footprint:** processor and memory use for the new system against the several hundred mirrors it ran at peak, plus a 25% capacity win in CI [2].
- **Six months — Hosting exit:** Deno Deploy's shutdown window, against one year of monthly patches for the runtime itself [1].

<!-- tactical-insight -->

## What I'd watch:

What I'm watching is how fast a buyer can build an escape hatch when a vendor exits. Each notice is half of a renewal talk. The vendor owns the roadmap call, and the buyer owns the live-system question, and only one side usually has a plan.

- **Where the seller's margin sits:** Cloudflare gives away the runtime and sells its network, its data layer and the platform around it, so the shutdown costs the vendor nothing it wants to keep [3].
- **Whether the exit is open or shut:** the runtime is open source and self-hostable, the very property the vendor sells as a reason to sign [3]. A closed tool that is dropped leaves customers with nothing to run.
- **How long a stand-in takes:** seven people and five months covered the rewrite, the review tooling, search and access rules together. That pace leaned on a token budget the lab says no other business would match [2].
- **What the notice promises:** paying Deno Deploy customers get help moving to Workers, and the package registry keeps running as its systems move to Cloudflare [1][4].

The build path is where this stops being abstract, because [the math of running that layer yourself](/your-ci-bill-232-hours/) turns on how busy it is, not on the sticker price.

<!-- nuanced-takeaway -->

## The catch

Anthropic spends its closing section arguing against the obvious read of its own post. The system "is by no means a suitable replacement for git for general use", it says, and the ideas only make sense for truly enormous repos [2]. It adds that every company facing this alone "would be an inefficient use of engineering resources" [2].

My read is that the post is a warning dressed as a diary. The build was partly research, because the lab says it does this work in part to test what its models can do [2]. That is not a budget line most leaders can copy, so the two notices describe one decision from opposite ends. The honest form of it is not build or buy. It is which layer you are buying, and whether you can make a successor before the seller stops.

<!-- tldr -->

## At a glance

- **The Big Shift:** Deno's team joined Cloudflare on 2026-10-09, with Deno Deploy closing after six months and the runtime patched for one more year. Four days later, Anthropic said it had replaced git in five months because agent-written code pushed merges past 30,000 a day.
- **Why It Matters:** A vendor now competes at the layer above the tool it sells you. A purchase can be solid and still have a short future, and a custom build can be justified while remaining the wrong choice for anyone outside that scale.
- **What I'd Watch:** How the two halves of a renewal conversation line up, since the vendor owns the roadmap and the buyer owns whether a stand-in exists.
  - **Layer margin:** Whether the seller's profit sits above or below the thing being bought, which predicts what gets given away and what gets charged for.
  - **Exit freshness:** Whether the runtime is open source and self-hostable today, which decides if a shutdown is an inconvenience or a rebuild.
  - **Replacement capacity:** How many people and months a stand-in would take, measured against the length of the notice.
- **The Catch:** Anthropic says its system suits only enormous repos, that building one per company would waste engineering effort, and that its token budget is unlike any other business. The build marks a ceiling, not a recipe.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "70% of Agent Failures" -> /agent-failures-tests-stayed-green/ [same site (aichieve.net); same category; topical overlap: runtime] Link "70% of Agent Failures" in the section where the article touches runtime. -->
<!-- internal-link hint: "OpenAI just made the agent loop a commodity" -> /openai-just-made-the-agent-loop-a-commodity/ [same site (aichieve.net); same category; topical overlap: hosted] Link "OpenAI just made the agent loop a commodity" in the section where the article touches hosted. -->
<!-- internal-link hint: "$915M Illusion: Your AI Judge Moves" -> /buying-ai-quality-when-the-score-belongs-to-the-judge/ [same site (aichieve.net); same category] Link "$915M Illusion: Your AI Judge Moves" in the section where the article touches this topic. -->
## Related reading

- [70% of Agent Failures](/agent-failures-tests-stayed-green/)
- [OpenAI just made the agent loop a commodity](/openai-just-made-the-agent-loop-a-commodity/)
- [$915M Illusion: Your AI Judge Moves](/buying-ai-quality-when-the-score-belongs-to-the-judge/)
<!-- internal-links:end -->

## Sources

[1] Deno, "Deno is joining Cloudflare", 2026-10-09 — https://deno.com/blog/cloudflare
[2] Anthropic, "Redesigning source control at Anthropic", 2026-10-13 — https://www.anthropic.com/engineering/redesigning-source-control
[3] Cloudflare, "Deno is joining Cloudflare", 2026-10-09 — https://blog.cloudflare.com/deno-joins-cloudflare
[4] The New Stack, "Cloudflare acquires Node.js creator's startup that copied its serverless playbook", 2026-10-09 — https://thenewstack.io/cloudflare-acquires-deno-ryan-dahl
