# Published Log

Append-only record of articles that cleared the `@Simon approve` gate and were copied into
`published/`. Ground truth for "is it live?" is `published/*.md` itself — this table must never
list a file that is not there. Rows are appended in publish order, not re-sorted.

| Date | Vertical | Slug | Headline | Reader URL | Distribution |
|---|---|---|---|---|---|
| 2026-09-03 | supply_chain | customs-enforcement-operational-risk | On Sept 18, a stale address can void your importer number and stop your cargo at the port | https://pressflow.aichieve.net/published/2026-09-03_customs-enforcement-operational-risk.md | manual review (LinkedIn auto-post off) |
| 2026-09-04 | home_systems_reno | electrification-rebate-window-closes | The federal rebate for swapping your gas furnace for a heat pump just died | https://pressflow.aichieve.net/published/2026-09-04_electrification-rebate-window-closes.md | manual review (LinkedIn auto-post off) |
| 2026-09-07 | agentic_ai | anthropic-multiagent-turf-war | Anthropic's own red team watched three Claude agents sabotage each other with self-replicating malware — no attacker required | https://pressflow.aichieve.net/published/2026-09-07_anthropic-multiagent-turf-war.md | manual review (LinkedIn auto-post off) |
| 2026-09-07 | supply_chain | ieepa-refund-wave-hits-earnings | The $166B tariff clawback is finally hitting earnings — and the biggest check was never filed | https://pressflow.aichieve.net/published/2026-09-07_ieepa-refund-wave-hits-earnings.md | manual review (LinkedIn auto-post off) |
| 2026-09-03 | agentic_ai | owasp-excessive-agency-2026 | OWASP's 2026 LLM Top 10 is the first built on incident data — and the danger moved from the model to the permissions | https://pressflow.aichieve.net/published/2026-09-03_owasp-excessive-agency-2026.md | manual review (LinkedIn auto-post off) |
| 2026-09-08 | enterprise_tech_leadership | cloud-repatriation-roi-calculator-bare-metal | Cloud Repatriation Roi Calculator Bare Metal: Production Architecture & Cost Reality | https://pressflow.aichieve.net/published/2026-09-08_cloud-repatriation-roi-calculator-bare-metal.md | manual review (LinkedIn auto-post off) |
| 2026-09-08 | enterprise_tech_leadership | mckinsey-ai-roi-flat-build-vs-buy-flip | AI adoption hit an all-time high in 2026 — and the share of companies seeing real earnings from it didn't move | https://pressflow.aichieve.net/published/2026-09-08_mckinsey-ai-roi-flat-build-vs-buy-flip.md | manual review (LinkedIn auto-post off) |
| 2026-09-08 | agentic_ai | mcp-server-implementation-python | Mcp Server Implementation Python: Production Architecture & Cost Reality | https://pressflow.aichieve.net/published/2026-09-08_mcp-server-implementation-python.md | manual review (LinkedIn auto-post off) |
| 2026-09-09 | gpu_hardware | nvidia-279b-memory-bottleneck | Nvidia says its GPUs aren't sold out. Its CFO's $279 billion memory bet says otherwise. | https://pressflow.aichieve.net/published/2026-09-09_nvidia-279b-memory-bottleneck.md | manual review (LinkedIn auto-post off) |
| 2026-09-10 | agentic_ai | google-agents-challenge-four-patterns | The four patterns that actually won Google's AI Agents Challenge | https://pressflow.aichieve.net/published/2026-09-10_google-agents-challenge-four-patterns.md | manual review (LinkedIn auto-post off) |
| 2026-09-10 | supply_chain | reshoring-capacity-gap | Reshoring hit a wall — satisfaction fell from 96% to 65% as tripled investment bought 1.5% capacity | https://pressflow.aichieve.net/published/2026-09-10_reshoring-capacity-gap.md | manual review (LinkedIn auto-post off) |
| 2026-09-11 | home_systems_reno | nys-weatherized-tier-heat-pump-rebate | New York heat pump rebate pays double to sealed homes | https://pressflow.aichieve.net/published/2026-09-11_nys-weatherized-tier-heat-pump-rebate.md | manual review (LinkedIn auto-post off) |

## Corrections (2026-09-12 integrity audit)

- Removed duplicate rows: `customs-enforcement-operational-risk` (09-03) and
  `electrification-rebate-window-closes` (09-04) were each logged twice.
- `owasp-excessive-agency-2026` (09-03) had been logged here as published while the file existed
  only in `context/drafts/`. It is genuinely published from 2026-09-12 (row above, after approval);
  the earlier row was still a false claim at the time it was written.
- Replaced the placeholder `local/site` target with the resolvable reader URL for each row.
- Table rebuilt to six explicit columns (`Reader URL`, `Distribution`) so the publisher
  (`scripts/publish.py::record_publish`) can insert rows in place instead of appending at EOF —
  the old format's free-text `targets`/`live URLs` columns are what let the log drift from the
  filesystem unnoticed.
- `scripts/publish.py` hardened in the same pass: it now loads the repo `.env` (previously it ran
  with no Supabase credentials when invoked from a shell, so the "always upsert" step silently
  skipped) and normalises slugs that already carry a date prefix (which had produced
  `published/<date>_<date>_<slug>.md`).

## Approval record (2026-09-12)

Owner approved publishing the eight drafts held at the gate since 09-03 (OWASP, three from 09-08,
NVIDIA 09-09, two from 09-10, NYS heat-pump 09-11). All eight were published on 2026-09-12 and
upserted to Supabase (`articles`); the table above is the record.

## Awaiting approval — NOT published

None as of 2026-09-12: every finished draft in `context/drafts/` has been published. New drafts land
here (or in this section) only after a pipeline run finishes and before the `@Simon approve` gate.
