# Verified Brief: agentic_ai (evergreen) — 2026-10-05

Every claim below was read verbatim from the cited primary source on 2026-10-05.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| 1 | Coordination upside | A multi-agent system (Opus 4 lead + Sonnet 4 subagents) outperformed single-agent Claude Opus 4 by 90.2% on an internal research eval | VERIFIED | https://www.anthropic.com/engineering/multi-agent-research-system | "a multi-agent system with Claude Opus 4 as the lead agent and Claude Sonnet 4 subagents outperformed single-agent Claude Opus 4 by 90.2% on our internal research eval." |
| 2 | Coordination cost | Multi-agent systems use about 15× the tokens of chats (agents alone about 4×) | VERIFIED | https://www.anthropic.com/engineering/multi-agent-research-system | "agents typically use about 4× more tokens than chat interactions, and multi-agent systems use about 15× more tokens than chats." |
| 3 | Failure taxonomy | Analysis of 150 traces yields 14 unique failure modes in 3 categories (system design, inter-agent misalignment, task verification) | VERIFIED | https://arxiv.org/abs/2503.13657 | "We develop MAST through rigorous analysis of 150 traces … This process identifies 14 unique modes, clustered into 3 categories: (i) system design issues, (ii) inter-agent misalignment, and (iii) task verification." |
| 4 | Ensemble upside | A layered ensemble of open-source LLMs scored 65.1% on AlpacaEval 2.0 vs 57.5% for GPT-4 Omni | VERIFIED | https://arxiv.org/abs/2406.04692 | "our MoA using only open-source LLMs is the leader of AlpacaEval 2.0 by a substantial gap, achieving a score of 65.1% compared to 57.5% by GPT-4 Omni." |
| 5 | Handoff topology ships | A coordinated multi-agent conversation framework reached top results on GAIA by about 8 points | VERIFIED | https://www.microsoft.com/en-us/research/blog/autogen-enabling-next-gen-llm-applications-via-multi-agent-conversation-framework/ | "we were actually able to, in March, achieve the top results on the GAIA leaderboard for that benchmark by about 8 points." |

**Gate result:** 5/5 VERIFIED, 0 FLAGGED, 0 REMOVED. Evidence spans 3 hosts (anthropic.com, arxiv.org, microsoft.com). Not a synthesis brief — no dual-anchor gate applies; the two evidence families (capability/cost measurement in rows 1–2, failure/ensemble/shipping evidence in rows 3–5) are each independently verified.

**Evergreen framing:** durable decision = which coordination topology to wire and what it costs. Time-bound figures carry `as of` dates (Anthropic 2025 write-up; MAST v1 2025-03-17; MoA 2024-06-07).
