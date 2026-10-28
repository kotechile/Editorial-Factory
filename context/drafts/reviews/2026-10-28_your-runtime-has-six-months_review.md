# Review report — 2026-10-28_your-runtime-has-six-months_held.md

- verdict: **HELD — do not publish**
- draft: `2026-10-28_your-runtime-has-six-months_draft.md` · attempt kept: 2 of 2
- figures in the ledger: 9 · citations: 4 · quotes: 4 · sources: 4

## The reviewer's reading

THROUGH-LINE: The shutdown of Deno and Anthropic's custom git replacement demonstrate that enterprise engineering leaders must evaluate vendor tools based on which layer holds the margin and whether their own team could survive building a replacement when the vendor exits.
SHAPE: Lead: Introduces the twin events of October 2026 to frame the build-versus-buy dilemma. ; The big picture: Explains why vendors abandon tools (margin sits elsewhere) and why buyers are forced to build (workload outgrows the tool). ; By the numbers: Quantifies the scale of both the exit timeline and the workload that forced a custom build. ; What I'd watch: Outlines the structural factors (margin location, open-source escapes, build capacity) that determine survival during a vendor transition. ; The catch: Argues that Anthropic's build is a warning about the extreme cost of replacing foundational layers, not a playbook for standard teams. ; At a glance: Summarizes the shift, the stakes, the metrics to watch, and the structural limits of custom builds.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 1103 | 1069 |
| sentence length mean | 14.6 | 19.3 |
| sentence length spread (sd) | 5.5 | 8.0 |
| rhythm health (0-1) | 0.426 | 0.904 |
| short sentences (<=8 words) | 15.6% | 9.4% |
| filler per 1,000 words | 2.72 | 1.87 |
| hedge per 1,000 words | 1.81 | 1.87 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 49.8 (FAIL) |
| sections restating the through-line | 2 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Hard failures still present

- accessibility gate: Flesch 49.8 < floor 50.0 — the long words costing the score, each to be replaced or used once: internal, anthropic, cloudflare, successor, replacement, engineers, control, software, network, platform, problem, workers

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 6, "regressions": 2, "rhythm_sd": [5.5, 5.0], "rhythm_health": [0.426, 0.366], "filler": [2.72, 1.31], "words": 761, "flesch": 49.7, "score": [false, -6, 0.44]}
{"attempt": 2, "ok": false, "hard": 1, "regressions": 0, "rhythm_sd": [5.5, 8.0], "rhythm_health": [0.426, 0.904], "filler": [2.72, 1.87], "words": 1069, "flesch": 49.8, "score": [false, -1, 4.64]}
```
