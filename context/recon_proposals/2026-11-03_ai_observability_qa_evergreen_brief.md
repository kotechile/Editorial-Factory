# Evergreen Brief: ai_observability_qa — 2026-11-03
**Archetype:** evergreen
**Vertical:** ai_observability_qa
**Persona:** evals_infra_eng
**Decision the reader is facing:** How to spend a synthetic-case generation budget so the suite actually discriminates — how many variants to ask for per seed prompt, which axes to vary, and which number proves the suite got better — before a release gate is allowed to ride on its pass rate.
**Durability:** The mechanism is a property of how a generator answers a prompt, not of any model version: asking one prompt for many cases collapses onto the same phrasing and the same idea, while changing the audience and the format inside the instruction produces different content. Every figure is dated as of its own publication — the requirements-classification ablation as of the 26 June 2025 preprint (arXiv 2506.21138), the Cosmopedia build as of March 2024 (Hugging Face blog), the duplicate-sample table as of the 14 August 2025 revision of the DCScore evaluation (arXiv 2502.08512v3) — and none of them depends on a price, a leaderboard position or a model release that moves inside a year.
**De-dup:** `2026-10-13_100-case-eval-925-coverage` (published) is this vertical's nearest prior artifact: it settles how many cases a gate needs and which interval to print, and `2026-10-27_ai_observability_qa_evergreen_brief.md` settles whether a green suite proves correctness (mutant kill rate, answer leakage). This piece asks neither question — it asks what the cases are made of, and shows that a similarity-based curation pass which improves the diversity metrics can cut the suite's measured utility, so "more diverse" is not the same claim as "better gate". Cross-vertical check, run before writing: the strongest rejected candidate (tool-interface drift as a schema regression test) is already argued in `published/2026-10-19_your-tool-surface-is-a-release-surface.md` (agentic_ai) from the same arXiv paper, so it was dropped by hand rather than shipped as a duplicate.
**Thesis:** A synthetic suite's diversity is set by the axes written into its prompts, not by how many cases you request or how aggressively you dedupe afterwards: asking one prompt for 20 cases instead of one lifted classification F1 by 6–43.8 points, Cosmopedia needed audience-and-style instructions (four audiences × three styles = 12× the prompts) before rewording alone stopped producing a high duplicate rate, and a similarity-based curation pass that improved every diversity metric still cut F1 in 9 of 12 configurations — so report the effective case count and re-measure the suite's own discrimination, never the diversity score alone.

**Lead:** The vertical's own `primary_angles` entry "synthetic dataset stress testing", read against the persona's `wants` ("deterministic vs probabilistic gates", "judge calibration") and the founder's §3 position that probabilistic gating must be calibrated against adversarial edge-case suites. The material is a sample-per-prompt ablation on a requirements-classification corpus (arXiv 2506.21138), a production synthetic corpus whose prompt-curation section states exactly which axes it had to vary (Hugging Face Cosmopedia), and a diversity-evaluation table that keeps duplicates constant (arXiv 2502.08512).

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Shivam, Vaidhyanathan et al., "How Good Are Synthetic Requirements? Evaluating LLM-Generated Datasets for AI4RE" (arXiv 2506.21138) | https://arxiv.org/html/2506.21138v1 | 2026-11-03 | 43.8 percentage points — the multi-sample setting improved F1 by 6-43.8 percentage points across classification tasks | measured |
| 2 | Shivam, Vaidhyanathan et al., "How Good Are Synthetic Requirements?" (arXiv 2506.21138) | https://arxiv.org/html/2506.21138v1 | 2026-11-03 | 7.4 percentage points — similarity-based curation improved every diversity metric, yet the worst F1 drop was 7.4 percentage points | measured |
| 3 | Allal, Lozhkov, van Strien, "Cosmopedia: how to create large-scale synthetic data for pre-training" (Hugging Face blog, 20 March 2024) | https://huggingface.co/blog/cosmopedia | 2026-11-03 | 12 times the number of prompts — four audiences and three generation styles yield up to 12 times the prompts, and rewording the same prompt alone was insufficient to prevent a high duplicate rate | vendor claim |
| 4 | Allal, Lozhkov, van Strien, "Cosmopedia" (Hugging Face blog) | https://huggingface.co/blog/cosmopedia | 2026-11-03 | 23 million prompts — the corpus was ultimately built from 23 million prompts after the audience-and-style pass | vendor claim |
| 5 | Zhang et al., "Measuring Diversity in Synthetic Datasets" (DCScore, arXiv 2502.08512) | https://arxiv.org/html/2502.08512v3 | 2026-11-03 | 5937.00 — DCScore reads 5937.00 at zero duplicates and 5936.99 after 6,000 duplicate samples are added, so the score reports effective samples and does not move when rows are copied | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Where a synthetic suite's diversity actually comes from: variants per prompt, the axes inside the instruction, and why a dedupe pass can lower the score it improves | 9 | 9 | 8 | 8 | 8.6 | **winner** |
| Tool-interface drift as a schema regression test (renames vs distractor tools) | 9 | 9 | 8 | 8 | 8.6 | dropped — cross-vertical duplicate of `published/2026-10-19_your-tool-surface-is-a-release-surface.md`, same arXiv 2610.23342 drift table and the same 0.717→0.813 / 0.580→0.805 figures |
| Judge position bias: run both orders and treat a flip as unresolved | 8 | 9 | 8 | 9 | 8.4 | dropped — third judge artifact inside a month and the same class as the 2026-11-03 news brief (arXiv 2611.02633/2611.03377: the scoring rule decides the number) |
| Trace sampling and span-attribute cardinality | 7 | 8 | 5 | 7 | 6.8 | dropped — no fetchable primary states a cardinality ceiling or a sampling rate with a figure the gate could verify |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=5 fetched=5 sources=3 hosts=2 decision="sha1:60ae1d2990" dedup="matched a prior artifact: 2026-10-13_100-case-eval-925-cover" window_days=180 checked_at=2026-11-03T17:33:50+00:00 -->
<!-- evergreen-gate:end -->
