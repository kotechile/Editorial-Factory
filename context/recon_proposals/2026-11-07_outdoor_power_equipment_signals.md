# Signals: outdoor_power_equipment — 2026-11-07
**Window:** 2026-10-08 → 2026-11-07
**Queries run:** 21

**Dating note.** Every row below is event-dated inside the window. Two rows are dated by the
publisher's own field rather than by the search snippet: the Stanley Black & Decker release carries
"Nov 04, 2026, 06:00 ET", the Husqvarna interim report was submitted "07:00 CEST on Oct 21, 2026",
and both CPSC records print their own warning/recall dates. The Canadian recall row is the only
government record whose page prints a date modified rather than a publication date; its recall date
is 2026-10-26 and its incident cut-off ("As of October 5, 2026, the company has received 19 reports")
is quoted in the claim cell. The market-promotion page that turned up in the sweep (Cub Cadet's
"2026 Ultimate Sales Event", which advertises $300–$1,000 off) is **excluded from the rows**: its own
disclaimer says the offer ran 4/2/2026 – 5/13/2026, so it is a stale page still rendering, not a
current discount.

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | Stanley Black & Decker 3Q 2026: gas walk-behind moved to a licensing model | https://www.prnewswire.com/news-releases/stanley-black--decker-reports-3q-2026-results-302928496.html | 2026-11-04 | Tools & Outdoor net sales up 2% as volume rose 7% and pricing fell 3%, with "the previously announced strategic transition to a licensing model for the gas walk-behind outdoor products (-2%)"; segment margin 17.0%, up 520 bp, with tariff refunds worth about 430 bp of it | The factory leaves, the badge stays | 88 |
| 2 | CPSC safety warning: PowRyte pressure washers lack the plug-side GFCI | https://www.cpsc.gov/Warnings/2027/CPSC-Warns-Consumers-to-Stop-Using-PowRyte-Pressure-Washers-Immediately-Due-to-Serious-Shock-and-Electrocution-Hazards-Risk-of-Serious-Injury-or-Death | 2026-10-22 | Units "lack an integrated immersion protection device on or near the power plug", sold on Amazon and eBay "for between $92 and $320"; "Powell Works, Inc. of China has not responded to requests for a recall"; remedy is to cut the cord and dispose of it; warning 27-036 | No recall to wait for | 86 |
| 3 | CPSC recall #27-016: 42,860 DR Power trimmer mowers, fire hazard | https://www.cpsc.gov/Recalls/2027/DR-Power-Equipment-Recalls-Pilot-and-Premier-Trimmer-Mowers-Due-to-Risk-of-Serious-Injury-or-Death-from-Fire-and-Burn-Hazards | 2026-10-08 | About 42,860 Pilot and Premier walk-behind trimmer mowers recalled; 19 reports of the mowers catching fire and 2 injuries; free repair kit; sold Nov 2022 – Jul 2026 for $380 to $550 at Ace, Tractor Supply, Bomgaars and drpower.com; imported by Generac Power Systems of Waukesha, Wisconsin; Fast Track recall | The same defect, a different answer | 84 |
| 4 | Husqvarna Q3 2026: organic sales down 5% on a cost-and-price program | https://www.husqvarnagroup.com/sites/husqvarna/files/pr/202610207143-1.pdf | 2026-10-21 | Net sales SEK 9,012m, organic sales down 5%; the SEK 3bn gross-savings program reached about SEK 935m year to date, "including around SEK 305m in the third quarter"; the quarter's response is "targeted price increases, supply chain actions and product cost optimization" | The other big maker is cutting, not building | 80 |
| 5 | Greenworks Commercial debuts a 400-volt OPTIMUS UTV | https://www.prnewswire.com/news-releases/greenworks-commercial-debuts-all-new-optimus-utv-at-equip-exposition-2026-302913553.html | 2026-10-20 | The OPTIMUS UTV extends the high-voltage OPTIMUS platform into utility vehicles at Equip Exposition 2026, with a launch expected in early 2027 | The challenger extends the platform, the incumbent hands off the brand | 74 |
| 6 | Health Canada: 37,667 Benchmark electric snow throwers, cord cracks in extreme cold | https://recalls-rappels.canada.ca/en/alert-recall/benchmark-branded-22-inch-15-amp-electric-snow-thrower-recalled-due-electric-shock | 2026-10-26 | 37,667 units of the 22-inch, 15-amp YF6022 sold Nov 2020 – May 2026; "As of October 5, 2026, the company has received 19 reports of the power cord of the product breaking in Canada"; remedy is to destroy the product in exchange for a refund from Home Hardware | Destroy it for a refund | 64 |

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=6 candidates=0 heuristic=- window=2026-10-08..2026-11-07 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

## Dated background

- Stanley Black & Decker's agreement to sell its Excel Industries business — the professional-grade,
  gas-powered ride-on and zero-turn mowers sold under the Hustler brand, expected to generate about
  $300m of FY2026 revenue — to Bad Boy Mowers, announced 2026-09-04, **outside the 30-day window** and
  carried here as the antecedent of the in-window licensing row:
  https://www.prnewswire.com/news-releases/stanley-black--decker-announces-agreement-to-sell-excel-industries-to-bad-boy-mowers-302870329.html
- The 2026-11-04 release also records "a pre-tax impairment loss in the third quarter of 2026 related
  to the Excel Industries ("Excel") business" — the same document as row 1.
- OPEI's litigation over the EPA waiver that lets California enforce its small-off-road-engine
  zero-emission standards, reported in the October 2026 CAG newsletter (month-dated, no day):
  https://publicaffairs.scga.org/blog/cag-newsletter-october-2026
- Agiiman recalled about 80 electric pressure washers on 2026-04-16 for the same missing integral
  GFCI, with a full refund and a cut-the-cord photo requirement, sold on Amazon for about $90:
  https://www.cpsc.gov/Recalls/2026/Agiiman-Recalls-Pressure-Washers-Due-to-Serious-Risk-of-Injury-or-Death-from-Shock-and-Electrocution-Hazards
- LANCHEZ pressure washers were recalled for the same missing GFCI plus a short power cord, a class
  CPSC keeps restating: https://www.cpsc.gov/Recalls/2026/LANCHEZ-Pressure-Washers-Recalled-Due-to-Serious-Risk-of-Injury-or-Death-from-Shock-and-Electrocution-Hazards
- The July 2026 Kobalt 24V/48V USB-C battery recall (about 554,780 units, fire hazard) is outside the
  window and is not a row: https://www.cpsc.gov/Recall-Products/Leaf-Blowers
