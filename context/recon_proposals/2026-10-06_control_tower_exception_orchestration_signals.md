# Signals: control_tower_exception_orchestration — 2026-10-06
**Vertical:** control_tower_exception_orchestration (Control Tower Visibility & Real-Time Exception Orchestration)
**Window:** 2026-09-06 → 2026-10-06
**Queries run:** 18 (web fan-out on the vertical's sources + Supply Chain Intel MCP `--recent 30`)
**Persona:** supply_chain_architect

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Tive 2026 research: Cargo Theft Prevention in the Age of AI | https://www.tive.com/press-release/tive-research-45-of-companies-using-active-monitoring-recover-more-than-half-of-stolen-cargo-1-5x-the-rate-of-those-relying-on-passive-monitoring | 2026-09-29 | Survey of 442 supply chain leaders: 45% of orgs on active in-transit monitoring recover more than half of stolen cargo vs 30% on passive (1.5x); route-deviation alerts 53% vs 29% (1.8x); 55% who identified their latest theft's method cited identity-based fraud (fictitious pickup, synthetic/AI-generated identities); 84% would trust AI to run at least one cargo-security function autonomously and 3 in 10 would let it place a shipment on hold or escalate to law enforcement | Real-time exception orchestration: which cargo-security signals actually change recovery outcomes, and where identity fraud defeats them | 90 |
| 2 | SCMR: From forecast to action — how agentic AI is rewiring supply chain exception management | https://www.scmr.com/article/agentic-ai-supply-chain-exception-management | 2026-09-30 | The insight-to-action handoff is the bottleneck: an alert has limited value if the exception then waits in a queue; routine, high-volume, clear-rule cases with measurable cost of delay are candidates for bounded agent action, while consequential decisions should require approval and an audit trail | Autonomy architecture: tiering agent authority by risk, and what oversight an exception-orchestration agent needs | 78 |
| 3 | Supply Chain Dive: CH Robinson to buy RXO for $5.8B | https://www.supplychaindive.com/news/ch-robinson-to-buy-rxo-for-58b-combining-3pl-heavyweights/832124/ | 2026-10-05 | C.H. Robinson agreed to acquire RXO for $5.8 billion, subject to approval, combining two large 3PL/brokerage networks | Control-tower data dependency: the carrier network and the exception data layer consolidating into the same vendor | 85 |
| 4 | Supply Chain Dive: USPS lengthens some delivery expectations outside contiguous US | https://www.supplychaindive.com/news/usps-lengthens-some-delivery-expectations-outside-contiguous-us/831958/ | 2026-10-05 | USPS lengthened delivery expectations for Ground Advantage and Priority Mail to and from Alaska, Hawai'i and other non-contiguous areas | ETA baselines: planned transit windows are set by the carrier, so a control tower's on-time exception logic inherits the carrier's own revision | 72 |
| 5 | Supply Chain Dive: FedEx rolls out added security option for select deliveries | https://www.supplychaindive.com/news/fedex-rolls-out-added-security-option-for-select-deliveries/831596/ | 2026-10-02 | FedEx introduced Authenticated Delivery, a security option for select shipments that requires the recipient to present a one-time code at handoff | Last-mile release control: moving the proof-of-delivery from a signature to a code bound to a named recipient | 68 |
| 6 | Tive: Cargo theft season is gone — it's now a 24/7/365 pursuit | https://www.tive.com/blog/cargo-theft-season-is-gone-its-now-a-24-7-365-pursuit | 2026-10-02 | The seasonal pattern of cargo theft has broken down; high-value freight is now targeted year-round, so a security posture that dials up for holiday peaks leaves the other ten months exposed | Monitoring cadence: 24/7 coverage vs peak-season staffing of the exception desk | 70 |
| 7 | Supply Chain Dive: Ikea freight to be hauled by driverless Kodiak trucks | https://www.supplychaindive.com/news/ikea-freight-to-be-hauled-by-driverless-kodiak-trucks/831764/ | 2026-10-02 | Unsupervised long-haul service between Dallas-Fort Worth and Houston is expected to launch by the end of 2026 | Driverless corridors: who owns the exception when there is no driver to call, and which telemetry the tower must ingest | 66 |
| 8 | Supply Chain Dive: Costco CFO doubles down on tariff strategy | https://www.supplychaindive.com/news/costco-cfo-doubles-down-on-tariff-strategy-winks-at-churro-comeback/832022/ | 2026-10-05 | Costco said it has 'predominantly' used initial IEEPA tariff refunds to lower prices (no dollar amount or percentage disclosed) | Landed-cost exception: tariff refunds landing as cash rather than as exceptions the tower tracks | 62 |

## Candidate Synthesis Pairs


<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=8 candidates=1 heuristic=0.74-0.74 window=2026-09-06..2026-10-06 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

| Pair | Signals | Shared axis | Contrasting axis | Anchor URLs | Heuristic | Flags |
|---|---|---|---|---|---|---|
| 1 | #1 ⨂ #2 | governance_x_runtime | A: Real-time exception orchestration: which cargo-security signals actually change recovery outcomes, and where identity fraud defeats them | B: Autonomy architecture: tiering agent authority by risk, and what oversight an exception-orchestration agent needs | https://www.tive.com/press-release/tive-research-45-of-companies-using-active-monitoring-recover-more-than-half-of-stolen-cargo-1-5x-the-rate-of-those-relying-on-passive-monitoring https://www.scmr.com/article/agentic-ai-supply-chain-exception-management | 0.74 | - |

**Heuristic terms (advisory):**
- #1: token_coverage=0.5 intensity=0.84 angle_fit=0.75 contrast=1.0 → 0.74 (governance_x_runtime)
<!-- synthesis-seed:end -->

