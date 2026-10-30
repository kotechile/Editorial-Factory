# Verified Brief: consumer_asset_repair_replace_tco — 2026-10-30 (evergreen)
**Brief it verifies:** `2026-10-30_consumer_asset_repair_replace_tco_evergreen_brief.md` (gate PASS, 7 rows, hosts epson.com + hp.com)
**Topic:** what a printed page costs in an ink subscription, in overage, and on a tank printer.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | Subscription ladder | The five monthly Instant Ink tiers are 10, 50, 100, 300 and 700 pages a month | VERIFIED | https://www.hp.com/us-en/printers/instant-ink.html | "Best for light printing Includes 10 pages per month 10 pages per month $1.99/mo … Best for small business Includes 700 pages per month 700 pages per month $32.99/mo" |
| 2 | Subscription ladder | The 100-page monthly tier costs $8.49 | VERIFIED | https://www.hp.com/us-en/printers/instant-ink.html | "Best for home use Includes 100 pages per month 100 pages per month $8.49/mo" |
| 3 | Subscription ladder | The yearly ladder's largest tier is 8,400 pages for $355.99 | VERIFIED | https://www.hp.com/us-en/printers/instant-ink.html | "Best for small business Includes 8400 pages per year 8400 pages per year $355.99/y" |
| 4 | Overage | Extra pages past a plan's cap are sold as sets of 10 to 15 pages for $2 each | VERIFIED | https://www.hp.com/us-en/printers/instant-ink.html | "Need more pages? Buy extra sets of 10–15 pages for just $2 each." |
| 5 | No-subscription price | Pay As You Print sells 20-page sets at $5.49 and 75-page sets at $19.99 | VERIFIED | https://www.hp.com/us-en/printers/instant-ink.html | "20-Page Set $5.49 75-Page Set $19.99 Only pay for what you print." |
| 6 | Rollover cap | Unused pages roll over at most three times the monthly allowance, and the yearly plan rolls nothing | VERIFIED | https://www.hp.com/us-en/printers/instant-ink.html | "Ink plans can roll over 3x the number of pages in your plan (Example: 150 pages if on the 50-page plan)." / "For Yearly Plan, unused pages do not roll over to the next year and are not available for future use." |
| 7 | Machine capital | The plan needs an eligible HP printer, whose firmware tracks ink levels and triggers delivery | VERIFIED | https://www.hp.com/us-en/printers/instant-ink.html | "HP Instant Ink is an ink delivery service for eligible HP printers in which the printer monitors ink levels and automatically ships new ink cartridges before you run out." |
| 8 | Tank list price | The EcoTank ET-2800 lists at $239.99; the page's own promo price is $189.99, valid 2026-10-25 to 2026-10-31 | VERIFIED | https://epson.com/For-Home/Printers/Inkjet/Epson-EcoTank-ET-2800-Wireless-Color-All-in-One-Cartridge-Free-Supertank-Printer/p/C11CJ66202 | "Our Price: $239.99 After 21% savings: $189.99" / "Offer Valid from October 25, 2026 to October 31, 2026 while supplies last." |
| 9 | Tank yields | The 522 bottles are rated at 4,500 black and 7,500 colour ISO pages | VERIFIED | https://epson.com/For-Home/Printers/Inkjet/Epson-EcoTank-ET-2800-Wireless-Color-All-in-One-Cartridge-Free-Supertank-Printer/p/C11CJ66202 | "Replacement Ink Yield ISO Pages: T522 — Black: 4,500, Color: 7,500" |
| 10 | Included ink | "Up to 2 years of ink in the box" is based on about 125 pages a month | VERIFIED | https://epson.com/For-Home/Printers/Inkjet/Epson-EcoTank-ET-2800-Wireless-Color-All-in-One-Cartridge-Free-Supertank-Printer/p/C11CJ66202 | "Includes up to 2 years of ink in the box" / "4 Based on average monthly document print volumes of about 125 pages." |
| 11 | Bottle price | One 522 black bottle costs $17.99 | VERIFIED | https://epson.com/For-Home/Ink/Ink-Bottles/T522-EcoFit-Ink-Bottle-Black/p/T522120-S | "Epson 522, Black Ink Bottle Ink Code: T522120-S Our Price: $17.99" |
| 12 | Yield caveat | Yields are ISO-pattern ratings taken under Epson's methodology, and fall when printing is infrequent or uses one colour | VERIFIED | https://epson.com/For-Home/Ink/Ink-Bottles/T522-EcoFit-Ink-Bottle-Black/p/T522120-S | "Replacement ink bottle yields based on the ISO/IEC 24712 pattern with Epson's methodology … Yields may be lower when printing infrequently or predominantly with one ink colo" |
| 13 | Promo scope | The $189.99 price is a promotion, not the machine's list price, so the article must do its arithmetic on $239.99 and name the promo separately | FLAGGED | https://epson.com/For-Home/Printers/Inkjet/Epson-EcoTank-ET-2800-Wireless-Color-All-in-One-Cartridge-Free-Supertank-Printer/p/C11CJ66202 | "Offer Valid from October 25, 2026 to October 31, 2026 while supplies last." |
| 14 | Scope caveat | The tank comparison assumes the reader is buying a machine; an owner of an eligible HP printer already has the capital in place, so for that reader the honest comparison is subscription against Pay As You Print | FLAGGED — arithmetic of the run, not a source claim | https://www.hp.com/us-en/printers/instant-ink.html | "an ink delivery service for eligible HP printers" |

## Arithmetic (recomputed in the run from rows 1–11; no derived figure is quoted from a draft)
- Subscription per page: $1.99/10 = $0.1990; $5.99/50 = $0.1198; $8.49/100 = $0.0849; $16.99/300 = $0.0566; $32.99/700 = $0.0471; $355.99/8,400 = $0.0424.
- Pay As You Print: $5.49/20 = $0.2745; $19.99/75 = $0.2665.
- Overage: $2/10 = $0.2000; $2/15 = $0.1333. Overage ÷ yearly page ($0.0424) = 4.7x at the dearest end.
- Step-up: ($16.99 − $8.49)/200 = $0.0425 a page, against $0.1333–$0.2000 for an overage page.
- Tank: $17.99/4,500 = $0.0040 black; $0.0040 + 3 × ($17.99/7,500) = $0.0112 for a page carrying black plus three colours; $0.0424/$0.0112 = 3.8x.
- Overage vs black bottle page: $0.2000/$0.0040 = 50x.
- Three-year comparison at $239.99 with 3,000 included pages (125 pages/month × 24): 50 pages/month $5.99 × 36 = $215.64 vs $239.99 — subscription ahead by $24.35, tank payback month 40; 75 pages/month $8.49 × 36 = $305.64 vs $239.99 — tank ahead by $65.65, payback month 28; 100 pages/month $305.64 vs $246.71 — tank ahead by $58.93; 300 pages/month $611.64 vs $327.30 — tank ahead by $284.34.

## Rules handed to the drafter
- One money figure family per section: the lead carries the ladder table and the machine's list price; the tension/numbers section carries the derived per-page rates and the three-year totals; the tactical and catch sections carry **no dollar values at all** (page counts, months and ratios only), so `article_shape`'s two-section limit holds.
- Do not state the promo price as the machine's price. Do not present the tank's page as typical: it is an ISO-pattern page from a bottle's rated yield, and row 12 is the caveat that belongs in the catch.
- The overage price must always be printed as a range ($0.13 to $0.20), never as the single worst case in a way that reads as the plan's rate.
- No hands-on or tested claim: this desk has no printer, and none of the sources reports a measured page count from a lab run.
