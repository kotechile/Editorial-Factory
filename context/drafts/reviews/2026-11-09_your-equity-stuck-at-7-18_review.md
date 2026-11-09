# Review report — 2026-11-09_your-equity-stuck-at-7-18_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-09_your-equity-stuck-at-7-18_draft.md` · attempt kept: 1 of 3
- figures in the ledger: 28 · citations: 3 · quotes: 0 · sources: 3
- reader-side critic: 1 holding defect(s), 4 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: The article argues that the $13.2 trillion accessible-equity pile is really a rate-gap artifact — the $11.6 trillion counted as locked gets reclassified whenever the prevailing 30-year rate moves, so the reachable share shrinks without any homeowner doing anything, and the cheapest way to tap equity is a second lien on a small job.
SHAPE: At a glance gives the shift, the number, and the risk; A benchmark that moved after the report explains the reclassification mechanism and the 6.6 example; By the numbers holds three figures the prose does not use; Two lock bands, two loan choices applies the bands to refinance versus second-lien costs; The catch handles the two surveys and the estimate caveat.
NOT-YET-EARNED: The $1.6 trillion reachable remainder is the reporter's arithmetic on rounded published bands, so it must stay labeled approximate.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 880 | 775 |
| sentence length mean | 20.4 | 17.6 |
| sentence length spread (sd) | 9.2 | 7.9 |
| rhythm health (0-1) | 0.728 | 0.969 |
| short sentences (<=8 words) | 7.5% | 7.1% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 1.14 | 0.0 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 54.5 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- <!-- nuanced-takeaway --> carries no first-person sentence — it currently opens "The two anchors are not one series. First American's 6.49% is its own national average at quarter end [1]. Freddie Mac's 7.18% covers conventional pur…". The body is one person commenting, so this section needs one observation, labelled opinion or attention cue in the writer's own words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [9.2, 7.9], "rhythm_health": [0.728, 0.969], "filler": [0.0, 0.0], "words": 775, "flesch": 54.5, "score": [false, -1, 2.61], "critic_fails": 1, "critic_advisories": 4}
{"attempt": 2, "ok": false, "hard": 3, "regressions": 2, "rhythm_sd": [9.2, 4.8], "rhythm_health": [0.728, 0.314], "filler": [0.0, 0.0], "words": 708, "flesch": 54.7, "score": [false, -3, -2.63], "critic_fails": 2, "critic_advisories": 2}
{"attempt": 3, "ok": false, "hard": 4, "regressions": 1, "rhythm_sd": [9.2, 7.7], "rhythm_health": [0.728, 0.97], "filler": [0.0, 0.0], "words": 746, "flesch": 50.0, "score": [false, -4, 1.82], "critic_fails": 0, "critic_advisories": 3}
```
