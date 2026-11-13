---
title: "Your Collar Kills the 12-Month Clock"
vertical: concentrated_equity_portfolio_capital
kind: evergreen
archetype: evergreen
evergreen: true
persona: financial_architect
one_big_thing: "A collar on employer stock is a short sale wrapped in a straddle — the put restarts the long-term holding clock on shares under a year old, the put's loss is deferred against the stock's own unrealised gain, and the dividend drops out of the qualified bucket for the whole stretch the downside is covered."
date: 2026-11-13
slug: your-collar-kills-the-long-term-clock
meta_title: "Your Collar Kills the 12-Month Clock"
meta_title_source: "derived_from_title"
meta_description: "A collar is what a broker proposes when a holder with one large position says: protect me without selling. It means buying a put and selling a call either…"
meta_description_source: "derived_from_lead"
---

<!-- lead -->
A collar is what a broker proposes when a holder with one large position says: protect me without selling. It means buying a put and selling a call either side of today's price, so the position stops falling and stops rising. The pitch leaves out one thing. The Internal Revenue Service treats that put as a short sale of the shares underneath it, so a position eleven months into its holding period can go back to month zero with no share changing hands [2]. The collar kills the 12-month clock you had nearly finished.

<!-- tldr -->

## At a glance

- **The shift:** A put is a short sale, so covering a position under a year old restarts its holding clock.
- **The number:** 12 months, counted again from the day the put closes.
- **The risk:** The same structure defers the put's loss against the stock's unrealised gain.

<!-- tension -->

## Why the code sees a sale

The code reaches a collar through a definition rather than a description. Two positions form a straddle when holding one cuts the loss risk of the other [1]. Stock joins that definition when a position on the same shares offsets it, which a put on those shares does [1]. A collared holding of a listed stock is therefore straddle property. The arithmetic that follows is the part holders miss, and I read the statute twice before a worked example made it concrete. A loss on one leg is recognised only above the unrealised gain in the other, and the rest carries into the next year [1].

There is an exit from those rules, and it is narrower than the folklore about covered calls. A straddle made only of qualified covered calls and the stock they cover, standing alone, is not treated as a straddle at all [1]. A qualified covered call must trade on an exchange and must be written more than 30 days before it expires [1]. It must also stay out of deep-in-the-money territory, and must come from someone other than an options dealer [1]. A collar breaks the standing-alone clause, because the put makes the straddle larger than the call-and-stock pair [1]. Once the exemption is gone, interest and carrying charges stop being deductible and go into basis instead [7].

The tax agency says the same thing in plainer words. Buying a put is generally treated as a short sale, and its exercise, sale or expiry closes that short sale [2]. Where the stock has been held for a year or less, the holding period begins again on the earliest of four dates: the sale of the stock, the exercise of the put, the sale of the put, or its expiry [2]. The regulation behind the rule exempts only an option acquired on the same day as the shares it is identified against [3]. The statute adds that where the shares had been held a year or less, the gain on closing that short sale is short-term, however long they sat in the account [4].

## By the numbers

- **$2,250 deductible:** what the publication's own straddle example leaves of a closed loss, before the rest is carried forward [2].
- **$125 benchmark:** the second-highest strike below the stock price in the publication's covered-call example [2].

<!-- tactical-insight -->

## What the desks actually do

The term limit decides whether a structure is sound or decorative. The rules require a qualified covered call to expire within 12 months of the day it is written, and that requirement has applied since July 28, 2002 [2]. The two-year call that makes a long collar look cheap is therefore not a qualified covered call at all. I keep coming back to how quietly that disqualifies the popular structure. The strike draws the attention; the expiry decides the exemption.

The benchmark ladder is the other half. Above a strike of $50 and a term beyond 90 days, the benchmark is the second-highest listed strike below the stock price [1]. Below a stock price of $150, the benchmark can sit no lower than $10 under it [1]. The publication's example writes a September $120 call on stock that closed at $130.25, and lands the benchmark on $125 [2]. Any strike under that line turns the call into a deep-in-the-money option and takes it out of the exemption [1].

What desks around big single-stock positions do follows from those rules. Puts go on lots already past the statutory year, where a restart has nothing left to take. Others use expiries short enough that a restart costs a quarter rather than a year. Some skip the put and write the call alone, which keeps the exemption and gives up the upside without buying protection [1]. My read is that a collar is a liquidity tool for a holder who has priced the tax cost, not a way around it.

<!-- nuanced-takeaway -->

## The catch

The dividend is where the structure costs money the statement never shows. A dividend stops being qualified income on a share whose holding period under the distribution rules is not met [5]. For an individual those rules use 60 days inside a 121-day window [5]. The same rules cut the holding period for every stretch in which the holder can sell the shares, with a qualified covered call as the one carve-out [6]. A covered position collects the dividend and has it taxed as ordinary income instead.

The honest limit is that none of this touches a position already past the year. Those shares keep their treatment, the loss is still deferred, and the dividend cut still bites if the stock pays one. What moves is the size of the cost, not its direction, and the direction is the same for any covered position. For a holder weighing a partial sale against a collar, [the hold-versus-sell model](/calculators/rsu-hold-vs-sell/) prices the sale side on the same after-tax basis.

The part I find hard to square is the asymmetry at the end. The structure that keeps the exemption gives up the upside and buys no protection. The structure that buys protection gives up the exemption. A collar sells part of the future gain and shortens your own clock, and it is priced as neither.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: none — no live page on this site scored for this topic -->
<!-- internal-links:end -->

## Sources

- [1] Cornell Legal Information Institute, "26 U.S.C. § 1092 — Straddles" — https://www.law.cornell.edu/uscode/text/26/1092
- [2] Internal Revenue Service, "Publication 550 (2025), Investment Income and Expenses — Puts and calls; Straddles" — https://www.irs.gov/publications/p550
- [3] Code of Federal Regulations, "26 CFR § 1.1233-1 — Gains and losses from short sales, options to sell" (title 26 current as of 11/10/2026) — https://www.ecfr.gov/current/title-26/section-1.1233-1
- [4] Cornell Legal Information Institute, "26 U.S.C. § 1233 — Gains and losses from short sales" — https://www.law.cornell.edu/uscode/text/26/1233
- [5] Cornell Legal Information Institute, "26 U.S.C. § 1(h)(11) — Dividends taxed as net capital gain" — https://www.law.cornell.edu/uscode/text/26/1
- [6] Cornell Legal Information Institute, "26 U.S.C. § 246(c)(4) — Holding period reduced where risk of loss diminished" — https://www.law.cornell.edu/uscode/text/26/246
- [7] Cornell Legal Information Institute, "26 U.S.C. § 263(g) — Certain interest and carrying costs in the case of straddles" — https://www.law.cornell.edu/uscode/text/26/263
