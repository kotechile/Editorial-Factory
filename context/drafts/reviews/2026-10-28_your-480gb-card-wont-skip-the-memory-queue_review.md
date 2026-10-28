# Review report — 2026-10-28_your-480gb-card-wont-skip-the-memory-queue_held.md

- verdict: **HELD — do not publish**
- draft: `2026-10-28_your-480gb-card-wont-skip-the-memory-queue_draft.md` · attempt kept: 3 of 3
- figures in the ledger: 21 · citations: 5 · quotes: 4 · sources: 5

## The reviewer's reading

THROUGH-LINE: Intel's capacity-first D270 trades bandwidth for memory capacity, but it does not let buyers escape the memory shortage because the alternative low-power memory it uses is part of the same constrained, high-value supply chain.
SHAPE: Lead: Introduces the D270 card's specs and contrasts it with SK hynix's massive margins on memory. ; The big picture: Explains the collision—Intel sells a bandwidth escape, but the buyer just enters a different queue in the same tight memory market. ; By the numbers: Bulleted hard specs comparing Intel, AMD, NVIDIA, and the memory market. ; What I'd watch: Explains the technical pivot (prefill vs decode) and monitors workload splits and power limits. ; The catch: Highlights the lack of pricing and availability, linking the card's viability directly to fluctuating memory costs. ; At a glance: Summary bullets of the shift, importance, watch-points, and caveats.
UNEARNED: The claim in the original draft's "At a glance" section about software coverage in vLLM and SGLang trailing the incumbent stack is not supported by any evidence in the body text or the verified brief, so it was cut from the rewrite.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 1086 | 1043 |
| sentence length mean | 21.5 | 18.3 |
| sentence length spread (sd) | 10.0 | 8.0 |
| rhythm health (0-1) | 0.753 | 0.982 |
| short sentences (<=8 words) | 12.9% | 5.7% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 0.0 | 0.0 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 51.9 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- <!-- nuanced-takeaway --> carries no first-person sentence — it currently opens "The card is not on sale. Intel is sampling the hardware with no price and no ship date, and the analyst house that tore it down expects volume early i…". The body is one person commenting, so this section needs one observation, labelled opinion or attention cue in the writer's own words

## Flow regressions against the draft

- rhythm flattened: sentence-length sd 10.0 -> 8.0 (kept 80% of the draft's variance)

## Advisories

- rhythm flattened: sentence-length sd 10.0 -> 8.0 (kept 80% of the draft's variance)

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 2, "regressions": 2, "rhythm_sd": [10.0, 6.3], "rhythm_health": [0.753, 0.741], "filler": [0.0, 0.0], "words": 832, "flesch": 45.2, "score": [false, -2, -0.9]}
{"attempt": 2, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [10.0, 8.9], "rhythm_health": [0.753, 0.689], "filler": [0.0, 0.0], "words": 1084, "flesch": 52.0, "score": [false, -1, -0.51]}
{"attempt": 3, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [10.0, 8.0], "rhythm_health": [0.753, 0.982], "filler": [0.0, 0.0], "words": 1043, "flesch": 51.9, "score": [false, -1, 1.83]}
```
