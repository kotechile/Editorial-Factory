---
title: "Your Sandbox Boot Tax: 110x, Then Nothing"
vertical: agentic_ai
persona: ai_architect
archetype: evergreen
evergreen: true
one_big_thing: "A sandbox boot is a fixed cost paid once per run and split across its actions, so the substrate question is arithmetic: a boot divided by six actions is a tax you feel, the same boot divided by a hundred and fifty is noise — which is why the cheapest sandbox and the warm pool can both be wrong for the same run."
date: 2026-10-29
slug: your-sandbox-boot-tax-110x-then-nothing
meta_title: "Your Sandbox Boot Tax: 110x, Then Nothing"
meta_title_source: "derived_from_title"
meta_description: "Your sandbox boot is a tax you pay on every run. Four kinds of sandbox — plain containers, hosted sandboxes, Kubernetes-run containers and cloud servers…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-sandbox-boot-tax-110x-then-nothing/featured.jpg"
image_style: "component_assembly"
image_model: "nanobanana"
image_alt: "Measuring The Sandbox Boot Tax. A steel modular block resting across multiple parallel copper blades on a concrete surface."
image_caption: "Measuring The Sandbox Boot Tax: Why container startup delays tax your agentic workflows."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

Your sandbox boot is a tax you pay on every run. Four kinds of sandbox — plain containers, hosted sandboxes, Kubernetes-run containers and cloud servers — were timed side by side [1]. Their startup delay varied by up to 110x, and the gap came to a 1.8x spread in worker-hours for a million runs of 150 steps — a gap that bites because a runtime building a box per job pays it again on every run [2]. By the time a job hits a hundred and fifty actions there is nothing left of that boot to see: at the 125-millisecond floor Firecracker publishes, the boot spread over that many steps comes to under a millisecond a step.

The authors come first. All six work for Daytona, the firm that ranks first in its own test [1]. The useful part is the math. A boot is a fixed charge, and it splits across the steps a task takes.

<!-- tension -->

## The big picture:

Agents reach these tools over the Model Context Protocol (MCP), an open standard that lets a model call outside code. The runtime builds a box, uses it, and throws it away [2]. The trade-off has two sides, and one study names both. Neither side is free.

Keep a pool warm and you pay memory for empty room; start them on demand and you eat a hard delay under load [2]. I read that as a billing dispute, not a technical flaw. Two ways to pay one debt, in different units and at different moments.

Where the bill lands also shifts. The four-way test splits a run into setup, readiness, work time and scheduling, and light containers spend most of a run on the task itself while heavier boundaries pay a steep toll up front [1]. That split means the same money can look like a slow first call or a long drag later on.

## By the numbers

- **110x — Startup spread:** the widest gap across the four kinds of sandbox timed, biggest on the shortest tasks and down to about 1.9x on the longest test tier, where one startup is spread over many actions [1].
- **278 h — One second, a million runs:** the same paper prices small drags at scale, where 100 milliseconds per action across 150 actions adds 4,167 worker-hours per million runs [1].
- **2.9x — Boot hidden behind the model:** starting the sandbox while the model still writes cuts the slowest one percent of turns by up to 2.9x, and peak memory falls 45.9% against a pool kept warm [2].
- **125 ms — the floor for a microVM:** Firecracker, an open-source virtual machine monitor, lists a boot under 125 milliseconds, under 5 mebibytes (MiB) of overhead each, and up to 150 starts a second per host [3].

<!-- tactical-insight -->

## What I'd watch:

Most of the arguments I hear stay on the vendor chart, but four questions settle it: cost per shortest run, which horn the fleet is on, whether the boot can hide, and how many lines exist.

- **What the shortest run costs:** divide the boot by the actions in that run. A 90-millisecond start over six actions is 15 milliseconds each; a one-second start over the same six is about 167 milliseconds, eleven times the other [4].
- **Which horn the fleet is on:** a pool that is never idle is the first choice, while a fresh start on every call is the second. The second one shows up on a price sheet, since one cloud bills per second of run time and sells more room at $500 a month for 600 boxes at once [5].
- **Whether the boot can hide:** start the sandbox once the model's next call is sure, and let it build while tokens stream. Only that option pays neither bill in full, pulling 2.9x off the tail [2].
- **How many lines you already run:** each sandbox is a thing with its own image, its own health check, and its own pager. Our prior note on [what a service boundary costs](/your-tool-boundary-costs-3-engineers/) prices that half of the bill, which no delay chart shows.

<!-- nuanced-takeaway -->

## The catch

The headline number carries a conflict of interest. I would not plan around it without the note attached. The 110x spread was timed by engineers at Daytona, it favours the sandbox Daytona sells, and it is a preprint sent to a conference rather than a peer-reviewed paper [1]. The math survives. The finding is that a startup rules short runs and fades across long ones, and the paper's own tiers pull the gap down to about 1.9x at the top.

The floor deserves the same caution. The 125 milliseconds is the goal Firecracker sets for itself, and the 90 milliseconds is a line on a product page [3][4]. Neither is an outside test of your code or your network. I read two papers, a project page, a vendor doc, and a price list for this piece, running no code myself.

None of those sources gives a break-even count: dividing a boot by actions hands you a tax per action. The count where a warm pool wins depends on how often runs arrive and what the idle room would cost instead. This remains a choice per service, and it moves when run length does.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "68 Loops Your Runtime Never Stopped" -> /agent-loop-bound-not-a-budget/ [same site (aichieve.net); same category; topical overlap: every, nothing] Link "68 Loops Your Runtime Never Stopped" in the section where the article touches every, nothing. -->
<!-- internal-link hint: "Your 90% Restart Monitor Proves Nothing" -> /your-90-restart-monitor-proves-nothing/ [same site (aichieve.net); same category; topical overlap: every, nothing] Link "Your 90% Restart Monitor Proves Nothing" in the section where the article touches every, nothing. -->
<!-- internal-link hint: "Your Agent's Contract Gap" -> /your-agent-contract-gap-63-unmet/ [same site (aichieve.net); same category; topical overlap: sandbox] Link "Your Agent's Contract Gap" in the section where the article touches sandbox. -->
## Related reading

- [68 Loops Your Runtime Never Stopped](/agent-loop-bound-not-a-budget/) — more on Autonomous & Agentic Workflows
- [Your 90% Restart Monitor Proves Nothing](/your-90-restart-monitor-proves-nothing/) — more on Autonomous & Agentic Workflows
- [Your Agent's Contract Gap](/your-agent-contract-gap-63-unmet/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Sandbox-backed agent runtimes start a fresh box per tool job, so a setup cost that used to be paid once is paid on every run. Keeping boundaries alive and starting them on demand are two ways of paying it.
- **Why It Matters:** A boot split across a few actions is a heavy tax on every turn, while the same boot across a long run disappears. A choice made on vendor ranks instead of run length puts the cost on the wrong side of the fleet.
- **What I'd Watch:** whether teams price the boot against the run it lands in, and whether the fix they pick hides the cost or merely moves it.
  - **The division:** boot time over actions per run, the only figure that says whether warmth is worth paying for.
  - **The horn:** a warm pool pays memory, a fresh start pays delay, and a metered block of boxes puts the first one on an invoice.
  - **The overlap:** building the sandbox while the model is still writing, the one option that shortens the tail instead of shifting it.
- **The Catch:** the headline spread comes from a vendor preprint that ranks its own product first, the boot figures are goals rather than outside tests, and no source states the action count at which a warm pool wins.

## Sources
[1] Graviet, Pešut, Dagelić, Jukic and Burazin (all affiliated with Daytona), "The Rollout Infrastructure Tax in Coding-Agent Reinforcement Learning," arXiv:2607.01415v1, 1 July 2026, preprint submitted to ACM SoCC 2026. https://arxiv.org/html/2607.01415v1
[2] Zhang, Wo, Wang, Sun, Zhang, Yuan, Li, Hu, Zomaya and Yang, "SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving," arXiv:2607.23933v2, 5 August 2026. https://arxiv.org/html/2607.23933v2
[3] Firecracker, open-source microVM project page (AWS), boot and density figures. https://firecracker-microvm.github.io/
[4] Daytona, sandboxes documentation. https://www.daytona.io/docs/
[5] E2B, pricing page, list prices read 29 October 2026. https://e2b.dev/pricing
