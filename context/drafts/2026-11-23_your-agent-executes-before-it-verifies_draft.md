---
title: "Your Agent Executes Before It Verifies: The 74.83% Cost"
vertical: agentic_ai
kind: evergreen
archetype: evergreen
evergreen: true
persona: ai_architect
one_big_thing: "An ungated agent executes its worst calls harmfully at a 74.83% rate; the cheapest fix is a deterministic gate in program logic that checks every action before it runs, not a bigger model."
date: 2026-11-23
slug: your-agent-executes-before-it-verifies
---

<!-- lead -->
Your agent executes each action before anything verifies it, and that gap costs more than a bad day: on a 600-command test track, an agent with no guard ran harmful shell commands at a 74.83% rate [2]. Because a wrong call against a real system is hard to undo, the fix belongs before the call, not after the damage.

<!-- tldr -->
## At a glance
This piece prices the verification layer for AI systems architects: what a gate in program logic, a trained guardrail and a model judge each catch before a tool call executes. Three measured studies from 2026 put most of the reliability in the cheapest layer.

<!-- tension -->
## What the gate catches
Start with the worst case. In July 2026, a study called CARE (short for command pre-execution verification) tested a shell-running agent with no guard at all. Of 600 agent-written commands executed inside a Docker sandbox, 449 did real harm [2]. The team set that rate as the harm ceiling, the number every guard has to move.

The next finding points the other way. A guardrail study called ToolSafe, published by the Association for Computational Linguistics (ACL) in 2026, put a check in front of every tool invocation. Harmful calls fell by 65% on average. Safe tasks did not suffer; completion even rose about 10% when prompts carried hidden attacks [1].

A third study explains why the timing matters. Its authors injected failures that only half-happen — a tool call that completes, half-completes, or fails after making a change. An agent that verifies outside state before retrying finished 80% of its tasks; the same agent without the check finished 58% [4]. Verifying before the retry, rather than hoping the retry lands better, was the main source of that lift [4].

The reason sits in the architecture, not in any model's talent. The model proposes; the runtime decides whether to hand the call to the tool. A check written as code — a pattern match, a list lookup, a test of the call's result — is cheap, stable, and it answers the same question the same way every time. A check written as another model call (a judge) can read what no pattern can, but each check burns tokens, and its answer only holds if the runtime actually stops the call on a no.

The group that pays for the gap is whoever owns the system the agent writes to. A wrong call lands as a valid request against a real endpoint. The error shows up days later as a cleanup job. The gate turns that silent miss into a visible block.

## By the numbers
- **449 commands:** did harm on the 600-command shell track with no guard in place. [2]
- **0.34 milliseconds:** the static gate's cost per checked command in its static profile. [3]
- **20 points:** the task-success lift that verify-before-retry added over the ungated agent. [4]

<!-- tactical-insight -->
## What the closest teams buy
The measured teams split the work the way an architect would. CARE ships two profiles: a static one that catches most bad commands at 0.34 ms each, and a slower one backed by a language model for calls no pattern can read [3]. ToolSafe builds the same split at the run level — a trained guardrail model watches each tool invocation before it executes and returns a reason with its verdict [1].

The verify-before-retry study adds the second half of the gate, after the call. When a tool call may only half-complete, the agent checks outside state before it tries again: postconditions confirmed, retry keys attached, repeat calls refused. Duplicate actions fell from about 42% to 20% under that regime [4]. The failure it prevents is familiar from the field: the loop that re-tries a failing strategy until a bill stops it. The gate answers it with loop control rather than a stronger model.

What I find hard to square is how much of this work is plain code. One study of verification as a runtime layer counted its own enforcement: gates fired 24 times while judges were consulted three times, and no judge ever reversed a gate [5]. That ratio, not the judge's accuracy, is the budget line — most of the checks you need are cheap predicates, and paying judge prices for them is a choice, not a requirement. The guardrail frameworks reaching production converge on the same default: check the proposed action where the model's reasoning meets the tool's permissions.

<!-- nuanced-takeaway -->
## The catch
A gate in code buys stability, not correctness. It passes any action that is wrong in a way the pattern does not express — a command that clears the blocklist and still drops the wrong table, a valid payload aimed at an endpoint the account may not touch. That is why the static profile's 37.33% is a floor to raise, not a number to ship and forget [3]. The studies carry a quieter limit too: blocking every unsafe action still does not make every task safe, and the gap between those two measures is exactly where an auditor will look [2]. What I keep circling is the state the gate cannot see on its own — what a completed step actually changed — which is the same missing state this desk has argued in [agent tool contracts](/durable-execution-not-a-transaction/), and no pattern you write today will invent it for you.

## Sources
- [1] Mou, Xue, Li, Liu, Zhang, Ye & Shao, "ToolSafe: Enhancing Tool Invocation Safety of LLM-based agents via Proactive Step-level Guardrail and Feedback", Findings of ACL 2026 — https://aclanthology.org/2026.findings-acl.1850/
- [2] "CARE: Pre-Execution Command Verification for Shell-Executing LLM Agents", arXiv:2607.21642v2 — https://arxiv.org/html/2607.21642v2
- [3] CARE, abstract and Section V, same paper — https://arxiv.org/html/2607.21642v2
- [4] "Verified Tool Calls Improve LLM Agent Reliability Under Non-Atomic Failures", arXiv:2608.02645v1 — https://arxiv.org/html/2608.02645v1
- [5] "Verification as an Architectural Layer for LLM Agents", arXiv:2609.31937v1 — https://arxiv.org/html/2609.31937v1
