# SKILL: Evergreen Track (Loop 1E — Useful, Durable Topics)

## 1. Objective

Publish one **useful, durable** article for a vertical: a topic a reader would search for and act
on months from now. Not a news sweep.

The news pipeline (`skills/radar_30day.md` → `skills/virality_judge.md`) is built to find a fresh
30-day signal; its gate weights **Novelty 0.40** and drops anything whose load-bearing claim is
older than the window. That is correct for news and wrong for everything else: it is why verticals
whose beat is periodic (annual surveys, statute books, procurement cycles) returned
*"no publish"* week after week, and why the runs logged *"undated evergreen; not anchored to
window"* while discarding material readers actually want.

This track exists because those are two different products. **The news gate does not run here** —
do not score Novelty, do not run `synthesize_topics.py --seed`, do not widen a window. And the
converse holds: a topic whose value expires inside ~90 days is a news story, and belongs in the
news pipeline, not here.

## 2. What makes a topic admissible

Come to the topic from evidence, never from your own idea of what would be interesting. Any of
these is a legitimate lead; a topic with none of them is an invented topic and is refused:

| Lead | Where it lives |
|---|---|
| The vertical's own beats | `primary_angles` in `context/verticals.json` |
| What the reader is trying to decide | the persona's `wants` in `context/personas.json` |
| The founder's standing positions | `context/growth_os/founder-voice.md` §2 (content pillars) and §3 (per-vertical angles) |
| Real field friction with numbers | `context/growth_os/customer-truth.md` (per-vertical anecdotes) |
| Recurring non-news material | the intel feeds' `product_evaluations` / `market_metrics` (via `scripts/home_lifestyle_intel_client.py`, `scripts/supply_chain_intel_client.py`) |
| Demand the site is already close to winning | `scripts/gsc_analyzer.py --vertical <id> --export-md` — **bonus signal only**: impressions are thin on a young site, so low volume never vetoes a good topic |

## 3. The Evergreen Gate (hard)

Mechanical floor, enforced by `scripts/evergreen_gate.py` — a `PASS` there is required before a
single word of prose is drafted:

- **≥ 3 distinct primary sources** (`MIN_SOURCES`), on **≥ 2 distinct hosts** (`MIN_HOSTS`). Three
  pages of one vendor's site are one source wearing a costume.
- **Every cited source is fetched and must actually contain the figure it is cited for.** Not the
  URL pattern, the page. A paywalled, PDF-only or 404 source is a failure to fix, not a footnote;
  replace it.
- **A named persona decision** — the sentence the reader is trying to settle. If you cannot state
  it, there is no article.
- **A proven de-dup check** against the last **180 days** (`DEDUP_WINDOW_DAYS`) of this vertical's
  briefs and published articles: name the nearest prior artifact (a date or slug) that exists. The
  gate proves the artifact exists rather than pretending to judge similarity — a token-overlap test
  on a one-line thesis produces both false retreads and false passes.
- **An `as of` date** for any time-bound figure (a price, a rate, a cap, a standard). An undated
  figure is a news fact wearing an evergreen label, and it will be wrong within a year.

**The de-dup check is per-vertical; the corpus is not (learned 2026-10-19).** `check_dedup` reads this
vertical's briefs and published articles only, so a topic already published under a *different* vertical
passes the gate cleanly and ships as a duplicate. Observed: a prompt-caching candidate (mechanics, prices,
break-even rule) scored 9.0 and cleared every floor on paper while
`published/2026-10-08_cache-boundary-decides-input-bill.md` (enterprise_ai_finops) already owned that
thesis in the same corpus — the gate could not see it because the artifact carried another vertical's
name. Before writing the brief, grep the whole corpus for the candidate's subject tokens
(`grep -ril "prefix cach\|cache breakpoint" published/ context/recon_proposals/`) and read the nearest
hit's `one_big_thing:`; a candidate whose mechanism is already argued anywhere in `published/` is refused
by hand, and the brief's `De-dup:` line should name that cross-vertical artifact as checked-and-dropped
so the audit shows the check happened.

Beyond the floor, judge the topic yourself on the four axes and write the score into the brief:

| Axis | Question | Weight |
|---|---|---|
| Usefulness | Does it settle a decision the persona actually faces this year? | 0.35 |
| Durability | Is it still correct in 12 months, with the cited figures dated? | 0.25 |
| Evidence | Are the anchors primary, measured, and about this beat (not vendor claims)? | 0.25 |
| Actionability | Does it carry at least one rule with numbers — a threshold, a payback, a gotcha? | 0.15 |

Composite = round(0.35·U + 0.25·D + 0.25·E + 0.15·A, 1). **≥ 8 → proceed.** Below that, either
sharpen the evidence or return "no publish" and say why. There is no quota: a vertical that has
nothing durable to say this week says nothing.

**Refused outright (these are what "evergreen" degenerates into):**
- a listicle of unverified statistics — that is what `skills/citation_hub.md` is for, and it has its
  own stricter data gate;
- a "complete guide" whose every section restates the same three sources;
- a re-argued version of a published article (see the de-dup rule);
- anything whose honesty depends on a figure you could not fetch.

## 4. Output — the evergreen brief

Write `context/recon_proposals/YYYY-MM-DD_<vertical>_evergreen_brief.md` (the name is load-bearing:
it never collides with the news track's `_signals.md` / `_angle_brief.md`, and
`scripts/verify.sh` discovers briefs by it):

```markdown
# Evergreen Brief: <vertical> — YYYY-MM-DD
**Archetype:** evergreen
**Vertical:** <vertical_id>
**Persona:** <persona_id from context/personas.json>
**Decision the reader is facing:** <the decision + when it bites — >= 40 chars>
**Durability:** <why this is still true in 12 months; state what the figures are *as of*>
**De-dup:** <the nearest prior artifact for this vertical in the last 180 days + why this differs>
**Thesis:** <the one sentence the article must defend>

**Lead:** <which of §2's evidence sources produced this topic, and the specific material>

| # | Source | URL | Retrieved | Figure/claim it supports | Vendor claim or measured? |
|---|---|---|---|---|---|
| 1 | <publisher + title> | https://… | YYYY-MM-DD | <the exact figure> | measured |
| 2 | … | … | … | … | vendor claim |
| 3 | … | … | … | … | measured |

## Candidate topics considered
| Topic | Usefulness | Durability | Evidence | Actionability | Composite | Verdict |
|---|---|---|---|---|---|---|
| <topic> | 9 | 8 | 9 | 7 | 8.4 | **winner** |
| <topic> | 7 | 9 | 6 | 8 | 7.4 | dropped — one anchor is a vendor claim |

## Gate result
<!-- written by scripts/evergreen_gate.py — do not hand-edit; re-run the gate if you edit a row -->
```

Then run the gate:

```bash
python3 scripts/evergreen_gate.py --brief context/recon_proposals/YYYY-MM-DD_<vertical>_evergreen_brief.md
```

It fetches every row, prints the evidence it found for each figure, and writes the
`<!-- evergreen-gate: -->` marker on pass. **Editing a row after that makes the marker stale, and
`scripts/verify.sh` reads a stale or missing marker as a build failure** — re-run the gate.

**Writing the figure cell so the gate can read it:** the matcher looks for numeric tokens, so a row
whose figure is written in words must *begin* with the number word (`six months — …` matches "six
months" or "6 months"; `at least six months — …` generates no pattern at all and reads as
`figure_absent`). Lead the cell with the figure, then the gloss, and never bury it after prose —
the same row that fails this way will pass once the figure moves to the front.

**Lead the `De-dup:` line with the artifact, not with the word "evergreen" (learned 2026-10-13).**
`evergreen_gate.check_dedup` returns the *first* ref in the line that matches a filename, and its ref
regex accepts any run of 9+ `[a-z0-9-]` characters — so "the published evergreen `2026-10-06_<slug>`"
matches on the word **evergreen** (every `*_evergreen_brief.md` satisfies it) and the marker records
`dedup="matched a prior artifact: evergreen"`: the gate still PASSes, but the audit trail names nothing.
Open the field with the bare slug or date-slug (`` `2026-10-06_<slug>` is this vertical's nearest prior
evergreen artifact … ``) so the marker proves the check the rule intends.

**A multi-token figure can verify on the wrong number.** `citation_hub_dossier.figure_evidence`
returns evidence as soon as *any* numeric token in the cell appears in the fetched page, so a range
written `8% to 15%` will "verify" on a bare `8` the source never tied to the claim (observed: the
phrase was absent from both cited pages entirely, and a lone `8` elsewhere on the page passed it).
Lead the cell with the one distinctive figure the source actually states (e.g. `20% to 30%`), and
eye-check that the *phrase* — not a coincidental single digit — is on the page. A figure that
verifies this way ships a claim the source never made.

**The gate fetches with a fixed, non-browser user-agent — check fetchability before you write a
row.** `citation_hub_dossier.fetch_source` sends
`Mozilla/5.0 (compatible; EditorialFactorySourceVerifier/1.0)`, and several hosts answer it with
HTTP 403 even though the page is public in a browser. Observed: the entire Bureau of Labor
Statistics site (`bls.gov` — OEWS/CES/JOLTS/ECEC), which is otherwise the best measured anchor for
wage, turnover and benefit figures, returns 403 to the verifier and therefore cannot carry a gate
row. Probe a candidate URL through the same fetch the gate uses before committing to it:

```bash
python3 -c "import sys; sys.path.insert(0,'scripts'); import citation_hub_dossier as c; \
print(c.fetch_source('<url>')['status'])"
```

A `verified` row needs `status == 'fetched'`; a 403/404/PDF row fails the floor no matter how good
the figure is, so build the topic around sources that actually retrieve.

**arXiv `abs` pages carry no numbers — cite the `/html/<id>vN` full text for any mined figure (learned 2026-10-13).**
The abstract page fetches fine and its prose supports a qualitative row, but the numeric figure a row leads with
is usually absent from it: the `abs` page for "Quantifying Variance in Evaluation Benchmarks" rendered zero `%`
tokens, while the same paper's `/html/2406.10229v1` carries the tables. `https://arxiv.org/html/<id>vN` retrieves
with the figure as text (45–110 KB bodies observed; an ICML position paper's "92.5% coverage at N=100", its
"N = 20 questions" figure and an "at least 1,000 questions" recommendation were all present there and absent from
the corresponding `abs` pages), so build every numeric row on the HTML full text and keep the `abs` URL only when
the row cites a claim the abstract itself states. Same run: `nvlpubs.nist.gov` PDFs come back `unsupported` (no
PDF extractor in the fetch path), but NIST's own HTML news/publication pages for a report fetch at ~12 KB carrying
that report's findings, its benchmark names, its model count and the document number — a standards row the PDF
cannot carry.

**A `fetched` row can also be an error page wearing HTTP 200 — check the body, not just the status.**
EIA's `epm_table_grapher.php` URLs (Electric Power Monthly figure tables) intermittently answer 200 with
a ~260-character stub reading *"Sorry! Unexpected Error … routed to the appropriate person"* and no
numbers at all, so the same row passes on one fetch and reads `figure_absent` on the next (observed
2026-10-09: the July 2026 industrial price row verified on a manual probe, then failed inside the gate
run). Prefer a stable EIA prose page for the same figure — `eia.gov/energyexplained/electricity/…`
carries the annual average price by customer class in plain text and retrieves every time — and treat any
`fetched` body under ~400 characters as unreachable until you eyeball it.

**Hosts probed live 2026-10-10, building a wage-and-price audit from retrievable rows.** Works, with the
figure as plain text: `onetonline.org` (median wage by occupation, hourly **and** annual — the measured
wage anchor that `bls.gov`'s 403 refuses), `eia.gov` energy-explained, `synology.com` product spec pages
(power draw in watts), and the vendor list-price pages `fastmail.com/pricing`,
`workspace.google.com/pricing.html`, `digitalocean.com/pricing/droplets`, `support.apple.com/en-us/108047`
and `tailscale.com/pricing` — the reliable way to cite "what the managed alternative costs" without
leaning on a secondary writeup. Fails: `raspberrypi.com` documentation (403), `reddit.com` wikis
(403 Blocked), `nvd.nist.gov` and `cve.org` dashboards (client-rendered, 10–42 character bodies), and
`analytics.home-assistant.io` (HTTP 200 but ~700 characters — its install-count stub is the whole page).
A price page is a legitimate row for a price claim as long as its table cell reads `vendor claim`, and a
per-unit figure written `$4.00 per month` verifies on the row's own `$ 4.00` token.

**`eur-lex.europa.eu` fetches but cannot carry a quoted row (observed 2026-10-12).** A full Official
Journal regulation page (`https://eur-lex.europa.eu/eli/reg/…/oj/eng`) retrieves at HTTP 200 with a
~300 KB body, yet the article's own text is not in the fetched document: a brief row quoting the Data
Act's switching-charge wording (`switching charges`, `12 January 2027` in the operative sentence) read
`figure_absent` twice in a row while the page's navigation and the date table did match. Cite the
regulation through a page whose prose the fetcher can actually read (a national regulator's summary, a
commission implementation page, or the consolidated-version text page), or drop the row — do not
assume the OJ link is self-evidencing because the regulation is public. The same run re-confirmed the
EIA `electricity/monthly/update/end-use.php` flakiness below: one `--check-artifacts` pass read a row
`figure_absent` (18.31 cents/kWh) and a re-probe minutes later found the figure on the same page, so
treat an EIA row that fails once as retryable-before-replaceable.

**A row on `artificialintelligenceact.eu` can verify on a navigation digit — eye-check the phrase, not the gate's excerpt (observed 2026-10-12).** The site lists every article number in its sidebar above the body, and `figure_evidence` matches a single numeric token anywhere on the page: a row citing "15 days" from Article 73 "verified" against `Arts. 8–15` in the nav, and a row citing "72 hours" from GDPR Article 33 against `Art. 72 Procedure`, so the marker's evidence excerpt reads as navigation while the real quote sits further down. The rows are honest — the phrases are in the body — but the audit trail is not self-evidencing, so confirm each phrase inside its own sentence before drafting and write the check into the verified companion (`python3 -c "import sys,re; sys.path.insert(0,'scripts'); import citation_hub_dossier as c; t=c.fetch_source('<url>')['text']; print(re.search(r'.{0,160}15 days.{0,160}', t).group(0))"`). Prefer a lead figure the page states once — a full date ("2 December 2027") or a rare phrase is safer than a two-digit number the nav already contains.

**An eCFR page's own banner header poisons a row that leads on a small integer (learned 2026-10-17).** The
eCFR prints `Displaying title 19, up to date as of 10/15/2026` above the regulations, so a cell beginning
`10 days — …` matches the **banner date's** `10` and reports that boilerplate as the row's evidence, the same
class as a nav-digit match. Write such a cell digit-free and let the word-number pattern do the work
(`ten days — an oral prior disclosure must be confirmed within ten days` matches the sentence and nothing in
the banner), lead on a rare token whose window is the operative sentence (`$100,000` for a review threshold),
and remember that `thirty`/`forty`-class words are not in `_WORD_NUMBERS` while `ten` is — a digit-free
`thirty days` cell generates no pattern at all and dies as `figure_absent`. `cbp.gov` stayed unreachable to
the verifier again, so an agency figure it publishes is citable through the Federal Register full-text
endpoint (`https://www.federalregister.gov/documents/full_text/text/YYYY/MM/DD/<doc>.txt`) instead.

**A `fetched` row can still fail as `figure_absent` — the page loaded and the number did not.**
Several vendor rate-card hosts render their tables client-side, so the verifier gets HTTP 200 with a
body that carries no numeric tokens at all. Observed 2026-10-08 building the supply_chain evergreen
brief: `fedex.com`, `odfl.com`, `xpo.com`, `tforcefreight.com`, `saia.com` and `ups.com` fuel-surcharge
pages either 404 or return a `fetched` page whose text is navigation only, so a row on a carrier's own
published surcharge table fails the floor even though the table is visible in a browser.
`fred.stlouisfed.org` is unreachable to the verifier outright. The source types that reliably return the
figure as text are government statistics pages (`eia.gov` works where `bls.gov` 403s), arXiv/doc sites,
and industry explainers — so check the figure, not just `status`, before committing a row:
`python3 -c "import sys; sys.path.insert(0,'scripts'); import citation_hub_dossier as c; \
print(c.figure_evidence('<figure>', c.fetch_source('<url>')['text']))"`.

**Hosts probed live 2026-10-13, building a panel-ampacity / load-management brief out of a residential-electrification decision.** Carries the figure as plain text and fetches first try: `greenhomeinstitute.org` (a transcribed webinar article — the 80 % load-calculation threshold, the ~$8K-$10K installed smart-panel price against a $780 load-manager MSRP, full electrification "on services as small as 150 amps"), `afdc.energy.gov` (the DOE Alternative Fuels Data Center charger page — "7.2 kW", the dedicated 40-Amp circuit, National Electric Code Article 625), `emporiaenergy.com` (product page: 24,000 samples per second, +/-2 % accuracy, the $99.99/$149.99/$199.99 bundle prices; its blog: a worked "80 amps of your 100-amp service" example), `span.io` (48A / 11.5 kW dynamic against the "24-40A (5.7-9.6 kW)" a worst-case fixed install is limited to). Fails or cannot carry a row: `cltc.ucdavis.edu` (403 to the verifier on its project pages, and the service-upgrade-avoidance field study itself is a PDF — the best *measured* anchor for this beat is unreachable to the gate), `eaton.com` (unreachable), `ecmag.com` (403), `up.codes` (HTTP 500), `blog.se.com` (fetches at ~5.8 KB but the body carried no numeric tokens at all, so no row can lead on it), and guessed `energy.gov/energysaver/<slug>` URLs (404 — the NREL/LBNL/ACES panel-capacity material is PDF-only and therefore `unsupported`). A brief on this beat can be built from fetchable HTML primaries, but it cannot cite a code article number beyond the one the DOE page states; write the code pathway in prose ("systems inspectors accept when properly listed") rather than inventing a citation.

**Hosts probed live 2026-10-14, building a warehouse-wage-and-floor brief.** Carries the figure as plain text and fetches first try: `onetonline.org` (median wage by occupation, hourly *and* annual, from the 2025 vintage — the measured anchor `bls.gov`'s 403 refuses, and it works for any SOC code: 53-7051.00, 53-7062.00, 53-7065.00 and 53-7064.00 all retrieved at 24–30 KB with "Median wages (2025) $19.35 hourly, $40,240 annual" as text, plus each page's own occupation description and sample of reported job titles, which is the licence to gloss the occupation in prose); `oregon.gov/boli/workers/pages/minimum-wage.aspx` (a state floor published as a dated forward window — the three tiers for July 1, 2026 through June 30, 2027, the annual July 1 inflation rule, and the federal $7.25 floor in the same body); `dol.ny.gov/minimum-wage-0` (rates for a *future* date — $17.00 / $16.00 from 01/01/2027 — with the statutory off-ramp that blocked the 2027 increase explained on the page, a state's floor path being the one wage input published in advance); `mmh.com` survey articles (the operator survey's own figures as text: the turnover distribution 55% at ≤15% and 29% at 16–30%, "during peak periods, 30% or more of the workforce is temporary", and the median projected capex and technology budget). Fails or cannot carry a row: `irs.gov` and `ssa.gov` (both unreachable to the verifier, so no §179 expensing, bonus-depreciation or payroll-tax row can ride on the statute — an aggregator that does fetch is not the code); `lni.wa.gov`, `dir.ca.gov`, `dol.gov` (WHD), `labor.illinois.gov` PDFs, `dllr.state.md.us` and `labor.vermont.gov` (unreachable), `twc.texas.gov` (unreachable, so a low-floor state cannot be cited from its own agency); `supplychaindive.com` article URLs and `dcvelocity.com` (unreachable); and the equipment vendors `crown.com`, `enersys.com` and `fluxpower.com` fetched with **no numeric tokens at all** while `mobile-industrial-robots.com` carried only a runtime — so a robot-hour energy claim cannot be evidenced from a vendor spec page and the industrial tariff alone prices the input, not the usage.

**Hosts probed live 2026-10-15, building a cargo-claim-evidence brief (what a freight claim must be in writing, and which dates decide if the money is recoverable).** Carries the figure as plain text and fetches first try: `ecfr.gov` title-49 parts (Part 370 truck/forwarder claim procedure and Part 1005 its railroad twin — § 370.3(b)–(c) the three parts of a claim and the explicit rule that a shortage or damage notation on a delivery receipt is not one, § 370.5(a)/§ 1005.3 the 30-day acknowledgment, § 370.9(a)/§ 1005.5 the 120-day disposition with status letters every 60 days, and the amendment note "as amended at 91 FR 7859, Feb. 19, 2026" — a housekeeping change that dates the rule's currency); `govinfo.gov` U.S. Code HTML pages (`USCODE-<year>-title49/html/…-sec14706.htm` and `…-sec11706.htm` both retrieve at 6–10 KB with the statutory floors as text: "a period of less than 9 months for filing a claim … and … less than 2 years for bringing a civil action"); and `law.cornell.edu/uscode/text/46/30701` (23 KB with the Carriage of Goods by Sea Act's own limits — the carrier and ship discharged unless suit within one year, and the three-day written notice for a non-apparent loss, plus the sentence saying that missing the notice does not affect the right to sue inside the year). Fails or cannot carry a row: `federalregister.gov` **API** (`/api/v1/documents.json…`) fetches and is the cheapest way to locate a rule's citation, effective date and document number, but the guardrail is on the host: `cbp.gov` (ISF/10+2 page), `fmcsa.dot.gov`, `transportation.gov`, `iata.org`, `nmfta.org` and `portoflosangeles.org`/`polb.com` are all unreachable to the verifier, `uscode.house.gov/view.xhtml` renders a 1.1 KB stub with no figures, `govinfo.gov`'s title-46 path for § 30701 returns a 1.9 KB stub (the Cornell copy is the one that works), and `ups.com`'s dimensional-weight page returns 189 characters — so a claims brief rides on the CFR, the U.S. Code and Cornell LII rather than on any carrier page. **Two adjacent evergreen topics are now taken, and a third anchor is parked:** `published/2026-10-06_demurrage-invoice-30-day-clocks` owns 46 CFR Part 541 (the ocean billing clocks on a fee the shipper OWES) and this run's `published/2026-10-15_freight-claim-dies-at-9-months` owns 49 CFR Part 370/1005 (the cargo-liability clocks on money the carrier owes), so do not re-argue either; `fmc.gov/consumer-affairs/detention-and-demurrage/` fetches at 4.9 KB and carries a measured, dated market anchor nobody has used yet — the nine named carriers collected roughly **$15.4 billion** in demurrage and detention between 1 April 2020 and 31 March 2025, with Q1 2025 billings down 24% and collections 19% quarter-to-quarter — which is the natural anchor for a *pricing* piece (what the fees actually cost and who pays them) rather than another clock piece.

**Hosts probed live 2026-10-15, building a retainage / owner-payment-clock brief (how much of a remodel payment an owner may withhold, and for how long).** Carries the figure as plain text and fetches first try: `oregon.public.law` (ORS 701.420 in full — "not more than five percent of the contract price of the work completed" with *home improvement* contracts named in the same subsection, the one-percent-per-month interest on a final payment that commences 30 days after the owner accepts, the 15-day accept-or-list window, the $500,000 escrow trigger, and the 15-day retainage release after a contractor pays a sub in full — one page can carry four or five rows); `revisor.mn.gov` (statutes 337.10 subd. 4(b)–(c): a five percent retainage cap, the owner's power to cut it on any monthly payment with the contractor cutting subcontractor retainage at the same rate, and release of all retainage within 60 days of substantial completion; 337.01 subd. 2 defines "building and construction contract" as covering real property, which is the licence to say a house is inside that cap); `california.public.law` (**a fetchable mirror of the California codes where `leginfo.legislature.ca.gov` answers HTTP 403 to the verifier** — § 8811 prints the 5 percent private-works retention cap for contracts entered into on or after January 1, 2026 *and* the (b)(3) carve-out for a non-mixed-use residential project of four stories or fewer, so one page carries both the cap and the exemption); `law.lis.virginia.gov` (§ 2.2-4333, the 95 percent / 5 percent public-contract retainage rule — a boundary row: the statute sits in the Public Procurement Act, so it binds public bodies, not a homeowner); `leg.state.nv.us` NRS-624.html (the private-owner prompt-payment and 5 percent retention rules are genuinely in there, but the file is a single 352 KB page and every short figure in it — `5`, `21 days`, `50 percent` — matches an unrelated earlier section, so a Nevada row's evidence window reads as a coincidence; a per-section URL or the contractors board would be needed for a clean row). Fails or cannot carry a row: `leginfo.legislature.ca.gov` and `law.justia.com` (403), `www.nysenate.gov/legislation/laws/...` (403), `le.utah.gov` per-section guesses (404), `cga.ct.gov` (SSL certificate failure in the verifier's fetch path), `nolo.com` (403), `mass.gov` (403), `statutes.capitol.texas.gov/Docs/PR/htm/...` (a 1.3 KB navigation stub, not the chapter), `energy.gov/energysaver/<guessed-slug>` (404 — the DOE pages that resolve are worth finding by search, not by guessing), and `codes.ohio.gov` prints its payment-timing statute with the deadlines in words ("within ten calendar days") plus an `eighteen per cent per annum` interest clause that the word-number matcher cannot lead on (`_WORD_NUMBERS` stops at twelve).

**Hosts probed live 2026-10-15, building an agent-runtime termination-bound brief.** Carries the figure as text and fetches first try: `arxiv.org/html/<id>vN` (the full text of a paper's *tables* — a static-analysis census's Table II rendered every count and ratio as prose, e.g. "We evaluate IAL-Scan on 6,549 LLM agent repositories … manual review confirms 68 IAL failures across 47 projects, achieving 91.9% precision", plus its framework, impact, root-cause and failure-pattern rows, so one measured paper can carry several rows whose evidence windows land on the table itself); `docs.langchain.com` (a framework's own documented default — "Starting in version 1.0.6, the default recursion limit is set to 1000 steps"); `reference.langchain.com` (a ~1.2 KB body, but it holds the docstring a reader may be quoting — "If not provided, defaults to 25" — and two official pages of one vendor stating different numbers is *itself* a citable claim, provided the row attributes each to its own page); `github.com/<org>/<repo>/issues/<n>` (a tracker issue fetches at ~60 KB with body, reproduction and closed status as text, and the title carries the figure); and `docs.crewai.com` (a field table with the documented default — "max_iter int Maximum iterations before the agent must provide its best answer. Default is 20"). Fetches but cannot carry a row: `openai.github.io` (the SDK reference shows `max_turns: int | None = DEFAULT_MAX_TURNS` and never the constant's value, so no figure to lead on — `raw.githubusercontent.com/<org>/<repo>/main/<path>` does retrieve the source file when the rendered docs omit it); `docs.claude.com/en/api/agent-sdk/python` (documents `max_turns` and `max_budget_usd`, both defaulting to `None`: "the bound is off by default" is exactly the claim, and the page states no numeric token for a row to lead on, so the row fails the *matcher*, not the desk — grep the page for a dollar figure before planning on it); and `google.github.io/adk-docs/agents/` (9.4 KB with 23 digits total). A documented default is only a row when the number is in the fetched body: "defaults to None" cannot be one, because the gate reads figures.

**Hosts probed live 2026-10-15, building a per-resolved-task pricing brief (the sticker price of a model tier vs the cost of the task it resolves).** Carries the figure as plain text and fetches first try: `arxiv.org/html/<id>vN` again, twice over — OckBench's financial-inversion paragraph (a 7B model priced at 50% of its 14B sibling emitting 3.13× more output tokens and landing 57% dearer per query, with the pricing footnote dated "as of Jan 2026") and Terminal-Bench 2.0's per-agent resolution/token table plus its §G.2 correlation sentence, so one HTML full text can carry a measured *and* a comparative row; `docs.claude.com/en/docs/about-claude/pricing` (a 29 KB body with the whole model table as text — input, output, 5m/1h cache writes, cache hits — plus the Batch API's "50% discount on both input and output tokens"); `cloud.google.com/vertex-ai/generative-ai/pricing` (~120 KB of plain-text rate tables, including "Price per 1M output and thinking tokens", a thinking-token audit note pointing at the `thoughts` field, and *dated* promo windows — "through November 30, 2026", "Starting January 1, 2027" — which is the cheapest way to give an evergreen piece its "as of" anchor); `platform.openai.com/docs/pricing` (Standard/Batch/Flex/Fast lanes as one text table, so the same model can carry standard and batch rows) and `platform.openai.com/docs/guides/reasoning` (the sentence that reasoning tokens "are not visible via the API" while being "billed as output tokens", plus a usage example whose `reasoning_tokens: 1024` gives the row a numeric token to lead on); and `onetonline.org` (median wage, the measured labour anchor `bls.gov`'s 403 refuses). Fails or cannot carry a row: **the commitment-pricing pages fetch but print no prices.** `azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/` retrieves at ~71 KB and `aws.amazon.com/bedrock/pricing/` at ~172 KB, yet every PTU cell renders as `$-` and every Bedrock cell as a `{priceOf!bedrock/…}` template token filled by client-side JavaScript — so a committed-throughput vs pay-per-token break-even cannot be built from the vendor's own price page, and the row would die as `figure_absent` no matter how good the reservation discount is. Probe the *figure*, not the status, before planning such a brief: `python3 -c "import sys,re; sys.path.insert(0,'scripts'); import citation_hub_dossier as c; t=c.fetch_source('<url>')['text']; print(re.findall(r'\\$\\s?\\d[\\d,\\.]*', t)[:20])"` — a page with hundreds of digits and no dollar amount is a JavaScript price list. Also unreachable this run: `finops.org` and `help.openai.com` articles.

**A comma-grouped dollar figure written without its comma renders no pattern that exists on the page (learned 2026-10-14).** `figure_patterns("$425,000 …")` yields `425` and `000`, and the window lands on the sentence carrying the claim; the same figure written `425000` yields one pattern that appears nowhere, so `figure_evidence` returns nothing and the row dies as `figure_absent` even though the page prints the number. Write money the way the source prints it — comma included — and check the cell with `c.figure_evidence(cell, text)` before committing the row.

**A cell that leads on a word number is matched on the digits it also carries (learned 2026-10-14).**
`figure_patterns` returns digit patterns whenever the cell contains *any* digit, so
`three minor releases — release branches are maintained only for the most recent three minor releases (1.37, 1.36, 1.35)`
is probed on `1.37` first and its evidence window becomes whatever text mentions 1.37, not the claim the row
makes: the row still PASSes, so the marker's audit trail reads as a coincidence — the same class as the
comma-grouped and stray-`24/7` cases below. When the lead figure is a word, keep the whole cell digit-free
(`three minor releases — release branches are maintained only for the most recent three minor releases, and
current versions receive approximately one year of patch support`), and carry whatever version numbers or dates
the row wants in the article's prose instead, where the same page citation covers them.

**The matcher splits a comma-grouped figure — lead the cell with a different number, or expect a coincidental excerpt (learned 2026-10-14).**
`figure_patterns` tokenises with `\d+(?:\.\d+)?`, so a figure cell leading on `4,989 tokens` produces the
patterns `4` and `989`: the first one matches the earliest bare `4` anywhere on the page (observed: the
prefill-phase text's "spans 4 nodes"), and `figure_evidence` returns that window as the row's evidence. The
row still verifies, but the audit trail reads as a coincidence — the same class as the stray-`24/7` case
below. Fix it the way this brief did: move the comma-formatted claim *into* a row that already leads on a
distinctive token (`73.7k tokens/s input … in the same window the average KV-cache length per output token
was 4,989 tokens`), so the evidence window is the sentence about the claim and the second figure rides
along inside a verified row.

**Lead each row with the token the page states *once* — `figure_evidence` returns the window around the first occurrence of the first numeric token in the cell (learned 2026-10-13).** A row written `24,000 samples per second` evidenced on a stray `24/7` in the page's navigation, `48A` evidenced on an `MLO 48` product-family label, and a Home Assistant recorder retention row written `10` evidenced on `MariaDB ≥ 10.3` — every one of those phrases is genuinely on its page, so the gate PASSes, but the marker's audit trail reads as a coincidence. Probe each candidate figure with `c.figure_evidence(<figure>, text)` before writing the row and lead with the token whose excerpt is a sentence about the claim (`80 amps` → the worked example; `$199.99` → the price line); when the natural figure collides, pick the page's rarer one rather than shipping a row whose evidence a reader cannot check.

**Vendor docs pages are the same class, keyed on the model name in their own sidebar (learned 2026-10-19).** Building a model-retirement-notice brief, the OpenAI deprecations row that led on `6 months` evidenced on the navigation label `GPT-6` before the operational paragraph, while the same page's `3 months` landed on the sentence carrying all three tiers ("At least 6 months … At least 3 months … such as 2 weeks"). Fetchable vendor lifecycle pages, with the figure as plain text, that round: `platform.openai.com/docs/deprecations`, `docs.claude.com/en/docs/about-claude/model-deprecations` (60 days, plus the sentence that partner platforms set their own schedules), `cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions` (per-model release/retirement table, "at least 12 months after release"), and `docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html` (two Legacy periods, 6 months and 45 days). Unreachable to the verifier: every `learn.microsoft.com` and `azure.microsoft.com` model-retirement path tried (HTTP 403), so an Azure notice row cannot carry the gate — write the Azure point in prose or leave it out.

**Hosts probed live 2026-10-15, building a forecast-value-added / naive-benchmark audit brief (the demand_sensing beat).** Carries the figure as plain text and fetches first try: `ideas.repec.org` (a publisher's abstract record for a paywalled journal paper — 20 KB with the study's own numbers as prose: "around 147,000 forecasts from six studies", improvements "for only just over half of stock keeping units (SKUs)", "Positive adjustments were confirmed as more likely to worsen performance"). This is the workaround when the publisher blocks the gate: `sciencedirect.com` and `tandfonline.com` are both **unreachable** to the verifier, but the same paper's abstract is citable through RePEc; `research.manchester.ac.uk` (a university repository record carrying the same abstract text — "more than 60,000 forecasts and outcomes from four supply-chain companies", "the smaller adjustments often damaged accuracy" — so one paper can be reached on a second host when a row needs host diversity); `demand-planning.com` (a practitioner blog reporting Morlidge's study via Gilliland/Tashman/Sglavo — "After studying over 300,000 forecasts they found that a staggering 52% of the forecasts were worse than using a random walk" — label such a row *measured, as cited*, since the page is a secondary citation, never the study itself); `lokad.com` (a supplier reference page: the Gilliland 2010 illustration "11 out of 13 weeks (85% fail rate), averaging 13.8 percentage points of error" and "a forecast might be 40% more accurate but the associated cost means the company makes 75% less profit overall" — a vendor page is the right home for a critique leg, labelled vendor claim); `doss.com` (a vendor survey report dated 18 May 2026 — "DOSS surveyed 661 professionals", 16% did not formally measure forecast accuracy at all, 51% proceed on forecasts they know are unreliable). Fetches but cannot carry an independent row: `infomineo.com` (the demand-sensing-vs-forecasting page states the test — every layer "should have to prove it beats the layer beneath it" — but its only numeric token repeats the Morlidge 52%, so it is corroboration only). Two matcher lessons: on `doss.com` a cell leading on `16%` evidences against the earlier "Private label products: 16%" list and reads as navigation — lead that row on the survey's own `661` and let the percentages ride inside it; and a horizon phrase written `one to four weeks` carries no digit token, so it can never anchor a row (keep such a claim as prose under a verified row). Every leading figure in this brief had to be a digit token (52%, 147,000, 60,000, 13.8, 661).

**Hosts probed live 2026-10-13, building a build-wait / hardware-debt payback brief.** Carries the figure
as plain text and fetches first try: `pugetsystems.com` (the measured-benchmark anchor `bls.gov`'s 403
denies — lab articles print compile times in prose *and* in spec tables that also carry CPU list MSRPs:
"the 32-core 7975WX takes 5 minutes and 30 seconds, while the 64-core 7985WX completes it in 4 minutes
flat", "AMD Ryzen Threadripper PRO 9985WX 8,000 64 … Jul 2025", and the lab's own audit line "the extra
$3500 may be better served elsewhere"); `onetonline.org` (median wage, hourly *and* annual, by occupation);
`eia.gov` energy-explained (retail price by customer class — the commercial rate, not residential, is the
one a workstation payback needs); and NVIDIA's workstation product pages under
`nvidia.com/en-us/products/workstations/professional-desktop-gpus/<part>/`. Fails: `intel.com` spec pages
(403), guessed `amd.com` product URLs (404 — resolve the real slug first), `phoronix.com` review pages
(client-rendered, ~2.3 KB bodies), `ccache.dev/manual` and `bazel.build` (they fetch, but their numeric
tokens are cache/GC timers, not build times), and `dora.dev/research/…` (3 KB landing pages; the report
itself is a PDF).

**A row's `measured`/`vendor claim` cell is a claim too — check it on the page that row cites (learned
2026-10-13).** The gate verifies the figure, never the provenance gloss: a row inherited NVIDIA's
"preliminary product specifications, subject to change" footnote from the RTX PRO 5500 page onto the RTX
PRO 6000 page, which does not carry it. Read the footnote on the named page before writing that cell; a
wrong provenance line survives every gate and misstates how firm the figure is.

**Hosts probed live 2026-10-15, building a cross-border disclosure-penalty brief (what a move abroad obliges a US person to report, and what a miss is charged).** Carries the figure as plain text and fetches first try: `irs.gov` (the FBAR page's $10,000 aggregate trigger, its "whether the account produced taxable income has no effect" sentence and its April 15 date with the automatic October 15 extension; `irs.gov/businesses/corporations/do-i-need-to-file-form-8938-statement-of-specified-foreign-financial-assets` for the $200,000 last-day / $300,000 any-time lines for a taxpayer living abroad and $400,000 / $600,000 on a joint return; `irs.gov/instructions/i5471` — 320 KB, whose penalties section prints the $10,000-per-annual-accounting-period sentence a row can lead on with `90 days`); `law.cornell.edu` (three *different* statutes on one host — 26/6038D, 26/6038, 31/5321 — which is how one publisher can still carry several honest rows); `ecfr.gov` (31 CFR 1010.821's penalty table, whose header prints the edition's own currency — "up to date as of 10/13/2026" — the cheapest as-of anchor for an indexed figure). Fails or cannot carry a row: `oecd.org`, `ssa.gov` and `ato.gov.au` (all HTTP 403 to the verifier), `canada.ca` (unreachable), guessed `tax.ny.gov` telecommuter paths (404 — the convenience-rule pages have moved), and **`fincen.gov`**: the regulator's FBAR page fetches but opens with a stack of disaster-extension notices dated `10/11/2024`, so a `$10,000`-led row matches one of those dates first and its evidence window reads as navigation — cite it as corroboration in the brief, never as a gate row. A comma-grouped `$10,000` always tokenises to `10`/`000`, so lead such a row with a rarer token from the same sentence where one exists (`90 days`, `50 percent`, or the date the ceiling applies from).

**Hosts probed live 2026-10-16, building a roof-settlement / two-payment brief (the `resilient_home_assets` evergreen).** Carries the figure as plain text and fetches first try: `flsenate.gov/Laws/Statutes/<year>/<section>` — the Florida Statutes pages for the *current* edition; § 627.7011 prints the 15-year roof-age rule, the inspection right at the owner's expense and the ACV-first sentence ("the insurer must initially pay at least the actual cash value of the insured loss, less any applicable deductible"), while § 627.701 (24 KB) carries the roof-deductible cap ("the lesser of 2 percent of the Coverage A limit of the policy or 50 percent of the cost to replace the roof") and its five carve-outs — **but lead the cell with the rarer token: a cell beginning "2 percent" evidences on an unrelated subsection (2), while "50 percent" lands on the operative sentence**; `california.public.law/codes/ca_ins_code_section_<n>` (a fetchable mirror of the California codes, insurance sections included — § 2051.5 carries the recovery window ("less than 12 months", "36 months", the 100-day proof-of-loss floor, the six-month good-cause extensions) and § 2051 the measure of indemnity; each page prints its own source line and a "Verified:" date, a free as-of anchor); `content.govdelivery.com/accounts/<AGENCY>/bulletins/<id>` (a state regulator's consumer bulletin — the Iowa Insurance Division's roof-coverage page carries the DOE-attributed "average roof replacement cost is $10,000" and the endorsement warning that a rider "may replace replacement cost coverage with actual cash value", though the page prints no date); `thehartford.com/aarp/homeowners-insurance/recoverable-depreciation` (a carrier's own explainer — the right home for a vendor-claim row: the $900 / $750 / $150 worked example and "we don't pay your replacement cost until you've repaired or replaced the damage"); and `iii.org/fact-statistic/facts-statistics-<topic>` (Triple-I statistics pages fetch at 8–30 KB with the tables as text — severity "$20,062" (2023) against "$13,884" (2019), the cause table's "42.5" wind-and-hail share, the wildfire page's state tables — while every `iii.org/article/...` URL tried returned `unreachable`, so a consumer page is not a citable row there). Fails or cannot carry a row: `readyforwildfire.org`, `usfa.fema.gov`, `fema.gov`, `fire.ca.gov`, `osfm.fire.ca.gov`, `insurance.wa.gov`, `doi.colorado.gov`, `ny.dfs.ny.gov`, `tdi.texas.gov`, `content.naic.org` and `corelogic.com` (all unreachable), `firststreet.org/risk-factor/fire-factor/` (HTTP 200 with a 260-character body), `moen.com` and `phyn.com` product pages (unreachable), `floodsmart.gov`'s subpages (`/flood-insurance`, `/why-flood-insurance`, `/plan-ahead` unreachable while its root page fetches), and `nfpa.org` (a 35-character body). Two costs worth not repeating: probe every candidate through `citation_hub_dossier.fetch_source` **before** choosing the topic — 12 of 22 first-round candidates here were unreachable, including the whole ember-vent/defensible-space beat (`nfpa.org`, `readyforwildfire.org`, `usfa.fema.gov`, `calfire`), which is why the reserve candidate died on evidence and not on argument — and prefer a statute page to a regulator's press release, since the statute prints the figure beside the rule it governs.

**Hosts probed live 2026-10-16, building a manager-hours / true-hourly-rate brief (the `career_velocity_equity_engineering` evergreen).** Carries the figure as plain text and fetches first try: `onetonline.org/link/summary/<SOC>` — **the O*NET summary page carries a measured wage *and* a measured work-week distribution on one page**, which makes it the working anchor for any hours-based pay topic now that `bls.gov` still 403s to the verifier: "Median wages (2025) $84.20 hourly, $175,140 annual" for computer and information systems managers (11-3021.00, whose work context reads 65% responded "More than 40 hours."), $65.38 / $135,980 for software developers (15-1252.00, 90% responded "40 hours.") and $50.85 / $105,770 for general and operations managers (11-1021.00, 70% more than 40 hours). The hourly figure is the annual median spread over 2,080 hours, so an "hours actually worked" claim can be built honestly by dividing a cited annual median by a stated week (the two agreed to the dollar: 84.20 × 2,080 = 175,136). Also fetching: `ecfr.gov/current/title-29/section-541.600` and `/section-541.100` (the overtime-exemption salary floor — $684 per week — and the duties test, two rows on the regulation host, ~9–10 KB each with the section text as plain text, § 541.100's authority note running to 91 FR 27835, May 15, 2026); `irs.gov/publications/p15` (306 KB, the flat 22% supplemental-wage withholding rate, 37% above $1 million, stated as a complete sentence in the 2026 edition). Fails or cannot carry a row: **`ec.europa.eu/eurostat` statistics-explained hours-of-work pages answer 404 to the verifier**, so a European hours series cannot be the counterweight to a US wage row; and — the trap specific to this host — **an O*NET page's numeric task-importance scores precede the work-context block in document order, so a row leading on a percentage evidences on an unrelated score**: a cell beginning `65% responded: More than 40 hours` matched "65 Core Evaluate data processing proposals", and `90% responded: 40 hours` matched "90 Working with Computers". Lead every O*NET row with the distinctive **dollar** figure ($84.20 / $65.38 / $50.85) and let the work-week share ride inside that row as eye-checked gloss rather than giving the share a row of its own. One instrument fact worth knowing before fighting it: `check_accessibility.body_of` strips the `## Sources` section, so the **NET token inside "O*NET OnLine" never fails the acronym gate** — it only matters if the token is spelled out in body prose (as "the Occupational Information Network"), which is why the back catalogue cites O*NET without a definition.

**Hosts probed live 2026-10-16, building a depot-charging / metered-kWh brief (the `last_mile_routing_fleet_carbon` evergreen).** Carries the figure as plain text and fetches first try: `afdc.energy.gov/fuels/electricity-stations` (the DOE Alternative Fuels Data Center charger page — the Level 2 spec as one sentence, "Most residential Level 2 chargers operate at up to 30 Amps, delivering 7.2 kW of power. These units require a dedicated 40-Amp circuit to comply with the National Electric Code requirements in Article 625", plus the 2.9–19.2 kW Level 2 output band, the ~25 miles of range per hour of AC Level 2, the three-phase `SAE J3068` band at 6 kW to 130 kW on 208/120 V and 480/277 V, and the DC-fast ceiling "up to 500 kW" beside "many EVs on the roads today are not capable of charging at rates higher than 200 kW"); `afdc.energy.gov/laws/10513` (a federal credit page whose *status* is the deliverable — the summary table's own headline reads "Expired: 06/30/2026", and the body carries the window "Beginning January 1, 2023, through June 30, 2026", each charging port as "a single item", and "6% of the depreciable costs, up to $100,000 per item; or, 30% … if the installation meets U.S. Department of Labor" wage rules); `afdc.energy.gov/fuels/electricity-benefits` (battery life as text — "may last 12 to 15 years in moderate climates (8 to 12 years in extreme climates)" and the "8-year/100,000-mile battery warranties" line); `eia.gov/energyexplained/electricity/prices-and-factors-affecting-prices.php` (15 KB, the annual price by customer class *and* the state spread — "13.63¢ per kilowatthour" U.S. average for 2025, "35.72¢ per kWh in Hawaii to 8.20¢ per kWh in North Dakota", the class table residential 17.30¢ / commercial 13.41¢ / industrial 8.62¢, with the tables it cites named in the footnotes); and `fueleconomy.gov/feg/evtech.shtml` (6 KB, "Battery charging efficiency can vary, but it is often 84% to 93%, based on published studies … and data from the Idaho National Laboratory" plus "EVs convert over 77% of the electrical energy from the grid to power at the wheels" against "12%–30%" for gasoline). **Guessing AFDC paths wastes a probe round:** `afdc.energy.gov/fuels/electricity_charging.html`, `…/electricity-infrastructure.html` and `…/vehicles/electric-emerging-technologies.html` all answer 404 to the verifier — resolve the real slug (`/fuels/electricity-stations`, `/laws/<n>`, `/fuels/electricity-benefits`) from a web search before probing. **Two rows on this beat want a rarer lead token:** a cell beginning `40-Amp circuit` evidences on "about 40 miles of electric range" earlier in the page (lead with `7.2 kW`, whose window is the operative sentence), and `200 kW` evidences on the DC heading "100 to 200+ miles of range per 30 minutes" — so carry the ~200 kW vehicle-acceptance caveat inside the `500 kW` row, which windows on the DC-fast sentence, and never give it a row of its own. Fails or is unneeded here: `bls.gov` is still 403 and no wage row was needed; the DOE/EPA explainer pages carry the spec, the price and the losses, but **no fetched source prices a depot's demand charge or its utility interconnection queue** — that is a stated gap in the article, not a row. One drafting fact worth carrying: the frontier re-cut a hand-set STRONG title on this run (to "Fleet Architects: 7.2 kW Sets Your Charger Gap") and restored it at audit time, so score the `_final.md`'s title against its own body before persisting, not only the draft's.

**Hosts probed live 2026-10-19, building an assessment-carrying-cost brief (what a completed improvement costs
every year after the cap).** Carries the figure as plain text and fetches first try: `flsenate.gov/Laws/Statutes/<year>/<section>`
(Florida Statutes § 193.155 — the cap sentence "(a) Three percent of the assessed value of the property for the prior
year", plus subsection (9)(b), which assesses changes, additions or improvements at just value as of the first January 1
after they were substantially completed); `legislature.mi.gov/Laws/MCL?objectName=mcl-<section>` (MCL 211.27a(2)(a) —
"multiplied by the lesser of 1.05 or the inflation rate, plus all additions" — and MCL 211.34d(1)(b)(iii), which defines
new construction as property "not in existence on the immediately preceding tax day and not replacement construction",
the plainest statutory statement of the renewal-versus-addition split); `oregon.public.law/statutes/ors_<section>`
(ORS 308.146(1) — "103 percent of the property's assessed value from the prior year" — and ORS 308.153, new improvements
at real market value); `california.public.law/codes/ca_rev_and_tax_code_section_<n>` (§ 2192's "12:01 a.m. on the first
day of January"; § 70(a)'s definition of new construction).
**A statute's small integers collide with its own subsection numbering**: § 51's "2 percent" cap generates the token `2`
and evidences on "Section 2 of Article XIIIA", so that claim was quoted in prose with the section cited in Sources
instead of shipped as a row — the same class as the eCFR banner date. Lead a statute row on a figure the section states
once and rarely (`1.05`, `103 percent`, `12:01`, a comma-grouped dollar threshold), never on a bare `2`, `3` or `10`;
a cap written in words is matchable if the whole cell is digit-free (`Three percent — …` resolves through
`_WORD_NUMBERS`, while `3 percent` would probe the first stray `3`). Unreachable to the verifier, so no rate row can
carry this beat: `census.gov`, `taxfoundation.org`, `floridarevenue.com`, `boe.ca.gov`, `oregon.gov/dor` and
`…/ca_rev_and_tax_code_section_110_1`. A carrying-cost article therefore states the statutory caps and leaves the
county rate to the reader's own tax bill rather than inventing a national average.

## 5. Handoff

Only after `PASS`: `skills/fact_check.md` → `skills/story_draft.md` → `skills/claude_humanizer.md`
→ `scripts/publish.py`. The article keeps the house schema (section markers, `## Sources`, the
LinkedIn variant) and adds two frontmatter flags so the reader surfaces and the audit can tell it
apart from a news piece:

```yaml
archetype: evergreen
evergreen: true
```

Persistence to the site + Supabase is **not** approval-gated. Outbound distribution (LinkedIn /
Ghost / Reddit) waits for the founder's `@Simon approve` gate, exactly as the news track does.

## 6. Failure handling

- **No candidate clears ≥ 8** → return "no publish", log the axes table to
  `skills/self_improvement_eval.md`, and say what evidence was missing. Never pad.
- **A source stops resolving** (moved, paywalled, deleted) → replace the row and re-run the gate;
  never drop the figure's citation and keep the claim.
- **The de-dup names nothing** → look at `context/published_log.md` and
  `context/recon_proposals/*_<vertical>_*` for the last 180 days before re-arguing a thesis you
  already ran.
- **The topic is really news** (value expires in < 90 days) → hand it to the news track; do not
  smuggle it here, where the freshness gate cannot see it.
