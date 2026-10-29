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
Your sandbox boot is a fixed tax paid on every run. Four types of isolation environment — plain containers, hosted sandboxes, Kubernetes-orchestrated containers and cloud virtual machines — were timed side by side to measure this delay; their startup latency varied by up to 110x, creating a 1.8x spread in projected worker-hours across one million trajectories of 150 steps [1]. The architecture question is how you divide that initial penalty. A fixed setup cost split across dozens of actions feels weightless. Yet the exact same delay ruins a short run.

<!-- tension -->

## The big picture:

Agents reach these isolated environments over the Model Context Protocol (MCP), an open standard for giving a model tools. You can provision these boxes lazily per trajectory, or you can reserve a worker permanently. One academic prototype names the dual penalty of this specific design choice: keep the boundary alive and you pay persistent memory for idle capacity, but start it on demand and you swallow a hard startup delay under multi-user load [2]. My reading of the trade-off is that neither path fixes the underlying arithmetic. Both architectural paths pay the exact same underlying bill. The four-way benchmark splits a trajectory into setup, readiness, action time and scheduling [1]. Light containers spend almost all their time on actions. Heavier isolation pays a massive penalty up front, meaning the identical money appears as a slow initial call or a long tail later on.

## By the numbers

- **110x — Startup spread:** the widest gap across the four kinds of sandbox timed, biggest on the shortest tasks and down to about 1.9x on the longest test tier, where one startup is spread over many actions [1].
- **278 h — One second, a million runs:** the same paper prices small drags at scale, where 100 milliseconds per action across 150 actions adds 4,167 worker-hours per million runs [1].
- **2.9x — Boot hidden behind the model:** starting the sandbox while the model still writes cuts the slowest one percent of turns by up to 2.9x, and peak memory falls 45.9% against a pool kept warm [2].
- **125 ms — the floor for a microVM:** Firecracker, an open-source virtual machine monitor, lists a boot under 125 milliseconds, under 5 mebibytes (MiB) of overhead each, and up to 150 starts a second per host [3].

<!-- tactical-insight -->

## What I'd watch:

Architects often debate substrate choices while ignoring the denominator; I am watching how teams calculate the cost per action on their shortest expected runs. Divide the boot by the actions. A 90-millisecond start over six actions is 15 milliseconds each; a one-second start over the same six is about 167 milliseconds, most of a tool turn [4]. The billing model forces a choice between persistent memory and fresh delays. The second path shows up immediately on a price sheet, since one cloud provider bills per second of run time and sells more room at $500 a month for 600 boxes at once [5]. Hiding the boot entirely is the only true structural fix. You can start the sandbox once the model's next call becomes predictable, letting the environment build while tokens stream, which ensures this overlapping approach pays neither bill in full.

<!-- nuanced-takeaway -->

## The catch

The widest latency gap comes with a direct conflict of interest. The 110x spread was timed by engineers at Daytona, it favours the sandbox Daytona sells, and it is a preprint sent to a conference rather than a peer-reviewed paper [1]. I treat the shape of the curve as reliable, even if the vendor ranking requires skepticism; a startup penalty dominates short runs and fades across long ones, and the paper's own tiers pull the gap down to about 1.9x at the top end. The baseline floor deserves the exact same level of caution. The 125 milliseconds is a design goal posted by the Firecracker project, and the 90 milliseconds is a vendor product page claim [3][4]. Neither figure serves as an independent test of your network. No source provides a universal break-even count where a warm pool wins, because the math changes the moment your run length does.

<!-- tldr -->

## At a glance

- **The shift:** Agent runtimes treat the sandbox as a metered boundary, so a fixed setup cost is paid on every trajectory. Keeping environments alive and starting them on demand are two ways of paying it.
- **Why it matters:** A boot split across a handful of actions is a heavy tax on every turn. The exact same boot across a long run becomes statistical noise.
- **What to watch:** Whether teams price the boot against the trajectory it lands in, and whether their chosen fix hides the cost or just moves it.
  - **The division:** Boot time divided by actions per run determines if warmth is worth buying.
  - **The billing:** A permanent pool costs memory, a fresh start costs delay, and a metered block of environments puts the first option on an invoice.
  - **The overlap:** Building the sandbox while the model writes tokens is the one option that shortens the tail.
- **The catch:** The headline spread comes from a vendor-written preprint ranking its own product first. The boot figures are design goals, and no source states the precise action count at which a warm pool wins.

## Sources
[1] Graviet, Pešut, Dagelić, Jukic and Burazin (all affiliated with Daytona), "The Rollout Infrastructure Tax in Coding-Agent Reinforcement Learning," arXiv:2607.01415v1, 1 July 2026, preprint submitted to ACM SoCC 2026. https://arxiv.org/html/2607.01415v1
[2] Zhang, Wo, Wang, Sun, Zhang, Yuan, Li, Hu, Zomaya and Yang, "SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving," arXiv:2607.23933v2, 5 August 2026. https://arxiv.org/html/2607.23933v2
[3] Firecracker, open-source microVM project page (AWS), boot and density figures. https://firecracker-microvm.github.io/
[4] Daytona, sandboxes documentation. https://www.daytona.io/docs/
[5] E2B, pricing page, list prices read 29 October 2026. https://e2b.dev/pricing
