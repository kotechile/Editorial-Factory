---
title: "Silent Errors Halve Agent Success: 33.6% Noticed at Best"
vertical: agentic_resilience_failure
persona: infra_engineer
one_big_thing: "Meta's contained, isolated agent design bounds a failure that announces itself, but the dominant measured failure in agent workflows is a schema-valid wrong value that roughly halves task success and is noticed in only 20.8% to 33.6% of rollouts, so detection belongs in a state check at the tool boundary rather than in the router or the prompt."
date: 2026-10-21
slug: isolation-isnt-detection
synthesis: true
sources:
  - https://engineering.fb.com/2026/10/19/ml-applications/thin-orchestrator-ai-agent/
  - https://arxiv.org/abs/2610.27777
meta_title: "Silent Errors Halve Agent Success: 33.6% Noticed"
meta_description: "Meta's contained agent design bounds failures that announce themselves. A new benchmark finds the failure that halves agent success arrives with no signal at all."
---

<!-- lead -->
One day apart, Meta published a production agent system whose reliability claim is containment, and a benchmark measured the failure class that containment cannot see [1, 2]. In the benchmark, a tool returned a value that passed its schema and was wrong [2]. Silent errors halved agent task success across ten models, and the best model noticed the bad value in 33.6% of runs [2].

Meta's router is 1,300 lines. It sends more than 20 workflows to 14 specialist agents, and it does no domain work itself. If a worker fails, the router retries or escalates, and the failure does not touch the other workers' state [1].

<!-- tension -->

## The big picture:

The split at Meta was well founded. One agent loaded with every subsystem's knowledge began to invent. Past a certain context limit, "additional knowledge degraded rather than improved performance", and it carried naming rules from one system into another [1].

That agent held 70-80% success with a hand-written prompt for each task. Without that help it fell to 10-20% [1]. So the work became two layers. Templates set the order. Fourteen agents own the domain detail.

In the post's own words: "No agent sees the full picture. That's the feature, not the bug" [1]. I keep coming back to that line, because it names the fix and the blind spot in one breath.

A silent error is the case where nobody fails. The tool call completes. The response matches the schema, and the value is wrong for this task, with nothing in the response to say so [2]. The paper's example is a profile tool that answers "local sports" at build time and "blockchain" after a change, because one video mentioned fan tokens [2].

Both answers are valid strings. One of them sends the next six steps somewhere useless.

The measurement is the part that should worry a platform team. RITE (Resilience to Incorrect Tool Evidence) built 167 matched units across nine workflows, 501 instances in all [2]. Each one has a clean twin and an explicit-failure twin at the same step. Ten current models ran them.

Silent errors cut success by about half, and they were harder than failures that raise an error [2].

The share of runs that noticed the bad value at all ran from 20.8% to 33.6% [2]. The authors put it plainly: most silent errors go unrecognized.

Under Meta's design, the picture is worse. The router is rule-based and reads no domain values, by design [1]. Its gate checks for "active warnings or required reviewers", which is a process check, not a value check [1]. The worker that could compare a value against its own domain sees one subsystem and never the others [1]. Containment keeps a wrong value tidy. It does not ask whether the value is right.

## By the numbers

- **1,300 lines, 14 agents — the containment design:** the router sends 20+ workflows to 14 specialists and does no domain work itself, so order and a warnings-and-reviewers gate are all that sit in the centre [1].
- **Roughly half — the silent-error cost:** across 501 instances in nine workflows and ten current models, a plausible wrong value cut task success by about half and proved harder than an explicit failure [2].
- **20.8% to 33.6% — noticed:** the share of runs that flagged the bad value at all, with the paper concluding that most silent errors go unrecognized [2].
- **0.387 to 0.655 — recovery with a refetch:** the recovery score when a noticed error was traced back to the tool that produced it, against when it was not [2].

<!-- tactical-insight -->

## What I'd watch:

The teams closest to this are moving to the tool boundary, and the evidence splits by what each control can see.

- **Checks on the call:** a framework that mines formal rules from tool docs and checks each call with a solver removed 59-87% of failed calls across models [5]. It also lifted task success by 5.4 points under a 40-call budget. That is a real gain, and it still validates the request, while the silent error arrives in the response.
- **Checks on the value:** RITE's own fix asked the model to treat every tool result as suspect before using it. It raised how often agents noticed and re-queried, and moved final success only a little [2]. The useful number sits underneath: recovery ran at 0.387 when a noticed error was not traced back to its producer, and 0.655 when it was [2].
- **Checks after the fact:** a vendor's replay of 12 public agent incidents stopped 14 of 15 harmful actions, with rules written for none of them [4]. The one it missed is this case. A bad package added a hidden recipient inside the mail server, after the visible send had been approved, so the approver saw a normal message and said yes [4].
- **Awareness as a trained skill:** on a second test of computer-use agents, error awareness topped out at 44.0% across six agents and six takeover depths, and fine-tuning lifted one model from 19.9% to 35.2% [3]. Training helps. It lands well short of reliable.

What I'm watching next is whether these designs publish a detection rate at all. Meta's post reports prep time and the share of changes that land without edits, which are honest production numbers [1]. A false value caught per thousand calls is the number that would tell a reader whether the isolation catches anything, and nobody in this window published it.

The second thing I'd want answered is where a value check could live without rebuilding the fat agent. A workflow template already knows its step and what the last step returned. That is a comparison a stateless gateway cannot make and a router is not allowed to make.

<!-- nuanced-takeaway -->

## The catch:

The benchmark's setup is kinder than production in one specific way. Each instance corrupts a single value, and re-querying the producing tool returns the clean answer. So the measured 0.387 to 0.655 assumes a trustworthy path back to the truth exists [2].

A tool that keeps lying, or a fault that spans several calls, is outside the measurement [2]. The scores also come from a language-model judge, which the authors flag as a source of error in absolute numbers [2].

Meta's numbers are one team's production case, reported by that team, with no failure count and no detection rate [1]. The vendor replay is the vendor's own product on incidents it picked, and its one miss is disclosed rather than audited [4].

My read is that this is a coverage gap, not a refutation. Containment buys real things: a smaller blast radius, a shorter prep time, and two-thirds of changes landing without a human edit [1].

Both designs are reasonable, and they optimise different failures. One bounds the damage a broken worker can do. The other would bound the damage a wrong answer can do, and that one has no owner in either design.

<!-- tldr -->

## At a glance

- **The Big Shift:** Meta documented a production agent system that got reliable by moving all domain reasoning out of its router and into 14 isolated specialists, with containment as the stated reliability property [1]. A day later, a benchmark found that the failure which roughly halves agent task success is a plausible wrong value with no failure signal, noticed in only 20.8% to 33.6% of runs [2].
- **Why It Matters:** Isolation limits blast radius and removes the cross-system context in which a wrong value might look wrong, while the router is built to read no domain values. A team can pass every containment test and still ship a wrong answer at full speed.
- **What I'd Watch:** whether containment designs start publishing a detection rate beside their prep-time numbers.
  - **A value check:** a comparison of the returned value against what the workflow expected at that step, which needs state the gateway does not hold.
  - **A producer refetch:** re-querying the tool that supplied a value, the move that lifted recovery from 0.387 to 0.655 in the benchmark [2].
  - **A constraint check:** a solver test on the shape of the request, which is cheap and real but blind to a schema-valid wrong answer [5].
- **The Catch:** the benchmark corrupts one value at a time and assumes re-querying returns the truth, its scores come from a language-model judge, and Meta's figures are one team's self-reported production case [1, 2].

## Sources

[1] Plawan Rath, Akhil Jindal and Ashwini Verma, "The Thin Orchestrator: How We Made Our AI Agents More Reliable by Giving the Router Less to Do", Engineering at Meta, 19 October 2026 — https://engineering.fb.com/2026/10/19/ml-applications/thin-orchestrator-ai-agent/
[2] "RITE: Evaluating End-to-End Resilience to Silent Tool Errors in E-Commerce Agentic Systems", arXiv:2610.27777, submitted 20 October 2026 — https://arxiv.org/abs/2610.27777
[3] "CUA-Recovery: Benchmarking Error Recovery in Long-Horizon Computer-Use Agents", arXiv:2610.27645, submitted 20 October 2026 — https://arxiv.org/abs/2610.27645
[4] "12 real AI agent incidents, replayed", Squidbrake benchmark, 21 October 2026 — https://squidbrake.com/benchmark
[5] "Symbolic Constraint Agents: Mining Formal Tool-Call Constraints to Prevent Agent Errors", arXiv:2610.25552, submitted 18 October 2026 — https://arxiv.org/abs/2610.25552
