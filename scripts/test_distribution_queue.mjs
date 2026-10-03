#!/usr/bin/env node
/**
 * Queue-card lifecycle test — a card must not outlive its article.
 *
 * The distribution seed only ever ADDS and REFRESHES cards, so five articles deleted by founder
 * request (2026-10-01) left 12 cards in the queue, each still offering to post a withdrawn article
 * and each still carrying the reader URL it was seeded with (which was the internal dashboard,
 * before PressFlow's article surface was closed). The prune is the fix; these are its rules.
 *
 * Wired into scripts/verify.sh. Pure functions, no server, no network, no credentials.
 *
 * Usage: node scripts/test_distribution_queue.mjs
 */
import { pruneOrphanTasks } from '../site/distribution.mjs';

const failures = [];
const check = (ok, label, detail = '') => {
  console.log(`${ok ? '✓' : '✗'} ${label}${detail ? ` — ${detail}` : ''}`);
  if (!ok) failures.push(label);
};

const card = (over = {}) => ({
  id: 'reddit:example:technology',
  platform: 'reddit',
  source_type: 'article',
  source_id: '2026-09-23_withdrawn-article',
  status: 'ready',
  ...over,
});

const published = new Set(['2026-10-02_live-article', '2026-09-21_older-but-live']);

// 1. a card for a withdrawn article is dropped
{
  const { keep, dropped } = pruneOrphanTasks([card()], published);
  check(dropped.length === 1 && keep.length === 0,
    'a card whose article left published/ is dropped', `kept ${keep.length}`);
}

// 2. a card for a live article is kept
{
  const live = card({ source_id: '2026-10-02_live-article' });
  const { keep, dropped } = pruneOrphanTasks([live], published);
  check(keep.length === 1 && dropped.length === 0,
    'a card for a live article is kept', `dropped ${dropped.length}`);
}

// 3. hand-written / external / sourceless cards are never touched
{
  const manual = [
    card({ source_type: 'link', source_id: 'some-external-thing' }),
    card({ source_type: 'tool', source_id: 'not-a-published-artifact' }),
    card({ source_type: 'article', source_id: '' }),
    { id: 'hand:made', platform: 'linkedin', status: 'ready' },
  ];
  const { keep, dropped } = pruneOrphanTasks(manual, published);
  check(keep.length === 4 && dropped.length === 0,
    'manual, external and sourceless cards are never pruned',
    `kept ${keep.length}, dropped ${dropped.length}`);
}

// 4. a completed card for a withdrawn article is pruned too (the article is gone either way)
{
  const { dropped } = pruneOrphanTasks([card({ status: 'done', completed_at: '2026-10-01T00:00:00Z' })],
    published);
  check(dropped.length === 1, 'a completed card for a withdrawn article is pruned',
    `dropped ${dropped.length}`);
}

// 5. mixed input: only the orphans go, and the rest keep their order and payload
{
  const input = [
    card({ id: 'a', source_id: '2026-09-23_withdrawn-article' }),
    card({ id: 'b', source_id: '2026-10-02_live-article' }),
    card({ id: 'c', source_id: '2026-09-23_another-withdrawn' }),
    card({ id: 'd', source_id: '2026-09-21_older-but-live' }),
  ];
  const { keep, dropped } = pruneOrphanTasks(input, published);
  check(keep.map((t) => t.id).join(',') === 'b,d' && dropped.map((t) => t.id).join(',') === 'a,c',
    'a mixed queue keeps exactly the live cards, in order',
    `kept ${keep.map((t) => t.id)}, dropped ${dropped.map((t) => t.id)}`);
}

if (failures.length) {
  console.error(`\ndistribution queue: ${failures.length} failure(s)`);
  process.exit(1);
}
console.log('\ndistribution queue: ok — a card cannot outlive the article it was seeded from');
