# Verified Brief: multi_agent_enterprise_fabric — 2026-10-14

**Angle:** `stale-grants-travel-the-graph` — Synthesis (Authority Type: Synthesis). Both legs primary; the
dual-anchor gate below is PASS (leg A 4 VERIFIED, leg B 4 VERIFIED). Primaries fetched by id from the
arXiv API (the abstract is the primary record for these preprints); the vendor page was fetched and read.

## Leg A — "CreepScope: Measuring Post-Use Authorization Exposure in Tool-Using Agents" (https://arxiv.org/abs/2610.15988, measured 2026-10-11)

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| A1 | A | The per-call authorization check cannot see how long earlier authority stays usable — the paper names the failure "privilege creep" | VERIFIED | https://arxiv.org/abs/2610.15988 | "Authorization checks at individual tool calls do not reveal how long earlier authority remains usable. We study this lifecycle failure as privilege creep: a capability stays reachable after its last justified workflow step." |
| A2 | A | Three standing-grant regimes share the same stale-after-use exposure of 13 capability-steps; a step lease is zero by construction; Full Access adds 91.33 never-required capability-steps | VERIFIED | https://arxiv.org/abs/2610.15988 | "A 96-cell deterministic replay over 12 controlled storage, communication, and cloud-operation workflows validates these semantics: Static Task Scope and Monotonic On-Demand retain mean CSEs of 26 and 13, whereas an oracle-controlled Step Lease has zero CSE and zero residual debt by construction. All three persistent regimes share the same stale-after-use exposure of 13, so their CSE differences come from scope and grant timing rather than post-use retention; Full Access alone adds 91.33 never-required capability-steps." (CSE = Capability-Step Exposure; RPD = Residual Privilege Debt) |
| A3 | A | An executed mail workflow: the injected stale send fires in all nine persistent-policy episodes and in none of the three step-lease episodes, with all required sequences still completing | VERIFIED | https://arxiv.org/abs/2610.15988 | "A separate 24-episode local case then lets Qwen2 7B choose tools in one simulated mail workflow: the injected stale send executes in all nine persistent-policy episodes and in none of the three Step-Lease episodes, while all 24 required action sequences complete." |
| A4 | A | CARRIED CAVEAT — the containment case is one workflow and one small model, by the authors' own statement | VERIFIED | https://arxiv.org/abs/2610.15988 | "These results establish a reproducible containment case, not cross-workflow or cross-model effectiveness." |

## Leg B — "When Agents Talk, Secrets Travel: Topology-Driven Leakage and Recipient-Conditioned Sanitization in Multi-Agent LLM Systems" (https://arxiv.org/abs/2610.16039, measured 2026-10-12)

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| B1 | B | Propagation, not compromise: information legitimately disclosed to one agent reaches an unauthorized one through routine coordination | VERIFIED | https://arxiv.org/abs/2610.16039 | "Multi-agent LLM systems (MALS) introduce a privacy-leakage problem that conventional sensitivity-based defenses miss, since information disclosed to one authorized agent can propagate through routine coordination to an unauthorized one, without compromise or malicious behavior." |
| B2 | B | Changing only the graph's shape moves disclosure to topology-introduced recipients from 0% to 52.2% while surface leakage stays flat | VERIFIED | https://arxiv.org/abs/2610.16039 | "We evaluate 485 scenarios across coordinator-worker, peer-to-peer, and hierarchical topologies, instrumenting seven communication channels… Topology changes where protected information propagates, with disclosure to topology-introduced recipients rising from 0% to 52.2% while surface leakage stays nearly flat at 60.6-62.8%." |
| B3 | B | Framework choice alone drives a 150x leakage spread, so topology alone does not explain it | VERIFIED | https://arxiv.org/abs/2610.16039 | "This effect persists across four generator models and a second orchestration framework, though magnitude and relay paths differ; framework choice separately drives a 150x leakage spread, so topology alone is not sufficient." |
| B4 | B | The recipient-conditioned sanitizer cuts residual disclosure to 29.25% from 96.7% and keeps 94.1% of authorized disclosures — but its residual is dominated by what its detector misses | VERIFIED | https://arxiv.org/abs/2610.16039 | "RECONS reduces residual disclosure from 96.7% without sanitization to 29.25%, preserving 94.1% of authorized disclosures versus 20.5% under blanket redaction. Detection coverage is the dominant bottleneck, accounting for 95.5% of residual disclosures." |

## Bridge / corroborating rows (each its own primary; the article cites the URL below)

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| R1 | Bridge | The shipped enterprise control plane at the MCP boundary enforces a *single-use allowance per exact action* — and states its own limit | VERIFIED | https://arxiv.org/abs/2610.14810 | "signed permission for an exact action, a shared allowance that can be consumed only once, target-side conditions for applying the change, and retained outcome records… In the single-resource evaluation, 6,560 concurrent ledger claim attempts yielded exactly one successful claim for each of 82 allowances… A 32-call gateway race produced one committed mock effect, and a retry after a lost response produced no additional dispatch." Limit, in the paper's own words: "Deliberately permissive policy nevertheless authorized an undesirable effect, exposing the limits of execution authorization." Untested, per the paper: "Distributed reservations, enforcement of every production access route, native crash recovery, exactly-once effects at real targets, and interoperability between independent implementations remain untested." Evaluation is three etcd members on one host with synthetic auth inputs and a mock target. |
| R2 | Bridge | The enterprise answer shipping this month is a node inventory with per-request identity — dated 2026-10-08 | VERIFIED | https://docs.cloud.google.com/agent-registry/overview | "Agent Registry is a centralized catalog that lets you store, discover, and govern agentic components, such as Model Context Protocol (MCP) servers, tools, standalone skills, and AI agents, within Google Cloud… It maintains the authoritative inventory of agents, MCP servers, tools, skills, and external endpoints, and generates the identifiers and resource names referenced by discovery clients and security policies… Other services, such as Agent Identity, determine who makes the request." Page footer: "Last updated 2026-10-08 UTC." No measurement on the page — a design statement, carried as friction, never as an anchor. |
| R3 | Bridge | Action-level evaluation detects only 0.09 of state-dependent violations; state-level evaluation reaches 0.96 | VERIFIED | https://arxiv.org/abs/2610.17685 | "Experiments on the benchmark show that action-level evaluation detects only 0.09 of state-dependent violations, whereas state-level evaluation reaches 0.96. Existing guardrail methods largely overlook such risks unless they are explicitly applied to workflow states." |
| R4 | Bridge | Evidence authority is not release authority — a work product may be needed as evidence without its full meaning being authorized to persist | VERIFIED | https://arxiv.org/abs/2610.16414 | "This creates a privacy boundary that task relevance alone does not capture: an observation may be needed as evidence for a task without its full semantics being authorized to persist. We call this mismatch the purpose-to-state semantic gap. The key distinction is that evidence authority is not release authority." |

## Gate rules applied

- **Dual-Anchor Gate (fact_check.md §5): PASS** — leg A 4 VERIFIED, leg B 4 VERIFIED; both trace to
  primary records fetched in this run (arXiv abstracts by id, both dated inside the 2026-09-14 → 2026-10-14 window).
- **REMOVED: 0. FLAGGED: 0.** One caveat is *carried into the draft* rather than flagged as a defect: A4
  (one workflow, one small model) and R1's untested list must appear in `## The catch`.
- **Arithmetic authorised (compute before drafting):** A2's CSE comparison (26 / 13 / 0 / 91.33) is quoted as
  published, not derived. Date intervals used by the draft: 2026-10-08 → 2026-10-11 = **3 days**;
  2026-10-11 → 2026-10-12 = **1 day**. No subtraction of two figures is authorised — the draft must not
  present "91.33 − 13" or any derived spread as a finding.
- **Attribution rule:** the vendor page is the *only* non-A measure in this brief. It may be described as what
  the page says, never as evidence that inventory-based governance fails (no source measures that).
- **No unsourced number may enter the draft.** Figures permitted: 13, 91.33, 26, 0, 96 (cells), 12 (workflows),
  24 (episodes), 9, 3, 7B, 485, 7 (channels), 3 (topologies), 0% → 52.2%, 60.6–62.8%, 150x, 96.7% → 29.25%,
  94.1%, 20.5%, 95.5%, 6,560, 82, 32, 0.09, 0.96, and the dates.
