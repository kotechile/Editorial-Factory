# Review report — 2026-11-11_8-hi-hbm-costs-more-per-gigabit_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-11_8-hi-hbm-costs-more-per-gigabit_draft.md` · attempt kept: 1 of 3
- figures in the ledger: 12 · citations: 4 · quotes: 0 · sources: 4
- reader-side critic: 0 holding defect(s), 0 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: Samsung has already sold its 2027 HBM at an agreed price, and the cheaper-looking 8-Hi stack costs more per gigabit, so the only defensible way to size a 2027 memory budget is to measure your own session mix rather than buy on fleet averages.
SHAPE: lead: states the settled price and the inversion; tldr: three-line box with the shift, the number, the risk; tension: dates the settlement, explains the 8-Hi premium, introduces the measured substitute; tactical-insight: what the workload split means for operators and what to ask before signing; nuanced-takeaway: the simulation's limits and the narrower reading that survives.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 816 | 807 |
| sentence length mean | 19.1 | 18.9 |
| sentence length spread (sd) | 7.1 | 6.7 |
| rhythm health (0-1) | 0.843 | 0.768 |
| short sentences (<=8 words) | 7.9% | 7.9% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 1.23 | 0.0 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 56.9 (PASS) |
| sections restating the through-line | 3 | 3 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- <!-- nuanced-takeaway --> carries no first-person sentence — it currently opens "The flash result is a simulation, and its authors say so: the outputs are projections, not measurements of a working system [3]. Their own sensitivity…". The body is one person commenting, so this section needs one observation, labelled opinion or attention cue in the writer's own words

## Flow regressions against the draft

- rhythm health fell 0.843 -> 0.768 (mean 19.1 -> 18.9 words, sd 7.1 -> 6.7) — vary sentence length and break any run-on past 40 words
- the through-line is restated in 3 sections (lead, tension, nuanced-takeaway) — develop it, do not repeat it
- boilerplate observer cue(s): the part i keep circling

## Advisories

- rhythm health fell 0.843 -> 0.768 (mean 19.1 -> 18.9 words, sd 7.1 -> 6.7) — vary sentence length and break any run-on past 40 words
- the through-line is restated in 3 sections (lead, tension, nuanced-takeaway) — develop it, do not repeat it
- boilerplate observer cue(s): the part i keep circling

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 3, "rhythm_sd": [7.1, 6.7], "rhythm_health": [0.843, 0.768], "filler": [0.0, 0.0], "words": 807, "flesch": 56.9, "score": [false, -1, -1.66], "critic_fails": 0, "critic_advisories": 0}
{"attempt": 2, "ok": false, "hard": 2, "regressions": 1, "rhythm_sd": [7.1, 6.7], "rhythm_health": [0.843, 0.826], "filler": [0.0, 0.0], "words": 822, "flesch": 56.5, "score": [false, -2, -0.4], "critic_fails": 1, "critic_advisories": 0}
{"attempt": 3, "ok": false, "hard": 2, "regressions": 1, "rhythm_sd": [7.1, 6.9], "rhythm_health": [0.843, 0.816], "filler": [0.0, 0.0], "words": 816, "flesch": 56.4, "score": [false, -2, -0.48], "critic_fails": 0, "critic_advisories": 0}
```
