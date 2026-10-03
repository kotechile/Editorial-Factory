# Evergreen Brief: personal_microeconomics_tinkering_tax — 2026-10-03
**Archetype:** evergreen
**Vertical:** personal_microeconomics_tinkering_tax
**Persona:** systems_tinkerer_pro
**Decision the reader is facing:** Whether a hobbyist 3D printer actually pays for itself versus just buying commercial or injection-molded replacement parts, once failed prints and wasted filament are counted rather than only the price of a spool.
**Durability:** The load-bearing figures are behavior/material properties, not prices, so they do not expire: a 2019 academic study of desktop FDM fabrication found a 41.1% print-failure rate, and 2019/2021 filament surveys put failed prints at >80% of waste. The only time-bound figure is the electricity rate, stated as of 2026 (18.44¢/kWh US residential average), and I write it so a reader can re-run the per-print cost at their own local rate.
**De-dup:** 2026-09-26_disney-hulu-fourth-hike-subscription-creep (the only prior published article for this vertical) — that ran the subscription-creep angle; this is the 3D-printing true-cost angle, a distinct beat, and no evergreen brief exists for this vertical yet.
**Thesis:** The $20/kg filament spool is the cheap part — failed prints and filament waste, not electricity, are the real cost of hobby 3D printing.

**Lead:** From the vertical's own `primary_angles` (angle 4: "the true cost of 3d printing and fabrication hobbies filament waste and calibration"), the persona's wants in `context/personas.json` ("3D printing true cost models"), `context/growth_os/founder-voice.md` §3 ("The True Unit Economics of 3D Printing & Fabrication" — a $15 bracket that takes 3 failed attempts is a loss against an injection-molded retail part) and `context/growth_os/customer-truth.md` Anecdote 3 ($42 of filament, test prints and electricity to make an $8.99 replacement clip). No GSC striking-distance data exists for this vertical (bonus signal only), and the intel feeds carry no 3D-printing material, so the topic is sourced from the vertical's own durable beat, not an invented idea.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | Annenberg Media (USC) — "How sustainable is 3D printing, really?" (Apr 24, 2026), reporting Telenko's 2019 study of desktop FDM fabrication | https://www.uscannenbergmedia.com/2026/04/24/how-sustainable-is-3d-printing-really | 2026-10-03 | 41.1% print failure rate in a 2019 study of 3D printing in university MakerSpaces | measured |
| 2 | Filamentive — "The 3D Printing Waste Problem" (2019 survey + 2021 update) | https://www.filamentive.com/the-3d-printing-waste-problem | 2026-10-03 | failed prints account for more than 80% of 3D printing waste | measured |
| 3 | Sinterit — "Do 3D printers use a lot of electricity?" | https://sinterit.com/3d-printing-guide/costs-of-a-3d-printing/3d-printer-electricity-use | 2026-10-03 | FDM printers consume between 50 and 250 watts per hour during operation | vendor claim |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The true cost of 3D printing: failed prints and filament waste, not the $20 spool | 9 | 9 | 8 | 8 | 8.6 | **winner** |
| The "free" self-hosting trap: opportunity cost of your own maintenance hours | 9 | 9 | 5 | 7 | 7.5 | dropped — anchors are secondary blog estimates ($75/hr, 0.25–0.5 FTE); no measured primary for the load-bearing time-cost claim |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=3 fetched=3 sources=3 hosts=3 decision="sha1:98767a46be" dedup="matched a prior artifact: 2026-09-26_disney-hulu-fourth-hike" window_days=180 checked_at=2026-10-03T17:33:32+00:00 -->
<!-- evergreen-gate:end -->
