---
title: "64% of Your Buffer Isn't Demand"
vertical: meio_working_capital_tco
kind: evergreen
archetype: evergreen
evergreen: true
persona: ops_leader
one_big_thing: "The safety-stock sum splits into a demand term that grows with the lead time and a supplier term that grows with its square, so on a two-week lane with a one-day delivery swing the supplier carries 64% of the buffer's variance; halving that swing cuts the buffer 27.9% while halving forecast error cuts 14.5%, and shortening the lead time without tightening the swing buys only 9.4%."
date: 2026-11-09
slug: 64-of-your-buffer-isnt-demand
meta_title: "64% of Your Buffer Isn't Demand"
meta_description: "A one-day delivery swing on a two-week lane carries 64% of the safety buffer's variance, so the lever that moves it is the supplier's clock, not the forecast."
---

<!-- lead -->
A one-day swing in a supplier's delivery date puts 64% of a two-week lane's safety buffer on the supplier. The other 36% sits in demand [1]. Variance here means how widely the number swings around its average, and the split decides which lever pays: halving the delivery swing takes 27.9% off the buffer, while halving the forecast error takes 14.5% [2]. Most planning models cannot see the choice. They hold lead time at one fixed number and park every bit of uncertainty in demand [3].

<!-- tldr -->
## At a glance

- **The shift:** Your buffer splits into demand variance and delivery variance, and delivery grows with lead time squared [2].
- **The number:** 27.9% — the buffer a halved delivery swing removes, against 14.5% for halved forecast error.
- **The risk:** Below a service level above 50%, a tighter swing raises the buffer instead [1].

<!-- tension -->
## Why a day outweighs a fifth

The safety-stock sum is one square root over two terms. One term is the demand swing scaled by the lead time. The other is average daily demand scaled by the delivery swing, and that one carries an extra lead time [2]. That extra multiplication is what lifts a delivery swing above a demand swing that looks larger as a percentage.

Stated in like units, the effect gets sharper. A delivery swing measured as a share of the average lead time gets multiplied by the square root of that lead time before it competes with the demand swing [3]. On a five-day lane with a one-day swing, the supplier term is 83.3% of the value under the root [2]. On a twenty-day lane with a five-day swing it is 96.9% [4].

That is why the published advice keeps contradicting itself. Set the two terms equal and the crossover is one ratio: the delivery swing as a share of the lead time, against the demand swing as a share of daily volume divided by the square root of the lead time. On the two-week lane, a swing wider than three-quarters of a day has already overtaken a demand swing of a fifth of volume. A supplier that misses its quoted date by a day is past that line.

The peer-reviewed result complicates the advice rather than settling it. Chopra, Reinhardt and Dada show that the usual shortcut fails in a band above a 50% service level [1]. They find a threshold above that figure, and below it a tighter swing raises the reorder point. A shorter lead time is then the right lever, and the tighter swing is not [1]. What I find hard to square is how often the tighter-swing advice gets repeated without that condition attached.

A plainer test says the same thing. Take the two-week lane down to one week and leave the one-day swing alone; the buffer falls 9.4%, less than halving the forecast error buys [2]. A faster supplier that is just as erratic is barely a cheaper supplier. The same absolute wobble now fills a bigger share of a shorter window. The formula pages usually show the demand-only version first, and that is the one most models run [3].

## By the numbers

- **181 units — the combined formula:** 100 units a day on a five-day lane, a 20-unit demand swing and a 1-day delivery swing [2].
- **9.4% — half the lead time:** the buffer a two-week lane sheds when it shortens to one week and the delivery swing stays a day.
- **$5,712 — the tighter window:** what one stock item saves when a twenty-day lane's delivery swing narrows from five days to two [4].

<!-- tactical-insight -->
## Where the receipt file comes in

Measurement is the part that is not in the planning system. A planning master stores one lead time per item. So the delivery swing a buffer really depends on stays hidden until someone joins purchase-order issue dates to dock receipts [2]. What I keep circling is how cheap that join is next to the software projects teams buy to attack the same inventory.

Once the swing is measured, the equation ranks the lanes without much argument. Where the supplier term wins, the work sits on the delivery clock: confirmed ship dates, a booked collection slot, a scorecard built on the swing rather than the average. Where demand wins, forecast work earns its money. A two-week lane with a disciplined carrier is a different business from an ocean lane with a wobbly one. The pooling argument in [four warehouses halve stock](/four-warehouses-halve-stock/) decides where a buffer sits; this ratio decides what the buffer is made of before anyone moves it.

<!-- nuanced-takeaway -->
## The catch

The equation assumes the two swings move separately and the service target holds still. Under a port strike or a parts shortage neither holds. The delivery swing widens exactly when demand shifts, and the two terms stop adding under a square root [2]. The threshold result is the other limit: where the reversal begins depends on the shape of the lead-time spread, so it is a real warning and not a fixed number [1]. And the buffer is not the whole bill. Expedited freight, write-offs and the working capital behind the stock sit outside this math, which is why the ratio ranks levers rather than settling a budget.

The honest use is narrower than the sales pitch on either side. It tells you which of three levers has room left on a lane — a shorter lead time, a tighter delivery swing, or a better forecast — and it tells you when the answer flips. It does not tell you what service level the lane deserves. That is a margin question, not a variance one.

## Sources

- [1] Chopra, Reinhardt & Dada, "The effect of lead time uncertainty on safety stocks", Decision Sciences 35(1), 2004 — https://pure.johnshopkins.edu/en/publications/the-effect-of-lead-time-uncertainty-on-safety-stocks-4
- [2] PulpWMS, "Safety Stock: Formula, Calculation and Best Practices" — https://blog.pulpowms.com/safety-stock
- [3] Sevenledger, "Safety Stock: The Formula, the Mistakes, and How to Set It Right" — https://www.dhoon.co/blogs/safety-stock-formula
- [4] Lead Time Calculator, "How Lead Time Variance Inflates Safety Stock", September 14, 2026 — https://leadtimecalculator.net/blog/lead-time-variance-safety-stock
