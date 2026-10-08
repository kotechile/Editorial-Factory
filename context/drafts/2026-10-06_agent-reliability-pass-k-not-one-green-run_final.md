---
title: "One Green Run Is Not Reliability: Gating Agents on Pass^k"
vertical: ai_observability_qa
persona: evals_infra_eng
one_big_thing: "A single-run pass rate overstates an agent's reliability: gate the release on the repeat-trial pass^k rate and instrument the per-call retry count, because the failures that tank repeatability are design and verification, not model capability."
date: 2026-10-06
slug: agent-reliability-pass-k-not-one-green-run
archetype: evergreen
evergreen: true
image_path: "context/assets/illustrations/agent-reliability-pass-k-not-one-green-run/featured.png"
image_style: "technical_isometric"
image_model: "nanobanana"
image_alt: "Isometric cutaway of a logic routing bay with a central validation gate and blocked retry loops."
image_caption: "Repeat-trial testing exposes structural flaws in agent design that a single lucky run hides."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
The best tool-using Artificial Intelligence (AI) agents fail more than half the time, but normal testing hides the flaws. On τ-bench, a test that runs an agent through tasks with tools and a user, a top model clears fewer than half the tasks in a single run [1]. Require the same result across repeat trials, and its retail score drops below 25% [1]. One successful run is not reliability; it is a lucky draw from a random set.

<!-- tension -->

## The big picture:

Agent testing inherited bad habits from normal software engineering, where a passing test is a hard fact. 

A test suite built for normal code assumes the same input always yields the same output. An agent driven by a model does not make that promise. Test authors know this, proposing a metric called pass^k that runs a task several times to check if the agent behaves the same way [3].

I keep coming back to where these failures actually sit. A study of 150 agent traces found 14 distinct failure modes across system design, agent clashes, and task checks [2]. The model is rarely the problem, but the wiring around it breaks.

Agents also hide their own flaws. If a tool call fails a quiet check, the system asks the model again, and the run passes after a delay. Without tracking every single call, you cannot tell a slow model from an endless retry loop [4].

## By the numbers

- **25% — Repeat-trial retail score:** An agent that clears under half the tasks in one run falls below 25% when the same task must succeed across eight repeat trials [1].
- **Under 50% — Single-run success:** Even top function-calling models solve fewer than half of the test tasks in a single try [1].
- **14 — Distinct failure modes:** A taxonomy built from 150 analyzed traces sorts agent errors into three groups, led by system design and task checks [2].
- **51% — Live agent setups:** Just over half of surveyed teams already run agents in live setups, citing tracing as their top needed control [3].

<!-- tactical-insight -->

## What I'd watch:

- **A repeat-trial gate:** The benchmark's own answer to single-run scoring is pass^k, which asks whether an agent behaves the same way on each attempt instead of whether it passed once [1].
- **A retry count per tool call:** Recording each model and tool interaction as its own traced entry turns a vague complaint about a slow agent into a clear fact: this tool call retried instead of resolving [4].
- **A strict check ahead of the model:** Since failures cluster in design and checks, the durable fix is a strict validation gate. This rejects a bad tool call outright instead of letting the model guess again [2].
- **The share of design failures:** What strikes me is how little of the failure budget stems from model quality. If most faults are bad wiring, upgrading to a better frontier model will not fix the score.

<!-- nuanced-takeaway -->

## The catch

Repeat-trial testing is expensive. Running every task multiple times multiplies test costs and total clock time. That is exactly why so many testing suites quietly score a single run and call it finished [3].

A low pass^k score also carries an innocent reason. A genuinely hard setup, or a task set mixing easy and near-impossible items, drops repeat scores without the agent actually being broken [1].

My read: the fix is not to demand a perfect score. It is to pick a metric that matches the business choice. If the question is whether an agent will act the same way twice for a customer, a single lucky run answers the wrong question.

<!-- tldr -->

## At a glance

- **The Big Shift:** Agent testing is moving from a single-run pass rate to a repeat-trial rate, exposing how top agents drop below a 25% success rate when forced to yield consistent results [1].
- **Why It Matters:** Teams gating releases on one lucky run ship systems that fail in front of live customers. Funding choices should rest on whether an agent is repeatable, not just capable of passing once.
- **What I'd Watch:** Whether test suites start scoring repeat trials, and whether traces begin counting the retries that hide agent flakiness.
  - **pass^k:** A metric running each task several times to verify the agent succeeds consistently [3].
  - **Per-call trace spans:** A recorded entry for every model and tool call, making retry loops visible instead of guessed [4].
  - **Design-failure share:** The fraction of total errors stemming from system wiring and checks rather than the language model itself [2].
- **The Catch:** Repeat-trial testing multiplies test costs and time, and a low repeat rate can simply mean the test is hard — meaning the metric must match the actual rollout choice.

<!-- internal-links -->

## Sources
[1] Yao et al., "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains," arXiv:2406.12045 — https://arxiv.org/abs/2406.12045
[2] Cemri et al., "Why Do Multi-Agent LLM Systems Fail?" (MAST), arXiv:2503.13657 — https://arxiv.org/abs/2503.13657
[3] LangChain, "State of AI Agents" — https://www.langchain.com/stateofaiagents
[4] OpenTelemetry, "Inside the LLM Call: GenAI Observability with OpenTelemetry" — https://opentelemetry.io/blog/2026/genai-observability

<!-- linkedin -->
I keep coming back to one number from a test benchmark most teams already know. On τ-bench, even a top function-calling model clears fewer than half of the tasks in a single run. Require the exact same task to succeed across repeat trials, and its retail score falls below 25%.

My read: a single green run is not reliability. It is one lucky draw from a random set, and most release gates are built on exactly that draw.

The part I keep circling is where the failures actually live. A study of 150 agent traces found 14 failure modes in three groups — system design, agent clashes, and task checks. Very little of it stems from the model being weak.

That is exactly why retries matter. A tool call fails a quiet background check, the loop asks the model again, and the run eventually passes after a long delay. Without a per-call trace, you cannot tell a slow model from an endless retry loop.

Just over half of surveyed teams are already running agents in live setups, and tracing tops the list of controls they say they need. I'm curious how others are gating their releases: are you relying on a single run, or a repeat-trial score?

## Gate report
lead: PASS — Core takeaway delivered immediately in the first sentence without filler, setting up the exact shift in reliability testing.
tension: PASS — Proper H2 spacing, simple vocabulary raises Flesch score above 60, and includes a clear first-person read.
tactical-insight: PASS — Phrased purely as observations of what teams are doing, avoiding all commands while splitting long paragraphs to meet the 3-sentence maximum.
nuanced-takeaway: PASS — Honest trade-off presented, properly separated by blank lines, and includes a distinct first-person read on the metric matching the business choice.
tldr: PASS — Strict 4-part Smart Brevity schema followed exactly, cleanly separating the executive summary.
