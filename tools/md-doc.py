"""Render a simple markdown file to .docx with real hyperlinks (Google Docs opens it with the links live).

    python tools/md-doc.py SRC.md OUT.docx

Supports: '# ', '## ', '### ' headings, '- ' bullets, paragraphs, inline [text](url) links and **bold**.
Anything else is written as plain text. Used for docs/sourcing-calendar-2026-11.md on Ricky's Drive.
"""
import re
import sys
from pathlib import Path

import docx
from docx import Document
from docx.oxml.shared import OxmlElement, qn
from docx.shared import Pt

INLINE = re.compile(r'(\[([^\]]+)\]\((https?://[^)\s]+)\))|(\*\*([^*]+)\*\*)')


def add_link(par, url, text):
    rid = par.part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK, is_external=True)
    h = OxmlElement('w:hyperlink'); h.set(qn('r:id'), rid)
    r = OxmlElement('w:r'); rpr = OxmlElement('w:rPr')
    c = OxmlElement('w:color'); c.set(qn('w:val'), '1155CC'); rpr.append(c)
    u = OxmlElement('w:u'); u.set(qn('w:val'), 'single'); rpr.append(u)
    r.append(rpr)
    t = OxmlElement('w:t'); t.text = text; t.set(qn('xml:space'), 'preserve'); r.append(t)
    h.append(r); par._p.append(h)


def write_inline(par, text):
    pos = 0
    for m in INLINE.finditer(text):
        if m.start() > pos:
            par.add_run(text[pos:m.start()])
        if m.group(1):
            add_link(par, m.group(3), m.group(2))
        else:
            par.add_run(m.group(5)).bold = True
        pos = m.end()
    if pos < len(text):
        par.add_run(text[pos:])


src, out = Path(sys.argv[1]), Path(sys.argv[2])
doc = Document()
st = doc.styles['Normal']; st.font.name = 'Arial'; st.font.size = Pt(11)
for line in src.read_text(encoding='utf-8').splitlines():
    if line.startswith('### '):
        write_inline(doc.add_heading('', level=3), line[4:])
    elif line.startswith('## '):
        write_inline(doc.add_heading('', level=2), line[3:])
    elif line.startswith('# '):
        write_inline(doc.add_heading('', level=1), line[2:])
    elif line.startswith('- '):
        write_inline(doc.add_paragraph(style='List Bullet'), line[2:])
    elif line.strip():
        write_inline(doc.add_paragraph(), line)
out.parent.mkdir(parents=True, exist_ok=True)
doc.save(out)
print('wrote', out)
