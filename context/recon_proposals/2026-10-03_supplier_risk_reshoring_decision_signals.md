# Signals: supplier_risk_reshoring_decision — 2026-10-03

**Window:** 2026-09-03 → 2026-10-03
**Vertical:** supplier_risk_reshoring_decision (Supplier Risk Management & Reshoring/Nearshoring Decision Engines)
**Queries run:** 1 (Supply Chain Intel MCP `--recent 30 --limit 60`; 60 docs) + 10 web fan-outs (reshoring/nearshoring news, US-China tariff relief, Kearney index, Mexico nearshoring, Section 301 status, maritime cyber, landed-cost/dual-sourcing, US Steel/Pirelli investments).

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | US-China deal cuts tariffs on $60B of "non-sensitive" goods | https://www.supplychaindive.com/news/us-china-trade-board-carves-path-for-tariff-relief-on-60b-of-goods/831479 | 2026-09-28 | ~$60B combined bilateral trade ($30B each way); household goods, toys, holiday decorations; USTR Greer "market access for about 30% of US exports to China"; no reduction amounts or implementation date | Tariff regime / reshoring economics | 88 |
| 2 | US Steel breaks ground on $475M Fairfield Q&T tubular line | https://www.ussteel.com/media/newsroom-details | 2026-09-21 | $475M quench-and-tempering facility at Fairfield Tubular Operations (Alabama); ~250 permanent jobs + ~600 construction; oil & gas tubular market | Reshoring / domestic strategic capacity | 76 |
| 3 | Pirelli to build $1.2B tire plant in Rome, Georgia | https://www.manufacturingdive.com/news/amazon-us-steel-pirelli-eli-lilly-investments-layoffs-september-2026/831373 | 2026-09-22 | $1.2B new US tire manufacturing plant serving the US market | Reshoring / domestic manufacturing | 70 |
| 4 | IndustrialSage tracker: $2.084T announced US manufacturing investment | https://www.industrialsage.com/us-manufacturing-investment-tracker | 2026-09-28 | $2.084T announced private-sector US manufacturing commitments across 251 companies / 43 states (as of Sept 28); ~90% of reshoring jobs in high/medium-high tech (electronics, EV batteries, solar, transportation) | Reshoring / investment concentration | 74 |
| 5 | FBI + Coast Guard board two oil tankers over suspected cyberattacks | https://www.reuters.com/world/two-us-bound-vessels-apparently-compromised-by-hackers-us-officials-say-2026-09-17 | 2026-09-17 | Two foreign-flagged US-bound tankers (incl. VL Prosperity, 333m supertanker) boarded Aug 21/24 after networks compromised by "foreign cyber actors" (Iran-linked per reports) | Supplier risk / maritime cyber | 68 |
| 6 | Forced-labor + excess-capacity Section 301 tariffs to stack | https://www.nortonrosefulbright.com/en-us/knowledge/publications/bb2e6618/ustr-formally-implements-forced-labor-tariffs | 2026-09-18 | 10–12.5% forced-labor tariffs (60 economies) effective Jul 24; additional Section 301 tariffs on 16 economies' "excess capacity" expected "in the coming weeks" and "very well may stack" | Tariff regime / input-cost stacking | 64 |
| 7 | SMB supply chains squeezed by pressures beyond tariffs | https://www.supplychaindive.com/news/beyond-tariffs-a-storm-of-pressures-is-hampering-smb-supply-chains/831880 | 2026-10-01 | SMB supply chains facing a "storm of pressures" beyond tariffs (no hard figure disclosed) | Supplier risk / SMB | 62 |

**Primary-source upgrade notes (used during fact-check):**
- #1 primary = USTR Greer statement (Sept 28) via Supply Chain Dive (https://www.supplychaindive.com/news/us-china-trade-board-carves-path-for-tariff-relief-on-60b-of-goods/831479) / Logistics Management (https://www.logisticsmgmt.com/article/u.s_china_advance_trade_talks_with_60_billion_in_potential_tariff_relief_for_non_sensitive_goods — source of the "$30B each way" split, the 10M-ton coal commitment, and the China-side product list) / CNN; corroborating = ASI Central (30% figure), CNN ("from coal to toys").
- #2 primary = US Steel press release (Sept 15/16/21, Fairfield Q&T groundbreaking).
- #3 primary = Pirelli / Manufacturing Dive (Sept 22).
- #4 primary = IndustrialSage US Manufacturing Investment Tracker (Sept 28, $2.084T / 251 companies / 43 states).
- #5 primary = Reuters (Sept 17) + Bloomberg (Sept 15) + CBS (Sept 16).
- #6 primary = Norton Rose Fulbright client note (Sept 18) on USTR Section 301 forced-labor + excess-capacity dockets.
- **De-dup flags:**
  - #1 shares its load-bearing EVENT with the 10-01 `supply_chain` winner `goods-tariff-relief-vs-vessel-fee` (US-China $30B-each-way relief). The EVENT is not fresh (5 days, cross-vertical); only a DIFFERENT thesis (reshoring bifurcation, not vessel-fee offset) can clear Novelty. Flag: cross-vertical event reuse.
  - Reshoring-volume signals (#2/#3/#4) sit in the same family as the 09-10 `supply_chain` `reshoring-capacity-gap` winner (Kearney + Reshoring Initiative) — cap standalone Novelty ≤ 6.0; they are usable only as the "where capital is flowing" leg of a synthesis, not as a single-signal.
  - #5 (tanker cyber) is a maritime-security story; off the reshoring axis (weak persona fit for `ops_leader` sourcing decisions).
  - Prior-run thesis de-dup (§3.5): the 09-26 first run for THIS vertical won `reshoring-moved-the-tariff-upstream` (Coca-Cola $10B ⨂ plastics Section 338). Its thesis — "the tariff relocates upstream into inputs" — is a *vertical* migration; a new thesis must be a *horizontal* one (sensitive vs non-sensitive split) to clear as fresh.

## Candidate Synthesis Pairs


<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=7 candidates=7 heuristic=0.60-0.87 window=2026-09-03..2026-10-03 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

| Pair | Signals | Shared axis | Contrasting axis | Anchor URLs | Heuristic | Flags |
|---|---|---|---|---|---|---|
| 1 | #3 ⨂ #6 | freight_chokepoint_x_nearshoring | A: Reshoring / domestic manufacturing | B: Tariff regime / input-cost stacking | https://www.manufacturingdive.com/news/amazon-us-steel-pirelli-eli-lilly-investments-layoffs-september-2026/831373 https://www.nortonrosefulbright.com/en-us/knowledge/publications/bb2e6618/ustr-formally-implements-forced-labor-tariffs | 0.87 | - |
| 2 | #1 ⨂ #3 | freight_chokepoint_x_nearshoring | A: Tariff regime / reshoring economics | B: Reshoring / domestic manufacturing | https://www.supplychaindive.com/news/us-china-trade-board-carves-path-for-tariff-relief-on-60b-of-goods/831479 https://www.manufacturingdive.com/news/amazon-us-steel-pirelli-eli-lilly-investments-layoffs-september-2026/831373 | 0.86 | - |
| 3 | #1 ⨂ #2 | freight_chokepoint_x_nearshoring | A: Tariff regime / reshoring economics | B: Reshoring / domestic strategic capacity | https://www.supplychaindive.com/news/us-china-trade-board-carves-path-for-tariff-relief-on-60b-of-goods/831479 https://www.ussteel.com/media/newsroom-details | 0.65 | - |
| 4 | #2 ⨂ #6 | freight_chokepoint_x_nearshoring | A: Reshoring / domestic strategic capacity | B: Tariff regime / input-cost stacking | https://www.ussteel.com/media/newsroom-details https://www.nortonrosefulbright.com/en-us/knowledge/publications/bb2e6618/ustr-formally-implements-forced-labor-tariffs | 0.65 | - |
| 5 | #4 ⨂ #6 | freight_chokepoint_x_nearshoring | A: Reshoring / investment concentration | B: Tariff regime / input-cost stacking | https://www.industrialsage.com/us-manufacturing-investment-tracker https://www.nortonrosefulbright.com/en-us/knowledge/publications/bb2e6618/ustr-formally-implements-forced-labor-tariffs | 0.65 | - |
| 6 | #1 ⨂ #4 | freight_chokepoint_x_nearshoring | A: Tariff regime / reshoring economics | B: Reshoring / investment concentration | https://www.supplychaindive.com/news/us-china-trade-board-carves-path-for-tariff-relief-on-60b-of-goods/831479 https://www.industrialsage.com/us-manufacturing-investment-tracker | 0.64 | - |
| 7 | #1 ⨂ #6 | freight_chokepoint_x_nearshoring | A: Tariff regime / reshoring economics | B: Tariff regime / input-cost stacking | https://www.supplychaindive.com/news/us-china-trade-board-carves-path-for-tariff-relief-on-60b-of-goods/831479 https://www.nortonrosefulbright.com/en-us/knowledge/publications/bb2e6618/ustr-formally-implements-forced-labor-tariffs | 0.6 | prior_cycle_token_overlap:tariffs |

**Heuristic terms (advisory):**
- #1: token_coverage=1.0 intensity=0.67 angle_fit=0.75 contrast=1.0 → 0.87 (freight_chokepoint_x_nearshoring)
- #2: token_coverage=1.0 intensity=0.79 angle_fit=0.75 contrast=0.83 → 0.86 (freight_chokepoint_x_nearshoring)
- #3: token_coverage=0.5 intensity=0.82 angle_fit=0.5 contrast=0.86 → 0.65 (freight_chokepoint_x_nearshoring)
- #4: token_coverage=0.5 intensity=0.7 angle_fit=0.5 contrast=1.0 → 0.65 (freight_chokepoint_x_nearshoring)
- #5: token_coverage=0.5 intensity=0.69 angle_fit=0.5 contrast=1.0 → 0.65 (freight_chokepoint_x_nearshoring)
- #6: token_coverage=0.5 intensity=0.81 angle_fit=0.5 contrast=0.83 → 0.64 (freight_chokepoint_x_nearshoring)
- #7: token_coverage=0.5 intensity=0.76 angle_fit=0.5 contrast=0.67 → 0.6 (freight_chokepoint_x_nearshoring)
<!-- synthesis-seed:end -->
