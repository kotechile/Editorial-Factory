# Signals: supplier_risk_reshoring_decision — 2026-09-26

**Window:** 2026-08-27 → 2026-09-26
**Vertical:** supplier_risk_reshoring_decision (Supplier Risk Management & Reshoring/Nearshoring Decision Engines)
**Queries run:** 1 (Supply Chain Intel MCP `--recent 30 --limit 60`; 51 docs) + 6 web fan-outs (Coca-Cola reshoring, plastics/packaging tariffs, Reshoring Initiative survey, Section 122/301 status, near-shoring-Mexico economics, USITC tariff data) + 3 primary-source fetches (Rabobank report PDF, Canada Dept of Finance counter-tariff order, Fortune CFO interview).

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Coca-Cola system commits $10B to US infrastructure (2026–2030) | https://fortune.com/2026/09/15/coca-cola-invest-10-billion-us-growth-through-2030-cfo | 2026-09-15 | $10B system-wide; CFO John Murphy calls it "a growth play, not a tariff hedge"; 98¢ of every dollar already stays in the US economy; $85B 2025 US GDP; ~1M jobs; $37B to US suppliers | Reshoring / domestic production | 88 |
| 2 | Plastics & packaging pulled into tariff turmoil | https://www.supplychaindive.com/news/plastics-get-pulled-into-tariff-turmoil/830768 | 2026-09-23 | ~$3.1B of ~$15B US–Canada plastics trade exposed; ~53–55% all-in duty (Section 338 stacks on base, overrides USMCA); "tariff whiplash is the baseline" (Rabobank, Aug 2026) | Input-cost / packaging tariff risk | 84 |
| 3 | Reshoring Initiative 2026 USA Reshoring Survey | https://reshorenow.org/August-30-2026 | 2026-08-31 | 36% of OEMs reshored or actively engaged (up from 29%); 63% of OEMs planning US capex for reshoring; 249 manufacturers surveyed | Reshoring survey | 78 |
| 4 | Penn Wharton: effective US tariff rate 6.7% | https://budgetmodel.wharton.upenn.edu/p/2026-09-09-effective-tariff-rates-and-revenues-updated-september-9-2026 | 2026-09-09 | Effective tariff rate 6.7% as of July 2026 (post-SCOTUS decline), per updated USITC data | Tariff regime / sourcing cost | 72 |
| 5 | Tariff lawyer: CFOs told to "go back to basics" | https://www.supplychaindive.com/news/want-a-smart-tariff-strategy-lawyer-tells-cfos-to-go-back-to-basics/831204 | 2026-09-24 | Trade counsel urging landed-cost re-baselining + HTS-code hygiene over headline-chasing | Tariff strategy / landed cost | 68 |
| 6 | Lego spends $400M on Mexico warehouse + packing | https://www.supplychaindive.com/news/lego-to-spend-400m-to-add-warehouse-space-at-mexico-plant/831302 | 2026-09-25 | $400M capex for warehouse + packing at Mexico plant | Nearshoring / regionalization | 70 |
| 7 | Electronics makers fret over extreme-heat supplier disruptions | https://www.supplychaindive.com/news/electronics-manufacturers-fret-over-extreme-heat-disruptions/830938 | 2026-09-22 | Climate-driven supplier-performance risk in electronics supply chains | Supplier risk / climate | 66 |
| 8 | CBP to expand IEEPA tariff processing in October | https://www.supplychaindive.com/news/cbp-to-expand-ieepa-tariff-processing-in-october/830618 | 2026-09-17 | Duty-reimbursement processing expansion (no figure disclosed) | Tariff processing | 66 |

**Primary-source upgrade notes (used during fact-check):**
- #1 primary = Coca-Cola/Fortune CFO interview (Sept 15); corroborating = Food Dive (Sept 15), Supply Chain Digital (Sept 23).
- #2 primary = Rabobank "Unwrapped: Plastic packaging matters" (Aug 2026) — https://media.rabobank.com/asset/d0da754d-5253-48d8-a4c9-1ff0045fae48/Unwrapped-Plastic-packaging-matters-August-2026.pdf ; underlying tariff action = White House Section 338 proclamation (July 20, 2026; ~$20B Canadian goods, effective Aug 22); Canada counter-tariff order — https://www.canada.ca/en/department-finance/news/2026/08/list-of-products-from-the-united-states-subject-to-counter-tariffs-effective-september-8-2026.html
- #3 retread flag: re-argues the 2026-09-10 `supply_chain` winner `reshoring-capacity-gap` (Reshoring Initiative survey / Kearney index). Cap standalone Novelty ≤ 6.0 for this vertical.
- #6 retread flag: nearshoring/regionalization re-argues the same 09-10 reshoring thesis family. Cap Novelty ≤ 6.0.
- #2 freshness note: the Section 338 order itself is July 20 (out of window); the *signal* here is the Sept 23 packaging-industry fallout plus the Aug 2026 Rabobank quantification — both the exposure figure (~$3.1B / ~15B) and the "tariff whiplash is the baseline" frame are fresh analysis, not a re-litigated July event.

## Candidate Synthesis Pairs


<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=8 candidates=11 heuristic=0.63-0.81 window=2026-08-27..2026-09-26 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

| Pair | Signals | Shared axis | Contrasting axis | Anchor URLs | Heuristic | Flags |
|---|---|---|---|---|---|---|
| 1 | #1 ⨂ #6 | freight_chokepoint_x_nearshoring | A: Reshoring / domestic production | B: Nearshoring / regionalization | https://fortune.com/2026/09/15/coca-cola-invest-10-billion-us-growth-through-2030-cfo https://www.supplychaindive.com/news/lego-to-spend-400m-to-add-warehouse-space-at-mexico-plant/831302 | 0.81 | - |
| 2 | #4 ⨂ #6 | freight_chokepoint_x_nearshoring | A: Tariff regime / sourcing cost | B: Nearshoring / regionalization | https://budgetmodel.wharton.upenn.edu/p/2026-09-09-effective-tariff-rates-and-revenues-updated-september-9-2026 https://www.supplychaindive.com/news/lego-to-spend-400m-to-add-warehouse-space-at-mexico-plant/831302 | 0.74 | - |
| 3 | #1 ⨂ #5 | freight_chokepoint_x_nearshoring | A: Reshoring / domestic production | B: Tariff strategy / landed cost | https://fortune.com/2026/09/15/coca-cola-invest-10-billion-us-growth-through-2030-cfo https://www.supplychaindive.com/news/want-a-smart-tariff-strategy-lawyer-tells-cfos-to-go-back-to-basics/831204 | 0.72 | - |
| 4 | #3 ⨂ #5 | freight_chokepoint_x_nearshoring | A: Reshoring survey | B: Tariff strategy / landed cost | https://reshorenow.org/August-30-2026 https://www.supplychaindive.com/news/want-a-smart-tariff-strategy-lawyer-tells-cfos-to-go-back-to-basics/831204 | 0.71 | - |
| 5 | #1 ⨂ #2 | freight_chokepoint_x_nearshoring | A: Reshoring / domestic production | B: Input-cost / packaging tariff risk | https://fortune.com/2026/09/15/coca-cola-invest-10-billion-us-growth-through-2030-cfo https://www.supplychaindive.com/news/plastics-get-pulled-into-tariff-turmoil/830768 | 0.69 | - |
| 6 | #1 ⨂ #4 | freight_chokepoint_x_nearshoring | A: Reshoring / domestic production | B: Tariff regime / sourcing cost | https://fortune.com/2026/09/15/coca-cola-invest-10-billion-us-growth-through-2030-cfo https://budgetmodel.wharton.upenn.edu/p/2026-09-09-effective-tariff-rates-and-revenues-updated-september-9-2026 | 0.68 | - |
| 7 | #2 ⨂ #3 | freight_chokepoint_x_nearshoring | A: Input-cost / packaging tariff risk | B: Reshoring survey | https://www.supplychaindive.com/news/plastics-get-pulled-into-tariff-turmoil/830768 https://reshorenow.org/August-30-2026 | 0.68 | - |
| 8 | #1 ⨂ #8 | freight_chokepoint_x_nearshoring | A: Reshoring / domestic production | B: Tariff processing | https://fortune.com/2026/09/15/coca-cola-invest-10-billion-us-growth-through-2030-cfo https://www.supplychaindive.com/news/cbp-to-expand-ieepa-tariff-processing-in-october/830618 | 0.67 | - |
| 9 | #3 ⨂ #4 | freight_chokepoint_x_nearshoring | A: Reshoring survey | B: Tariff regime / sourcing cost | https://reshorenow.org/August-30-2026 https://budgetmodel.wharton.upenn.edu/p/2026-09-09-effective-tariff-rates-and-revenues-updated-september-9-2026 | 0.66 | - |
| 10 | #3 ⨂ #8 | freight_chokepoint_x_nearshoring | A: Reshoring survey | B: Tariff processing | https://reshorenow.org/August-30-2026 https://www.supplychaindive.com/news/cbp-to-expand-ieepa-tariff-processing-in-october/830618 | 0.66 | - |
| 11 | #1 ⨂ #3 | freight_chokepoint_x_nearshoring | A: Reshoring / domestic production | B: Reshoring survey | https://fortune.com/2026/09/15/coca-cola-invest-10-billion-us-growth-through-2030-cfo https://reshorenow.org/August-30-2026 | 0.63 | - |

**Heuristic terms (advisory):**
- #1: token_coverage=0.75 intensity=0.79 angle_fit=0.75 contrast=1.0 → 0.81 (freight_chokepoint_x_nearshoring)
- #2: token_coverage=0.75 intensity=0.71 angle_fit=0.5 contrast=1.0 → 0.74 (freight_chokepoint_x_nearshoring)
- #3: token_coverage=0.5 intensity=0.78 angle_fit=0.75 contrast=1.0 → 0.72 (freight_chokepoint_x_nearshoring)
- #4: token_coverage=0.5 intensity=0.73 angle_fit=0.75 contrast=1.0 → 0.71 (freight_chokepoint_x_nearshoring)
- #5: token_coverage=0.5 intensity=0.86 angle_fit=0.5 contrast=1.0 → 0.69 (freight_chokepoint_x_nearshoring)
- #6: token_coverage=0.5 intensity=0.8 angle_fit=0.5 contrast=1.0 → 0.68 (freight_chokepoint_x_nearshoring)
- #7: token_coverage=0.5 intensity=0.81 angle_fit=0.5 contrast=1.0 → 0.68 (freight_chokepoint_x_nearshoring)
- #8: token_coverage=0.5 intensity=0.77 angle_fit=0.5 contrast=1.0 → 0.67 (freight_chokepoint_x_nearshoring)
- #9: token_coverage=0.5 intensity=0.75 angle_fit=0.5 contrast=1.0 → 0.66 (freight_chokepoint_x_nearshoring)
- #10: token_coverage=0.5 intensity=0.72 angle_fit=0.5 contrast=1.0 → 0.66 (freight_chokepoint_x_nearshoring)
- #11: token_coverage=0.5 intensity=0.83 angle_fit=0.5 contrast=0.75 → 0.63 (freight_chokepoint_x_nearshoring)
<!-- synthesis-seed:end -->

