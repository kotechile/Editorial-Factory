# Angle Brief: supply_chain — 2026-11-05

**Angle Type:** Synthesis (Cross-Topic Fusion)
**Winner:** "The bottleneck moved a thousand miles inland" — the record import months at Los Angeles and Long Beach are being absorbed inland at the fastest quarterly rate since early 2023, and the rail leg that has to carry that freight is the only part of the chain now holding inventory: 35,688 containers waiting for on-dock trains, 29.6% of them nine days or older, while the boxes that leave by truck clear in 3.18 days.
**Scores:** E=9 A=9 S=9 → **Composite=9.0** (≥ 8.0 gate cleared)
**Signal A (Anchor 1):** FreightWaves, 2026-10-28 — https://www.freightwaves.com/news/backlog-grows-as-35000-containers-await-rail-service-at-la-long-beach — 35,688 import containers awaiting on-dock trains at the two ports on Oct. 26; 10,562 on the terminals nine days or longer; Los Angeles 8,133 of 19,626 (41.4%) against Long Beach 2,429 of 16,062 (15.1%); Pacific Merchant Shipping Association average rail-container dwell 7.19 days in September from 6.75 in August, against 3.18 days for truck-departing boxes from 2.95.
**Signal B (Anchor 2):** Cushman & Wakefield, U.S. Industrial MarketBeat Q3 2026, released 2026-10-14 — https://www.cushmanwakefield.com/en/united-states/insights/us-marketbeats/us-industrial-marketbeat — net absorption 76.6 msf, highest since Q1 2023; year-to-date 203 msf, 69% above the first three quarters of 2025; **inland markets 80% of YTD absorption**; vacancy 6.8% from the late-2025 peak of 7.0%; asking-rent growth 4%; 64 msf delivered in the quarter, 185 msf YTD (13% behind last year), pipeline 324 msf.
**Emergent Collision Point:** Both documents describe one pipeline from opposite ends and neither states the joint fact. The throughput the ports celebrate (September: 1,042,652 TEU at Los Angeles, 997,177 at Long Beach) is increasingly *not* staying at the coast — four-fifths of the year's warehouse absorption happened inland — so a larger share of every vessel has to leave the dock by train. That is precisely the leg the second document does not measure and the first document shows failing: rail-bound containers sit 7.19 days against 3.18 for truck-bound ones, and at Los Angeles 41.4% of the rail inventory is nine days or older. The constraint has migrated from berth capacity (ships are not queueing) to railcar supply and inland ramp capacity, which are set by where the empty boxes and the cars have to come back from — inland. A shipper watching the port's vessel queue sees nothing; a shipper watching average port dwell sees a number that is only 2.3x its truck equivalent; a shipper watching *the age distribution of the rail inventory* is the only one who sees the delay before it hits their line.
**Hook:** The busiest month in the two ports' history left almost no ships waiting offshore — and 35,688 containers parked on the dock, a third of them on their second week.

## Candidate scoring (§2.2 / §2.5)

| Candidate | N/U | A | S | Composite | Verdict |
|---|---|---|---|---|---|
| **Synthesis: rail-leg backlog ⨂ inland absorption** | E9 | A9 | S9 | **9.0** | **Adopted.** Margin over the best single-signal candidate is +0.6, above the 0.3 precedence floor. |
| A alone: the on-dock rail backlog and its age split | 8.5 | 8.5 | 8.0 | 8.4 | Runner-up. Strong and unreported, but the number has no consequence attached until you know where the boxes are going. |
| F alone: the 250 watchmen at the gate (row 6) | 8.0 | 7.5 | 8.5 | 8.0 | Runner-up. A live labour risk, not a mechanism a reader can act on this week; the deadline moved twice inside the window and is unresolved. |
| E alone: Q3 truck spend +32.1% on +0.5% volume (row 5) | 7.0 | 9.0 | 8.0 | 7.9 | Dropped on §3.5: `parcel-fuel-percentage-weekly-january` (10-29) already argued price-up-on-flat-volume, one week ago on the same front. Novelty capped at 7. |
| B alone: inland absorption / vacancy / rents | 7.0 | 9.0 | 7.0 | 7.6 | Runner-up leg; too slow and too broker-flavoured to carry a news slot alone. |
| C+D alone: the two September records | 6.5 | 9.0 | 6.5 | 7.3 | Dropped: a record month is a press release, and both ports published theirs inside the window with no consequence attached. |
| Row 7: Georgia inland hub, 26,000 containers | 7.0 | 7.0 | 7.0 | 7.0 | Dropped: it is the *remedy* for the adopted thesis, and folding it in as evidence would overstate one state programme's scale. |
| Row 8: 3M's 16 closures and 10 more | 6.5 | 8.0 | 6.5 | 6.9 | Dropped: a single company's network programme; it would make the piece a case study rather than a mechanism. |

**Seeder result, recorded as input (not a verdict):** `synthesize_topics.py --seed` returned `rows=8 candidates=0` — "no valid pair". This is the documented measurement-collision case in `virality_judge` §2.5: the two legs collide on a *quantity of time* (a dwell distribution against an absorption share) and share no archetype vocabulary, so the token layer cannot see it by construction. The pair is therefore asserted by the Judge, and the zero-candidate result is carried here rather than treated as an absence of a story.

**Precedence (§2.5):** synthesis 9.0 against the best single-signal candidate at 8.4 → margin +0.6 ≥ 0.3. Adopted.

**De-dup (§3.5):** within this vertical's 30 days, `suez-returns-91-surcharge-doesnt` (10-22) is about a carrier's per-TEU surcharge outliving a capacity change at sea; `parcel-fuel-percentage-weekly-january` (10-29) is a USPS surcharge mechanism plus a UPS price/volume split; `your-carriers-750000-doesnt-cover-cargo` (10-29, evergreen) is cargo-liability instruments; `fuel-surcharge-peg-mpg-audit` (10-08, evergreen) is a truckload fuel peg. None measures post-discharge rail evacuation or the geography of warehouse absorption. Across the shared `aichieve.net` front the last seven days are agent-runtime, MCP-security and resilience pieces; nothing touches physical freight. Desk-wide figure check: `35,688`, `7.19`, `1,042,652` and `997,177` appear in no published artifact.

## Carry-through obligations

- `synthesis: true` in the artifact frontmatter, with **both** anchors under `sources:`.
- `kind: news` (news run, 30-day window; `evergreen` is the other track and is not this one).
- Numbers section carries **one figure from each anchor** (a rail-dwell or backlog figure, and an inland-absorption figure) — the known failure is a rewrite that rebuilds "By the numbers" from one leg.
- The article must not claim causation the sources do not state. C&W says inland markets drove 80% of absorption and that trade policy is reinforcing inland strategies; FreightWaves says railcar shortages and empty repositioning are slowing inland movement. The piece may juxtapose them and describe the mechanism (inland-bound boxes need rail; rail is the slow leg); it may **not** say the inland shift caused the backlog, and it must carry FreightWaves' own caveat that the Oct. 26 counts are a point-in-time inventory, not an average wait.

## Desk arithmetic to verify before drafting (computed in-session, printed endpoints only)

- 10,562 ÷ 35,688 = 29.6% of the rail inventory is nine days or older.
- 7.19 ÷ 3.18 = 2.26x, rail dwell over truck dwell, September.
- Los Angeles: 8,133 ÷ 19,626 = 41.4%; Long Beach: 2,429 ÷ 16,062 = 15.1%; the two-port spread is 26.3 percentage points.
- September two-port throughput: 1,042,652 + 997,177 = 2,039,829 TEU.
- Los Angeles empties share: 371,205.95 ÷ 1,042,652.30 = 35.6%. Long Beach: 396,040 ÷ 997,177 = 39.7%.
- Long Beach export share of boxes: 91,747 ÷ 997,177 = 9.2%.
