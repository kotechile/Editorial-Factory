---
title: Your $16.53 Tester's Blind Spot
vertical: home_diagnostics_tech
kind: review
archetype: review
format: comparison
persona: homeowner_pro
one_big_thing: "A lamp tester cannot see a bootleg ground, because the jumper makes the neutral and ground slots read the same; only a device that loads the circuit and measures the wire changes the answer, and it still makes no false-ground claim."
date: 2026-11-08
slug: your-16-53-tester-blind-spot
price_as_of: "2026-11-08"
meta_title: "Your $16.53 Tester's Blind Spot"
meta_description: "Three outlet testers, one bootleg ground. The $16.53 lamp tester lights a correct pattern on a live yoke, and the load-test analyzer makes no false-ground call."
---

<!-- lead -->
The space heater goes into the bedroom outlet in the first cold week, and that outlet is where an older house keeps its worst secret: a three-prong socket whose ground was faked with a jumper from the grounding screw to the neutral screw. A $16.53 lamp tester lies about that socket. It lights the pattern that means correct wiring, and so does a mid-priced tester with a voltage display, because both only compare voltages from slot to slot, and that is the blind spot no lamp pattern can close. A circuit analyzer that costs about ten times as much loads the circuit and measures the voltage it loses instead, which is a real reading of the wiring, and its maker still claims no fake-ground call. The answer for one house costs less than any of the three.

<!-- tldr -->

## At a glance

- **The shift:** A lamp tester shows the pattern a fake ground makes, which is the pattern of a real one.
- **The number:** $159.99 buys a load test and no fake-ground claim.
- **The risk:** A reversed bootleg puts line volts on the yoke while the lamp says fine.

<!-- tension -->

## Why the lamps miss a jumper

A three-lamp tester is three small voltage sensors sharing one plug. Each lamp answers a question about one pair of slots: the left one reads between the neutral and ground slots, the centre between neutral and hot, the right between hot and ground [7]. The chart on the front of the tester turns that pattern into words.

A jumper between the grounding screw and the neutral screw collapses two of those questions into one. The hot slot now drives both the neutral and the ground slot, so the tester reads out the pattern it calls correct wiring [7]. Nothing in the device is broken. The fault sits in a wire the plug cannot reach.

The reversed version is the one that hurts. With a faked ground and reversed polarity, the metal yoke of the outlet sits at line voltage, and so does the frame of anything plugged into it, while the tester still shows correct wiring [7]. Mike Twitty, a licensed electrician and code inspector who wrote the guide for home inspectors, adds that no lights do not mean the outlet is dead [7].

| Unit | Price | Claimed | What it measures | Fails at |
|---|---|---|---|---|
| Klein RT210 | $16.53 | five wiring conditions from a lamp chart [1] | voltage between three slot pairs | any fault that makes two slots equal |
| Klein RT250 | $36.46 | voltage readout and a ground-fault trip timer [2] | the same three voltages, plus a timer | the same blind spot, with a number on it |
| Klein RT390 | $159.99 | load tests and arc-fault inspection [3] | percentage voltage drop under load | the maker claims no fake-ground detection |

## By the numbers

- **$19.93:** The step from the RT210 to the RT250 buys a voltage readout and a ground-fault trip timer, and nothing on the ground [2].
- **Five conditions:** What the RT210's lamp chart can report, and a fake ground is not one of them [4].
- **1,440 watts:** What a heater pulls on a bedroom circuit, the load class that the analyzer's smallest test simulates [6].

<!-- tactical-insight -->

## What the analyzer measures

The RT390 earns its price on a different question. It applies a load at three settings and reports the percentage voltage drop, inspects ground-fault and arc-fault devices with a trip time, and flags a dual open-neutral and open-ground fault [6]. That reading previews what the wiring does once the load arrives, which is the question in a house about to carry two heaters. A load of one heater is the smallest of its three test settings.

What it does not do is make the fake-ground call. Klein's page for the RT390 lists wiring faults, the dual open fault, both device inspections and the voltage-drop tests, and no fake-ground row appears in that list [6]. The RT210's page is the same: five conditions, no fake ground [4]. The RT250 adds a display and a trip timer, states that arc-fault testing is not included, and adds nothing on the ground [5].

The one class that advertises the call is the Ideal Electrical SureTest. Its feature list says it identifies false grounds, reads ground impedance down to a hundredth of an ohm, reads ground-to-neutral voltage, and tests a ground-fault device at a measured current [8]. A trade review of the successor model describes the same load tests and adds that the resistance of the hot, neutral and ground wires is measured and displayed [11]. That series is listed at $421.33 by a distributor [8]. The maker's own page for that model says it has been discontinued [10]. The ceiling of this comparison is an outgoing unit at twenty-five times the price of the tester, sold on a claim whose accuracy nobody here publishes.

<!-- nuanced-takeaway -->

## The catch

Every tester here is a two-terminal device. It can only compare the slots to each other, and a bootlegger's jumper makes two of those comparisons identical, so no plug-in instrument settles the question on its own. That is why the honest test for one house is not a purchase. Twitty's guidance is to read the panel first: in an older home with apparently grounded outlets, look for the equipment grounding wires, and if none or very few are present, expect bootlegging [7]. Then take one cover off and look for the jumper [7].

That is a screwdriver, ten minutes, and no instrument at all. The cheap tester stays worth carrying, because it catches the faults the lamps can see — open ground, reversed polarity, open hot, open neutral, hot and ground reversed [4] — and because a ground-fault outlet still has to be tripped once a year. What it cannot do is certify a ground, and nothing in this comparison certifies one at any price. My read of the three steps is that the money buys better readings of a different question, not a better answer to the ground question.

## What we did not test

This review is built from three Klein Tools specification tables, four retailer price pages, one licensed electrician's published guide for home inspectors and one trade review of a successor analyzer. No unit was held, plugged in or measured for it, and no outlet was opened. Every price is a standing retail figure read on 2026-11-08, and no source in this set measures any of these devices against a known fake ground.

## Which one, by situation

| If this is your situation | Buy this |
|---|---|
| Older house, three-prong outlets, one heater going in | Klein RT210, then read the panel and open one outlet [1] |
| You want a voltage number and a trip time on the same walk | Klein RT250, knowing the ground question is unchanged [2] |
| A whole house about to be loaded, and you want a drop reading per circuit | Klein RT390 [3] |
| You need the false-ground call itself, on many properties | Ideal Electrical SureTest, current model, above the discontinued listing [10] |

The cheap Klein RT210 tester keeps working as the sweep tool in all four cases. The [imager piece on what conditions do to a reading](/your-250-imager-needs-15-degrees/) makes the same point about a different instrument: a number is only as good as the conditions it was taken in. For the arithmetic on what a diagnostic habit costs against what it prevents, the [true-cost-of-ownership calculator](/calculators/true-cost-of-ownership/) runs the comparison, and the [home diagnostics hub](/categories/home-diagnostics-tools/) carries the rest of this vertical's instruments.

## Sources

- [1] Elliott Electric Supply, "Klein RT210 GFCI Outlet Tester" — https://www.elliottelectric.com/P/Item/KLE/RT210
- [2] Elliott Electric Supply, "Klein RT250 GFCI Receptacle Tester with LCD" — https://www.elliottelectric.com/P/Item/KLE/RT250
- [3] Haus of Tools, "Klein Tools RT390 Circuit Analyzer" — https://hausoftools.com/products/klein-tools-rt390-circuit-analyzer
- [4] Klein Tools, "RT210 GFCI Outlet Tester, specifications" — https://www.kleintools.com/catalog/electrical-testers/gfci-outlet-tester
- [5] Klein Tools, "RT250 GFCI Receptacle Tester with LCD, specifications" — https://www.kleintools.com/catalog/electrical-testers/gfci-receptacle-tester-lcd
- [6] Klein Tools, "RT390 Circuit Analyzer, specifications" — https://www.kleintools.com/catalog/electrical-testers/circuit-analyzer
- [7] Mike Twitty, "The Inconvenient Truth About Three-Light Receptacle Testers", Working RE — https://www.workingre.com/the-inconvenient-truth-about-three-light-receptacle-testers
- [8] Licensed Electrician, "Ideal SureTest Circuit Analyzers 61-165 and 61-164" — https://www.licensedelectrician.com/Store/ID/SureTest_Analyzers.htm
- [9] Test Equipment Depot, "Ideal Electrical 61-164 SureTest Circuit Analyzer" — https://www.testequipmentdepot.com/ideal-electrical-61-164-suretest-circuit-analyzer.html
- [10] Ideal Electrical, "SureTest Circuit Analyzer", model 61-164, discontinued — https://idealelectricalinc.com/product/suretest-circuit-analyzer
- [11] Pro Tool Reviews, "Ideal Suretest Digital Analyzer 61-165" — https://www.protoolreviews.com/ideal-suretest-digital-analyzer-61-165
- [12] Elliott Electric Supply, "Klein RT390 Circuit Analyzer" — https://www.elliottelectric.com/P/Item/KLE/RT390
