# Angle Brief: control_tower_exception_orchestration — 2026-11-17
**Angle Type:** Single-Signal (document analysis, with a measured corroboration)
**Winner:** Your carrier scorecard's own reliability benchmark counted some vessel calls on two trade
lanes at once for eleven years — and the fix moved which alliance looked most reliable, by more than
the margin that had separated the top two.
**Scores:** N=9.0 A=9.5 S=8.5 → Composite=9.0
**Hook:** On 7 November 2026 Sea-Intelligence told its subscribers that its aggregated alliance
schedule-reliability figures had double-counted a subset of vessel arrivals, that the error dated to
the first alliance section in April 2015, and that it had gone unnoticed for eleven years by the
publisher *and* by the alliance carriers receiving the raw data.
**Tension:** The double count never touched a carrier's score or a trade's score — only the alliance
aggregate. That is the layer a shipper cannot rebuild itself and the one it uses to compare Gemini,
MSC, the Ocean Alliance and Premier. The correction consequently flipped the August/September 2026
ranking (previously MSC 68.9% ahead of Gemini 68.4%; corrected Gemini 70.4% ahead of MSC 69.5%), a
1.4-point swing against a published gap of 0.5 points. Meanwhile the live half of the same problem is
worse: a cross-platform FedEx monitor reports that 90% of the 162 carrier-affecting incidents it
recorded were reported by only one of four platforms run by three companies, that 29% of those
incidents had their carrier inferred from a title, and that its own uptime numbers are "as reported by
the platforms, not independently measured". So both the benchmark a tower cites and the feed it
escalates from are counts whose denominators are set by the party being measured.
**Target reader:** supply_chain_architect
**Single claim to defend:** An exception is a count compared against a threshold, and every count in
a control tower is assembled by a counting rule someone chose — so the audit that pays is on the
denominator (one key per call, an observer you do not also employ, a baseline that is stated), not on
the threshold, because the threshold is being tuned against a number that may be wrong by more than
the difference it is trying to detect.
**Runner-ups + why rejected:**
- **Project44 Hormuz Week 34 (transshipment dwell 12–59% above a disclosed pre-conflict baseline;
  Jebel Ali export dwell 26.8 vs 8.5 days) — 7.6.** Fresh, measured, first-party, and the best
  available example of a *disclosed* baseline; it loses as a story because it reports the level of
  congestion rather than anything the reader can change, and this vertical published ocean dwell
  analysis on 2026-10-13 and 2026-11-03. Carried into the winner as the positive example of a stated
  baseline.
- **Shipzil's FedEx cross-platform monitoring as the anchor (162 incidents, 90% single-company, 8x
  spread in recorded incidents, uptime "as reported") — 8.7 as a synthesis leg.** This is the pair
  the Judge tested under §2.5: Emergence 9 (neither the publisher nor the monitor states that the
  benchmark and the feed fail the same way), dual authority 8 (Shipzil is the measurer of its own
  data and discloses its limits, but it is a small vendor, not an independent authority), tension 9
  → 8.7. It does not beat the 9.0 single-signal by the 0.3 precedence margin, so per §2.5 it is
  carried as *corroboration* — the live-feed half of the same failure class — and the artifact
  publishes without the `synthesis: true` flag.
- **The seeder's own answer:** `synthesize_topics.py --seed` returned `rows=7 candidates=0`. Both
  legs are measurements, and the token layer has no archetype for two published counts of two
  different systems; recorded as input, not a verdict.
- **USPS's 2027 rate increase with a permanent fuel surcharge (5.9%, effective 2027-01-17,
  matching FedEx and UPS) — 7.9.** In-window and hard-numbered, but the fuel-surcharge half was
  published by the sibling vertical `supply_chain` on 2026-10-29 (same `aichieve.net` front), which
  makes it a retread under §3.5's sibling rule; and a rate table is pricing, not orchestration.
- **Samsara Agent Studio / 7x agent adoption — 7.4.** Dated 2026-10-13, five days before the window
  opened: an anchor-freshness failure, dropped at Stage 1. Same verdict for Descartes' OpsForce
  (2026-03-04 announcement; its FreightWaves write-up is 2026-01-30), which is a shame, because the
  vendor's own admission that geofenced arrivals "always triggered human follow-up" and that its
  agent "removes false exceptions" would otherwise be the cleanest statement of the false-positive
  half.
- **FourKites leaving the Gartner RTTVP Magic Quadrant — dropped.** A past-week search hit, but the
  announcement is 2025-02-24.

## De-dup (§3.5)

- **Within vertical, prior 30 days:** 2026-11-03 `your-cold-chain-blind-spot` (reefer excursion
  window), 2026-11-03 `your-9-day-notice-9-day-queue` (LA/LB rail backlog against notice windows),
  2026-11-10 `your-15-day-entry-gap` (customs deadlines the tower does not own), 2026-10-27
  `your-miss-costs-9x-the-chargeback` and `your-eta-misses-27-hours`, 2026-10-20 `your-3-0-0-feed-stuck-until-2027`
  and `your-exception-log-owes-5-years`, 2026-10-19 `your-30-exception-bill-is-wrong`. None argues
  that a benchmark or an exception count is mis-assembled.
- **Same-source caution:** the 2026-10-13 article `49.9% On Time: Shippers Stuck in the Gap` cited
  Sea-Intelligence (press release 410) for the *level* of reliability against rail dwell. It is 35
  days old (outside the prior-30-day window) and its thesis is the handoff between ship and train;
  this piece is about how the number is assembled, and it deliberately does not rest on the level of
  reliability at all — the 50.6% September figure appears once, as context, not as the argument.
- **Sibling verticals on `aichieve.net`, last 7 days:** `ai_observability_qa` (2026-11-17, warning vs
  deny path in agent tool calls), `nhil_infrastructure_ops` (2026-11-17, probe-to-service binding),
  `enterprise_tech_leadership` (2026-11-17, approval gates and AI spend), `workstation_compute_economics`
  (2026-11-17, local box memory/speed). All software-operations beats; none touches carrier
  reliability, platform incident counts or a data publisher's correction. Note the adjacent theme
  (nhil's "a check can certify a path the traffic has left") is about *what is measured*, whereas
  this piece is about *how the count is built* — different mechanism, different evidence.
- **Desk-wide figure rule:** `grep -ril "sea-intelligence\|schedule reliability" published/` returns
  the two artifacts named above; the 68.9/68.4/70.4/69.5 figures and the 461-call count appear
  nowhere in `published/`, `context/drafts/` or `context/recon_proposals/` outside this run's files.
