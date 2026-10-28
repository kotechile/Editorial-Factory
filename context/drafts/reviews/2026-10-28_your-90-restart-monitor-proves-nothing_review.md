# Review report — 2026-10-28_your-90-restart-monitor-proves-nothing_held.md

- verdict: **HELD — do not publish**
- draft: `2026-10-28_your-90-restart-monitor-proves-nothing_draft.md` · attempt kept: 2 of 3
- figures in the ledger: 18 · citations: 5 · quotes: 0 · sources: 5

## The reviewer's reading

THROUGH-LINE: A restart monitor's accuracy score tells you nothing about its value, because the true price of abandoning a run is the replacement attempt's probability of finishing on the remaining budget.
SHAPE: Lead: introduces the core gap between monitor accuracy and restart value ; The big picture: contextualizes the rapid arrival of recovery tooling and the failure of standard metrics to price it ; By the numbers: lists the exact metrics proving the disconnect ; What I'd watch: highlights the shift from detector metrics to decision value metrics in production ; The catch: limits the scope of the findings based on sample size and study design.
UNEARNED: The draft mentions a 42.29-point loss on a second model without explaining that this stems from transferring a cutoff scale between models, leaving the reader without the context for why the drop occurred.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 872 | 881 |
| sentence length mean | 17.2 | 17.2 |
| sentence length spread (sd) | 4.4 | 4.4 |
| rhythm health (0-1) | 0.301 | 0.291 |
| short sentences (<=8 words) | 3.4% | 3.4% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 3.44 | 2.27 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 57.3 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- <!-- nuanced-takeaway --> carries no first-person sentence — it currently opens "The alarm study covers 19 issues from one repository, one harness and five tries per task [1]. Its 103-choice review ran after the tests, not before t…". The body is one person commenting, so this section needs one observation, labelled opinion or attention cue in the writer's own words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 5, "regressions": 0, "rhythm_sd": [4.4, 4.9], "rhythm_health": [0.301, 0.403], "filler": [0.0, 0.0], "words": 872, "flesch": 48.1, "score": [false, -5, 2.19]}
{"attempt": 2, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [4.4, 4.4], "rhythm_health": [0.301, 0.291], "filler": [0.0, 0.0], "words": 881, "flesch": 57.3, "score": [false, -1, 0.62]}
{"attempt": 3, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [4.4, 4.3], "rhythm_health": [0.301, 0.266], "filler": [0.0, 0.0], "words": 863, "flesch": 50.6, "score": [false, -1, 0.39]}
```
