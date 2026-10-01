---
title: "Fold the Model Choice Into the Plan"
vertical: agentic_ai
persona: ai_architect
one_big_thing: "Planner-as-Router cuts multi-agent cost 44% by assigning each subtask a model tier at plan time — no router model, no training data — and its own pilot warns cheap routing may quietly compound errors."
date: 2026-10-01
slug: planner-as-router-plan-time-routing
---

<!-- lead -->
A frontier model can cost 25 times what a small model costs per token, and that gap compounds every time a workflow chains calls together [1]. On Sept 26, three authors posted Planner-as-Router (PaR) to arXiv with a sharper answer than "train a router model": fold the model choice into the plan itself, and cut 44% of the cost [1].

<!-- tension -->
## The Router Moved Upstream

I've been watching how agent builders fight the inference bill all month, and the interesting shift here is *where* the routing decision lives. Most production systems lean on a per-call cascade router — a separate component that looks at one node at a time and picks a model tier. PaR argues that is backwards. It assigns each subtask a model tier — small, mid, or frontier — at *plan* time, before any specialist runs, so the dependencies between subtasks are visible up front [1]. There is no router model to train and no training data to collect [1].

**The big picture:** Routing is becoming a first-class architectural decision rather than a downstream cost hack. What makes the paper worth reading is its honesty — it frames its advantage as "frontier position," not a clean win, because several accuracy gaps fall inside a ±6-point confidence interval [1]. The subagent cost problem is no longer "which vendor is cheapest"; it is "which tier can each step of the workflow actually afford, and what breaks when we pick wrong."

**By the numbers:**
- **25×:** What a frontier model can cost per token versus a small model, before chaining compounds it [1].
- **44%:** The cost cut PaR achieves against all-frontier routing, at a 2.9-point accuracy cost [1].
- **1,157:** Evaluations across eight routers and three seeds, on 54 enterprise tasks graded by executing SQL and MongoDB queries against live databases [1].

<!-- tactical-insight -->
## What I'd Watch

What strikes me here is how clean the mechanism is, and how thin the confidence is. The approach reads like a systems design, not a machine-learning trick: the planner assigns a tier to every subtask up front, and the dispatcher runs them in dependency order, escalating one tier on failure [1]. The whole thing ships open source, benchmark and evaluation code included [1].

**What I'd watch:**
- **Plan-time assignment:** Whether routing decisions made before execution — where subtask dependencies are visible — hold up against per-call routers on messy, real workloads [1].
- **The escalating dispatcher:** Running subtasks in dependency order and bumping one tier on failure is the deterministic fallback the architecture crowd has wanted for a while, and it is worth tracking against ad-hoc retry logic [1].
- **The compounding penalty:** The paper flags — but does not validate — that cheap routing may compound errors on long, compositional workflows. I'd want to see that reproduced at scale before trusting the 44% [1].

<!-- nuanced-takeaway -->
**The catch:** The headline is a ceiling, not a floor. The 44% saving comes with a 2.9-point accuracy drop, and the paper says several of those gaps sit inside the ±6-point confidence interval of a 54-task study [1]. My read: PaR's real contribution is not the number. It is moving the routing decision into the plan where dependencies are visible, and naming the risk — compounding error — that most cheaper-router pitches leave unsaid [1].

**Go deeper:**
<!-- internal-links -->

<!-- tldr -->
- **The Big Shift:** A new paper, Planner-as-Router, folds the model-tier choice into multi-agent planning — assigning each subtask a small, mid, or frontier model before any of them runs — and cuts 44% of cost against running the frontier model everywhere.
- **Why It Matters:** Model routing is becoming an architectural decision, not a downstream fix. The approach needs no separate router model or training data, which changes what a team has to build and maintain.
- **What I'd Watch:** whether the 44% holds up and whether the "compounding penalty" shows up.
  - **Plan-time tiering:** Picking a model tier for each subtask when the plan is made, so the dependencies are visible up front.
  - **Escalating dispatcher:** Running subtasks in order and bumping one tier up on failure, a deterministic fallback instead of ad-hoc retries.
  - **Compounding penalty:** The paper's own un-validated hint that routing cheap models may quietly add up errors across long workflows.
- **The Catch:** The 44% saving costs 2.9 accuracy points, and several gaps fall inside the study's ±6-point confidence interval — the win is "frontier position," not a clean accuracy victory.

## Sources
[1] Planner-as-Router: Joint Plan-Time Model Routing for Cost-Efficient Multi-Agent Workflows — arXiv:2609.32917 (submitted Sept 26, 2026) — https://arxiv.org/abs/2609.32917

<!-- linkedin -->
I've been reading the agent-routing papers all month, and one from Sept 26 stopped me. Planner-as-Router (PaR) tries something different: instead of a separate router model picking a model tier for each call, it folds the choice into planning — each subtask gets a small, mid, or frontier model before any of them run.

The result: a 44% cost cut against running the frontier model everywhere, at a 2.9-point accuracy cost, across 1,157 evaluations. No router model to train, no training data.

My read: the real contribution isn't the number — it's moving the routing decision into the plan, where subtask dependencies are visible, instead of bolting a classifier on downstream.

The part I keep circling: the paper quietly flags that cheap routing "may carry a hidden compounding penalty on compositional workflows" — and then says it hasn't validated it. Every cheaper-router pitch has left that risk unsaid. This one names it.

The catch: the 44% is a ceiling, not a floor — several accuracy gaps fall inside the study's ±6-point confidence interval.

I'm curious how routing teams are handling it: is the compounding penalty real at scale, or just a small-pilot blip?
