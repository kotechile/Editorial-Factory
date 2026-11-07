---
title: Your Cheap Board Now Costs $385
vertical: personal_microeconomics_tinkering_tax
kind: news
synthesis: true
sources:
  - https://support.spotify.com/us/article/family-address-verification
  - https://www.raspberrypi.com/news/price-rises-for-some-16gb-raspberry-pi-products/
persona: systems_tinkerer_pro
one_big_thing: "The informal half of a cheap stack — an unenforced household rule and unused memory headroom — is being priced, so the audit now carries a check line and a capacity line."
date: 2026-11-07
slug: your-cheap-board-costs-385
meta_title: "Your Cheap Board Now Costs $385"
meta_title_source: "derived_from_title"
meta_description: "The 16-gigabyte Raspberry Pi 5, long the cheap board for a home server, now costs $385 after its maker ran short of the memory chips the board needs."
meta_description_source: "derived_from_lead"
---

<!-- lead -->
The 16-gigabyte Raspberry Pi 5, long the cheap board for a home server, now costs $385 after its maker ran short of the memory chips the board needs [1]. Spotify's family plan now checks where members live. Anyone who cannot prove they share the manager's address loses the plan, then faces a 12-month lock-out from shared plans [2]. Neither company changed a rate it had already quoted. Both put a price on something that used to be free: the friend who was never quite in the household, and the memory bought just in case.

<!-- tldr -->
## At a glance

- **The shift:** Two vendors stopped absorbing the informal half of a deal and priced it.
- **The number:** $385, the 16-gigabyte Pi 5's price after an $80 rise.
- **The risk:** A failed household check locks a member out of shared plans for 12 months.

<!-- tension -->

## What was free is now invoiced

Spotify's household rule is old; the checking is what arrived this month. Family plans have always been sold to "up to 6 family members residing at the same address" [3]. On 15 October, as Ars Technica reported, Goldman Sachs told clients that "a meaningful share of family plan users are not actual household members" and called tighter checking "additional monetization upside" because enforcement had been "minimal in practice" [4]. The help page now sets the order: seven days from the email, a scan in person if the address does not check out, then a 12-month bar on any other shared plan [2].

Raspberry Pi told the same story with memory instead of addresses. The board launched at $120 in January 2025 [9]. The moves since then:

| Product | Date | Price change |
|---|---|---|
| 2-gigabyte Raspberry Pi 4 | Oct 1, 2026 | $12.50 rise to $67.50 [5] |
| 2-gigabyte Raspberry Pi 5 | Oct 1, 2026 | $12.50 rise to $77.50 [5] |
| 16-gigabyte Raspberry Pi 5 | Nov 2, 2026 | $80 rise [1] |
| Raspberry Pi 500+ (same memory, drive and keyboard) | Nov 2, 2026 | held price [1] |

Eben Upton's post gives the reason plainly: no second source for 16-gigabyte memory, plus shortages of other parts [1]. It also tells buyers to check what they run before paying for headroom [1].

Neither company is doing anything exotic. A vendor can carry a quiet discount while it stays small. It cannot carry it once an analyst writes down that the discount is large, or once a part inside the product gets scarce. My read is that pricing it lands on whoever was quietly relying on the gap.

A household of six splits the family rate to about $3.67 a head [3]. A member who fails the check falls back to the individual plan. Not everyone it catches is freeloading: the adult child at university, the partner who works away, and the sibling sharing a flat are the cases Ars Technica raised when the prompts began [4]. The hardware side has the same shape. The buyer who paid for 16 gigabytes so as not to touch the box again absorbs the shortage, while the 2-gigabyte board that does the actual job moved up in price.

## By the numbers

- **$307.50 — the high-density premium:** what fourteen extra gigabytes cost over the 2-gigabyte Pi 5 (desk arithmetic).
- **$111.90 a year — the demotion penalty:** the gap between the $12.99 individual plan and a six-way split of the $21.99 family rate (desk arithmetic).

<!-- tactical-insight -->

## Where the invoice lands next

Not every vendor is making this trade. Home Assistant shipped its largest release this week and folded the community store into the product [7]. Its notes state that "Everything in the Marketplace is free, and that will not change" [7]. That is the same fortnight and the opposite decision, which is the useful part: the pattern is a choice, not a law of the market.

Inside Raspberry Pi's own price list the gap is now visible. The bare board costs more than the all-in-one that carries the same memory, a drive and a keyboard [6]. A buyer at this price pays for the part that is scarce, not the part that is useful, and the vendor has said so in its own advice [1].

The memory market is set elsewhere. TrendForce expects memory contract prices to rise 10–15% this quarter as suppliers favor server parts over consumer ones [8]. Upton calls the conditions "difficult but ultimately temporary" and promises to roll the increases back when memory costs fall [1]. The part I keep circling is that a household does not get to wait for that cycle. The address check runs in days and the memory cycle runs in quarters, so the deal now carries both.

<!-- nuanced-takeaway -->

## The catch

Two vendors are not a trend, and what connects them is a pricing move, not a shared cause. Spotify did not raise its fee; it enforced a term that was always there, and the lock-out applies to joining another shared plan, not to keeping an account. Raspberry Pi did not change its model; it passed on a parts cost the company says is temporary, and 16 gigabytes buys real headroom when a box runs several virtual machines. Nor does the check catch only people bending the rule: a travelling spouse or a student living away will fail a test built for households. What I keep coming back to is the same cost-per-use math this desk already runs on [an espresso machine](/calculators/coffee-arbitrage/), where a bigger cost up front meets a smaller one each time and the answer tracks how many cups you make. What changed this fortnight is that two inputs stopped being free to leave blank: how much you use, and whether you can prove where you live.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "Is a $3,000 Espresso Maker Machine Worth It?" -> /is-a-3000-espresso-maker-machine-worth-it/ [same site (giniloh.com); topical overlap: costs, home, maker] Link "Is a $3,000 Espresso Maker Machine Worth It?" in the section where the article touches costs, home, maker. -->
<!-- internal-link hint: "Pi 5 Jumps $12.50: Older Kit Is Your Cheap Upgrade" -> /pi-5-price-jump-older-kit-wins/ [same site (giniloh.com); topical overlap: cheap, home, raspberry] Link "Pi 5 Jumps $12.50: Older Kit Is Your Cheap Upgrade" in the section where the article touches cheap, home, raspberry. -->
<!-- internal-link hint: "Home Assistant Renamed Its Cloud" -> /home-assistant-cloud-rename-hardware-rent/ [same site (giniloh.com); topical overlap: home, maker] Link "Home Assistant Renamed Its Cloud" in the section where the article touches home, maker. -->
## Related reading

- [Is a $3,000 Espresso Maker Machine Worth It?](/is-a-3000-espresso-maker-machine-worth-it/)
- [Pi 5 Jumps $12.50: Older Kit Is Your Cheap Upgrade](/pi-5-price-jump-older-kit-wins/)
- [Home Assistant Renamed Its Cloud](/home-assistant-cloud-rename-hardware-rent/)
<!-- internal-links:end -->

## Sources

- [1] Raspberry Pi, "Price rises for some 16GB Raspberry Pi products", 2026-11-02 — https://www.raspberrypi.com/news/price-rises-for-some-16gb-raspberry-pi-products/
- [2] Spotify Support, "Address and verification for Family plan", checked 2026-11-07 — https://support.spotify.com/us/article/family-address-verification
- [3] Spotify, "Spotify Premium" plan page, US list prices, checked 2026-11-07 — https://www.spotify.com/us/premium/
- [4] Ars Technica, "Spotify ramps up policy enforcement on family plans", 2026-10-23 — https://arstechnica.com/gadgets/2026/10/spotify-ramps-up-policy-enforcement-on-family-plans
- [5] Raspberry Pi, "Price increases for 2GB Raspberry Pi 4 and Raspberry Pi 5", 2026-10-01 — https://www.raspberrypi.com/news/price-increases-for-2gb-raspberry-pi-4-and-raspberry-pi-5/
- [6] Raspberry Pi, "Buy a Raspberry Pi 500+", product page, checked 2026-11-07 — https://www.raspberrypi.com/products/raspberry-pi-500-plus/
- [7] Home Assistant, "2026.11: A lot in store!", 2026-11-04 — https://www.home-assistant.io/blog/2026/11/04/release-202611/
- [8] TrendForce, "AI Server Demand Sustains Memory Contract Price Increases in 4Q26", 2026-09-30 — https://www.trendforce.com/presscenter/news/20260930-13258.html
- [9] Raspberry Pi, "16GB Raspberry Pi 5 on sale now at $120", 2025-01-09 — https://www.raspberrypi.com/news/16gb-raspberry-pi-5-on-sale-now-at-120/
