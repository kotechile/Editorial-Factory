---
title: "Your Sandbox Boot Tax: 110x, Then Nothing"
vertical: agentic_ai
persona: ai_architect
archetype: evergreen
evergreen: true
one_big_thing: "A sandbox boot is a fixed cost paid once per run and split across its actions, so the substrate question is arithmetic: a boot divided by six actions is a tax you feel, the same boot divided by a hundred and fifty is noise — which is why the cheapest sandbox and the warm pool can both be wrong for the same run."
date: 2026-10-29
slug: your-sandbox-boot-tax-110x-then-nothing
---

<!-- lead -->
Your sandbox boot is a fixed tax charged once per trajectory. When four types of isolation—plain containers, hosted sandboxes, Kubernetes-run containers and cloud servers—were timed side by side, their startup delay varied by up to 110x [1]. That gap creates a 1.8x spread in projected worker-hours across a million runs of 150 steps [1]. The spread matters because agent runtimes now build a fresh boundary for most tool-using jobs.

The math decides the architecture. A startup penalty is a static cost divided by the number of actions an agent takes. When a run spans a hundred and fifty actions, that initial delay fades into the background. When a run spans only six actions, the boot dominates the entire turn.

<!-- tension -->

## The big picture:

Agents reach these boxes over the Model Context Protocol (MCP), where boundaries open and close per job [2]. The design forces a choice between two penalties. You can keep environments alive and pay memory for idle room, or you can start them on demand and eat a hard delay under load [2]. My reading of the trade-off is that neither path solves the cost, because both just shift the same burden into a different metric.

Where the bill lands depends on the run length. The four-way test splits a run into setup, readiness, action time and scheduling [1]. Light containers spend most of their life on actions, while heavier isolation pays its toll upfront. The same budget either buys a slow first call or a long tail later on.

## By the numbers

- **110x — Startup spread:** the widest delay gap across the four tested environments, which peaks on brief tasks and drops to a 1.9x spread on the longest test tier, where a single startup divides across many actions [1].
- **278 h — One second, a million runs:** the study prices minor delays at scale, calculating that an extra second per rollout adds 278 worker-hours across a million runs, while a 100-millisecond lag per action over 150 actions adds 4,167 worker-hours [1].
- **2.9x — Boot hidden behind the model:** triggering the sandbox while the model generates its response cuts the slowest one percent of turns by up to 2.9x, while peak memory drops 45.9% compared to maintaining a warm pool [2].
- **125 ms — the floor for a microVM:** the open-source virtual machine monitor Firecracker claims a boot time under 125 milliseconds, with less than 5 mebibytes (MiB) of overhead per instance and up to 150 starts per second per host [3].

<!-- tactical-insight -->

## What I'd watch:

Architects looking at these boundaries often skip the division. What I am watching is how teams calculate their per-action tax before they pick a vendor. I break the math into four questions.

- **What the shortest run costs:** divide the boot time by the total actions. A 90-millisecond start spread over six actions costs 15 milliseconds each. A one-second start over those same six actions adds about 167 milliseconds, eating up most of a tool turn [4].
- **Which penalty the fleet pays:** a permanent pool avoids the delay, while a fresh start avoids the idle memory. The latter appears directly on invoices, as one cloud provider bills per second of runtime and sells concurrent capacity at $500 a month for 600 boxes [5].
- **Whether the boot can hide:** speculative execution starts the sandbox once the next call becomes predictable. Letting the environment build while tokens stream is the only choice here that shrinks the tail without paying for idle room [2].
- **How many boundaries exist:** each sandbox carries its own image, health check and operational load. The engineering cost of maintaining that boundary is a separate bill entirely.

<!-- nuanced-takeaway -->

## The catch

The widest gap here carries a conflict of interest. The 110x spread was timed by engineers at Daytona, the vendor whose hosted sandbox ranks fastest in their own table [1]. I read that preprint as a useful map of the math rather than an outside test of the market. The finding that survives the bias is the shape of the tax.

The speed floors demand similar care. The 125 milliseconds is a project goal for Firecracker, and the 90 milliseconds is a vendor claim on a product page [3][4]. Neither figure acts as an outside test of a live network. No source gives a universal break-even count for when a warm pool wins. That line depends on how often your runs arrive and what your idle memory costs.

<!-- tldr -->

## At a glance

- **The Big Shift:** Agent runtimes now build an isolated boundary per tool-using job. A setup cost that used to be paid once per deployment is now paid on every run.
- **Why It Matters:** A boot divided across a handful of actions acts as a heavy tax on every turn. The same boot divided across a long run becomes background noise.
- **What I'd Watch:** whether teams calculate the boot against the specific run length it lands in, rather than relying on raw vendor speeds.
  - **The division:** boot time divided by actions per run, which dictates whether idle capacity is worth the memory cost.
  - **The penalty:** a permanent pool consumes memory, a fresh start creates delay, and a metered block of boxes turns concurrency into a monthly invoice.
  - **The overlap:** building the sandbox while the model streams tokens, the only architectural choice that reduces the tail without inflating memory.
- **The Catch:** the headline latency spread comes from a vendor-authored preprint that ranks its own product first, and the baseline boot figures are design goals rather than independent network tests.

## Sources
[1] Graviet, Pešut, Dagelić, Jukic and Burazin (all affiliated with Daytona), "The Rollout Infrastructure Tax in Coding-Agent Reinforcement Learning," arXiv:2607.01415v1, 1 July 2026, preprint submitted to ACM SoCC 2026. https://arxiv.org/html/2607.01415v1
[2] Zhang, Wo, Wang, Sun, Zhang, Yuan, Li, Hu, Zomaya and Yang, "SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving," arXiv:2607.23933v2, 5 August 2026. https://arxiv.org/html/2607.23933v2
[3] Firecracker, open-source microVM project page (AWS), boot and density figures. https://firecracker-microvm.github.io/
[4] Daytona, sandboxes documentation. https://www.daytona.io/docs/
[5] E2B, pricing page, list prices read 29 October 2026. https://e2b.dev/pricing
