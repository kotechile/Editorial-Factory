# Angle Brief: expat_cross_border_relocation — 2026-10-08

**Angle Type:** *(none — no publish this cycle)*
**Winner:** *(none — no publish this cycle)*
**Verdict:** **NO PUBLISH** — anchor-driven vertical, third run; the window (2026-09-08 → 2026-10-08) advanced only ~7 days since the 2026-10-01 second run, no candidate clears the ≥8.0 gate, and the mechanically-seeded synthesis block's best pair scores far below the gate (and the runner-up pairs two rows of the same story).

## Scoring table — single-signal candidates (composite = 0.40·N + 0.30·A + 0.30·S)

| Candidate | Novelty | Authority | Shareability | Composite | Disposition |
|---|---|---|---|---|---|
| Dutch Tax Plan 2027 / Prinsjesdag 2026 (30% ruling → 27% from 1 Jan 2027, higher thresholds, partial non-resident status ends; new startup stock-option break) — signals #1 / #3 | 6.5 | 8.5 | 7.5 | **7.4** | Below gate — the headline figure (the 27% cut) was decided in the **2025** Tax Plan, so Prinsjesdag re-confirms a scheduled change rather than reporting a new one; the only genuinely new 2027 measure (the 65%-of-gain startup stock-option break) is an employer/startup angle, not the expat persona's core |
| Spain employer information obligations (in force 5 Oct 2026) — signal #4 | 6.5 | 6.5 | 5.5 | **6.3** | Below gate — an employment-transparency duty, off the vertical's FEIE/FTC/FX/healthcare beat and low reach |
| IRS Rev. Proc. 2026-24 (2027 HSA limits, first official 2027 figure) — corroborating note | 6.0 | 9.0 | 3.0 | **5.7** | Below gate — HSA-specific and tangential; significant only as evidence the IRS is releasing 2027 amounts piecemeal while the main Rev. Proc. (FEIE 2027) stays pending |

## Scoring table — mechanically-seeded synthesis pairs (`synthesize_topics.py --seed`, advisory)

Synthesis composite = 0.35·E + 0.30·A + 0.35·S.

| Pair | Emergence (E) | Dual Authority (A) | Tension (S) | Composite | Disposition |
|---|---|---|---|---|---|
| #1 ⨂ #4 — Dutch expat-regime tightening ⨂ Spain employer information obligations | 4.0 | 7.0 | 5.0 | **5.3** | Rejected — a token collision, not a thesis: the two are unrelated policy areas (Dutch *personal* tax regime vs a Spanish *employment-transparency* duty); combining them yields no emergent claim either leg states |
| #1 ⨂ #3 — Dutch Tax Plan ⨂ a DLA Piper alert on the same Dutch Tax Plan | 2.0 | 7.0 | 3.0 | **3.8** | Rejected — the two legs are the same story (a corroborating legal alert of signal #1), not independent anchors (the seeder itself flagged `prior_cycle_token_overlap:ruling`); a "synthesis" of a signal with its own corroboration is not a synthesis |

No synthesis clears 8.0, and none beats the best single-signal candidate (7.4) by the required ≥0.3 margin.

## Why "no publish" (not "widen to 45 days")

The sweep returned a healthy result set (32 queries across the IRS, OECD, US-expat-tax, foreign-regime, remote-nexus, visa, wealth-migration and cost-of-living surfaces) but the vertical is anchor-driven: its configured sources (`irs_international_bulletins`, `oecd_tax_reports`, `pwc_global_mobility`, `numbeo_cost_of_living`, `international_living`, `nomad_capitalist_audits`) publish annually/quarterly. The single acute watch-item carried across all three cycles — the **official IRS Rev. Proc. 2026-xx with the FEIE 2027 figure** — has **not** landed (the IRS/Treasury 2026–2027 Priority Guidance Plan still lists the 2027 inflation-adjustment revenue procedure as pending; only the HSA-only Rev. Proc. 2026-24 has published).

The one genuinely fresh in-window primary is the **Dutch Tax Plan 2027** (Prinsjesdag, 15 September 2026). It is well-sourced and on-vertical — a strong **Authority** leg (Dutch government primary) with real **Shareability** for the Netherlands' large expat population. But its load-bearing headline figure is **not new in the window**: the 30%→27% cut and the end of the partial non-resident status were both decided in the **2025** Tax Plan and have been widely covered for over a year; Prinsjesdag 2026 re-confirms that they proceed. Per `virality_judge.md` §3.5's anchor-freshness rule, an out-of-window anchor must not be carried past the freshness gate on authority/shareability alone — and the reportable "new" element (the RVO-certified startup/scale-up stock-option break) lands on the `career_velocity_equity_engineering`/employer beat, not this vertical's FEIE/FTC/FX/healthcare core. Scored honestly it is a 7.4, not ≥8.

**Per `virality_judge.md` §3.5 + `radar_30day.md` §4:** an anchor-driven vertical whose window advanced ~7 days legitimately yields "no publish"; the correct outcome is a hold with a sharp watch-list, never a widened window or a padded composite.

## Single claim to defend (for the next cycle, when the official figure lands)

*"The 2025 government shutdown deleted a CPI month, and that missing number is quietly breaking the 12-month inflation average that sets the Foreign Earned Income Exclusion — so the IRS's own 2027 FEIE figure is less predictable this year than any in recent memory."* (Only defensible once the official Rev. Proc. 2026-xx publishes — that is the primary that makes the missing-CPI consequence load-bearing, not a forecast.)

## Runner-up rejected (highest single-signal composite)

**Dutch Tax Plan 2027 / Prinsjesdag 2026 (7.4).** Genuinely fresh as a *primary document* and dead-on the `cross_border_expat` persona — but the number the piece would lead on (the ruling dropping to 27%) is a >12-month-old decision. Held, not run: the moment the official Rev. Proc. 2026-xx publishes the 2027 FEIE (expected mid/late Oct or early Nov 2026), re-score the collision *(shutdown-CPI mechanism ⨂ new FEIE figure)* — it is the most likely next ≥8 candidate for this vertical. A second runnable angle: the Dutch 2027 Tax Plan's **new startup/scale-up stock-option regime** if a primary Dutch-government source (Belastingplan 2027 / RVO) confirms the 65%-of-gain mechanics.

## Failure class

Anchor-driven vertical, third run, weak window. Already covered by `radar_30day.md` §4 + `virality_judge.md` §3.5 — no new skill patch required (see `skills/self_improvement_eval.md` log).
