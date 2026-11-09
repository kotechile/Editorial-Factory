# Review report — 2026-11-09_your-condensers-repair-bill-2090-vs-700_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-09_your-condensers-repair-bill-2090-vs-700_draft.md` · attempt kept: 2 of 3
- figures in the ledger: 8 · citations: 7 · quotes: 0 · sources: 7
- reader-side critic: 0 holding defect(s), 3 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: The refrigerant inside the condenser, not the efficiency rating on the quote, decides the repair bill because R-410A sits at a 2,090 warming potential above the 700 ceiling for new residential systems and the statutory phasedown makes that old gas scarcer on a fixed schedule.
SHAPE: lead: names the three costs and puts the refrigerant number ahead of the rating; tldr: reduces the shift, the number, and the risk to three lines; tension: states the rule, the supply cap, and the uneven effect on replace-versus-repair; numbers: isolates the old gas, the replacement gas, and the later allowance; tactical: reads the bid through the data plate, build date, and handling class; catch: separates what the rule bans from what it still permits.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 907 | 855 |
| sentence length mean | 18.2 | 19.8 |
| sentence length spread (sd) | 8.2 | 6.9 |
| rhythm health (0-1) | 0.984 | 0.746 |
| short sentences (<=8 words) | 8.7% | 0.0% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 4.41 | 5.85 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 56.5 (FAIL) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- accessibility gate: undefined acronym(s): A2L

## Flow regressions against the draft

- rhythm flattened: sentence-length sd 8.2 -> 6.9 (kept 84% of the draft's variance)
- rhythm health fell 0.984 -> 0.746 (mean 18.2 -> 19.8 words, sd 8.2 -> 6.9) — vary sentence length and break any run-on past 40 words
- hedge density rose: 4.41 -> 5.85 per 1,000 words

## Advisories

- rhythm flattened: sentence-length sd 8.2 -> 6.9 (kept 84% of the draft's variance)
- rhythm health fell 0.984 -> 0.746 (mean 18.2 -> 19.8 words, sd 8.2 -> 6.9) — vary sentence length and break any run-on past 40 words
- hedge density rose: 4.41 -> 5.85 per 1,000 words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 2, "regressions": 1, "rhythm_sd": [8.2, 7.4], "rhythm_health": [0.984, 0.837], "filler": [0.0, 0.0], "words": 778, "flesch": 53.1, "score": [false, -2, -0.85], "critic_fails": 0, "critic_advisories": 5}
{"attempt": 2, "ok": false, "hard": 1, "regressions": 3, "rhythm_sd": [8.2, 6.9], "rhythm_health": [0.984, 0.746], "filler": [0.0, 0.0], "words": 855, "flesch": 56.5, "score": [false, -1, -2.77], "critic_fails": 0, "critic_advisories": 3}
{"attempt": 3, "error": "frontier output truncated (finish_reason=length); raise max_tokens"}
```
