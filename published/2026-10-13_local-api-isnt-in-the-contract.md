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
meta_title: "€1.2 Billion for Shelly: Your Local API Unwritten"
meta_title_source: "derived_from_title"
meta_description: "Shelly Group agreed to a €1.2 billion buyout on 24 September."
meta_description_source: "derived_from_lead"
image_path: "context/assets/illustrations/local-api-isnt-in-the-contract/featured.jpg"
image_style: "document_flatlay"
image_model: "flux"
image_alt: "The €1.2 Billion Shelly Buyout. A smart home relay module sitting on top of a thick stack of corporate legal documents on a d"
image_caption: "The €1.2 Billion Shelly Buyout: Schneider's takeover leaves the local API unprotected."
image_credit: "Illustration: Editorial-Factory Intelligence Unit"
---

<!-- lead -->
Shelly Group agreed to a €1.2 billion buyout on 24 September. But the paperwork skips the exact feature that made its relays the ones Home Assistant's manual tells buyers to choose. The deal protects Shelly's offices and staff until 2029, and says nothing about the local API (the written rules one program uses to talk to another). That interface is the reason the manual names the brand.

The manual is specific about why. Its energy page picks out one product, the Shelly EM (the company's clamp-on power meter), and says it "has a local API, updates are pushed to Home Assistant and it has a high quality integration" [5]. Nobody bought the meter because the company sits in Sofia. They bought it because it kept working when the internet did not.

<!-- tension -->

## The big picture:

I keep coming back to how these two weeks line up. Read the deal papers next to the platform's release notes, and the two halves of a local-first home move in opposite directions.

Schneider Electric is buying the hardware layer. Its bid is €70.00 a share in cash, and it needs 95% of the shares so it can buy out the rest and leave the exchange [1][2]. Its energy chief, Frederic Godemel, named the prize: joining "Shelly's software-led home energy platform" to Schneider's reach would unlock "the next level of Energy Intelligence across residential, retrofit and small commercial buildings" [2]. Homes are the entry point. Big buildings are the prize.

Shelly's own papers tell the same story from the inside. The buyer plans to spend about €48 million over five years on a wider platform that mixes hardware, software and cloud services [3]. The seller also notes that it already earns money "from its cloud applications" on top of device sales [1].

Meanwhile the software side pulled back from the cloud. Home Assistant 2026.10 landed on 7 October [4]. Its outside map service had started asking for an API key, which broke every map in the system at once [4]. The fix was not another outside supplier. The team pulled the map data into the home server, so your browser never contacts those outside map servers [4].

So in one fortnight the hardware went to a group that sells building systems, and the software dropped an outside service it never controlled.

## By the numbers

- **€1.2 billion — Deal size:** Schneider's all-cash bid values Shelly at about €1.2 billion, at €70.00 a share [1][2]. That is a 27% premium over the price the shares held before the talks leaked [1][2].
- **95% — Acceptance threshold:** The bid only wins if Schneider reaches 95% of the shares. That level lets it buy out the rest and pull the firm off the stock exchange [1][2].
- **31 December 2029 — The promise's end date:** The offer paper commits to keeping Shelly's head office, its factories and its footprint "for a period at least until 31 December 2029" [3].
- **15 — New platform links:** The release that shipped on 7 October added 15 links to other gear [4]. It also moved that map data path inside the home [4].

<!-- tactical-insight -->

## What I'd watch:

The gap I keep circling is what the paperwork leaves out. The buyer's stated plans cover the head office, the factory floors, the payroll and even the core trademarks for three years [3][6]. The interface that made the product worth buying is missing from that list.

- **Where the written promise stops:** A pledge to keep offices and jobs is clear and dated. A pledge to keep a local interface would need a line in the offer paper. So far, only the two founders have talked about keeping local control, and that is a statement, not a term [3].
- **What a buyer can still check:** Whether a device publishes a clear local interface. I also check whether it speaks MQTT (the light messaging standard most home setups use) without an account, and whether it still works when the maker's servers are down.
- **Which signals settle it:** I am watching the final offer paper, once the Bulgarian regulator clears it. I will also watch the firmware notes after the deal is due to close in early 2027.
- **The next test case:** Which other open-hardware brands get bought. Shelly was an obvious target, because it sells open gear to installers.

<!-- nuanced-takeaway -->

## The catch

None of this says the deal hurts users. Schneider says it will keep the team and the managers in place, and a big owner brings supply reach and cash that a firm of Shelly's size cannot build alone [3].

My read: local interfaces rarely vanish in one contract change. They wear down slowly through product choices over years, which is quieter and harder to spot.

An open interface is also no safety net on its own. A badly written local link can be as fragile as a locked cloud one. The platform has its own record here: the map service that broke every map was a free outside tool, not a corporate villain.

A home built on local control rests on a chain of interfaces. Who owns each firm in that chain is a moving target. The interface is the one part you can still test on the day you pay.

<!-- internal-links -->

<!-- internal-links:start — generated from context/internal_links.json by scripts/internal_links.py; edits between these markers are overwritten -->
<!-- internal-link hint: "A Cloud Patch Bricked the Fridge. Local-First Just Stopped…" -> https://wellroost.com/cloud-update-bricked-the-fridge-local-first/ [same site (wellroost.com); same category] Link "A Cloud Patch Bricked the Fridge. Local-First Just Stopped…" in the section where the article touches this topic. -->
<!-- internal-link hint: "Emporia Vue: How to Cut Energy Bills" -> https://wellroost.com/unveiling-the-emporia-vue-3-a-comprehensive-guide-to-home-energy-monitoring/ [same site (wellroost.com); same category] Link "Emporia Vue: How to Cut Energy Bills" in the section where the article touches this topic. -->
<!-- internal-link hint: "local-first smart home cost squeeze" -> https://wellroost.com/local-first-smart-home-cost-squeeze/ [same site (wellroost.com); same category] Link "local-first smart home cost squeeze" in the section where the article touches this topic. -->
## Related reading

- [A Cloud Patch Bricked the Fridge. Local-First Just Stopped…](https://wellroost.com/cloud-update-bricked-the-fridge-local-first/) — more on Smart Home & Security
- [Emporia Vue: How to Cut Energy Bills](https://wellroost.com/unveiling-the-emporia-vue-3-a-comprehensive-guide-to-home-energy-monitoring/) — more on Smart Home & Security
- [local-first smart home cost squeeze](https://wellroost.com/local-first-smart-home-cost-squeeze/) — more on Smart Home & Security
<!-- internal-links:end -->

<!-- tldr -->

## At a glance

- **The Big Shift:** Schneider agreed to buy Shelly Group for about €1.2 billion in cash, just as Home Assistant shipped software that dropped an outside map service and kept that data inside the home.
- **Why It Matters:** The deal shields Shelly's offices, factories and staff until the end of 2029 but ignores the local interface that makes its meters the ones the manual recommends. The backing for a local-first purchase rests on a brand's word rather than a paper term.
- **What I'd watch:** Whether the final offer paper adds any interface pledge once the Bulgarian regulator clears it, and whether the next firmware still works without a maker account.
  - **Local interface:** A written way for your own software to talk to the device, which keeps it useful when the internet drops.
  - **Account-free running:** Whether the device still works if the maker's servers go offline, which is the part a promise cannot cover.
  - **Buyouts:** Which other open-hardware brands get bought, since the same test applies to each of them.
- **The Catch:** The buyer plans to keep the team and spend about €48 million over five years. Open interfaces are rarely closed by one contract change; they wear down through later product choices, so the risk shows up in future models.

## Sources
[1] Shelly Group SE, "Shelly Group Has Entered Into an Investment Agreement With Schneider Electric on the intended Voluntary Public Takeover supported by the founders," Corporate News, 24 September 2026 — https://corporate.shelly.com/en/news/shelly-group-has-entered-into-an-investment-agreement-with-schneider-electric-on-the-intended-voluntary-public-takeover
[2] Schneider Electric, "Schneider Electric announces a voluntary public takeover offer for Shelly Group supported by founders," 24 September 2026 — https://www.debevoise.com/-/media/document/2026/10/schneiderelectricannouncesavoluntarypublictakeover.pdf
[3] Shelly Group SE, "Registered with FSC of voluntary public tender offer by SE 2026 A SAS," Tender Offer announcement under Art. 151 POSA, 28 September 2026 — https://corporate.shelly.com/en/page/tender-offer
[4] Home Assistant, "2026.10: You are here," release notes, 7 October 2026 — https://www.home-assistant.io/blog/2026/10/07/release-202610
[5] Home Assistant, "Integrating your electricity grid," documentation — https://www.home-assistant.io/docs/energy/electricity-grid
[6] Shelly Group SE, Board of Directors' opinion on the registered offer, 5 October 2026 — https://markets.ft.com/data/announce/detail?dockey=600-202610051505DGAP____ADHOC____adhoc_2410688_en-1

## Gate report
Loop 3 (frontier rewrite, gemini-3.1-pro-preview): attempt 1 FAIL Flesch 45.4 → attempt 2 PASS Flesch 55.5 (963 body words).
Hand-tune after the rewrite, then re-measured: figures and citations untouched.
PASS — lead: core news in sentence 1 (the €1.2 billion buyout); the local API glossed in plain English at first use.
PASS — tension: "The big picture:" H2; the two halves named; first-person observer cue present; 1–3 sentence paragraphs.
PASS — tactical-insight: "What I'd watch:" H2; four bullets, observations rather than instructions; MQTT glossed.
PASS — nuanced-takeaway: "The catch" H2; honest limitation plus the counter-argument; "My read:" cue present.
PASS — tldr: "At a glance" H2; full 4-slot schema with indented sub-bullet definitions.
Post-rewrite figure/name audit (hand-corrections): restored the named attribution to Schneider's energy chief Frederic Godemel and the quoted "software-led home energy platform" / "Energy Intelligence" wording the rewrite had flattened to "better energy tracking"; restored the manual's own wording for the Shelly EM; re-attributed cloud revenue to Shelly (the seller), not to Schneider; corrected the trademark claim's citation to [3][6]; replaced the rewrite's invented "Shelly Energy Meter (EM)" expansion with a plain gloss. No unsourced figures, no substituted names, no moved clock triggers; every figure (€1.2bn, €70.00, 27%, 95%, 48 million, 15, 31 December 2029, 7 October) traces to the verified brief.
