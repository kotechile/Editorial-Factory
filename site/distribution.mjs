/**
 * Deterministic multi-platform distribution formatter.
 *
 * Turns a finished article into copy-ready distribution tasks for Reddit and LinkedIn.
 * No platform API is used anywhere: Reddit is handled with a submit web-intent URL (the
 * operator pastes the text and clicks Post) and LinkedIn by copy-paste, which is exactly
 * the constraint we are working under.
 *
 * Ported and adapted from the deleted software-factory engine
 * (`src/lib/calc/content-distributor/engine.ts`, commit 791d6cd), retargeted at this repo's
 * draft/published markdown (frontmatter + `<!-- section -->` markers).
 *
 * Voice: the framing lines this module owns come from `social_voice.mjs` (observer commenting on
 * the news — skills/claude_humanizer.md §3.8), and `scripts/check_social_voice.mjs` gates the
 * generated copy plus the authored `<!-- linkedin -->` block it carries.
 */
import { OBSERVER_FRAMING, isQuoteable } from './social_voice.mjs';

export const STATUSES = ['ready', 'published', 'deleted'];
export const PLATFORMS = ['reddit', 'linkedin'];

export const REDDIT_TITLE_LIMIT = 300;
export const LINKEDIN_LIMIT = 3000;

const SUBREDDITS = {
  agentic_ai: ['AI_Agents', 'LocalLLaMA'],
  enterprise_tech_leadership: ['ExperiencedDevs', 'technology'],
  gpu_hardware: ['hardware', 'LocalLLaMA'],
  supply_chain: ['supplychain', 'logistics'],
  home_systems_reno: ['HomeImprovement', 'heatpumps'],
  home_infrastructure_lifecycle_tco: ['HomeImprovement', 'energy'],
  workstation_compute_economics: ['buildapc', 'LocalLLaMA'],
  enterprise_build_vs_buy: ['ExperiencedDevs', 'devops'],
  expat_cross_border_relocation: ['expats', 'tax'],
  career_velocity_equity_engineering: ['cscareerquestions', 'financialindependence'],
  personal_microeconomics_tinkering_tax: ['selfhosted', 'homelab'],
  default: ['technology'],
};

const BANNED_AI_TELLS = [
  "in today's fast-paced",
  'in an era of',
  "it's no secret that",
  "it's important to remember",
  'furthermore',
  'moreover',
  'delve into',
  "let's explore",
  'in conclusion',
  'game-changing',
  'cutting-edge',
  'revolutionary',
];

export function cleanRawContent(text) {
  const lines = String(text || '')
    .replace(/<!--[\s\S]*?-->/g, ' ')
    .replace(/^---[\s\S]*?---/, ' ')
    .split(/\r?\n/);
  const kept = [];
  for (const raw of lines) {
    const line = raw
      .replace(/^#{1,6}\s*/, '')
      .replace(/^\s*[-•*]\s*/, '')
      .replace(/\*\*([^*]+)\*\*/g, '$1')
      .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')
      .replace(/[*_`>]/g, '')
      .replace(/\|/g, ' ')
      .replace(/[ \t]{2,}/g, ' ')
      .trim();
    if (!line) { kept.push(''); continue; }
    // Drop heading/label lines: short, unpunctuated and numberless ("The hidden costs",
    // "Why it matters:") — they otherwise glue onto the next sentence when flattened.
    if (line.length < 64 && !/[.!?]["']?$/.test(line) && !/\d/.test(line)) continue;
    kept.push(line);
  }
  return kept.join('\n').replace(/\n{3,}/g, '\n\n').replace(/ {2,}/g, ' ').trim();
}

/** Frontmatter + section markers -> a structured article. */
export function parseArticleMarkdown(markdown) {
  const fm = {};
  const fmMatch = String(markdown).match(/^---\s*[\r\n]+([\s\S]*?)[\r\n]+---/);
  if (fmMatch) {
    for (const line of fmMatch[1].split(/\r?\n/)) {
      const m = line.match(/^([A-Za-z0-9_-]+)\s*:\s*(.*)$/);
      if (!m) continue;
      let v = m[2].trim();
      if (v.startsWith('"') && v.endsWith('"')) v = v.slice(1, -1);
      else if (v.startsWith('[') && v.endsWith(']')) {
        v = v.slice(1, -1).split(',').map((s) => s.trim().replace(/^["']|["']$/g, '')).filter(Boolean);
      }
      fm[m[1]] = v;
    }
  }

  const title =
    fm.title ||
    (String(markdown).match(/^#\s+(.+)$/m) || [])[1] ||
    (String(markdown).match(/^##\s+(.+)$/m) || [])[1] ||
    'Untitled';

  const section = (marker) => {
    const re = new RegExp(`<!--\\s*${marker}\\s*-->([\\s\\S]*?)(?=<!--|$)`, 'i');
    const m = String(markdown).match(re);
    return m ? cleanRawContent(m[1]) : '';
  };

  const linkedinBlock = (() => {
    const parts = String(markdown).split(/<!--\s*linkedin\s*-->/i);
    return parts.length > 1 ? parts[1].split(/^##\s/m)[0].trim() : '';
  })();

  return {
    title: String(title).replace(/^["']|["']$/g, ''),
    slug: String(fm.slug || '').replace(/^\d{4}-\d{2}-\d{2}_/, ''),
    vertical: fm.vertical || 'default',
    persona: fm.persona || fm.target_persona || '',
    date: fm.date || '',
    primaryKeyword: fm.primary_keyword || '',
    secondaryKeywords: Array.isArray(fm.secondary_keywords) ? fm.secondary_keywords : [],
    lead: section('lead'),
    tension: section('tension'),
    tactical: section('tactical-insight'),
    takeaway: section('nuanced-takeaway'),
    tldr: section('tldr'),
    linkedinPost: buildLinkedInFromBlock(linkedinBlock),
    sources: (String(markdown).match(/^##\s*Sources[\s\S]*$/m) || [''])[0],
  };
}

/** The `<!-- linkedin -->` block is authored by the drafter; strip its URL-append artefacts and any
 *  pipeline marker that leaked in behind it — a leaked `<!-- schema -->` reached live LinkedIn
 *  cards, which is internal metadata, not post copy. */
function buildLinkedInFromBlock(block) {
  return String(block || '')
    .split(/<!--\s*schema\s*-->|<!--\s*internal-links\s*-->/i)[0]
    .replace(/<!--[\s\S]*?-->/g, '')
    .split(/\n{3,}/)
    .join('\n\n')
    .replace(/^\s*📖\s*Read the full[\s\S]*$/m, '')
    .replace(/^\s*🛠️\s*Try the[\s\S]*$/m, '')
    .trim();
}

/**
 * Abbreviations and dates that end in a period but do not end a sentence. Without this guard a
 * naive `(?<=[.!?])\s+` split cuts "…truce to Jan. 10, 2027" into "…truce to Jan." + "10, 2027",
 * which then drops the date from the bullet and leaves a fragment ("- 10 as a hard deadline").
 */
const SENTENCE_ABBREVIATION =
  /(?:^|\s)(?:jan|feb|mar|apr|jun|jul|aug|sept?|oct|nov|dec|mon|tue|wed|thu|fri|sat|sun|u\.s|u\.k|u\.n|e\.u|inc|ltd|co|corp|plc|vs|etc|approx|est|no|fig|dept|gov|sen|rep|sec|dr|mr|mrs|ms|st|jr|sr|[a-z])\.$/i;

/** Split prose into sentences without cutting inside dates, abbreviations or initials. */
export function splitSentences(text) {
  const out = [];
  for (const raw of String(text || '').split(/(?<=[.!?])\s+/)) {
    const chunk = raw.trim();
    if (!chunk) continue;
    const prev = out.length ? out[out.length - 1] : '';
    const continues = SENTENCE_ABBREVIATION.test(prev) || /\d\.$/.test(prev) || /^[a-z]/.test(chunk);
    if (prev && continues) out[out.length - 1] = `${prev} ${chunk}`;
    else out.push(chunk);
  }
  return out;
}

export function extractKeySentences(text, maxPoints = 3) {
  const clean = cleanRawContent(text);
  const sentences = splitSentences(clean)
    .map((s) => s.trim())
    .filter((s) => s.length > 35 && s.length < 320);
  const scored = sentences
    .map((sentence) => ({
      sentence,
      score:
        (/\d/.test(sentence) ? 3 : 0) +
        (/\$|%|\b(billion|million|percent)\b/i.test(sentence) ? 2 : 0) +
        (/\b(fell|rose|jumped|dropped|doubled|tripled|capped|deadline|required)\b/i.test(sentence) ? 1 : 0) +
        (/^(the|a|an|if|when|because|but)\b/i.test(sentence) ? 1 : 0),
      index: sentences.indexOf(sentence),
    }))
    .sort((a, b) => b.score - a.score || a.index - b.index);
  return scored.slice(0, maxPoints).map((s) => s.sentence.replace(/\s+—\s+/g, ' — '));
}

/**
 * Social copy quotes the article's prose, so a sentence addressed to the reader as advice ("You must
 * re-run every project plan", "The lesson for anyone…") cannot be pasted into an observer-voice post
 * — the card would read as the reader's advisor no matter what framing surrounds it. Drop those and
 * keep the observation-shaped sentences; when nothing survives, the caller falls back.
 */
export function socialQuoteableSentences(text, maxPoints = 3) {
  return extractKeySentences(text, Math.max(maxPoints * 3, maxPoints))
    .filter(isQuoteable)
    .slice(0, maxPoints);
}

export function extractHashtags(article, max = 4) {
  const words = [
    ...(article.secondaryKeywords || []),
    article.primaryKeyword,
  ]
    .filter(Boolean)
    .map((k) => String(k).split(/\s+/).slice(0, 3).join(''))
    .map((k) => k.replace(/[^A-Za-z0-9]/g, ''))
    .filter((k) => k.length > 2)
    .map((k) => `#${k.charAt(0).toUpperCase()}${k.slice(1)}`);
  const uniq = [...new Set(words)];
  if (uniq.length >= max) return uniq.slice(0, max);
  const fallback = { agentic_ai: '#AIAgents', gpu_hardware: '#GPUs', supply_chain: '#SupplyChain', home_systems_reno: '#HeatPumps', enterprise_tech_leadership: '#TechLeadership' };
  if (fallback[article.vertical] && !uniq.includes(fallback[article.vertical])) uniq.push(fallback[article.vertical]);
  return uniq.slice(0, max);
}

export function getRecommendedSubreddits(article) {
  return SUBREDDITS[article.vertical] || SUBREDDITS.default;
}

export function buildRedditSubmitUrl(subreddit, title, text) {
  const params = new URLSearchParams({ title: String(title || '').slice(0, REDDIT_TITLE_LIMIT), text: String(text || '') });
  return `https://www.reddit.com/r/${subreddit}/submit?${params.toString()}`;
}

function trimToLimit(text, limit) {
  const s = String(text || '').trim();
  if (s.length <= limit) return s;
  const cut = s.slice(0, limit);
  const lastStop = Math.max(cut.lastIndexOf('. '), cut.lastIndexOf('\n'));
  return (lastStop > limit * 0.6 ? cut.slice(0, lastStop + 1) : cut).trim();
}

function ensureNoAiTells(text) {
  let out = String(text || '');
  for (const phrase of BANNED_AI_TELLS) {
    out = out.replace(new RegExp(phrase.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi'), '');
  }
  return out.replace(/ {2,}/g, ' ').trim();
}

/** r/<sub> variant 1 — the numbers first, framed as what the writer pulled out and read. */
export function buildRedditBreakdownVariant(article, readerUrl) {
  const leadHead = String(article.lead || '').slice(0, 60);
  const takeawayText = String(article.takeaway || '').trim();
  const points = socialQuoteableSentences([article.tactical, article.takeaway].join(' '), 8)
    // never repeat the lede as a bullet — it is already the opening paragraph
    .filter((p) => !leadHead || !p.startsWith(leadHead.slice(0, 40)))
    // the read is printed verbatim below, so its sentences must not also appear as bullets
    .filter((p) => !takeawayText.includes(p.replace(/^[-*\s]+/, '').trim()))
    .slice(0, 4);
  const read = isQuoteable(takeawayText) ? takeawayText : (socialQuoteableSentences(article.takeaway, 1)[0] || '');
  const fallback = socialQuoteableSentences(article.tension, 1)[0] || '';
  const bullets = points.map((p) => `- ${p}`).join('\n');
  const body = [
    article.lead,
    '',
    OBSERVER_FRAMING.redditNumbers,
    '',
    bullets || (fallback ? `- ${fallback}` : ''),
    '',
    read ? `${OBSERVER_FRAMING.redditRead} ${read}` : '',
    readerUrl ? `\nFull write-up with the sources: ${readerUrl}` : '',
  ].filter((line) => line).join('\n');
  return ensureNoAiTells(body);
}

/** r/<sub> variant 2 — the writer's provisional read, then an invitation to compare notes. */
export function buildRedditDiscussionVariant(article, readerUrl) {
  const leadHead = String(article.lead || '').slice(0, 40);
  const points = socialQuoteableSentences([article.tactical, article.tension].join(' '), 12)
    .filter((p) => !leadHead || !p.startsWith(leadHead))
    .slice(0, 3);
  const fallback = socialQuoteableSentences(article.tension, 1)[0] || '';
  const body = [
    article.lead,
    '',
    OBSERVER_FRAMING.redditDiscussion,
    '',
    ...(points.length ? points.map((p) => `- ${p}`) : (fallback ? [`- ${fallback}`] : [])),
    '',
    OBSERVER_FRAMING.redditAsk,
    readerUrl ? `\nBackground and primary sources: ${readerUrl}` : '',
  ].filter((line) => line).join('\n');
  return ensureNoAiTells(body);
}

/** r/<sub> variant 3 — "here is what I found" framing. */
export function buildRedditShowAndTellVariant(article, readerUrl) {
  const tldr = socialQuoteableSentences(article.takeaway, 3).map((p) => `- ${p}`).join('\n');
  const body = [
    article.lead,
    '',
    OBSERVER_FRAMING.showAndTell,
    tldr,
    '',
    socialQuoteableSentences(article.tactical, 2).map((p) => `- ${p}`).join('\n'),
    readerUrl ? `\nI wrote up the full breakdown with the primary sources here: ${readerUrl}` : '',
  ].filter((line) => line).join('\n');
  return ensureNoAiTells(body);
}

function redditTitle(article) {
  const base = article.title || article.lead || 'Untitled';
  return trimToLimit(base.replace(/^["']|["']$/g, ''), REDDIT_TITLE_LIMIT);
}

function linkedInText(article, readerUrl) {
  let text = article.linkedinPost;
  if (!text) {
    // Fallback when no authored block exists: still an observation, never a lecture, and never
    // article prose that addresses the reader as advice.
    const read = socialQuoteableSentences([article.tactical, article.takeaway].join(' '), 3)
      .map((p) => `- ${p}`).join('\n');
    text = [article.lead, '', OBSERVER_FRAMING.linkedinFallback, read].filter((line) => line).join('\n');
  }
  const tags = extractHashtags(article);
  if (readerUrl && !text.includes(readerUrl)) {
    text += `\n\n📖 Read the full illustrated breakdown: ${readerUrl}`;
  }
  if (tags.length) text += `\n\n${tags.join(' ')}`;
  return trimToLimit(text, LINKEDIN_LIMIT);
}

/**
 * Build the distribution tasks for one article: one Reddit task per recommended subreddit
 * (variant 1 for the primary subreddit, variant 2 for the second) plus one LinkedIn task.
 *
 * Ids are stable (`<platform>:<slug>[:<sub>]`) so re-seeding is idempotent and never resets
 * a status the operator already set.
 */
export function buildTasksForArticle(article, { readerUrl = '', sourceId = '', sourceType = 'article' } = {}) {
  const slug = article.slug || (article.title || '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  const subreddits = getRecommendedSubreddits(article);
  const tasks = [];

  subreddits.slice(0, 2).forEach((subreddit, index) => {
    const variant = index === 0 ? 'math_breakdown' : 'discussion_question';
    const body = index === 0
      ? buildRedditBreakdownVariant(article, readerUrl)
      : buildRedditDiscussionVariant(article, readerUrl);
    const title = redditTitle(article);
    tasks.push({
      id: `reddit:${slug}:${subreddit.toLowerCase()}`,
      platform: 'reddit',
      channel: `r/${subreddit}`,
      variant,
      source_type: sourceType,
      source_id: sourceId || slug,
      source_title: article.title,
      vertical: article.vertical,
      post_title: title,
      post_content: body,
      submit_url: buildRedditSubmitUrl(subreddit, title, body),
      status: 'ready',
    });
  });

  tasks.push({
    id: `linkedin:${slug}`,
    platform: 'linkedin',
    channel: 'LinkedIn feed',
    variant: 'authored',
    source_type: sourceType,
    source_id: sourceId || slug,
    source_title: article.title,
    vertical: article.vertical,
    post_title: article.title,
    post_content: linkedInText(article, readerUrl),
    submit_url: 'https://www.linkedin.com/feed/?shareActive=true',
    status: 'ready',
  });

  return tasks;
}
