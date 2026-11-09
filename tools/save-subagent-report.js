// usage: node tools/save-subagent-report.js <session transcript .jsonl> <agentId> <out.md> <lane label>
// Pulls a subagent hand-back out of the session transcript and saves it verbatim.
const fs = require('fs');
const [tx, id, out, label] = process.argv.slice(2);
const strings = [];
const walk = v => {
  if (typeof v === 'string') strings.push(v);
  else if (v && typeof v === 'object') Object.values(v).forEach(walk);
};
for (const line of fs.readFileSync(tx, 'utf8').split('\n')) {
  if (!line.includes(id)) continue;
  try { walk(JSON.parse(line)); } catch {}
}
const marker = `<agent-message from="${id}">`;
const hit = strings.find(s => s.includes(marker) && s.includes('The report follows:\n'));
if (!hit) { console.error('not found'); process.exit(1); }
let body = hit.slice(hit.indexOf(marker));
body = body.slice(body.indexOf('The report follows:\n') + 'The report follows:\n'.length);
const end = body.indexOf('\n</agent-message>');
if (end >= 0) body = body.slice(0, end);
body = body.split('\n').map(l => (l.startsWith('  ') ? l.slice(2) : l)).join('\n').trimEnd() + '\n';
const header = `<!-- Saved verbatim by the parent Opus session from subagent lane ${label}'s final message, ${new Date().toISOString().slice(0,10)} (the harness refuses subagent report writes). -->\n\n`;
fs.writeFileSync(out, header + body);
console.log(out, Buffer.byteLength(header + body), 'bytes');
