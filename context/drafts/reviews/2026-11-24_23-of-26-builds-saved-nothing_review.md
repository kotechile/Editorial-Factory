# Review report — 2026-11-24_23-of-26-builds-saved-nothing_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-24_23-of-26-builds-saved-nothing_draft.md` · attempt kept: 1 of 1
- figures in the ledger: 18 · citations: 3 · quotes: 2 · sources: 3
- reader-side critic: 2 holding defect(s), 0 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: The switch to building software with AI is measurable and mainstream, but in the first measured cohort not one build has a verified saving — so the savings case, not the trend, is the unproven half.

SHAPE: lead — the 23-of-26 finding stated once, cold; At a glance — what the report is and who should care, one paragraph; chronology/tension — the report's window, the bill-sharing cohort, the verdicts, then the ledger that undercuts them, ending on the buy-side rule and the one small counter-case; By the numbers — three figures the prose does not restate; tactical — what the report's own limits section implies for how teams price a build, and what answer comes next (first verified replacement report); catch — absence of evidence is not evidence of absence, and the working rule.

NOT YET EARNED: the draft's "the switch is real" needs the 32%/1,719 figure kept attributed to McKinsey via the report (FLAG 3); $6.86M must stay "shared bills", never market spend (FLAG 1); the €300 case must stay one founder's backoffice, not a pattern; "this cohort has not met it" needs the $250k upkeep framing kept as the standard, not a claim the report tested. The tactical section's "price it like a renewal" is advice-shaped — keep it as a description of what close teams do.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 634 | 720 |
| sentence length mean | 15.2 | 16.8 |
| sentence length spread (sd) | 9.0 | 10.2 |
| rhythm health (0-1) | 0.799 | 0.644 |
| short sentences (<=8 words) | 37.5% | 29.4% |
| filler per 1,000 words | 1.58 | 0.0 |
| hedge per 1,000 words | 0.0 | 1.39 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 55.0 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Flow regressions against the draft

- rhythm health fell 0.799 -> 0.644 (mean 15.2 -> 16.8 words, sd 9.0 -> 10.2) — vary sentence length and break any run-on past 40 words
- hedge density rose: 0.0 -> 1.39 per 1,000 words

## Advisories

- rhythm health fell 0.799 -> 0.644 (mean 15.2 -> 16.8 words, sd 9.0 -> 10.2) — vary sentence length and break any run-on past 40 words
- hedge density rose: 0.0 -> 1.39 per 1,000 words

## Attempt trail

```
{"attempt": 1, "ok": true, "hard": 0, "regressions": 2, "rhythm_sd": [9.0, 10.2], "rhythm_health": [0.799, 0.644], "filler": [1.58, 0.0], "words": 720, "flesch": 55.0, "score": [true, 0, -0.49], "critic_fails": 2, "critic_advisories": 0}
```
