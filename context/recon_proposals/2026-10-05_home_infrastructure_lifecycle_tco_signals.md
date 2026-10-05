# Signals: home_infrastructure_lifecycle_tco — 2026-10-05

**Window:** 2026-09-05 → 2026-10-05
**Vertical:** Home Infrastructure & Major Asset Lifecycle TCO
**Queries run:** 14 (home_lifestyle_intel MCP recent-30 + web fan-out: HVAC price increases, DOE water-heater standards, R-410A/A2L refrigerant transition, heat-pump rebate programs, NEM 3.0 solar+battery payback, home water-leak detection, insurance/roof replacement)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | NEADA: heating-oil winter cost to jump ~50% (~$878/household) | https://www.usatoday.com/story/money/personal-finance/2026/10/02/heating-oil-costs-surge-2026/92038345007 | 2026-10-02 | Avg winter heating-oil cost +$878 (~50%) to ~$2,627 (up from $1,749); 4.79M households on heating oil; Maine $2,939; diesel $6.53/gal all-time record | heat-pump switch economics for delivered-fuel homes | 72 |
| 2 | DOE commercial/residential-duty gas water-heater standard effective Oct 6, 2026 | https://www.bradfordwhite.com/doe-landing | 2026-10-06 | Non-condensing commercial gas water heaters (incl. residential-duty models >75,000 BTU/hr used in large homes) can no longer be manufactured/imported after Oct 6; TE 80%→95–96%; civil-penalty enforcement delayed to Oct 6, 2027 | replacement-window regulation (major asset) | 62 |
| 3 | Xcel Colorado heat-pump rebate step-down 3x→2x effective Oct 1 | https://www.zerohomes.com/rebate-programs | 2026-10-01 | Xcel CO heat-pump bonus drops 3x→2x standard rebate Oct 1; cold-climate heat pump $2,250→$1,500 per heating ton (install+invoice by Oct 1, file by Oct 15 to keep higher tier) | rebate window closing on HVAC transition | 60 |
| 4 | Canary Media: "Here's why your energy bills are going up" | https://www.canarymedia.com/articles/affordability/why-energy-bills-are-going-up | 2026-10-05 | $18.6B electric+gas rate-increase requests H1 2026 (record Q2 $9.2B, 56M customers); ~5M households on heating oil face spiked winter costs; 9 states enacted plug-in solar laws | utility rate structure vs. asset payback | 60 |

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=4 candidates=1 heuristic=0.68-0.68 window=2026-09-05..2026-10-05 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

| Pair | Signals | Shared axis | Contrasting axis | Anchor URLs | Heuristic | Flags |
|---|---|---|---|---|---|---|
| 1 | #3 ⨂ #4 | electrification_subsidies_x_utility_rates | A: rebate window closing on HVAC transition | B: utility rate structure vs. asset payback | https://www.zerohomes.com/rebate-programs https://www.canarymedia.com/articles/affordability/why-energy-bills-are-going-up | 0.68 | - |

**Heuristic terms (advisory):**
- #1: token_coverage=0.5 intensity=0.6 angle_fit=0.75 contrast=1.0 → 0.68 (electrification_subsidies_x_utility_rates)
<!-- synthesis-seed:end -->
