/**
 * Deterministic promotion-task formatter for the PressFlow to-do queue.
 *
 * The queue promotes the software factory's LIVE APPS (catalog: `context/promoted_apps.json`),
 * not articles. Each app produces one card per recommended subreddit plus one LinkedIn card.
 * No platform API is used anywhere: Reddit is handled with a submit web-intent URL (the operator
 * pastes the text and clicks Post) and LinkedIn by copy-paste, which is exactly the constraint we
 * are working under.
 *
 * History: this module used to derive Reddit/LinkedIn cards from published articles, picking the
 * subreddit from a vertical->subreddit map. That pipeline is gone on purpose (the to-do list is a
 * promotion list for the apps, and article cards kept re-seeding over it). What survives is the
 * part that is still true: stable ids, one card per place to post, an explicit subreddit
 * recommendation, and a prune that stops a card outliving its source.
 *
 * Voice: the copy ships verbatim, so it is gated by `scripts/check_social_voice.mjs` against the
 * observer-voice rules in `site/social_voice.mjs` (skills/claude_humanizer.md §3.8) — a card must
 * read as one person describing something they built, not as a brand issuing instructions.
 */

export const STATUSES = ['ready', 'published', 'deleted'];
export const PLATFORMS = ['reddit', 'linkedin'];

export const REDDIT_TITLE_LIMIT = 300;
export const LINKEDIN_LIMIT = 3000;
export const LINKEDIN_SUBMIT_URL = 'https://www.linkedin.com/feed/?shareActive=true';

/**
 * Source types this module can regenerate. A card carrying one of these AND a non-empty
 * `source_id` is prunable when its source is no longer produced — hand-written, external-link and
 * sourceless cards are never touched by a re-seed.
 *
 * `article` stays listed even though nothing generates it any more: the queue still held article
 * cards when the source changed, and a re-seed has to be able to clear them.
 */
export const GENERATED_SOURCE_TYPES = ['app', 'article'];

/** Trim to a platform's hard limit without cutting mid-sentence when a clean stop is close by. */
export function truncate(text, limit) {
  const s = String(text || '').trim();
  if (s.length <= limit) return s;
  const cut = s.slice(0, limit);
  const lastStop = Math.max(cut.lastIndexOf('. '), cut.lastIndexOf('\n'));
  return (lastStop > limit * 0.6 ? cut.slice(0, lastStop + 1) : cut).trim();
}

export function buildRedditSubmitUrl(subreddit, title, text) {
  const params = new URLSearchParams({
    title: String(title || '').slice(0, REDDIT_TITLE_LIMIT),
    text: String(text || ''),
  });
  return `https://www.reddit.com/r/${subreddit}/submit?${params.toString()}`;
}

/** The source ids a catalog of apps can legitimately produce. */
export function appSourceIds(apps = []) {
  return new Set(apps.map((app) => String(app && app.slug || '').trim()).filter(Boolean));
}

/**
 * Build the promotion tasks for one app: one Reddit task per recommended subreddit (each with its
 * own title and framing) plus one LinkedIn task.
 *
 * Ids are stable (`<platform>:<app-slug>[:<sub>]`) so re-seeding is idempotent and never resets a
 * status the operator already set, and so a card can be traced back to its app.
 */
export function buildTasksForApp(app) {
  const slug = String((app && app.slug) || '').trim();
  if (!slug) throw new Error('app slug is required');
  const name = String(app.name || slug);
  const sourceTitle = `${name} — ${app.tagline || ''}`.replace(/ — $/, '').trim();
  const tasks = [];

  for (const card of app.reddit || []) {
    const subreddit = String(card.subreddit || '').replace(/^r\//i, '').trim();
    if (!subreddit) throw new Error(`app ${slug}: a reddit card has no subreddit`);
    const title = truncate(card.title, REDDIT_TITLE_LIMIT);
    const body = String(card.body || '').trim();
    if (!body) throw new Error(`app ${slug}: reddit card r/${subreddit} has empty copy`);
    tasks.push({
      id: `reddit:${slug}:${subreddit.toLowerCase()}`,
      platform: 'reddit',
      channel: `r/${subreddit}`,
      channel_note: String(card.why || ''),
      variant: String(card.variant || 'math_breakdown'),
      source_type: 'app',
      source_id: slug,
      source_title: sourceTitle,
      vertical: String(app.category || ''),
      post_title: title,
      post_content: body,
      submit_url: buildRedditSubmitUrl(subreddit, title, body),
      status: 'ready',
    });
  }

  const linkedin = app.linkedin || {};
  const linkedinBody = String(linkedin.body || '').trim();
  if (!linkedinBody) throw new Error(`app ${slug}: linkedin card has empty copy`);
  const hashtags = (linkedin.hashtags || []).join(' ').trim();
  tasks.push({
    id: `linkedin:${slug}`,
    platform: 'linkedin',
    channel: 'LinkedIn feed',
    channel_note: String(linkedin.why || ''),
    variant: 'authored',
    source_type: 'app',
    source_id: slug,
    source_title: sourceTitle,
    vertical: String(app.category || ''),
    post_title: truncate(linkedin.title || name, REDDIT_TITLE_LIMIT),
    post_content: truncate(hashtags ? `${linkedinBody}\n\n${hashtags}` : linkedinBody, LINKEDIN_LIMIT),
    submit_url: LINKEDIN_SUBMIT_URL,
    status: 'ready',
  });

  return tasks;
}

/** Every task a catalog of apps produces. */
export function buildTasksForApps(apps = []) {
  return apps.flatMap((app) => buildTasksForApp(app));
}

/**
 * Drop queue cards whose source is no longer produced.
 *
 * The seed only ever adds and refreshes, so a card survived its source disappearing — and kept
 * offering to post it, carrying whatever URL it was seeded with. A card is prunable only when it
 * was generated (a known generated `source_type` plus a non-empty `source_id`) and that id is not
 * in the current source set: hand-written, external-link and sourceless cards are left alone.
 *
 * This is also how the queue moved from articles to apps: the article cards were generated rows
 * whose source ids are not app slugs, so the first re-seed after the switch clears them.
 */
export function pruneOrphanTasks(tasks, validSourceIds) {
  const keep = [];
  const dropped = [];
  for (const task of tasks) {
    const generated = task && GENERATED_SOURCE_TYPES.includes(task.source_type) && task.source_id;
    if (generated && !validSourceIds.has(task.source_id)) dropped.push(task);
    else keep.push(task);
  }
  return { keep, dropped };
}
