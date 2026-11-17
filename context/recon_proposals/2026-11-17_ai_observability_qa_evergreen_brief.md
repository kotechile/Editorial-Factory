# Evergreen Brief: ai_observability_qa — 2026-11-17
**Archetype:** evergreen
**Vertical:** ai_observability_qa
**Persona:** evals_infra_eng
**Decision the reader is facing:** Whether a judge model may block a release on its agreement with humans, and which number the gate prints on that verdict — raw percent match, chance-corrected kappa with its interval, or a repeat-run stability score — a call that bites the first time a judge is asked to fail a deploy this quarter.
**Durability:** Chance agreement is arithmetic, not a trend: kappa subtracts the agreement two raters would reach by guessing from the label distribution, so the gap between raw match and kappa opens wherever one label dominates, whatever the judge model is. The figures are as of the June 2026 audit of 21 judges (reported 2026-06-17), the 2026-03-10 journal comparison on radiology reports, and the 2023 MT-Bench baseline as printed in the NeurIPS proceedings; the rule "print both numbers, set the bar against the human-human ceiling" stays true while the metric exists.
**De-dup:** `2026-11-03_your-grader-adds-22-points` is this vertical's nearest prior artifact (published 2026-11-03): it attacks the machinery around the judge — the renderer that turns a run into the text a judge reads and the parser that turns a reply into a verdict — not the agreement statistic itself. `2026-10-06_buying-ai-quality-when-the-score-belongs-to-the-judge` is the second (published 2026-10-06) and quotes a paper saying position bias, logic chains and human agreement "barely show how well the judge actually ranks replies", i.e. discrimination between two good answers; this brief is about the calibration number against human labels being inflated by chance and by repeatability, and about a domain where the flattered number happens to be true. Cross-vertical check run before writing: `grep -ril "position bias\|test-retest\|chance-corrected\|inter-rater\|agreement with humans" published/` returns `2026-10-06_buying-ai-quality-when-the-score-belongs-to-the-judge` and `2026-10-07_agent-tool-count-ceiling` (a tool-count ceiling piece that uses a chance-corrected model-selection method for a different question); no artifact argues kappa deflation, so this is not a retread of anything in the corpus.
**Thesis:** An agreement number is only as good as the chance it forgives: across 21 judges and roughly 541,000 judgments raw exact-match agreement overstated chance-corrected kappa by 33.8 to 41.3 points on MT-Bench, two production judges held test–retest above 0.95 while carrying position bias above 0.10, and the one place the judge genuinely matched people it reached kappa 0.82 against human-human 0.79 — so print kappa beside the raw number, set the bar against the human-human ceiling instead of 1.0, and never let repeat-run stability stand in for validity.

**Lead:** Founder-voice §3 names "LLM-as-a-judge calibrated against human consensus" as this vertical's probabilistic gate, and the persona's `wants` list "judge calibration" directly; customer-truth Anecdote 2 supplies the field friction — a judge whose pass rate drifted from 74% to 96% and whose true rate was 68%. The material that settles the decision is the 2026 audit of judge agreement statistics (arXiv:2606.19544), the peer-reviewed NeurIPS record of the MT-Bench agreement claim, and a 2026 journal study where a domain judge hit kappa parity with humans.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Norman, Rivera & Hughes — "Reliability without Validity" (arXiv:2606.19544v1, submitted 2026-06-17) | https://arxiv.org/html/2606.19544v1 | 2026-11-17 | 33.8–41.3 pp — exact-match agreement overstates Cohen's kappa on MT-Bench by 33.8 to 41.3 percentage points across 21 judges from nine providers, cohort mean 38.6 pp, over roughly 541,000 judgments in 118 runs | measured |
| 2 | Norman, Rivera & Hughes — "Reliability without Validity" (arXiv:2606.19544v1) | https://arxiv.org/html/2606.19544v1 | 2026-11-17 | 0.95 — test–retest reliability above 0.95 coexists with position bias above 0.10 in two production-deployed judges; judge rankings shift by up to 14 positions across benchmarks | measured |
| 3 | ESMO Real World Data and Digital Oncology — "Prompting large language models and evaluating inter- and intra-rater agreement for cancer progression assessment from radiology reports" (2026 Mar 10;11:100689) | https://pmc.ncbi.nlm.nih.gov/articles/PMC12993880 | 2026-11-17 | 0.82 — mean Cohen's kappa of 0.82 (95% CI 0.74–0.89) for human-to-LLM against 0.79 (95% CI 0.71–0.86) for human-to-human, with 72% of manual review removed | measured |
| 4 | Zheng et al. — "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena", NeurIPS 2023 Datasets & Benchmarks | https://papers.nips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html | 2026-11-17 | 80% — GPT-4 as judge reached over 80% agreement with human preference, described as the same level of agreement between humans | measured |
| 5 | Zheng et al. — "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (arXiv:2306.05685v4, full text) | https://arxiv.org/html/2306.05685v4 | 2026-11-17 | 85% — GPT-4 vs expert agreement with ties excluded reaches 85%, higher than the agreement among humans (81%) | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The judge's agreement number is inflated by chance — print kappa beside raw match and set the bar at the human-human ceiling | 9 | 9 | 9 | 8 | 8.8 | **winner** |
| Redundant retry-cycle detection from trace flamegraphs | 8 | 8 | 7 | 8 | 7.8 | dropped — the mechanism is already published as `2026-10-15_agent-loop-bound-not-a-budget` (agentic_ai) |
| How many human labels a judge calibration needs before it may gate | 8 | 9 | 4 | 7 | 7.1 | dropped — every sample-size recommendation traced to secondary blogs, no primary page printed the figure |
| Deterministic-vs-probabilistic tier split: what share of failures a schema gate catches | 7 | 9 | 5 | 6 | 6.8 | dropped — no measured split ratio found on a fetchable primary source |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=5 fetched=5 sources=4 hosts=3 decision="sha1:eb436f740e" dedup="matched a prior artifact: 2026-11-03_your-grader-adds-22-poi" window_days=180 checked_at=2026-11-17T17:33:30+00:00 -->
<!-- evergreen-gate:end -->
