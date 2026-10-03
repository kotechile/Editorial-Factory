#!/usr/bin/env node
/**
 * Public-surface test — what PressFlow serves to a stranger on the internet.
 *
 * PressFlow is an INTERNAL dashboard. The articles it holds are exported to the reader sites
 * (giniloh.com / wellroost.com), so nothing here may be readable without the shared secret: not the
 * published article pages, not the article manifest, not the drafts. An earlier revision whitelisted
 * `/published/*` and `/api/articles.json` as "the reader surface", which published a second public
 * copy of every article — including the ones still sitting as CMS drafts — on a domain that is not a
 * reader surface at all.
 *
 * Wired into scripts/verify.sh. Hermetic: spawns the real server on a free port with a throwaway
 * secret and an empty env file (PRESSFLOW_ENV_FILE), so it needs no credentials, no Supabase and no
 * network, and writes nothing.
 *
 * Usage: node scripts/test_public_surface.mjs
 */
import { spawn } from 'node:child_process';
import { createServer } from 'node:net';
import { readdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const SECRET = 'test-secret-public-surface';

const failures = [];
const check = (ok, label, detail = '') => {
  console.log(`${ok ? '✓' : '✗'} ${label}${detail ? ` — ${detail}` : ''}`);
  if (!ok) failures.push(label);
};

function freePort() {
  return new Promise((resolve, reject) => {
    const srv = createServer();
    srv.once('error', reject);
    srv.listen(0, '127.0.0.1', () => {
      const { port } = srv.address();
      srv.close(() => resolve(port));
    });
  });
}

async function startServer({ secret }) {
  const port = await freePort();
  const env = { ...process.env, PORT: String(port), PRESSFLOW_ENV_FILE: '/dev/null' };
  if (secret) env.PRESSFLOW_AUTH_SECRET = secret;
  else {
    delete env.PRESSFLOW_AUTH_SECRET;
    delete env.EDITORIAL_SECRET;
  }
  const child = spawn(process.execPath, [join(ROOT, 'site', 'server.mjs')], {
    env, cwd: ROOT, stdio: ['ignore', 'pipe', 'pipe'],
  });
  let stderr = '';
  child.stderr.on('data', (d) => { stderr += d.toString(); });
  const base = `http://127.0.0.1:${port}`;
  for (let i = 0; i < 60; i += 1) {
    try {
      const res = await fetch(`${base}/healthz`);
      if (res.ok) return { child, base, port };
    } catch { /* not listening yet */ }
    await new Promise((r) => setTimeout(r, 150));
  }
  child.kill('SIGKILL');
  throw new Error(`server did not come up on ${base}\n${stderr.slice(0, 400)}`);
}

async function probe(base, path, headers = {}) {
  const res = await fetch(`${base}${path}`, { headers, redirect: 'manual' });
  return { status: res.status, headers: res.headers, body: await res.text() };
}

// A real artifact to try to read, so a passing test cannot be a 404 in disguise.
function sampleArticle() {
  const files = readdirSync(join(ROOT, 'published')).filter((f) => f.endsWith('.md')).sort();
  return files[files.length - 1];
}

let ctx;
try {
  ctx = await startServer({ secret: SECRET });
  const { base, child } = ctx;
  const article = sampleArticle();

  const health = await probe(base, '/healthz');
  check(health.status === 200, 'GET /healthz is public (platform health probe)', `got ${health.status}`);

  const robots = await probe(base, '/robots.txt');
  check(robots.status === 200 && /disallow:\s*\//i.test(robots.body),
    'GET /robots.txt tells crawlers to stay out', `got ${robots.status}`);

  check(/noindex/i.test(health.headers.get('x-robots-tag') || ''),
    'every response carries X-Robots-Tag: noindex', String(health.headers.get('x-robots-tag')));

  const anon = {
    '/': 'the dashboard',
    '/api/articles.json': 'the article manifest',
    [`/published/${article}`]: 'a published article page',
    '/api/drafts': 'unpublished drafts',
    '/api/distribution/tasks': 'the distribution queue',
  };
  for (const [path, what] of Object.entries(anon)) {
    const res = await probe(base, path);
    check(res.status === 401, `${path} requires the secret (${what})`, `got ${res.status}`);
  }

  const authed = await probe(base, '/api/articles.json', { 'x-editorial-key': SECRET });
  check(authed.status === 200, 'the secret still opens the manifest', `got ${authed.status}`);

  const bearer = await probe(base, `/published/${article}`, { Authorization: `Bearer ${SECRET}` });
  check(bearer.status === 200, 'the secret still opens an article page (internal review)',
    `got ${bearer.status}`);

  child.kill('SIGKILL');
  await new Promise((r) => setTimeout(r, 250));

  // Fail closed: with no secret configured, nothing is served — not even the dashboard.
  const closed = await startServer({ secret: '' });
  const closedHealth = await probe(closed.base, '/healthz');
  check(closedHealth.status === 200, 'without a secret, /healthz still answers', `got ${closedHealth.status}`);
  const closedRoot = await probe(closed.base, '/api/articles.json');
  check(closedRoot.status === 503, 'without a secret, the app fails closed (503)', `got ${closedRoot.status}`);
  closed.child.kill('SIGKILL');
} catch (err) {
  check(false, 'the public-surface test ran', err.message);
} finally {
  if (ctx?.child) ctx.child.kill('SIGKILL');
}

if (failures.length) {
  console.error(`\npublic surface: ${failures.length} failure(s)`);
  process.exit(1);
}
console.log('\npublic surface: ok — only /healthz and /robots.txt are reachable without the secret');
