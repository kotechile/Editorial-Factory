# Review report — 2026-11-10_your-gpu-starves-at-5-9-gibs_held.md

- verdict: **HELD — do not publish**
- draft: `2026-11-10_your-gpu-starves-at-5-9-gibs_draft.md` · attempt kept: 1 of 3
- figures in the ledger: 11 · citations: 7 · quotes: 0 · sources: 7
- reader-side critic: 0 holding defect(s), 1 prose advisory(ies) (scripts/readability_critic.py)

## The reviewer's reading

THROUGH-LINE: A training workstation is fed by bytes per sample times samples per second — one accelerator wants about 5.9 GiB/s of steady read at benchmark pressure — but because the measured stall survives even a fully cached dataset, the next purchase after the card is CPU cores and a decoded cache, not a faster drive.
SHAPE: Lead sets the core tension between drive speed and the persistent stall ; At a glance gives the three-line summary ; The big picture explains the feed-rate arithmetic and why storage is per-card ; By the numbers isolates the three figures that prove the argument ; What I'd watch reports what the people closest to the story do and what busy time actually tells you ; The catch caps the number's meaning and points at the real bottleneck.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 794 | 778 |
| sentence length mean | 18.2 | 17.8 |
| sentence length spread (sd) | 8.1 | 8.2 |
| rhythm health (0-1) | 0.861 | 0.857 |
| short sentences (<=8 words) | 10.3% | 12.8% |
| filler per 1,000 words | 0.0 | 0.0 |
| hedge per 1,000 words | 0.0 | 0.0 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 2 | 2 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 55.3 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- <!-- nuanced-takeaway --> carries no first-person sentence — it currently opens "My reading, held loosely: the 5.9 GiB/s figure is a ceiling, not a budget. It comes from the hungriest workload in the suite, reading 140 MiB image fi…". The body is one person commenting, so this section needs one observation, labelled opinion or attention cue in the writer's own words

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [8.1, 8.2], "rhythm_health": [0.861, 0.857], "filler": [0.0, 0.0], "words": 778, "flesch": 55.3, "score": [false, -1, -0.83], "critic_fails": 0, "critic_advisories": 1}
{"attempt": 2, "ok": false, "hard": 3, "regressions": 0, "rhythm_sd": [8.1, 7.7], "rhythm_health": [0.861, 0.955], "filler": [0.0, 0.0], "words": 792, "flesch": 56.4, "score": [false, -3, -0.05], "critic_fails": 0, "critic_advisories": 1}
{"attempt": 3, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [8.1, 8.9], "rhythm_health": [0.861, 0.851], "filler": [0.0, 0.0], "words": 800, "flesch": 55.0, "score": [false, -1, -0.88], "critic_fails": 0, "critic_advisories": 1}
```
