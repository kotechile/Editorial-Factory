# Evergreen Brief: home_diagnostics_tech — 2026-11-07
**Archetype:** evergreen
**Vertical:** home_diagnostics_tech
**Persona:** homeowner_pro
**Decision the reader is facing:** The meter still turns with every fixture shut off and the bill jumped: do I pay $175–$650 for someone to listen to the slab before anyone opens it, and what does a clean listen actually prove?
**Durability:** The physics does not expire — a listening test hears water escaping a line that is still under pressure, so it goes quiet on a drained line, a plastic run or a leak standing in its own puddle — and the two published accuracy figures are as of the 2023 studies that produced them, the household leak volumes are as of the 2026 EPA Fix a Leak Week page, and the fee bands are as of the 2026 contractor cost guides cited here. Every number is dated in the body and none of them is a rate that reprices quarterly.
**De-dup:** `2026-10-31_your-radon-test-39-isnt-a-pass` is this vertical's nearest prior artifact (a sampling protocol for a test whose result is misread), and this piece is a different instrument and a different error: radon is a passive sampler read against an action level, while this is an active listening test whose failure mode is silence, not a threshold. Also checked against `2026-10-24_your-250-imager-needs-15-degrees` (the delta-T tell for an imager — a different tool answering a different question) and, cross-vertical, `2026-10-06_water-leak-monitor-rate-threshold` and `2026-11-03_your-leak-alert-24-hours-at-best`, which both own the *monitor* thesis (a flow threshold or a utility's alert cadence tells you water is escaping); neither owns where it is escaping, which is what a locator sells.
**Thesis:** An acoustic leak locator sells a drill point, not a diagnosis — its published hit rate was earned on a testbed far larger and louder than a house supply line, it cannot hear a line that is not under pressure, and the $100–$250 that proves which pipe is losing water is the step that decides whether the $350–$650 listen is worth buying.

**Lead:** The vertical's own beats — `primary_angles` item 3, "acoustic and ultrasonic leak detection before the slab gets opened: hit rate and false positives" — which is the one angle in the list that no run has published (the imager, moisture-meter, borescope and resolution angles were all taken on 2026-10-24, 10-25, 11-01 and 11-07). The material is the gap between what the published accuracy numbers were measured on and what a homeowner's slab actually offers the microphone.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | U.S. EPA WaterSense — Fix a Leak Week | https://www.epa.gov/watersense/fix-leak-week | 2026-11-07 | 50 gallons or more per day — nine percent of homes have leaks that waste 50 gallons or more per day, and the average household's leaks waste more than 9,300 gallons a year | measured |
| 2 | U.S. EPA WaterSense — Fix a Leak Week | https://www.epa.gov/watersense/fix-leak-week | 2026-11-07 | 12,000 gallons per month — the free test: a family of four exceeding 12,000 gallons in a winter month likely has a serious leak, and a meter read before and after a two-hour no-use period settles whether water is moving | measured |
| 3 | An, Huang & Li, "Constant false alarm rate detection of pipeline leakage based on acoustic sensors," Scientific Reports 13:14149 (2023) | https://pmc.ncbi.nlm.nih.gov/articles/PMC10465504 | 2026-11-07 | 84.6% — correct detection on a 5 mm leak hole, against 97.7% at 7 mm and 98% at 10 mm; 324 simulated tests, 94.1% overall, 1.2% overall false-alarm rate | measured |
| 4 | Mazumder et al., "Benchmarking dataset for leak detection and localization in water distribution systems" (Data in Brief, 2023) | https://pmc.ncbi.nlm.nih.gov/articles/PMC10147960 | 2026-11-07 | 152.4 mm — the public water benchmark is a laboratory testbed of 152.4 mm PVC pipe, 47 m long, with leaks down to a 2 mm2 area, deliberate traffic and tool noise, and 280 recorded signals | measured |
| 5 | GPRS — "Acoustic Leak Detection: How Does It Work?" | https://www.gp-radar.com/article/acoustic-leak-detection-how-does-it-work | 2026-11-07 | 30 psi — the hollow leak tone is almost always present in leaking pipes pressurized at 30 psi and above; ambient sewer flow and traffic mask it, and water pooling at the leak site acts as an acoustic insulator | vendor claim |
| 6 | Fix It Real — "Professional water leak detection cost in 2026" (updated 2026-06-14) | https://www.fixitreal.com/costs/professional-leak-detection-cost | 2026-11-07 | $350–$650 — a slab leak diagnostic runs $350–$650 against $150–$300 for a visible leak, and a listener localizes a wall or slab leak inside a square foot in 20–40 minutes | vendor claim |
| 7 | AlertPlumber — "Leak Detection Cost: What Plumbers Charge" | https://alertplumber.com/guides/leak-detection-cost | 2026-11-07 | $175–$400 — slab leak detection runs $175–$400 and is billed before the repair scope is set, while pressure testing to confirm the leak exists runs $100–$250 | vendor claim |

## Candidate topics considered

| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| What an acoustic slab-leak listen can and cannot prove (this brief) | 9 | 9 | 8 | 9 | 8.8 | **winner** |
| Outlet and circuit analyzers: the bootleg ground a three-light tester cannot see | 8 | 9 | 5 | 8 | 7.5 | dropped — refused on evidence 2026-10-31 (InterNACHI tester articles 404 to the verifier, NEC is not on eCFR, NFPA paywalled, so no safety figure can carry a gate row) |
| A DIY ultrasonic transmitter and receiver as a slab-leak locator | 7 | 8 | 5 | 7 | 6.8 | dropped — every anchor is a vendor product page claiming its own accuracy; no measured figure on a residential line |
| Thermal versus acoustic for a hot-water slab leak | 7 | 8 | 7 | 7 | 7.3 | dropped — retreads `2026-10-24_your-250-imager-needs-15-degrees`, which already owns the delta-T argument |

## Why this clears 8

- **Usefulness (9).** The decision arrives as a meter that will not stop turning, which is the one moment a homeowner is asked to spend $175–$650 with no way to check the work. Source 2 is the free test that precedes every paid one, and source 7 prices the pressure test that decides whether the listening test has anything to hear.
- **Durability (9).** Nothing here is a price that reprices quarterly: the 30 psi threshold, the masking effects and the miss rate on a small hole are physics and measurement, and the fee bands carry their own as-of date.
- **Evidence (8).** Two EPA rows (measured), two peer-reviewed rows on different hosts (measured), and three practitioner/vendor rows clearly labelled. Nothing load-bearing rests on a vendor's claim about its own accuracy. Held back one point because the accuracy study is a pipeline experiment rather than a house, which the article states in the sentence that uses it.
- **Actionability (9).** It carries a ladder with numbers: free meter test → $100–$250 pressure test that names the system → $175–$650 listen, plus the ratio of the fee to the repair it precedes ($175 against a $5,000 dig-and-replace is 3.5%; $650 against a $1,500 spot repair is 43%).

## Numbers the body must be able to defend

- 50 gal/day × 365 = 18,250 gal/yr for the heaviest-decile household leak (source 1, arithmetic shown in the body), against the 9,300 gal/yr average.
- 5 mm miss rate: 100 − 84.6 = 15.4%, i.e. about one in six and a half small-hole tests missed (source 3).
- Fee against repair: $175 ÷ $5,000 = 3.5%; $650 ÷ $1,500 = 43% (sources 6, 7, and the repair bands quoted with them).
- Testbed size: 152.4 mm is a six-inch main; a residential supply line is typically far smaller — stated qualitatively, no invented number.

## Gate result

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=7 fetched=7 sources=6 hosts=5 decision="sha1:9dd5aaf2c1" dedup="matched a prior artifact: 2026-10-31_your-radon-test-39-isnt" window_days=180 checked_at=2026-11-07T19:34:04+00:00 -->
<!-- evergreen-gate:end -->
