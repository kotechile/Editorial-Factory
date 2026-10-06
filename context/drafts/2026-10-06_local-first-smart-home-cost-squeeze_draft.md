---
title: The local-first smart home got pricier the same week the cloud got disowned
vertical: smart_home_telemetry
persona: pro_homeowner
one_big_thing: "Both ways to run a smart home got more expensive in the same week: the cloud is adding paywalls, and the local-first hardware is being repriced by AI datacenter memory demand."
date: 2026-10-06
slug: local-first-smart-home-cost-squeeze
synthesis: true
sources:
  - https://www.raspberrypi.com/news/price-increases-for-2gb-raspberry-pi-4-and-raspberry-pi-5/
  - https://www.home-assistant.io/blog/2026/10/02/big-tech-ruined-the-cloud-so-were-renaming-ours/
---

<!-- lead -->
On 1 October, Raspberry Pi raised its prices for the third time this year, adding $12.50 to its two cheapest current boards: the 2GB Raspberry Pi 4 now costs $67.50 and the 2GB Raspberry Pi 5 costs $77.50 [1][2]. A day later, Home Assistant — the open-source platform most local-first homes run on — renamed its cloud service because, in its own words, "Big Tech has given the cloud a bad name" [4].

<!-- tension -->

## The big picture:

The smart home has two escape routes from rising costs, and both got more expensive in the same week.

The first is to stay on the vendor's cloud. That is getting pricier by policy. Samsung is ending free SmartThings API (application programming interface) access and moving individual developers to a $4.99-a-month plan, a change that lands on the Home Assistant integration many owners rely on [5]. Home Assistant's vice-president of commercial wrote that the cloud now stands for "ever-increasing subscription prices to outages and data harvesting" [4].

What strikes me here is that the other route — own your hardware — is being repriced by the same force. Raspberry Pi blames memory costs, which it says "have risen very steeply over the past two years and continues to increase" [1]. That is the artificial-intelligence datacenter build-out arriving at your hallway hub.

Micron's chief executive told investors on the same day that the shortage runs through at least 2028, that demand will keep outpacing supply, and that three-quarters of its 2027 output is already spoken for [3]. Samsung expects high-bandwidth memory (HBM) — the fast memory that AI chips devour — to take almost 30% of DRAM (dynamic random-access memory) factories' wafer capacity next year, up from 20% this year [3]. Consumer boards get what is left.

## By the numbers

- **$12.50 — Raspberry Pi's third hike of 2026:** The 2GB Pi 4 rises to $67.50 and the 2GB Pi 5 to $77.50, effective 1 October, with memory costs as the stated cause [1][2].
- **75% — Micron's 2027 output already sold:** The memory maker says most of its current sales talks are about 2028, and its chief expects demand to outrun supply for years [3].
- **30% vs 20% — AI memory's share of DRAM wafers:** Samsung expects high-bandwidth memory to take almost a third of factory wafer capacity in 2027, up from a fifth this year, thinning the supply left for consumer gear [3].
- **$4.99 a month — the new cloud door fee:** SmartThings free API access ends this month; the personal plan applies to non-commercial developers, including the Home Assistant integration [5].

<!-- tactical-insight -->

## What I'd watch:

The people closest to this are doing arithmetic, not ideology. I've been watching the Home Assistant forum fill with owners migrating off SmartThings before the fee lands.

- **The cheap tier, chosen on purpose:** Raspberry Pi's own advice is to buy only the memory you need and to consider older boards where they already do the job [1]. A hub is not a workstation.
- **The floor that held:** The 1GB boards and the 2GB Compute Modules kept their prices this round [1]. That is now the stable end of the market, and I'd expect buyers to camp there.
- **The mini-PC detour:** An entry Intel mini-PC often costs less than a high-memory board once you add storage and a case. I want to see whether local-first homes start jumping across.
- **The 2028 question:** If the shortage really runs to 2028 [3], then "wait for prices to fall" is not a plan for anyone building this year.

<!-- nuanced-takeaway -->

## The catch

I could be wrong to tie a memory shortage to a naming decision. Home Assistant's rename costs users nothing — the service stays optional, and the home keeps working without it [4].

The honest limit is that the two legs run on different clocks. The Pi hike is a single move this month. The memory shortage is a two-year trend. The cloud paywall is a pricing choice. The local-first premium is a supply shock, and supply shocks reverse.

What I keep circling is this. The local-first promise is a fixed cost — buy once, run it for years. That promise only holds if the hardware underneath is stable. Right now it is not. The escape hatch from subscription creep is turning into a subscription to hardware inflation.

<!-- tldr -->

## At a glance

- **The Big Shift:** In the same week, Raspberry Pi raised board prices for the third time this year, and Home Assistant renamed its cloud service because "Big Tech has given the cloud a bad name".
- **Why It Matters:** Both ways to run a smart home got more expensive. The cloud is adding paywalls, and the local alternative is being repriced by AI datacenter memory demand.
- **What I'd Watch:**
  - **The cheap tier:** Whether buyers stop paying for memory headroom and pick older boards or modest mini-PCs instead.
  - **The mini-PC detour:** Whether local-first homes move to small Intel boxes that cost less than a high-memory single-board computer.
  - **The floor that held:** The 1GB boards whose prices did not move, now the stable end of the market.
- **The Catch:** The rename costs users nothing and the shortage may ease by 2028. But "wait for prices to fall" is not a plan for someone building now.

## Sources
[1] Raspberry Pi, "Price increases for 2GB Raspberry Pi 4 and Raspberry Pi 5" (2026-10-01). https://www.raspberrypi.com/news/price-increases-for-2gb-raspberry-pi-4-and-raspberry-pi-5/
[2] Tom's Hardware, "Memory shortages drive Raspberry Pi prices up by up to 23%" (2026-10-01). https://www.tomshardware.com/raspberry-pi/component-shortages-drive-raspberry-pi-prices-up-by-up-to-23-percent-escalating-lpddr4-lpddr5-costs-trigger-the-third-price-hike-of-the-year
[3] Ars Technica, "Memory executives expect RAM shortage to continue through 2028" (2026-10-01). https://arstechnica.com/information-technology/2026/10/memory-supplies-are-only-getting-tighter-micron-ceo-says/
[4] Home Assistant, "Big Tech ruined the cloud, so we're renaming ours" (2026-10-02). https://www.home-assistant.io/blog/2026/10/02/big-tech-ruined-the-cloud-so-were-renaming-ours/
[5] SmartThings, "A New Enhanced SmartThings API Experience" (2026-06-23). https://blog.smartthings.com/smartthings-updates/a-new-enhanced-smartthings-api-experience/

<!-- linkedin -->
I've been reading the smart-home price news this week, and two things landed in the same 48 hours.

On 1 October, Raspberry Pi raised prices for the third time this year. The 2GB Pi 4 is now $67.50 and the 2GB Pi 5 is $77.50 — both blamed on the cost of memory. The same day, Micron's chief said the memory shortage runs through at least 2028 and that most of its 2027 output is already sold.

A day later, Home Assistant renamed its cloud service to "Link" because "Big Tech has given the cloud a bad name", citing ever-increasing subscription prices. On the other side, Samsung is putting the SmartThings API behind a $4.99-a-month plan this month, which hits the Home Assistant integration many owners use.

My read: both escape routes from rising smart-home costs got more expensive at once. The cloud is adding paywalls. The local-first answer — own your hardware — is being repriced by the same AI datacenter build-out that makes the cloud feel extractive.

What I'm watching next is whether owners stop buying memory headroom and camp on the cheap tier. Curious how others are pricing their next hub.
