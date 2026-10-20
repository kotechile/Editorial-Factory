---
title: "Your Render Bill Multiplies by 22.97"
vertical: workstation_compute_economics
persona: infra_engineer
one_big_thing: "Cloud transcoding is billed per output minute scaled by a multiplier table the price list does not lead with, so a six-rung render ladder bills eleven minutes for every source minute ($4.95 a source hour on MediaConvert's basic tier) while one current-generation graphics card encodes 1080p at 506 frames a second for about half a cent of power an hour — and a $2,500 encode box therefore needs roughly 506 source hours of that ladder work to pay back."
date: 2026-10-20
slug: your-render-bill-multiplies-by-22-97
archetype: evergreen
evergreen: true
meta_title: "Your Render Bill Multiplies by 22.97"
meta_description: "Cloud transcoding bills the render ladder, not the footage: a six-rung ladder bills eleven output minutes per source minute, $4.95 an hour on AWS's basic tier."
---

<!-- lead -->
Amazon Web Services (AWS) multiplies each high-definition output minute by 22.97 in its own worked example, before it applies the per-minute rate [1]. Your render ladder sets the bill, not the length of your footage. Price that ladder the way the vendors do and one hour of source footage costs $4.95 to deliver on Elemental MediaConvert's basic tier, and $9.90 on Google's transcoder service [1, 2]. One current-generation GeForce card encodes the same 1080p output at 506 frames a second, for about half a cent of electricity per output hour [3, 4, 5].

<!-- tension -->

## The big picture:

The headline price is the least important number on either rate card.

Elemental MediaConvert quotes $0.0075 per "normalized" minute on its basic tier. That price covers the first 100,000 minutes a month, then drops to $0.0053 and $0.0038 [1]. The professional tier starts at $0.0120 [1]. Google's transcoder quotes $0.015, $0.03 and $0.06 per output minute for standard, high and ultra-high definition output [2].

A normalized minute is not a minute of video. It is a minute of video multiplied by the resolution, the frame rate and the codec quality you asked for [1].

Take plain, single-pass Advanced Video Coding. The multiplier runs 1x for standard definition, 2x for high definition and 4x for 4K at 30 frames a second [1]. Push the frame rate past 30 and the same three outputs cost 1.25x, 2.5x and 5x [1]. Ask for VP9 in multi-pass mode and high definition jumps from 2x to 4x, then to 7x at 60 frames [1].

Now build a ladder. Three standard tiers, two high-definition tiers and one 4K tier is an everyday delivery set.

That ladder is 11 normalized minutes for every source minute: 3 + 4 + 4 [1]. At $0.0075, one source hour costs $4.95 [1]. The same six renditions cost $9.90 on Google's card, which prices each output by its own resolution and gives no ladder discount [2].

The two vendors' headline prices differ by a factor of two. The multiplier structure keeps that gap. Nothing in either document is hidden. The number a buyer remembers is the per-minute price; the number that arrives on the invoice is the multiplier.

AWS's example is blunter than anything I could build myself. Ten thousand 45-minute videos, a standard-definition ladder at 11.48x and a high-definition ladder at 22.97x, for 15.5 million normalized minutes in one month [1].

I keep coming back to what that does to a small shop. Forty hours of source a month is a weekly half-hour show plus clips. On the 11x ladder that is $198 a month on AWS and $396 on Google [1, 2].

The local sum looks nothing like that. Nvidia's hardware encoder (NVENC) runs 977 frames a second on 1080p H.264 at its fastest preset on Blackwell silicon [3]. It runs 506 at a mid preset and 227 at its slowest. Those are 8-bit 4:2:0 measurements at 1,920 by 1,080, with the clocks stated [3].

At 506 frames a second, one wall-clock hour yields 16.9 hours of 30-frame output. A 575-watt card on the 13.41-cent commercial power rate burns 7.7 cents in that hour [4, 5]. That is 0.46 cents per output hour.

So the local box does not compete with the transcode fee at the margin. It competes with the hours you feed it.

Divide the box's price by $4.95 and you get the source hours it must eat. A $2,500 machine needs about 506 of them [1]. That is twelve and a half months at 40 hours a month, and over four years at 10.

## By the numbers

- **22.97x — Ladder multiplier:** AWS multiplies one high-definition 60-frame VP9 output minute by 22.97 before charging the $0.0120 professional rate [1].
- **$4.95 vs $9.90 — One source hour:** Six renditions — three standard, two high, one 4K — cost $4.95 an hour on MediaConvert's basic tier and $9.90 on Google's transcoder [1, 2].
- **1,134 fps — Blackwell high-efficiency encoding:** The fastest preset runs 1,134 frames a second on 1080p high-efficiency video coding (HEVC), and 181 at the slowest [3].
- **0.46 cents — Local power per output hour:** A 575-watt card at 13.41 cents a kilowatt hour, at 506 frames a second, spends under half a cent of power per hour of output [3, 4, 5].

<!-- tactical-insight -->

## What I'd watch:

The pipelines I have watched go local all count renditions before they count minutes. The ones that stay on cloud transcode usually ship one or two outputs per source.

Concurrency is where the local plan usually breaks. Nvidia's licensing policy limits non-qualified, meaning consumer GeForce, cards to eight sessions at once per system [3]. That cap counts every such card in the box. A second GeForce card buys speed, not more sessions.

Nvidia's support matrix lists twelve sessions for the current GeForce flagship, so the two documents disagree [7]. I would want the driver checked before anyone sizes a farm on either number.

The quality preset is the dial nobody prices. Between the fastest and slowest settings the same card loses 83% of its H.264 throughput, and 84% on HEVC [3].

Short clips carry a billing quirk. Six-second clips in six renditions bill as six ten-second outputs. So 36 seconds of content is charged as 60, a 67% overhead [1].

Then there is file size. HandBrake's own benchmark notes say hardware encoders go faster "at the expense of some loss in quality and/or larger file sizes" [6]. Its test found x264 the better balance of speed, quality and size [6].

Bigger files move cost off the transcode line and onto storage and egress. Neither transcode rate card includes those. That is the part of this comparison I have not seen anyone publish in full.

<!-- nuanced-takeaway -->

## The catch

The 22.97x figure is a professional-tier VP9 ladder at 60 frames, not a default [1]. Quoting it as typical would be the same trick as quoting the cheapest per-minute rate as the average. The plain single-pass ladder in this piece is 11x.

My read is that the transcode fee is small for most teams. It is large only for ladder-heavy, high-frame-rate output. Below roughly 40 source hours a month the cloud line is cheaper in cash than any box [1]. A local rig then has to justify itself on turnaround or on privacy, not on arithmetic.

The local cost above is also incomplete in the vendors' favour. It prices the card's power and nothing else. No host, no cooling, no failed drives, no engineer's afternoon lost to a driver upgrade.

What the evidence does support is narrower and more useful than the usual claim. The cloud prices the rendition. The box prices the hour. The two only meet at a volume the reader has to measure. I could be wrong about how many shops sit above 500 source hours a month, but the ones that do are easy to spot: their transcode invoice is a four-figure line.

<!-- tldr -->

## At a glance

- **The Big Shift:** Cloud transcoding bills per output minute, scaled by a multiplier table that rarely enters a buying conversation. The delivery ladder decides the invoice, not the footage.
- **Why It Matters:** At $4.95 a source hour on AWS and $9.90 on Google, a many-rendition pipeline pays a real monthly bill. The same output on one graphics card spends about half a cent of power per hour of output.
- **What I'd Watch:** Where the volume line falls, and what the vendors do there.
  - **Ladder composition:** How many renditions each source minute is delivered in, since every tier and frame-rate band carries its own multiplier.
  - **Session limits:** The cap on simultaneous encode sessions per system, which decides whether a local farm scales by adding cards.
  - **File-size trade:** Whether the faster hardware encode costs more in storage and egress than it saves on the transcode line.
- **The Catch:** The 22.97x example is a professional-tier VP9 ladder, the cheapest per-minute rate is not the average, and the local figure here prices only the card's power.

## Sources
[1] AWS Elemental MediaConvert — On-Demand Pricing: https://aws.amazon.com/mediaconvert/pricing/
[2] Google Cloud — Transcoder API pricing: https://cloud.google.com/transcoder/docs/pricing
[3] NVIDIA — NVENC Application Note, Video Codec SDK 13.0: https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/nvenc-application-note/index.html
[4] NVIDIA — GeForce 5090 specifications: https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/
[5] U.S. Energy Information Administration — Electricity explained: Prices and factors affecting prices: https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php
[6] HandBrake Documentation — Performance: https://handbrake.fr/docs/en/latest/technical/performance.html
[7] NVIDIA — Video Encode and Decode Support Matrix: https://developer.nvidia.com/video-encode-and-decode-gpu-support-matrix-new
