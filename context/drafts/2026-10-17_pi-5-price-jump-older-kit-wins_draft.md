---
title: "Pi 5 Jumps $12.50: Older Kit Is Your Cheap Upgrade"
vertical: personal_microeconomics_tinkering_tax
persona: systems_tinkerer_pro
one_big_thing: "The capital side of self-hosting was repriced by AI datacenter demand, and the only substitution that still saves money is older hardware."
date: 2026-10-17
slug: pi-5-price-jump-older-kit-wins
synthesis: true
sources:
  - https://www.raspberrypi.com/news/price-increases-for-2gb-raspberry-pi-4-and-raspberry-pi-5
  - https://diskprices.com/
---

<!-- lead -->
The 2GB Raspberry Pi 5 jumps to $77.50, a $12.50 rise on October 1 that lands on the cheapest board most people use for an always-on box. Raspberry Pi's own advice to buyers was to weigh older kit — a 3B, 3A+ or 3B+ — as the cheaper upgrade. Two days later, the price index that ranks storage by cost per terabyte put its cheapest line at $4.56, on tape, a medium the professional world retired two generations ago [1][3].

<!-- tension -->

## The big picture:

The self-hosting pitch has always been a trade: a monthly rent swapped for maintenance hours. That trade quietly assumed the hardware was a fixed asset, already bought, slowly losing value.

This quarter the hardware is an input with a price set by somebody else's datacenter. Memory analysts at TrendForce expect DRAM (the working memory chips) contract prices to rise 10% to 15% in the fourth quarter. They expect NAND (the flash memory inside drives) contract prices to rise 15% to 20% [2]. Their reason is the same in both cases: suppliers are giving advanced capacity to server parts, and the consumer side is left on "production cuts" [2].

What strikes me is how cleanly that lands on the hobby. A 2GB board is not a server part. It is the cheapest way to own an always-on box, and it just got 19% dearer, from $65 to $77.50 [1].

## By the numbers

- **$12.50 — Pi 5 2GB increase:** the board went to $77.50 on October 1, and the 2GB Pi 4 went to $67.50; in April the company could still hold these two down, and this time it said that had "now become unsustainable" [1].
- **10% to 15% and 15% to 20% — memory contracts:** TrendForce's projection for DRAM and NAND contract prices in the fourth quarter of 2026 [2].
- **$4.56 versus $23.57 — cost per terabyte:** the cheapest tape on the Disk Prices index against the cheapest hard disk, in the same October 3 listing. Tape is 5.17 times cheaper per terabyte, before a drive is bought [3].
- **$85.00 — solid-state per terabyte:** the cheapest solid-state drive in that listing was a 4TB unit at $340, which is 3.6 times the cheapest disk per terabyte [3].

<!-- tactical-insight -->

## What I'd watch:

I keep coming back to the fact that both answers are older technology. That is the shape of this quarter, not a coincidence.

- **The vendor's own downgrade:** Raspberry Pi tells buyers to check they are "not paying for headroom you don't need" and to weigh a 3B, 3A+ or 3B+ at lower cost [1]. When the seller points at last year's model, the price signal is doing the talking.
- **The 18-terabyte sum:** at the index's cheapest disk rate, 18TB costs about $424. The same capacity in LTO (Linear Tape-Open) cartridges costs $82, because a 20-pack runs $1,640 [3]. That gap is $342, and it is the number that sends people to eBay for tape drives.
- **The used tier is doing the work:** a used 18TB enterprise drive sat at $23.89 per terabyte against $23.57 for the cheapest new 14TB unit [3]. The second-hand market is no longer a bargain bin; it is the market.
- **The fast tier is the worst place to hoard:** at $85 per terabyte, solid-state is for things that must be fast, not for the archive [3]. Anyone storing photos on flash is paying 3.6 times the disk rate for capacity they will read twice a year.
- **The supply side is not loosening:** enterprise solid-state demand is projected to grow more than 80% this year, and it is the only memory category whose price growth accelerates in the fourth quarter [2]. That is where the capacity is going.

<!-- nuanced-takeaway -->

## The catch

My read is that the tape arithmetic is real but incomplete, and the incompleteness is where most people get hurt. The $4.56 per terabyte buys cartridges, not a working backup. The drive is separate, and a used one runs a few hundred dollars. The workflow is manual too: one cartridge at a time, offline, with a copy job someone has to remember to run [4].

The capacity claim needs a second look too. A label on an LTO-5 cartridge says 3TB, but that assumes 2:1 compression you will not get on photos and video — the usable figure is about 1.5TB per cartridge [4]. Tape is cheap per terabyte and slow per restore, and a restore is the only moment the whole exercise matters.

There are three honest hedges on the other side. The index is retail listings, not a survey, so its cheapest rows move week to week [3]. TrendForce expects the DRAM increase to moderate, not to stop [2]. And Raspberry Pi says it will reverse its increases when memory prices subside [1].

I would not build a five-year plan on any of those. I would not pretend the trend line is permanent either.

<!-- tldr -->

## At a glance

- **The Big Shift:** The cheapest hardware for an owned, always-on stack got dearer in the same week that the cheapest storage turned out to be tape. Both moves trace to AI datacenter demand pulling memory and flash capacity away from consumer parts.
- **Why It Matters:** The self-hosting case rests on a capital cost that was stable. If a 2GB board rises 19% and a terabyte of disk costs $23.57 at the cheap end, the rent-versus-own comparison has to be re-run, not assumed.
- **What I'd Watch:** Whether buyers follow the vendors into older silicon, and whether the second-hand tier absorbs the demand.
  - **Headroom:** Memory you paid for and do not use, which is the first thing a price rise makes visible.
  - **Media tiering:** Fast flash for what is read often, cheap disk or tape for the archive.
  - **Used enterprise gear:** Off-lease drives and old tape libraries, now the value end of the market.
- **The Catch:** Tape's price is media only — the drive, the manual workflow and the slow restore are the rest of the bill. The index reflects one week of retail listings, and the memory forecast is for a slower rise, not a reversal.

## Sources

[1] Raspberry Pi, "Price increases for 2GB Raspberry Pi 4 and Raspberry Pi 5" (Eben Upton, 2026-10-01) — https://www.raspberrypi.com/news/price-increases-for-2gb-raspberry-pi-4-and-raspberry-pi-5
[2] TrendForce, "AI Server Demand Sustains Memory Contract Price Increases in 4Q26, While Consumer-Side Pressure Persists" (2026-09-30) — https://www.trendforce.com/presscenter/news/20260930-13258.html
[3] Disk Prices (US), price index, last updated 2026-10-03 16:18:45 UTC — https://diskprices.com/
[4] Hackaday, "Backup Tapes Come Back To The Homelab" (2026-10-12) — https://hackaday.com/2026/10/12/backup-tapes-come-back-to-the-homelab/
