---
title: "Your 100-Case Eval: 92.5% Coverage, Not 95%"
vertical: ai_observability_qa
persona: evals_infra_eng
one_big_thing: "A release gate's score answers one of two different questions, and the small suite that runs in CI cannot carry the plain 95% interval usually printed beside it: at 100 questions a nominal 95% interval held the true value only 92.5% of the time, and the question a ship-or-hold call needs — accuracy over the wider pool of similar cases — carries wider bars than the benchmark number on the label."
date: 2026-10-13
slug: 100-case-eval-925-coverage
archetype: evergreen
evergreen: true
meta_title: "Your 100-Case Eval: 92.5% Coverage, Not 95%"
meta_title_source: "derived_from_title"
meta_description: "Your 100-case eval prints one number. If it prints a bar at all, it calls that bar 95%."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/100-case-eval-925-coverage/featured.png"
image_style: "component_assembly"
image_model: "nanobanana"
image_alt: "The 100-Case Eval Problem. Precision mechanical inspection gauge with brackets failing to span the full width of a modular te"
image_caption: "The 100-Case Eval Problem: Why small test suites fail standard confidence intervals."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Your 100-case eval prints one number. If it prints a bar at all, it calls that bar 95%.

The paper behind the habit ran the math. At 100 questions, that bar delivered 92.5% coverage, not the 95% it claimed [1].

Two questions hide behind that single number. The National Institute of Standards and Technology (NIST) made the split clear in a February 2026 report [2].

The first asks how the system did on the exact cases that ran. The second asks how it would do on the wider pool of cases those tests stand for. That second set of bars is much wider [2].

A three-point drop on a 20-question suite means nothing at all. The same math on a thousand questions says something real.

<!-- tension -->

## The big picture:

Eval scores have moved out of research papers and into release gates.

These gates are small. A typical custom test holds 20 to 100 items, not thousands [5].

NIST draws a line most dashboards blur. Benchmark accuracy scores only the cases that ran. Generalized accuracy (the wider pool of similar cases) is a second measure [2].

Bars for the second come out wider, because the first treats the test suite as the whole world [2]. NIST also found pairs of models that look different on benchmark accuracy and act alike on the wider measure [2].

What strikes me here is that a standards body had to say this out loud. The plain average — right answers divided by case count, with a standard error under it — is called under-confident for benchmark accuracy beside a valid alternative [2].

Then comes the small-suite failure. Under a few hundred cases, the usual bar stops covering what it claims [1].

At 20 questions on a tool-use test, the bars ran below 0 and above 1, values a pass rate cannot take [1]. That result rests on 80,000 simulated test sets [1].

## By the numbers

- **92.5% — True coverage rate:** how often a stated 95% bar held the true value at 100 questions [1].
- **20 questions — Breaking point:** the size at which the usual method gave bars below 0 and above 1 [1].
- **1,000 questions — Signal threshold:** the math lands near 969 cases to spot a three-point gap 80% of the time with a 5% false-alarm rate [3].
- **22 models — NIST's example:** three common benchmarks where the plain average fell short of a valid method [2].

<!-- tactical-insight -->

## What I'd watch:

I have been reading these papers the way a gate owner reads a build log.

- **The gate's question:** a suite of 60 templates scores those 60 templates. The release call is about next month's traffic, which is the wider question, with more room to move [2].
- **The bar you print:** at 20 questions the usual bar left the possible range. The paper backs a Bayesian interval, which starts from a range of likely scores and narrows it case by case [1]. I would want that bar on the dashboard.
- **Where the power comes from:** comparing the same cases across two versions beats comparing two summaries. I watch for clustered errors when cases arrive in related batches [3].
- **The temperature trap:** turning sampling temperature down to settle a flaky suite does not remove the spread. The paper notes it can push that noise into the spread of the averages, or bias the guess [3].
- **Suite choice:** across 30 benchmarks and 375 open-weight models, suites differed a lot in how well they split better models from worse [4].

<!-- nuanced-takeaway -->

## The catch

The coverage figure is a simulation. The sample-size math rests on inputs the paper calls fictional but reasonable [3].

Neither one measures a named model. Both show the shape of the problem. The 20-to-100 range comes from a survey of what teams do, not a true census [5].

My read on the grouping point: a suite built from templates holds fewer separate cases than its raw count suggests. That is why the paper reaches for clustered errors when questions arrive in related groups [3].

A printed bar is a floor, not a ceiling.

None of this argues for dropping the gate. A small suite still catches a huge regression. What it cannot measure is a small move, and small moves are what a tuning cycle makes.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "$915M Illusion: Your AI Judge Moves" -> https://giniloh.com/buying-ai-quality-when-the-score-belongs-to-the-judge/ [same site (giniloh.com); same category] Link "$915M Illusion: Your AI Judge Moves" in the section where the article touches this topic. -->
<!-- internal-link hint: "70% of Agent Failures" -> https://giniloh.com/agent-failures-tests-stayed-green/ [same site (giniloh.com); same category] Link "70% of Agent Failures" in the section where the article touches this topic. -->
<!-- internal-link hint: "Agentic AI Adoption Soars, But Profits Stall in 2026" -> https://giniloh.com/agentic-ai-adoption-soars-but-profits-stall-in-2026/ [same site (giniloh.com); same category] Link "Agentic AI Adoption Soars, But Profits Stall in 2026" in the section where the article touches this topic. -->
## Related reading

- [$915M Illusion: Your AI Judge Moves](https://giniloh.com/buying-ai-quality-when-the-score-belongs-to-the-judge/)
- [70% of Agent Failures](https://giniloh.com/agent-failures-tests-stayed-green/)
- [Agentic AI Adoption Soars, But Profits Stall in 2026](https://giniloh.com/agentic-ai-adoption-soars-but-profits-stall-in-2026/)
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Small eval suites now gate releases, and the math for a suite of 20 to 100 cases has been measured. A stated 95% bar held the true value just 92.5% of the time at 100 questions, and at 20 questions it broke the possible range.
- **Why It Matters:** The release call turns on which question the score answers. Benchmark accuracy covers only the fixed suite that ran, while the wider figure carries wider bars. A small suite cannot settle a small move either way.
- **What I'd Watch:**
  - **The dashboard label:** whether a score reflects the fixed suite or estimates the wider pool. The two carry different doubt.
  - **The bar type:** at small sizes the plain bar covers less than it claims. A Bayesian interval is the pick the paper backs.
  - **The comparison design:** paired case-level differences, plus clustered errors where cases arrive in batches.
  - **The temperature habit:** cooling the sampling temperature does not remove the spread a flaky suite shows.
- **The Catch:** the headline numbers come from a simulation and an example table built on fictional inputs, and the typical suite size is a survey figure. Bars read as a floor, because grouped cases count for less than they look like.

## Sources
[1] Bowyer, Aitchison and Ivanova, "Position: Don't Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints" (ICML 2025 Spotlight Position Paper). https://arxiv.org/abs/2503.01747
[2] National Institute of Standards and Technology, NIST AI 800-3, "Expanding the AI Evaluation Toolbox with Statistical Models" (CAISI and ITL, February 2026). https://www.nist.gov/news-events/news/2026/02/new-report-expanding-ai-evaluation-toolbox-statistical-models
[3] Evan Miller, "Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations." https://arxiv.org/abs/2411.00640
[4] Heineman et al., "Signal and Noise: A Framework for Reducing Uncertainty in Language Model Evaluation." https://arxiv.org/abs/2508.13144
[5] Stats for LLM Evals, "Resources" — a curated practitioner survey. https://statsforevals.com/resources.html

## Gate report
lead: PASS — the 92.5% coverage figure lands in the first two sentences, with no preamble and no definition opener.
tension: PASS — frames the shift into release gates, carries a first-person observer cue, and keeps the source's own limit on the plain average.
tactical-insight: PASS — observer voice throughout, reported rather than prescribed, with the five watched items bulleted.
nuanced-takeaway: PASS — states the honest limits (simulation, fictional inputs, survey range) and labels the writer's own read.
tldr: PASS — four-part Smart Brevity summary under its own H2.
corrections: PASS — post-rewrite audit: restored the drafted STRONG headline (the rewrite's 8-word core scored 81); re-voiced "It may be tempting to reduce the sampling temperature" into plain words; every figure checked against the verified brief (92.5%, 100 questions, 20 questions, 0 and 1, 80,000 test sets, 969, 1,000, 80%, 5%, 22 models, 20-100 items, 30 benchmarks, 375 models); no new number introduced; NIST expanded at first use.
