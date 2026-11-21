# Run log: your-applecare-79-96-vs-89 — 2026-11-20 (evergreen, consumer_asset_repair_replace_tco)

## What ran
- STEP 0 gate: GENERATION OK (evergreen ON for consumer_asset_repair_replace_tco).
- Topic from `primary_angles[2]` (warranty/extended-plan vs self-insure) — the only primary_angle of this
  vertical no artifact had ever taken. Cross-corpus grep: AppleCare appears only as context in
  your-screen-gap-999-vs-99 (single-device repair risk) and your-battery-expires-at-500-cycles (the swap
  itself); this piece prices the plan as a household insurance contract.
- Brief: 11 rows, 3 hosts (apple.com/support/products, support.apple.com/iphone/repair,
  ifixit.com/Wiki/iPhone_Battery_Replacement). Gate FAIL once on row 11 (word-number figure cell
  "Three —" → rewrote as "3 —", digits lead the cell) then PASS. Gate re-run after an arithmetic
  correction (add-on path: $5.99/mo = $71.88/device-yr, CHEAPER per device than the base's implicit
  $79.96 — the first brief draft had this backwards; recomputed 4/5/6-device pools).
- Verified brief: 11 VERIFIED, 1 FLAGGED (Apple's per-device US AppleCare+ price table renders model
  names without dollars; program-summary PDF returns 0 bytes; repair page renders "Pricing failed to
  load" — uninsured accidental-damage ladder left as the reader's own variable, per the fridge
  evergreen's FLAG-3 precedent).
- Draft: headline "Your AppleCare Costs $79.96 a Device" 100/100 STRONG, lead_ok True. Pre-tune:
  accessibility FAIL at Flesch 43.5 → word swaps (no sentence-splitting) to 52.1 PASS; critic FAIL on
  At-a-glance 53 words → trimmed to 50; article_shape advisory only.
- Frontier (deepseek-v4-pro): ACCEPT attempt 1, hard=0, rhythm 7.5→7.5.
- Gates: 8/8 ok (accessibility, shape, critic, headline, sources, review_audit, voice, publish_gate).
- Publish: post 1810 (status publish), term 40, kind tag 44 (evergreen), category 2 (Major Purchases &
  Assets), media 1809, Supabase row f77cb888-14ec-4702-880f-d31bc91f81ae; sitemap refreshed; auto-deploy
  pushed. Front 404 at t+1 min (build lag), 200 at t+4 min with title, og:image, and the inline
  tech-debt-repair calculator link live.

## Score
U9 D8 E8 A9 = 8.6 (in brief: use 9 / durability 8 / evidence 8 / actionability 9 — composite 8.6).

## Notable
- apple.com/legal AppleCare+ disclosures PDF (2509/...) answers 0 bytes to the fetcher — figures from
  it are unusable for the evergreen gate; the live /support/products/ page carries AppleCare One tiers
  and service fees in plain text and is the workhorse source.
