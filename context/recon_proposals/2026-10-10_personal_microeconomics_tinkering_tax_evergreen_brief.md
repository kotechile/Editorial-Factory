# Evergreen Brief: personal_microeconomics_tinkering_tax — 2026-10-10
**Archetype:** evergreen
**Vertical:** personal_microeconomics_tinkering_tax
**Persona:** systems_tinkerer_pro
**Decision the reader is facing:** Whether to keep self-hosting a service (mail, files, remote access, an automation container) or pay the $4–10/month managed plan — a decision the reader can settle at their own loaded hourly rate before the next renewal, by dividing the managed annual fee by what an hour of their time is worth.
**Durability:** The two load-bearing anchors are dated measured figures — O*NET's median wage for network and computer systems administrators (2025: $47.66/hour) and the EIA's 2025 annual average US residential electricity price (17.30¢/kWh) — and the managed fees are vendor list prices as of 2026-10-10. The framework itself does not expire, because it is one division a reader re-runs when a price moves: annual managed fee ÷ hourly rate = break-even maintenance hours per year. The article states each figure with its date so it stays checkable after any of them drifts.
**De-dup:** 2026-10-03_personal_microeconomics_tinkering_tax_evergreen_brief (the 3D-printing true-cost evergreen) and 2026-10-10_home-assistant-cloud-rename-hardware-rent (the published news piece on a vendor renaming its cloud tier) — the first prices a fabrication hobby's failures, the second reports a vendor's pricing move. This brief prices the recurring maintenance hours of any self-hosted service against the managed fee, and it is the self-hosting beat neither prior artifact took.
**Thesis:** Self-hosting is a control decision wearing a cost costume: at the 2025 median network-admin rate a single hour of maintenance a year already costs more than nine months of managed email, so self-host only what you would run anyway — and count the always-on wattage before calling the hardware free.

**Lead:** From the vertical's own beats and the founder's standing position. `primary_angles` #1 in `context/verticals.json` is "the trap of free open-source self-hosting and reverse proxy debugging hours"; the persona's `wants` in `context/personas.json` are "tinkering tax audits, self-hosting maintenance breakdown, micro-SaaS audit framework"; `context/growth_os/founder-voice.md` §3 carries the pillar "The Free Open-Source Self-Hosting Trap" (14 weekend hours at a $150/hr engineer rate = $2,100 of personal opportunity cost to dodge a $12/month managed fee) and visual format 36 ("Tinkering Opportunity Cost Balance Sheet"); `context/growth_os/customer-truth.md` Anecdote 1 is the 26-hour self-hosted Postfix/Dovecot weekend. The gap that makes it an article rather than a blog post: the founder's numbers are anecdotal, so this brief replaces them with a measured wage benchmark and a measured electricity price so any reader can run their own audit. The intel feeds carry nothing for this beat (`home_lifestyle_intel_client.py --search "self-host"` → 0 items), and `gsc_analyzer.py --vertical personal_microeconomics_tinkering_tax` found 0 high-potential queries (GSC is a bonus signal only).

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | O*NET OnLine — "15-1244.00 Network and Computer Systems Administrators" (US DOL, Wages & Employment Trends) | https://www.onetonline.org/link/summary/15-1244.00 | 2026-10-10 | $47.66 per hour (median wage, 2025) — the measured benchmark for what one hour of self-hosting maintenance is worth | measured |
| 2 | U.S. Energy Information Administration — "Electricity explained: Prices and factors affecting prices" | https://www.eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php | 2026-10-10 | 17.30 cents per kilowatthour — 2025 annual average US residential retail price, the rate the always-on hardware is billed at | measured |
| 3 | Synology — "DS223j" product specifications (Power Consumption) | https://www.synology.com/en-us/products/DS223j | 2026-10-10 | 16.31 watts — power draw of a two-bay home NAS in access mode (4 watts with drives hibernating) | vendor claim |
| 4 | Fastmail — Pricing (Individual, billed yearly) | https://www.fastmail.com/pricing/ | 2026-10-10 | $60 for 12 months — the managed mailbox bill a self-hosted mail server is meant to replace | vendor claim |
| 5 | Google Workspace — Pricing (Business Starter) | https://workspace.google.com/pricing.html | 2026-10-10 | $7.00 per user per month — managed mail, docs and calendar price | vendor claim |
| 6 | DigitalOcean — Droplet pricing (basic, smallest size) | https://www.digitalocean.com/pricing/droplets | 2026-10-10 | $4.00 per month — the rent-a-box alternative to buying hardware for a self-hosted service | vendor claim |
| 7 | Apple — iCloud+ storage plan prices (2 TB tier, USD) | https://support.apple.com/en-us/108047 | 2026-10-10 | $9.99 per month — managed price for the 2 TB of storage a self-hoster provisions on disks | vendor claim |
| 8 | Tailscale — Pricing (free plan limits) | https://tailscale.com/pricing | 2026-10-10 | 6 users — count included free, i.e. the remote-access layer a self-hoster otherwise rebuilds as a WireGuard and reverse-proxy stack costs nothing | vendor claim |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| Self-host or pay: the break-even test at your own hourly rate | 9 | 8 | 9 | 9 | 8.8 | **winner** |
| What an always-on homelab server costs in electricity alone | 7 | 9 | 8 | 6 | 7.6 | dropped — settles only the watts half of the decision; carried as a section of the winner |
| The micro-SaaS zombie audit: cancelling tools with no sessions in 90 days | 8 | 7 | 6 | 8 | 7.2 | dropped — retreads the 2026-09-26 subscription-creep article and its anchors are more vendor price pages with no measured baseline |
| The hobbyist automation payback: how long a script must run to break even | 8 | 8 | 5 | 8 | 7.2 | dropped — the load-bearing setup and maintenance hours (8 hours plus a quarterly chore, 5.2-year payback) exist only in `founder-voice.md`; no external measured source to cite |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->

## Gate result

<!-- evergreen-gate:start -->
<!-- evergreen-gate: helper=evergreen_gate.py rows=8 fetched=8 sources=8 hosts=8 decision="sha1:3c2db4a852" dedup="matched a prior artifact: 2026-10-03_personal_microeconomics" window_days=180 checked_at=2026-10-10T17:34:22+00:00 -->
<!-- evergreen-gate:end -->
