# Signals: supply_chain — 2026-10-01

**Window:** 2026-09-01 → 2026-10-01
**Queries run:** 1 (Supply Chain Intel MCP `--recent 30 --limit 100`; 69 documents, 53 newsroom / 16 podcast) + verification web searches / primary-source fetches (USTR Greer statement, White House 30-for-30 release, CBP Section 301 vessel-fee bulletin, NFTC joint association letter, FedEx surcharge table).
**Source:** Coolify Supply Chain Intelligence server (`intel.giniloh.com`) — healthy (69 docs)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | U.S.-China Board of Trade recommends reduced tariffs on ~$30B of non-sensitive goods each way | https://ustr.gov/about/policy-offices/press-office/press-releases/2026/september/ambassador-greer-issues-statement-announcement-recommendations-us-china-board-trade | 2026-09-27 | Greer: "$30 billion of trade in non-sensitive goods on each side"; "about 30 percent of U.S. exports to China"; household goods, toys, ag, medical devices; no reduction amounts or implementation date given | Tariff relief / landed cost | 84 |
| 2 | Section 301 China-linked vessel fees suspended but pause set to expire Nov 9; trade groups urge extension | https://www.nftc.org/wp-content/uploads/2026/09/Joint-Association-USTR-Letter-Sec-301-Vessel-Fee-Suspension-Extension-Request-Final-092326.pdf | 2026-09-23 | $18/net ton or $120/container (whichever higher) for Chinese-built vessels; $50/net ton for Chinese-operated; suspended Nov 10 2025, expires 11:59pm ET Nov 9 2026; NRF + RILA + AgTC urge extension | Maritime port fees / vessel cost cliff | 82 |
| 3 | FBI, Coast Guard probe suspected cyberattacks on ships entering US waters | https://www.supplychaindive.com/news/fbi-coast-guard-probe-suspected-cyberattacks-on-ships-entering-us-waters/830774/ | 2026-09-21 | Coast Guard/FBI boarded 2 foreign-flagged oil tankers (Aug 21, Aug 24) in Gulf of Mexico en route to Texas after networks "compromised by foreign cyber actors"; no operational disruption | Maritime cybersecurity / port security | 72 |
| 4 | FedEx preps 5.9% GRI plus surcharge increases for 2027 | https://www.supplychaindive.com/news/fedex-preps-59-rate-hike-surcharge-increases-for-2027/830903/ | 2026-09-21 | 5.9% avg rate increase Jan 4 2027; First Overnight 6.01%, 2Day A.M. 6.65%; Ground 1–5 lb e-commerce packages 6.49%; surcharges e.g. additional handling $46→$49.50, $25 paper-document fee | Parcel GRI / surcharge creep | 70 |
| 5 | Old Dominion announces 4.9% general rate increase | https://www.supplychaindive.com/news/old-dominion-announces-49-general-rate-increase/830901/ | 2026-09-23 | 4.9% GRI effective Oct 5 on selected services; LTL bellwether | LTL pricing / freight budget | 62 |
| 6 | Amazon debuts direct rail service LA → East Coast | https://www.supplychaindive.com/news/amazon-debuts-direct-rail-service-for-los-angeles-to-east-coast-shipments/830836/ | 2026-09-23 | "Standard Ocean Express" direct rail, claimed faster cross-country; no transit time, pricing, or reliability disclosed | Intermodal / rail shift | 64 |
| 7 | Maersk broadens US logistics beyond ocean freight (multimodal) | https://www.supplychaindive.com/news/not-just-ocean-how-maersk-grew-its-us-logistics-capabilities/829105/ | 2026-09-30 | 5 capabilities referenced (ocean, ground, e-commerce, contract logistics, air); no quantitative metrics disclosed | Carrier consolidation / control tower | 60 |

**Retread flags (per virality_judge §3.5):**
- #2 (Section 301 vessel fees) is maritime, but a *government tariff instrument* — distinct from the 2026-09-17 winner `samsung-cma-cgm-186m-dnd-dispute` (a commercial carrier demurrage/detention dispute, FMC Docket 26-12). Not a retread; different instrument and policy lever.
- #1 (tariff relief) is a *relief/reduction* signal, distinct from the 2026-09-26 winners `tariff-cliff-already-priced-in` (truce *extension* + refund hoarding) and `reshoring-moved-the-tariff-upstream` (tariff migration to packaging inputs). The relief direction is new; the vessel-fee leg is a never-covered instrument.

**Primary-source upgrade notes (used during fact-check):**
- #1 primary = USTR Greer statement (Sept 27) — https://ustr.gov/about/policy-offices/press-office/press-releases/2026/september/ambassador-greer-issues-statement-announcement-recommendations-us-china-board-trade ; corroborating "30-FOR-30" list + terms of reference — https://www.whitehouse.gov/releases/2026/09/u-s-china-board-of-trade/
- #2 primary (fee structure) = CBP Trade Information Notice TIN# 66448963 — https://content.govdelivery.com/accounts/USDHSCBP/bulletins/3f5ee43 ; primary (suspension expiry + signatories) = NFTC joint association letter (Sept 23) — https://www.nftc.org/wp-content/uploads/2026/09/Joint-Association-USTR-Letter-Sec-301-Vessel-Fee-Suspension-Extension-Request-Final-092326.pdf

## Candidate Synthesis Pairs


<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=7 candidates=2 heuristic=0.53-0.57 window=2026-09-01..2026-10-01 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

| Pair | Signals | Shared axis | Contrasting axis | Anchor URLs | Heuristic | Flags |
|---|---|---|---|---|---|---|
| 1 | #1 ⨂ #3 | freight_chokepoint_x_nearshoring | A: Tariff relief / landed cost | B: Maritime cybersecurity / port security | https://ustr.gov/about/policy-offices/press-office/press-releases/2026/september/ambassador-greer-issues-statement-announcement-recommendations-us-china-board-trade https://www.supplychaindive.com/news/fbi-coast-guard-probe-suspected-cyberattacks-on-ships-entering-us-waters/830774/ | 0.57 | - |
| 2 | #2 ⨂ #3 | freight_chokepoint_x_nearshoring | A: Maritime port fees / vessel cost cliff | B: Maritime cybersecurity / port security | https://www.nftc.org/wp-content/uploads/2026/09/Joint-Association-USTR-Letter-Sec-301-Vessel-Fee-Suspension-Extension-Request-Final-092326.pdf https://www.supplychaindive.com/news/fbi-coast-guard-probe-suspected-cyberattacks-on-ships-entering-us-waters/830774/ | 0.53 | - |

**Heuristic terms (advisory):**
- #1: token_coverage=0.5 intensity=0.78 angle_fit=0.0 contrast=1.0 → 0.57 (freight_chokepoint_x_nearshoring)
- #2: token_coverage=0.5 intensity=0.77 angle_fit=0.0 contrast=0.8 → 0.53 (freight_chokepoint_x_nearshoring)
<!-- synthesis-seed:end -->

