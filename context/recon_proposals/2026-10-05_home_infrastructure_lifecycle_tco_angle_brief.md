# Angle Brief: home_infrastructure_lifecycle_tco — 2026-10-05

**Verdict: no publish** (weak cycle; virality gate — second run, window advanced only ~2 days)

## Prior-cycle thesis de-dup (§3.5)

The 10-03 first run for this vertical already won the window's sharpest acute story and published
`heat-pumps-cheaper-to-run-pricier-to-buy` (8.5, Synthesis). Its load-bearing primaries are still
in-window and were consumed by that run:

- RMI "Delivered Fuel Customers in Maryland…" (Sept 24) — ~330,000 MD homes on oil/propane save $1,200–$1,600/yr switching to a heat pump (Anchor A)
- ACHR News "Price Increases Remain Part of the Residential HVAC Outlook" (Sept 18) — Gitlin "we can and will continue to raise price"; Trane two 5% increases (Anchor B)

That run's thesis — running-cost savings rising ⨂ upfront equipment price rising — is precisely the
collision any fresh heating-cost story re-forms. The two natural legs for a fresh synthesis are both
already consumed:

- the **delivered-fuel heating-cost leg** → 10-03 RMI-Maryland run (this vertical)
- the **diesel $6.53/gal record leg** → 10-02 `last_mile_routing_fleet_carbon` (cross-vertical)
- the **utility rate-request leg** ($18.6B) → 10-05 `home_equity_tco` sweep (cross-vertical, scored 6.3)

## Fresh signals swept this run (Oct 3–5 window advance)

| # | Signal | N | A | S | Composite | Why it fails |
|---|--------|---|---|---|-----------|--------------|
| 1 | NEADA heating-oil winter forecast: +$878 (~50%) to $2,627 (Oct 2) | 7.0 | 8.0 | 7.0 | **7.3** | fuel-price shock, forecast not realized price; the fuel-switch payoff is itself the 10-03 winner's Anchor A (retread leg); diesel-record leg cross-consumed |
| 2 | DOE residential-duty gas water-heater standard effective Oct 6 (2026) | 6.0 | 8.0 | 5.5 | **6.5** | retread — same event was 10-03 signal #5 (scored 6.2); commercial-duty classification, weak pro_homeowner reach; Novelty capped 6.0 per §3.5 |
| 3 | Xcel CO heat-pump rebate step-down 3x→2x (Oct 1) | 6.5 | 6.0 | 6.0 | **6.2** | single utility, regional; modest rebate reduction; already scored 6.2 in the 10-05 home_equity sweep |
| 4 | Canary "why your energy bills are going up" (Oct 5) | 6.0 | 6.0 | 7.0 | **6.3** | aggregator; load-bearing $18.6B rate-request figure is July 14 PowerLines data (out of window) |

## Synthesis candidates — all below the gate

- **#3 ⨂ #4 (rebate shrinking ⨂ utility rates rising)** — the mechanically-seeded pair
  (`electrification_subsidies_x_utility_rates`, heuristic 0.68): "the rebate is shrinking at the same
  moment the rate base is rising." Coherent but weak: leg B is an aggregator with an out-of-window
  load-bearing figure, so Dual Authority fails, and the tension is regional (one Colorado utility).
  E=6.0, A=5.5, S=6.5 → **6.0**. Below gate.
- **#1 ⨂ 8% HELOC / heat-pump finance (10-03 anchor)** — "the $2,627 oil bill is the new case for
  financing a heat pump." E=7.5, A=7.0, S=7.5 → **7.3**. Reuses the 10-03 run's own anchor leg and
  re-forms the already-published thesis; the fuel-switch payoff leg is cross-consumed by RMI-Maryland.
- **#1 ⨂ #3 (oil shock ⨂ rebate step-down)** — same heating-cost axis, no emergent tension → ~6.8.
- **#1 ⨂ #2 (oil shock ⨂ water-heater mandate)** — no shared axis; two unrelated replacement-window
  items → ~6.2.

## Mechanical seed note

`scripts/synthesize_topics.py --seed` found **1 candidate** (rows=4, candidates=1) — the
`electrification_subsidies_x_utility_rates` archetype fired on #3 (rebate step-down) ⨂ #4 (utility
rate). This is the same quasi-match the 10-05 home_equity run's seeder surfaced and the Judge there
rejected at ~6.5; here it scores 6.0 because leg B carries an out-of-window load-bearing figure. No
synthesis clears the ≥8 gate or beats the best single-signal candidate (7.3) by the ≥0.3 margin.

## Failure class

Already covered by `virality_judge.md` §3.5 (re-run cadence caveat — window barely advanced) and
`radar_30day.md` §4 (anchor-driven vertical). No new patch; logged to `self_improvement_eval.md`.

## Watch-items (most likely next ≥8 primary)

- **EIA Winter Fuels Outlook (~Oct 2026)** — the authoritative cross-fuel heating-cost forecast; a fresh EIA figure could anchor the heating-oil/heat-pump TCO gap with a proper primary (rather than NEADA's forecast).
- **ACHR "HVAC Price Increase List: October 2026"** — the monthly list is the freshest equipment-price primary; if the October list lands with a sharper increase than September's 5–15%, it re-opens the buy-side leg of the break-even race.
- **DOE residential water-heater standard (2029) implementation milestones** and any fresh heat-pump water-heater rebate launch (PA "Penn Energy Savers", MN "Save Energy Minnesota" both pending DOE approval).
- **Remodeling Magazine 2026 Cost vs. Value report** (annual) for the 10-year capex / replacement-window axis.
