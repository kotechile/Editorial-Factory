# Review report — 2026-10-28_your-11-agents-3-die-none-wrong_final.md

- verdict: **ACCEPTED**
- draft: `2026-10-28_your-11-agents-3-die-none-wrong_draft.md` · attempt kept: 2 of 2
- figures in the ledger: 15 · citations: 5 · quotes: 0 · sources: 5

## The reviewer's reading

THROUGH-LINE: Agent fleets fail under load not because individual calls break, but because uncoordinated retries exhaust shared capacity, meaning the only effective fix is placing concurrency limits, rate-limit state, and retry queues in a single gateway in front of the shared key.
SHAPE: 
Lead: Introduces the failure mode (concurrency causing queue collapse despite API capacity).
The big picture: Explains the queueing math (Little's Law) and why individual agents cannot see the bottleneck.
By the numbers: Provides the measured failure rates, queue sizes, and the ablation test proving concurrency caps alone fail.
What I'd watch: Details the gateway solution, who handles retries, and what metrics matter next.
The catch: Evaluates the limitations of the preprint data and the architectural trade-offs of adding a central proxy.
At a glance: Summarizes the argument for the skimmer.
NOT YET EARNED: The draft claimed a "live check against two local model servers," but the verified brief states the field run wasted tokens "despite the API having sufficient aggregate capacity," pointing to a shared API key rather than local servers. I have removed the local server claim to match the brief.

## What the rewrite did to the prose

| metric | draft | final |
|---|---|---|
| words | 1140 | 1122 |
| sentence length mean | 19.0 | 18.2 |
| sentence length spread (sd) | 7.9 | 7.7 |
| rhythm health (0-1) | 0.931 | 0.984 |
| short sentences (<=8 words) | 12.9% | 12.5% |
| filler per 1,000 words | 0.88 | 0.0 |
| hedge per 1,000 words | 0.0 | 0.0 |
| abstraction per 1,000 words | 0.0 | 0.0 |
| repeated 5-grams | 0 | 0 |
| sentences repeated verbatim | 0 | 0 |
| Flesch reading ease | — | 53.8 (PASS) |
| sections restating the through-line | 1 | 1 |
| staccato paragraphs | 0.0% | 0.0% |

## Attempt trail

```
{"attempt": 1, "ok": false, "hard": 4, "regressions": 1, "rhythm_sd": [7.9, 7.6], "rhythm_health": [0.931, 0.85], "filler": [0.88, 0.0], "words": 995, "flesch": 52.8, "score": [false, -4, 0.23]}
{"attempt": 2, "ok": true, "hard": 0, "regressions": 0, "rhythm_sd": [7.9, 7.7], "rhythm_health": [0.931, 0.984], "filler": [0.88, 0.0], "words": 1122, "flesch": 53.8, "score": [true, 0, 1.3]}
```
