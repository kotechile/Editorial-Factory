# Signals: agentic_ai — 2026-11-23
**Window:** 2026-10-24 → 2026-11-23
**Queries run:** 12 (arXiv API × 6 terms, HN Algolia × 6 terms, web × 2 angles)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | IBM ships self-distilled agent memory in production (CUGA, watsonx Orchestrate); "the right amount of memory is a property of the model, not the memory" | http://arxiv.org/abs/2611.26361v1 | 2026-11-19 | DeepSeek-V3.2 +9.5 pts task completion with full 191-guideline set; gpt-oss-120b 39.9%→51.2% with all 199 guidelines but 55.4% with a selected subset of ~29 | memory tiering L1-L4 | 88 |
| 2 | GrepMem: lossless, index-free agent memory — an append-only plain-text log + grep beats structured memory | http://arxiv.org/abs/2611.25123v1 | 2026-11-18 | 95–97% accuracy on ContextBench vs at most 21% for lossy baselines; +8.8 pts over SUPO summarization on BCP-Multi | memory tiering L1-L4 | 85 |
| 3 | MemFolder: structure-guided memory folding cuts stored records in half without losing the answer | http://arxiv.org/abs/2611.26427v1 | 2026-11-19 | Retains 99.0% of average performance on LoCoMo/PersonaMem/LongMemEval with 50% fewer records; +1.9 pts retention over strongest baseline | memory tiering L1-L4 | 82 |
| 4 | NestDaddy grades every remote MCP server in the Official MCP Registry daily; first public reliability portrait of the tool fabric | https://nestdaddy.com/blog/state-of-remote-mcp-servers-2026 | 2026-11-22 | 86.8% of servers answer every daily check, 11.0% miss ≥1 in 10; 25.1% rewrote ≥1 tool in the last 30 days; 33.7% (13,848) hide tools behind a key; 322,242 public tools across 22,576 servers; median first answer 253 ms | tool use and MCP protocol fabric | 87 |
| 5 | BespokeLabs launches Multi-Agent Coordination Bench | https://benchmarks.bespokelabs.ai/multi-agent-coordination-bench/ (HN story 50550085) | 2026-11-18 | Benchmark landing page claims coordination-mode coverage; not yet fetched to figure level | multi-agent coordination modes | 66 |

**Dropped:** Google Developers Blog "MCP Stateless updates" (developers.googleblog.com, dated AUG 5 2026 — outside the 30-day window). NestDaddy/digitalapplied "100 MCP servers stress test" appears to predate the window (April 2026 ecosystem framing) — superseded by #4, which is dated 22 November 2026.

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=5 candidates=0 heuristic=- window=2026-10-24..2026-11-23 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

## Notes
- Papers' figures are from the arXiv API abstracts (fetched 2026-11-23), the primary record per skills/radar_30day.md. If a pair advances, fetch `arxiv.org/html/<id>v1` per-section counts before the brief is locked.
- #4 figures are from the NestDaddy report body fetched 2026-11-23 (dated 22 November 2026 in the page).
- Earned in fact-check pass: the report also states every server page carries a tool-change history with an RSS feed — "Our score rewards stability, and every server page shows a history of tool changes with an RSS feed, so users can see what changed and when." This is the change-feed material the draft cites.
