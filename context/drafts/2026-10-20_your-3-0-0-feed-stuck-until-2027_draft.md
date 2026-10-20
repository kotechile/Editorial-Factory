---
title: Your 3.0.0 Feed Stuck Until 2027
vertical: control_tower_exception_orchestration
persona: supply_chain_architect
one_big_thing: "Standard event names shrink a control tower's mapping bill but do not settle whose timestamp counts — and the industry's own eBL adoption data shows the stall has moved to the platform seam."
date: 2026-10-20
slug: your-3-0-0-feed-stuck-until-2027
synthesis: true
sources:
  - https://dcsa.org/newsroom/track-and-trace-3-0-0-iot-reefer-visibility
  - https://www.ajot.com/news/electronic-bill-of-lading-adoption-grows-as-focus-shifts-to-interoperability
---

<!-- lead -->
Your tower's 3.0.0 feed is stuck until 2027. The Digital Container Shipping Association (DCSA) published the new version of its container tracking standard on 30 September 2026. It is the first version that carries sensor data. It also stays closed to non-members until the second half of 2027 [1].

The new event types are why it matters. One covers connected boxes: where a container is, when it crosses a fence, whether its door is open. The other covers refrigerated cargo: temperature, setpoint changes, power and alarms [1].

Twenty days later, on 20 October, the trade's own bill-of-lading survey landed. An electronic bill of lading (eBL) is the most standard document in container shipping. Just over half of respondents now use one, 51.1%. Yet 46.2% of the written answers named the same barrier: getting data from one platform into another [2].

Put the two dates together and the next bill in exception handling looks different from the usual one. Catching the event is no longer the hard part. Deciding which version of it counts is.

<!-- tension -->

## The big picture:

I keep coming back to the arithmetic inside the standard. Version 2.2.0 covered three kinds of event: shipment, transport and equipment. Version 3.0.0 adds two more [1].

Each new event comes from a different device, run by a different company, on its own clock. A fence ping, a door sensor and a reefer alarm can describe the same hour of the same box in three ways.

The bill-of-lading record hints at what happens next. Use rose from 49.2% in 2024 to 51.1% this year.

But only 11.2% of respondents dropped paper. Another 39.9% run both [2].

Among bank respondents, 75% still work on paper and none work only online [2].

So the barrier moved. It is no longer the law, which now recognises the document in many markets. It is the seam between systems, according to the Future International Trade (FIT) Alliance's own survey [2].

My read is that a standard fixes names, not authority. DCSA says as much: the same shipment event "might carry a different name, format or set of fields depending on who reports it" [1].

Common fields cut the mapping work. They do not settle which timestamp stands when the carrier, the terminal and the sensor disagree.

The queue behind that question is not shrinking. WiseTech's September outlook, reported by FreightWaves, found late delivery is now the most likely outcome on some Asia–North America lanes [5]. When a miss is the base case, a tower triages under disagreement. It does not chase a rare fault.

## By the numbers

- **51.1% — eBL use:** respondents using an electronic bill of lading, alone or with paper, up from 49.2% in 2024. Only 11.2% are fully electronic; 39.9% run both [2].
- **46.2% — the platform seam:** written answers that named interoperability and platform fragmentation, ahead of legal checks at 41.5% [2].
- **75% — banks on paper:** bank respondents who still rely on paper only. Another 22.2% use eBLs in part, and none use them alone [2].
- **3 → 5 — event types:** 2.2.0 covered shipment, transport and equipment. 3.0.0 adds connected-container and reefer events, with public release in the second half of 2027 [1].

<!-- tactical-insight -->

## What I'd watch:

- **Where the tie-break is written:** whether a tower publishes a rank order for carrier events, terminal gate-outs and device alarms, and whether its auditors accept that order.
- **The migration window:** DCSA shipped a guide with side-by-side comparisons and value mappings [1]. The member-only year is where carriers and platforms do the work, so the first public feeds will show whether the fields match.
- **Device economics:** reefer alarms only pay on cargo worth more than the hardware and the airtime. The desk's own field note has a pharma load saved by a 40-minute alert, and plenty of sensor data that never earns its fee.
- **The vendor repricing:** FourKites now sells outcomes rather than visibility. It claims one billion hours of agent work over the next decade, across 1,600+ brands and 500,000+ carriers [4]. Its chief executive calls the models a commodity. Price lists tend to agree with that in the end.
- **What a tower keeps:** the exception rules and the cost model under them. No standards body is drafting those.

<!-- nuanced-takeaway -->

## The catch

The part I keep circling is the sample. The survey rests on 190 cleaned records, gathered through the member networks of five trade bodies [3]. That is small, and the people who answer are already interested.

The 46.2% is a share of written answers, not of respondents. And a standard is not a switch. 3.0.0 is gated until 2027, and it also adds clearer rules for corrections and withdrawn events [1].

That last point cuts against my framing. If the new version says how a correction replaces an earlier event, part of the tie-break is already written.

What it does not say is whose event wins when two parties report the same moment differently. That argument stays with the carrier contract and the tower's own rule book.

The honest version: standards take cost out of the plumbing. The plumbing was never the expensive part once an exception was live.

<!-- tldr -->

## At a glance

- **The Big Shift:** DCSA published Track & Trace 3.0.0 on 30 September 2026, adding sensor and reefer event types to the container tracking standard, with public release held until the second half of 2027. Twenty days later, the FIT Alliance's eBL survey showed the industry's most standard document still stalls on moving between platforms.
- **Why It Matters:** Common field names cut a tower's mapping bill. They do not settle which party's event is the one that counts, and two more event types mean more versions of the same box to reconcile.
- **What I'd Watch:** The signals that will show whether the seam closes:
  - **Tie-break rules:** a written rank order for conflicting timestamps, so a dispute has an answer before the invoice does.
  - **Migration timing:** when carriers and platforms actually ship 3.0.0 output, since the public release is still a year out.
  - **Feed pricing:** whether visibility vendors keep charging for data they now call a commodity.
- **The Catch:** The survey rests on 190 self-reported records through member networks, and the standard's correction rules already cover part of the authority gap described above.

## Sources
[1] Digital Container Shipping Association, "DCSA publishes Track & Trace 3.0.0, expanding standard to cover IoT and reefer visibility", 30 September 2026 — https://dcsa.org/newsroom/track-and-trace-3-0-0-iot-reefer-visibility
[2] FIT Alliance 2026 global survey on electronic Bills of Lading, joint statement published 20 October 2026, carried by the American Journal of Transportation — https://www.ajot.com/news/electronic-bill-of-lading-adoption-grows-as-focus-shifts-to-interoperability
[3] Smart Maritime Network, "eBL adoption reaches 51% as interoperability becomes priority", 20 October 2026 (sample and fieldwork detail) — https://smartmaritimenetwork.com/2026/10/20/ebl-adoption-reaches-51-as-interoperability-becomes-priority
[4] FourKites, "FourKites launches Outcome-as-a-Service for supply chain", carried by the American Journal of Transportation, 15 October 2026 — https://www.ajot.com/news/fourkites-launches-outcome-as-a-service-for-supply-chain-backed-by-a-new-mission-and-more-than-a-decade-of-network-data
[5] FreightWaves, "Ocean Freight Risk: Late Is Now the Likely Outcome" (WiseTech/e2open Ocean Freight Risk Outlook, September data), 5 October 2026 — https://www.freightwaves.com/news/ocean-freight-risk-late-is-now-the-likely-outcome
