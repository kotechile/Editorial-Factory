# Signals: agentic_ai — 2026-11-26
**Window:** 2026-10-27 → 2026-11-26
**Queries run:** 9 (5 arXiv API, 6 HN Algolia; 2 web corroborations)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Practitioner manifesto: multiagent coding declared a paradigm shift, with an orchestrator (Grimm) running "2–100+ Claudes in a devbox" that talk to each other | https://www.kalzumeus.com/2026/11/25/multiagent-coding-is-the-future/ | 2026-11-24 | "Grimm puts 2-100+ Claudes in a devbox. They can talk to each other. You can talk to them via a web UI over tmux."; multiagent "as much of a paradigm shift as LLMs coding" | multi-agent coordination modes | 88 |
| 2 | First-party launch: Perplexity Computer ships a Multiagent effort level above Ultra — lead agent runs up to 16 agents on different frontier models in parallel, cross-checking each other | https://www.perplexity.ai/hub/blog/introducing-computer-multiagent | 2026-11-17 | "the lead can assign up to 16 agents, while taking on part of the work itself"; default team Claude Opus 5.5 + GPT 6.1 Sol + Gemini 4 Carbon; Fable 5.2 plans | multi-agent coordination modes | 84 |
| 3 | Measured cost of fan-out: empirical study on repository construction — parallel subagents raise hidden-test pass rates by only 1–5 points at up to 3.8× the cost; a one-sentence probe instruction recovers most of the gain | https://arxiv.org/abs/2611.33893 | 2026-11-25 | "parallel subagents raise the share of hidden tests passed by only about 1 to 5 percentage points, at up to 3.8 times the cost of a single agent"; "one sentence to probe the reference program first recovers most of this gain at a fraction of the cost" | subagent cost optimization | 92 |
| 4 | Coordination benchmark shows the duplicated-work failure concretely: three agents fixed the same failure simultaneously; two of three parallel fixes discarded after merge conflicts | https://benchmarks.bespokelabs.ai/multi-agent-coordination-bench/ | 2026-11-18 | "Cotton, dune and plum each pushed a separate fix for the T0068 coast and TMI failure. Dune and plum hit merge conflicts and reset to origin"; "Two of three parallel fixes discarded after conflicts" | multi-agent coordination modes | 78 |
| 5 | Budget-aware routing: MeterRouter hits comparable accuracy to the strongest MAS at 82% lower cost by treating the per-query budget as an explicit constraint | https://arxiv.org/abs/2611.34327 | 2026-11-25 | "reaching that accuracy at 82% lower cost than the strongest MAS router" | subagent cost optimization | 82 |
| 6 | Routing reliability is a distinct scaling bottleneck: CypherMAS isolates communication in fixed graphs — small models fail at routing outright, models above 27B degrade as graph diameter grows | https://arxiv.org/abs/2611.33242 | 2026-11-24 | "dense models above 27B degrade with diameter, and successful runs exceed minimum LLM calls"; eleven open-weight models 4B–753B | distributed microservices architecture | 76 |

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=6 candidates=0 heuristic=- window=2026-10-27..2026-11-26 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

## Dated background
- https://arxiv.org/abs/2611.29804 — FORGETMENOT (2026-11-22), memory privacy audit of commercial agents (~3800 sessions, ~20% transparency gap, deletion leakage). Strong, but off the coordination beat.
- https://arxiv.org/abs/2611.27041 — Subverting Tool Arguments (2026-11-20), defense-evading metadata poisoning in LLM agents.
- https://arxiv.org/abs/2611.34215 — PROVE (2026-11-25), long-horizon LLM collusion mitigation.
- https://arstechnica.com/security/2026/11/amazon-says-hackers-ai-agents-found-and-exploited-0-day-with-little-human-input/ (2026-11-26) — HN-circulated security story; security beat, not architecture.
- https://www.wired.com/story/ai-agents-can-get-honeypotted-too-aw/ (2026-11-26) — Anthropic agent honeypot; security beat.

**Dating note:** all six table rows carry the publisher's own date field (arXiv `published`, HN/Algolia `created_at`, Perplexity blog byline 2026-11-17, Bespoke bench page discovered 2026-11-26 with in-page run minutes and HN circulation 2026-11-18; kalzumeus post byline 2026-11-24). None is a status page.
