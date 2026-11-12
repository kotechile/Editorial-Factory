---
title: "Idle Host, Starved Tools: Your 11% Trap"
vertical: agentic_ai
kind: evergreen
archetype: evergreen
evergreen: true
persona: ai_architect
one_big_thing: "An agent request is a burst, not a steady stream — the host-side tool stage cuts into every model turn, host CPU on one traced run sits near an 11% median and rises toward 100% at stage boundaries, and a container's cores are metered in 100-millisecond slices — so a box planned from the average starves the tool stage just when it fires; the measured levers are a released-work budget instead of eager release (up to 71.4% off workflow tail time, a 3.5x gain under contention), cores pooled by role (up to 46% less tool CPU demand, 13% better worst-case tool latency), and reclaimed idle cores (95% of standalone throughput at under 3% slowdown)."
date: 2026-11-12
slug: idle-host-starved-tools-11-trap
meta_title: "Idle Host, Starved Tools: Your 11% CPU Trap"
meta_description: "An agent's tools run on the host between model calls, so CPU demand bursts from an 11% median toward saturation — and a quota set to the average throttles the burst."
image_path: "context/assets/illustrations/idle-host-starved-tools-11-trap/featured.jpg"
image_style: "cinematic_still"
image_model: "flux"
image_alt: "Idle Host, Starved Tools. A host CPU rack flares amber under a tool-stage burst while adjacent racks idle in cool blue inside a data hall"
image_caption: "Idle Host, Starved Tools: A host averaging 11% CPU is idle between tool bursts, not headroom to spare."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
A host reporting 11% average CPU is not a host with room to spare. It is idle because the agent is between tool bursts, and reading that number as headroom is the trap. On one traced coding-agent run, host use held near an 11% median through the sequential portions and rose toward nearly 100% when a workflow fired its tools [1]. The same study pairs a look across Microsoft's Azure fleet with four open-source agent frameworks, and it puts the host-side tool phase on the path that sets a request's clock [1]. A box planned from the average leaves the tools starved the moment a turn needs them, so the slowest runs become a planning decision rather than a model decision.

<!-- tldr -->

## At a glance

- **The shift:** An agent's tools run on the host between model calls, so demand arrives in bursts.
- **The number:** 11% — the median host CPU on a run that climbs toward full use [1].
- **The risk:** A quota set to that average chokes each 100-millisecond window [3].

<!-- tension -->

## The host runs half the request

An agent request is not one model call. It is a chain of model turns, with tool stages between them, and each result has to be read back into the run's state before the next turn starts [1]. That reading is host work. A scheduler parses the model's output, sends the call, waits, and folds the answer back in. A classic serving stack uses the host only to feed the graphics processing unit (GPU). In an agent runtime the central processing unit (CPU) sits on the path that sets the clock, because each task crosses between host and chip several times [1].

The load that work creates is spiky, and the shape comes from how workflows are built. Use stays low while the agent thinks, then jumps when a stage starts several builds or test runs at once. The study's contrast is a median near a ninth of the box, then a rise to almost full use [1]. Its fleet data says the same from the other side: one request makes many tool calls, and the 99th-percentile count runs far above the average [1].

I keep coming back to how mechanical the failure is. A container turns that spikiness into a hard stop. Docker documents the scheduler period as defaulting to 100,000 microseconds, and the quota as the microseconds per period a container gets before it is throttled [3]. The kernel's own account is blunter: a throttled thread waits until the next period refills the quota [4]. A quota sized to the average is spent in the first moments of a burst, and the rest of the slice goes to waiting.

## By the numbers

- **11% median host CPU:** What one traced agent run averaged between stage boundaries, before the climb toward full use [1].
- **3.5x at the tail:** The best measured effect of holding turns under a work budget instead of sending them at once [2].
- **100 milliseconds per quota window:** The default scheduler period a throttled container sits out [3].

<!-- tactical-insight -->

## What the runtime engineers are changing

I read the pooling numbers twice before I believed them. Two of the study's fixes aim at the host. Pooling cores by role — schedulers in one pool, tool work in another, pinned so a run keeps its cache — cut the tools' CPU demand by up to 46% and worst-case tool latency by 13%, while serving throughput held at 99% [1]. Reclaiming cores that would otherwise sit idle got back 95% of a co-located workload's standalone throughput, and host use rose by 30% with agent slowdown under 3% [1]. The chip side moved too: oversubscribing GPUs freed a third of them, lifted generation throughput by 82% and cut tail latency 2.5 times [1].

The scheduling half is priced apart, and it is the cheaper half to try. A tail-aware policy holds ready turns back under a bounded work budget instead of sending each one the instant it is ready. On real traces that cut workflow time at the slowest 5% by up to 71.4%, a 3.5x gain under load [2]. When the box was lightly used, it matched eager release [2]. Its controller starts the budget at 120,000 work units and moves it between 30,000 and 300,000 as queue pressure changes. What travels is the shape of a bounded budget, not the number inside it.

| Lever | What it changes | Measured effect | Where it stops working |
|---|---|---|---|
| Released-work budget | When a ready turn is sent, not how fast it runs | Up to 71.4% off tail time, 3.5x under load [2] | Needs a per-turn work estimate; drifts when that estimate is off |
| Role-pooled cores | Which core runs scheduler versus tool work | Up to 46% less tool CPU demand, 13% better worst-case tool latency [1] | Assumes the tools share the host with the scheduler |
| Reclaimed idle cores | Whether slack capacity is refilled with other work | 95% of standalone throughput, under 3% slowdown [1] | Slack is gone once workflows are spread out rather than bursty |

Google's Site Reliability Engineering (SRE) book makes the same move for retries. Its example allows a process 60 retries a minute, after which a request fails instead of retrying [5]. A cap counted in tries per task cannot do that job, because what the budget protects is the queue.

What I keep circling is how much of this sits out of the model's reach. The session side of the same box has its own roof, and this desk has already priced it — [the number an architect caps is sessions per box, not calls](/your-192-sessions-stall-the-model-not-the-tools/) — while the release policy above never touches the model at all. If two of the three wins come from the scheduler, the model upgrade on the roadmap may be buying less than the logic beside it.

<!-- nuanced-takeaway -->

## The catch

The burst contrast rests on one traced run inside a study whose fleet evidence is pooled. It shows a shape, not a spread to copy. The 71.4% figure needs a work estimate for each turn, and a runtime that guesses badly will hold turns back without moving the tail. Pooling also assumes the tool work shares the host with the scheduler. An agent whose tools are remote interfaces has moved its tail onto the network, where a core pool buys nothing and the release budget still helps. Unthrottled cores are not the answer either, since the slices that choke a burst are what stop one agent from eating a neighbour's share.

Where I've landed: the average is the wrong input for this call. The cheapest first move is the release policy, because it costs code and not more cores. The two numbers that would settle it are dull to collect — the 99th-percentile tool count per request, and the longest gap a container spends throttled inside one window. Neither sits on a standard dashboard yet, which is why the trap holds.

## Sources

- [1] Jirong Yang, Peizhe Liu, Chaojie Zhang and Jovan Stojkovic, "Architectural Implications of Agentic AI Workflows" (arXiv:2608.04458v1, 5 Aug 2026) — https://arxiv.org/html/2608.04458v1
- [2] Bochao Feng, Jianjiang Li, Haojie Wang, Lin Qiao, Yinghui Li, Yukun Yan and Jidong Zhai, "Decoupling Readiness from Release for Tail-Aware Scheduling of Agentic LLM Workflows" (arXiv:2609.10964v1, 10 Sep 2026) — https://arxiv.org/html/2609.10964v1
- [3] Docker Docs, "Resource constraints" (CPU period and quota) — https://docs.docker.com/engine/containers/resource_constraints/
- [4] Linux kernel documentation, "CFS Bandwidth Control" — https://docs.kernel.org/scheduler/sched-bwc.html
- [5] Google SRE Book, "Addressing Cascading Failures" — https://sre.google/sre-book/addressing-cascading-failures/
