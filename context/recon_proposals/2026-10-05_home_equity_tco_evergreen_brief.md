# Evergreen Brief: home_equity_tco — 2026-10-05
**Archetype:** evergreen
**Vertical:** home_equity_tco
**Persona:** pro_homeowner
**Decision the reader is facing:** With a finite capital budget this year and a home-equity line as the funding source, should the money go to the discretionary interior remodel the household most wants (a kitchen or bath), or to entry-and-envelope replacements — and how much does that plan change if the home is sold within three years rather than held for ten?
**Durability:** The load-bearing figure — the share of a project's cost recovered at resale — is re-published every year by the same two national studies (Zonda/JLC's *Cost vs. Value* and NAR/NARI's *Remodeling Impact Report*), so the *ranking* is what lasts even as the percentages drift edition to edition; every number here is dated to its 2025 edition (Cost vs. Value published 2025-09-18; Remodeling Impact Report 2025-04-09; JCHS *Improving America's Housing* 2025-03). The structural finding — entry and envelope replacements recover more at resale than discretionary interior remodels — has repeated for years, and the stock of 145 million US homes still needing envelope and mechanical renewal does not shrink. Figures are as of the 2025 editions; a reader in 2026 should re-read the next editions for the current percentages, not the shape of the answer.
**De-dup:** 2026-10-03_heloc-at-8-vs-battery-that-earns is this vertical's nearest prior published artifact — a *news* synthesis about borrowing cost versus a battery's grid revenue, framed by an 8%-HELOC rate that is now stale. This brief decides a different and durable question: which *category* of remodel preserves capital at resale, anchored to the annual resale studies rather than to a rate snapshot. The vertical's own news track for this week returned "no publish" (2026-10-05_home_equity_tco_angle_brief), so nothing newer competes; the adjacent draft 2026-10-03_heat-pumps-cheaper-to-run-pricier-to-buy is a different vertical (home_infrastructure_lifecycle_tco) and a different thesis (running cost vs. equipment price).
**Thesis:** The resale data prices the shell, not the show: entry and envelope replacements routinely recover more than they cost (garage door 267.7%, steel door 216.4%, stone veneer 207.9%), while the remodel categories homeowners most enjoy — kitchen and bath — recover roughly half or less (mid-range major kitchen 51%, upscale 36%), and the majority of that discretionary work (54%) is financed with home equity; so the durable capital rule is to fund the >100%-recovery shell projects first and treat the cosmetic remodel as consumption you pay for with cash, not leverage.

**Lead:** From the vertical's own `primary_angles` in `context/verticals.json` ("remodel capitalization trap vs mechanical upgrades") and `context/growth_os/founder-voice.md` §3 (`home_equity_tco`: "The Remodel Capitalization Trap" — cosmetic renovations return "less than 40 cents on the dollar"; "true equity preservation focuses on building envelope integrity, electrical service capacity, and mechanical lifecycle renewals"), cross-checked against the persona's `wants` in `context/personas.json` (`pro_homeowner`: "TCO depreciation math … friction reduction") and the founder's field note in `context/growth_os/customer-truth.md` (the $92k Boston kitchen that yielded a $32k appraisal bump). GSC (`scripts/gsc_analyzer.py --vertical home_equity_tco`) returned 0 opportunities — bonus signal only on a young site, never a veto. The founder's "under 40 cents" claim had no fetchable primary in the corpus, so the durable figures were grounded against the annual, measured resale studies rather than asserted.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Zonda — "2025 Cost vs. Value Report" (38th annual; the report's publisher, Zonda/JLC Group) | https://zondahome.com/2025-cost-vs-value-report | 2026-10-05 | 267.7% — garage-door replacement cost recouped ($4,672 job cost vs. $12,507 value at sale), the report's #1 project | measured |
| 2 | Zonda — "2025 Cost vs. Value Report" | https://zondahome.com/2025-cost-vs-value-report | 2026-10-05 | 112.9% — minor kitchen remodel cost recouped ($28,458 vs. $32,141), the only interior project in the top five | measured |
| 3 | Zonda — "2025 Cost vs. Value Report" | https://zondahome.com/2025-cost-vs-value-report | 2026-10-05 | 207.9% — manufactured stone veneer replacement cost recouped ($11,702 vs. $24,328) | measured |
| 4 | Zillow — "Kitchen Remodel Return on Investment" (reproduces the JLC/Zonda 2025 Cost vs. Value national table) | https://www.zillow.com/learn/kitchen-remodel-roi | 2026-10-05 | 51% — mid-range major kitchen remodel cost recouped ($82,793 cost vs. $42,130 return) | measured (resale survey) |
| 5 | Zillow — "Kitchen Remodel Return on Investment" (JLC/Zonda 2025 CVV national table) | https://www.zillow.com/learn/kitchen-remodel-roi | 2026-10-05 | 36% — upscale major kitchen remodel cost recouped ($164,104 cost) | measured (resale survey) |
| 6 | NARI / NAR — "2025 Remodeling Impact Report" (2025-04-09) | https://nari.org/nari-blog-main/2025-remodeling-impact-report | 2026-10-05 | 100% — cost recovery on a new steel front door, the report's highest-recovery project (joy leaders: kitchen upgrade, primary suite, new roofing, all 10/10) | measured |
| 7 | NARI / NAR — "2025 Remodeling Impact Report" | https://nari.org/nari-blog-main/2025-remodeling-impact-report | 2026-10-05 | 54% — share of consumers who financed a remodel with a home-equity loan or line of credit (savings 29%, credit cards 10%) | measured |
| 8 | Harvard Joint Center for Housing Studies — "Improving America's Housing 2025" | https://www.jchs.harvard.edu/improving-americas-housing-2025 | 2026-10-05 | $600 billion — US remodeling market size, still 50 percent above pre-pandemic levels, across 145 million homes | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Cosmetic remodel vs. the shell: where home capital actually survives at resale | 9 | 9 | 9 | 8 | 8.9 | **winner** |
| Deferred-maintenance 1-to-10 cost decay and the annual capital-reserve rate | 8 | 9 | 5 | 8 | 7.5 | dropped — the decay ratio and the 1–2% reserve exist only as founder-voice assertions; no fetchable primary states them |
| Time-of-use arbitrage and battery amortization payback | 8 | 8 | 7 | 7 | 7.6 | dropped — overlaps the published 2026-10-03_heloc-at-8-vs-battery-that-earns, and durable arbitrage figures are utility-tariff-specific, not national |
| Heat-pump balance point and the electric strip-heat shock | 7 | 8 | 6 | 7 | 7.0 | dropped — nearest to the adjacent-vertical 2026-10-03_heat-pumps-cheaper-to-run-pricier-to-buy, and the load-bearing COP/balance-point figures are brand datasheets, not neutral primaries |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=8 fetched=8 sources=4 hosts=4 decision="sha1:722276b0f0" dedup="matched a prior artifact: 2026-10-03_heloc-at-8-vs-battery-t" window_days=180 checked_at=2026-10-05T18:33:22+00:00 -->
<!-- evergreen-gate:end -->
