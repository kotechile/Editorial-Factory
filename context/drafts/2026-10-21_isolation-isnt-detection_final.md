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
meta_title: "Silent Errors Halve Agent Success: 33.6% Noticed at Best"
meta_description: "Meta's contained agent design bounds failures that announce themselves. A new benchmark finds the failure that halves agent success arrives with no signal at all."
---

<!-- lead -->
Meta published how it builds agents for its data pipelines, and the reliability property it claims is containment [1]. A day later, a new test measured the failure class that containment cannot see [2]. Silent errors roughly halve task success across ten models, and the best model noticed the bad value in only 33.6% of runs [2].

If one worker fails, the router retries or escalates, and the failure does not spread to the others [1]. Meta's router is 1,300 lines. It sends more than 20 workflows to 14 specialist agents, and it does no domain work itself [1].

<!-- tension -->

## The big picture:

Meta split up its system for a good reason. One giant agent loaded with too much knowledge started to make things up [1]. Past a certain limit, adding facts made the agent worse. It began mixing up rules from different systems [1].

With a hand-written prompt for each task, that big agent worked 70% to 80% of the time. Without help, it dropped down to 10% to 20% [1]. So Meta split the work. Templates set the steps, and 14 separate agents handle the details [1].

The post says: "No agent sees the full picture. That's the feature, not the bug" [1]. I keep coming back to that line. It names the fix and the blind spot at the same time.

A silent error happens when no one crashes. The tool finishes the job. The answer fits the rules, but the data is wrong for the task [2]. For example, a profile tool says "local sports" at first. Later, it flips to "blockchain" because a user watched one video about fan tokens [2].

Both answers are valid text. But the wrong one sends the next steps down a useless path.

The Resilience to Incorrect Tool Evidence (RITE) test built 167 matched units across nine workflows [2]. Each unit carries a clean twin, an explicit-failure twin and the silent-error case at the same step. Testing ten models showed that silent errors roughly halve success [2]. They were harder to handle than failures that raise an error [2].

Models caught the bad data in only 20.8% to 33.6% of runs [2]. Most silent errors slip right by.

Under Meta's setup, this blind spot grows. The router only follows rules and never reads the actual data [1]. It checks for warnings or required reviewers, not wrong answers [1]. The worker that could check the data only sees its own small piece [1]. Keeping agents apart keeps a wrong answer neat. It never asks if the answer is true.

## By the numbers

- **1,300 lines — The router size:** Meta's router sends work to 14 specialists and does no domain work itself, relying on order and process checks [1].
- **Roughly half — The success drop:** Across 501 instances, a wrong answer that looked right cut task success by roughly half [2].
- **20.8% to 33.6% — The catch rate:** The share of runs across ten models that caught the bad data at all [2].
- **0.387 to 0.655 — The recovery jump:** The recovery score when a caught error was traced back to the tool that made it, compared to when it was not [2].

<!-- tactical-insight -->

## What I'd watch:

The work closest to this problem is moving to the tool edges. The results change based on what each check can see.

- **Checks on the call:** A setup that pulls rules from tool manuals and checks each call removed 59% to 87% of failed calls across models [5]. It lifted task success by 5.4 points under a 40-call budget. This checks the request, but silent errors hide in the response [5].
- **Checks on the value:** The RITE test asked the model to doubt every tool result. Agents noticed errors more often, but final success barely moved [2]. The real win is underneath: recovery hit 0.655 when a caught error was traced back to its maker, up from 0.387 when it was not [2].
- **Checks after the fact:** A vendor replayed 12 public agent incidents and stopped 14 of 15 harmful actions without writing a rule for any of them [4]. The one miss was a silent error. A bad package added a hidden recipient inside the mail server after the visible send had been approved [4].
- **Awareness as a skill:** In another test of computer-use agents, error awareness peaked at 44.0% across six agents [3]. Extra training lifted one model from 19.9% to 35.2% [3]. Training helps, but it is not reliable yet.

What I'm watching next is whether these split designs ever share a catch rate. Meta reports that configuration prep fell from three or four days by hand to under an hour, and that two-thirds of changes land without significant human edits [1]. A metric tracking false values caught per thousand calls would actually show if the setup works.

I also want to see where a value check could live without building a giant agent again. A workflow template knows its current step and what the last step sent back. A stateless gateway cannot make that check, and a router is not allowed to.

<!-- nuanced-takeaway -->

## The catch

The test setup is kinder than real life in one specific way. Each run breaks just one value, and asking the tool again brings back the clean truth [2]. The measured jump in recovery assumes a safe path back to the truth actually exists [2].

A tool that keeps lying, or a bug that spans several calls, falls outside this test [2]. The scores also come from a language-model judge, which the writers note can make mistakes [2].

Meanwhile, Meta's numbers are one team's own report, with no failure count and no catch rate [1]. The vendor test is the vendor's own product on incidents it picked itself, and its miss is disclosed rather than audited [4].

My read is that this shows a gap in coverage, not a failed design. Keeping agents apart buys real wins: a smaller blast radius, faster prep time, and most changes landing without a human edit [1].

Both designs make sense, but they fix different things. One limits the damage a broken worker can do. The other limits the damage a wrong answer can do. Right now, that wrong answer has no owner in either setup.

<!-- tldr -->

## At a glance

- **The Big Shift:** Meta shared a live agent system that works by moving all reasoning out of its router and into 14 separate workers [1]. A day later, a test found that a wrong answer with no crash signal cuts success in half and is caught in only 20.8% to 33.6% of runs [2].
- **Why It Matters:** Keeping agents apart limits the blast radius but hides the wider context needed to spot a bad answer. A team can pass every safety test and still ship a confident wrong answer at full speed.
- **What I'd Watch:** Whether split designs start sharing catch rates next to their speed metrics.
  - **A value check:** A test of the returned data against what the workflow expected, which needs state the gateway does not hold.
  - **A producer refetch:** Asking the tool that supplied a value again, which lifted recovery from 0.387 to 0.655 in the test [2].
  - **A constraint check:** A rules check on the shape of the request, which is cheap but blind to a wrong answer that fits the rules [5].
- **The Catch:** The test only breaks one value at a time and assumes asking again returns the truth, while Meta's numbers are a single team's self-reported case [1, 2].

## Sources

[1] Plawan Rath, Akhil Jindal and Ashwini Verma, "The Thin Orchestrator: How We Made Our AI Agents More Reliable by Giving the Router Less to Do", Engineering at Meta, 19 October 2026 — https://engineering.fb.com/2026/10/19/ml-applications/thin-orchestrator-ai-agent/
[2] "RITE: Evaluating End-to-End Resilience to Silent Tool Errors in E-Commerce Agentic Systems", arXiv:2610.27777, submitted 20 October 2026 — https://arxiv.org/abs/2610.27777
[3] "CUA-Recovery: Benchmarking Error Recovery in Long-Horizon Computer-Use Agents", arXiv:2610.27645, submitted 20 October 2026 — https://arxiv.org/abs/2610.27645
[4] "12 real AI agent incidents, replayed", Squidbrake benchmark, 21 October 2026 — https://squidbrake.com/benchmark
[5] "Symbolic Constraint Agents: Mining Formal Tool-Call Constraints to Prevent Agent Errors", arXiv:2610.25552, submitted 18 October 2026 — https://arxiv.org/abs/2610.25552

## Gate report
PASS — Lead is direct and punchy, delivering the core takeaway immediately in the first sentence using plain words.
PASS — Tension explains the architectural split and introduces the silent error problem clearly with everyday vocabulary and correct formatting.
PASS — Tactical insight observes operator actions without giving commands, strictly following bullet formatting and using simple phrasing.
PASS — Nuanced takeaway provides realistic trade-offs and acknowledges measurement limits with clear, accessible language.
PASS — TL;DR follows the 4-part Smart Brevity schema exactly, using simple sentences and separating cleanly with an H2.
