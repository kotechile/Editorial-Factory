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
meta_title: "Your Green Score's Hidden 7.0-Point Drop"
meta_title_source: "derived_from_title"
meta_description: "Six frontier models lost 7.0 points when they were re-tested on re-worded MMLU (the multiple-choice general-knowledge benchmark) questions, because the…"
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/your-green-score-rides-138-contaminated-data/featured.jpg"
image_style: "document_flatlay"
image_model: "flux"
image_alt: "MMLU Contamination Hides A 7-Point Drop. Two multiple-choice answer sheets side by side: one neatly filled and stamped green, its re-worded"
image_caption: "MMLU Contamination Hides A 7-Point Drop: Six frontier models lost 7 points on re-worded MMLU — your green score may be recall."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Six frontier models lost 7.0 points when they were re-tested on re-worded MMLU (the multiple-choice general-knowledge benchmark) questions, because the originals had already leaked into their training data. That gap is a hidden 7.0-point drop: the part of your green score's clean look that was never reasoning. The release call belongs to a fresh mirror run, not to the published number.

<!-- tldr -->

## At a glance

This piece is for eval engineers who gate releases on public benchmark scores. A 2026 scan found 13.8% of MMLU questions contaminated, and re-worded tests show frontier models dropping points they should not have had. The fix is gating on a mirror the model has never seen.

<!-- tension -->

## How the leak got measured

The evidence arrived in three steps. Apple's GSM-Symbolic study paraphrased GSM8K (a public set of grade-school math (GSM) problems) and found the originals outscoring their own re-worded versions on 21 of 25 models [6]. A second team then built GSM1k, a private mirror of that math set matched for difficulty, and leading models dropped up to 8% on that mirror [3]. By 2026 the same test reached general knowledge: a scan of 513 MMLU questions found 13.8% contaminated, and 66.7% in Philosophy, the worst subject [1].

The mechanism is simple. Public test suites get scraped wholesale into pre-training corpora, so any item published before a model's training cutoff may be in that scrape, sometimes with its answer. What I keep circling is how often teams treat this as another lab's problem. The failure lands in your own gate when a score that looks like reasoning is really recall. The teams who pay are the ones releasing on a delta a mirror run would erase.

## By the numbers

- **13.8% of MMLU:** the leaked share a word-overlap scan measured across all 57 subjects [1].
- **21 models:** scored the original GSM8K questions above their own paraphrased spread [6].
- **335 detector evaluations:** how many the leading contamination tests were audited on; barely three in five ended correct [5].

<!-- tactical-insight -->

## Where this bites

The teams closest to the problem score with data the model cannot have memorized. The GSM1k group built a fresh mirror matched for difficulty, human solve rates and answer size [3]. On that mirror, overfit models lost points their benchmark number never admitted; the paper's abstract reports drops up to 13% on first release, revised to 8% in the peer-reviewed version [4]. The re-wording test, where each question gets a fresh surface form, is the cheap version. Six frontier models answering re-worded MMLU questions fell 7.0 points on average, and 19.8 points in Law, the most leaked subject [2]. A private held-out slice of cases, collected after the training cutoff and never published, is the cleaner floor, and sizing it is [the same math a 100-case eval needs for confidence intervals](/100-case-eval-925-coverage/).

**What I'd watch:** where a mirror gets its difficulty guarantee. A mirror drop only means something when the two sets match on human solve rates and answer size. Without that match, a lower score is a mix-up, not a leak.

<!-- nuanced-takeaway -->

## The catch

The tools that claim to vouch for a benchmark cannot carry the verdict yet. Across 335 detection runs, only 201 were solved, and the failures are built in [5]. Membership-inference tests — statistical checks that guess whether one example sat in the training data — raise false alarms when the suspect set shifts its mix. They also run too weak when a benchmark is tiny next to a pre-training corpus. A detector can flag a benchmark as suspect; my read is it cannot clear one yet.

The cut runs the other way too. A mirror proves contamination when the score drops, but a flat score on a mirror is not innocence — it may mean the mirror was easier. So the decision left to you is which number to gate on: the lasting signal is a delta between two runs on matched difficulty, not either score alone.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "70% of Agent Failures" -> /agent-failures-tests-stayed-green/ [same site (aichieve.net); same category; topical overlap: green] Link "70% of Agent Failures" in the section where the article touches green. -->
<!-- internal-link hint: "Agentic AI Adoption Soars, But Profits Stall in 2026" -> /agentic-ai-adoption-soars-but-profits-stall-in-2026/ [same site (aichieve.net); same category; topical overlap: already] Link "Agentic AI Adoption Soars, But Profits Stall in 2026" in the section where the article touches already. -->
<!-- internal-link hint: "Half Your Tokens: 5% of Your Bill" -> /half-your-tokens-5-of-bill/ [same site (aichieve.net); same category; topical overlap: models] Link "Half Your Tokens: 5% of Your Bill" in the section where the article touches models. -->
## Related reading

- [70% of Agent Failures](/agent-failures-tests-stayed-green/)
- [Agentic AI Adoption Soars, But Profits Stall in 2026](/agentic-ai-adoption-soars-but-profits-stall-in-2026/)
- [Half Your Tokens: 5% of Your Bill](/half-your-tokens-5-of-bill/)
<!-- internal-links:end -->

## Sources

- [1] "Are Large Language Models Truly Smarter Than Humans? Benchmark Contamination, Surface-Pattern Reliance, and Behavioral Memorization Across Six Frontier Models" (2026) — https://arxiv.org/html/2603.16197v1
- [2] Same study, Experiment 2 paraphrase and indirect-reference diagnostic (2026) — https://arxiv.org/html/2603.16197v1
- [3] Srivastava et al., "A Careful Examination of Large Language Model Performance on Grade School Arithmetic" (NeurIPS 2024 Datasets & Benchmarks) — https://arxiv.org/html/2405.00332v4
- [4] The same GSM1k paper's abstract record on Hugging Face Papers — https://huggingface.co/papers/2405.00332
- [5] "The Reliability Gap in Benchmark Auditing: Distribution Shift and Scale as Failure Modes of Contamination Detection" (2026) — https://arxiv.org/html/2606.03305
- [6] Mirzadeh et al., "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models" (Apple, 2024) — https://arxiv.org/html/2410.05229v1
