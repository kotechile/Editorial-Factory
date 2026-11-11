# Signals: multi_agent_enterprise_fabric — 2026-11-11
**Window:** 2026-10-12 → 2026-11-11
**Queries run:** 31 (12 arXiv API sweeps sorted by submission date; 8 Hacker News Algolia `search_by_date` pulls bounded to the window with a points ≥ 8 floor; 2 web fan-outs on the SAP TechEd beat; 3 full-text arXiv HTML fetches for figure verification; 3 first-party SAP pages fetched; 3 dating lookups)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | WorkflowArena benchmark (Jiang et al., Navers Lab / Einsia.AI / Tsinghua) | https://arxiv.org/abs/2611.12856 | 2026-11-09 | 145 long-horizon tasks, 8 domains, 22 model–harness–effort configurations; best configuration resolves **36.95%**; at high effort Opus and Sonnet in Claude Code average **0.86 and 0.76** Workflow calls per task with **5.55 and 6.14** worker invocations per Workflow, while Astra and Sol in Codex average **2.09 and 1.94** calls with **1.72 and 1.69** workers; holding the executor fixed on 32 tasks, Opus-authored workflows add **6.41 points** in static mode and **6.27** in dynamic mode averaged over four executors, while Astra-authored workflows average **−2.53** in static mode | Orchestration quality is a capability separable from task performance, and it travels with the authored workflow rather than the executing model | 94 |
| 2 | SAP TechEd 2026 press release — "SAP Empowers AI Developers to Build What Matters and Turn Intent into Autonomous Execution" | https://news.sap.com/?p=248010 | 2026-10-27 | Joule Studio builders choose "from more than 70 AI models"; third-party agents "securely invoke Joule Agents through a governed agent gateway"; new SAP Enterprise AI Gateway "will consolidate authentication, policy enforcement, routing, monitoring, usage tracking and auditing"; Joule Studio gains "new observability and administrative controls … visibility into agent behavior, model usage and spend" | The enterprise fabric is being sold as one governed platform with a wide model menu and a governed pipeline in front of production | 86 |
| 3 | SAP TechEd 2026 Innovation News Guide | https://www.sap.com/topics/events/teched/innovation-news-guide-2026 | 2026-10-27 | "All modifications go through a governed pipeline before production"; Joule Studio can "design and run n8n workflows"; SAP Enterprise AI Gateway "General availability is planned for Q1 2027"; A2A gateway access control "General availability is now underway in a phased approach" | What the vendor's change control actually approves: an agent build passing a pipeline, not a run-time topology | 78 |
| 4 | SAP "Top 5 things to know from SAP TechEd 2026" | https://www.sap.com/blogs/top-sap-teched-2026-announcements | 2026-10-27 | "A single, governed entry point lets agents from different providers participate in the same business workflow, with access control enforced throughout." | The governed entry point is offered as the answer to multi-vendor orchestration | 74 |
| 5 | Agent Architecture Cost–Success Trade-offs (Nandi et al., Amazon / University of Washington) | https://arxiv.org/abs/2611.12953 | 2026-11-07 | 13 enterprise SOPs, 4 architectures, 8 arms, model held fixed at `claude-opus-4-8`; every coordinated arm spends **1.4–4.7×** the baseline's tokens and **2.6–5.8×** its latency; single agent is Pareto-optimal (24.9k tokens, 67.4%); orchestration-v2 is the only arm to beat it significantly (**OR 1.72, p = 0.007**) at **4.7×** tokens | Architecture choice is mostly not separable in aggregate; cost is the robust separator | 88 |
| 6 | ShadowBench-MCP (shadow invocations in MCP-style tool routing) | https://arxiv.org/abs/2611.11720 | 2026-11-09 | 120 routing decisions, 96 original-versus-variant comparisons, six security-sensitive workflows; efficiency-first routing produces a **29.2%** shadow-invocation rate and **26.7%** safety-tool skip rate; policy-aware routing reduces them to **4.2%** and **1.7%** (85.7% relative reduction); pre-execution ROC AUC up to **0.94** | The route a model picks is itself the control surface | 80 |
| 7 | ErosionBench (alignment decay in enterprise multi-agent systems) | https://arxiv.org/abs/2611.11266 | 2026-11-08 | 1,728 scenarios across four enterprise domains and four decay mechanisms, plus 198 image-based attacks; "Perimeter defenses suppress attacks only by over-refusing **54–92%** of legitimate work"; reference Meta-Auditor reaches **98.5%** recall at a **2.9%** false-positive rate on a 906-scenario held-out split | The perimeter's failure mode is over-refusal, not only leakage | 84 |
| 8 | MCPHallu (reasoning, execution and memory hallucinations in MCP agents) | https://arxiv.org/abs/2611.07689 | 2026-11-05 | 358 tasks, 36 production MCP servers, 5,012 trajectories, 14 agents; average score **0.642**; Unreachable Goal tasks average **0.458** with **23.2%** of runs passing; "agents often continue issuing tool calls or claim successful completion rather than recognizing infeasible goals" | A fabric's stopping condition is weaker than its calling condition | 76 |
| 9 | From Process Models to Composable Agentic Workflows (BPMN + agents + enterprise knowledge) | https://arxiv.org/abs/2611.13196 | 2026-11-09 | SemTalk BPMN models are transformed into executable workflows on a LangGraph/Pregel runtime; "conventional BPMN controls process flows, deterministic decisions, system interactions and human approvals"; agents expose business processes as reusable "Agentic Tools" | The process model, not the agent, is the reusable unit — a claim this desk already argued on 2026-11-04 | 72 |
| 10 | ReTrace (distilling tool-using agents into planner-free workflows) | https://arxiv.org/abs/2611.14492 | 2026-11-10 | 79 procedures from a production platform: **93.8%** completion against the agent's **96.8%** at **24%** lower cost per task; on τ²-Bench **75.8%** task success and **1.3 s** against the agent's **170 s** | Compiling the procedure removes the planner — a thesis this desk published on 2026-11-04 | 74 |

**Dating note.** All ten rows are dated inside the window from the publisher's own record. Rows 2–4 are
first-party SAP pages for the TechEd 2026 event held in Berlin **27–29 October 2026**; the press release
prints "October 27, 2026" in its own body, and the Innovation News Guide's general-availability lines
(phased now, Q1 2027 for the Enterprise AI Gateway) are what the piece must keep straight — the gateway
is announced and planned, not shipped. Rows 1, 5–10 are arXiv records dated by their own submission
stamp (`2611.*` = November 2026); row 1's figures were read from the paper's HTML body (Tables 1–2,
§§ 4.2–4.5), not from the abstract, because the abstract rounds the transfer gain to one decimal.

**Row-1 body figures used for the claim cells** (from https://arxiv.org/html/2611.12856v1): "The best
configuration, Opus at max effort, resolves 36.95% of tasks"; "Opus at high effort resolves 34.11% of
tasks with 7.36M tokens per task"; "Sol at low effort resolves 27.59% of tasks at $3.61 per task and
Opus at high effort 34.11% at $6.66, whereas Astra at xhigh effort resolves 30.80% at $29.26, 3.31
points below Opus at high effort at 4.4× its cost"; "a single call accounts for 70% of Opus and 68% of
Sonnet executions, compared with about 32% for Astra and Sol"; "groups of nine or more workers make up
24% of Opus and 30% of Sonnet invocations, whereas about 99% of Astra and Sol Workflows contain at most
four workers"; "From low to max effort, Astra's calls per task rise by 67%, from 1.33 to 2.22, while
its worker invocations per Workflow change by only 5%"; "With Opus dynamic workflows, Kimi improves
from 35.75 to 46.61 and DeepSeek from 18.37 to 25.24, while Luna and Doubao obtain their highest scores
with Opus static workflows, at 30.37 and 28.04"; "Because the source model never edits the workspace,
these gains arise from the workflow it authors, including the instructions it gives each worker, rather
than from work performed by the source."

**Row-1 limitations carried into the brief** (paper's own "Limitations"): "Each configuration is
evaluated once per task, so differences between closely ranked configurations are reported without
variance estimates"; each model ran "in a single harness, and differences between the Claude and GPT
systems therefore reflect the model and its harness jointly"; "because source models also write the
instructions given to workers, its gains may combine better organization with task knowledge conveyed
in those instructions"; the transfer experiment covers "a subset of the benchmark and two source
models", and content/3-D deliverables are graded by an LLM judge with no measured human agreement.

## Dated background

- **Rivet** — "Launch HN: Rivet (YC W23) – Scale and Orchestrate Agents on S3", 2026-11-05, 122 points,
  59 comments: https://github.com/rivet-dev/rivet . Industry direction only; a code-availability row,
  kept out of the table so the pairing layer cannot match every candidate against it.
- **WorkflowArena project homepage** (task catalogue, leaderboard): https://lab.einsia.ai/workflowarena .
- **arXiv HTML record for row 1** (figures verified from body text): https://arxiv.org/html/2611.12856v1 .
- **Camunda 8.10** ("The Great Process Re-Engineering Starts Now", dated 2026-10-13 by the vendor's own
  announcements index at https://camunda.com/blog/category/announcements) — noted as an in-window
  process-orchestration release, but its own post URL 404'd on fetch, so no claim rests on it.

## Candidate Synthesis Pairs



<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=10 candidates=5 heuristic=0.66-0.75 window=2026-10-12..2026-11-11 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

| Pair | Signals | Shared axis | Contrasting axis | Anchor URLs | Heuristic | Flags |
|---|---|---|---|---|---|---|
| 1 | #2 ⨂ #8 | governance_x_runtime | A: The enterprise fabric is being sold as one governed platform with a wide model menu and a governed pipeline in front of production | B: A fabric's stopping condition is weaker than its calling condition | https://news.sap.com/?p=248010 https://arxiv.org/abs/2611.07689 | 0.75 | prior_cycle_token_overlap:execution |
| 2 | #1 ⨂ #2 | governance_x_runtime | A: Orchestration quality is a capability separable from task performance, and it travels with the authored workflow rather than the executing model | B: The enterprise fabric is being sold as one governed platform with a wide model menu and a governed pipeline in front of production | https://arxiv.org/abs/2611.12856 https://news.sap.com/?p=248010 | 0.74 | - |
| 3 | #2 ⨂ #5 | governance_x_runtime | A: The enterprise fabric is being sold as one governed platform with a wide model menu and a governed pipeline in front of production | B: Architecture choice is mostly not separable in aggregate; cost is the robust separator | https://news.sap.com/?p=248010 https://arxiv.org/abs/2611.12953 | 0.74 | - |
| 4 | #2 ⨂ #6 | governance_x_runtime | A: The enterprise fabric is being sold as one governed platform with a wide model menu and a governed pipeline in front of production | B: The route a model picks is itself the control surface | https://news.sap.com/?p=248010 https://arxiv.org/abs/2611.11720 | 0.67 | - |
| 5 | #2 ⨂ #9 | governance_x_runtime | A: The enterprise fabric is being sold as one governed platform with a wide model menu and a governed pipeline in front of production | B: The process model, not the agent, is the reusable unit — a claim this desk already argued on 2026-11-04 | https://news.sap.com/?p=248010 https://arxiv.org/abs/2611.13196 | 0.66 | - |

**Heuristic terms (advisory):**
- #1: token_coverage=0.75 intensity=0.81 angle_fit=0.5 contrast=0.92 → 0.75 (governance_x_runtime)
- #2: token_coverage=0.5 intensity=0.9 angle_fit=0.75 contrast=0.94 → 0.74 (governance_x_runtime)
- #3: token_coverage=0.5 intensity=0.87 angle_fit=0.75 contrast=1.0 → 0.74 (governance_x_runtime)
- #4: token_coverage=0.5 intensity=0.83 angle_fit=0.5 contrast=0.92 → 0.67 (governance_x_runtime)
- #5: token_coverage=0.5 intensity=0.79 angle_fit=0.5 contrast=0.93 → 0.66 (governance_x_runtime)
<!-- synthesis-seed:end -->

