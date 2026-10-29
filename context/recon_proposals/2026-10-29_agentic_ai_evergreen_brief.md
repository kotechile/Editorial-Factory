# Evergreen Brief: agentic_ai — 2026-10-29
**Archetype:** evergreen
**Vertical:** agentic_ai
**Persona:** ai_architect
**Decision the reader is facing:** Which isolation substrate an agent's code-execution tool runs on — a permanently reserved worker, a container or sandbox provisioned per trajectory, or a hosted sandbox billed by the second — and how many actions a trajectory must run before its cold start stops being the dominant cost of the turn.
**Durability:** The arithmetic is structural, not a model-version artifact: a fixed provisioning cost S divided across N actions is a per-action tax of S/N, so the substrate that wins a 150-step run loses a 6-step one no matter which model sits above it, and no vendor can remove the boot by pricing it differently. The measured spread (up to 110x across four substrates, as of the 01 Jul 2026 SoCC preprint), the prototype result (2.9x P99 and 45.9% peak memory, as of arXiv 2607.23933v2, 05 Aug 2026), the microVM floor (under 125 ms, as of the Firecracker project page read 2026-10-29) and the list prices (as of the E2B pricing page read 2026-10-29) are dated snapshots a reader can re-check in twelve months; the S/N rule they feed does not expire.
**De-dup:** `2026-10-26_agentic_ai_evergreen_brief.md` is this vertical's nearest prior artifact, three days old, and it decides how many deployed boundaries the runtime should own — a service-boundary purchase evaluated on deploy and on-call cost. This one takes a single boundary as given and prices its boot: what one sandbox costs per action, and when warmth pays. Cross-vertical check run and dropped by hand: `2026-10-26_your-agent-contract-gap-63-unmet` treats the sandbox as a trust control at a call site (what may the workload reach), never as a latency or memory cost. `grep -ril "cold start\|cold-start\|firecracker\|microvm" published/` returns no artifact arguing boot economics, so the mechanism is unclaimed in the whole corpus.
**Thesis:** The sandbox is a metered boundary, not plumbing: its boot is paid once per trajectory and amortised across that trajectory's actions, so a 110x cold-start spread decides throughput on short runs and disappears on long ones — and both published answers to it (reserve forever, or create lazily) are wrong, because the only fix that moves both numbers is overlapping the boot with inference the model was going to spend anyway.

**Lead:** The vertical's own beat — `primary_angles` "deterministic RPC boundaries" and "tool use and MCP protocol fabric" — plus the persona's stated want ("microservice RPC boundaries", "state recovery patterns"). The specific material: two 2026 papers that measure the sandbox provisioning path rather than assert it — SpecBox (Beihang/Leeds/Sydney, arXiv 2607.23933v2, 05 Aug 2026), which frames the trade-off as persistent reservation versus lazy on-demand over MCP-invoked sandboxes, and *The Rollout Infrastructure Tax in Coding-Agent Reinforcement Learning* (arXiv 2607.01415v1, 01 Jul 2026), a four-substrate head-to-head that finds up to 110x variation in cold-start latency. The floor is set by Firecracker's own published boot characteristics (<125 ms, <5 MiB), and the price side by E2B's list, which meters a running sandbox per second and sells concurrency in blocks. GSC was checked as a bonus signal only (`2026-10-22_gsc_agentic_ai_opportunities.md`, candidate count 0) — no impressions to mine, no veto.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | SpecBox: Speculative Sandbox Scheduling for Efficient LLM Agent Serving (Zhang et al., arXiv 2607.23933v2) | https://arxiv.org/html/2607.23933v2 | 2026-10-29 | 2.9 — SpecBox cuts P99 end-to-end latency by up to 2.9x against the on-demand sandbox baseline on high-concurrency multi-turn agent traces | measured (academic prototype, own traces; not peer-reviewed) |
| 2 | SpecBox (same paper, same abstract) | https://arxiv.org/html/2607.23933v2 | 2026-10-29 | 45.9% — peak memory consumption cut by 45.9% against permanently reserved sandbox deployments | measured (academic prototype) |
| 3 | The Rollout Infrastructure Tax in Coding-Agent Reinforcement Learning (Graviet et al., arXiv 2607.01415v1, SoCC 2026 preprint) | https://arxiv.org/html/2607.01415v1 | 2026-10-29 | 110 — cold-start latency varies by up to 110x across single containers, hosted sandboxes, Kubernetes-orchestrated containers and cloud VMs, with a 1.8x spread in projected worker-hours for one million 150-step trajectories | measured (vendor-authored: all six authors affiliated with Daytona) |
| 4 | The Rollout Infrastructure Tax (Table 1, same paper) | https://arxiv.org/html/2607.01415v1 | 2026-10-29 | 278 h — one extra second per rollout across one million rollouts adds 278 worker-hours, and 100 ms per action over 150 actions adds 4,167 worker-hours | measured (arithmetic table in the paper) |
| 5 | Firecracker — open-source microVM project page (AWS) | https://firecracker-microvm.github.io/ | 2026-10-29 | 125 ms — a microVM boots in under 125 ms at under 5 MiB overhead per VM, with up to 150 microVMs created per second per host | vendor claim (project's own documentation, not an independent benchmark) |
| 6 | Daytona — sandboxes documentation | https://www.daytona.io/docs/ | 2026-10-29 | 90 ms — sandboxes spin up in under 90 ms from code to execution | vendor claim (list price/feature page) |
| 7 | E2B — pricing page (sandbox cloud) | https://e2b.dev/pricing | 2026-10-29 | $500/mo — a Pro+ concurrency add-on is $500/mo for 600 concurrent sandboxes, on top of usage charged per second of a running sandbox (Pro++ is $1,000/mo for 1,100) | vendor claim (list price, read 2026-10-29) |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| What one sandbox boundary costs per action: substrate choice and warmth, priced from boot time and trajectory length | 9 | 9 | 8 | 9 | 8.8 | **winner** |
| Idempotency keys and dedupe windows for an agent's external writes | 8 | 9 | 6 | 9 | 7.9 | dropped — adjacent to the 2026-10-12 timeout/retry artifact (both decide how a call is retried); every fetchable anchor states one figure (Stripe's 24-hour key retention), so the evidence row count would be one number repeated |
| Where to place durable-execution checkpoints in a multi-step run | 8 | 9 | 7 | 8 | 8.0 | dropped — the beat is recovery, which `2026-10-28_your-90-restart-monitor-proves-nothing` (this vertical) and the resilience vertical's checkpoint corpus already own; this run's subject is the boundary's cost, not its replay |
| RAM and latency cost per million vectors in an HNSW memory tier | 7 | 8 | 7 | 8 | 7.4 | dropped — sits inside the tiering decision already argued by `2026-10-08_agentic_ai_evergreen_brief.md` and the retrieval funnel of 2026-10-22; a third pass over vector-store sizing is a re-argued thesis |

## Rulings and notes

- **The 110x figure is a vendor-authored measurement, and the article must say so.** All six authors of
  arXiv 2607.01415v1 are affiliated with Daytona, whose hosted sandbox the paper finds fastest, and the
  cheapest of the four substrates it measures is the one it sells. The number that survives that caveat is
  the shape, not the ranking: cold-start spread is largest on the shortest trajectories (T0) and compresses
  to about 1.9x by T2, and fixed startup costs are amortised as action counts rise. Write the caveat in the
  same paragraph as the figure, and never as a claim that Daytona won a fair race.
- **Rows 3 and 4 are one paper on one host.** The host floor is met by Firecracker, Daytona and E2B; two
  rows from `arxiv.org` count as one source class, which is why the brief carries five distinct documents.
- **Row 4's lead figure is 278, not 4,167.** A comma-grouped `4,167` tokenises to `4` and `167` and the
  matcher returns a window on the table of contents; the same table's `278` evidences on the Table 1
  sentence, which itself prints `4,167`. Carry the 4,167 in prose under that row, not as a second cell.
- **Row 6 and row 5 are both vendor numbers and neither is a benchmark.** Firecracker's `<125 ms` is the
  design target published by the project (and the gate reads it as `125`, which lands on the "Speed by
  Design" block); Daytona's `<90 ms` is a marketing line. Neither may be presented as an independent
  measurement of the reader's workload, and the article says what each is.
- **The article's own arithmetic, which no source supplies:** per-action boot tax = S / N. With S = 90 ms
  and a six-action trajectory the tax is 15 ms per action, about 7% of a 200 ms tool turn; with S = 1 s it
  is 167 ms, most of the turn. That rule is the reason this is durable, and it must be computed from the
  cited figures and re-checked after the frontier pass — a derived ratio is the class of claim no gate reads.
- **No hands-on claim.** The desk ran no sandbox and no benchmark; it read two papers, a project page, a
  vendor doc and a price list.
- **Section plan (figure ownership, from `article_shape`'s two-section rule):** put the boot-cost ladder
  (125 ms / 90 ms / the 110x spread) in a small table inside the lead; keep the single derived S/N
  break-even in `By the numbers`; write `At a glance` figure-free.

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=7 fetched=7 sources=5 hosts=4 decision="sha1:fa01a0c0f6" dedup="matched a prior artifact: 2026-10-26_agentic_ai_evergreen_br" window_days=180 checked_at=2026-10-29T17:34:39+00:00 -->
<!-- evergreen-gate:end -->
