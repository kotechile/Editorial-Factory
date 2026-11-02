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

At 192 live jobs running at once, the model stalls. Its writing time stretches more than seventeen-fold, while the tools barely move [1]. That test ran three kinds of agent work, and it points at a unit most engines cap wrong. Room is used up by whole jobs, not by single calls, and the queue a busy fleet builds lands on the half of the loop that is hard to fix.

A call asks for one answer. A working session is a chain of linked answers that share a prefix, wait on tools, and start up again. Because each job holds that prefix in cache for its whole life, the cap belongs on live jobs per box against a cache budget. Engines built for chat count the first; agents live in the second, and the count an operator watches rarely matches the thing being used.

## The big picture:

Agent work is now one long conversation, not many separate calls. Over fourteen days on a fleet running coding agents, cached tokens made up 77.7% of all input tokens [2]. The same trace puts decode, the phase where the model writes rather than reads, at 78.4% of the time a call takes [2]. A job is mostly a warm cache plus a slow writer, and both are held open by the queue in front of them.

The billing layer makes that worse rather than better. Providers meter tokens per minute, and caching multiplies what a quota buys. One provider's page works through a 2,000,000 input-token limit that turns into 10,000,000 tokens at an 80 percent hit rate [3]. I read the provider's quota page twice: it is a queueing point wearing a price list. A job that loses its cache slot pays twice, once in redone work and once against a cap that assumed it kept the slot.

Agent-hosting papers add that the fix already exists one layer down. A queue planner that takes the whole agent task as its unit can see that a queued call is blocking the call that would have freed it. A call-level queue cannot see that shape at all [4]. The engine's work trouble is a visibility issue first and a space issue second.

## By the numbers

- **4-15x — Whole-task planning:** Autellix, an engine that schedules agent programs rather than lone calls, wins back 4-15x the work done at the same delay as a mainstream engine, and 5.5x over the preemptive call-level option on mixed work [4].
- **34.7% — Grouping under a delay target:** on an operator's live fleet of more than 1,000 graphics chips, grouping calls while keeping shared-prefix reuse cut hosting boxes by 34.7% and raised per-box call output by 36.8% [2].
- **24.6% — The delay target is a purchase:** the same queue planner used 13.0-16.8% fewer active graphics-chip hours at a 30-millisecond per-token target, and 21.1-24.6% fewer at 50 milliseconds, which prices the gap between a tight and a loose delay target [2].
- **45% — Where the delay actually sits:** tool execution accounts for 45%-57% of end-to-end agent delay across research, coding and science tasks, so the tool side is where a system can win time back without touching the model [1].

## What I'd watch:

The people closest to this work are settling on four moves. I see one decision under all four: cap who waits, not how fast each step runs.

- **A cap on jobs, not calls:** PackServe groups calls onto fewer boxes while holding a time-per-output-token target, which is job-level control described as a grouping question [2]. The unit it guards is the shared prefix.
- **Cache reuse as a queue rule:** Autellix preempts and ranks calls using their task's own finished work, and inside a single task the paper reports cache-hit rates above 90% across input lengths [4]. That is the asset the queue was quietly spending.
- **Overlap instead of more parallel work:** PASTE, a hosting system that runs likely tool calls early, starts those calls while the model is still writing, cutting mean task time by 43.5%, then holds back new jobs so the returning work does not swamp the engine [1]. The hold is what makes the speed-up real.
- **Ramp rather than jump:** one provider's advice for steady load is to grow traffic by no more than 50% every 15 minutes once it passes 1,000,000 input tokens per minute [5], which is a cap curve written by the party holding the quota.

An earlier note on [what a session costs to start](/your-sandbox-boot-tax-110x-then-nothing/) prices the other half of this bill, and it sits in the same category for a reason: boot and cache are both fixed costs a queue planner can waste.

## The catch

The headline gain carries a condition I want to state plainly. Autellix earns its 4-15x by seeing calls at the whole-task level, and a system that calls a hosted endpoint one call at a time cannot see that shape at all [4]. If the engine is not yours and the gateway is not yours, the 4-15x is someone else's result.

The live numbers deserve the same care. PackServe's shares come from one operator's fourteen-day trace and one fleet, so 77.7% and 34.7% describe that fleet's prefix habit, not a rule anyone can adopt [2]. The 192-job mark is a point on a load curve, not a published ceiling, and no source in the stack says how many jobs one graphics chip should hold. That number has to be measured against your own prefix lengths.

The last caveat is the one that changes the plan. PASTE's authors ran a test that doubled tool speed while leaving the model's queue alone, and under load the faster tools handed back more work for the model to absorb [1]. Tool-side delay is cheap to attack, and attacking it with no cap on jobs just moves the queue onto the engine. The tool side is where the time is; the job cap is what makes buying it worth anything.

## At a glance

**The shift:** Systems now hold long jobs that share a cached prefix, so the limit that matters is live jobs per box, not calls per minute.
**The number:** Grouping those jobs while keeping prefix reuse cut a live queue planner's hosting boxes by 34.7%.
**The risk:** The whole-task gains need control of the call path, and faster tools without a job cap push the queue back onto the model.

## Sources
[1] Sui, Zhao, Ma, He, Wang and Xu, "PASTE: Parallelizing Tool Execution and LLM Generation for Low-Latency Agent Serving," arXiv:2603.18897v3, 16 June 2026. https://arxiv.org/html/2603.18897v3
[2] Tan, Zhu, Jiang, Zheng et al., "PackServe: SLO-Aware Request Scheduling for Agentic LLM Serving at Scale," arXiv:2609.33224v1, 27 September 2026. https://arxiv.org/html/2609.33224v1
[3] Anthropic, "Rate limits," provider documentation, effective-throughput example read 2 November 2026. https://docs.claude.com/en/api/rate-limits
[4] Luo, Shi, Cai, Zhang, Wong, Wang, Wang, Huang, Chen, Gonzalez and Stoica, "Autellix: An Efficient Serving Engine for LLM Agents as General Programs," arXiv:2502.13965v1, 19 February 2025. https://arxiv.org/html/2502.13965v1
[5] OpenAI, "Rate limits," provider documentation, usage tiers and ramp rate read 2 November 2026. https://platform.openai.com/docs/guides/rate-limits
