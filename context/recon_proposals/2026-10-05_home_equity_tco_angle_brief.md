# Angle Brief: home_equity_tco — 2026-10-05

**Verdict: no publish** (weak cycle; virality gate — second run, window advanced only ~2 days)

## Prior-cycle thesis de-dup (§3.5)

The 10-03 first run for this vertical already won the window's sharpest acute story and published
`heloc-at-8-vs-battery-that-earns` (8.5, Synthesis). Its load-bearing primaries are still in-window
and were consumed by that run:
- HELOC 8.194% / 10-yr 8.164% / 15-yr 8.503% (Fortune/MRC, Oct 2) + 30-yr fixed 7.30%, refi −9% WoW (MND, Oct 2)
- SB 913 + SB 905 VPP battery compensation signed Sept 30 (CALSSA)
- FHFA +2.6% / Case-Shiller +1.9% below ~3.4% inflation (Oct 2)

Cross-vertical, the two natural second legs for any fresh heat-pump/energy-cost story are also consumed:
- the **diesel $6.53/gal all-time record** → 10-02 `last_mile_routing_fleet_carbon` (same-day-race-undoes-route-optimization)
- the **RMI Maryland heat-pump savings ($1,200–$1,600/yr)** → 10-03 `home_infrastructure_lifecycle_tco` (heat-pumps-cheaper-to-run-pricier-to-buy)

## Fresh signals swept this run (Oct 3–5 window advance)

| # | Signal | N | A | S | Composite | Why it fails |
|---|--------|---|---|---|-----------|--------------|
| 1 | NEADA heating-oil winter forecast: +$878 (~50%) to $2,627 (Oct 2) | 7.5 | 8.0 | 7.0 | **7.5** | fuel-price shock, not a structural TCO thesis; diesel-record leg already consumed cross-vertical; forecast, not realized price |
| 2 | Canary "why your energy bills are going up" (Oct 5) | 6.0 | 6.0 | 7.0 | **6.3** | aggregator; load-bearing $18.6B rate-request figure is July 14 PowerLines data (out of window) |
| 3 | WarrantyWeek deferred-maintenance/warranty risk (Sept 29) | 6.0 | 6.0 | 6.5 | **6.2** | aggregator citing Pearl/HIRI/JCHS/HomeServe — vendor marketing + mixed 2024–2026 sources, no acute 30-day anchor |
| 4 | Xcel CO heat-pump rebate step-down 3x→2x (Oct 1) | 6.5 | 6.0 | 6.0 | **6.2** | single utility, regional; modest rebate reduction, weak pro_homeowner reach |
| 5 | CA building-code approval delays / AB 130 moratorium (Oct 5) | 6.5 | 7.0 | 5.5 | **6.4** | regional policy, weak home-capital-TCO fit; more a builder/permitting story |

## Synthesis candidates — all below the gate

- **#1 ⨂ 8% HELOC (10-03 anchor):** "the $2,627 oil bill is the new case for financing a heat pump at 8%." E=8.0, A=8.0, S=7.5 → **7.8**. Below 8.0, and reuses the 10-03 run's own HELOC anchor — dilutes novelty, and the fuel-switch leg (heat-pump savings) is itself cross-consumed by the 10-03 RMI-Maryland run.
- **#1 ⨂ #4 (oil shock ⨂ rebate step-down):** same heating-cost axis, no emergent tension → ~7.0.
- **#4 ⨂ #2 (rebate shrinking ⨂ utility rates rising):** mechanically unscoped (seeder found no pair); as a manual pairing it is a coherent but weak collision (regional rebate ⨂ aggregator) → ~6.5.

## Mechanical seed note

`scripts/synthesize_topics.py --seed` reported "no valid pair" (rows=5 candidates=0) — the two
archetypes scoped to this vertical (`electrification_subsidies_x_utility_rates`,
`insurance_withdrawal_x_asset_resilience`) do not touch the heating-oil/deferred-maintenance token set,
and the one quasi-match (rebate ⨂ utility-rate) fails because the angle text carries "time of use"
(space) where the token is "time-of-use" (hyphenated). Same pattern as the 09-26/10-01/10-02/10-03
synthesis runs: the pairs the token layer misses are the ones the Judge must look for — and here the
Judge finds none that clears ≥ 8.

## Failure class

Already covered by `virality_judge.md` §3.5 (re-run cadence caveat — window barely advanced) and
`radar_30day.md` §4 (anchor-driven vertical). No new patch; logged to `self_improvement_eval.md`.

## Watch-items (most likely next ≥8 primary)

- EIA Winter Fuels Outlook (~Oct 2026) — the authoritative cross-fuel heating-cost forecast; a fresh EIA figure could anchor the heating-oil/heat-pump TCO gap with a proper primary.
- NOAA winter outlook + any NEADA follow-up as crude/ho prices move.
- Fed Oct 27–28 meeting — 12/18 officials pencil one more hike; a realized hike would reprice HELOC/borrowing-cost.
- Remodeling Magazine 2026 Cost vs. Value report (annual, ~late 2026) for the remodel-capitalization axis.
