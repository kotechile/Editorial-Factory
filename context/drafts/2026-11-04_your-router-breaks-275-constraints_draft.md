---
title: "Your Router Breaks 275 Rules"
vertical: multi_agent_enterprise_fabric
kind: evergreen
persona: ai_architect
one_big_thing: "An agent fabric's reliability is set by how much of the request path is code rather than by the model in it: a written blueprint beat the strongest agent baseline 35.56% to 18.00% on the same model with 96% fewer broken constraints, and Meta's production router keeps six of seven steps in code while taking setup for a new column from days to under an hour."
date: 2026-11-04
slug: your-router-breaks-275-constraints
archetype: evergreen
evergreen: true
---

<!-- lead -->
A router that lets the model choose each step breaks 275 planning rules on the TravelPlanner test, against 11 for the same work run as written code [1]. The written version also passed 35.56% of the tasks, against 18.00% for its loosest rival [1]. Both called the same Claude Sonnet 4 model, so the gap is not in what the model can do [1]. It is in who owned the order of the steps.

<!-- tension -->

## The model answers a settled question

Meta's agent platform made that cut explicit in production. Its router is 1,300 lines that send 20+ workflows to 14 specialist agents, and it does no domain work itself: it never reasons about code, writes a config or touches the codebase [2]. Each request follows a fixed seven-step path, and steps one to five and seven are plain code [2]. Only the sixth, the hand-off to a specialist, calls a model, and that call runs in its own agent holding one domain's knowledge [2].

The templates are the part worth copying. Meta calls them state machines that constrain the model's decision space, which is a stronger claim than a well-written prompt [2]. The model is never asked what to do next. It is asked one narrow question inside a step whose inputs the code has already gathered and checked.

For a fabric in front of a finance system, the same cut decides where the duplicate check, the field check and the approval gate sit. Put them in a planner's prompt and they are decided again on every request. Put them in a step and they run every time. What I keep circling is that the reliability here is not about how smart the model is. It is about how little each model call has to hold.

## By the numbers

- **70-80% — Single agent, hand-tuned:** Meta's single-agent option reached that rate only with a prompt built for each task, and fell to 10-20% without one [2].
- **65-fold — Token gap under load:** at 80-task batches the split runs used up to 65-fold fewer tokens than the single agent [3].
- **27.1% — Steps saved:** the blueprint finished TravelPlanner in 10.2 steps against 14.0 for the strongest agent baseline [1].

<!-- tactical-insight -->

## Where the cut pays and costs

The change bill arrives before the accuracy gain. Setting up a new column took three to four days by hand and about a day with Meta's earlier config-driven system; the thin router gets it under an hour [2]. About two-thirds of the system's changes now land without much human editing [2]. Adding a workflow is the cost a fabric pays again and again, and it is the number I take into a design review.

Meta's answer was reuse. The same specialists run in a different order for each use case, so a new workflow meant a new template and no new agent code [2]. The teams closest to this stop treating a workflow as a prompt and start treating it as a plan the code can run, so the routing layer stops growing with each integration.

The governance standard points the same way. The design tenets from the US National Institute of Standards and Technology make hard-coded checks the main way an agent gets an access decision, with model output as an input only, and they say that guardrails alone are not enough [4]. The checks between steps still decide whether a wrong one spreads, which is [what a gate between agent steps is for](/gate-the-step-not-the-model/).

<!-- nuanced-takeaway -->

## The catch

The paper is honest about where the cut stops paying. On an open-ended test whose tasks need a kind of digging that a fixed plan cannot predict, the blueprint's edge shrank from raw success to speed and consistency [1]. The design pays in proportion to how well the steps can be known ahead of time, which leaves out the work nobody has written down yet.

The batch result has the same edge. Splitting the work adds a fixed cost in extra calls and repeated prompts, and at small batches it can raise both tokens and latency before the split pays off [3]. At five tasks the two designs start close, at 90.6% for the split runs against 73.1% for the single agent. By eighty tasks the single agent had fallen to 16.6% while the split runs held 65.3% [3].

My read, held loosely: this measures something other than the desk's earlier finding that a wide fan-out costs money. A fan-out sends several branches out and multiplies the context each one carries; a split of the same work divides that context instead. One buys reach, the other buys room under load, and a fabric that confuses them buys the wrong one.

<!-- tldr -->

## At a glance

**The shift:** Fabric teams are moving the order of steps out of the model and into code, leaving it one narrow job.
**The number:** 35.56% of tasks passed on the blueprint, against 18.00% for the strongest agent design.
**The risk:** The gain fades where the steps cannot be known in advance.

## Sources
[1] Libin Qiu, Yuhang Ye, Zhirong Gao et al., "Blueprint First, Model Second: A Framework for Deterministic LLM Workflow" (arXiv:2508.02721v2, revised 16 June 2026) — https://arxiv.org/html/2508.02721v2
[2] Meta Engineering, "The Thin Orchestrator: How We Made Our AI Agents More Reliable by Giving the Router Less to Do" (19 October 2026) — https://engineering.fb.com/2026/10/19/ml-applications/thin-orchestrator-ai-agent-architecture/
[3] Eyal Klang, Mahmud Omar, Ganesh Raut et al., "Orchestrated multi agents sustain accuracy under clinical-scale workloads compared to a single agent" (npj Health Systems 3, article 23, 9 March 2026) — https://www.nature.com/articles/s44401-026-00077-0
[4] National Institute of Standards and Technology, "Design Tenets for Agent Identity Management Systems" (27 October 2026) — https://www.nist.gov/blogs/cybersecurity-insights/design-tenets-agent-identity-management-systems
