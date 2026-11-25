---
title: "Agent Instruction Drift: 16 Steps to Zero"
vertical: agentic_resilience_failure
meta_title: "Agent Instruction Drift: 16 Steps to Zero"
meta_description: "Long agent runs stop following the standing instructions they were given once. A 10,664-trajectory study pins the driver on step count, not context length."
primary_keyword: "agent instruction drift"
secondary_keywords: [long-horizon agent reliability, agent FSM procedure enforcement]
kind: evergreen
archetype: evergreen
evergreen: true
persona: infra_engineer
one_big_thing: "A long agent run stops following the instructions it was given once: every tested model falls from near-perfect to near zero within sixteen dependent steps, and the driver is step count, not context length."
date: 2026-11-25
slug: your-agent-forgets-your-rules-16-steps
---

<!-- lead -->

Agent instruction drift is not a context-window cliff. It is a step-count cliff. One study measured 10,664 agent trajectories over long runs. Every model tested fell to near zero within 16 chained steps [1]. The run ages because each step's output becomes the next step's input, so a slip is carried forward, not corrected. The failure is not attention being squeezed out of a full window. It is the run outliving the instruction. That changes where the standing procedure has to live.

<!-- tldr -->

## At a glance

Long unattended agent runs drift away from procedures stated once at the start. The decay tracks how many steps the run takes, not how full its context window is. The finding comes from 10,664 measured trajectories and lands on whoever keeps long-horizon agent workflows in production.

<!-- tension -->

## Step Count Drives the Drift

The evidence arrived in a fixed order. In March 2025, METR (Model Evaluation and Threat Research, an independent lab) showed the length of tasks agents complete doubling about every 7 months [4]. That meant production horizons were heading into the zone where this behavior lives. Two months later, a study of more than 200,000 simulated conversations measured the same model on the same tasks. Delivered across turns instead of one prompt, performance fell by an average of 39% [3].

In September 2026, a fleet-scale study of long-run decay pinned the mechanism [1].

Across 10,664 analyzed trajectories, decay is driven by step count rather than context length. Bounding the context window made decay steeper, not shallower. The measured odds of success fell faster with a trimmed window: a logit slope of −0.69 versus −0.44, where the slope is how quickly success odds drop per step [1].

That last comparison is the part that hurts. The instinct when a long run degrades is to trim the transcript and keep the window tidy. The measured result says that shortcut moves the wrong variable. The agent is not drowning in context. It is aging in steps [1]. This is close kin to the context-overflow problem in memory design, yet the fix points the other way. [Long Context Is Not Memory: Why AI Agents Need Tiered State](/agent-memory-tiering-l1-l4/) argues for tiered state to preserve content. This data says preserving content is not what keeps a run on its procedure.

## By the numbers

- **Sixteen dependent steps:** where every tested model falls from near-perfect success to near zero, across 10,664 analyzed trajectories [1].
- **39% average drop:** what the same model loses when the same task arrives over turns instead of one prompt [3].
- **+10.5 accuracy points:** the gain an enforced state machine holds over a plain agent whose instructions drift [2].

<!-- tactical-insight -->

## What teams are doing about it

The most direct response in the 2026 literature is to stop storing the procedure in the prompt at all. A November 2026 study kept workflow state in an executable finite-state machine (FSM, a small program that holds which step the run is on) outside the model's context [2]. It enforced that state at three points: tool calls, transitions and turn endings. The enforcement arm raised strict instruction accuracy by +10.5 points over the plain agent, and the gain repeated in 7 of 8 seeds [2].

The same paper found why the common fixes fail. Restating the instructions, or resuming a stopped agent, only moved the drift to a different shortcut [2].

The trade is honest about its price. Where both were measured, the enforced runtime cost 1.2 to 3.5 times the plain agent's time or cost [2]. I find that pricing comparison tells the whole story. The enforcement cost is booked per run, and it is bounded. The drift cost is booked per incident, and you usually do not see the incident.

The horizon arithmetic is the signal to watch, not the model release notes. METR's doubling time of about 7 months means next year's workload sits deeper into the decay curve than this quarter's benchmark [4]. On the study's most agentic task family, near-zero lands by step 16. That makes 16 a shape marker, not a universal tripwire. The direction held across every model tested [1].

<!-- nuanced-takeaway -->

## The catch

The enforcement result is promising and young. The FSM study reports its gains on its own evaluation domains: debugging, customer service and improvement loops. Its strict-accuracy confidence interval spans 1.2 to 23.4 points, which is wide for a headline number [2]. Part of the decay evidence sits on a paper abstract rather than full fetched tables, so interior numbers stay unverified until the full text parses. What I keep coming back to is the refutation, not the remedy. Step count, not context length, drives the decay [1]. A remedy built on the wrong lever will trim the transcript, spend money every run, and leave the sixteen-step cliff untouched.

## Sources

- [1] S. Mittal, "How Fast Do Agents Rot? An Empirical Study of Long-Horizon Degradation in LLM Agents for Production Decision-Making", arXiv:2609.01660 — https://arxiv.org/abs/2609.01660
- [2] "Keeping LLM Agents on Procedure: Executable Finite-State Control for Long-Horizon Instruction Fidelity", arXiv:2611.10884v1 — https://arxiv.org/html/2611.10884v1
- [3] "LLMs Get Lost in Multi-Turn Conversation", arXiv:2505.06120v1 — https://arxiv.org/html/2505.06120v1
- [4] T. Kwa, B. West, J. Becker et al., "Measuring AI Ability to Complete Long Tasks", METR, 2025-03-19 — https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/
