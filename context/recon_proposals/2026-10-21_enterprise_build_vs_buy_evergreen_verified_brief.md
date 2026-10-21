# Verified Brief: enterprise_build_vs_buy — 2026-10-21 (EVERGREEN track)

**Source brief:** `context/recon_proposals/2026-10-21_enterprise_build_vs_buy_evergreen_brief.md` (gate PASS, rows=5 fetched=5 hosts=5, checked 2026-10-21T19:03:20+00:00)
**Slug:** `your-ci-bill-232-hours` · **Persona:** `eng_leader` · **Archetype:** evergreen

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | Hosted CI rate | A Linux two-core hosted runner minute is billed at $0.006; macOS 3/4-core at $0.062, Windows two-core at $0.010, Linux two-core arm64 at $0.005, Linux one-core slim at $0.002 | VERIFIED | https://docs.github.com/en/billing/concepts/product-billing/github-actions | "Operating system Billing SKU Per-minute rate (USD) Linux 1-core (x64) actions_linux_ slim $0.002 Linux 2-core (x64) actions_linux $0.006 Linux 2-core (arm64) actions_linux_arm $0.005 Windows 2-core (x64) actions_windows $0.010 … macOS 3-core or 4-core (M1 or Intel) actions_macos $0.062" |
| 2 | Hosted storage meter | Shared artifact and package storage is $0.25 per GB-month; the Actions cache is $0.07 per GB-month | VERIFIED | https://docs.github.com/en/billing/concepts/product-billing/github-actions | "Storage type Price per GB/month Shared storage (artifacts and GitHub Packages) $0.25 USD Actions cache $0.07 USD Custom image storage $0.07 USD" |
| 3 | "Free" self-hosted usage | GitHub states that Actions usage is free for self-hosted runners — the sentence that makes the built side look costless | VERIFIED | https://docs.github.com/en/billing/concepts/product-billing/github-actions | "GitHub Actions usage is free for self-hosted runners and for public repositories that use standard GitHub-hosted runners." |
| 4 | Rented compute | A DigitalOcean Droplet with two vCPUs and 2 GiB of memory is $18.00 per month, published as $0.02679 per hour | VERIFIED | https://www.digitalocean.com/pricing/droplets | "2 GiB 2 vCPUs 3,000 GiB 60 GiB $0.02679 $ 18.00" |
| 5 | Labour rate | Median wage for software developers (15-1252.00) is $65.38 hourly and $135,980 annual, 2025 vintage | VERIFIED | https://www.onetonline.org/link/summary/15-1252.00 | "Median wages (2025) $65.38 hourly, $135,980 annual" |
| 6 | Second vendor's unit | GitLab charges hosted runners in cost factors: Linux small 1, medium 2, large 3, xlarge 6, 2xlarge 12; macOS M1 medium 6, M2 Pro large 12; GPU-enabled medium 7; Windows medium 1; "job duration / 60 × cost factor" | VERIFIED | https://docs.gitlab.com/ci/pipelines/compute_minutes/ | "Runner type Machine size Cost factor Linux x86-64 (default) small 1 Linux x86-64 medium 2 Linux x86-64 large 3 Linux x86-64 xlarge 6 Linux x86-64 2xlarge 12 … macOS M1 medium 6 (Beta) macOS M2 Pro large 12 (Beta) Windows medium 1 (Beta)" |
| 7 | Third vendor's add-on meter | CircleCI bills Docker layer caching at 200 credits per job run (stated as $0.12 per job run) on top of compute credits; network and storage beyond plan thresholds at 420 credits per GB ($0.252/GB) | VERIFIED | https://circleci.com/pricing/ | "Docker layer caching uses 200 credits per job run in a pipeline (equivalent to $0.12 per job run) … charged at 420 credits per GB ($0.252/GB)" |

## Authorised arithmetic (derived — recompute before the push, never re-derive from the draft)

| Derived figure | Basis | Value |
|---|---|---|
| Hosted two-core cost per hour | $0.006 × 60 | $0.36 |
| Hosted two-core cost, continuous month | $0.36 × 730 hours | $262.80 |
| Monthly price multiple | $262.80 ÷ $18.00 | 14.6 ("about 14 times") |
| Hourly price multiple | $0.36 ÷ $0.02679 | 13.4 |
| macOS premium over Linux | $0.062 ÷ $0.006 | 10.3 ("about 10 times") |
| Hardware break-even utilisation | $18.00 ÷ $262.80 | 6.85% ("about 6.9%") |
| Hardware break-even hours | $18.00 ÷ $0.36 | 50.0 hours a month |
| Hosted hours equal to one engineer-hour | $65.38 ÷ $0.36 | 181.6 ("182 hours") |
| Bar with one hour of upkeep a month | ($18.00 + $65.38) ÷ $0.36 | 231.6 hours ("about 232") ≈ 7.6 hours a day |
| Bar with two hours of upkeep a month | ($18.00 + $130.76) ÷ $0.36 | 413.2 hours ≈ 13.6 hours a day |
| Two single-core slim lanes vs one two-core lane | ($0.002 × 2 = $0.004) against $0.006 | 33% cheaper per minute of wall clock |
| Cache vs shared storage | $0.07 against $0.25 | 3.57 (not load-bearing; optional) |

## Gate rulings for the drafter

1. **The comparison is priced on list rates only.** Committed-spend discounts, bundled minutes and free-tier allowances are not in any cited row, so they may appear only as a reason the hosted rate could be *lower* than list — never as a figure.
2. **No claim about self-hosting macOS runners exists in the evidence.** The macOS row may state the rate and the premium; it may not speculate on licensing, on Apple hardware terms or on Mac-in-the-cloud pricing.
3. **"Free" must stay quoted to GitHub.** The free-for-self-hosted sentence is GitHub's own [1][3]; the article may read it as the trap, but it may not generalise it to other vendors.
4. **Every ratio in the body must be recomputed from the two prices it divides**, never copied from the draft: the 730-hour month is an assumption and must be stated as one, and $0.02679 × 730 does not equal $18.00 because the host bills a monthly cap — the monthly multiple uses the capped $18.00, the hourly multiple uses $0.02679, and the two must never be mixed in one sentence.
5. **Unit nouns are load-bearing:** a build *minute*, a server *hour*, a cost *factor* and a *credit* are four different quantities. Never write that one vendor is "cheaper per minute" than another unless the minute has been converted into the same unit.
6. **The wage is a national median, not a loaded cost.** Say so where the arithmetic is applied; the article may note that a real loaded engineer-hour costs more, and must not invent a loaded multiplier.
7. **No claim that self-hosting always or never pays.** The evidence supports a threshold, and the article must land on the threshold.

## Fact-check result

7 VERIFIED, 0 FLAGGED, 0 REMOVED. Every row was fetched through the gate's own fetcher (`citation_hub_dossier.fetch_source`, `EditorialFactorySourceVerifier/1.0` UA) and the cited figure was found on the page; the evergreen-gate marker in the source brief is fresh at rows=5.
