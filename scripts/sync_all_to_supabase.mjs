#!/usr/bin/env node
import { readFile, readdir } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const ROOT = join(__dirname, '..');

// 1. Load .env
const envFile = join(ROOT, '.env');
if (existsSync(envFile)) {
  const content = await readFile(envFile, 'utf8');
  for (const line of content.split(/\r?\n/)) {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('#') && trimmed.includes('=')) {
      const idx = trimmed.indexOf('=');
      const k = trimmed.slice(0, idx).trim();
      const v = trimmed.slice(idx + 1).trim();
      if (!process.env[k]) process.env[k] = v;
    }
  }
}

const SUPABASE_URL = (process.env.SUPABASE_URL || '').replace(/\/$/, '');
const SUPABASE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY || process.env.SUPABASE_KEY || '';

if (!SUPABASE_URL || !SUPABASE_KEY) {
  console.error('ERROR: SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY not configured.');
  process.exit(1);
}

function parseFrontmatter(markdown) {
  if (!markdown) return {};
  const fmMatch = markdown.match(/^---\s*[\r\n]+([\s\S]*?)[\r\n]+---/);
  if (!fmMatch) return {};
  const data = {};
  const lines = fmMatch[1].split(/\r?\n/);
  for (const line of lines) {
    const m = line.match(/^([a-zA-Z0-9_-]+)\s*:\s*(.*)$/);
    if (!m) continue;
    const key = m[1].trim();
    let rawVal = m[2].trim();
    if (rawVal.startsWith('[') && rawVal.endsWith(']')) {
      try {
        data[key] = JSON.parse(rawVal);
      } catch (e) {
        data[key] = rawVal.slice(1, -1).split(',').map((s) => s.trim().replace(/^["']|["']$/g, '')).filter(Boolean);
      }
    } else if ((rawVal.startsWith('"') && rawVal.endsWith('"')) || (rawVal.startsWith("'") && rawVal.endsWith("'"))) {
      data[key] = rawVal.slice(1, -1);
    } else if (!isNaN(Number(rawVal)) && rawVal !== '') {
      data[key] = Number(rawVal);
    } else if (rawVal.toLowerCase() === 'true') {
      data[key] = true;
    } else if (rawVal.toLowerCase() === 'false') {
      data[key] = false;
    } else {
      data[key] = rawVal;
    }
  }
  return data;
}

async function supabaseFetch(path, options = {}) {
  const headers = {
    'apikey': SUPABASE_KEY,
    'Authorization': `Bearer ${SUPABASE_KEY}`,
    'Content-Type': 'application/json',
    'Prefer': 'return=representation,resolution=merge-duplicates',
    ...(options.headers || {}),
  };

  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 8000);

  try {
    const res = await fetch(`${SUPABASE_URL}/rest/v1/${path}`, {
      ...options,
      headers,
      signal: controller.signal,
    });
    clearTimeout(timeoutId);

    if (!res.ok) {
      const txt = await res.text();
      throw new Error(`Supabase error ${res.status}: ${txt}`);
    }
    const text = await res.text();
    return text ? JSON.parse(text) : null;
  } catch (err) {
    clearTimeout(timeoutId);
    throw err;
  }
}

async function syncArticle(item) {
  const markdown = await readFile(item.path, 'utf8');
  const fm = parseFrontmatter(markdown);
  const titleMatch = markdown.match(/^#\s+(.+)$/m);
  const title = fm.title || (titleMatch ? titleMatch[1].trim() : item.file);

  const baseName = item.file.replace(/\.md$/, '').replace(/_final$/, '').replace(/_draft$/, '');
  const slug = fm.slug || baseName.replace(/^\d{4}-\d{2}-\d{2}_/, '');
  const vertical = fm.vertical || 'general';
  const status = item.type === 'published' ? 'published' : 'draft';

  // Extract linkedin post if present
  let linkedin = '';
  if (markdown.includes('<!-- linkedin -->')) {
    linkedin = markdown.split('<!-- linkedin -->')[1].trim();
  }

  const seoMetadata = {
    primary_keyword: fm.primary_keyword || null,
    secondary_keywords: Array.isArray(fm.secondary_keywords) ? fm.secondary_keywords : [],
    search_volume: fm.search_volume || null,
    search_intent: fm.search_intent || null,
    keyword_difficulty: fm.keyword_difficulty || null,
    meta_title: fm.meta_title || null,
    meta_description: fm.meta_description || null,
  };

  const metadata = {
    slug,
    vertical,
    headline: title,
    status,
    file: item.file,
    targets: item.type === 'published' ? ['published/'] : ['context/drafts/'],
    seo: seoMetadata,
    linkedin_post: linkedin,
  };

  const payload = {
    slug,
    vertical,
    headline: title,
    title,
    body_md: markdown,
    content: markdown,
    status,
    primary_keyword: fm.primary_keyword || null,
    secondary_keywords: Array.isArray(fm.secondary_keywords) ? fm.secondary_keywords : [],
    search_volume: fm.search_volume || null,
    search_intent: fm.search_intent || null,
    meta_title: fm.meta_title || null,
    meta_description: fm.meta_description || null,
    metadata,
  };

  // 1. Check if article exists by slug or metadata->>slug
  const encSlug = encodeURIComponent(slug);
  let existing = null;
  try {
    const rows = await supabaseFetch(`articles?select=id,slug,metadata&or=(slug.eq.${encSlug},metadata->>slug.eq.${encSlug})&limit=1`);
    if (Array.isArray(rows) && rows.length) existing = rows[0];
  } catch (e) {
    try {
      const rows = await supabaseFetch(`articles?select=id,metadata&metadata->>slug=eq.${encSlug}&limit=1`);
      if (Array.isArray(rows) && rows.length) existing = rows[0];
    } catch (e2) {}
  }

  if (existing && existing.id) {
    await supabaseFetch(`articles?id=eq.${encodeURIComponent(existing.id)}`, {
      method: 'PATCH',
      body: JSON.stringify({ ...payload, updated_at: new Date().toISOString() }),
    });
    return { action: 'updated', id: existing.id, slug, title, status };
  } else {
    const inserted = await supabaseFetch('articles', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
    const id = Array.isArray(inserted) && inserted.length ? inserted[0].id : null;
    return { action: 'inserted', id, slug, title, status };
  }
}

async function main() {
  const pubDir = join(ROOT, 'published');
  const draftsDir = join(ROOT, 'context', 'drafts');

  const allItems = [];

  if (existsSync(pubDir)) {
    const pubFiles = (await readdir(pubDir)).filter((f) => f.endsWith('.md'));
    for (const f of pubFiles) {
      allItems.push({ file: f, path: join(pubDir, f), type: 'published' });
    }
  }

  if (existsSync(draftsDir)) {
    const draftFiles = (await readdir(draftsDir)).filter((f) => f.endsWith('.md') && !f.endsWith('_draft.md'));
    for (const f of draftFiles) {
      allItems.push({ file: f, path: join(draftsDir, f), type: 'draft' });
    }
  }

  console.log(`Starting sync of ${allItems.length} article(s) to Supabase (${SUPABASE_URL})...\n`);

  let count = 0;
  for (const item of allItems) {
    try {
      const res = await syncArticle(item);
      count++;
      console.log(`[${res.status.toUpperCase()}] [${res.action}] ${item.file} -> slug: '${res.slug}'`);
    } catch (err) {
      console.error(`[FAIL] ${item.file}: ${err.message}`);
    }
  }

  console.log(`\nSuccessfully synchronized ${count}/${allItems.length} article(s) to Supabase.`);
}

main().catch((err) => {
  console.error('Fatal error:', err);
  process.exit(1);
});
