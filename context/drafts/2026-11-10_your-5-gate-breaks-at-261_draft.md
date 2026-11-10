---
title: Your 5% Gate Breaks at 26.1%
vertical: ai_observability_qa
kind: evergreen
archetype: evergreen
evergreen: true
persona: evals_infra_eng
one_big_thing: "A gate's false-positive rate is set by how many times you look, not by the threshold you set — so an eval or canary that can be stopped early needs an interval valid at every look, or a horizon fixed in advance, and never a 0.95 posterior threshold read as a switch."
date: 2026-11-10
slug: your-5-gate-breaks-at-261
meta_title: "Your 5% Gate Breaks at 26.1%"
meta_description: "A 5% gate is a promise about one look at the data. Check a running eval after every case and the same gate found a winner 26.1% of the time on identical arms."
---

<!-- lead -->
Your eval gate says 5%, and that number is true only once. It holds when you read the score once, at the end of a run whose case count you fixed in advance. Stop the run at the first result that clears the bar, and the same gate breaks. On two identical arms it found a "significant" difference 26.1% of the time [2]. Streaming evals and live canary dashboards have made that broken gate the default one.

<!-- tldr -->

## At a glance

- **The shift:** Evals are watched while they run, so a gate gets consulted many times, not once.
- **The number:** 26.1% found a winner on identical arms once the run could stop early [2].
- **The risk:** An interval built for one look stops meaning anything at the second.

<!-- tension -->

## Why the fifth look differs

Evan Miller worked this out in April 2010. Dashboards refreshed after every order then, and teams stopped tests as soon as the number looked good. Adrian Molas ran the Bayesian version of the same experiment on 30 October 2025, and found the shortcut no safer. In August 2026 a UK AI Security Institute preprint reversed the question. Rather than ask how many looks spoil a threshold, it asked when a run may honestly be stopped [1].

The mechanism is the sampling plan, not the statistics software. A false-positive rate — how often a gate calls a difference that is not there — holds only when the number of cases is fixed before the data arrives. Every extra look is another chance to cross the bar, and the looks feed on each other.

Miller's table shows how big the effect is. With ten looks at a running experiment, a dashboard has to read 1.0% for the real error rate to be 5% [2]. The part I keep circling is that nobody sets a gate to 1.0%. The ten-look gate keeps its label and loses its meaning.

The Bayesian turn is where most teams believe they have escaped. A posterior probability — the chance, given the data so far, that one version is better — stays readable at any sample size, which is a real advantage. It is not a licence to stop on success. Molas ran a simulation with two arms at the same conversion rate, checked the posterior every hundred cases, and stopped whenever it passed 0.95. The false-positive rate reached 80% [3]. His conclusion is narrower than the shortcut, and worth keeping in his words: the posterior stays readable under continuous monitoring, but a fixed threshold does not control false positives when you peek and stop on success [3].

An eval harness adds speed to that problem. A few hundred cases finish in minutes, so the score is legible long before it is complete. The interval that [how many cases a 95% gate actually needs](/100-case-eval-925-coverage/) tells you to print assumes exactly one look.

## By the numbers

- **80% false positives:** Molas's Bayesian gate at a 0.95 threshold, checked every 100 cases on two arms that behave the same [3].
- **57% to 97% of planned trials:** what a precision-based stopping rule removed across nine validation settings [1].

<!-- tactical-insight -->

## Where this lands in a harness

Two fixes exist, and they are not interchangeable. The first is to stop looking: fix the case count in advance and report the interval that belongs to that one look. Mid-run readings become progress indicators rather than decisions. Miller's rule of thumb for the fixed sample is sixteen times the variance over the square of the smallest gap worth detecting [2]. For a pass rate, the cases you need grow fast as the gap you care about narrows.

The second fix keeps looking and changes the instrument. An interval that stays valid at any stopping time is a different object from one computed at a fixed sample size. Johari, Pekelis and Walsh call that property always valid, and it lets a team act on data as it comes in without losing the promise [4]. The 2026 preprint carries the idea into an eval harness as a precision rule: sample the cases where uncertainty is highest, stop where the estimate is tight enough [1].

What I find hard to square is how often the safeguard is the part teams drop. That rule samples more cautiously as measured performance approaches zero, because a suite near the floor turns on a handful of successes [1]. A stopping policy tuned on a healthy pass rate will misbehave on the suite that matters most.

<!-- nuanced-takeaway -->

## The catch

The 57% to 97% range belongs to one example design: a 200-item set run to ten epochs, reported in a single-author preprint [1]. The paper says the savings depend on how the evaluation is built. A suite of independent, expensive cases will not save as much as a fixed plan that repeats cheap items an estimate never needed.

I keep returning to the width. An interval that stays honest across every look is wider than one made at the end. A team that adopts it loses some of the detail its old dashboard appeared to have, and part of that detail was the artifact. Miller's 26.1% is likewise one setting, a test after every observation with a 150-observation cap, and he calls it close to a worst case [2].

What survives is the plain question to ask of any number a gate prints: how many times was it allowed to move before somebody acted on it. A rate that describes a model cannot be separated from the schedule that produced it. The schedule is the part a team controls.

## Sources

- [1] Toby D. Pilditch, "Knowing When to Stop: Bayesian Optimal Stopping for LLM Evaluations" (arXiv:2608.14425v1, 14 August 2026) — https://arxiv.org/html/2608.14425v1
- [2] Evan Miller, "How Not To Run an A/B Test" (18 April 2010) — https://www.evanmiller.org/how-not-to-run-an-ab-test.html
- [3] Adrián Molas, "Bayesian A/B testing is not immune to peeking" (30 October 2025) — https://www.alexmolas.com/2025/10/30/bayesian-ab-test-peeking.html
- [4] Ramesh Johari, Leo Pekelis and David J. Walsh, "Always Valid Inference: Bringing Sequential Analysis to A/B Testing" (arXiv:1512.04922) — https://arxiv.org/abs/1512.04922
