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
image_path: "context/assets/illustrations/your-5-gate-breaks-at-261/featured.jpg"
image_style: "long_lens_industry"
image_model: "flux"
image_alt: "Your 5% Gate Breaks At 26.1%. A row of industrial inspection gates in a data hall, one propped ajar by a yellow stop-wedge."
image_caption: "Your 5% Gate Breaks At 26.1%: Reading after every case turns a 5% gate into a 26.1% false-positive rate."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->

Your eval gate says 5%, and that number is true only once. It holds when you read the score once, at the end of a run whose case count you fixed in advance. Stop the run at the first result that clears the bar, and the same gate breaks. On two identical arms it found a "significant" difference 26.1% of the time [2]. Streaming evals and live canary dashboards have made that broken gate the default one.

<!-- tldr -->

## At a glance

- **The shift:** Evals are watched while they run, so a gate gets consulted many times instead of once.
- **The number:** 26.1% on arms that were the same, once the run could stop early [2].
- **The risk:** An interval built for one look means nothing at the second.

<!-- tension -->

## Why the fifth look differs

Evan Miller worked this out in April 2010. Dashboards refreshed after every order then, and teams stopped tests as soon as the number looked good. Adrián Molas asked the same question with a Bayesian simulation on 30 October 2025, and found the shortcut no safer. In August 2026, a UK AI Security Institute preprint reversed the question. Instead of asking how many looks spoil a threshold, it asked when a run may be stopped honestly [1].

The mechanism is the sampling plan, not the software. A false-positive rate — how often a gate calls a difference that is not there — holds only when the case count is fixed first. Every extra look is another chance to cross the bar, and one chance changes the odds for the next. A test read after every case is not the test that was designed.

Miller's table shows how large the effect is: with ten looks at a running test, a dashboard has to read 1.0% for the real error rate to be 5% [2]. I read that row three times before I believed it. Nobody sets a gate to 1.0%, so the ten-look gate keeps its label and loses its meaning.

A Bayesian posterior probability looks like an escape. It stays readable at any sample size, a real plus, but it does not make stopping on success safe. Molas ran a simulation with two arms at the same conversion rate, checked the posterior every hundred cases, and stopped whenever it passed 0.95. The false-positive rate reached 80% [3]. His conclusion is narrower than that. The posterior stays readable under continuous monitoring, but a fixed threshold does not control false positives when you stop on success [3].

An eval harness adds speed to that problem: a few hundred cases finish in minutes, so the score is legible long before the run is complete. The sums behind [how many cases a 95% gate actually needs](/100-case-eval-925-coverage/) assume exactly one look.

## By the numbers

- **80% false positives:** Molas's Bayesian gate at a 0.95 threshold, checked every 100 cases on two arms that behave the same [3].
- **57% to 97% of planned trials:** what a precision-based stopping rule removed across nine validation settings [1].
- **16 times the variance:** Miller's rule of thumb for the sample a fixed-horizon gate needs [2].

<!-- tactical-insight -->

## Where this lands in a harness

Harness teams have two fixes, and they are not interchangeable. Some stop looking: they fix the case count in advance and report the interval that belongs to that one look. Mid-run readings become progress indicators rather than decisions. Miller's fixed-sample rule gives that count directly; for a pass rate, the cases needed grow fast as the smallest difference worth detecting narrows [2].

Other teams keep looking and change the instrument. An interval that stays valid at any stopping time is a different object from one computed at a fixed sample size. Johari, Pekelis and Walsh call that property always valid; it lets a team act on data as it comes in without losing the promise [4]. The 2026 preprint works differently. It treats an eval as a sequence of measurements, samples where uncertainty is high, and stops where the estimate is tight [1].

I would watch the safeguard more than the stopping rule. It samples more cautiously as measured performance nears zero, because a suite near the floor turns on a handful of successes [1]. The open question is whether that safeguard holds on a real suite whose pass rate is near zero.

<!-- nuanced-takeaway -->

## The catch

The savings range in that paper belongs to one example design: a 200-item set run to ten epochs, reported in a single-author preprint [1]. The paper says the savings depend on how the eval is built. A suite of independent, costly cases may not save as much as a fixed plan that repeats cheap items once the estimate is tight.

I think the width is the actual product, not a drawback. Any interval that stays honest across every look is wider than one made at the end. When a team adopts it, some of the detail its old dashboard appeared to have disappears, and part of that detail was noise. Miller's 26.1% is likewise one setting: a test after every observation with a 150-observation cap, which he calls close to a worst case [2].

The question to ask of any number a gate prints is plain: how many times was it allowed to move before somebody acted on it? A rate that describes a model cannot be separated from the number of looks that produced it. The number of looks is the part a team controls.

## Sources

- [1] Toby D. Pilditch, "Knowing When to Stop: Bayesian Optimal Stopping for LLM Evaluations" (arXiv:2608.14425v1, 14 August 2026) — https://arxiv.org/html/2608.14425v1
- [2] Evan Miller, "How Not To Run an A/B Test" (18 April 2010) — https://www.evanmiller.org/how-not-to-run-an-ab-test.html
- [3] Adrián Molas, "Bayesian A/B testing is not immune to peeking" (30 October 2025) — https://www.alexmolas.com/2025/10/30/bayesian-ab-test-peeking.html
- [4] Ramesh Johari, Leo Pekelis and David J. Walsh, "Always Valid Inference: Bringing Sequential Analysis to A/B Testing" (arXiv:1512.04922) — https://arxiv.org/abs/1512.04922
