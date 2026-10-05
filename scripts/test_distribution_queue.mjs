#!/usr/bin/env node
/**
 * Queue-card lifecycle test — a card must not outlive its source.
 *
 * The seed only ever ADDS and REFRESHES cards, so a card survived its source disappearing: five
 * articles deleted by founder request (2026-10-01) left 12 cards still offering to post a withdrawn
 * article, and when the queue's source moved from articles to the promoted apps the same defect
 * would have left 54 article cards advertising articles nobody asked to promote. The prune is the
 * fix; these are its rules.
 *
 * Wired into scripts/verify.sh. Pure functions, no server, no network, no credentials.
 *
 * Usage: node scripts/test_distribution_queue.mjs
 */
import { pruneOrphanTasks, GENERATED_SOURCE_TYPES } from '../site/distribution.mjs';

const failures = [];
const check = (ok, label, detail = '') => {
  console.log(`${ok ? '✓' : '✗'} ${label}${detail ? ` — ${detail}` : ''}`);
  if (!ok) failures.push(label);
};

const card = (over = {}) => ({
  id: 'reddit:ledgerlink:stripe',
  platform: 'reddit',
  source_type: 'app',
  source_id: 'ledgerlink',
  status: 'ready',
  ...over,
});

const apps = new Set(['ledgerlink', 'facturgate', 'parcelproof', 'caseproof']);

// 1. a card whose app left the catalog is dropped
{
  const { keep, dropped } = pruneOrphanTasks([card({ source_id: 'retired-app' })], apps);
  check(dropped.length === 1 && keep.length === 0,
    'a card whose app left the catalog is dropped', `kept ${keep.length}`);
}

// 2. a card for a promoted app is kept
{
  const { keep, dropped } = pruneOrphanTasks([card()], apps);
  check(keep.length === 1 && dropped.length === 0,
    'a card for a promoted app is kept', `dropped ${dropped.length}`);
}

// 3. the article cards the old source produced are cleared by the first re-seed
{
  const articles = [
    card({ id: 'reddit:mcp-skills-extension:ai_agents', source_type: 'article', source_id: '2026-09-21_mcp-skills-extension' }),
    card({ id: 'linkedin:mcp-skills-extension', source_type: 'article', source_id: '2026-09-21_mcp-skills-extension' }),
  ];
  const { keep, dropped } = pruneOrphanTasks(articles, apps);
  check(dropped.length === 2 && keep.length === 0,
    'article cards (the queue\'s old source) are pruned', `kept ${keep.length}`);
}

// 4. hand-written / external / sourceless cards are never touched
{
  const manual = [
    card({ source_type: 'link', source_id: 'some-external-thing' }),
    card({ source_type: 'tool', source_id: 'not-a-promoted-app' }),
    card({ source_type: 'app', source_id: '' }),
    { id: 'hand:made', platform: 'linkedin', status: 'ready' },
  ];
  const { keep, dropped } = pruneOrphanTasks(manual, apps);
  check(keep.length === 4 && dropped.length === 0,
    'manual, external and sourceless cards are never pruned',
    `kept ${keep.length}, dropped ${dropped.length}`);
}

// 5. a completed card for a withdrawn source is pruned too (the source is gone either way)
{
  const { dropped } = pruneOrphanTasks([card({ source_id: 'retired-app', status: 'deleted', completed_at: '2026-10-01T00:00:00Z' })],
    apps);
  check(dropped.length === 1, 'a completed card for a withdrawn source is pruned',
    `dropped ${dropped.length}`);
}

// 6. mixed input: only the orphans go, and the rest keep their order and payload
{
  const input = [
    card({ id: 'a', source_id: 'retired-app' }),
    card({ id: 'b', source_id: 'facturgate' }),
    card({ id: 'c', source_type: 'article', source_id: '2026-09-23_an-article' }),
    card({ id: 'd', source_id: 'caseproof' }),
  ];
  const { keep, dropped } = pruneOrphanTasks(input, apps);
  check(keep.map((t) => t.id).join(',') === 'b,d' && dropped.map((t) => t.id).join(',') === 'a,c',
    'a mixed queue keeps exactly the live cards, in order',
    `kept ${keep.map((t) => t.id)}, dropped ${dropped.map((t) => t.id)}`);
}

// 7. the generated-source list still covers what a re-seed must be able to clear
{
  check(GENERATED_SOURCE_TYPES.includes('app') && GENERATED_SOURCE_TYPES.includes('article'),
    'generated source types cover both the current source and the one it replaced',
    GENERATED_SOURCE_TYPES.join(', '));
}

if (failures.length) {
  console.error(`\ndistribution queue: ${failures.length} failure(s)`);
  process.exit(1);
}
console.log('\ndistribution queue: ok — a card cannot outlive the source it was seeded from');
