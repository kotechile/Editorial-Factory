# Review report — 2026-10-28_your-60-drop-isnt-the-model_held.md

- verdict: **HELD — do not publish**
- draft: `2026-10-28_your-60-drop-isnt-the-model_draft.md` · attempt kept: 2 of 3
- figures in the ledger: 30 · citations: 7 · quotes: 0 · sources: 7

## The reviewer's reading

THROUGH-LINE: The success of an enterprise agent fabric depends on the interface shape and the stack's error handling, two architectural choices made before any model is selected, yet buyers mistakenly treat the model as the primary dial.
SHAPE: Lead: Introduces the central contradiction that task score collapses come from the tool protocol and stack, not model size. ; The big picture: Synthesizes two papers to show how representation and error handling dictate outcomes, contrasting this with vendor control planes that ignore these factors. ; By the numbers: Lists the critical metrics proving the thesis. ; What I'd watch: Shifts to actionable metrics and tactical tests for buyers to evaluate fabrics properly. ; The catch: Contextualizes the limits of the research (stress tests, mid-sized models, preprints) while maintaining the argument's validity. ; At a glance: Summarizes the argument and tactical takeaways.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 1353 | 1292 |
| sentence length mean | 21.4 | 18.8 |
| sentence length spread (sd) | 11.4 | 6.0 |
| rhythm health (0-1) | 0.76 | 0.629 |
| short sentences (<=8 words) | 15.4% | 2.4% |
| filler per 1,000 words | 1.48 | 0.0 |
| hedge per 1,000 words | 0.74 | 0.77 |
| abstraction per 1,000 words | 0.74 | 0.77 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 54.3 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- <!-- nuanced-takeaway --> carries no first-person sentence — it currently opens "The 60% is a stress result, not a field rate. The faults came from a mix heavy in permanent breakage, testing 25 single-server tasks and one model fam…". The body is one person commenting, so this section needs one observation, labelled opinion or attention cue in the writer's own words

## Flow regressions against the draft

- rhythm flattened: sentence-length sd 11.4 -> 6.0 (kept 53% of the draft's variance)
- rhythm health fell 0.76 -> 0.629 (mean 21.4 -> 18.8 words, sd 11.4 -> 6.0) — vary sentence length and break any run-on past 40 words

## Advisories

- rhythm flattened: sentence-length sd 11.4 -> 6.0 (kept 53% of the draft's variance)
- rhythm health fell 0.76 -> 0.629 (mean 21.4 -> 18.8 words, sd 11.4 -> 6.0) — vary sentence length and break any run-on past 40 words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 6, "regressions": 0, "rhythm_sd": [11.4, 11.4], "rhythm_health": [0.76, 0.773], "filler": [1.48, 0.0], "words": 1343, "flesch": 53.8, "score": [false, -6, 1.58]}
{"attempt": 2, "ok": false, "hard": 1, "regressions": 2, "rhythm_sd": [11.4, 6.0], "rhythm_health": [0.76, 0.629], "filler": [1.48, 0.0], "words": 1292, "flesch": 54.3, "score": [false, -1, 0.41]}
{"attempt": 3, "ok": false, "hard": 2, "regressions": 1, "rhythm_sd": [11.4, 9.2], "rhythm_health": [0.76, 0.753], "filler": [1.48, 0.0], "words": 1359, "flesch": 55.3, "score": [false, -2, 1.42]}
```
