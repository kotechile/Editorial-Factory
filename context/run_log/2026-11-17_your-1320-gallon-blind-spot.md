# Run log — 2026-11-17 · nhil_infrastructure_ops · EVERGREEN

**Artifact:** `published/2026-11-17_your-1320-gallon-blind-spot.md` — "Your 1,320-Gallon Blind Spot"
**Slug:** `your-1320-gallon-blind-spot` · **kind:** evergreen · **persona:** `it_ops_leader`
**Surfaces:** Supabase `aa742d32-d7a5-4729-9b61-a25b0007023c` · WordPress post 1752 (status publish,
tag 44 `evergreen`, vertical term 38) · media 1751 · front `https://aichieve.net/your-1320-gallon-blind-spot/` (200, hero + 4 internal links)

## Topic selection
Gate (`generation_gate.py --mode evergreen --vertical nhil_infrastructure_ops`) returned GENERATION OK.
`run_pipeline.py start` printed the four angles and the three titles not to repeat (11-17 check/probe,
11-10 certificate, 11-03 1N plant). GSC export returned 0 opportunities (young site, thin impressions —
bonus signal only).

Lead: the vertical's own `primary_angles` entry "substation interconnection queues and behind-the-meter
power", the persona's `wants`, founder-voice §3 ("governed by thermal and electrical physics"), and the
customer-truth anecdote of the fintech that hit a 38-month utility queue and pivoted to behind-the-meter
generation. That pivot is where a site starts storing fuel; the storage rulebook has not been argued in
this vertical. Corpus grep for `SPCC`, `spill prevention`, `secondary containment`, `1,320` returned no
published artifact; the `diesel` hits are freight fuel-surcharge pieces in the logistics verticals.

## Candidates and scores
| Topic | U | D | E | A | Composite | Verdict |
|---|---|---|---|---|---|---|
| Backup fuel storage counted by container (SPCC / UST) | 9 | 9 | 8 | 9 | 8.8 | winner |
| Refrigerant step-down (AIM Act GWP) | 8 | 6 | 6 | 8 | 7.0 | dropped — rule under reconsideration; no GWP ceiling evidenced in 40 CFR 84 on first probe |
| 48V DC busbar vs AC PDU (ORV3) | 9 | 9 | 6 | 8 | 8.0 | dropped — opencompute.org document PDFs unreachable to the verifier |
| Li-ion UPS cabinet spacing (NFPA 855) | 8 | 8 | 5 | 9 | 7.4 | dropped — codes.iccsafe.org serves a captcha to the verifier; NFPA paywalled |

## Gate
`evergreen_gate.py --brief` PASS: 6 rows, 6 fetched, 5 distinct URLs, 2 hosts (ecfr.gov, law.cornell.edu),
dedup matched `2026-11-03_your-backup-66-mw-permit-trap`.

## Verification
10 claims VERIFIED, 1 FLAGGED (the 40 CFR 280.12 heating-oil exclusion is a definition, not a ruling that
generator fuel escapes Part 280 — the draft quotes it and refuses to design around it). No REMOVED claims.
Writer-side draft: Flesch 54.0, headline 100/100, shape ok.

## Frontier pass
`article_reviewer.py` ran three attempts. Attempt 3 audited clean (hard=0, regressions=0) but the run kept
attempt 1 by score (hard=0, 2 flow regressions) and wrote the pair to `context/drafts/reviews/` as HELD.
Adopted attempt 1 per the `hard=0` rule and repaired by hand:
- replaced the banned cue "My reading, held loosely:" (boilerplate family, `skills/claude_humanizer.md` §3.8)
  with "Where I've landed:";
- restored the opening's "driven by" clause so the lead answers *why* the count grows;
- rebuilt sentence-length variance (short beats beside connected sentences) and cut hedges;
- split a 7-sentence paragraph.
`article_reviewer.py --audit` on the repaired pair: PASS.

## Gates at the push
`run_pipeline.py gate --file …_final.md`: accessibility ok, shape ok, critic ok, headline ok, sources ok,
review_audit ok, voice ok (the 4 problems reported are pre-existing drafts from 11-08/11-09), publish_gate ok.
Reader-side: Flesch 54.6, headline 100/100, mean 18.6 words/sentence.

## Persistence
`run_pipeline.py publish` — published artifact, published log, Supabase row, sitemap, CMS post (status
publish), internal-links block (3 links) before `## Sources`, metadata.wordpress recorded, auto-deploy pushed.
Hero verified on the rendered front (`-1024x576` derivative 200, og:image set).

**Alt repair:** the art director's alt text shipped as two sentences with a title-cased possessive
("Backup Fuel'S …"). `scripts/fix_alt_blindspot_1117.py` rewrote it to one 100-character sentence in all
four places (sidecar revision 4, published artifact, `_final.md`, WP media 1751, Supabase
`metadata.illustration.alt_text` / `wordpress.media_alt`) and read both back.

## Open / lessons
- The reviewer's attempt selector orders by score after hard-failure filtering, so a regression-free
  attempt can lose to a higher-scoring one that regresses rhythm. Re-run with `--keep-attempts` or hand-adopt.
- Comma-grouped figure cells split into tokens in `figure_evidence` (`1,320` → `1`, `320`; `10,000` → `10`,
  `000`), so the first token evidences on an early stray digit. Lead such rows on a comma-free token from
  the same sentence and let the comma figure ride in the row's gloss / prose.
- Host walls on this beat: `epa.gov` SPCC paths, `opencompute.org` document PDFs, `codes.iccsafe.org`
  (captcha), `apnic.net` / `arin.net`, and `federalregister.gov` document HTML all unreachable to the
  verifier; `federalregister.gov`'s API JSON does fetch. `law.cornell.edu` and `ecfr.gov` fetch first try.
