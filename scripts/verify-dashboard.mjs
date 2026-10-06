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
  await page.waitForTimeout(4000); // let boot() finish (it opens the newest article and re-tabs)
  check((await page.title()).includes('PressFlow'), 'dashboard loads', await page.title());

  // The README/verify.sh removal of the LinkedIn/Reddit channel is what this pins: no
  // Distribution tab, no distribution API, and the remaining channel-copy cards still render.
  // The API check goes through the browser context's request API (not `fetch` inside the page):
  // a 404 logged by the page would trip the "no console errors" check below.
  check(await page.locator('[data-tab="tab-distribution"]').count() === 0, 'no Distribution tab');
  const distApi = (await page.request.get(`${BASE}/api/distribution/tasks`)).status();
  check(distApi === 404, 'distribution API is gone', `HTTP ${distApi}`);
  await page.click('[data-tab="tab-suite"]');
  await page.waitForTimeout(1500);
  check(await page.locator('#twitterPreviewBox').count() === 1
    && await page.locator('#newsletterPreviewBox').count() === 1, 'channel copy renders (X + newsletter)');
  check(await page.locator('#linkedInPreviewBox').count() === 0, 'no LinkedIn card in the suite');

  // Reader-facing synthesis surface: the flag + anchors in the public manifest, the badge on the
  // article page. A synthesis article that ships unmarked is exactly what verify.sh §8 prevents in
  // the repo, so this asserts the flag survives the deploy that publishes it.
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
