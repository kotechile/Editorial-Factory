#!/usr/bin/env node
/**
 * Dashboard smoke test — drives the real PressFlow UI in a headless browser.
 *
 * Why this exists: `site/index.html` is one large inline script. A single duplicate identifier
 * (e.g. a second `const escapeHtml`) is a parse-time SyntaxError that kills every handler on the
 * page while the server still returns 200 and `curl` shows a perfectly fine HTML document. Only a
 * browser run catches that class of breakage.
 *
 * Usage:
 *   PRESSFLOW_AUTH_SECRET=$(cat /root/.pressflow_auth_secret) \
 *     node scripts/verify-dashboard.mjs [base-url]        # default http://127.0.0.1:3999
 *
 * Playwright is not a dependency of this repo; point PLAYWRIGHT_PATH at an install that has it
 * (the sibling software-factory-core repo ships one):
 *   PLAYWRIGHT_PATH=/root/software-factory-core/node_modules/playwright
 *
 * Exits non-zero on: console/page errors, a missing tab, or a failed surface assertion.
 */
import { createRequire } from 'node:module';
import { readFileSync } from 'node:fs';

const require = createRequire(import.meta.url);
const PLAYWRIGHT_PATH = process.env.PLAYWRIGHT_PATH || '/root/software-factory-core/node_modules/playwright';
const { chromium } = require(PLAYWRIGHT_PATH);

const BASE = process.argv[2] || process.env.PRESSFLOW_BASE_URL || 'http://127.0.0.1:3999';
const SECRET = process.env.PRESSFLOW_AUTH_SECRET
  || (() => { try { return readFileSync('/root/.pressflow_auth_secret', 'utf8').trim(); } catch { return ''; } })();
if (!SECRET) {
  console.error('Set PRESSFLOW_AUTH_SECRET (or keep the secret in /root/.pressflow_auth_secret).');
  process.exit(2);
}

const host = new URL(BASE).hostname;
const failures = [];
const check = (ok, label, detail = '') => {
  console.log(`${ok ? '✓' : '✗'} ${label}${detail ? ` — ${detail}` : ''}`);
  if (!ok) failures.push(label);
};

const browser = await chromium.launch();
const ctx = await browser.newContext();
await ctx.addCookies([{ name: 'pressflow_auth', value: SECRET, domain: host, path: '/' }]);
const page = await ctx.newPage();
const errors = [];
page.on('pageerror', (e) => errors.push(`pageerror: ${e.message}`));
page.on('console', (m) => { if (m.type() === 'error') errors.push(`console: ${m.text()}`); });

try {
  await page.goto(`${BASE}/`, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(4000); // let boot() finish
  check((await page.title()).includes('PressFlow'), 'dashboard loads', await page.title());

  // The dashboard no longer shows articles: they are pushed to the CMS and read on the fronts, so
  // an article surfaced here would be a second copy with no destination. This asserts the removal
  // survived — the workspace, the library, the multi-channel suite and the article editor are gone.
  check(await page.locator('[data-tab="tab-workspace"]').count() === 0, 'no article workspace tab');
  check(await page.locator('[data-tab="tab-suite"]').count() === 0, 'no multi-channel article suite tab');
  check(await page.locator('#libraryModalBackdrop').count() === 0, 'no article library modal');
  check(await page.locator('#markdownEditor').count() === 0, 'no article markdown editor');
  check(await page.getByRole('button', { name: /Library/ }).count() === 0, 'no library button in the header');

  // Verticals is the home tab and owns the Supabase sync, so it must render registry rows and the
  // sync status on a cold load, without a click.
  check(await page.locator('#tab-verticals.active').count() === 1, 'verticals is the default tab');
  const verticalCards = await page.locator('#verticalsGrid .clean-white-card').count();
  check(verticalCards >= 10, 'vertical registry renders', `${verticalCards} cards`);
  check(await page.locator('#verticalSyncStatus .tag-quiet').count() >= 3, 'verticals tab reports its Supabase sync status');
  const verticalsApi = (await page.request.get(`${BASE}/api/verticals`)).status();
  check(verticalsApi === 200, 'verticals API responds 200', `HTTP ${verticalsApi}`);

  // App Promotion to-do queue is present for software factory apps only.
  check(await page.locator('[data-tab="tab-distribution"]').count() === 1, 'App Promotion to-do tab present');
  const distApi = (await page.request.get(`${BASE}/api/distribution/tasks`)).status();
  check(distApi === 200, 'distribution API responds 200', `HTTP ${distApi}`);

  // Approvals: one row per decision, and the app inventory with a retire reply. The rows come from
  // the factory repo (or the committed fallback), so a 200 with zero rows would mean the parse or
  // the fallback is broken — fail on that rather than render an empty tab.
  const approvalsApi = await page.request.get(`${BASE}/api/approvals`);
  check(approvalsApi.status() === 200, 'approvals API responds 200', `HTTP ${approvalsApi.status()}`);
  const approvals = await approvalsApi.json();
  check(Array.isArray(approvals.items) && approvals.items.length > 0, 'decision queue has rows', `${(approvals.items || []).length} item(s)`);
  check(Array.isArray(approvals.apps) && approvals.apps.length >= 4, 'app inventory is parsed from the factory registry', `${(approvals.apps || []).length} app(s)`);
  await page.click('[data-tab="tab-approvals"]');
  await page.waitForTimeout(2000);
  check(await page.locator('#tab-approvals .pf-decision').count() >= 2, 'approval rows render');
  check(await page.locator('#tab-approvals [data-reply]').count() >= 1, 'each ask carries a copyable reply');
  check(await page.locator('#approvalsWaitingGroup .pf-group-title').count() === 1, 'waiting group renders');
  check(await page.locator('#approvalsInventoryGroup .pf-decision').count() >= 4, 'app inventory renders with per-app retire replies');

  // What's next: the calendar must name the next article run and the next app-harvest sweep.
  const calendarApi = await page.request.get(`${BASE}/api/calendar?days=7`);
  check(calendarApi.status() === 200, 'calendar API responds 200', `HTTP ${calendarApi.status()}`);
  const calendar = await calendarApi.json();
  check(Array.isArray(calendar.by_day) && calendar.by_day.length > 0, 'calendar has article runs', `${calendar.total_runs || 0} run(s)`);
  check(Boolean(calendar.next_run && calendar.next_run.label), 'calendar names the next article vertical',
    calendar.next_run ? `${calendar.next_run.label} (${calendar.next_run.mode})` : 'none');
  check(Boolean(calendar.harvest && calendar.harvest.sweeps && calendar.harvest.sweeps.length > 0
    && calendar.harvest.sweeps[0].verticals.length > 0), 'calendar names the next app-harvest verticals');
  await page.click('[data-tab="tab-calendar"]');
  await page.waitForTimeout(2000);
  check(await page.locator('#calendarDays .pf-day').count() >= 1, 'calendar day groups render');
  check(await page.locator('#calendarHarvest .pf-day').count() >= 1, 'harvest sweeps render');
  check(await page.locator('#calendarHero .pf-hero-card').count() === 2, 'the two "next up" cards render');

  // Every remaining tab must open without a page error (one duplicate identifier in the inline
  // script kills every handler on the page while the server still answers 200).
  for (const tab of ['tab-seo', 'tab-personas', 'tab-fleet', 'tab-distribution', 'tab-verticals']) {
    await page.click(`[data-tab="${tab}"]`);
    await page.waitForTimeout(700);
    check(await page.locator(`#${tab}.active`).count() === 1, `${tab} opens`);
  }

  // The article manifest is still served to the pipeline (auth-gated, never rendered in the UI):
  // the synthesis flag and its anchors are what verify.sh §8 protects in the repo, so this asserts
  // the flag survives the deploy that publishes it.
  const manifest = await page.evaluate(async () => (await (await fetch('/api/articles.json')).json()));
  const flagged = manifest.filter((a) => a.synthesis === true);
  check(manifest.length > 0 && manifest.every((a) => typeof a.synthesis === 'boolean' && Array.isArray(a.sources)),
    'articles.json reports synthesis + sources', `${manifest.length} article(s)`);
  check(manifest.every((a) => a.sourceCount === a.sources.length && a.sourceCount > 0),
    'every article reports its source count', `min=${Math.min(...manifest.map((a) => a.sourceCount))}`);
  check(flagged.length > 0 && flagged.every((a) => a.sourceCount >= 2),
    'the synthesis flag implies >= 2 anchors', `${flagged.length} flagged: ${flagged.map((a) => a.slug).join(', ')}`);

  if (flagged.length) {
    const reader = await page.context().newPage();
    await reader.goto(`${BASE}/published/${flagged[0].file}`, { waitUntil: 'domcontentloaded' });
    check(await reader.locator('p.synthesis .pill').count() === 1, 'reader page badges the synthesis',
      await reader.locator('p.synthesis').first().textContent().catch(() => ''));
    const bodyText = await reader.locator('body').innerText();
    check(!/Gate report|synthesis: true|^---/.test(bodyText),
      'reader page hides pipeline sections + frontmatter', flagged[0].file);
    check((await reader.title()) === flagged[0].title, 'reader page title is the headline',
      await reader.title());
    await reader.close();
  }
} catch (err) {
  check(false, 'dashboard verification ran', err.message.split('\n')[0]);
} finally {
  check(errors.length === 0, 'no console/page errors', errors.slice(0, 3).join(' | '));
  await browser.close();
}

if (failures.length) {
  console.error(`\n${failures.length} check(s) failed: ${failures.join(', ')}`);
  process.exit(1);
}
console.log('\nAll dashboard checks passed.');
