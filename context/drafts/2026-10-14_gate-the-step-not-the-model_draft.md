---
title: "Your Agent's Next Step: 11-14x Likelier to Fail"
vertical: agentic_resilience_failure
persona: infra_engineer
one_big_thing: "An agent's end-to-end reliability is set at the boundary between its steps, not inside the model — one wrong step makes the next roughly 11 to 14 times likelier to be wrong, recovery fails in most runs, and the boundary controls with measured effect (89% less cascade spread, 64% smaller blast radius, 71% faster recovery at three or more patterns) are the cheapest reliability purchase available."
date: 2026-10-14
slug: gate-the-step-not-the-model
archetype: evergreen
evergreen: true
---

<!-- lead -->
One wrong step does not stay one mistake. In a study of 2,518 agent runs, a single wrong step made the next step roughly 11 to 14 times likelier to fail, so your agent's next step is where the error lands [1]. The same study found the agent recovered from its first mistake in only 30.5% of runs. In 38.5% of them it never noticed the error at all, and the run carried on looking correct [1].

<!-- tension -->

## The big picture:

Most reliability work on agents has been aimed at the model. The 2026 evidence keeps pointing at the seams between steps instead.

A catalogue of 150 production incidents found the failures cluster at component boundaries. An error crosses a boundary and spreads. Quality drops with no alarm raised. Individually correct parts agree on a wrong answer together [3].

What strikes me is where the controls that worked sit. They act on the seam, not on the model. Circuit breakers cut cascade spread by 89% in controlled tests. Output gates caught 73% of the quiet quality loss. Separating components cut the blast radius by 64% [3]. Teams running three or more of these controls cut their mean time to recovery (MTTR) by 71% [3].

None of that shows up in the outcome. One operator's eight-week postmortem corpus of 22 incidents found every one had a silent phase: the system was already failing while every automated check stayed green [2]. About 70% were caught by a person reading the output, not by unit tests, health checks or audits [2].

The way a small fault becomes an outage is old news. Google's site reliability book works the arithmetic: let 5% of requests stop completing and sit on a 100-second deadline, and they eat the whole 1,000-thread pool of a frontend. Only 19.6% of requests get served, so the error rate lands at 80.4% [5]. On an agent, the shared pool is the chain of steps that trust the ones before them.

## By the numbers

- **11 to 14 times — Next-step penalty:** After one wrong step, the next step is roughly 11 to 14 times likelier to be wrong, so the later a run goes, the more of it is inherited error [1].
- **30.5% — Recovery after a first mistake:** The share of runs where the agent recovers from its first error; in 38.5% of runs it never detects the error at all [1].
- **89% — Cascade spread cut:** The reduction in cascade propagation from circuit breakers in controlled fault-injection tests, against 64% for component isolation and 73% of silent quality loss caught by output gates [3].
- **3.1% — Containment with enforcement removed:** Take out quarantine and rollback and containment falls to 3.1%, close to the 2.2% of running no defense at all, while that run spends the most tokens of any variant [4].

<!-- tactical-insight -->

## What I'd watch:

I keep coming back to the order of the controls, because the ablation is blunt about it. Taking out screening and verification lowers containment, and taking out quarantine and rollback lowers it further [4]. Screening without enforcement spent the most tokens of any variant, 34,991, and contained almost nothing [4].

So the thing I am watching is where teams put the gate, and whether it can actually stop a step.

- **A gate between stages:** A check on one stage's output before the next stage reads it, rather than a check on the final answer, which is the only place a compounding error can be stopped cheaply.
- **A quarantine path:** Somewhere for a suspect step's output to go that is not the next step's input, since rollback is the control whose removal costs the most containment [4].
- **A containment rate, not a verdict:** Scoring a release by the share of injected faults that never reached the next stage, the way the six-framework study did, instead of judging the run by whether the task passed [4].
- **A small step-checker:** The same group trained a four-billion-parameter model to label each step right or wrong, and it beat six frontier judges at finding the first mistake [1]. I would want to know how many teams run a check like that against their own traces rather than reaching for a bigger generator.

One more signal worth tracking: 41.1% of surveyed engineers meet agent problems daily or more, and their top blocker is tracking state, ahead of debugging and cost [6]. That is the same complaint as the rest of this evidence, said from the other end.

<!-- nuanced-takeaway -->

## The catch

The figures here are directional, not a service-level agreement. I would treat the containment ladder as a shape worth copying, not a promise.

Three limits stand out. The 11 to 14 times figure comes from a lab study of trajectories that are close to real deployment, not from live traffic [1]. The fault-injection percentages come from controlled tests rather than field telemetry [3]. The ablation's spreads are enormous, with one variant swinging by 35 percentage points, so 3.1% is a direction and not an estimate [4]. The eight-week corpus, meanwhile, is one operator's system rather than a survey of many [2].

The practitioner survey has a softer problem. It is vendor-sponsored, by a company that sells durable execution, which is the very thing its respondents say they lack [6]. The finding still lines up with everything else here, but I would not quote it as neutral.

The last caveat is arithmetic. The 80.4% example assumes nothing else goes wrong [5]. Real systems shed load, time out early, or fall back to a cache. That is the point: containment is the extra assumption, and without it a small fault is free to become the outage.

<!-- tldr -->

## At a glance

- **The Big Shift:** Agent reliability is being measured in the wrong place. The 2026 evidence puts the failure at the boundary between steps: one wrong step makes the next roughly 11 to 14 times likelier to be wrong, and most runs never recover or even notice.
- **Why It Matters:** Boundary controls have measured effects, including 89% less cascade spread, a 64% smaller blast radius, 73% of silent quality loss caught, and 71% faster recovery for teams running three or more of them. They are cheaper than the outage they prevent.
- **What I'd watch:** Whether containment becomes something teams measure rather than a pattern they claim. The signals:
  - **A stage gate:** A check on a stage's output before the next stage reads it, which is the cheapest place to stop an error from compounding.
  - **A containment rate:** The share of injected faults that never reach the next stage, scored per release instead of judging a run by whether the task passed.
  - **A small step-checker:** A cheap model that labels each step right or wrong, which out-found six frontier judges at locating the first mistake.
- **The Catch:** Every figure here is dated and bounded. The lab study is not production, the ablation swings by tens of points, the postmortem corpus is one operator's, and the survey is vendor-sponsored.

## Sources
[1] Salman Rahman et al., "Locating Hidden Failures Makes Long-Horizon Agents More Reliable" (Traverse), arXiv:2609.17930, 2026-09-15 — 2,518 trajectories and 6,967 mistakes classified into 78 failure types; the 11 to 14 times next-step compounding, recovery in 30.5% of runs, non-detection in 38.5%, and the four-billion-parameter "Scout" verifier that beat six frontier judges (https://arxiv.org/html/2609.17930v1)
[2] Wei Wu, "When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime", arXiv:2606.14589, 2026-06-12 — an eight-week window (2026-04-09 to 2026-06-02) with 22 incidents, every one carrying a silent phase, one meta-pattern appearing at least 28 times, roughly 70% found by human observation, and the 0% ex-ante / 87% ex-post governance audit (https://arxiv.org/html/2606.14589v1)
[3] "Compound AI System Reliability: A Failure Taxonomy and Resilience Pattern Catalog from 150 Production Incidents", arXiv:2610.02503, 2026-10-01 — 150 incidents, 23 failure modes across five categories, and controlled fault-injection effects: 89% less cascade propagation, 73% of silent degradation caught by output gates, 64% blast-radius reduction from isolation, and 71% off mean time to recovery at three or more patterns (https://arxiv.org/html/2610.02503v1)
[4] Yizhe Xie, Congcong Zhu, Xinyue Zhang et al., "From Spark to Fire: Modeling and Mitigating Error Cascades in LLM-Based Multi-Agent Collaboration", arXiv:2603.04474v2, 2026-05-11 — the containment ablation (14.4% ± 35.2 without screening and verification, 3.1% ± 10.1 without quarantine or rollback, 2.2% ± 14.7 with no defense) and the no-blocking variant's 34,991 tokens at 85.7 ± 21.0 seconds (https://arxiv.org/html/2603.04474v2)
[5] Google, "Site Reliability Engineering", chapter 22, "Addressing Cascading Failures" — the worked example in which 5% of requests sitting on a 100-second deadline consume 5,000 thread-seconds of a 1,000-thread frontend, leaving 19.6% of requests served and an 80.4% error rate (https://sre.google/sre-book/addressing-cascading-failures/)
[6] Temporal, "The State of Development 2026" — 554 respondents surveyed 2026-04-29 to 2026-05-25; 41.1% meet agent issues daily or more, 9.0% say continuously, and the top blocker to wider use is tracking state (https://temporal.io/reports/state-of-development-2026)
