# Verified Brief: outdoor_power_equipment — 2026-10-31 (EVERGREEN)
**Brief:** `context/recon_proposals/2026-10-31_outdoor_power_equipment_evergreen_brief.md` (evergreen gate PASS, marker `rows=7 fetched=7 sources=5 hosts=4`, checked_at 2026-10-31T19:06:07+00:00)
**Claim rows:** 9 | **VERIFIED:** 9 | **FLAGGED:** 0 | **REMOVED:** 0
**Method:** every row below was re-fetched live on 2026-10-31 with `citation_hub_dossier.fetch_source` and the verbatim string was read inside its own sentence (`figure_evidence`), not merely found somewhere on the page.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | Cold capacity | A pack that delivers 100 percent capacity at 27°C delivers only about 50 percent at -18°C | VERIFIED | https://batteryuniversity.com/article/bu-502-discharging-at-high-and-low-temperatures | "Cold temperature increases the internal resistance and lowers the capacity. A battery that provides 100 percent capacity at 27°C (80°F) will typically deliver only 50 percent at –18°C (0°F). The momentary capacity-decrease differs with battery chemistry." |
| 2 | Rating temperature | Packs are specified at 27°C, which is why the label's run time is a mild-weather number | VERIFIED | https://batteryuniversity.com/article/bu-502-discharging-at-high-and-low-temperatures | "This is likely also the reason why manufacturers prefer to specify batteries at a toasty 27°C (80°F)." |
| 3 | Cold capacity is temporary | The shortfall is described as momentary and chemistry-dependent, not permanent damage | VERIFIED | https://batteryuniversity.com/article/bu-502-discharging-at-high-and-low-temperatures | "The momentary capacity-decrease differs with battery chemistry." |
| 4 | Sub-freezing charge | A consumer lithium-ion pack cannot be charged below 0°C, and a sub-freezing charge plates metallic lithium even while the pack appears to be charging normally | VERIFIED | https://batteryuniversity.com/article/bu-410-charging-at-high-and-low-temperatures | "Many battery users are unaware that consumer-grade lithium-ion batteries cannot be charged below 0°C (32°F). Although the pack appears to be charging normally, plating of metallic lithium occurs on the anode during a sub-freezing charge that leads to a permanent degradation in performance and safety." |
| 5 | Sub-freezing charge rate | At -30°C the allowable charge rate is 0.02C, which stretches a charge past 50 hours and is called impractical | VERIFIED | https://batteryuniversity.com/article/bu-410-charging-at-high-and-low-temperatures | "According to research papers, the allowable charge rate at –30°C (–22°F) is 0.02C. At this low current, the charge time would stretch to over 50 hours, a time that is deemed impractical." |
| 6 | Charge window | The best charging window is 10°C to 30°C; advanced chargers refuse to charge Li-ion below freezing | VERIFIED | https://batteryuniversity.com/article/bu-410-charging-at-high-and-low-temperatures | "For best results, charge between 10°C and 30°C (50°F and 86°F). Lower the charge current when cold." / "Advanced chargers (Cadex) prevent charging Li-ion below freezing." |
| 7 | Heat costs cycle life | Running a pack at 30°C instead of a moderate room temperature cuts cycle life 20 percent, and 40 percent at 40°C | VERIFIED | https://batteryuniversity.com/article/bu-502-discharging-at-high-and-low-temperatures | "If, for example, a battery operates at 30°C (86°F) instead of a more moderate lower room temperature, the cycle life is reduced by 20 percent. At 40°C (104°F), the loss jumps to a whopping 40 percent, and if charged and discharged at 45°C (113°F), the cycle life is only half of what can be expected if used at 20°C (68°F)." |
| 8 | Pack life and climate | National-laboratory modelling puts pack life at 12 to 15 years in moderate climates and 8 to 12 in extreme ones | VERIFIED | https://afdc.energy.gov/fuels/electricity-benefits | "Predictive modeling by the National Laboratory of the Rockies indicates that today's batteries may last 12 to 15 years in moderate climates (8 to 12 years in extreme climates)." |
| 9 | Same effect in a vehicle | For EVs, cold cuts fuel economy about 39 percent in mixed driving and range by 41 percent | VERIFIED | https://www.fueleconomy.gov/feg/coldweather.shtml | "For electric vehicles (EVs), fuel economy can drop roughly 39% in mixed city and highway driving, and range can drop by 41%. About two-thirds of the extra energy consumed is used to heat the cabin." |
| 10 | The machine the reader owns | EGO's 24-inch two-stage is listed as running on two recommended 7.5Ah ARC Lithium packs on the 56-volt platform | VERIFIED | https://www.egopowerplus.com/two-stage-snow-blower-snt2400 | "Powered by 2 (7.5ah) ARC Lithium™ Batteries (recommended)" / "Peak Power™ technology combines any two EGO batteries to clear, heavy, wet snow" |

## Derived arithmetic authorised for the article (computed here, stated as derived)

| Figure | Basis | Value |
|---|---|---|
| Energy in one recommended pack | 56 V × 7.5 Ah (row 10) | 420 Wh |
| Energy in the recommended pair | 2 × 420 Wh (row 10) | 840 Wh |
| What that pair delivers at -18°C | 840 Wh × 50 percent (rows 1, 10) | about 420 Wh |
| Charge time for a 7.5Ah pack at the -30°C rate | 7.5 Ah ÷ 0.15 A (0.02C, row 5) | 50 hours |

## Drafter rulings

1. **Write the cold figure as a comparison, never as a guarantee.** The source's sentence is "100 percent at 27°C … typically deliver only 50 percent at -18°C" and its next sentence says the decrease "differs with battery chemistry". The article may say a pack at -18°C gives about half its rated capacity; it may not say a specific blower clears exactly half a driveway, and it must not present -18°C as the reader's own storm temperature.
2. **Keep "momentary" and "permanent" apart.** The cold capacity loss is temporary and comes back when the pack warms (row 3); the sub-freezing charge is a permanent degradation (row 4). Do not let the two merge into "cold ruins your pack".
3. **The 50 percent is a capacity-at-temperature figure, not a run-time promise.** A tool's run time at -18°C also depends on load and cut-off voltage, which no fetched source quantifies; say "about half its rated capacity" and stop there.
4. **The 12 to 15 vs 8 to 12 band is "extreme climates", which includes heat, not cold alone** (row 8). Never write it as a cold-only penalty.
5. **Do not price anything.** No pack price, no dollars per watt-hour, no cost per charge — that arithmetic is the published thesis of `2026-10-25_your-550-battery-spare-is-wrong` and `2026-10-24_your-heated-mat-costs-50-times-the-blower`, and repeating it here re-argues them.
6. **The EGO configuration is a vendor claim dated 2026-10-31**, and the article says so; the two-pack arithmetic below is ours, not EGO's.
7. **Do not claim a cold-start feature exists on the reader's machine.** The nearest vendor evidence the desk had (STIHL's cold-start pack) is today's news artifact's subject; this piece stays on what the cells do.
