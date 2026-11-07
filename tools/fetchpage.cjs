#!/usr/bin/env node
// Fetch one URL as markdown from a cloud session, where crawl4ai is not installed.
// curl first (honours HTTPS_PROXY and the proxy CA); if the page comes back as a JS shell,
// render it with the pre-installed Playwright Chromium; then HTML -> markdown with turndown.
// usage: NODE_PATH="$(npm root -g)" node tools/fetchpage.cjs "<url>" <out.md> [--browser]
const { execFileSync } = require('child_process');
const fs = require('fs');
const TurndownService = require('turndown');

const [url, out, mode] = process.argv.slice(2);
if (!url || !out) { console.error('usage: fetchpage.cjs <url> <out.md> [--browser]'); process.exit(2); }
const UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36';
const stamp = new Date().toISOString().slice(0, 10);

function curlGet(u) {
  const hdr = '/tmp/fetchpage-hdr-' + process.pid;
  try {
    const body = execFileSync('curl', ['-sS', '-L', '-m', '60', '-A', UA, '-H', 'Accept-Language: en-US,en;q=0.9',
      '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const headers = fs.readFileSync(hdr, 'utf8'); fs.unlinkSync(hdr);
    const statuses = [...headers.matchAll(/^HTTP\/[\d.]+ (\d{3})/gm)].map(m => +m[1]);
    const ctype = (headers.match(/^content-type:\s*(.*)$/im) || [, ''])[1].trim();
    return { status: statuses[statuses.length - 1] || 0, ctype, body };
  } catch (e) {
    const msg = (e.stderr && e.stderr.toString()) || e.message;
    return { status: 0, ctype: '', body: Buffer.alloc(0), error: msg.trim() };
  }
}

function toMarkdown(html) {
  const cleaned = html
    .replace(/<script[\s\S]*?<\/script>/gi, '')
    .replace(/<style[\s\S]*?<\/style>/gi, '')
    .replace(/<noscript[\s\S]*?<\/noscript>/gi, '')
    .replace(/<svg[\s\S]*?<\/svg>/gi, '');
  const td = new TurndownService({ headingStyle: 'atx', codeBlockStyle: 'fenced', bulletListMarker: '-' });
  td.remove(['nav', 'footer', 'iframe', 'form', 'button', 'select', 'input']);
  return td.turndown(cleaned).replace(/\n{3,}/g, '\n\n');
}

function looksLikeShell(md) {
  const t = md.replace(/\s+/g, ' ');
  return t.length < 1200 || /enable javascript|please enable js|access denied|just a moment|verify you are human/i.test(t);
}

async function render(u) {
  const { chromium } = require('playwright');
  const proxy = process.env.HTTPS_PROXY || process.env.https_proxy;
  const browser = await chromium.launch({ proxy: proxy ? { server: proxy } : undefined, args: ['--no-sandbox'] });
  try {
    const page = await browser.newPage({ userAgent: UA, viewport: { width: 1280, height: 2000 } });
    const resp = await page.goto(u, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.waitForTimeout(2500);
    const html = await page.content();
    return { status: resp ? resp.status() : 0, html };
  } finally { await browser.close(); }
}

(async () => {
  let note = '', md = '', status = 0;
  if (mode !== '--browser') {
    const r = curlGet(url);
    status = r.status;
    if (r.error) note = 'curl: ' + r.error;
    else if (/json|text\/plain|markdown|csv|xml/i.test(r.ctype) && !/html/i.test(r.ctype)) md = r.body.toString('utf8');
    else md = toMarkdown(r.body.toString('utf8'));
  }
  if ((mode === '--browser' || looksLikeShell(md)) && !/CONNECT tunnel failed|response 403/i.test(note)) {
    try {
      const r = await render(url);
      const md2 = toMarkdown(r.html);
      if (md2.length > md.length) { md = md2; status = r.status; note += (note ? ' | ' : '') + 'rendered with Playwright'; }
    } catch (e) { note += (note ? ' | ' : '') + 'playwright: ' + e.message.split('\n')[0]; }
  }
  const header = `<!-- source: ${url}, fetched ${stamp}, http ${status}${note ? ', ' + note : ''} -->\n`;
  fs.mkdirSync(require('path').dirname(out), { recursive: true });
  fs.writeFileSync(out, header + md + '\n');
  const bytes = Buffer.byteLength(md);
  console.log(`${out} (${bytes} bytes, http ${status}${note ? ', ' + note : ''})`);
  if (bytes < 1024) { console.error('WARNING: under 1 KB, likely a wall or a blocked host, not a page.'); process.exit(1); }
})();
