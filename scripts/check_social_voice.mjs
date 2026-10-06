#!/usr/bin/env node
/**
 * scripts/check_social_voice.mjs — verify.sh §9, the article voice gate.
 *
 * The reader-facing body must read as one person commenting on the news, not as the owner of the
 * truth and not as the reader's advisor (skills/claude_humanizer.md §3.9). This checks every
 * artifact dated >= VOICE_ENFORCED_FROM (drafts and published copies — older artifacts are
 * grandfathered, their voice predates the rule):
 *
 *   1. each interpreting section (`<!-- tension -->`, `<!-- tactical-insight -->`,
 *      `<!-- nuanced-takeaway -->`) carries a first-person observer cue, and
 *   2. the whole reader-facing body is free of verdict / consultant / imperative constructions.
 *
 * Usage:
 *   node scripts/check_social_voice.mjs              # gate (exit 1 on any violation)
 *   node scripts/check_social_voice.mjs --self-test  # prove the rules bite (embedded fixtures)
 *   node scripts/check_social_voice.mjs --json       # machine-readable
 *   node scripts/check_social_voice.mjs --phase articles
 *
 * History: this gate also checked the authored `<!-- linkedin -->` variant and the
 * app-promotion cards. Both went with the LinkedIn/Reddit channels (removed by the owner
 * 2026-10-06), so what remains is the long-form contract. Artifacts written before that still
 * carry the block; it is ignored here because no surface ships it.
 *
 * What it cannot do: judge whether the point of view is any good. It enforces the mechanical floor
 * (an observer cue present, the authority constructions gone) so the taste question is never
 * decided by omission.
 */
import { readFile, readdir } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import { VOICE_ENFORCED_FROM, inspectLongform, INTERPRETING_SECTIONS } from '../site/social_voice.mjs';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');

const dateOf = (name) => (name.match(/^(\d{4}-\d{2}-\d{2})_/) || [])[1] || '';

async function artifacts() {
  const out = [];
  for (const dir of ['context/drafts', 'published']) {
    const path = join(ROOT, dir);
    if (!existsSync(path)) continue;
    for (const name of (await readdir(path)).sort()) {
      if (!name.endsWith('.md')) continue;
      const date = dateOf(name);
      if (!date || date < VOICE_ENFORCED_FROM) continue; // grandfathered: voice predates the rule
      out.push({ dir, name, path: join(path, name), text: await readFile(join(path, name), 'utf8') });
    }
  }
  return out;
}

async function checkArticles(report) {
  for (const file of await artifacts()) {
    // The legacy `<!-- linkedin -->` block is not reader-facing copy and no surface ships it, so
    // the body is everything before it (an artifact written since the channel was removed has no
    // block at all, and splitting on an absent marker returns the whole text).
    const body = String(file.text).split(/<!--\s*linkedin\s*-->/i)[0];
    const inspection = inspectLongform(body);
    for (const v of inspection.violations) {
      report.problems.push(`${file.dir}/${file.name}: article body ${v.label} — "${v.match}" … ${v.snippet}`);
    }
    for (const section of inspection.missingCues) {
      report.problems.push(`${file.dir}/${file.name}: <!-- ${section} --> has no observer cue — the body `
        + `is a comment on the news, so each interpreting section needs one ("I've been watching…", `
        + `"My read:", "The part I keep circling:", "What I'd watch next:") per skills/claude_humanizer.md §3.9`);
    }
    report.checked.push(`article ${file.dir}/${file.name}`);
  }
}

/** Long-form fixtures: the interpreting sections must carry a cue, and the body must not prescribe. */
const LONGFORM_SELF_TEST = [
  {
    name: 'article body, playbook voice (the pre-§3.9 tariff draft)',
    markdown: '---\ntitle: "Probe"\n---\n\n'
      + '<!-- lead -->\nWashington delayed the tariff truce to Jan. 10, 2027 [1].\n\n'
      + '<!-- tension -->\nFirms are hoarding refunds as cash instead of reinvesting them [2].\n\n'
      + '<!-- tactical-insight -->\n**The playbook:** Treat Jan. 10 as a live deadline and position for it now.\n\n'
      + '- Stress test your landed costs if suspended tariffs return.\n'
      + '- Match your cash posture to your tariff exposure.\n\n'
      + '<!-- nuanced-takeaway -->\nHoarding cash is also just smart liquidity management.\n\n'
      + '<!-- tldr -->\n- **The Winning Moves:** Lock in suppliers now.\n\n'
      + '<!-- linkedin -->\nThe signal is clear: CFOs are pricing in a cliff.\n',
    expectOk: false,
    expectMissingCues: ['tension', 'tactical-insight', 'nuanced-takeaway'],
  },
  {
    name: 'article body, observer voice',
    markdown: '---\ntitle: "Probe"\n---\n\n'
      + '<!-- lead -->\nWashington delayed the tariff truce to Jan. 10, 2027 [1].\n\n'
      + '<!-- tension -->\nFirms are hoarding refunds as cash instead of reinvesting them [2]. '
      + 'That gap is the part I keep circling.\n\n'
      + '<!-- tactical-insight -->\n**Where this bites:**\n\n'
      + '- Operators are re-quoting every landed-cost model I have seen this week.\n\n'
      + '<!-- nuanced-takeaway -->\nMy read: hoarding is also just sound liquidity management.\n\n'
      + '<!-- tldr -->\n- **What I\'d Watch:** Whether the December sourcing numbers move.\n\n'
      + '<!-- linkedin -->\nI keep coming back to one number from the Atlanta Fed.\n',
    expectOk: true,
    expectMissingCues: [],
  },
  {
    name: 'article body, no cue in the tactical section',
    markdown: '<!-- lead -->\nA tariff truce was extended [1].\n\n'
      + '<!-- tension -->\nI keep coming back to the refund numbers [2].\n\n'
      + '<!-- tactical-insight -->\n**Where this bites:**\n\n'
      + '- Operators are re-quoting landed-cost models.\n\n'
      + '<!-- nuanced-takeaway -->\nMy read: this is liquidity management.\n',
    expectOk: false,
    expectMissingCues: ['tactical-insight'],
  },
];

function selfTest() {
  const failures = [];
  for (const fixture of LONGFORM_SELF_TEST) {
    const result = inspectLongform(fixture.markdown);
    if (result.ok !== fixture.expectOk) {
      failures.push(`${fixture.name}: expected ok=${fixture.expectOk}, got ${result.ok} `
        + `(violations=[${result.violations.map((v) => v.label).join(', ')}], `
        + `missingCues=[${result.missingCues.join(', ')}])`);
      continue;
    }
    for (const section of fixture.expectMissingCues) {
      if (!result.missingCues.includes(section)) {
        failures.push(`${fixture.name}: expected <!-- ${section} --> to be flagged without a cue, got `
          + `[${result.missingCues.join(', ') || 'none'}]`);
      }
    }
    console.log(`✓ article: ${fixture.name} — ${result.ok ? 'passes' : `${result.violations.length} violation(s), ${result.missingCues.length} section(s) without a cue`}`);
  }

  if (failures.length) {
    console.error(`\n${failures.length} self-test case(s) failed:`);
    for (const f of failures) console.error(`  ✗ ${f}`);
    return 1;
  }
  console.log(`\nvoice rules bite as specified `
    + `(${INTERPRETING_SECTIONS.length} interpreting sections must each carry an observer cue).`);
  return 0;
}

const report = { problems: [], checked: [] };

if (process.argv.includes('--self-test')) {
  process.exit(selfTest());
}

const phaseIndex = process.argv.indexOf('--phase');
const phase = phaseIndex > -1 ? process.argv[phaseIndex + 1] : '';
if (phase && phase !== 'articles') {
  console.error(`unknown --phase '${phase}' — the only phase left is 'articles' `
    + `(the social-variant phases went with the LinkedIn/Reddit channels)`);
  process.exit(2);
}

await checkArticles(report);

if (process.argv.includes('--json')) {
  console.log(JSON.stringify({ checked: report.checked.length, problems: report.problems }, null, 1));
} else if (report.problems.length) {
  console.error(`FAIL: article voice — ${report.problems.length} problem(s) across ${report.checked.length} checks `
    + `(skills/claude_humanizer.md §3.9 long-form):`);
  for (const problem of report.problems) console.error(`  - ${problem}`);
} else {
  console.log(`article voice: OK — ${report.checked.length} check(s) read as an observer comment`);
}

process.exit(report.problems.length ? 1 : 0);
