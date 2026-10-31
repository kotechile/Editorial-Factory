# Evergreen Brief: outdoor_power_equipment — 2026-10-31
**Archetype:** evergreen
**Vertical:** outdoor_power_equipment
**Persona:** homeowner_pro
**Decision the reader is facing:** Whether to buy more battery capacity — a second pack, or the 10Ah kit over the 7.5Ah one — to get a cordless snow blower through a hard cold snap, or to spend nothing and change how the packs are stored and charged. The decision lands in the week before the first sub-zero storm, and it re-opens every winter for as long as the reader owns the machine.
**Durability:** The load-bearing numbers are cell chemistry, not catalogue copy: capacity at 27°C against capacity at -18°C, the 0°C floor below which a consumer lithium-ion pack may not be charged at all, and the 0.02C rate that makes a sub-freezing charge take more than 50 hours instead of one. Those do not move with model years, and the article states them as of the Battery University pages fetched 2026-10-31. The two figures that can date are dated in the body: the National Laboratory of the Rockies climate-life modelling as published on afdc.energy.gov as of 2026-10-31 (12 to 15 years in moderate climates, 8 to 12 in extreme ones), and EGO's two-7.5Ah recommended configuration as listed on egopowerplus.com on 2026-10-31.
**De-dup:** `2026-10-31_why-37667-snow-throwers-failed-winter` is this vertical's nearest prior artifact — today's news piece, which reads a manufacturer's -4°F cold-start claim and a Health Canada recall of 37,667 corded throwers whose power cord breaks in extreme cold. That article decides which number to look for on a spec sheet; its subject is the cord, and it never says what the cold does inside the pack. Two further artifacts checked and distinguished: `2026-10-25_your-550-battery-spare-is-wrong` (a three-machine review whose thesis is that a $50 kit step buys 280 Wh while a spare 10Ah pack costs $549.99 — a pricing argument this piece does not make) and `2026-10-24_your-heated-mat-costs-50-times-the-blower` (mat versus blower, priced per square foot and per inch cleared). This article carries no price at all; it is about what a pack delivers at temperature and how it is charged. A corpus grep for "cold-start", "-18", "lithium plating", "charge below" and "internal resistance" over `published/`, `context/drafts/` and `context/recon_proposals/` returns no artifact that argues the mechanism.
**Thesis:** A pack's run time is a 27°C measurement that roughly halves at -18°C, so a winter run-time shortfall is a temperature problem before it is a capacity problem — and the one cold mistake that is permanent is charging a frozen pack, which plates metallic lithium on the anode while the charger reports a normal charge.

**Lead:** The vertical's own beats in `context/verticals.json` `primary_angles` #6 ("cold-weather failure modes: what actually stops a battery blower at -10C"), read against #1 (the blower/mat/shovel comparison, which established that this reader owns a two-pack machine) and the `homeowner_pro` persona's stated wants — "payback math, gotchas, code/incentive reality". The specific material is the pair of numbers the cell-chemistry literature publishes and no snow-blower page does: the 27°C rating temperature and the 50 percent delivery at -18°C, and the separate prohibition on charging below 0°C. GSC was checked as a bonus signal only (`python3 scripts/gsc_analyzer.py --vertical outdoor_power_equipment --export-md` returned 0 candidates on 2026-10-31; thin impressions on a young site never veto a topic), and the intel feed was not the lead.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Battery University, BU-502 "Discharging at High and Low Temperatures" (capacity and internal resistance) | https://batteryuniversity.com/article/bu-502-discharging-at-high-and-low-temperatures | 2026-10-31 | -18°C — cold temperature increases the internal resistance and lowers the capacity, and a battery that provides 100 percent capacity at 27°C (80°F) will typically deliver only 50 percent at -18°C (0°F) | measured — a compilation of published lab discharge data, not a vendor claim |
| 2 | Battery University, BU-502 (the rating temperature) | https://batteryuniversity.com/article/bu-502-discharging-at-high-and-low-temperatures | 2026-10-31 | 27°C — this is likely also the reason why manufacturers prefer to specify batteries at a toasty 27°C (80°F) | measured — the source's reading of how the industry rates packs |
| 3 | Battery University, BU-502 (heat shortens cycle life) | https://batteryuniversity.com/article/bu-502-discharging-at-high-and-low-temperatures | 2026-10-31 | 40°C — at 40°C (104°F) the cycle-life loss jumps to a whopping 40 percent, against 20 percent at 30°C (86°F) | measured — compilation, stated as a general rule |
| 4 | Battery University, BU-410 "Charging at High and Low Temperatures" (sub-freezing charge rate) | https://batteryuniversity.com/article/bu-410-charging-at-high-and-low-temperatures | 2026-10-31 | 0.02C — according to research papers the allowable charge rate at -30°C is 0.02C, and at that current the charge time would stretch to over 50 hours | measured — literature rate, stated as impractical |
| 5 | U.S. Department of Energy, Alternative Fuels Data Center — batteries (climate and pack life) | https://afdc.energy.gov/fuels/electricity-benefits | 2026-10-31 | 12 to 15 years — predictive modeling by the National Laboratory of the Rockies indicates that today's batteries may last 12 to 15 years in moderate climates (8 to 12 years in extreme climates) | measured — national-laboratory modelling, published by the DOE |
| 6 | U.S. Department of Energy / EPA, FuelEconomy.gov — cold weather (the same effect in a vehicle pack) | https://www.fueleconomy.gov/feg/coldweather.shtml | 2026-10-31 | 39% — for electric vehicles, fuel economy can drop roughly 39% in mixed city and highway driving, and range can drop by 41% | measured — agency estimate over standardized drive cycles |
| 7 | EGO POWER+ SNT2400 24-inch two-stage snow blower product page (the configuration this reader owns) | https://www.egopowerplus.com/two-stage-snow-blower-snt2400 | 2026-10-31 | 7.5Ah — powered by 2 (7.5Ah) ARC Lithium batteries (recommended) on the 24-inch two-stage | vendor claim — the manufacturer's recommended configuration |

## Derived arithmetic (computed here, stated in the article as derived)

| Figure | Basis | Value |
|---|---|---|
| Energy in one recommended pack | 56 V × 7.5 Ah (row 7, EGO's 56-volt platform) | 420 Wh |
| Energy in the recommended pair | 2 × 420 Wh (row 7) | 840 Wh |
| What the pair delivers at -18°C | 840 Wh × 50 percent (rows 1, 7) | ~420 Wh — the machine behaves like a single pack on a mild day |
| A 7.5Ah pack's charge time at -30°C | 0.02C on 7.5 Ah (row 4) | 0.15 A, i.e. 50 hours |
| Pack life given up in an extreme climate | 12 years minus 8 years (row 5) | up to 4 years |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| What the cold does inside the pack: the 27°C rating, the 50 percent at -18°C, and the sub-freezing charge that damages the cells silently | 9 | 9 | 8 | 8 | 8.6 | **winner** |
| The battery platform trap: true five-tool cost across EGO, Greenworks, DeWalt FlexVolt and Ryobi, priced per watt-hour | 8 | 7 | 9 | 8 | 8.0 | dropped on the de-dup rule — the mechanism (what a spare pack's energy costs against the energy a kit bundles) is the published thesis of `2026-10-25_your-550-battery-spare-is-wrong`; a re-argued version is refused by §3 of the SOP regardless of score |
| Pressure washers where PSI sells and GPM cleans | 7 | 9 | 6 | 7 | 7.25 | dropped — the vendor spec pages fetch, but the surface-limit primaries (what pressure a wood deck or vinyl siding tolerates) are PDFs and extension pages that do not fetch, so the article would be a spec table with no measured leg |
| Cordless versus gas: the carburetor and stale-fuel maintenance tax | 8 | 8 | 5 | 6 | 6.95 | dropped — no fetchable measured anchor for small-engine repair frequency or carburetor cost; every number would be a shop blog |
| Electric zero-turn acre-per-charge and the pack replacement cliff | 8 | 7 | 5 | 7 | 6.85 | dropped — the acreage claims verify, the replacement-pack prices do not exist on any page the verifier can fetch (the same drop as 2026-10-24, re-probed today) |
| Buy-window timing: end-of-season markdown versus peak-storm pricing | 8 | 4 | 7 | 8 | 6.75 | dropped — a price-calendar piece expires inside 90 days, which routes it to the news track by the SOP's own rule |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=7 fetched=7 sources=5 hosts=4 decision="sha1:194dcea7ce" dedup="matched a prior artifact: 2026-10-31_why-37667-snow-throwers" window_days=180 checked_at=2026-10-31T19:06:07+00:00 -->
<!-- evergreen-gate:end -->
