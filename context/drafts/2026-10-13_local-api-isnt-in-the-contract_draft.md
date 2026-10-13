---
title: "€1.2 Billion for Shelly: Your Local API Unwritten"
vertical: smart_home_telemetry
persona: pro_homeowner
one_big_thing: "The takeover promise protects Shelly's offices and staff until 31 December 2029 and never names the local interface, so the lasting part of a local-first home is the interface you can test on the day you buy, not the brand you trust."
date: 2026-10-13
slug: local-api-isnt-in-the-contract
synthesis: true
sources:
  - https://corporate.shelly.com/en/news/shelly-group-has-entered-into-an-investment-agreement-with-schneider-electric-on-the-intended-voluntary-public-takeover
  - https://www.home-assistant.io/blog/2026/10/07/release-202610
---

<!-- lead -->
Shelly Group agreed to a €1.2 billion takeover on 24 September. Its relays and power meters are the ones Home Assistant's own manual tells buyers to choose. The part of the deal that protects what those buyers already own is a promise about offices and staff. It says nothing about the local interface in their fuse box. That interface is the reason the manual names the brand at all.

The manual is blunt about why. Its energy page picks out one product, the Shelly EM (a clamp-on power meter), and gives the reason in a line: it "has a local API (the way one program talks to another), updates are pushed to Home Assistant and it has a high quality integration" [5]. Nobody bought the meter because its owner sat in Sofia. They bought it because it kept working when the internet did not.

<!-- tension -->

## The big picture:

I keep coming back to how these two weeks line up. Read the deal papers and the platform's own release notes side by side, and the two halves of a local-first home head in opposite directions.

Schneider is buying the hardware layer. Its bid is €70.00 a share in cash, 27% above the price the shares held before the talks leaked, and it needs 95% of them so it can buy out the rest and leave the exchange [1][2]. Its energy chief, Frederic Godemel, named the prize. Joining "Shelly's software-led home energy platform" to Schneider's reach would unlock "the next level of Energy Intelligence across residential, retrofit and small commercial buildings" [2]. Homes are the way in. Buildings are the prize.

Shelly's own papers tell the same story from the inside. The buyer's plan is for the firm to keep growing "from a connected-device company into a broader energy management and smart-building platform combining hardware, software, cloud-enabled services and ecosystem partnerships", with about €48 million of spending over five years [3]. The seller also notes that it already earns money "from its cloud applications" on top of device sales [1].

Then look at what the software did in the same week. Home Assistant 2026.10 landed on 7 October. In it, the map service the program leaned on began stamping an "API key required" note across its map images, which "broke every map in Home Assistant at once" [4]. The fix was not another outside supplier. It was to draw the maps from OpenStreetMap and keep a copy "through your Home Assistant instance, so your browser does not contact external tile servers directly" [4].

So in one fortnight the hardware went to a group that earns money from the cloud, and the software dropped an outside service it never controlled.

## By the numbers

- **€1.2 billion — Deal size:** Schneider's all-cash bid values Shelly at about €1.2 billion, at €70.00 a share, a 27% premium to the €55.2 the shares averaged before the talks leaked [1][2].
- **95% — Acceptance threshold:** the bid only wins if Schneider reaches 95% of the shares, the level that lets it buy out the rest and delist the firm [1][2].
- **31 December 2029 — The promise's end date:** the offer paper commits to keeping Shelly's head office, its factories and its footprint "for a period at least until 31 December 2029", and expects no change to staff numbers [3].
- **15 — New add-ons in the platform release:** the version that shipped on 7 October added 15 links to other gear, next to the map fix that moved that data path inside the home [4].

<!-- tactical-insight -->

## What I'd watch:

The gap I keep circling is a gap in the paperwork. The buyer's stated plans cover the head office, the factory floors, the payroll and even the firm's core trademarks for three years. The interface that made the product worth buying is not on that list, in either direction [3].

That is not an accusation. It is a description of what a corporate promise can hold.

- **Where the written promise stops:** a pledge to keep offices and jobs is dated and specific. A pledge to keep a local interface would need a line in the offer paper, and the only talk of holding on to local control so far comes from the two founders, not from the terms [3].
- **What a buyer can still check:** whether a device publishes a documented local interface, whether it speaks MQTT (the light messaging standard most home setups use) without an account, and whether it still works when the maker's servers are down. The manual sets that bar.
- **Which signals settle it:** the offer paper, once the Bulgarian regulator clears it; the firmware notes after the deal is due to close in the first quarter of 2027; and whether a future model asks for an account before it will talk to the house.
- **The next test case:** which other open-hardware brands get bought. Shelly was the obvious target, because it sells open gear into professional installs.

<!-- nuanced-takeaway -->

## The catch

None of this says the deal hurts anyone. Schneider has said it will keep the team, the factories and the managers in place, and a big owner brings supply reach and capital that a firm of Shelly's size cannot build on its own [3]. Local interfaces rarely vanish through a contract. They wear down through product choices over years, which is slower and quieter.

The other side of the argument cuts back. An open interface is no safety net on its own. A badly written link can be as brittle as a locked one, and the platform has its own record here: the map service that broke every map was a free outside tool, not a villain.

What I take from the fortnight is smaller than either view. A home built on local control rests on a chain of interfaces, and who owns each firm in that chain is a moving part. The interface is the bit you can still test on the day you pay.

<!-- tldr -->

## At a glance

- **The Big Shift:** Schneider agreed to buy Shelly Group for about €1.2 billion in cash, and in the same two weeks Home Assistant shipped a release that dropped an outside map service and kept that data inside the home.
- **Why It Matters:** the deal shields Shelly's offices, factories and staff until the end of 2029 but never names the local interface that made its meters the ones the manual recommends, so the backing for a local-first purchase is a brand promise rather than a paper term.
- **What I'd watch:** whether the offer paper adds any interface pledge once the Bulgarian regulator clears it, and whether the next firmware still works without a maker's account.
  - **Local interface:** a written way for your own software to talk to the device, which is what keeps it useful when the internet drops.
  - **Account-free running:** whether the device still works if the maker's servers are off, which is the part a promise cannot cover.
  - **Buyouts:** which other open-hardware brands get bought, since the same test applies to each of them.
- **The Catch:** the buyer says it will keep the team and spend about €48 million over five years, and open interfaces are rarely closed by a contract. They wear down through later product choices, so the risk shows up in future models, not in this deal.

## Sources
[1] Shelly Group SE, "Shelly Group Has Entered Into an Investment Agreement With Schneider Electric on the intended Voluntary Public Takeover supported by the founders," Corporate News, 24 September 2026 — https://corporate.shelly.com/en/news/shelly-group-has-entered-into-an-investment-agreement-with-schneider-electric-on-the-intended-voluntary-public-takeover
[2] Schneider Electric, "Schneider Electric announces a voluntary public takeover offer for Shelly Group supported by founders," 24 September 2026 — https://www.debevoise.com/-/media/document/2026/10/schneiderelectricannouncesavoluntarypublictakeover.pdf
[3] Shelly Group SE, "Registered with FSC of voluntary public tender offer by SE 2026 A SAS," Tender Offer announcement under Art. 151 POSA, 28 September 2026 — https://corporate.shelly.com/en/page/tender-offer
[4] Home Assistant, "2026.10: You are here," release notes, 7 October 2026 — https://www.home-assistant.io/blog/2026/10/07/release-202610
[5] Home Assistant, "Integrating your electricity grid," documentation — https://www.home-assistant.io/docs/energy/electricity-grid
[6] Shelly Group SE, Board of Directors' opinion on the registered offer, 5 October 2026 — https://markets.ft.com/data/announce/detail?dockey=600-202610051505DGAP____ADHOC____adhoc_2410688_en-1
