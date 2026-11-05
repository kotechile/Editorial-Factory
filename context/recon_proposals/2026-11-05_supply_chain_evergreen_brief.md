# Evergreen Brief: supply_chain — 2026-11-05

**Archetype:** evergreen
**Vertical:** supply_chain
**Persona:** ops_leader
**Decision the reader is facing:** How many pounds of product one 53-foot trailer can legally carry on the routes you run, where to place the pallets so the load does not scale heavy on one tandem while the gross reads legal, and what a scale ticket's tolerance actually permits — the call a planner makes every time a dense SKU is load-planned, and the reason a load that "fits" can still be turned away at the scale.
**Durability:** These are statutory and regulatory ceilings, not market levels, which is why they stay true for years: the Interstate limits come from 23 U.S.C. 127 and the Bridge Gross Weight Formula, and the enforcement floor from 23 CFR 658.17. Figures are as of the 23 U.S.C. 127 text in Cornell LII's current edition and the eCFR's title 23 edition current 11/03/2026. What moves is a state's tolerance practice and permit regime, both named as the reader's own input rather than asserted as a national number.
**De-dup:** `2026-10-29_supply_chain_evergreen_brief.md` is this vertical's nearest prior evergreen artifact (published as `published/2026-10-29_your-carriers-750000-doesnt-cover-cargo.md`), and it answers a different question — which instrument (a carrier's public-liability filing, a broker's surety bond, a cargo policy) pays after a loss, i.e. money after damage. This piece is about whether the load may move at all: the axle and gross ceilings, the bridge formula, and the scale tolerance. The two nearest physical-logistics artifacts are `published/2026-10-22_your-golden-zone-costs-10-miles.md` (pick-face days of supply) and `published/2026-10-15_freight-claim-dies-at-9-months.md` (claim procedure); neither measures trailer weight. A cross-vertical sweep of `published/` and `context/recon_proposals/` for "bridge formula", "tandem axle" and "gross vehicle weight" returns only the 10-29 liability brief's passing mention of a carrier's filing, so no earlier artifact argues this mechanism.
**Thesis:** The 80,000-pound interstate ceiling is not a number you load to — it is what remains after two 34,000-pound tandem caps and whatever the steering axle may legally carry, and the bridge formula lowers the group cap on any axle span that is too short, so the number that turns a load away is a spacing measurement rather than a scale reading.

**Lead:** The founder's own position in `context/growth_os/founder-voice.md` §2 pillar 6 ("the friction point where algorithms hit real-world physics… pallet dimensions", and the note that "if an algorithm ignores driver dwell times, yard congestion, and pallet dimensions, it is just expensive fiction"), the persona's stated want in `context/personas.json` ("physical-to-digital friction fixes", tone "grounded in physical physics"), and `context/growth_os/customer-truth.md` Anecdote 1 for `supply_chain`, where a $6/unit sourcing gap became a $0.80 landed-cost gap only after transit and handling were priced. The specific material is the federal weight architecture: 23 U.S.C. 127's axle and gross ceilings, FHWA's Bridge Gross Weight Formula, and 23 CFR 658.17's enforcement floor and scale allowance — the three documents that decide whether a load plan is legal, none of which appears in any prior artifact this vertical has published.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | 23 U.S.C. § 127(a)(1) — Cornell Legal Information Institute | https://www.law.cornell.edu/uscode/text/23/127 | 2026-11-05 | five axles or more — a State must permit Interstate use by vehicles with twenty thousand pounds carried on any one axle, a tandem axle weight of thirty-four thousand pounds, or a gross weight of at least eighty thousand pounds for vehicle combinations of five axles or more | statute |
| 2 | FHWA — Bridge Formula Weights (Office of Operations) | https://ops.fhwa.dot.gov/freight/publications/brdg_frm_wghts/index.htm | 2026-11-05 | 80,000 pounds — Gross vehicle weight is limited to 80,000 pounds (23 U.S.C. 127), and axles 40 to 96 inches apart (tandem axles) are limited to 34,000 pounds | agency rule |
| 3 | FHWA — Bridge Formula Weights (Office of Operations) | https://ops.fhwa.dot.gov/freight/publications/brdg_frm_wghts/index.htm | 2026-11-05 | 500 pounds — W = 500(LN/(N−1) + 12N + 36), the weight on any group of two or more consecutive axles rounded to the nearest 500 pounds | agency rule |
| 4 | 23 CFR § 658.17(c) — Cornell CFR mirror | https://www.law.cornell.edu/cfr/text/23/658.17 | 2026-11-05 | 20,000 pounds — the maximum gross weight upon any one axle, including any one axle of a group of axles, is 20,000 pounds | regulation |
| 5 | 23 CFR § 658.17(d) — Cornell CFR mirror | https://www.law.cornell.edu/cfr/text/23/658.17 | 2026-11-05 | 34,000 pounds — the maximum gross weight on tandem axles is 34,000 pounds | regulation |
| 6 | 23 CFR § 658.17(g) — Cornell CFR mirror | https://www.law.cornell.edu/cfr/text/23/658.17 | 2026-11-05 | 5 percent — the accuracy of portable scales is generally within 2 or 3 percent of actual weight, but in no case shall an allowance in excess of 5 percent be applied | regulation |
| 7 | 23 CFR Part 658 — eCFR (title 23 current 11/03/2026) | https://www.ecfr.gov/current/title-23/chapter-I/subchapter-G/part-658 | 2026-11-05 | 96 inches — axles whose centres are spaced more than 40 inches and not more than 96 inches apart are a tandem, and the Federal tandem axle weight limit on the Interstate System is 34,000 pounds | regulation |

## Candidate topics considered

| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The trailer's legal payload is a spacing measurement: 34,000 × 2 tandem caps, the bridge formula, and what a scale ticket's tolerance allows | 9 | 10 | 9 | 9 | 9.3 | **winner** |
| The driver's clock as a lane-design constraint: 11 hours of driving inside a 14-hour window, the 30-minute interruption, and why a 600-mile lane is two days | 8 | 9 | 8 | 8 | 8.3 | runner-up — genuinely durable and sourceable (49 CFR 395.3 and 395.1(e) both fetch), but the lever sits with the carrier's dispatch; the shipper's own decision is thinner than the load plan, and the vertical's last four artifacts are already trucking-side |
| Ocean demurrage/detention invoice validity: 46 CFR 541's 30-day issue rule, the required invoice contents, and the certification that the billing party's own performance did not contribute | 10 | 10 | 5 | 9 | 8.6 | dropped — the best-fit topic for this vertical's own `primary_angles` ("demurrage dispute pipelines"), but every load-bearing figure sits in one host: 46 CFR part 541 is reachable on ecfr.gov and its operative numbers are the same "30 calendar days" repeated across 541.7 and 541.8, while 46 CFR 545 (the interpretive rule) fetches with no numeric token at all and fmc.gov's resource pages are unreachable to the verifier. The gate needs ≥ 3 sources on ≥ 2 hosts and the piece would have rested on one number restated |
| LTL freight class and density re-classification: what a reweigh does to a class-based rate | 8 | 8 | 4 | 8 | 6.7 | dropped — NMFC's own classification pages (nmfta.org) are unreachable to the verifier, so the class table has no primary anchor and the topic would rest on reseller explainers |

## Figures the article will compute, and from what

- Steering-axle weight as the remainder: 80,000 − 34,000 − 34,000 = 12,000 pounds, from rows 1 and 2. The familiar 12,000 / 34,000 / 34,000 split is arithmetic, not a rule.
- Bridge formula at a five-axle span: W = 500(1.25L + 96). At L = 51 ft, 79,875 pounds (inside the 80,000 cap); at 45 ft, 76,125; at 40 ft, 73,000. Computed from row 3's own formula, printed with its inputs.
- The 5 percent scale allowance on an 80,000-pound load is 4,000 pounds — the width of the band a portable scale may legally differ by, from row 4.

## Notes and gate rulings

- Row 1 leads on "five axles or more" because 23 U.S.C. 127's operative text writes its ceilings in words ("twenty thousand pounds… thirty-four thousand pounds… eighty thousand pounds"); any cell leading on a digit on that page evidences on the 1975 amendment note instead, which is why the statute row is digit-free and the digit-bearing rows ride on the regulation (rows 4–6), which states the same limits in numerals.
- Rows 2 and 3 share one URL deliberately: the FHWA page carries both the gross ceiling and the formula, and they are different claims.
- 23 CFR Part 658 on ecfr.gov is a single 257 KB page with stray integers throughout; its only cell used here leads on "96 inches", whose window lands in the tandem definition and states the 34,000-pound limit. The eCFR's own enforcement sentence ("no allowance in excess of 5 percent") reads as an amendment note on that page, which is why the scale-allowance row rides on the Cornell mirror of 658.17 instead.
- The article must state the boundary the sources state: these are Interstate System maxima, and states may not enforce lower (23 CFR 658.17(f)); non-Interstate routes, special permits for non-divisible loads (658.17(h)) and state grandfathers are outside the numbers, so the piece may not say "34,000 is the limit" without naming the Interstate.

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=7 fetched=7 sources=4 hosts=3 decision="sha1:9e4fe712fd" dedup="matched a prior artifact: 2026-10-29_supply_chain_evergreen_" window_days=180 checked_at=2026-11-05T18:35:36+00:00 -->
<!-- evergreen-gate:end -->
