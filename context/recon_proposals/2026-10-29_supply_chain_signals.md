# Signals: supply_chain — 2026-10-29

**Window:** 2026-09-29 → 2026-10-29
**Queries run:** 17 (1 Supply Chain Intel MCP pull, 12 date-agnostic web fan-outs across the vertical's
configured sources and `primary_angles`, 4 primary-page fetches + 4 URL status probes)

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | USPS creates a permanent, weekly fuel surcharge on competitive parcels | https://postalpro.usps.com/fuel-surcharge-faqs | 2026-10-26 | "The USPS is creating a Fuel Surcharge, which will be charged on all competitively priced packages and calculated as a percentage of the base postage. The surcharge will be updated weekly, based on the prices of diesel and jet fuel, as described on the eia.gov website." FAQ dated October 26, 2026. | Parcel price mechanism | 92 |
| 2 | USPS fuel fee starts January 2027, percentage published days ahead, on four products | https://www.supplychaindive.com/news/usps-to-debut-weekly-fuel-fee-in-2027-matching-fedex-ups-practices/872778/ | 2026-10-26 | "The U.S. Postal Service will begin levying a fuel surcharge on various package shipping services starting in January 2027"; applies to USPS Ground Advantage, Priority Mail, Priority Mail Express and Parcel Select; "the fuel surcharge will be calculated as a percentage of the base postage amount"; "The specific percentage will be published three to five days prior to implementation for shipments in which diesel applies, and three to four days before implementation for jet fuel-applicable shipments"; negotiated contracts "may have customized language"; domestic only. | Handoff timeline, contract carve-out | 88 |
| 3 | UPS 3Q26: U.S. domestic revenue up 4.5% on a 6.1% rise in revenue per piece | https://about.ups.com/us/en/newsroom/press-releases/financials/ups-releases-3q-2026-earnings.html | 2026-10-27 | "Revenue increased 4.5%, driven by a 6.1% increase in revenue per piece" (U.S. Domestic: revenue $14,865 M vs $14,220 M, operating margin 6.1%, non-GAAP adjusted 7.0%); fourth-quarter guidance revenue ~$25.7 B; full-year ~$92.6 B. | Price over volume | 90 |
| 4 | UPS call: fuel paid for half the per-piece price gain while daily volume fell 3.3% | https://www.supplychaindive.com/news/ups-gears-up-for-peak-season-with-less-amazon-volume-in-tow/872845/ | 2026-10-27 | "Revenue per piece increased 6.1% despite a 3.3% drop in average daily volume. About half of revenue per piece growth came from base shipping rates and improvements to customer mix, while higher fuel rates made up the remainder, according to Dykes"; UPS projects Q4 U.S. revenue +3% year over year despite a slight Q4 average daily volume decline; "A little more than 100 of UPS' U.S. customers drive about 80% of the company's peak season volume spike each year"; small- and medium-sized business shippers 35.1% of U.S. volume in Q3, up about 240 basis points; about 1,500 drivers accepted buyouts in Q3; plans to hire 100,000 seasonal employees. | Where the price growth came from | 91 |
| 5 | Nvidia reserves capacity at six upstream suppliers | https://nvidianews.nvidia.com/news/nvidia-and-supply-chain-partners-expand-capacity-to-accelerate-ai-infrastructure-buildout | 2026-10-21 | Substrate partners Ibiden, Samsung Electro-Mechanics and Unimicron to increase manufacturing capacity 2.5 times in aggregate over three years; packaging/test partners Amkor, King Yuan Electronics (KYEC) and Siliconware Precision Industries (SPIL); KYEC receives $1.1 billion for new U.S. testing facilities and equipment with high-volume production expected to start in April 2027; SPIL to expand capacity 15-fold by mid-2027 and double again by the end of 2028; Ibiden plant to triple capacity with additional production ramping in the first quarter of 2028; Amkor to raise interposer wafer capacity 300% by the end of 2028. Huang: "Demand is extraordinary. Capacity is the constraint." | Upstream Tier-1 to Tier-N blast radius | 80 |
| 6 | Kroger RFID pilot: 98% read performance across ~1,500 store bakeries | https://www.supplychaindive.com/news/kroger-taps-rfid-computer-vision-data-to-boost-inventory-management/872819/ | 2026-10-27 | "the RFID pilot has produced a 98% read performance, which refers to the number of items the technology can successfully read and recognize, while recording nearly 70% faster inventory counts and a 50% reduction in waste. Kroger plans to roll out the technology across more than 2,300 stores by 2029"; pilot runs across roughly 1,500 stores in the bakery division; AI tool "connects with 20 data pipelines and provides visibility down to the store-item level". | Inventory record accuracy | 74 |
| 7 | USPS board: 3Q26 shipping revenue $8,250 M on 1,554 M pieces | https://about.usps.com/newsroom/national-releases/2026/0807-usps-reports-third-quarter-fiscal-year-2026-results.htm | 2026-08-07 | "Shipping and Packages revenue increased $588 million, or 7.7 percent, on a volume decline of 55 million pieces, or 3.4 percent, compared to the same quarter last year"; Shipping and Packages revenue $8,250 M vs $7,662 M, volume 1,554 M vs 1,609 M pieces; total operating revenue $19,940 M, +6.1%; net loss $2.5 B. Steiner: "All of the statistics and results show that we have yet to cross the point that we should be changing our pricing strategy, and that we have more price to take in the marketplace." | Price over volume (prior quarter) | 86 |
| 8 | USPS's 8% "bridge" charge expires 17 January 2027 | https://about.usps.com/newsroom/national-releases/2026/0325-usps-announces-transportation-related-time-limited-price-change.htm | 2026-03-25 | "an 8 percent increase that would affect base postage prices on the following retail and commercial domestic competitive products: Priority Mail Express, Priority Mail, USPS Ground Advantage, and Parcel Select"; in effect "at midnight Central Time on April 26 and would remain in place until midnight Central Time on Jan. 17, 2027"; "We have steadfastly avoided surcharges and this charge is less than one-third of what our competitors charge for fuel alone"; the increase "will provide a necessary bridge to a permanent mechanism". | The mechanism being replaced | 84 |

## Dating note

Rows 1–6 are dated inside the 30-day window and are the anchor-eligible rows. **Rows 7 and 8 are the
two load-bearing historical records for this story and both fall outside the window** — row 7 is the
agency's third quarter fiscal 2026 release dated 2026-08-07 (quarter ended 30 June 2026), row 8 is the
March 2026 filing notice for the 8% bridge — so they are carried here as **dated background**, each
with its own date stated in the body wherever the figure is used, and neither is treated as an anchor.
Their inclusion follows `radar_30day.md` §3 (every URL a downstream artifact cites must appear in this
file); the story of the window is rows 1–4, the two prior records are what the window's mechanism is
replacing.

## Candidates considered and dropped at Stage 1

- *Rail and truckload 2027 bid round repricing together* (Journal of Commerce rail/intermodal items,
  Werner's "tighter truckload market to boost contract rates in 2027"): the headlines carry no dated
  figure and the underlying articles are paywalled, so no verbatim cell could be established for either
  leg. Dropped as unverifiable rather than weak.
- *Tesla Optimus 1 million units of installed capacity at Fremont* (Supply Chain Dive, 2026-10-28):
  fresh and figure-bearing, but it collides with the 2026-10-28 `warehouse_automation_robotics_capex`
  piece published yesterday on GXO/Agility humanoids and AutoStore — a desk-wide figure and actor
  overlap for the same reading week (`virality_judge` §3.5 desk de-dup).
- *Audi's $4 billion first U.S. plant in Georgia* (Supply Chain Dive, 2026-10-27): a capex
  announcement with a single figure and no operational mechanism; intensity below the bar as a
  standalone and no in-window partner leg.
- *MAAP consolidating three platforms onto one PLM* (Supply Chain Dive, 2026-10-27): vendor-case
  story, no measured outcome.

## Dated background

- USPS third quarter fiscal 2026 results (2026-08-07) — https://about.usps.com/newsroom/national-releases/2026/0807-usps-reports-third-quarter-fiscal-year-2026-results.htm
- USPS 8% time-limited price change notice (2026-03-25) — https://about.usps.com/newsroom/national-releases/2026/0325-usps-announces-transportation-related-time-limited-price-change.htm
- USPS third quarter fiscal 2026 financial conditions and results report (PDF) — https://about.usps.com/what/financials/financial-conditions-results-reports/fy2026-q3.pdf
- USPS remarks by Postmaster General David Steiner, Board of Governors, 2026-08-07 — https://about.usps.com/newsroom/national-releases/2026/0807-remarks-by-postmaster-general-david-steiner-at-the-aug-7-2026-usps-board-of-governors-meeting.htm
- Supply Chain Dive, "Nvidia forges supplier agreements to expand capacity for AI" (2026-10-28) — https://www.supplychaindive.com/news/nvidia-forges-supplier-agreements-to-expand-capacity-for-ai/872780/
- Supply Chain Dive, "How USPS shippers can navigate changes to pricing, parcel measurements" (context on USPS aligning with FedEx/UPS pricing practice) — https://www.supplychaindive.com/news/how-usps-shippers-can-navigate-changes-to-pricing-parcel-measurements/823336/
- UPS Q3 2026 earnings release PDF (investor copy) — https://investors.ups.com/_assets/_82dd7397931c18431557facb5a665332/ups/news/2026-10-27_UPS_Releases_3Q_2026_2172.pdf
- UPS Q3 2026 earnings call slides summary (investing.com) — https://www.investing.com/news/company-news/ups-q3-2026-slides-premium-strategy-lifts-margins-despite-volume-drop-93CH-4976276

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=8 candidates=0 heuristic=- window=2026-09-29..2026-10-29 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->
