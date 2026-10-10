---
title: Home Assistant Renamed Its Cloud Because "Big Tech Ruined the Cloud"
vertical: personal_microeconomics_tinkering_tax
persona: systems_tinkerer_pro
one_big_thing: "The cloud has become a recurring rent on hardware people already own — and the honest counterweight to it is not 'self-hosting is free' but 'self-hosting is a maintenance bill,' which is now being repriced too."
date: 2026-10-10
slug: home-assistant-cloud-rename-hardware-rent
---

<!-- lead -->
On October 2, the maker of Home Assistant said it is renaming its paid service. Home Assistant Cloud becomes Home Assistant Link, and the reason is the word "cloud" itself [1][2]. "We hate clouds," founder Paulus Schoutsen told The Verge. "Big tech ruined the cloud, so we're out" [3].

<!-- tension -->

## The big picture:

The word "cloud" now stands for "ever-increasing subscription prices … outages and data harvesting," Nabu Casa wrote in its note [1][2]. That is a fight over words. On its own it would be a footnote.

What lifts it is where the rent is going. The monthly fee is moving off content and onto hardware people have already paid for.

Nabu Casa draws the line plainly. Its service is optional, has no lock-in, and a home keeps working if you cancel [1][2]. A big-tech cloud, in its telling, is required and walled off [2].

Schoutsen's own examples are blunt. Nest switched off the cloud for thermostats in Europe. Weber shut down the servers behind the June Oven. "Now you have a dumb oven that cost $1,500," he said [3].

What strikes me here is that this is the tinkering tax read from the other side. This desk has long argued that "free" self-hosting is only free if your hours cost nothing. The vendors now run the same math in reverse. The sticker price buys the box; the plan buys the right to keep using it.

<!-- By the numbers -->

## By the numbers

- **$6.50 a month — Home Assistant Link:** the optional remote-access plan being renamed. Home Assistant runs on local hardware and still works if the plan is cancelled [3].
- **60% — profit to the nonprofit:** the share of Link's profit that goes to the Open Home Foundation, Home Assistant's parent nonprofit [3].
- **2.7 million — homes running Home Assistant:** the estimated base, a small slice of the market [3].
- **90 to 64 days — cert lifetime:** Let's Encrypt is cutting the free renewal window on February 10, 2027, then to 45 days by 2028 [4][5].

<!-- tactical-insight -->

## What I'd watch:

What I'm watching next is the upkeep side, because it is being repriced at the same time. Let's Encrypt's shorter windows mean a self-hosted service renews its security cert more often [4].

Modern renewal tools ask the issuer when to renew. They handle it unseen. Setups that hardcoded "renew 60 days out" will now expire early. That old number was picked for 90-day certs, and it is wrong for 64 [4][5].

- **The renewal cadence:** cert lives drop from 90 days toward 64, then 45. The safe point is now about two-thirds of the life, not a fixed offset [4][5].
- **The ease trend:** Home Assistant 2026.10 added 15 apps, a one-click hookup for an AI assistant, and swapped its map to locally drawn OpenStreetMap tiles after the old provider demanded a key [6].
- **The rent spreading:** cameras that save no video without a plan, and appliances bricked when a vendor retires a server, are the same story told with other hardware [3][7].

Schoutsen wants a plain label on the box, saying whether a device needs the cloud at all. Nabu Casa is building a list of ones that do not [3].

<!-- nuanced-takeaway -->

## The catch

The part I keep circling is how little actually changed. The Verge called the rename "mostly symbolic," and the fee still stands [3]. Nabu Casa is not giving anything away.

The local path is not a price cut either. It is a swap: a monthly cash bill becomes a bill paid in hours, hardware and power. This month that bill went up, when the cert windows shortened [4][5].

The tooling also breaks for reasons that have nothing to do with the user. A map provider demanded a key. The cert issuer changed its rules [4][6].

Not everyone wants to run a server room. Home Assistant sits in about 2.7 million homes, a rounding error next to the big platforms [3].

<!-- tldr -->

## At a glance

- **The Big Shift:** Home Assistant's maker renamed Home Assistant Cloud to Home Assistant Link on October 2, saying "Big Tech ruined the cloud." The service and its $6.50 monthly price are unchanged. The point is the argument: cloud access has become a recurring rent on hardware people already own.
- **Why It Matters:** The rent is spreading from subscriptions to the devices themselves. Cameras stop recording without a plan, and thermostats and ovens stop working when a vendor retires a server. The price on the box is no longer the price of ownership.
- **What I'd Watch:** Whether the upkeep bill behind the "own it yourself" path keeps rising while the cash bill rises on the other side.
  - **Cert renewals:** Let's Encrypt cuts free cert lifetimes from 90 days to 64 on February 10, 2027, then to 45 days by 2028. Automatic tools absorb it; hardcoded schedules do not.
  - **Local-first tooling:** Home Assistant 2026.10 ships one-click AI setup and locally drawn maps, steadily cutting the hours it takes to run the local path.
  - **Vendor hardware plans:** The same rent model showing up on cameras and appliances, where a working device dies when a server is switched off.
- **The Catch:** The rename is symbolic and the fee remains. And "own it locally" is not free. It swaps a cash bill for an upkeep bill, one that also just went up.

## Sources
[1] Nabu Casa, "Cloud becomes Link," 2026-10-02 — https://www.nabucasa.com/news/2026-10-02-cloud-becomes-link
[2] Home Assistant, "Big Tech ruined the cloud, so we're renaming ours," 2026-10-02 — https://www.home-assistant.io/blog/2026/10/02/big-tech-ruined-the-cloud-so-were-renaming-ours/
[3] The Verge, "Home Assistant says 'Big tech ruined the cloud, so we're out'," 2026-10-02 — https://www.theverge.com/tech/1003936/home-assistant-says-big-tech-ruined-the-cloud-so-were-out
[4] Let's Encrypt, "64-Day Certificate Lifetimes Coming Feb 2027," 2026-10-07 — https://letsencrypt.org/2026/10/07/64-day-certs
[5] Ars Technica, "Let's Encrypt cuts certificate lifetimes to 64 days starting February 2027," 2026-10-08 — https://arstechnica.com/gadgets/2026/10/lets-encrypt-cuts-certificate-lifetimes-to-64-days-starting-february-2027
[6] Home Assistant, "2026.10: You are here," 2026-10-07 — https://www.home-assistant.io/blog/2026/10/07/release-202610
[7] Arlo Community, "New Arlo Subscription Plans and Features," 2026-09-15 — https://community.arlo.com/t5/Arlo-Secure/bd-p/en-arlo-secure
