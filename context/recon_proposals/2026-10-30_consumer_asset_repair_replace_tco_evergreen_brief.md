# Evergreen Brief: consumer_asset_repair_replace_tco — 2026-10-30
**Archetype:** evergreen
**Vertical:** consumer_asset_repair_replace_tco
**Persona:** systems_tinkerer_pro
**Decision the reader is facing:** Whether to buy ink through an HP Instant Ink tier, keep buying page sets, or replace the machine with a tank printer — priced at the reader's own monthly page volume, because the tier chosen fixes the cost of every page that follows.
**Durability:** The rule survives price changes because it is a method applied to dated list prices: divide each plan's monthly fee by its page cap, then compare that page to a bottle refill's cost per ISO page. Its figures are as of 2026-10-30 (HP Instant Ink plan table and Pay As You Print sets read off the live page; Epson ET-2800 list price and 522 bottle price read off the live pages), and the article dates every price it prints.
**De-dup:** `2026-10-30_your-screen-gap-999-vs-99` is this vertical's nearest prior artifact (same day, also a plan-versus-fee piece) and it priced *repair risk* on a phone — the insured service column against the uninsured ladder — with no consumable, no volume and no machine-purchase alternative in it; this brief prices *consumables per printed page* and turns on a volume threshold (50 pages a month) that a service-fee ladder has no equivalent of. `2026-10-23_why-your-fridge-upgrade-pays-12-50` used the same cost-per-use frame on electricity for an appliance (a $12.50-a-year saving), so the frame is the vertical's, not this piece's; its subject was power draw and a compressor, not ink. Cross-corpus check: `grep -ril "cost per page|Instant Ink|EcoTank|inkjet|toner" published/ context/recon_proposals/` returns nothing, so no other vertical has argued a printer's consumable economics.
**Thesis:** Ink's price per page is set by the capacity you commit to, not by the brand — the same plan family runs from $0.042 to $0.27 a page, the page you print past your cap is priced like the smallest plan in the family, and a $240 tank undercuts every subscription tier above 50 pages a month inside three years.

**Lead:** The vertical's own beat — `primary_angles[1]`, "appliance and espresso-machine cost per use against purchase price, descaling and part replacement cycles" — read as a consumables question, and the persona's `wants` ("tinkering tax audits", "anti-subscription creep"). Two vendors' live price lists state the whole decision without either of them stating the comparison: HP publishes a five-tier monthly ladder, a five-tier yearly ladder and a no-subscription page-set price on one page, and Epson publishes a tank's list price, its ISO page yields and its bottle price on two more. Neither page divides its own price by its own page count.

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | HP — HP Instant Ink plan page (monthly ladder, live table) | https://www.hp.com/us-en/printers/instant-ink.html | 2026-10-30 | 700 pages per month — the largest monthly Instant Ink tier, billed $32.99 a month | vendor claim |
| 2 | HP — HP Instant Ink plan page (monthly ladder, live table) | https://www.hp.com/us-en/printers/instant-ink.html | 2026-10-30 | 8.49 — the 100-page monthly tier costs $8.49 a month | vendor claim |
| 3 | HP — HP Instant Ink plan page (Pay As You Print sets) | https://www.hp.com/us-en/printers/instant-ink.html | 2026-10-30 | 5.49 — a 20-page set under Pay As You Print, the no-subscription option; extra pages on a plan are sold as sets of 10-15 for $2 each | vendor claim |
| 4 | HP — HP Instant Ink plan page (rollover FAQ) | https://www.hp.com/us-en/printers/instant-ink.html | 2026-10-30 | 150 pages — a 50-page plan banks at most 150 rollover pages, three times its monthly allowance | vendor claim |
| 5 | Epson — EcoTank ET-2800 product page | https://epson.com/For-Home/Printers/Inkjet/Epson-EcoTank-ET-2800-Wireless-Color-All-in-One-Cartridge-Free-Supertank-Printer/p/C11CJ66202 | 2026-10-30 | 239.99 — list price of the EcoTank ET-2800; the 522 bottles are rated at 4,500 black and 7,500 colour ISO pages, and the page's promo price is $189.99 through 2026-10-31 | vendor claim |
| 6 | Epson — EcoTank ET-2800 product page (footnote 4) | https://epson.com/For-Home/Printers/Inkjet/Epson-EcoTank-ET-2800-Wireless-Color-All-in-One-Cartridge-Free-Supertank-Printer/p/C11CJ66202 | 2026-10-30 | 125 pages — the "up to 2 years of ink in the box" claim is based on average monthly document print volumes of about 125 pages | vendor claim |
| 7 | Epson — Epson 522 Black Ink Bottle (T522120-S) product page | https://epson.com/For-Home/Ink/Ink-Bottles/T522-EcoFit-Ink-Bottle-Black/p/T522120-S | 2026-10-30 | 17.99 — the 522 black bottle's price, sold against a 4,500-page ISO yield | vendor claim |

## Arithmetic the article performs (recomputed from the rows above, not copied from a draft)

- Subscription cost per page: $1.99/10 = $0.1990, $5.99/50 = $0.1198, $8.49/100 = $0.0849, $16.99/300 = $0.0566, $32.99/700 = $0.0471; yearly $355.99/8,400 = $0.0424.
- Pay As You Print: $5.49/20 = $0.2745 and $19.99/75 = $0.2665 per page — the dearest pages in the family, and the only ones with no subscription.
- Overage page: $2 for a 10-to-15-page set = $0.1333 to $0.2000 a page, i.e. 4.7x the yearly plan's page at the dearest end and priced like the 10-page plan.
- Stepping up instead of overrunning: 100-page ($8.49) to 300-page ($16.99) buys 200 more pages for $8.50 = $0.0425 a page, 3.1x to 4.7x cheaper than an overage page.
- Tank page: $17.99/4,500 = $0.0040 black; a page carrying black plus three colour inks = $0.0040 + 3 x ($17.99/7,500) = $0.0112, i.e. 3.8x cheaper than the cheapest subscription page and 24x cheaper than the dearest Pay As You Print page.
- Three-year comparison at list price ($239.99; included ink treated as 3,000 pages from the 125-pages-a-month basis): 10 pages/month $71.64 vs $239.99 (subscription ahead by $168.35); 50 pages/month $215.64 vs $239.99 (subscription ahead by $24.35, and the tank pays back at month 40); 75 pages/month $305.64 vs $239.99 (tank ahead by $65.65, payback month 28); 300 pages/month $611.64 vs $327.30 (tank ahead by $284.34).

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The ink plan's page price: tier, overage and the tank break-even at 50 pages a month | 9 | 8 | 7 | 9 | 8.3 | **winner** |
| Extended-warranty math versus self-insuring an appliance failure | 9 | 7 | 6 | 8 | 7.6 | dropped — no fetchable primary plan price survived probing, and today's `your-screen-gap-999-vs-99` already prices a plan against a fee ladder |
| Espresso-machine cost per shot against descaling and gasket cycles | 8 | 8 | 5 | 8 | 7.2 | dropped — the descaling and gasket prices live on retailer and repair-shop pages the verifier refuses, so the load-bearing figure had no primary |
| Right-to-repair parts-availability statute (how many years a maker must stock parts) | 8 | 9 | 6 | 7 | 7.6 | dropped — `leginfo.legislature.ca.gov` and the state bill pages are unfetchable to the verifier, leaving the statute quotable only through a mirror that does not carry session laws |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=7 fetched=7 sources=3 hosts=2 decision="sha1:7e915581b7" dedup="matched a prior artifact: 2026-10-30_your-screen-gap-999-vs-" window_days=180 checked_at=2026-10-30T19:38:14+00:00 -->
<!-- evergreen-gate:end -->
