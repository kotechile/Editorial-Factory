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

Every time an agent uses a tool, its code runs inside an isolated boundary. Runtimes now build a fresh sandbox for each run, creating a fixed setup cost paid before any work begins. Because that boot time is divided across the total actions in the run, a long job absorbs the delay while a short one suffers under the weight of the initial wait. One test of four sandbox types—plain containers, hosted sandboxes, Kubernetes-run containers, and cloud virtual machines—found their startup latencies varied by up to 110x [1]. Across a million runs of 150 steps, that gap creates a 1.8x spread in total worker-hours [1].

<!-- tension -->

## The big picture:

Agents talk to these boxes over the Model Context Protocol (MCP), a standard for giving models tools. This design forces teams into a strict trade-off. You either keep a pool of sandboxes running permanently and pay for the idle memory, or you create them lazily on demand and absorb a steep delay [2]. I see this as an arithmetic problem rather than a vendor choice. A fixed setup cost divided across a handful of steps forms a heavy per-action tax, so the exact same boot routine ruins a brief run while fading into the background of a complex one.

## By the numbers

- **110x:** This is the widest latency gap across the four tested sandbox types, shrinking to about 1.9x on the longest test tier [1].
- **278 h:** One extra second of delay across one million rollouts adds a penalty of 278 worker-hours [1].
- **4,167 h:** A 100-millisecond lag per action over 150 actions adds 4,167 worker-hours across a million runs [1].
- **2.9x:** Starting the sandbox while the model writes cuts the slowest one percent of end-to-end turns by up to 2.9x [2].
- **45.9%:** Peak memory consumption drops by 45.9% when using that overlapping start instead of a warm pool [2].
- **125 ms:** Firecracker lists a target boot ceiling under 125 milliseconds for a microVM, limiting overhead to under 5 mebibytes (MiB) each [3].
- **150:** A single host can start up to 150 microVMs per second under that same open-source monitor [3].

<!-- tactical-insight -->

## What I'd watch:

The math decides how developers must price their tool boundaries, because the rules hold true no matter which vendor sits underneath. My focus is on whether teams match their setup to their expected run length, because dividing a 90-millisecond start over six actions means you pay 15 milliseconds each, while stretching a one-second start over those same six actions causes the cost to jump to about 167 milliseconds per turn [4]. The alternative to eating that delay is paying for permanent capacity across the entire fleet. One cloud provider charges per second of active run time, selling a concurrency add-on at $500 a month for 600 boxes at once [5]. The only architecture that moves both numbers is speculative scheduling. By starting the box while the model is still streaming tokens, the boot hides behind inference the system was going to perform anyway [2].

<!-- nuanced-takeaway -->

## The catch

The starkest latency numbers come with a conflict of interest. I would treat the headline spread as a directional signal rather than a final verdict, since all six authors of the preprint work for Daytona, the vendor whose product ranks first [1]. The paper is also a conference submission, not a peer-reviewed publication. The baselines require similar caution. The 125 milliseconds is a project goal from Firecracker [3]. The 90 milliseconds is a vendor claim on a product page [4]. None of these sources provides the exact action count where a warm pool becomes cheaper than an on-demand boot.

<!-- tldr -->

## At a glance

- **The Big Shift:** Agent systems now build an isolated environment per tool-using job, turning the boot process into a fixed cost paid on every run.
- **Why It Matters:** Dividing that fixed cost by the number of actions determines the per-turn penalty. A long run makes the delay irrelevant, while a short run makes it dominate the wait time.
- **What I'd Watch:** Teams must manage the trade-off between idle memory and startup delay. A warm pool wastes resources, while lazy creation punishes short tasks. Overlapping the boot with the model's generation avoids both penalties.
- **The Catch:** The widest latency spread comes from a vendor-authored preprint evaluating its own software. The underlying floor figures are published project goals rather than independent benchmarks.

## Sources
[1] Graviet, Pešut, Dagelić, Jukic and Burazin (all affiliated with Daytona), "The Rollout Infrastructure Tax in Coding-Agent Reinforcement Learning," arXiv:2607.01415v1, 1 July 2026, preprint submitted to ACM SoCC 2026. https://arxiv.org/html/2607.01415v1
[2] Zhang, Wo, Wang, Sun, Zhang, Yuan, Li, Hu, Zomaya and Yang, "SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving," arXiv:2607.23933v2, 5 August 2026. https://arxiv.org/html/2607.23933v2
[3] Firecracker, open-source microVM project page (AWS), boot and density figures. https://firecracker-microvm.github.io/
[4] Daytona, sandboxes documentation. https://www.daytona.io/docs/
[5] E2B, pricing page, list prices read 29 October 2026. https://e2b.dev/pricing
