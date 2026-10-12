# Verified Brief: home_equity_tco (evergreen) — 2026-10-12

Topic: **Deferred maintenance as an unfunded liability** — the failure classes upkeep removes, priced
at the insurer's own measured frequency and severity, against the price of the service call that
prevents them and the published service life of the components that produce them.

Mode: **Evergreen** (`skills/evergreen_topics.md`). No 30-day window, no virality Judge, no dual-anchor
synthesis gate: this is a single durable thesis with 5 independent anchors on 5 hosts
(`evergreen_gate.py` PASS 2026-10-12, 9 rows / 9 verified).

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|------------|-------|--------|-----------|----------|
| L1 | III loss table | The "water damage and freezing" cause of loss runs **1.50%** claim frequency per insured home and **$15,400** average claim severity (2019–2023 average) | VERIFIED (table is claim of record; **prose discrepancy recorded**) | https://www.iii.org/fact-statistic/facts-statistics-homeowners-and-renters-insurance | Table "Average Homeowners Losses, 2019-2023 … Water damage and freezing 1.50 15,400". **The page's own prose says "1.6 percent of homes having a loss" — but that sentence describes the *prior* five-year period ("In the five-year period, 2018-2022, 5.8 percent … followed by water damage and freezing with 1.6 percent of homes having a loss"). Quote the table (1.50%, 2019–2023); do not print 1.6%.** |
| L2 | III loss table | Water damage and freezing accounted for **22.6%** of homeowners insurance claims in 2023 — second only to wind and hail (42.5%), ahead of fire and lightning (21.6%) | VERIFIED (**share of claims by cause, not share of dollars** — the table is "Homeowners Insurance Losses By Cause" and its own prose above it reads "Property damage, including theft, accounted for 97.3 percent of homeowners insurance claims in 2023"; causes sum above 100%, so never write "claim dollars") | https://www.iii.org/fact-statistic/facts-statistics-homeowners-and-renters-insurance | "Cause of loss 2019 2020 2021 2022 2023 … Wind and hail 38.1 47.7 38.9 45.4 42.5 Water damage and freezing 28.7 19.8 23.7 25.8 22.6 Fire and lightning 21.2 21.2 22.8 18.7 21.6" |
| L3 | III loss table | All causes: **5.33** claims per 100 insured homes in 2023 at **$20,062** average severity; the 2019–2023 average severity is **$17,059** | VERIFIED | https://www.iii.org/fact-statistic/facts-statistics-homeowners-and-renters-insurance | "In 2023, 5.3 percent of insured homes experienced a claim, compared with 6.4 percent in 2020."; "2019 5.37 $13,884 2022 5.81 $19,740 2020 6.37 14,864 2023 5.33 20,062 2021 5.34 16,601 Average (4) 5.64 $17,059" |
| L4 | III loss table | The classes a household cannot maintain away are the ones with the worst severity: fire and lightning **0.23%** frequency at **$88,170**, wind and hail **2.80%** at **$14,747**, theft **0.12%** at **$5,524** | VERIFIED | https://www.iii.org/fact-statistic/facts-statistics-homeowners-and-renters-insurance | "Property damage (4) 5.53 $16,857 Fire and lightning 0.23 88,170 Water damage and freezing 1.50 15,400 Wind and hail 2.80 14,747 Theft 0.12 5,524 All other (5) 0.88 9,043 Liability (6) 0.09 $2…" |
| L5 | EPA WaterSense | Household leaks waste nearly **1 trillion gallons** of water a year nationwide; fixing easily corrected leaks saves about **10 percent** on the water bill; one faucet dripping per second wastes more than **3,000 gallons** a year | VERIFIED | https://www.epa.gov/watersense/fix-leak-week | "Household leaks can waste nearly 1 trillion gallons of water annually nationwide…"; "Fixing easily corrected household water leaks can save homeowners about 10 percent on their water bills."; "A leaky faucet that drips at the rate of one drip per second can waste more than 3,000 gallons per year." |
| L6 | InterNACHI life-expectancy chart | The components that cause water and mechanical losses have published service lives: conventional water heater **6 to 12** years, central air conditioner **7 to 15**, ceiling vent fan **5 to 10**, sewer grinder pump **10** | VERIFIED | https://www.nachi.org/life-expectancy.htm | "Water Heater (conventional) 6 to 12"; "Air Conditioner (central) 7 to 15"; "Vent Fan (ceiling) 5 to 10"; "Sewer Grinder Pump 10" |
| L7 | O*NET OnLine (US DOL) | The trade that performs routine service calls has a **$23.84** median hourly wage in 2025 (**$49,590** a year) | VERIFIED | https://www.onetonline.org/link/summary/49-9071.00 | "Median wages (2025) $23.84 hourly, $49,590 annual" |
| L8 | Harvard JCHS | The US remodeling market is above **$600 billion**, still **50 percent** above pre-pandemic levels, spread over **145 million** homes | VERIFIED | https://www.jchs.harvard.edu/improving-americas-housing-2025 | "The US remodeling market soared above $600 billion in the wake of the pandemic and remains 50 percent above pre-pandemic levels."; "far more investment is needed to improve energy efficiency and disaster resilience for the country's 145 million homes." |

## Derived figures (arithmetic, ours — show the math, never present as a source's own number)

- **$231** = 1.50% × $15,400 — the expected annual insured water-damage loss per insured home.
- **$1,069** = 5.33% × $20,062 — the expected annual insured loss per home across all causes (2023).
- **1 in 67** = 1 ÷ 0.015 — how often an insured home files a water-damage claim in a year.
- All three are the *system's* expected loss per home, not the household's out-of-pocket exposure (see
  the drafting rules). They are arithmetic over verified figures, so they must be shown as arithmetic.

## Drafting rules from this brief

1. The **table is the claim of record**: use 1.50% (2019–2023), never the page's 1.6% prose (which
   describes 2018–2022).
2. **Do not** claim maintenance causes the absence of a claim — nothing here measures that. The
   defensible claim is narrower: the losses that routine upkeep addresses are the highest-frequency
   mid-severity class, and the classes upkeep cannot remove carry either near-zero frequency
   (fire, 0.23%) or a lower severity (wind and hail, $14,747).
3. **Self-insurance framing, honestly done:** $231 and $1,069 are what the *pool* pays out per home,
   not what the household pays. The household's cash exposure is the deductible, the uninsured part,
   the premium effect and the disruption — say so; do not write the claim average as the reader's bill.
4. **The founder's 1-to-10 decay ratio and the 1–2% reserve rule are corpus assertions**, not measured
   facts — the customer-truth anecdote may be used as an attributed field case, never as a statistic.
5. Every figure in the body must appear in this table or the derived list; the founder field note
   ($150 attic condensate clear → $16,800 claim) is corpus material and must be labelled as such.
6. Nothing here is a rate snapshot, so nothing expires on a news clock; still date every figure in the
   body to its **as-of** edition (III 2019–2023 table / 2023 column, O*NET 2025, JCHS 2025 edition,
   InterNACHI's standing chart, EPA WaterSense's standing page).
