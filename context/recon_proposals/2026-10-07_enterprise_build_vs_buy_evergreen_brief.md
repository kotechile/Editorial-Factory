# Evergreen Brief: enterprise_build_vs_buy — 2026-10-07

**Archetype:** evergreen
**Vertical:** enterprise_build_vs_buy
**Persona:** eng_leader
**Decision the reader is facing:** Whether to treat a critical dependency's uptime SLA as the safety net — trust the vendor and collect the credit when it fails — or to fund a fallback/redundancy layer, and how to size that fallback when the SLA's only remedy is a service credit capped at a percentage of the monthly fee while the downstream outage cost is not capped at all.
**Durability:** Still true in 12 months because the mechanism is contractual, not a version artefact: an SLA's remedy is a credit expressed as a share of the monthly bill (AWS EC2 pays 10% of the month for uptime below 99.99% but at or above 99.0%, 30% below 99.0%, and 100% only below 95.0%; Google Compute pays 10% / 25% / 100% on the same ladder; Vercel commits to 99.99% availability), and 99.99% is a 4.32-minute budget in a 30-day month. The percentages are as of the cited SLA pages (retrieved 2026-10-07), the statutory exit date is fixed (12 January 2027, EU Data Act Article 29), and the rule — a credit is a refund, never a fund for the outage, so price the fallback against the outage — does not expire.
**De-dup:** Nearest prior artifact for this vertical is `2026-10-07_vendor-replacement-ai-ceiling` (`published/2026-10-07_vendor-replacement-ai-ceiling.md`): that piece argues AI assistance thins out at the production boundary, so replacing a vendor moves the operational risk inward rather than removing it, and it rests on the Stack Overflow 2026 survey plus the Retool governance report — it carries no SLA-credit arithmetic. This is also distinct from the desk's cross-vertical `2026-10-06_cloud-repatriation-break-even` (enterprise_tech_leadership — repatriation capex break-even, a16z discount ceilings and Flexera waste; no uptime-credit rule) and from the withdrawn `2026-09-23_enterprise_build_vs_buy_angle_brief` (price-volatility maintenance tax, a news-cycle rule). No re-argument of any of the three.
**Thesis:** A vendor SLA credit is a refund capped at a slice of the monthly bill, never a fund for the outage — so the fallback for a critical dependency is justified by the outage's downstream cost, not by the credit, and the case for buying the enterprise tier is the escalation path (and the now-statutory cheap exit), not insurance.

**Lead:** The vertical's own `primary_angles` (\"api ingestion and third-party service redundancy costs and fallback layers\"), the `eng_leader` persona's wants in `context/personas.json` (\"concrete numbers, decision frameworks, what to do Monday morning\"), founder-voice §3 `enterprise_build_vs_buy` (\"API Ingestion & Redundancy Overhead: building custom resilient retry fabrics ... across 10 third-party APIs incurs continuous engineering overhead. Paying enterprise API tiers with strict SLAs is often cheaper than dedicating an on-call engineer to upstream vendor outages\"), and real field friction in `context/growth_os/customer-truth.md` §enterprise_build_vs_buy Anecdote 3 (a B2B logistics SaaS on a single third-party geocoding API without caching took a 9-hour partial degradation, halted route generation, and paid $85,000 in contract SLA penalties; an async queue plus local Redis geospatial cache and a secondary-provider fallback cost $6,500 to build). The decisive question — does the vendor's SLA actually cover that, or only refund part of the invoice? — is the reader's decision. `scripts/gsc_analyzer.py --vertical enterprise_build_vs_buy` returns thin impressions on a young site, so demand is a bonus signal here, not the driver. The topic is durable, not news: nothing in it expires within 90 days, so it belongs on this track and not in the 30-day radar.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | AWS, *Amazon Compute Service Level Agreement* (EC2 SLA) | https://aws.amazon.com/ec2/sla/ | 2026-10-07 | 10% — the first EC2 region-level service-credit tier: a month below 99.99% (but at or above 99.0%) earns a 10% credit, below 99.0% earns 30%, and a 100% credit needs uptime below 95.0%, against a stated commitment of 99.99% | contractual (vendor SLA) |
| 2 | Google Cloud, *Compute Engine Service Level Agreement* | https://cloud.google.com/compute/sla | 2026-10-07 | 25% — Google's Financial Credit for instances in multiple zones when monthly uptime falls to 95.00%–below 99.00%; it pays 10% for 99.00%–below 99.99% and 100% below 95.00%, and the SLO itself is 99.99% | contractual (vendor SLA) |
| 3 | Vercel, *Service Level Agreement* | https://vercel.com/legal/sla | 2026-10-07 | 99.99% — Vercel's platform availability commitment, with uptime measured in minutes and any Excused Downtime subtracted before the Credit in Section 3 applies | contractual (vendor SLA) |
| 4 | EU, *Regulation (EU) 2023/2854* (Data Act), Article 29 — collated text on EUR-Lex | https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng | 2026-10-07 | 12 January 2027 — from that date providers of data processing services shall not impose any switching charges on the customer for the switching process; only reduced, cost-linked charges are permitted until then | statute (primary law) |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The SLA credit is a refund, not insurance — price the fallback against the outage, and treat the credit as a slice of the invoice | 9 | 9 | 8 | 9 | 8.8 | **winner** |
| The outbound-gigabyte meter decides the repatriation break-even | 9 | 8 | 9 | 7 | 8.4 | dropped — it re-argues a live desk thesis: `2026-10-06_cloud-repatriation-break-even` (enterprise_tech_leadership) already prices the transfer meter against owned gear and cites R2 pricing, and today's survey piece for this vertical already treats vendor cost |
| The 3-year maintenance multiplier on \"free\" internal tools | 9 | 8 | 6 | 8 | 7.8 | dropped — the 3.8× multiplier is a desk field note; no fetchable primary states it, so the load-bearing figure would ship unverifiable |
| Internal-tooling maintenance tax from loaded salary rates | 8 | 7 | 6 | 7 | 7.1 | dropped — the loaded-salary anchor (BLS Occupational Outlook Handbook) returned HTTP 403 and the Hetzner price pages render only via script, so the rule would rest on unfetchable numbers |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=4 fetched=4 sources=4 hosts=4 decision="sha1:c6a7e92140" dedup="matched a prior artifact: 2026-10-07_vendor-replacement-ai-c" window_days=180 checked_at=2026-10-07T19:04:20+00:00 -->
<!-- evergreen-gate:end -->
