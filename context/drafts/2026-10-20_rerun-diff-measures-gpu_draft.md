---
title: "Your 9% Drop: Not the Model"
vertical: ai_observability_qa
persona: evals_infra_eng
one_big_thing: "A score belongs to the run, not to the model: at temperature 0 with a fixed seed the same request still returns different answers when batch size, processor count or number format changes, so a two-run delta is a difference between machine setups until one is held fixed."
date: 2026-10-20
slug: rerun-diff-measures-gpu
archetype: evergreen
evergreen: true
---

<!-- lead -->

A 235-billion-parameter model took the same prompt a thousand times at temperature 0. Nine hundred and ninety-two of those answers named the same town. Eight named a different one, and the split appeared at the 103rd token [1].

Across the thousand there were 80 distinct answers. The most common came back 78 times [1]. Nothing about the model changed between those runs. The batch it shared with other requests did.

That is the problem with your eval diff. When the suite scores 78 out of 100 on Monday and 82 on Tuesday, the change you shipped is only one of the variables in that gap.

<!-- tension -->

## The big picture:

Floating-point addition is not associative. Add the same list of numbers in a different order and the total changes. The engineers at Thinking Machines Lab showed the extreme case: one fixed array, summed in ten thousand random orders, gave 102 different results [1].

A graphics processor adds in an order that depends on how many rows it is working through. One kernel reducing 8 rows and another reducing 32 rows can group the sums in different ways. So a request alone in a quiet batch, and the same request in a busy batch, can part at some token [1].

The fix has a name. A kernel is batch-invariant when the order of the sums is fixed no matter the batch size [1]. With that switched on, all thousand answers came back identical [1].

Most stacks lack it. vLLM documents its seed as defaulting to 0, and offers two routes to repeatable output. One is fixed scheduling, which only works offline. The other is batch invariance, the only route in online serving [2].

What strikes me is how much slack that leaves under an ordinary release gate. A team reruns 200 cases after a prompt change, sees the pass rate fall from 81 to 77, and calls it a regression. The same harness, model, seed and temperature, on a different number of processors, can move that far on its own.

The measured numbers are not subtle. One study ran six models at fixed settings over eight tasks, five times each. Accuracy moved by up to 10 points, and no model stayed repeatable across all its tasks [3].

A second study swept a 7B reasoning model over 12 setups: two processor types, two counts, three batch sizes. Accuracy moved up to 9 points, and answer length moved by 9,000 tokens [4]. The authors say the awkward part plainly. Greedy decoding does not give the same output across hardware and system setups, even with a fixed seed [4].

It reaches published work too. One team reran the text and tabular workloads of three query benchmarks through their own harnesses, logging 1.2 million model calls. At temperature 0, between 0.07% and 10.2% of rows changed their output across five runs, and one task moved 24.0% [5].

In the published SemBench results, 21% of text results changed quality between runs. Of 28 tests of a second benchmark's advice, 16 were not settled by the runs it makes [5].

## By the numbers

- **992 of 1000 — Same answer, eight strays:** one fixed prompt at temperature 0 gave 80 distinct answers, the most common seen 78 times, splitting 992 to 8 at token 103 [1].
- **9% — Batch-size accuracy swing:** one 7B model under greedy decoding with 16-bit numbers, across 12 machine setups [4].
- **10% — Five-run spread:** six models at fixed settings, over eight tasks, five runs each [3].
- **10.2% — Rows that moved:** share of benchmark rows whose output changed over five runs at temperature 0, up to 24.0% on one task [5].

<!-- tactical-insight -->

## What I'd watch:

I have been reading these papers the way an eval owner reads a build log, hunting the variable nobody wrote down.

- **The setup printed on the report:** a score without its processor type, processor count, batch size, number format and serving version is a number with no units. The 9-point swing came from setup alone [4].
- **The control run:** repeat the suite with nothing changed and record the spread. That spread is the floor a real delta must clear. Without it, a four-point drop looks like a normal Tuesday.
- **The price of the fix:** batch-invariant serving cost about 20% against the standard matrix library in the lab's own test. A run of 1000 answers went from 26 seconds to 55, then 42 with a better attention kernel [1]. For a single greedy run, the second study points to 32-bit numbers [4].
- **Where it compounds:** four chained classifiers, each 95% steady, land at 81.4% end to end before their own errors on new inputs count [3].
- **Disagreement inside one run:** identical requests within a single run disagree as often as requests compared across runs [5]. That makes the within-run spread the cheapest honesty check there is.

<!-- nuanced-takeaway -->

## The catch

My read: the strongest parts of this evidence were measured on something narrower than a release gate.

The 1.2-million-call study is about query engines over text and tables, not about your eval suite [5]. It shows the failure class is real in a production harness. It does not measure your gate.

The 992-to-8 split is one prompt, one model, one serving build, dated 10 September 2025 [1]. It is not a reliability rate, and 992 out of 1000 is not 99.2% of anything.

Closed vendors do not publish this much about their sampling, so a team on a hosted interface cannot switch batch invariance on. Repeat runs are the fallback, and even they help only so much. Voting cuts the variance without removing it [5].

The cost side is thinner than it looks. The 20% figure comes from an unoptimized in-house kernel, and the second study puts no number on what 32-bit floating point costs in speed or memory [1][4].

<!-- tldr -->

## At a glance

- **The Big Shift:** A model served at temperature 0 with a fixed seed still returns different answers when the batch size, processor count or number format changes. Two eval runs are comparisons between machine setups unless one is held fixed.
- **Why It Matters:** A gate that reads a four-point move as a regression can be measuring the server instead of your change, and the same swing shows up between published benchmark runs.
- **What I'd Watch:** I am watching what teams print beside a score, because the number is unreadable without it.
  - **Setup stamp:** the processor type and count, batch size, number format and serving version behind a run.
  - **Control spread:** the score range from repeated runs of an unchanged suite, which sets the size a real delta must beat.
  - **Batch-invariant serving:** a kernel mode where the order of the sums is fixed, at about 20% less throughput in one lab's test.
- **The Catch:** Repeat runs shrink the noise without removing it, hosted vendors hide their sampling, and the biggest effect measured here comes from a research kernel rather than a production one.

## Sources
[1] Horace He, "Defeating Nondeterminism in LLM Inference", Thinking Machines Lab, 10 September 2025 — the 102-order array, the 992-to-8 split at token 103, batch invariance defined, about 20% against cuBLAS, 26/55/42 seconds on 1000 sequences (https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)
[2] vLLM documentation, "Reproducibility" — seed defaulting to 0, fixed scheduling offline, batch invariance as the only route in online serving (https://docs.vllm.ai/en/latest/usage/reproducibility.html)
[3] Ouyang, Wang, Chu, Chen, Jin, Wang & Liu, "Non-Determinism of 'Deterministic' LLM Settings" (arXiv:2408.04667v2, August 2024) — six models, eight tasks, five identical runs, accuracy variations up to 10%, and the 0.95^4 = 81.4% compounding example (https://arxiv.org/html/2408.04667v2)
[4] Yang et al., "Give Me FP32 or Give Me Death? Challenges and Solutions for Reproducible Reasoning" (arXiv:2506.09501v1, June 2025) — up to 9% accuracy and 9,000 tokens of length variation under bfloat16 greedy decoding across 12 runtime setups, and the recommendation to use 32-bit numbers for a single greedy run (https://arxiv.org/html/2506.09501v1)
[5] Hassanzadeh & Subramanian, "Same Query, Different Answer: Run-to-Run Variance in Semantic Query Processing" (arXiv:2610.13823v1, 9 October 2026) — 1.2 million logged calls, 0.07% to 10.2% of rows changing over five runs, 21% of SemBench text results changing quality, 16 of 28 tests unsettled (https://arxiv.org/html/2610.13823v1)

<!-- internal-links -->
