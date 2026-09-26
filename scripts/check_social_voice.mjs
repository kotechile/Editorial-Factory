#!/usr/bin/env node
/**
 * scripts/check_social_voice.mjs — verify.sh §9.
 *
 * The LinkedIn variant and the Reddit cards must read as one person commenting on the news, not as
 * the owner of the truth and not as the reader's advisor (skills/claude_humanizer.md §3.8). This
 * checks the two things that actually reach a platform:
 *
 *   1. the authored `<!-- linkedin -->` block in every artifact dated >= VOICE_ENFORCED_FROM
 *      (drafts and published copies — newer artifacts are grandfathered, their voice predates the
 *       rule), and
 *   2. the copy `site/distribution.mjs` generates for every published article: the Reddit variants
 *      the operator pastes and the LinkedIn text that ships.
 *
 * Usage:
 *   node scripts/check_social_voice.mjs              # gate (exit 1 on any violation)
 *   node scripts/check_social_voice.mjs --self-test  # prove the rules bite (embedded fixtures)
 *   node scripts/check_social_voice.mjs --json       # machine-readable
 *
 * What it cannot do: judge whether the point of view is any good. It enforces the mechanical floor
 * (an observer cue present, the authority constructions gone) so the taste question is never
 * decided by omission.
 */
import { readFile, readdir } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  VOICE_ENFORCED_FROM, inspectSocialVoice, describeViolations, inspectLongform, INTERPRETING_SECTIONS,
} from '../site/social_voice.mjs';
import { parseArticleMarkdown, buildTasksForArticle } from '../site/distribution.mjs';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const READER_BASE = (process.env.PRESSFLOW_READER_BASE_URL
  || 'https://pressflow.aichieve.net/published').replace(/\/$/, '');

/** The authored block: between the `<!-- linkedin -->` marker and the next marker or `## ` heading. */
export function extractLinkedInBlock(markdown) {
  const parts = String(markdown).split(/<!--\s*linkedin\s*-->/i);
  if (parts.length < 2) return '';
  return parts[1]
    .split(/<!--\s*(?:schema|internal-links)\s*-->/i)[0]
    .split(/^##\s/m)[0]
    .trim();
}

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

async function checkAuthored(report) {
  for (const file of await artifacts()) {
    const block = extractLinkedInBlock(file.text);
    if (!block) {
      report.problems.push(`${file.dir}/${file.name}: no <!-- linkedin --> block to check`);
      continue;
    }
    const inspection = inspectSocialVoice(block);
    if (!inspection.ok) report.problems.push(...describeViolations(`${file.dir}/${file.name}`, inspection));
    report.checked.push(`${file.dir}/${file.name}`);
  }
}

async function checkArticles(report) {
  for (const file of await artifacts()) {
    // The `<!-- linkedin -->` block is checked on its own; the long-form body is the rest.
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

async function checkGenerated(report) {
  const pubDir = join(ROOT, 'published');
  if (!existsSync(pubDir)) return;
  for (const name of (await readdir(pubDir)).sort()) {
    if (!name.endsWith('.md')) continue;
    const markdown = await readFile(join(pubDir, name), 'utf8');
    const article = parseArticleMarkdown(markdown);
    const tasks = buildTasksForArticle(article, { readerUrl: `${READER_BASE}/${name}` });
    for (const task of tasks) {
      const inspection = inspectSocialVoice(task.post_content);
      if (!inspection.ok) {
        report.problems.push(...describeViolations(`generated ${task.id}`, inspection));
      }
      report.checked.push(`generated ${task.id}`);
    }
  }
}

/** Embedded fixtures — the authority-voice sample is the sentence that shipped before this gate. */
const SELF_TEST = [
  {
    name: 'authority voice (the pre-§3.8 tariff post)',
    text: "The signal is clear: CFOs are pricing in a tariff cliff. A two-month pause is not a fix. "
      + "Here is the playbook for supply chain leaders:\n- Stress test your landed costs if suspended "
      + "tariffs return.\nTreat Jan. 10 as a live deadline. Not a December problem.",
    expectOk: false,
    expectLabels: ['verdict framing', 'consultant framing', 'imperative advice'],
  },
  {
    name: 'advisor framing without a banned phrase (no observer cue)',
    text: 'Three vendors changed prices five times this summer. Each price drop creates a new work '
      + 'ticket for the tech team. The lesson for anyone running these systems is to budget for churn.',
    expectOk: false,
    expectLabels: ['verdict framing'],
  },
  {
    name: 'observer voice',
    text: "I've been following the tariff truce news all week, and one number from the Atlanta Fed "
      + 'stopped me. My read: that is firms saying out loud that they expect the paused tariffs to come '
      + "back. I'm curious how ops teams are reading Jan. 10.",
    expectOk: true,
    expectLabels: [],
  },
];

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
  for (const fixture of SELF_TEST) {
    const result = inspectSocialVoice(fixture.text);
    if (result.ok !== fixture.expectOk) {
      failures.push(`${fixture.name}: expected ok=${fixture.expectOk}, got ${result.ok} `
        + `(cue="${result.cue}", violations=${result.violations.map((v) => v.label).join('|') || 'none'})`);
      continue;
    }
    for (const label of fixture.expectLabels) {
      if (!result.violations.some((v) => v.label === label)) {
        failures.push(`${fixture.name}: expected a "${label}" violation, got `
          + `[${result.violations.map((v) => v.label).join(', ')}]`);
      }
    }
    console.log(`${result.ok ? '✓' : '✓'} social: ${fixture.name} — ${result.ok ? 'passes' : `${result.violations.length} violation(s)`}`);
  }

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
  console.log(`\nsocial-voice rules bite as specified `
    + `(${INTERPRETING_SECTIONS.length} interpreting sections must each carry an observer cue).`);
  return 0;
}

const report = { problems: [], checked: [] };

if (process.argv.includes('--self-test')) {
  process.exit(selfTest());
}

const phaseIndex = process.argv.indexOf('--phase');
const phase = phaseIndex > -1 ? process.argv[phaseIndex + 1] : '';

if (phase === 'generated') {
  await checkGenerated(report);
} else if (phase === 'authored') {
  await checkAuthored(report);
} else if (phase === 'articles') {
  await checkArticles(report);
} else {
  await checkAuthored(report);
  await checkArticles(report);
  await checkGenerated(report);
}

if (process.argv.includes('--json')) {
  console.log(JSON.stringify({ checked: report.checked.length, problems: report.problems }, null, 1));
} else if (report.problems.length) {
  console.error(`FAIL: social voice — ${report.problems.length} problem(s) across ${report.checked.length} checks `
    + `(skills/claude_humanizer.md §3.8 social / §3.9 long-form):`);
  for (const problem of report.problems) console.error(`  - ${problem}`);
} else {
  console.log(`social voice: OK — ${report.checked.length} check(s) read as an observer comment`);
}

process.exit(report.problems.length ? 1 : 0);
