---
title: "One Green Run Is Not Reliability: Gate Agents on Pass^k"
vertical: ai_observability_qa
persona: evals_infra_eng
one_big_thing: "A single-run pass rate overstates an agent's reliability: gate the release on the repeat-trial pass^k rate and instrument the per-call retry count, because the failures that tank repeatability are design and verification, not model capability."
date: 2026-10-06
slug: agent-reliability-pass-k-not-one-green-run
archetype: evergreen
evergreen: true
---

<!-- lead -->
The best tool-using agents fail more than half the time, and the number most teams ship on hides it. On τ-bench, a benchmark that runs an agent through multi-step tasks with tools and a user, even a top function-calling model clears fewer than half of the tasks in a single run [1]. Ask for the same result across repeated trials, and its retail-domain score falls below 25% [1]. One green run is not reliability; it is a single draw from a distribution.

<!-- tension -->

## The big picture:

Agent evaluation inherited its habits from software testing, where a passing test is a fact. A model is not a test.

A suite written for deterministic code assumes the same input gives the same output. An agent driven by a model does not promise that. The benchmark authors knew this, so they proposed a second metric, pass^k, that runs a task several times and asks whether the agent behaves the same way each time [3].

I keep coming back to where the failures actually sit. A taxonomy built from 150 analysed agent traces found 14 distinct failure modes in three groups — system design, misalignment between agents, and task verification [2]. The instrument is usually not the problem. The wiring around it is.

The other half of the problem is that an agent can hide its own flakiness. A tool call fails a quiet validation check, the loop asks the model again, and the run eventually "passes" in more time. Without a per-call trace, you cannot tell a slow model from a retry loop [4].

## By the numbers

- **25% — pass^8 in retail:** An agent that clears under half the tasks in one run falls below 25% when the same task must succeed across eight repeat trials [1].
- **Under 50% — single-run success:** Even state-of-the-art function-calling models (the gpt-4o class) solve fewer than half of the benchmark's tasks in a single attempt [1].
- **150 traces — 14 failure modes:** The MAST taxonomy was built from 150 analysed traces and sorts those failures into three groups, led by system design and task verification [2].
- **51% — agents in production:** Just over half of surveyed teams already run agents in production, and tracing and observability head the list of controls they say they need [3].

<!-- tactical-insight -->

## What I'd watch:

- **A repeat-trial gate:** The teams I have watched tighten this are moving the release check off a single run and onto pass^k, so a regression has to survive repeat trials before it ships [3].
- **A retry count per tool call:** Recording each model and tool call as its own traced span — model, token counts, tool invocation — is what turns "the agent is slow" into "step four retried eleven times" [4].
- **A deterministic check ahead of the model:** Since the failures cluster in design and verification, the durable fix is a schema or validation gate that rejects a bad tool call outright instead of letting the model re-ask [2].
- **The share of design failures:** What strikes me is how little of the failure budget is model quality. If most faults are wiring, a better frontier model does not move the number.

<!-- nuanced-takeaway -->

## The catch

Repeat-trial testing is not free. Running every task k times multiplies eval cost and wall-clock, which is exactly why so many suites quietly score a single run and call it done [3].

A low pass^k also has an innocent reading. A genuinely hard environment, or a task set that mixes easy and near-impossible items, will depress repeatability without the agent being broken [1].

My read: the fix is not to demand a perfect score. It is to pick the number that matches the decision. If the question is "will this behave the same way twice in front of a customer," a single green run answers a different question than the one being asked.

<!-- tldr -->

## At a glance

- **The Big Shift:** Agent quality is moving from a single-run pass rate to a repeat-trial rate, as benchmarks like τ-bench show top agents dropping below a quarter of tasks once you require the same result across repeated runs.
- **Why It Matters:** A team that gates on one lucky run ships a system that fails in front of customers. The funding decision — keep the agent in production, or pull it — should rest on whether it is repeatable, not on whether it passed once.
- **What I'd Watch:** Whether eval suites start scoring repeat trials, and whether traces begin counting the retries that hide flakiness.
  - **pass^k:** A metric that runs each task several times and asks whether the agent succeeds consistently [3].
  - **Per-call trace spans:** One recorded entry for every model and tool call, so a retry loop is visible instead of guessed [4].
  - **Design-failure share:** The fraction of failures that come from wiring and verification rather than the model [2].
- **The Catch:** Repeat-trial testing multiplies eval cost and time, and a low repeat rate can simply mean the task set is hard — so the metric, not the wish, has to match the decision.

<!-- internal-links -->

## Sources
[1] Yao et al., "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains," arXiv:2406.12045 — https://arxiv.org/abs/2406.12045
[2] Cemri et al., "Why Do Multi-Agent LLM Systems Fail?" (MAST), arXiv:2503.13657 — https://arxiv.org/abs/2503.13657
[3] LangChain, "State of AI Agents" — https://www.langchain.com/stateofaiagents
[4] OpenTelemetry, "Inside the LLM Call: GenAI Observability with OpenTelemetry" — https://opentelemetry.io/blog/2026/genai-observability

<!-- linkedin -->
I keep coming back to one number from a benchmark most eval teams already know. On τ-bench, even a top function-calling model clears fewer than half of the tasks in a single run. Require the same task to succeed across repeat trials, and its retail score falls below 25%.

My read: a single green run is not reliability. It is one draw from a distribution, and most release gates are built on exactly that draw.

The part I keep circling is where the failures live. A taxonomy built from 150 agent traces found 14 failure modes in three groups — system design, misalignment between agents, and task verification. Very little of it is the model being weak.

That is also why retries matter. A tool call fails a quiet check, the loop asks the model again, and the run eventually passes in more time. Without a per-call trace you cannot tell a slow model from a retry loop.

Just over half of surveyed teams are already running agents in production, and tracing tops the list of controls they say they need. I'm curious how others are gating the release: a single run, or a repeat-trial score?
