---
title: "Your 100-Case Eval: 92.5% Coverage, Not 95%"
vertical: ai_observability_qa
persona: evals_infra_eng
one_big_thing: "A release gate's score answers one of two different questions, and the small suite that runs in CI cannot carry the plain 95% interval usually printed beside it: at 100 questions a nominal 95% interval held the true value only 92.5% of the time, and the question a ship-or-hold call needs — accuracy over the wider pool of similar cases — carries wider bars than the benchmark number on the label."
date: 2026-10-13
slug: 100-case-eval-925-coverage
archetype: evergreen
evergreen: true
---

<!-- lead -->

Your 100-case eval prints one number. If it prints a bar at all, it calls that bar 95%. The paper behind the habit ran the check. At 100 questions the bar held the true value just 92.5% of the time [1].

Two questions hide behind that one number. NIST (the U.S. National Institute of Standards and Technology) made the split plain in a February 2026 report [2]. The first question asks how the system did on the cases that ran. The second asks how it would do on the wider pool those cases stand for. The second set of bars is wider [2].

A three-point "drop" on a 20-question suite can be nothing at all. The same math on a thousand questions says something.

<!-- tension -->

## The big picture:

Eval scores have moved out of research write-ups and into release gates. The gates are small. A typical custom developer eval holds 20 to 100 items, not thousands [5].

NIST's report draws a line most dashboards blur. Benchmark accuracy scores the cases that ran. Generalized accuracy (the wider pool of similar cases) is a separate measure [2]. Bars for the second come out wider, because the first treats the suite as the whole world [2].

The report also found pairs of models that look different on benchmark accuracy and alike on the wider measure [2].

What strikes me is that a standards body had to say this out loud. The plain average — right answers divided by case count, with a standard error under it — is called under-confident for benchmark accuracy beside a valid alternative: bars wider than the method needs [2].

Then comes the small-suite failure the position paper measured. Under a few hundred cases, the usual interval stops covering what it claims [1]. At 20 questions on a tool-use test, the bars ran below 0 and above 1, values a pass rate cannot take [1]. That result rests on 80,000 simulated eval sets, at sizes of 3, 10, 30 and 100 [1].

## By the numbers

- **92.5% — Coverage at 100 questions:** how often a stated 95% interval held the true value [1].
- **20 questions — Where the bars broke:** the size at which the same method gave intervals below 0 and above 1 [1].
- **1,000 questions — Size for a three-point effect:** the paper's math lands near 969 cases to spot a three-point gap 80% of the time, at a 5% false-alarm rate [3].
- **22 models — NIST's worked example:** three common benchmarks, where the plain average fell short of a valid method [2].

<!-- tactical-insight -->

## What I'd watch:

I have been reading these papers the way a gate owner reads a build log.

- **Which question the gate answers:** a suite of 60 templates scores those 60 templates. The release call is about next month's traffic, which is the wider question, and the one with more give in it [2].
- **What sits beside the score:** at 20 questions the usual interval left the possible range. The paper's replacement is a Bayesian interval, which starts from a range of likely scores and narrows it case by case [1]. I would want that bar on the dashboard, not in a notebook.
- **Where the power comes from:** comparing the same cases across two versions, not two summaries. Cluster the error when cases arrive in related batches [3].
- **The temperature trap:** turning sampling temperature down to settle a flaky suite does not remove that variance. The paper says it can shift it into the spread of the averages, or bias the estimate [3].
- **Suite choice:** across 30 benchmarks and 375 open-weight models, some 900,000 results, suites differed in how well they separate better models from worse, and in how much they drift [4].

<!-- nuanced-takeaway -->

## The catch

The coverage figure is a simulation. The sample-size math rests on parameters the paper calls fictional but reasonable [3]. Neither one measures a named model. Both show the shape of the problem.

The 20-to-100 range comes from a practitioner survey, not a census [5]. Read it as a habit, not a measured spread.

My read on the grouping point: a suite built from templates holds fewer separate cases than its count suggests. That is why the paper reaches for clustered errors when questions arrive in related groups [3]. A printed bar is a floor, then, not a ceiling.

None of this argues for dropping the gate. A small suite still catches a large regression. What it cannot speak to is the small move, and small moves are what a tuning cycle makes.

<!-- tldr -->

## At a glance

- **The Big Shift:** Small eval suites now gate releases, and the math for a suite of 20 to 100 cases has been measured. A stated 95% interval held the true value 92.5% of the time at 100 questions, and at 20 questions it left the possible range.
- **Why It Matters:** The gate call turns on which question the score answers. Benchmark accuracy covers the fixed suite that ran. The wider-pool figure carries wider bars. A small suite cannot settle a small move either way.
- **What I'd Watch:**
  - **The question on the label:** whether a dashboard score is the fixed suite or an estimate of the wider pool, since the two carry different uncertainty.
  - **The interval beside the score:** at small sizes the usual bar covers less than it says. A Bayesian interval is the recommended replacement.
  - **The comparison design:** paired case-level differences, plus clustered errors where cases arrive in batches.
  - **The temperature habit:** cooling the sampling temperature does not remove the variance a flaky suite shows.
- **The Catch:** the headline numbers come from a simulation and an illustrative table built on fictional parameters, and the typical suite size is a survey figure. Bars read as a floor, because grouped cases count for less than they look like.

## Sources
[1] Bowyer, Aitchison and Ivanova, "Position: Don't Use the CLT in LLM Evals With Fewer Than a Few Hundred Datapoints" (ICML 2025 Spotlight Position Paper). https://arxiv.org/abs/2503.01747
[2] National Institute of Standards and Technology, NIST AI 800-3, "Expanding the AI Evaluation Toolbox with Statistical Models" (CAISI and ITL, February 2026). https://www.nist.gov/news-events/news/2026/02/new-report-expanding-ai-evaluation-toolbox-statistical-models
[3] Evan Miller, "Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations." https://arxiv.org/abs/2411.00640
[4] Heineman et al., "Signal and Noise: A Framework for Reducing Uncertainty in Language Model Evaluation." https://arxiv.org/abs/2508.13144
[5] Stats for LLM Evals, "Resources" — a curated practitioner survey. https://statsforevals.com/resources.html
