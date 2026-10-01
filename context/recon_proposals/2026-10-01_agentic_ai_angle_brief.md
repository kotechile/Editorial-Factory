# Angle Brief: agentic_ai — 2026-10-01

**Angle Type:** Single-Signal

**Winner:** Fold the model choice into the plan itself — Planner-as-Router cuts multi-agent cost 44% with no router model, and its own pilot warns cheap routing may quietly compound errors on long workflows.

**Scores:** N=8 A=8 S=8 → Composite=8.0

**Hook:** A frontier model can cost 25 times what a small model costs per token, and that gap compounds every time a workflow chains calls together. On Sept 26, three authors posted Planner-as-Router (PaR) to arXiv with a different fix: stop routing models downstream, and fold the model-tier choice into planning itself — so the planner assigns each subtask a small, mid, or frontier model before any specialist runs. The result is a 44% cost cut against running the frontier model everywhere, at a 2.9-point accuracy cost, with no separate router model and no training data. The quietest line is the most interesting: a small pilot hints that cheap routing "may carry a hidden compounding penalty on compositional workflows."

**Tension:** Agentic workloads already burn roughly 4× the tokens of a chat turn, and multi-agent fan-out roughly 15×, because every step re-sends instructions, tool definitions, and context. The dominant cost fix has been per-call cascade routing — look at one node, decide, move on. PaR's bet is that this is backwards: routing decisions should be made at plan time, where the dependencies between subtasks are visible, not one node at a time by a separate router model. The people this lands on first are the ai_architect deciding where each subtask's state lives and which model tier each step can afford — and the paper's own hypothesis is that routing cheap on compositional workflows is exactly where errors quietly compound, a failure mode that would not show up in single-step evals.

**Target reader:** ai_architect

**Single claim to defend:** Planner-as-Router (arXiv:2609.32917, Sept 26, 2026) shows that folding model-tier selection into multi-agent planning — assigning each subtask a small/mid/frontier model at plan time, with no separate router model or training data — cuts cost 44% versus all-frontier routing at a 2.9-point accuracy cost across 1,157 evaluations, and its own preliminary finding flags that cheap routing may carry a hidden compounding penalty on compositional workflows, making model routing an architectural decision rather than a post-hoc cost fix.

**Runner-ups + why rejected:**
- OpenAI Agents API computer use (Sept 29, changelog): fresh primary, on the tool-use angle, but an incremental extension of the Agents API whose runtime loop already won on 09-14 (`openai-agents-api-managed-runtime`); capped novelty → N=7 A=8 S=7 = 7.7, below the gate.
- OpenAI DevDay "Dots" (always-on agents, Sept 29): same-vendor, same-day, shares the always-on-runtime framing with computer use; not an independent leg → 7.2.
- "Be Careful Who You Trust" (arXiv:2609.31704, corrupted-communication coordination): real primary but game-theory framing, less load-bearing for a practitioner audience → 7.0.
- GLIDE (arXiv:2609.32295, heterogeneous-agent eval): eval-adjacent, off the vertical's core architecture axis → 6.8.

**Synthesis attempted + rejected:** PaR ⨂ OpenAI computer-use (plan-time routing meets a browser tool whose per-step screenshot cost inflates token volume) scores E=8 A=8 S=8 → 8.0. It does **not** beat the single-signal PaR by the ≥ 0.3 margin required by `virality_judge.md` §2.5, and both legs sit on the same cost axis — a tie-win synthesis displacing a stronger single story. Taken: single-signal PaR.

**Prior-cycle de-dup check (passed):** OWASP excessive agency (09-03), Anthropic multi-agent turf war (09-07), Google 4 patterns (09-10), OpenAI Agents API runtime (09-14), Salesforce harness > model (09-17), MCP Skills transport (09-21), MASkills skills-as-learning (09-24), GPT-6 prompt caching (09-28). PaR's thesis (plan-time model-tier routing + error-compounding penalty) is distinct from prompt-caching (cache-stability → interface-design rule) and from harness-evolution (training); the subagent-cost axis is the same, but the mechanism and the claim are new. Fresh primary (arXiv, Sept 26), fresh event, fresh angle. Not a retread.
