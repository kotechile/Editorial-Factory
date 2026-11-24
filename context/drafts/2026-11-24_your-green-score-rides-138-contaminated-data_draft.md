---
title: "Your Green Score's Hidden 7.0-Point Drop"
vertical: ai_observability_qa
kind: evergreen
archetype: evergreen
evergreen: true
persona: evals_infra_eng
one_big_thing: "A share of the eval data your green score rests on may already sit in the model's training data. Gate on a fresh mirror run, not on the benchmark number — and not on a contamination detector either."
date: 2026-11-24
slug: your-green-score-rides-138-contaminated-data
---

<!-- lead -->
When six frontier models met re-worded versions of MMLU (the multiple-choice general-knowledge benchmark), their scores fell 7.0 points — the hidden 7.0-point drop your green score keeps out of sight, because part of the test questions had already leaked into the models' training data. A score's clean look is really recall. The release call belongs to a re-run on a fresh mirror of the suite, not to the published number.

<!-- tldr -->
## At a glance
Eval engineers keep gating releases on scores that may be contaminated — test items that sat in the training data. A 2026 scan of MMLU measured the leak. The gate that survives it runs on a mirror the model has not seen.

<!-- tension -->
## Why the leak happens
The evidence came in three steps. First, Apple's GSM-Symbolic study paraphrased GSM8K (a public set of grade-school math problems) — GSM8K for short, and found the originals scoring above their own paraphrased scores, on 21 of 25 models [6]. Next, a team built GSM1k, a private mirror of that grade-school math (GSM) set, matched for difficulty, and leading models dropped up to 8% on the mirror [3]. By 2026 the same test had reached general knowledge: a scan of 513 MMLU questions found 13.8% contaminated, and 66.7% in Philosophy, the worst subject [1].

The mechanism is simple. Public eval suites get scraped wholesale into pre-training corpora. Any item published before a model's training cutoff may be in that scrape, sometimes with its answer. What I find hard to square is how often teams treat this as another model's problem. The failure lands in your own gate when a score that looks like reasoning is really recall. The teams who pay are the ones releasing on a delta that a mirror run would erase.

## By the numbers
- **13.8% of MMLU:** the contaminated share a lexical scan measured across all 57 subjects [1].
- **21 models:** scored the original GSM8K questions above their own paraphrased spread [6].
- **335 detector evaluations:** how many the leading contamination tests were audited on; barely three in five ended correct [5].

<!-- tactical-insight -->
## Where this bites
Teams close to the problem score with data the model cannot have memorized. The GSM1k group built a fresh mirror matched for difficulty, human solve rates and answer size [3]. On that mirror, overfit models lost points their benchmark number never admitted; the paper's abstract reports drops up to 13% on first release, revised to 8% in the peer-reviewed version [4]. The paraphrase test — re-wording each question so its surface form is new — is the cheap version. Six frontier models answering re-worded MMLU questions fell 7.0 points on average, and 19.8 points in Law, the most contaminated subject [2]. A private held-out slice of cases, collected after the training cutoff and never published, is the cleaner floor. The size that slice needs is the [same math a 100-case eval needs for confidence intervals](/100-case-eval-925-coverage/).

What I would watch next is where a mirror gets its difficulty guarantee. A mirror drop only means something when the two sets match on human solve rates and answer size. Without that match, a lower score is a confound, not contamination.

<!-- nuanced-takeaway -->
## The catch
The tools that claim to vouch for a benchmark are not ready to carry the verdict. Across 335 detection runs, only 201 were solved, and the failures are built in [5]. Membership-inference tests — statistical checks that guess whether one example sat in the training data — raise false alarms when the suspect set shifts its mix. They also run too weak when a benchmark is tiny next to a pre-training corpus. A detector can flag a benchmark as suspect; I don't think it can clear one yet. The catch cuts the other way too. A mirror proves contamination when the score drops, but a flat score on a mirror is not innocence — it may mean the mirror was easier. The lasting number is a delta between two runs on matched difficulty, not either score alone.

## Sources
- [1] "Are Large Language Models Truly Smarter Than Humans? Benchmark Contamination, Surface-Pattern Reliance, and Behavioral Memorization Across Six Frontier Models" (2026) — https://arxiv.org/html/2603.16197v1
- [2] Same study, Experiment 2 paraphrase and indirect-reference diagnostic (2026) — https://arxiv.org/html/2603.16197v1
- [3] Srivastava et al., "A Careful Examination of Large Language Model Performance on Grade School Arithmetic" (NeurIPS 2024 Datasets & Benchmarks) — https://arxiv.org/html/2405.00332v4
- [4] The same GSM1k paper's abstract record on Hugging Face Papers — https://huggingface.co/papers/2405.00332
- [5] "The Reliability Gap in Benchmark Auditing: Distribution Shift and Scale as Failure Modes of Contamination Detection" (2026) — https://arxiv.org/html/2606.03305
- [6] Mirzadeh et al., "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models" (Apple, 2024) — https://arxiv.org/html/2410.05229v1
