---
title: Your Lock's Blind 90% Bet
vertical: smart_home_telemetry
persona: pro_homeowner
one_big_thing: "A 2027 door lock is a choice between four different meanings of local — on-device, on-hub, on-your-block and on-the-vendor's-permission — and only one question survives all four: what has to be alive for the bolt to retract."
date: 2026-10-20
slug: your-locks-blind-90-bet
synthesis: true
sources:
  - https://www.apple.com/newsroom/2026/10/introducing-apple-home-collection-a-new-lineup-of-smart-home-accessories
  - https://www.aboutamazon.com/news/devices/ring-smart-lock-battery-recharge
---

<!-- lead -->
Ring's first smart lock keeps working when your home Wi-Fi dies. That is because it does not use your home Wi-Fi. Announced on 7 October, the deadbolt stays online through Amazon Sidewalk, a mesh of nearby Echo and Ring devices, so your door leans on a neighbour's router [6][7]. Amazon says that mesh covers more than 90% of people in the United States [4]. Six days later, Apple announced a lock with a different plan: the bolt is Matter compatible, supports Aliro, and Apple says it works "entirely locally so core access functions continue even without an internet connection" [1]. Both are sold as local control. Your lock's blind 90% bet is which network has to be alive, and there are four ways to answer it.

<!-- tension -->

## The big picture:

Matter has been the floor for gadgets that work together since 2022. Buy a device with the badge and it should talk to your hub, whatever the brand. Apple just shipped its own hardware that earns the badge honestly [1]. Its hinge is the part no box mentions: a hub you buy, and a Wi-Fi network you keep [3].

What strikes me here is that Amazon did not argue about any of it. It went around.

The Ring lock gets its link from a network Amazon already runs. A Sidewalk device reaches a Bridge up to half a mile away. The Bridge then sends the traffic to the cloud [4]. Amazon says more than 90% of people in the United States live inside that cover [4]. No hub on your side. No home router in the path.

So local now covers four setups, and each one fails in its own way. Local on the device: the bolt decides by itself. Local on your hub: Thread and Matter, with a box in the kitchen holding the keys. Local on your block: a neighbour's Echo carries the message. Local by the vendor's say-so: a working local link that a firmware change can switch off.

That last one is real. Home Assistant's October release dropped its SolarEdge Local integration. SolarEdge had turned off the local web interface in inverter firmware revisions from 2020 [8]. The replacement reads the same inverter over the home network, with no account and no cloud [8]. The wiring never changed. The permission did.

## By the numbers

- **More than 90% — Sidewalk's reach:** Amazon says over 90% of people in the U.S. live in an area with Sidewalk coverage, and a device can reach a Bridge up to a half mile away before the Bridge carries the data to the cloud [4].
- **0.15% — The neighbour's share:** a Sidewalk Bridge gives up no more than 0.15% of average US household internet use, which Ring likens to streaming about 10 minutes of 4K video [5].
- **10 days — Apple's video window:** camera events sit in the buyer's iCloud+ plan for 10 days, and Apple says there is no separate camera subscription [1].
- **13 November — The hub ships:** HomeView pre-orders opened on 13 October, with availability from 13 November. The accessories follow from December [2][3].

<!-- tactical-insight -->

## What I'd watch:

The people closest to this are not arguing about rules. They are arguing about what stays up.

- **Which parts count as core.** Apple says the lock's core access functions survive with no internet [1]. I want that list, because LG (the partner behind the cameras) says the family needs an Apple hub and a Wi-Fi connection [3]. One function on the device and one need in the house can both be true.
- **Whether the cover language firms up.** Ring's footnote lets Sidewalk coverage change or stop, and Amazon's own guide says the Bridge hands data to the cloud [4][7]. The signal I am watching for is the first public account of a lock that failed during a local outage.
- **Where the bill lands.** Apple's answer to "no hub" is a hub, and HomeView is one more purchase on top of the lock [2]. Amazon's answer is a network it owns and does not charge for [5]. That is why the spec sheets look alike and the bills do not.
- **Where the off switch sits.** The SolarEdge case shows a local link dying on a firmware call, with the community rebuilding on a second local one [8]. The open question for both locks is which of their local paths is written down and which is a favour.

<!-- nuanced-takeaway -->

## The catch

The honest version is that Amazon's lock drops a need that Apple's stack keeps, and Apple's lock promises something Amazon's cannot: a core function that never leaves the door. Both claims are narrow. Both are true as written.

Ring's Sidewalk route still ends at a cloud, just later in the path, and the network is Amazon's, with the coverage footnote written for the places it does not reach [4][7]. Apple's route ends at your hub, which is a computer the buyer has to buy, power and patch [3]. Neither is an island. My read, held loosely, is that "works locally" has become the least useful line on a smart home box. It names a shape, not a promise. The question that survives all four meanings is duller and better: what has to be alive for the bolt to retract?

<!-- tldr -->

## At a glance

- **The Big Shift:** In the same week, Ring shipped a smart lock that stays online through Amazon Sidewalk instead of home Wi-Fi, and Apple shipped a lock it says works entirely locally over Matter, Thread and Aliro. Two answers to the same failure, six days apart [1][6].
- **Why It Matters:** Neither answer removes a need. It moves the need. Apple's family calls for a hub and Wi-Fi, by its own partner's words, and Amazon's calls for Sidewalk cover that its own footnote can interrupt [3][7]. For a 2027 lock purchase, "local" no longer says which network has to survive a bad night.
- **What I'd Watch:** Which parts of each promise hold in an outage, and how each vendor writes them down.
  - **Core functions:** The short list of things a lock can still do with no internet, which Apple says it keeps and nobody has published yet.
  - **Cover terms:** Whether the "subject to change or interruption" line survives Sidewalk's first public failure.
  - **The vendor's off switch:** The SolarEdge Local removal, where a firmware change retired one local link and the fix was a second local one.
- **The Catch:** Apple's local path runs through hardware the buyer owns and has to keep running. Amazon's runs through a network it operates. Both are real. Neither is freedom.

## Sources

[1] Apple, "Introducing Apple Home Collection, a new lineup of smart home accessories," 2026-10-13 — https://www.apple.com/newsroom/2026/10/introducing-apple-home-collection-a-new-lineup-of-smart-home-accessories

[2] Apple, "Meet Apple HomeView, a new way to enjoy entertainment, stay connected, and manage the home," 2026-10-13 — https://www.apple.com/newsroom/2026/10/meet-apple-homeview-a-new-way-to-enjoy-entertainment-and-manage-the-home

[3] LG Global Newsroom, "LG Electronics Announces New Smart Home Accessories, Designed in Collaboration With Apple for the Apple Home Collection," 2026-10-13 — https://www.lg.com/global/newsroom/news/corporate/lg-electronics-announces-new-smart-home-accessories-designed-in-collaboration-with-apple

[4] Amazon, the About Amazon explainer on Amazon Sidewalk — https://www.aboutamazon.com/news/devices/everything-you-need-to-know-about-amazon-sidewalk

[5] Ring, "Amazon Sidewalk" product page — https://ring.com/amazon-sidewalk

[6] Amazon, "Ring ends smart lock anxiety with a lock you can recharge by hand," About Amazon, 2026-10-07 — https://www.aboutamazon.com/news/devices/ring-smart-lock-battery-recharge

[7] Ring, "Ring Announces Smart Lock, Expands 4K Camera Lineup, and Introduces New Pan-Tilt 2K Indoor Camera," The Ring Blog, 2026-10-09 — https://blog.ring.com/products-innovation/ring-announces-smart-lock-expands-4k-camera-lineup-and-introduces-new-pan-tilt-2k-indoor-camera

[8] Home Assistant, "2026.10: You are here," 2026-10-07 — https://www.home-assistant.io/blog/2026/10/07/release-202610
