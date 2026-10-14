# Verified Brief: agentic_resilience_failure — 2026-10-14 (EVERGREEN track)

Archetype: evergreen. Topic = **the boundary between steps is where an agent's reliability is decided**:
a fault compounds along a chain of unverified steps (11–14x on the next step, recovery in 30.5% of runs,
38.5% never detected), the controls that act on propagation have measured effects (circuit breakers −89%
cascade propagation, isolation −64% blast radius, output gates 73% of silent degradation, three or more
patterns −71% mean time to recovery), and removing enforcement measurably collapses containment while the
run spends *more* compute. Every external claim below traces to a source the evergreen gate fetched live
and confirmed contains the cited figure (6/6 gate rows verified on 3 hosts, `<!-- evergreen-gate: -->`
marker in `context/recon_proposals/2026-10-14_agentic_resilience_failure_evergreen_brief.md`).

| # | Signal Leg | Claim | Status | Source URL | Verbatim |
|---|---|---|---|---|---|
| 1 | Chain compounding | A single wrong step makes the next step **roughly 11 to 14 times** likelier to be wrong | VERIFIED | https://arxiv.org/html/2609.17930v1 | "Once made, an error spreads: a single wrong step makes the next roughly 11 to 14 times likelier to be wrong, so the later a run goes, the more of it is inherited error" |
| 2 | Recovery / detection | After its first mistake an agent recovers in only **30.5%** of runs and **never detects** the error in **38.5%** of them | VERIFIED | https://arxiv.org/html/2609.17930v1 | "after its first mistake, an agent recovers in only 30.5% of runs and never detects the error at all in 38.5%, yet keeps acting either way" |
| 3 | Corpus + reproduction detail | **2,518** trajectories, **6,967** mistakes classified into **78** failure types; six frontier judges fail to spot the first mistake in roughly two-thirds of runs ("fewer than a third"), while a **4-billion-parameter** verifier ("Scout", built on Qwen3-4B-Thinking-2507) located failure better and transferred to unseen domains | VERIFIED | https://arxiv.org/html/2609.17930v1 | "We study 2,518 agent trajectories across software engineering, computer use, and science, close to real deployment, and classify 6,967 mistakes into 78 failure types." / "even the strongest correctly identifies the first mistake in fewer than a third of runs. Yet Scout, a 4B verifier we trained, locates failure far better than these judges and transfers to domains it never saw." |
| 4 | Boundary controls, measured | **89%** cascade reduction from circuit breakers, **73%** of silent degradation caught by output quality gates, **64%** blast-radius reduction from component isolation, **71%** mean-time-to-recovery reduction for systems running three or more patterns | VERIFIED | https://arxiv.org/html/2610.02503v1 | "Circuit breakers reduce cascade propagation by 89%, output quality gates catch 73% of silent degradation before user impact, and component isolation reduces blast radius by 64%. Systems implementing three or more resilience patterns from our catalog reduce mean-time-to-recovery (MTTR) by 71% compared to unstructured monitoring baselines." |
| 5 | Boundary-shaped taxonomy | **150** production incidents → **23** failure modes in **five** categories (retrieval, generation, tool, orchestration, integration); the failure class is the seam, not the part | VERIFIED | https://arxiv.org/html/2610.02503v1 | "We analyze 150 production incident reports from open-source compound AI projects and anonymized enterprise deployments to construct a taxonomy of 23 failure modes organized into five categories: retrieval failures, generation failures, tool failures, orchestration failures, and integration failures." / "Cascading errors propagate across component boundaries, silent quality degradation evades standard monitoring, and coordination failures yield incorrect collective behavior from individually correct parts." |
| 6 | Containment ladder, ablated | Removing quarantine/rollback drops containment to **3.1%** (against **2.2%** with no defense and **14.4%** with screening/verification removed); the no-blocking variant spends the most tokens (**34,991**) and the most wall-clock time (85.7 ± 21.0 s) yet contains almost nothing | VERIFIED | https://arxiv.org/html/2603.04474v2 | "Removing quarantine or rollback further reduces BICR to 3.1 ± 10.1%, close to the None setting at 2.2 ± 14.7%." / "Without atomization, BICR remains at 40.0 ± 49.0%… Removing screening and verification lowers BICR to 14.4 ± 35.2%" / "The no_blocking variant consumes the most tokens, 34,991, and takes 85.7 ± 21.0 s, yet its BICR is only 3.1%." |
| 7 | One seed is enough | One injected atomic error seed cascades into widespread failure; three vulnerability classes — cascade amplification, topological sensitivity, consensus inertia; six mainstream frameworks tested | VERIFIED | https://arxiv.org/html/2603.04474v2 | "Through experiments on six mainstream frameworks, we identify three vulnerability classes: cascade amplification, topological sensitivity, and consensus inertia. We further instantiate an attack where injecting just a single atomic error seed leads to widespread failure." |
| 8 | Silence in production | **22** incidents in an **eight-week** window (2026-04-09 → 2026-06-02), every one with a silent phase; one meta-pattern appeared **at least 28 times** | VERIFIED | https://arxiv.org/html/2606.14589v1 | "Over an eight-week window we documented 22 incidents with full root-cause postmortems, within which a single meta-pattern—a failure whose error signal never reaches a human in actionable form—manifested at least 28 times." / "had a silent phase—a period in which the system was failing or had failed while all automated indicators stayed green" |
| 9 | Detection beats repair | Roughly **70%** of silent failures were caught by a human looking at output, not by tests or audits; a retrospective audit of **15** incidents gave the governance layer a **0%** ex-ante prevention rate but an **87%** ex-post regression-blocking rate; for silent failures, time-to-detect dominates time-to-repair by one to two orders of magnitude | VERIFIED | https://arxiv.org/html/2606.14589v1 | "roughly 70% of silent failures were ultimately caught by human user-view observation of system output, not by unit tests, health checks, or governance audits—all of which stayed green through most incidents" / "a retrospective audit of 15 incidents found our declarative governance layer had a 0% ex-ante prevention rate but an 87% ex-post regression-blocking rate—audits are regression engines, not prediction engines" |
| 10 | The amplification mechanism | **80.4%** error rate from a 5% fault: 5% of requests sitting on a 100-second deadline consume 5,000 thread-seconds of a 1,000-thread frontend, leaving only **19.6%** of requests served | VERIFIED | https://sre.google/sre-book/addressing-cascading-failures/ | "With a 100-second deadline, 5% of requests would consume 5,000 threads (50 QPS * 100 seconds), but the frontend doesn't have that many threads available. Assuming no other secondary effects, the frontend will only be able to handle 19.6% of the requests (1,000 threads available / (5,000 + 95) threads' worth of work), resulting in an 80.4% error rate." |
| 11 | Operational demand (context) | **41.1%** of surveyed engineers meet agent issues daily or more (**9.0%** "continuously"), and the top blocker to using agents more is **tracking state**, ahead of debugging and cost; 554 respondents, fielded 2026-04-29 → 2026-05-25 | VERIFIED | https://temporal.io/reports/state-of-development-2026 | "But also: 41.1% encounter issues daily or more; 9.0% say 'continuously'" / "Top blockers to using AI agents more: #1 tracking state, #2 debugging, #3 managing costs" / "Between April 29 to May 25, 2026 we commissioned the survey provider Qualtrics to solicit responses from 650 respondents currently using AI agents… We removed all responses we considered low quality and were left with 554 respondents." |

## Gate rules applied
- 11/11 claims VERIFIED against the fetched primary page; 0 REMOVED, 0 FLAGGED.
- Hosts among the six gate rows: arxiv.org (rows 1–9, four distinct papers), sre.google (row 10),
  temporal.io (row 11). Four arXiv papers are four different author groups; the two non-arXiv hosts
  are independent of them.
- No synthesis: single-signal evergreen topic; the dual-anchor gate does not apply.
- **Boundary wording for drafting:**
  - Rows 1–3 are a **lab study** (2,518 trajectories, "close to real deployment", as of the paper dated
    2026-09-15). Write the 11–14x as "roughly", never as an exact factor, and never as a production
    base rate.
  - Rows 4–5 are **controlled fault injection** over a 150-incident taxonomy (as of 2026-10-01). Say
    "in controlled fault-injection tests", not "in production".
  - Rows 6–7 are a **defense ablation** (as of the paper's v2, 2026-05-11) whose spreads are enormous
    (± 35.2 and ± 49.0 percentage points in places) — quote the point value with its spread or say
    "highly variable across runs"; never present 3.1% as a precise field estimate.
  - Rows 8–9 are one operator's **production postmortem corpus** (2026-04-09 → 2026-06-02, single
    system, not independently replicated) — attribute it ("one operator's eight-week corpus"), never
    "across production systems".
  - Row 10 is the book's own **worked example** from stated parameters, and it explicitly assumes "no
    other secondary effects".
  - Row 11 is a **vendor-sponsored survey** (Qualtrics, 554 respondents, fielded April–May 2026).
- Durability guard: the load-bearing facts are the mechanism (compounding along unverified steps; a
  boundary control acting on propagation) and the *direction* of every measured control; the
  percentages are dated and will drift as models improve. The article must not name a model version or
  a framework release as the thesis.
- Plain-English expansions the body must carry at first use: **MTTR** → "mean time to recovery (MTTR)";
  prefer "large language model" written out or "model" rather than a bare three-letter token;
  the two threat terms from row 7 need a gloss (cascade amplification = one bad step spreading;
  topological sensitivity = the wiring deciding how far it spreads; consensus inertia = agents agreeing
  with a wrong answer).
- Numbers the draft may use: 2,518 / 6,967 / 78 / 4 billion / 11–14x / 30.5% / 38.5% / 150 / 23 / five
  categories / 89% / 73% / 64% / 71% / 3.1% / 2.2% / 14.4% / 34,991 / 85.7 s / six frameworks / 22 / eight
  weeks / 28 / 70% / 15 / 0% / 87% / 5% / 100-second / 1,000 threads / 19.6% / 80.4% / 41.1% / 9.0% / 554.
  No other figure is authorised; a rewrite that produces one is reverted to qualitative wording.

De-dup: nearest prior artifact for this vertical is `2026-10-14_retry-permission-leaves-the-caller`
(news, published today — who may authorise a retry and whether the caller's compliance is measurable),
with `2026-10-07_retry-is-the-failure-amplifier` (the retry primitive duplicates an effect and reports
success) and the nearest published evergreen `2026-10-07_agent-memory-poisoning-write-path` (the memory
write path). This piece argues containment at the step boundary, and its evidence set (Traverse, the
150-incident fault-injection catalogue, the six-framework ablation, the eight-week postmortem corpus,
the SRE chapter, the 2026 practitioner survey) is disjoint from all three.
