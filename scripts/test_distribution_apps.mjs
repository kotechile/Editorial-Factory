#!/usr/bin/env node
/**
 * App-promotion card test — the to-do list promotes software apps, and each card names the
 * subreddit it is recommended for.
 *
 * The queue's source is `context/promoted_apps.json`. Two things about it are easy to break
 * silently: a card that stops naming a place to post (the recommendation IS the deliverable), and
 * a copy block that fails the observer-voice contract now that the copy is authored data instead of
 * generated prose. Both are asserted here, plus the platform limits and the link target.
 *
 * Wired into scripts/verify.sh. Pure functions + a file read, no server, no network, no credentials.
 *
 * Usage: node scripts/test_distribution_apps.mjs
 */
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import {
  buildTasksForApp, buildTasksForApps, appSourceIds,
  REDDIT_TITLE_LIMIT, LINKEDIN_LIMIT,
} from '../site/distribution.mjs';
import { inspectSocialVoice } from '../site/social_voice.mjs';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const APPS_FILE = join(ROOT, 'context', 'promoted_apps.json');

const failures = [];
const check = (ok, label, detail = '') => {
  console.log(`${ok ? '✓' : '✗'} ${label}${detail ? ` — ${detail}` : ''}`);
  if (!ok) failures.push(label);
};

const catalog = JSON.parse(readFileSync(APPS_FILE, 'utf8'));
const apps = catalog.apps || [];
const tasks = buildTasksForApps(apps);

check(apps.length >= 1, 'the catalog lists at least one app', `${apps.length} app(s)`);

// Every app is fully described and carries a recommendation.
for (const app of apps) {
  const missing = ['slug', 'name', 'url', 'category', 'tagline'].filter((k) => !String(app[k] || '').trim());
  check(missing.length === 0, `app "${app.slug}" is fully described`, missing.join(', ') || 'ok');
  check(/^https:\/\/apps\.giniloh\.com\//.test(String(app.url || '')),
    `app "${app.slug}" links to its public page`, String(app.url || '(no url)'));
  check(Array.isArray(app.reddit) && app.reddit.length >= 1,
    `app "${app.slug}" recommends at least one subreddit`, `${(app.reddit || []).length} card(s)`);
  for (const card of app.reddit || []) {
    check(Boolean(String(card.subreddit || '').trim()),
      `app "${app.slug}" card names a subreddit`, String(card.subreddit || ''));
    check(Boolean(String(card.why || '').trim()),
      `app "${app.slug}" r/${card.subreddit} explains the recommendation`, String(card.why || '').slice(0, 60));
  }
  check(Boolean(String((app.linkedin || {}).body || '').trim()),
    `app "${app.slug}" has LinkedIn copy`, '');
}

// One LinkedIn card plus one Reddit card per recommendation, ids stable and unique.
check(tasks.length === apps.length + apps.reduce((n, a) => n + (a.reddit || []).length, 0),
  'every app yields one LinkedIn card and one Reddit card per subreddit',
  `${tasks.length} card(s)`);
{
  const ids = tasks.map((t) => t.id);
  check(new Set(ids).size === ids.length, 'card ids are unique', `${ids.length} id(s)`);
  const expected = apps.flatMap((a) => [
    `linkedin:${a.slug}`,
    ...(a.reddit || []).map((c) => `reddit:${a.slug}:${String(c.subreddit).toLowerCase()}`),
  ]);
  check(expected.every((id) => ids.includes(id)), 'ids follow <platform>:<app>[:<sub>]', '');
  check([...appSourceIds(apps)].every((slug) => tasks.some((t) => t.source_id === slug)),
    'every app slug reaches the queue as a source_id', '');
}

// Per-card shape: the recommended channel, a working submit intent, the platform limits, the link.
for (const task of tasks) {
  const app = apps.find((a) => a.slug === task.source_id);
  if (task.platform === 'reddit') {
    check(/^r\/[A-Za-z0-9_]+$/.test(task.channel), `${task.id} names a subreddit channel`, task.channel);
    check(String(task.submit_url).startsWith(`https://www.reddit.com/r/${task.channel.slice(2)}/submit?`),
      `${task.id} has a Reddit submit intent for its channel`, String(task.submit_url).slice(0, 60));
    check(task.post_title.length <= REDDIT_TITLE_LIMIT,
      `${task.id} title is within Reddit's limit`, `${task.post_title.length}/${REDDIT_TITLE_LIMIT}`);
  } else {
    check(task.channel === 'LinkedIn feed', `${task.id} targets the LinkedIn feed`, task.channel);
    check(task.post_content.length <= LINKEDIN_LIMIT,
      `${task.id} copy is within LinkedIn's limit`, `${task.post_content.length}/${LINKEDIN_LIMIT}`);
  }
  const link = String((app || {}).url || '');
  check(link && task.post_content.includes(link),
    `${task.id} carries the public app link`, link || '(none)');
  check(!/pressflow\.|\/published\//.test(task.post_content),
    `${task.id} never points at the internal dashboard`, '');
  const inspection = inspectSocialVoice(task.post_content);
  check(inspection.ok, `${task.id} reads as an observer`, inspection.ok ? inspection.cue : inspection.violations.map((v) => v.label).join('|'));
}

if (failures.length) {
  console.error(`\ndistribution apps: ${failures.length} failure(s)`);
  process.exit(1);
}
console.log(`\ndistribution apps: ok — ${apps.length} app(s), ${tasks.length} card(s), every one names its subreddit`);
