# Review report — 2026-11-13_12-structures-froze-50000-policies_final.md

- verdict: **HELD — do not publish**
- draft: `2026-11-13_12-structures-froze-50000-policies_draft.md` · attempt kept: 1 of 3
- figures in the ledger: 21 · citations: 4 · quotes: 0 · sources: 4
- reader-side critic: 1 holding defect(s), 0 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: A 226-acre arson fire that destroyed 12 structures triggered a year of insurance protection for 50,000 policyholders, counted from a debris-cleanup declaration rather than from the fire itself, and that protection lands in a residual market writing fewer new policies each month while its exposure keeps climbing.
SHAPE: lead: state the strange fact; At a glance: the three-line frame; tension: chronology of the clock and the map; By the numbers: three figures the prose does not restate; tactical-insight: the FAIR Plan market behind the freeze; nuanced-takeaway: the limits of the comparison and what a homeowner can actually use.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 827 | 793 |
| sentence length mean | 15.4 | 15.7 |
| sentence length spread (sd) | 6.4 | 6.6 |
| rhythm health (0-1) | 0.622 | 0.662 |
| short sentences (<=8 words) | 12.2% | 13.0% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 1.21 | 0.0 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 52.2 (PASS) |
| sections restating the through-line | 3 | 3 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- section marker <!-- nuanced-takeaway --> dropped

## Flow regressions against the draft

- the through-line is restated in 3 sections (lead, tension, tactical-insight) — develop it, do not repeat it

## Advisories

- the through-line is restated in 3 sections (lead, tension, tactical-insight) — develop it, do not repeat it

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 1, "rhythm_sd": [6.4, 6.6], "rhythm_health": [0.622, 0.662], "filler": [0.0, 0.0], "words": 793, "flesch": 52.2, "score": [false, -1, 0.05], "critic_fails": 1, "critic_advisories": 0}
{"attempt": 2, "ok": false, "hard": 2, "regressions": 1, "rhythm_sd": [6.4, 6.4], "rhythm_health": [0.622, 0.619], "filler": [0.0, 0.0], "words": 822, "flesch": 54.3, "score": [false, -2, -1.03], "critic_fails": 0, "critic_advisories": 0}
{"attempt": 3, "ok": false, "hard": 2, "regressions": 1, "rhythm_sd": [6.4, 7.4], "rhythm_health": [0.622, 0.87], "filler": [0.0, 0.0], "words": 819, "flesch": 54.0, "score": [false, -2, 0.98], "critic_fails": 0, "critic_advisories": 0}
```
