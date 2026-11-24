# Evergreen Brief: nhil_infrastructure_ops — 2026-11-24

**Archetype:** evergreen
**Vertical:** nhil_infrastructure_ops
**Persona:** it_ops_leader
**Decision the reader is facing:** When to commit money to the utility feed for a site the racks will fill in 2029 — enter the transmission interconnection queue now and budget for the odds that the request never becomes a live feed, or bridge behind the meter — because the queue's own math, not the hardware roadmap, sets the clock, and the commitment bites at the application deposit and the substation engineering order, years before the first GPU lands.
**Durability:** The queue arithmetic is structural, not a news cycle: the duration doubling is measured across 2000–2024 cohorts, the completion and withdrawal rates are cumulative outcomes of requests submitted 2000–2019, and PJM's post-reform study pace is a fixed regulatory record — none of it moves with a GPU generation. Figures are as of the LBNL Queued Up 2025 edition (queue data through end-2024), RMI's PJM analysis as of its November 11, 2025 update, and LatitudeMedia's read of the 2024-edition queue data published in 2024.
**De-dup:** `2026-11-24_nobody-owns-your-ais-power-feed` is this vertical's nearest prior artifact — it argues improvised behind-the-meter generation (xAI's converted jet engines) as a news synthesis; this piece argues the queue itself, a different mechanism: the measured duration, completion and withdrawal arithmetic of waiting for the utility feed. `2026-11-03_your-backup-66-mw-permit-trap` prices the air-emissions permit ladder and `2026-11-17_your-1320-gallon-blind-spot` the fuel-storage regime — both downstream compliance, not the queue. Cross-vertical corpus grep for `interconnection queue`, `Queued Up`, `substation`, `cluster study` found no other published artifact arguing the queue's math.
**Thesis:** The transmission interconnection queue is the binding clock on every AI build — the median wait from request to live connection has doubled from under two years to over four, roughly three-quarters of the capacity that ever applied withdrew without a live feed, and a 100 MW+ feed averages 55 months — so the substation decision is a five-year capital commitment made against withdrawal odds today, not an electrical detail settled when the racks are ordered.

**Lead:** The vertical's own power angle (`primary_angles`: "substation interconnection queues and behind-the-meter power") plus `context/growth_os/founder-voice.md` §3 ("utility grid interconnection queues backed up 3 to 5 years") and `context/growth_os/customer-truth.md`'s 38-month substation queue anecdote. The 11/24 news run took the improvised-generation story; the queue's own measured arithmetic — the thing the founder voice asserts from experience — has never been argued from primary data. All anchors fetch with the factory verifier (probed 2026-11-24; `emp.lbl.gov` itself 403s, so the report's abstract on OSTI carries its figures).

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | LBNL, Queued Up: 2025 Edition — abstract, OSTI | https://www.osti.gov/biblio/3008763 | 2026-11-24 | over 4 years — the median duration from interconnection request to commercial operations, doubled from under 2 years for projects built 2000–2007 to over 4 years for those built 2018–2024 | measured |
| 2 | LBNL, Queued Up: 2025 Edition — abstract, OSTI | https://www.osti.gov/biblio/3008763 | 2026-11-24 | 77% — of the capacity that submitted interconnection requests from 2000–2019 had been withdrawn by the end of 2024; only 13% had reached commercial operations and 10% was still active | measured |
| 3 | LBNL, Queued Up: 2025 Edition — abstract, OSTI | https://www.osti.gov/biblio/3008763 | 2026-11-24 | 408 GW — of capacity already held a draft or executed interconnection agreement without reaching commercial operations as of end-2024 | measured |
| 4 | RMI, PJM's Speed to Power Problem | http://rmi.org/resources/pjms-speed-to-power-problem-and-how-to-fix-it | 2026-11-24 | eight years — the time it now takes to bring new generation online in PJM, against auctions run on a two- to three-year horizon | measured |
| 5 | RMI, PJM's Speed to Power Problem | http://rmi.org/resources/pjms-speed-to-power-problem-and-how-to-fix-it | 2026-11-24 | 544 days — the duration of PJM's completed TC1 cluster-study cycle, filed against a 540-day study allowance | measured |
| 6 | LatitudeMedia, on LBNL's 2024-edition queue data | https://www.latitudemedia.com/news/the-us-interconnection-queue-is-twice-its-installed-capacity | 2026-11-24 | 55 months — the median interconnection request to commercial-operations span for projects over 200 MW, against 4+ years for projects over 100 MW and 30 months or more past the 20 MW line | measured |
| 7 | LatitudeMedia, on LBNL's 2024-edition queue data | https://www.latitudemedia.com/news/the-us-interconnection-queue-is-twice-its-installed-capacity | 2026-11-24 | five years — the queue span of the average renewable project built in 2023, versus three years in 2015 and less than two years in 2008 | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| The interconnection queue is the build clock: commit against withdrawal odds | 9 | 9 | 9 | 8 | 8.8 | **winner** |
| Closed-loop remediation telemetry boundaries (out-of-band verification) | 8 | 8 | 6 | 7 | 7.4 | dropped — the 2026-10-13 remediator piece already argues the gate outside the agent, and the out-of-band numbers are vendor claims |
| Sovereign SLM confidential-compute tax, updated | 8 | 9 | 5 | 6 | 7.0 | dropped — the 2026-11-17 0.086ms piece and the 62.8% enclave piece already carry this beat's measured anchors |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=7 fetched=7 sources=3 hosts=3 decision="sha1:d161e7345c" dedup="matched a prior artifact: 2026-11-24_nobody-owns-your-ais-po" window_days=180 checked_at=2026-11-24T18:03:19+00:00 -->
<!-- evergreen-gate:end -->
