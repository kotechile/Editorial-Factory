# Review report — 2026-11-24_one-build-costs-81-3-is-compute_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-24_one-build-costs-81-3-is-compute_draft.md` · attempt kept: 1 of 1
- figures in the ledger: 23 · citations: 5 · quotes: 1 · sources: 5
- reader-side critic: 0 holding defect(s), 2 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: A build queue's real bill is paid in payroll, not compute, so hardware that shaves build minutes should be priced against $75 an hour of engineer, not against the cloud invoice.

SHAPE: lead — the $81 build with $3 of machine in it, the whole argument in four sentences ; At a glance — one plain paragraph saying what the piece prices and for whom ; tension (Where the money goes) — the cost split, then the re-entry tax, then the monthly payroll arithmetic on replaceable inputs ; By the numbers — three one-metric bullets, figures the prose carries ; tactical (What teams that fixed it did) — Elastic's measured 3-hour → 55-minute result and the payback arithmetic for a local box ; The catch — the re-entry figure is 2004–2005 office research, so measure your own gap before buying.

WHAT IS NOT YET EARNED: nothing new is needed — every claim has its source. Fixes: the tension opening "What I keep coming back to is" is a borrowed cue; rewrite. The tactical section reads slightly like a playbook ("Where I'd look"); keep it reported, not advisory. The chronology section must state the research timeline once (2004–2005 fieldwork, 2006 interview, 2022 survey, 2026 experiment) and stop re-dating. The At a glance box must be a plain description under 50 words, not a re-list of the tactical section. "GPU total-cost-of-ownership calculator" link has no grounding in the brief — drop it.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 747 | 721 |
| sentence length mean | 18.5 | 18.9 |
| sentence length spread (sd) | 7.3 | 7.8 |
| rhythm health (0-1) | 0.919 | 0.936 |
| short sentences (<=8 words) | 5.1% | 5.4% |
| filler per 1,000 words | 2.68 | 2.77 |
| hedge per 1,000 words | 4.02 | 4.16 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 51.1 (PASS) |
| sections restating the through-line | 2 | 2 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- <!-- nuanced-takeaway --> carries no first-person sentence — it currently opens "The strongest figure here is the least verifiable on your team. The 23-minute re-entry result — the measured recovery time from the Irvine research ab…". The body is one person commenting, so this section needs one observation, labelled opinion or attention cue in the writer's own words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [7.3, 7.8], "rhythm_health": [0.919, 0.936], "filler": [2.68, 2.77], "words": 721, "flesch": 51.1, "score": [false, -1, -0.04], "critic_fails": 0, "critic_advisories": 2}
```
