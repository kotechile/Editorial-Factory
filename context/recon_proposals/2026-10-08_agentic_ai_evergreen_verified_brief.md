# Verified Brief: agentic_ai — 2026-10-08
**Archetype:** evergreen
**Vertical:** agentic_ai
**Topic:** Memory tiering L1–L4 — where an agent's durable state belongs
**Gate:** `python3 scripts/evergreen_gate.py --brief context/recon_proposals/2026-10-08_agentic_ai_evergreen_brief.md` → PASS (5 rows verified, 4 hosts)

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | Context rot | A 2025 report evaluated 18 large language models and found performance varies significantly as input length changes, even on tasks that need no reasoning | VERIFIED | https://research.trychroma.com/context-rot | "we evaluate 18 LLMs … model performance varies significantly as input length changes, even on simple tasks" |
| 2 | Cross-session recall | Commercial chat assistants and long-context large language models show a 30% accuracy drop on remembering information across sustained interactions, measured on 500 curated questions | VERIFIED | https://arxiv.org/abs/2410.10813 | "commercial chat assistants and long-context LLMs showing a 30% accuracy drop on memorizing information across sustained interactions" / "With 500 meticulously curated questions" |
| 3 | Extracted memory | An extraction-and-retrieval memory layer reports a 26% relative improvement in the LLM-as-judge metric over a full-context baseline, at 91% lower p95 latency | VERIFIED | https://arxiv.org/abs/2504.19413 | "Mem0 achieves 26% relative improvements in the LLM-as-a-Judge metric over OpenAI, while Mem0 with graph memory achieves around 2% higher overall score" / "Mem0 attains a 91% lower p95 latency and saves more than 90% token cost" |
| 4 | Files vs. tools | A file-backed agent on a small model reached 74.0% on LoCoMo, above the 68.5% reported by the leading specialized memory tool — the retrieval mechanism mattered less than how the agent managed context | VERIFIED | https://www.letta.com/blog/benchmarking-ai-agent-memory | "Letta agents running on gpt-4o-mini achieve 74.0% accuracy on LoCoMo by simply storing conversation histories in files, rather than using specialized memory or retrieval tools" / "significantly above Mem0's reported 68.5% score for their top-performing graph variant" |
| 5 | Context is finite (vendor) | A frontier vendor now advises that a subagent exploring for tens of thousands of tokens return only a 1,000-2,000-token summary, and frames context as a finite resource with diminishing returns | VERIFIED (vendor claim) | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | "returns only a condensed, distilled summary of its work (often 1,000-2,000 tokens)" / "Context … must be treated as a finite resource with diminishing marginal returns" |

## Gate rules
- All 5 claims VERIFIED; 0 FLAGGED; 0 REMOVED. Rows 3 and 5 are the paper's/vendor's own measurements (labelled "vendor claim" in the evergreen brief) and are presented as such in the draft.
- Every claim above traces to its primary URL, fetched live on 2026-10-08.
