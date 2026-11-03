# Signals: smart_home_telemetry — 2026-11-03
**Window:** 2026-10-04 → 2026-11-03
**Queries run:** 16 (9 date-agnostic web fan-outs across the vertical's six configured sources and five primary angles; 1 Hacker News Algolia `search_by_date` sweep against the window epoch plus four keyword follow-ups; 1 GitHub/HN pass on Home Assistant release material; 1 intelligence-MCP pull via `home_lifestyle_intel_client.py --recent 30 --vertical smart_home_telemetry --format signals`, which returned 10 rows — Remodelista interiors, Canary Media tribal-energy and data-center-battery pieces, Redfin mortgage rates, one Ars Technica e-paper gadget — none on the local-first/telemetry beat, so none was used; 4 primary-source fetches and 1 publisher date check).

**Window note (freshness discipline — what was dropped, not softened).**
- **The Marketplace move** (HACS → Home Assistant Marketplace, 2026.11) was published as `your-hubs-4292-project-blind-spot` on 2026-10-27 and is a retread here; 2026.11 is used below only for its *telemetry* features, and the angle brief says why that is a different thesis.
- **Germany's smart-meter rollout analysis** is dated 2026-10-04 but its figures are the Federal Network Agency's data **as of 30 June 2026**; carried as a runner-up row with its as-of date in the claim cell, never as a load-bearing anchor.
- **Sense's D2C exit** remains 2025-11-03 (out of window); **SmartThings' $4.99 API plan** remains a June 2026 announcement (out of window). Both re-surfaced in search and were dropped again.
- **Zigbee temperature-sensor comparison** (SmartHomeScene) was submitted to Hacker News on 2026-10-04 but carries the publisher's own "UPDATED 14.08.2026" stamp; the article predates the window and was dropped.
- Also read and set aside: Apple HomeView / Home Collection (2026-10-13, the Apple-home story already argued in `your-locks-blind-90-bet`), Amber/Octopus tariff material with no fetchable primary, and a Techanvio-style "best energy monitor" roundup with no first-party numbers.

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | KRGV — "New Brownsville PUB program will notify customers of water leaks" | https://www.krgv.com/news/new-brownsville-pub-program-will-notify-customers-of-water-leaks | 2026-10-20 | The utility starts leak notifications on **Nov. 1, 2026** off its AMI meters. Spokesperson Alexa Perez, verbatim: "whenever our system notices that a customer is using water for prolonged periods of time, we're going to be providing a notification to them via text or via email"; "This notification will be **every 24 hours, weekly, or biweekly depending on the consumption**." Messages come from 96681 or a no-reply BPUB address and "will not ask for money." | The alert is a notification schedule with a daily floor, not a continuous detector | 90 |
| 2 | BPUB — Advanced Meter Infrastructure project page | https://www.brownsville-pub.com/projects/advanced-meter-infrastructure | 2026-11-03 (observation; standing page) | The utility's own page promises AMI "enabling real-time usage monitoring"; under Benefits: "**Daily Usage Data** — Monitor your electric and water usage daily through your online account" and "**Leak Detection** — Identify potential water leaks early through continuous usage monitoring". Timeline: initial deployment April 2025, "April 2027 — Full system deployment areas for water and electric". "There is no direct cost to customers for the meter replacement." | The same page sells a real-time meter and a daily product; the cadence is a policy, not a sensor limit | 86 |
| 3 | Kurrant — Brownsville adds water leak alerts to smart-meter rollout | https://kurrant.com/kurrantly-news/brownsville-public-utilities-board-adds-water-leak-alerts-to-smart-meter-rollout | 2026-10-22 | The AMI project "covers about **52,000 electric meters and about 58,000 water meters**, according to a City of Brownsville notice, as part of a **$29.7 million** infrastructure investment". A city progress report presented to the Commission on 2026-09-01 put completion "around **May 2027**" (the BPUB page says April 2027 — both recorded; the discrepancy is a FLAGGED row). | The capital scale behind one daily text | 78 |
| 4 | Home Assistant 2026.11 beta — "Reach the far corners with LoRaWAN" | https://rc.home-assistant.io/blog/2026/10/28/release-202611/ | 2026-10-28 | "LoRaWAN is a long-range, low-power wireless protocol, often used for battery-powered sensors in places your Wi-Fi never reaches, like a garden, a shed, or a field. **Home Assistant now speaks it.**" Connect "ChirpStack … or The Things Network", and the matching device integration (SenseCAP) appears when a supported device shows up. A new **LoRaWAN** page (Settings > Connectivity) shows connections, a device table, a gateway map, and per device "signal strength, the last time it reported in, and its battery". | The local hub absorbs the long-range, battery-powered sensor layer | 92 |
| 5 | Home Assistant 2026.11 beta — "Batteryless switches with Zigbee Green Power" | https://rc.home-assistant.io/blog/2026/10/28/release-202611/ | 2026-10-28 | "Zigbee Home Automation now supports Zigbee Green Power. These are the devices that run without a battery: a wall switch powered by the energy of your press, or a sensor that lives off the light in the room. Friends of Hue switches are the best-known example. Until now, Home Assistant passed them by." | A sensor that never needs its battery changed can live where leaks start | 84 |
| 6 | Home Assistant — The Things Network integration docs | https://www.home-assistant.io/integrations/thethingsnetwork | 2026-11-03 (observation; standing doc) | "This community-driven and open network supports LoRaWAN for long-range (**~5 to 15 km**) communication with low bandwidth (**51 bytes/message**)." | The envelope: kilometres of reach, tens of bytes a message — a leak signal fits inside it | 72 |
| 7 | heise online — Smart meter rollout in Germany continues to be slow | https://www.heise.de/en/news/Smart-meter-rollout-in-Germany-continues-to-be-slow-11475320.html | 2026-10-04 | Analysis by the Smart Meter Initiative from Federal Network Agency data for **H1 2026**: at end-June, "just over a quarter of mandatory installations (**26 percent**) were equipped with intelligent metering systems"; across all metering points the installation rate is "**5.9 percent**", up 0.4 points on the prior period; among the ten largest operators mandatory-case rates run **24 to 60 percent** (Berlin and Westnetz 60%, Netze BW 24%). Figures are as of 30 June 2026, not the publication date. | The regulated meter layer is not arriving on schedule anywhere | 76 |
| 8 | Consumer Reports Innovation — "Connected devices rob consumers of ownership. We have a fix." | https://innovation.consumerreports.org/11663-2 | 2026-10-08 | Consumers "have no idea how long they can expect manufacturers to maintain or secure the features enabled by connectivity"; CR's model **Connected Device Longevity Act** would require manufacturers to disclose support life and require businesses such as ISPs and alarm companies to remove devices when security updates stop. No US state yet requires the disclosure at purchase. | Ownership is the same question one layer down: nobody has to tell you when the thing stops working | 70 |

## Dating note
Rows 1, 3, 4, 5, 7 and 8 carry the publisher's own date inside the window (KRGV 2026-10-20; Kurrant 2026-10-22; the 2026.11 beta notes 2026-10-28; heise 2026-10-04; Consumer Reports 2026-10-08). Rows 2 and 6 are standing pages with no publication date: their Date cell is the **observation date** (2026-11-03), and the event they describe is stated inside the claim cell. Row 7's figures are dated **as of 30 June 2026** in the claim cell and are not treated as October data.

## Primary sources (corroboration — every URL an artifact may cite must appear in this file)

Brownsville leg:
- https://www.krgv.com/news/new-brownsville-pub-program-will-notify-customers-of-water-leaks
- https://www.brownsville-pub.com/projects/advanced-meter-infrastructure
- https://www.brownsvilletx.gov/CivicAlerts.aspx?AID=2888 (City of Brownsville notice, posted 2025-12-15: "approximately 52,000 electric meters and 58,000 water meters", "$29.7 million infrastructure investment", "receive quicker notifications for issues like water leaks")
- https://kurrant.com/kurrantly-news/brownsville-public-utilities-board-adds-water-leak-alerts-to-smart-meter-rollout
- https://www.prnewswire.com/news-releases/brownsville-public-utilities-board-receives-5-million-watersmart-grant-301837607.html (2023-05-31: $5M WaterSMART grant; 17,500 manual-read meters replaced, ~40,000 retrofitted)

Home Assistant leg:
- https://rc.home-assistant.io/blog/2026/10/28/release-202611/
- https://www.home-assistant.io/integrations/thethingsnetwork
- https://www.home-assistant.io/integrations/chirpstack (integration page named in the beta notes)
- https://www.home-assistant.io/integrations/sensecap_lorawan

## Dated background (not anchors — outside the window or not citable, kept for provenance)
- https://www.instagram.com/reel/Dez0hyEhd10 (BPUB's own post, 2026-10-22: "if our smart meters detect 24 hours of uninterrupted water flow, you'll be able to get a heads-up alert" — a social post, blocked as a citation; the same cadence is carried by KRGV's quoted spokesperson, which is the citable record)
- https://www.yahoo.com/news/us/articles/water-utility-text-customers-possible-234500113.html (syndicated write-up of the same KRGV report; aggregation, not a source of record)
- https://btxtoday.com/bpub-smart-meter-leak-alerts-november-2026 (local write-up, same quote)
- https://www.publicpower.org/periodical/article/brownsville-public-utilities-board-announces-launch-ami-smart-meter-program (2025-04 launch announcement; background)
- https://www.wsscwater.com/smart-pilot (WSSC Water AMI pilot: transmitters send "up to four times per day on weekdays and once per day on weekends" — an example of the network cadence being a design choice, not a sensor limit; standing page, observation only)
- https://www.heise.de/en/news/Smart-meter-rollout-in-Germany-continues-to-be-slow-11475320.html (runner-up, figure as of 2026-06-30)
- https://innovation.consumerreports.org/11663-2 (runner-up)
- https://advocacy.consumerreports.org/press_release/consumer-reports-us-pirg-and-secure-resilient-future-foundation-propose-connected-consumer-products-end-of-life-disclosure-act-to-address-iot-security-risks (the model bill, 2026-09-29)

## Candidate Synthesis Pairs

<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=8 candidates=0 heuristic=- window=2026-10-04..2026-11-03 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->
