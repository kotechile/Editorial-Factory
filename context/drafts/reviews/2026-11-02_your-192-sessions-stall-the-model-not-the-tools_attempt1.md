---
title: "Your Queue Caps the Wrong Unit: 192 Sessions"
vertical: agentic_ai
kind: evergreen
archetype: evergreen
evergreen: true
persona: ai_architect
one_big_thing: "An agent runtime's room is used up by sessions rather than single calls, so the number an architect caps is sessions per box against a cache budget — and the evidence says the damage from over-admitting lands on the model's writing time, while the tools, where more than half the delay sits, are where time can be won back."
date: 2026-11-02
slug: your-192-sessions-stall-the-model-not-the-tools
---

<!-- lead -->

At 192 sessions running at once, the model stalls: its writing time stretches more than seventeen-fold, while the tools barely move [1]. That test ran research, coding, and science tasks, and it points at a unit most runtimes cap wrong. Room is used up by whole sessions, not by single calls, and the queue a busy fleet builds lands on the half of the loop that is hard to fix.

A request is one answer. A session is a chain of linked answers that share a prefix, wait on tools, and start up again. Engines built for chat count the first. Agents live in the second, and the count an operator watches rarely matches the thing being used.

<!-- tension -->

## The big picture:

Agent work has become session-shaped, and a live trace says so. Over fourteen days on a cluster serving coding agents, cached tokens made up 77.7% of all input tokens [2]. The same trace puts decode, the phase where the model writes rather than reads, at 78.4% of the time a request takes [2]. A session is mostly a warm cache plus a slow writer, and both are held open by the queue in front of them.

The billing layer makes that worse. Providers meter tokens per minute, and caching multiplies what a quota buys: the worked example on one provider's page turns a 2,000,000 input-token limit into 10,000,000 tokens at an 80 percent hit rate [3]. I had to reread that example: it is a queueing rule wearing a price list. A session that loses its cache slot pays twice, once in redone work and once against a cap that assumed it kept the slot.

The serving papers add that the fix exists one layer down. A scheduler that treats the whole agent program as its unit can see that a queued call is blocking the call that would have freed it. A request-level queue cannot see that at all [4]. The runtime's throughput problem is a visibility problem first, and a room problem second.

## By the numbers

Autellix is an engine that schedules agent programs rather than lone calls. It wins back 4-15x program throughput at the same delay as a mainstream engine, and 5.5x over the preemptive call-level option on mixed work [4].

On a live cluster of more than 1,000 graphics chips, packing requests while keeping shared-prefix reuse cut serving boxes by 34.7% and raised per-box request throughput by 36.8% [2]. The same scheduler used 13.0-16.8% fewer active graphics-chip hours at a 30-millisecond per-token target, and 21.1-24.6% fewer at 50 milliseconds, which prices the gap between a tight and a loose service-level objective [2].

Tool execution accounts for 45%-57% of end-to-end agent delay across research, coding and science tasks [1]. That is where a runtime can win time back without touching the model.

<!-- tactical-insight -->

## What I'd watch:

The operators closest to this problem are settling on four moves, and each one is a session-level cap in disguise. PackServe packs requests onto fewer boxes while holding a time-per-output-token target, which is session-level control described as a packing problem [2]. Autellix preempts and ranks calls using their program's own finished work, and inside a single program the paper reports cache-hit rates above 90% across input lengths [4]. PASTE starts likely tool calls while the model is still writing, cutting mean task time by 43.5%, then holds back new sessions so the returning work does not swamp the engine [1]; I would watch the holdback more than the speed-up, because the hold is what makes the gain real. One provider's advice for steady load is to grow traffic by no more than 50% every 15 minutes once it passes 1,000,000 input tokens per minute [5], which is a cap curve written by the party holding the quota.

The earlier note on [what a session costs to start](/your-sandbox-boot-tax-110x-then-nothing/) prices the other half of this bill, and it sits in the same category for a reason: boot and cache are both fixed costs a scheduler can waste.

<!-- nuanced-takeaway -->

## The catch

The headline gain comes with a tie I would not paper over. Autellix earns its 4-15x by seeing calls at the program level, and a runtime that calls a hosted endpoint one request at a time cannot see that shape at all [4]. If the engine is not yours and the gateway is not yours, the 4-15x gain is someone else's result.

The live numbers deserve the same care. PackServe's shares come from one operator's fourteen-day trace and one cluster, so 77.7% and 34.7% describe that fleet's prefix habit, not a rule anyone can adopt [2]. The 192-session result is a point on a load curve, not a published ceiling, and no source names how many sessions one graphics chip should hold. That number has to be measured against your own prefix lengths.

The last caveat is the one that changes the plan. PASTE's authors ran a test that doubled tool speed while leaving the model's queue alone, and under load the faster tools handed back more work for the model to absorb [1]. Tool-side delay is easier to attack, and attacking it with no cap on sessions just moves the queue onto the engine. The tool side is where the time is; the session cap is what makes buying it worth anything.

<!-- tldr -->

## At a glance

**The shift:** Runtimes now hold long sessions that share a cached prefix, so the limit that matters is sessions per box, not requests per minute.

**The number:** Packing those sessions while keeping prefix reuse cut a live scheduler's serving boxes by 34.7%.

**The risk:** The program-level gains need control of the call path, and faster tools without a session cap push the queue back onto the model.

## Sources
[1] Sui, Zhao, Ma, He, Wang and Xu, "PASTE: Parallelizing Tool Execution and LLM Generation for Low-Latency Agent Serving," arXiv:2603.18897v3, 16 June 2026. https://arxiv.org/html/2603.18897v3
[2] Tan, Zhu, Jiang, Zheng et al., "PackServe: SLO-Aware Request Scheduling for Agentic LLM Serving at Scale," arXiv:2609.33224v1, 27 September 2026. https://arxiv.org/html/2609.33224v1
[3] Anthropic, "Rate limits," provider documentation, effective-throughput example read 2 November 2026. https://docs.claude.com/en/api/rate-limits
[4] Luo, Shi, Cai, Zhang, Wong, Wang, Wang, Huang, Chen, Gonzalez and Stoica, "Autellix: An Efficient Serving Engine for LLM Agents as General Programs," arXiv:2502.13965v1, 19 February 2025. https://arxiv.org/html/2502.13965v1
[5] OpenAI, "Rate limits," provider documentation, usage tiers and ramp rate read 2 November 2026. https://platform.openai.com/docs/guides/rate-limits
