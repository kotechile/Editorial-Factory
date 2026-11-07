# Verified Brief: home_diagnostics_tech — 2026-11-07 (evergreen)

Topic: what an acoustic slab-leak listen can and cannot prove. Companion to
`2026-11-07_home_diagnostics_tech_evergreen_brief.md` (gate PASS, 7 rows, 5 hosts).

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | household leak volume | Nine percent of US homes have leaks wasting 50 gallons or more per day, and the average household's leaks waste more than 9,300 gallons a year | VERIFIED | https://www.epa.gov/watersense/fix-leak-week | "The average household's leaks can account for more than 9,300 gallons of water wasted every year and nine percent of homes have leaks that waste 50 gallons or more per day." |
| 2 | the free test that comes first | A meter read before and after a two-hour no-use period settles whether water is moving; a family of four over 12,000 gallons in a winter month likely has a serious leak | VERIFIED | https://www.epa.gov/watersense/fix-leak-week | "If a family of four exceeds 12,000 gallons per month, there could be serious leaks. Check your water meter before and after a two-hour period when no water is being used." |
| 3 | accuracy of acoustic detection | 84.6% correct detection on a 5 mm leak hole, 97.7% at 7 mm, 98% at 10 mm; 324 simulated tests on a real pipeline; 94.1% overall; false alarm rates 3.3%, 0.7% and 0, overall 1.2% | VERIFIED | https://pmc.ncbi.nlm.nih.gov/articles/PMC10465504 | "detection accuracies of 84.6%, 97.7%, and 98% for different leakage diameter settings, i.e., 5 mm, 7 mm, and 10 mm leak hole diameters, respectively, with an overall accuracy of 94.1%, while the false alarm rates are 3.3%, 0.7%, and 0, respectively, as well as an overall of 1.2%." |
| 4 | what the public water benchmark is | A laboratory water testbed of 152.4 mm PVC pipe, 47 m long, leaks down to a 2 mm2 area (orifice about 1.6 mm), deliberate traffic and tool noise, 280 signals of 30 s | VERIFIED | https://pmc.ncbi.nlm.nih.gov/articles/PMC10147960 | "The dataset was generated through controlled leak experiments in a laboratory-scale (lab) water distribution testbed with 152.4 mm diameter PVC pipes and 47 m total pipe length … we created a 2 mm2 leak area … drilling to induce an orifice with a diameter of about 1.6 mm … background noise (traffic and tool noise) … two hundred and eighty signals were recorded" |
| 5 | the listening condition | The hollow leak tone is almost always present in pipes pressurized at 30 psi and above; ambient sewer flow and traffic mask it, and water pooling at the leak site acts as an acoustic insulator | VERIFIED | https://www.gp-radar.com/article/acoustic-leak-detection-how-does-it-work | "because it is almost always present in leaking pipes pressurized at 30 psi and above" / "water pooling around the site of a leak can act as an acoustic insulator and muffles the noise" / "ambient noise that can be caused by active sewer and other water pipes, and traffic rolling over the pipe at the street level" |
| 6 | the fee for a slab listen | Slab leak diagnostic $350–$650, against $150–$300 for a visible leak; a listener localizes a wall or slab leak inside a square foot in 20–40 minutes | VERIFIED (vendor claim) | https://www.fixitreal.com/costs/professional-leak-detection-cost | "Visible or accessible leak — $150–$300 … Slab leak — $350–$650" / "A pro can localize a wall or slab leak inside a square foot with one of these in 20–40 minutes." |
| 7 | the fee, second host, and the cheap test before it | Slab leak detection $175–$400, billed before the repair scope; pressure testing to confirm a supply-line leak $100–$250 | VERIFIED (vendor claim) | https://alertplumber.com/guides/leak-detection-cost | "Slab leak detection — the most complex scenario — runs $175–$400 and always precedes the repair, billed as a separate fee. Pressure testing for supply line integrity runs $100–$250." |
| 8 | provenance of the accuracy study | The 84.6% / 94.1% study is an acoustic pipeline-leak experiment on a real oil-and-gas pipeline, not a house | FLAGGED — the body must say "a pipeline" and must not present it as a residential result | https://pmc.ncbi.nlm.nih.gov/articles/PMC10465504 | "During the transportation of oil and gas pipelines, there are many potential factors that can lead to pipeline leakage" |
| 9 | the two fee bands disagree | $350–$650 (fixitreal) against $175–$400 (alertplumber) are two contractor/marketplace price guides, not a measured market rate | FLAGGED — present as a spread, never as one market price, and label both as published guide prices | sources 6 and 7 | $350–$650 vs $175–$400 |
| 10 | a residential false-negative rate | No source publishes the share of residential slab locates that miss | REMOVED — do not state; the only measured miss rate is the 15.4% at 5 mm on a pipeline | — | — |

## Derived arithmetic the body may perform (and must show)

- 50 gal/day × 365 days = 18,250 gallons a year for the heaviest-decile household leak, against the 9,300-gallon average (source 1).
- Miss rate at 5 mm: 100 − 84.6 = 15.4%, about one in six and a half (source 3).
- Fee against repair: $175 ÷ $5,000 = 3.5%; $650 ÷ $1,500 = 43% (sources 6 and 7; the repair bands are the dig-and-replace and spot-repair ends published beside them).
- Testbed scale: 152.4 mm is a six-inch main; a house supply line is far smaller — stated qualitatively, no invented diameter.

## Notes for the drafter

- The spine is a sequence, not a discovery: free meter test → $100–$250 pressure test that names which system is losing water → $175–$650 listen. Do not reorder it.
- Do not call the detector inaccurate. It is accurate at what it measures; the mismatch is between a controlled testbed and a house.
- The contrarian turn: the water is the cheap part. 18,250 gallons is a rounding error against a $1,500–$5,000 repair, so the fee is buying a smaller hole in the floor, not a water saving.
- Every price is a 2026 published guide price, labelled as such in the sentence.
