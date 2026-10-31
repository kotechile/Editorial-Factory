# Verified Brief: yard_robotics — 2026-10-31

Source of record: `context/recon_proposals/2026-10-31_yard_robotics_evergreen_brief.md` (evergreen gate PASS, rows=7 fetched=7 hosts=4).
Every row below was re-fetched on 2026-10-31 through the same fetch path the gate uses; the Verbatim cell is copied from the retrieved page, not from memory.

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | Contract price | Residential lawn mowing is quoted at $45–$75 per visit, with most homeowners paying $60 | VERIFIED | https://lawnlove.com/blog/lawn-mowing-cost/ | "Lawn mowing costs $45 to $75 per visit, with most people paying $60." (byline: "Updated: October 26, 2026") |
| 2 | Contract scope | The national table is priced for a typical quarter-acre lawn, on data from September 2025 to September 2026 | VERIFIED | https://lawnlove.com/blog/lawn-mowing-cost/ | "The table below offers a snapshot of lawn mowing costs across the country, based on Lawn Love data from September 2025 to September 2026 for a typical 1/4-acre lawn" |
| 3 | Season length — Northeast | The Northeast mowing season runs ~24 weeks, at $49–$77 a week | VERIFIED | https://lawnlove.com/blog/lawn-mowing-cost/ | "Region Typical Mowing Season Weekly Cost Est. Annual Total Northeast ~24 weeks $49–$77 $1,176–$1,848" |
| 4 | Season length — Southeast | The Southeast mowing season runs ~45 weeks, at $46–$72 a week | VERIFIED | https://lawnlove.com/blog/lawn-mowing-cost/ | "Southeast ~45 weeks $46–$72 $2,070–$3,240" |
| 5 | Season length — Midwest / Southwest / West & Northwest | Midwest ~26 weeks ($1,248–$1,820); Southwest ~46 weeks ($1,932–$2,944); West/Northwest ~34 weeks ($1,530–$2,312) | VERIFIED | https://lawnlove.com/blog/lawn-mowing-cost/ | "Midwest ~26 weeks $48–$70 $1,248–$1,820 Southwest ~46 weeks $42–$64 $1,932–$2,944 West/Northwest ~34 weeks $45–$68 $1,530–$2,312" |
| 6 | Annual range | Annual mowing totals run from $1,176 in the Northeast to $3,240 in the Southeast | VERIFIED | https://lawnlove.com/blog/lawn-mowing-cost/ | "Annual totals run from $1,176 in the Northeast to $3,240 in the Southeast." |
| 7 | DIY comparison | A homeowner's own mower costs $135–$3,940 up front, carries $100+ a season of gas, oil, blades and filters, and takes 1+ hour per mow | VERIFIED | https://lawnlove.com/blog/lawn-mowing-cost/ | "DIY Hiring a pro Upfront cost $135 – $3,940 ( lawn mower cost , depending on type) $45 – $75 average per visit Ongoing costs $100+ per season (gas, oil, blades, filters) None Time required 1+ hour per mow, plus maintenance time" |
| 8 | Labour anchor | Landscaping and groundskeeping workers earned a median $18.82 an hour ($39,150 a year) in the 2025 survey | VERIFIED | https://www.onetonline.org/link/summary/37-3011.00 | "Median wages (2025) $18.82 hourly, $39,150 annual" |
| 9 | Machine price — quarter acre | Kress lists its quarter-acre KR161 at $2,799.98, and was selling it at $1,499.99 in a promotion dated to 31 December 2026 | VERIFIED | https://www.kress.com/en-us/robotic-mowers | "Kress RTKⁿ ¼-acre robotic lawn mower KR161 $2,799 .98 Only $1,499 .99" … "Offer valid through December 31, 2026, or while supplies last." |
| 10 | Machine price — one acre | Husqvarna lists the one-acre Automower 420 iQ at $3,299.99 | VERIFIED | https://www.husqvarna.com/us/robotic-lawn-mowers/automower-420-iq/ | "Price from $3,299.99 $3,299.99 MSRP" |

## Derived arithmetic (ours, not a source's — the article must show the formula)

| Figure | Working | Result |
|---|---|---|
| Payback, Northeast, list price | 2,799.98 ÷ 1,176 and ÷ 1,848 | 2.38 years to 1.52 years |
| Payback, Southeast, list price | 2,799.98 ÷ 2,070 and ÷ 3,240 | 1.35 years to 0.86 years |
| Payback, Midwest, list price | 2,799.98 ÷ 1,248 and ÷ 1,820 | 2.24 years to 1.54 years |
| Payback, one-acre machine, Northeast / Southeast | 3,299.99 ÷ 1,176 / ÷ 3,240 | 2.81 years / 1.02 years |
| Payback spread, slowest to fastest season | 2.38 ÷ 0.86 | 2.8× |
| One season of your own mowing, Northeast | 24 weeks × 1 hour × $18.82 | $451.68 |
| One season of your own mowing, Southeast | 45 weeks × 1 hour × $18.82 | $846.90 |
| Machine price in seasons of your own labour | 2,799.98 ÷ 451.68 ; ÷ 846.90 | 6.2 seasons ; 3.3 seasons |
| A single visit in worker-hours | $45 ÷ $18.82 ; $60 ÷ $18.82 ; $75 ÷ $18.82 | 2.4 h ; 3.2 h ; 4.0 h |

## Flags carried to the drafter

- **FLAGGED — the vendor dataset is one marketplace's.** Rows 1–7 all come from a single mowing marketplace's own quote data, published to sell bookings. The article names it as a marketplace's data and never calls it an industry survey. Nothing in the piece should read as "the national average price of mowing"; the claim is "this is what one national booking marketplace publishes, by region".
- **FLAGGED — the monthly average is a different page and a different basket.** The marketplace's pricing page (https://www.lawnlove.com/pricing) carries "The average homeowner spends $150-$200 per month on professional lawn care services". That is a full-service figure annualised over twelve months, and it includes work a mower does not displace. The article uses it only as the wrong denominator to warn against, never as the number to divide by, and never restates it as a mowing bill.
- **FLAGGED — the published totals are quarter-acre totals.** Every price in rows 1–6 is scoped to a typical quarter-acre lawn. The one-acre machine in row 10 is therefore being priced against a bill for a quarter of its rated area; the article says so plainly and does not present the Northeast payback as the number for a one-acre lot.
- **FLAGGED — Kress is mid-promotion.** Row 9 carries both the list price and a dated promotional price. The payback division uses the list price; the promotional price and its 31 December 2026 expiry are stated because they halve every payback number in the piece.
- **REMOVED — the vertical's "$150–250 a month" angle wording.** No fetchable source prices a quarter-to-one-acre mowing contract at that band; the only year-round monthly figure found is the full-service average above. The band does not appear in the article.
- **REMOVED — "a robot mower saves X hours a year" as a sourced claim.** The "1+ hour per mow" line is the source's DIY estimate, not a measured study of robot owners; the article multiplies it out and labels the result as its own arithmetic.
