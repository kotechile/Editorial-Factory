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

Your sandbox's boot is a tax, and it is charged per run. Four kinds of sandbox — plain containers, hosted sandboxes, Kubernetes-run containers and cloud servers — were timed side by side, and their startup delay varied by up to 110x, with a 1.8x spread in worker-hours for a million runs of 150 steps [1]. That spread matters because agent runtimes now build a fresh box for most tool-using jobs [2].

Read the authors before the figure. All six work for Daytona, the hosted sandbox firm its own table ranks fastest [1]. The part I would plan around is the shape. A boot is a fixed cost, split across however many actions a run takes, and by the time a run spends a hundred and fifty actions on it there is nothing left to see.

The fresh box pays before the first line of code runs. An independent study of that boundary lists what the payment covers — image loading, file prep, namespace setup and a runtime handshake, all before work starts [2].

<!-- tension -->

## The big picture:

Agents reach those boxes over the Model Context Protocol (MCP), an open standard for giving a model a set of tools, and the boxes are made and thrown away per job [2]. The trade has two horns, and one study names both. Keep sandboxes alive and you pay memory for idle room. Start them on demand and you eat a hard startup delay under multi-user load [2]. What strikes me here is that neither is a pricing decision. They are two ways to pay one bill, in different units and at different moments.

Where the bill lands also shifts. The four-way test splits a run into setup, readiness, action time and scheduling, and finds that light containers spend most of a run on actions while heavier isolation and scheduling pay up front [1]. That split is the useful part of the paper, more than its ranking of vendors. It says the same money can appear as a slow first call or as a long tail later on.

## By the numbers

- **110x — Startup spread:** the widest gap across the four kinds of sandbox timed, biggest on the shortest tasks and down to about 1.9x on the longest test tier, where one startup is spread over many actions [1].
- **278 h — One second, a million runs:** the same paper prices small drags at scale, where 100 milliseconds per action across 150 actions adds 4,167 worker-hours per million runs [1].
- **2.9x — Boot hidden behind the model:** starting the sandbox while the model still writes cuts the slowest one percent of turns by up to 2.9x, and peak memory falls 45.9% against a pool kept warm [2].
- **125 ms — the floor for a microVM:** Firecracker, an open-source virtual machine monitor, lists a boot under 125 milliseconds, under 5 mebibytes (MiB) of overhead each, and up to 150 starts a second per host [3].

<!-- tactical-insight -->

## What I'd watch:

The architects I talk to argue about sandboxes and skip the division. I read the call as four questions, in this order.

- **What the shortest run costs:** divide the boot by the actions in that run. A 90-millisecond start over six actions is 15 milliseconds each; a one-second start over the same six is about 167 milliseconds, most of a tool turn [4].
- **Which horn the fleet is on:** a pool that is never idle is the first; a fresh start on every call is the second. The second one shows up on a price sheet, since one cloud bills per second of run time and sells more room at $500 a month for 600 boxes at once [5].
- **Whether the boot can hide:** start the sandbox once the model's next call is predictable, and let it build while tokens stream. That is the only option here that pays neither bill in full, at 2.9x on the tail [2].
- **How many lines you already run:** each sandbox is a thing with its own image, its own health check and its own pager. Our earlier note on [what a service boundary costs](/your-tool-boundary-costs-3-engineers/) prices that half of the bill, which no delay chart shows.

<!-- nuanced-takeaway -->

## The catch

The best number here has a conflict of interest, and I would not quote it without the note attached. The 110x spread was timed by engineers at Daytona, it favours the sandbox Daytona sells, and it is a preprint sent to a conference rather than a published paper [1]. The finding that travels is the shape. A startup rules short runs and fades across long ones, and the paper's own tiers pull the gap down to about 1.9x at the top.

The floor deserves the same care. The 125 milliseconds is the goal Firecracker's own project posts, and the 90 milliseconds is a line on a product page, so neither is an outside test of your image or your network [3][4]. I ran no sandbox and no test for this piece. I read two papers, a project page, a vendor doc and a price list.

None of those sources gives a break-even count. Divide a boot by actions and you get a tax per action, but the count where a warm pool wins depends on how often runs arrive and what the idle room would cost instead. Where I've landed is that this is a call per service, not per firm, and it moves when run length does.

<!-- tldr -->

## At a glance

- **The Big Shift:** Agent runtimes now build an isolated sandbox per tool-using job, so a fixed setup cost that used to be paid once is paid on every run. Keeping boxes alive and starting them on demand are two ways of paying it.
- **Why It Matters:** A boot split across a handful of actions is a real tax on every turn, while the same boot across a long run disappears. A choice made on vendor rankings instead of run length puts the cost on the wrong side of the fleet.
- **What I'd Watch:** whether teams price the boot against the run it lands in, and whether the fix they pick hides the cost or merely moves it.
  - **The division:** boot time over actions per run, the only figure that says whether warmth is worth paying for.
  - **The horn:** a permanent pool pays memory, a fresh start pays delay, and a metered block of boxes makes the first one show up on an invoice.
  - **The overlap:** building the sandbox while the model is still writing, the one option that shortens the tail instead of shifting it.
- **The Catch:** the headline spread comes from a vendor-written preprint that ranks its own product first, the boot figures are design goals rather than outside tests, and no source states the action count at which a warm pool wins.

## Sources
[1] Graviet, Pešut, Dagelić, Jukic and Burazin (all affiliated with Daytona), "The Rollout Infrastructure Tax in Coding-Agent Reinforcement Learning," arXiv:2607.01415v1, 1 July 2026, preprint submitted to ACM SoCC 2026. https://arxiv.org/html/2607.01415v1
[2] Zhang, Wo, Wang, Sun, Zhang, Yuan, Li, Hu, Zomaya and Yang, "SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving," arXiv:2607.23933v2, 5 August 2026. https://arxiv.org/html/2607.23933v2
[3] Firecracker, open-source microVM project page (AWS), boot and density figures. https://firecracker-microvm.github.io/
[4] Daytona, sandboxes documentation. https://www.daytona.io/docs/
[5] E2B, pricing page, list prices read 29 October 2026. https://e2b.dev/pricing
