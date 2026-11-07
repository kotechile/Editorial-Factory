---
title: "Your Peso Upside Is Billed: 2.28%"
vertical: supplier_risk_reshoring_decision
kind: evergreen
archetype: evergreen
evergreen: true
persona: ops_leader
one_big_thing: "The peso slide a Mexico business case counts as upside is already billed into the contract: a twelve-month forward prices the peso 2.28 percent weaker than spot because Mexican rates sit above dollar rates, so the honest budget rate is the forward — and the duty on a peso invoice is converted at a third rate, the quarterly one Customs certifies."
date: 2026-11-07
slug: your-peso-upside-is-priced
meta_title: "Your Peso Upside Is Billed at 2.28%"
meta_description: "A twelve-month peso forward already bills the slide a Mexico case counts as upside, and Customs converts the duty on a peso invoice at a separate quarterly rate."
---

<!-- lead -->
A twelve-month forward prices the peso at 19.0164 to the dollar, and spot is 18.5922. That 2.28 percent slide is the upside your Mexico case counts on, and it is already billed in the contract you can buy today. No bank is handing out a discount. The price follows the gap between what Banco de México pays on pesos and what your dollars earn, because a bank that holds pesos for a year earns the peso rate and gives up the dollar rate. Budget at spot and the landed-cost case rests on a rate nobody will trade at for a payment a year out.

<!-- tldr -->
## At a glance

- **The shift:** The peso slide is sold forward, not left for the buyer to win.
- **The number:** 2.28 percent is how much weaker the peso trades twelve months out.
- **The risk:** A model built on spot prices next year's invoice at a rate no bank will quote.

<!-- tension -->
## Where the forward price comes from

A forward is a contract to buy pesos later at a price fixed now. The bank holding those pesos earns the peso rate and gives up the 3.88 percent your dollars would otherwise earn [2]. The forward therefore leans toward whichever currency pays more, and with the peso rate at 6.25 percent that lean is a weaker peso [3].

Nothing in that price is a forecast a strategist made. If the forward drifted away from the two money rates, a bank could borrow dollars, buy pesos at spot, lend them out, and sell the pesos forward for a profit with no risk. That trade is what holds the price to the two rates.

When a supplier invoices in pesos, Customs does not convert at your bank's rate. Section 159.34 of title 19 in the federal code sets the order: the quarterly rate Customs certifies applies to every export date inside that quarter, and a daily rate replaces it only when the two differ by five percent or more [4]. That rule has not been rewritten since 1981 [4].

| Rate on one peso invoice | Who sets it | What it fixes |
|---|---|---|
| Spot | the market, that day | what a dollar buys today |
| Twelve-month forward | the gap between the two money rates | what the purchase costs next year |
| Certified quarterly rate | Customs, each quarter | the dollar duty on the invoice |

So the price you pay and the duty you owe can be converted at different rates, and the dollar duty is not a fixed share of the dollar cost. My read: the duty line needs its own rate cell in the model, not the exchange rate typed into the price column.

## By the numbers

- **6.25 percent — Peso policy rate:** The leg that pushes the forward weaker than spot [3].
- **18.5922 pesos — Spot rate:** What one dollar bought on 30 October, against 19.0164 in the twelve-month contract [1].
- **$223,059 — Forward saving:** What the weaker forward takes off a $10,000,000 peso bill converted at spot [1].

<!-- tactical-insight -->
## Where the currency actually bites

The exposure that lands on a plant is not annual, it is per cycle, and a shorter cycle carries less of it. On a $1,000,000 peso purchase held 42 days, the drift the forward implies is about $2,625; held four days, it is $250, which is roughly the transit gap between a Southeast Asian port and Monterrey in our own field work.

Put that beside the duty on the same purchase, charged at the rate the reader's own tariff line sets, and the currency case for nearshoring shrinks to noise. The [landed-cost comparison that put Mexico ahead of China](/the-sticker-price-lies-why-mexico-beats-china-on-total-landed-cost/) carried freight, duty and travel, and the exchange rate was one column in it, which is about right.

What I watch is where treasury sets the budget rate. The desks that get this right set it at the forward and buy contracts in tranches against the payment schedule, so the rate is known before the order is signed. The desks that get it wrong use the spot print from the morning the budget was built, then explain the gap in a quarterly review.

<!-- nuanced-takeaway -->
## The catch

A forward does not insure you against a peso crash, and it does not save you 2.28 percent against doing nothing. It fixes the rate at the market's own estimate, which means the crash case is inside the price you paid. What a hedge removes is variance, and variance is what the board asks about when a plan misses.

A dollar invoice looks like the simpler answer, and it is the dearer way to buy the same cover. The supplier's dollar price carries the same rate gap plus whatever the supplier pays to hedge, and the next contract re-prices it. My read, held loosely: whoever carries the peso, you are paying for it, and only one of the two ways shows that cost on your own books.

The limit is the arithmetic itself. A bank quotes a little worse than the rate the two money rates imply, peso rates can move the week you sign, and a duty converted at the quarterly rate can sit up to five percent away from the rate on your invoice. The rate you can trade at is the only one worth budgeting; the spot print is a price for people paying today.

## Sources

- [1] Federal Reserve Board, "Foreign Exchange Rates — H.10 Weekly", release dated 2 November 2026, Mexico peso at 18.5922 for 30 October 2026 — https://www.federalreserve.gov/releases/h10/current/
- [2] Federal Reserve Board, "H.15 Selected Interest Rates", release dated 6 November 2026, federal funds (effective) at 3.88 percent for 5 November 2026 — https://www.federalreserve.gov/releases/h15/
- [3] countryeconomy.com, "Mexico — key rates", Banco de México key rate cut 0.25 percentage points from 6.50 percent to 6.25 percent, November 2026 — https://countryeconomy.com/key-rates/mexico
- [4] U.S. Code of Federal Regulations, title 19, section 159.34 "Certified quarterly rate" (quarterly rate for any export date in the quarter; daily rate when the two differ by 5 percent or more; last amended T.D. 81-117, 46 FR 24944, May 4, 1981), eCFR edition current as of 2026-11-06 — https://www.ecfr.gov/current/title-19/section-159.34
