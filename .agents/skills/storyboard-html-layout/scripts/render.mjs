import { readFile, writeFile, mkdir } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';
const [input, output] = process.argv.slice(2);
if (!input || !output) throw new Error('Usage: node render.mjs input.json output.html');
const doc = JSON.parse(await readFile(resolve(input), 'utf8'));
if (typeof doc.title !== 'string' || !doc.title.trim() || !Array.isArray(doc.rows) || !doc.rows.length) throw new Error('title and non-empty rows are required');
if (doc.rows.some(row => !Array.isArray(row) || row.length !== 7 || row.some(cell => typeof cell !== 'string'))) throw new Error('Each row must contain seven strings');
if (new Set(doc.rows.map(row => row[0])).size !== doc.rows.length) throw new Error('Shot IDs must be unique');
for (const [shot, pick] of Object.entries(doc.materials || {})) {
  if (!doc.rows.some(row => row[0] === shot)) throw new Error('Unknown material shot ID: ' + shot);
  if (pick.codes && (!Array.isArray(pick.codes) || pick.codes.some(code => typeof code !== 'string'))) throw new Error('Material codes must be strings');
}
const template = await readFile(new URL('../assets/storyboard.html', import.meta.url), 'utf8');
const json = JSON.stringify(doc).replace(/</g, '\\u003c');
const html = template.replace('__STORYBOARD_JSON__', () => json);
await mkdir(dirname(resolve(output)), { recursive: true });
await writeFile(resolve(output), html, 'utf8');
console.log(resolve(output));
