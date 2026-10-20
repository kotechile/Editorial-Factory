# Signals: control_tower_exception_orchestration — 2026-10-20
**Window:** 2026-09-20 → 2026-10-20
**Queries run:** 15 web fan-outs + 1 intel-MCP pull + 12 primary/trade fetches

Sweep anchor: the data layer the control tower sits on. Sources run: DCSA press room and standards
reference, the FIT Alliance 2026 eBL survey as released on 2026-10-20, FourKites' own announcement
carried by the American Journal of Transportation, FreightWaves (WiseTech/e2open Ocean Freight Risk
Outlook; 2026 AI Excellence awards), Kuehne+Nagel myKN weekly port operational update, Sea-Intelligence
/ WorldCargo News congestion outlook, plus the vertical's `supply_chain_intel` MCP feed
(`supply_chain_intel_client.py --recent 30 --vertical control_tower_exception_orchestration
--format signals`: 10 items, 5 of them sponsored Supply Chain Dive posts and the rest off-axis
maritime/parcel items). Date-agnostic fallback phrasing was used on every angle (the search backend
silently drops `after:`/`since:`); every row below was timestamp-checked against the window, and the
trade-press dates were read from each publisher's own WordPress REST `date` field where it allowed REST.

| # | Signal | Source URL | Date | Figure/Claim | Angle | Intensity |
|---|--------|-----------|------|--------------|-------|-----------|
| 1 | DCSA publishes Track & Trace 3.0.0, expanding the container visibility standard to IoT and reefer events | https://dcsa.org/newsroom/track-and-trace-3-0-0-iot-reefer-visibility | 2026-09-30 | Version 3.0.0 adds two event types: IoT events (geolocation, geofence crossing, door status) and reefer events (temperature, setpoint adjustments, power status, alarms); "will initially be made available to DCSA members and DCSA+ partners before being released to the public during the second half of 2027"; organisations on 2.2.0 "will need to plan and implement a migration", with a migration guide of comparisons, value mappings and implementation guidance; DCSA's own rationale — without a common standard "the same shipment event can be described differently by every supply chain party and platform that touches it" | Standard now carries condition data, but is member-gated for ~a year | 94 |
| 2 | FIT Alliance 2026 global eBL survey: adoption grows, focus shifts to interoperability (joint statement carried by AJOT) | https://www.ajot.com/news/electronic-bill-of-lading-adoption-grows-as-focus-shifts-to-interoperability | 2026-10-20 | 51.1% of respondents now use eBLs, exclusively or alongside paper, up from 49.2% in 2024; 39.9% run paper and electronic in parallel while 11.2% have gone exclusive; 93.8% call eBLs a key enabler of wider digitalisation; interoperability and platform fragmentation are the most-cited barrier, named in 46.2% of substantive open-ended responses, ahead of legal effectiveness and authenticity verification at 41.5% and implementation/onboarding at 41.5%; among bank respondents 22.2% report at least partial eBL use while 75% "continue to rely on paper only" and "no bank respondent reports using eBLs exclusively" | The one document the industry standardised still stalls at the platform seam | 93 |
| 3 | Smart Maritime Network report on the same 2026 eBL survey, with the sample | https://smartmaritimenetwork.com/2026/10/20/ebl-adoption-reaches-51-as-interoperability-becomes-priority | 2026-10-20 | The research was conducted with Shanghai Maritime University and the Digital Supply Chain Institute, "drawing on 190 cleaned survey records collected through FIT Alliance member networks"; the Alliance will focus its 2027 work on interoperability; 75% of bank respondents rely exclusively on paper | Sample size and methodology for row 2 | 84 |
| 4 | FourKites launches "Outcome-as-a-Service for Supply Chain" and drops the visibility product frame | https://www.ajot.com/news/fourkites-launches-outcome-as-a-service-for-supply-chain-backed-by-a-new-mission-and-more-than-a-decade-of-network-data | 2026-10-15 | Commits to using AI agents to "complete one billion hours of operational work for its customers over the next decade"; network graph of "1,600+ brands, 500,000+ carriers and 3.6 million facilities across 176 countries"; "a typical Fortune 2000 supply chain runs on 10 to 15 separate tools"; the product catalogue is replaced by "70+ outcomes"; CEO Mathew Elenjickal — "We founded real-time visibility to show customers where the problem was. Outcome-as-a-Service is how we solve it for them," and "AI models are becoming a commodity. What can't be copied is real-world network data and the context around it" | The largest visibility vendor stops selling visibility | 82 |
| 5 | WiseTech/e2open Ocean Freight Risk Outlook, September data, via FreightWaves | https://www.freightwaves.com/news/ocean-freight-risk-late-is-now-the-likely-outcome | 2026-10-05 | "Degrading execution and reliability — not capacity — is the defining risk in ocean freight right now"; on some Asia–North America lanes "a late delivery is now the most likely outcome, not the exception"; "some lanes that — being late is now the most likely case"; carrier selection is "a greater predictor of a good outcome than maybe the lane you're moving on"; a container arriving 30 days late is "probably the single highest impact" cost driver | Exception is the base case on the lane, not the tail | 80 |
| 6 | Kuehne+Nagel port operational update, 7–13 October 2026 | https://mykn.kuehne-nagel.com/news/article/port-operational-updates-from-13-10-2026 | 2026-10-13 | Seven-day average vessel waiting time: Conakry 13.33 days, Beira 9.33 days, Tema 5.59 days, Cotonou 4.0 days, Pointe Noire 3.77 days with yard occupancy "approximately 95%", Mombasa 2.5 days; a strike in Spain is forecast to disrupt supply chain activities nationwide; berth delays of 3–5 days persist as PSA terminals remain heavily congested | The exception queue is multi-region, not one port | 74 |
| 7 | Supply Chain Dive sponsored essay: visibility tells you what happened, not what it cost | https://www.supplychaindive.com/spons/supply-chain-visibility-tells-you-what-happened-can-you-see-what-it-cost/832819/ | 2026-10-19 | Illustrative example in the piece: a $2,000 expected freight cost against a $3,800 billed cost — "the invoice may be correct, but leaders need to explain the additional $1,800 and its root cause" | Sponsored: the cost gap after the event — not admissible as an anchor | 62 |

## Primary-source notes
- Row 1 is the primary record (dcsa.org press release, Amsterdam dateline 30 September 2026). The
  same release was read in full; the quotes above are verbatim from it. The standard itself sits at
  https://dcsa.org/standards/track-and-trace and the release notes `reference.dcsa.org` as the
  documentation home.
- Row 2 is the FIT Alliance joint statement as carried verbatim by the American Journal of
  Transportation on 2026-10-20 (the Alliance's own site had not posted the 2026 results at the time of
  the sweep: the page at https://www.fit-alliance.org/post/fit-alliance-ebl-report still carries the
  2024 edition, dated 12 Dec 2024 — do NOT quote the 2024 figures from it, they read 49.2% and are the
  prior edition). Row 3 (Smart Maritime Network) independently reports the same percentages and adds
  the sample of 190 cleaned records and the Shanghai Maritime University / DSCI fieldwork. The 2024
  edition's own numbers (32.2% intent to implement within two years; 94% awareness) are prior-edition
  figures and are excluded from the article.
- Row 4 is FourKites' own announcement; every figure is the company's own claim, not a measured
  outcome. It may corroborate the standards story ("AI models are becoming a commodity") but it can
  never serve as a dual-authority anchor beside a measured leg.
- Row 6 dates from the update's own week label (7 Oct – 13 Oct 2026); Kuehne+Nagel publishes one
  such update per week, so the week is named in the row rather than inferred.
- Row 7 is sponsored content (Supply Chain Dive "spons" path). Recorded because its $2,000/$3,800
  example is illustrative only; it is not cited in the artifact.

## Dated background (outside the window or non-anchor — URLs recorded so nothing downstream cites an unlisted link)
- Sea-Intelligence via WorldCargo News, "Asian port congestion could persist into mid-2027",
  2026-10 — global schedule reliability "below 50% for the first time since the pandemic", disruption
  unlikely to clear before the Chinese New Year peak in February 2027 —
  https://www.worldcargonews.com/news/2026/10/sea-intelligence-asian-port-congestion-could-persist-into-mid-2027
  (page date not retrievable from the article page or its REST API; the same reliability figure
  anchored the 2026-10-13 article for this vertical, so it is carried as context, never as an anchor).
- Linerlytica via The Maritime Executive, port congestion record of 4.31 million TEU stranded,
  2026-08-25 (outside the window) — https://maritime-executive.com/article/port-congestion-sets-new-record-at-4-3m-teu-in-stranded-volume
- Gartner, "60% of Supply Chain Disruptions Will Be Resolved Without Human Intervention by 2031",
  2026-03-18 (outside the window) —
  https://www.gartner.com/en/newsroom/press-releases/2026-03-18-gartner-predicts-60-percent-of-supply-chain-disruptions-will-be-resolved-without-human-intervention-by-2031
- NMFTA Digital Standards Development Council, "In-Transit Visibility Isn't a Data Problem—It's a
  Standardization Problem" — an LTL visibility API standard, undated on the page and not retrievable
  through the site's REST API (HTTP 401): https://nmfta.org/news/in-transit-visibility-isnt-a-data-problem-its-a-standardization-problem.
  Not admissible as a row; recorded only so the LTL thread can be checked next cycle.
- FreightWaves, 2026 AI Excellence in Supply Chain Awards (NFI's build-versus-buy framework,
  "reclaimed more than 100 hours per..."), published 2026-07-16 (outside the window) —
  https://www.freightwaves.com/news/2026-ai-excellence-in-supply-chain-awards-winners

## Candidate Synthesis Pairs


<!-- synthesis-seed:start -->
<!-- pair-seeding: helper=synthesize_topics.py rows=7 candidates=0 heuristic=- window=2026-09-20..2026-10-20 -->
> Advisory: mechanical pre-filter only. The Judge (`skills/virality_judge.md` §2.5) owns the collision vector
> and the >= 8 publish gate. `emergence_heuristic` is a hint, not a score; it cannot clear any gate.
> Seeded mechanically from this file's own rows by `python3 scripts/synthesize_topics.py --seed <this file>`; re-run it after adding or removing a signal row. The Judge scores the rows and writes the collision vector per `skills/virality_judge.md` §2.5.

_No mechanically valid pair. That is a legitimate answer, not a failure: the Judge may still find a synthesis this token layer cannot see._
<!-- synthesis-seed:end -->

