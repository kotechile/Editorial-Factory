---
title: "Your 90% Restart Monitor Proves Nothing"
vertical: agentic_resilience_failure
persona: infra_engineer
one_big_thing: "Whether to restart a failing agent run is a purchase, and its price is the replacement run's own chance of finishing on the calls the abandoned run gives back — a number no monitor accuracy figure reports, which is why 103 live restart decisions in the one published audit could not be certified either way."
date: 2026-10-28
slug: your-90-restart-monitor-proves-nothing
---

<!-- lead -->
Every alarm tool ships with one number on the box, and for your stack it is the wrong number. An alarm that sorts failing runs at a 90% hit rate sounds fine [1]. In task success it can land anywhere from a five-point loss to a 35-point gain [1]. What moves it is the substitute run's chance of passing with the calls the abandoned run gives back, and no sorter reports that [1]. Jain and Vedam, at Intuit, derive the swing as an identity rather than a tracked metric, then audit their own traces [1]. They found 103 live reset choices, and not one could be certified either way, so the hit rate proves nothing about what the alarm sets off [1].

<!-- tension -->

## The big picture:

The recovery tooling is arriving faster than anyone can price it. DeltaBox Lite open-sourced an abort-and-commit sandbox for coding agents on 16 October [5]. Five days later it shipped a Windows build, and its own notes call it Git for agent sessions [5]. Every change an agent makes can be reviewed, committed or aborted, per task or per tool call [5]. That is a snapshot on every safe edge, the policy the only logged study prices at a loss one step past the first cut [2].

I see three papers this week tracking the three calls a recovering harness makes [1][2][3]. They cover whether to drop a run, where to cut a save state, and whether an error needs a person [1][2][3]. Each one finds the usual gauge pointing away from what the choice is worth. Jain and Vedam name the missing number restartability [1]. It is the chance that one clean boot still finishes, starting over with the calls that are left [1]. Starting over pays only when that beats the current run's own chance of passing, and no tool reports either [1].

The team that gains is the one holding full traces, because the audit needs no extra model calls [1]. It runs over what the team already recorded. The team exposed is the one that bought a reset add-on using a sensor score chart [1]. Its reliability review says how many faults the watcher caught, and never asks what the resets earned [1].

## By the numbers

- **−5 to +35 points — Same tool, two outcomes:** one 90% alarm covers both ends, resting on the next try's chance of passing [1].
- **0 of 103 — Certified restart calls:** the review rests on 194 runs across 19 issues from live software tasks with hidden tests [1].
- **100.0 s then −1.1 s — Checkpoint value:** the first cut yielded 100.0 s on 156.5 s of protected work, and the next returned −1.1 s on 41.8 s [2].
- **725 of 1,403 — Errors that fixed themselves:** tallied across 1,259 agent traces, usually in just a few steps [3].

<!-- tactical-insight -->

## What I'd watch:

What I am watching next is whether the add-on ships a value figure or only a sensor score.

- **Hit rates on reset tools:** DeltaBox states a design and gives no value figure, which is fair for a building block and thin for a purchase [5].
- **Tests with room to recover:** one cohort gave no live call at all, because the run finished before the alarm [1]. Another yielded many faults and no fresh finish inside 14 calls [1].
- **Reversibility as the routing term:** pulling it out raised harmful runs from 7.02% to 15.53%, inside a simulation where the repair step is assumed rather than tracked [4].
- **Where a threshold comes from:** the timeout case already has an answer, where [Agent Timeouts: Pick 0.1%, Not a Round Number](/agent-timeout-false-alarm-budget/) sets its alarm budget using a rate an operator will tolerate.

<!-- nuanced-takeaway -->

## The catch

The alarm study covers 19 issues from one repository, one harness and five tries per task [1]. Its 103-choice review ran after the tests, not before them [1]. The snapshot study is 12 tasks across three repositories, on one agent and one model version [2]. Its authors call it a pilot, so the direction travels and the sizes do not.

A 42.29-point loss on a second model is a warning about shifting a cutoff, not a forecast for your traffic [1]. My reading of the zero of 103 is that the evidence never settled the sign [1]. It is not a finding that starting over never helps, which the authors decline to claim [1].

<!-- tldr -->

## At a glance

- **The Big Shift:** The choice to reset now has arithmetic, and it does not run on sorter scores. A 90% alarm can lose five points or gain thirty-five, on what the next try can still win.
- **Why It Matters:** Recovery is sold as an add-on, with abort and commit on every call, while the only logged study prices the second cut at worse than useless. Teams buy the tool and inherit a choice they cannot value.
- **What I'd Watch:**
  - **Value figures on the tool:** whether a vendor can show, from a customer's own traces, what a fresh run earned against carrying on, rather than how well its sensor sorted faults.
  - **Tests with room to recover:** a set full of faults proves nothing if no run could have passed after a reset, which is what happened to one cohort here.
  - **Self-recovery rates:** just over half the errors in the timing study cleared on their own, so a reset rule fires mostly on errors that were about to fix themselves.
- **The Catch:** Nineteen chosen issues and twelve pilot tasks are direction, not fit to your traffic. The audit leaves the sign of a reset's value unproven at these sizes.

## Sources

[1] S. Jain and V. N. Vedam, "Monitor Accuracy Isn't the Answer: A Decision-Value Framework for Evaluating AI Agent Restart Monitors," Intuit, arXiv:2610.36544, submitted 2026-10-27 — https://arxiv.org/abs/2610.36544

[2] M. Akewar and R. Ranjan, "RippleCP: Measuring Counterfactual Checkpoint Advantage in Coding Agents," Florida International University, arXiv:2610.09088, submitted 2026-10-06 — https://arxiv.org/abs/2610.09088

[3] "When to Intervene? An Empirical Study of Errors and Self-Recovery in LLM Agents," arXiv:2610.36471, submitted 2026-10-27 — https://arxiv.org/abs/2610.36471

[4] "CASEL: Consequence-Aware Selective Execution for Reliable Long-Horizon Tool-Using Agents," arXiv:2610.36570, submitted 2026-10-27 — https://arxiv.org/abs/2610.36570

[5] DeltaBox Lite, `delta-box/deltabox-lite`, project notes, changelog entry 2026-10-16 — https://github.com/delta-box/deltabox-lite
