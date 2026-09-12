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
 * Exits non-zero on: console/page errors, missing Distribution tab, wrong card counts, or a
 * failing status round-trip.
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
  await page.waitForTimeout(4000); // let boot() finish (it opens the newest article and re-tabs)
  check((await page.title()).includes('PressFlow'), 'dashboard loads', await page.title());

  await page.click('[data-tab="tab-distribution"]');
  await page.locator('#distGrid').waitFor({ state: 'visible', timeout: 15000 });
  await page.waitForTimeout(1500);

  const empty = await page.locator('#distGrid .clean-white-card').count();
  if (empty === 0) {
    console.log('· queue is empty — running “Generate from published” first');
    await page.click('#distSeedBtn');
    await page.waitForTimeout(6000);
  }

  const cards = await page.locator('#distGrid .clean-white-card').count();
  check(cards > 0, 'distribution cards render', `${cards} card(s)`);
  const badge = await page.textContent('#distStorageBadge');
  check(/Supabase|Local file/.test(badge), 'storage badge reports the backend', badge);

  const api = await page.evaluate(async () => {
    const r = await fetch('/api/distribution/tasks', { credentials: 'same-origin' });
    const d = await r.json();
    return { status: r.status, total: d.total, storage: d.storage, counts: d.counts };
  });
  check(api.status === 200 && api.total > 0, 'queue API responds', `total=${api.total} storage=${api.storage}`);

  // status round-trip through the UI, left clean afterwards
  const first = page.locator('#distGrid .clean-white-card').first();
  await first.locator('button[data-action="deleted"]').click();
  await page.waitForTimeout(2000);
  const afterDelete = await page.evaluate(async () => (await (await fetch('/api/distribution/tasks?status=deleted', { credentials: 'same-origin' })).json()).tasks.length);
  check(afterDelete > 0, 'mark deleted persists', `deleted=${afterDelete}`);
  await page.locator('#distGrid .clean-white-card button[data-action="ready"]').first().click();
  await page.waitForTimeout(2000);
  const afterReopen = await page.evaluate(async () => (await (await fetch('/api/distribution/tasks?status=deleted', { credentials: 'same-origin' })).json()).tasks.length);
  check(afterReopen === 0, 'reopen as ready persists', `deleted=${afterReopen}`);
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
