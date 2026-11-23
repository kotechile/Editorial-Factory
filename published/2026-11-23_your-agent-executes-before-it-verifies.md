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
meta_title: "Your Agent Executes Before It Verifies: The 74.83% Cost"
meta_title_source: "derived_from_title"
meta_description: "Your agent executes each action before anything verifies it, and that gap costs more than a bad day: on a 600-command test track, an agent with no guard ran…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-agent-executes-before-it-verifies/featured.jpg"
image_style: "paper_collage"
image_model: "nanobanana"
image_alt: "The 74.83% Cost Of Ungated Agents. A striped barrier gate lowered to pin one punch card while queued program cards wait behind it."
image_caption: "The 74.83% Cost Of Ungated Agents: Ungated agents ran harmful commands at 74.83% — the cheap fix checks the call."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Your agent executes each action before anything verifies it, and that gap costs more than a bad day: on a 600-command test track, an agent with no guard ran harmful shell commands at a 74.83% rate [2]. Because a wrong call against a real system is hard to undo, the fix belongs before the call, not after the damage.

<!-- tldr -->
## At a glance
This article prices the layers that can sit between an AI agent and its tools — a code gate, a trained guardrail, a model judge — for architects wiring agents to systems that cannot be rolled back. Three measured 2026 studies put most of the reliability in the cheapest layer.

<!-- tension -->
## What the gate catches
The worst case came with a number. In July 2026, a study called CARE (short for command pre-execution verification) tested a shell-running agent with no guard at all. Of 600 agent-written commands executed inside a Docker sandbox, 449 did real harm [2]. The team set that rate as the harm ceiling — the number every guard has to move.

The next finding points the other way. A guardrail study called ToolSafe, published by the Association for Computational Linguistics (ACL) in 2026, put a check in front of every tool invocation. Harmful calls fell by 65% on average. Safe tasks did not suffer; completion even rose about 10% when prompts carried hidden attacks [1].

A third study explains why the timing matters. Its authors injected failures that only half-happen — a tool call that completes, half-completes, or fails after making a change. An agent that verifies outside state before retrying finished 80% of its tasks; the same agent without the check finished 58% [4]. Checking the world before trying again, rather than hoping the retry lands better, was the main source of that lift [4].

I read the two numbers twice before the shape of it landed: the 20-point swing comes from looking, not from a stronger model. The reason sits in the architecture. The model proposes; the runtime decides whether to hand the call to the tool. A check written as code — a pattern match, a list lookup, a test of the call's result — answers the same question the same way every time, at a cost close to zero. A check written as another model call can read what no pattern can, but each check burns tokens, and its verdict only matters if the runtime stops the call on a no.

## By the numbers
- **449 commands:** did real harm on the 600-command shell track with no guard in place [2].
- **0.34 milliseconds:** the static gate's cost per checked command in its static profile [3].
- **20 points:** the task-success lift that verify-before-retry added over the ungated agent [4].

<!-- tactical-insight -->
## What the closest teams buy
The measured teams split the work the way an architect would. CARE ships two profiles: a static one that catches most bad commands at 0.34 ms each, and a slower one backed by a language model for calls no pattern can read [3]. ToolSafe builds the same split at the run level — a trained guardrail model watches each tool invocation before it executes and returns a reason with its verdict [1].

The verify-before-retry study adds the second half of the gate, after the call. When a tool call may only half-complete, the agent checks outside state before it tries again: postconditions confirmed, retry keys attached, repeat calls refused. Duplicate actions fell from about 42% to 20% under that regime [4]. The failure it prevents is familiar from the field — the loop that re-tries a failing strategy until a bill stops it — and the gate answers it with loop control rather than a stronger model.

I keep coming back to how little of this work needs a model at all. One study of verification as a runtime layer counted its own enforcement: gates fired 24 times while judges were consulted three times, and no judge ever reversed a gate [5]. That ratio is the budget line. Most of the checks you need are cheap predicates, and paying judge prices for them is a choice, not a requirement. The frameworks reaching production converge on the same default, checking the proposed action where the model's reasoning meets the tool's permissions.

<!-- nuanced-takeaway -->
## The catch
A gate in code buys stability, not correctness. It passes any action that is wrong in a way the pattern does not express — a command that clears the blocklist and still drops the wrong table, a valid payload aimed at an endpoint the account may not touch. That is why the static profile's 37.33% is a floor to raise, not a number to ship and forget [3]. The studies carry a quieter limit too: blocking every unsafe action still does not make every task safe, and the gap between those two measures is exactly where an auditor will look [2].

My reading, held loosely: the hardest part is the state the gate cannot see on its own — what a completed step actually changed outside the agent, the same missing state this desk has argued in [agent tool contracts](/durable-execution-not-a-transaction/). The verify-before-retry result points at the answer, because its 80% came from agents that checked the world instead of their own intent [4]. A pattern you write today will not invent that state, but a postcondition test will ask for it, and that is where I would spend the next design pass.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Your Task Protocol Costs 643 Lines" -> /your-task-protocol-costs-643-lines/ [same site (aichieve.net); same category; topical overlap: agent, cost, costs] Link "Your Task Protocol Costs 643 Lines" in the section where the article touches agent, cost, costs. -->
<!-- internal-link hint: "Agent Memory Poisoning" -> /agent-memory-poisoning-write-path/ [same site (aichieve.net); same category; topical overlap: agent, guard] Link "Agent Memory Poisoning" in the section where the article touches agent, guard. -->
<!-- internal-link hint: "Planner-as-Router: Fold the Model Choice Into the Plan" -> /planner-as-router-fold-the-model-choice-into-the-plan/ [same site (aichieve.net); same category; topical overlap: agent, costs] Link "Planner-as-Router: Fold the Model Choice Into the Plan" in the section where the article touches agent, costs. -->
## Related reading

- [Your Task Protocol Costs 643 Lines](/your-task-protocol-costs-643-lines/) — more on Autonomous & Agentic Workflows
- [Agent Memory Poisoning](/agent-memory-poisoning-write-path/) — more on Autonomous & Agentic Workflows
- [Planner-as-Router: Fold the Model Choice Into the Plan](/planner-as-router-fold-the-model-choice-into-the-plan/) — more on Autonomous & Agentic Workflows
<!-- internal-links:end -->

## Sources
- [1] Mou, Xue, Li, Liu, Zhang, Ye & Shao, "ToolSafe: Enhancing Tool Invocation Safety of LLM-based agents via Proactive Step-level Guardrail and Feedback", Findings of ACL 2026 — https://aclanthology.org/2026.findings-acl.1850/
- [2] "CARE: Pre-Execution Command Verification for Shell-Executing LLM Agents", arXiv:2607.21642v2 — https://arxiv.org/html/2607.21642v2
- [3] CARE, abstract and Section V, same paper — https://arxiv.org/html/2607.21642v2
- [4] "Verified Tool Calls Improve LLM Agent Reliability Under Non-Atomic Failures", arXiv:2608.02645v1 — https://arxiv.org/html/2608.02645v1
- [5] "Verification as an Architectural Layer for LLM Agents", arXiv:2609.31937v1 — https://arxiv.org/html/2609.31937v1
