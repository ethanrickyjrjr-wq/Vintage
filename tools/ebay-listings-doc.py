"""Write the buyer-facing listing copy for an eBay batch as .docx (opens in Google Docs) and .txt (copy-paste).

    python tools/ebay-listings-doc.py assets/ebay-2026-11-08/listings-copy.md OUT.docx OUT.txt

Source format: '# Title' starts an item; '## Heading' a block; other lines are paragraphs or '- ' bullets.
Blanks for the tape are written as ____ with the photo estimate in brackets; Ricky replaces them before publishing.
"""
import re
import sys
from pathlib import Path

from docx import Document
from docx.shared import Pt

src, out_docx, out_txt = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
doc = Document()
style = doc.styles['Normal']; style.font.name = 'Arial'; style.font.size = Pt(11)
txt = []
for line in src.read_text(encoding='utf-8').splitlines():
    if line.startswith('# '):
        doc.add_heading(line[2:], level=1); txt += ['', '=' * 70, line[2:], '=' * 70]
    elif line.startswith('## '):
        doc.add_heading(line[3:], level=2); txt += ['', line[3:].upper()]
    elif line.startswith('- '):
        doc.add_paragraph(line[2:], style='List Bullet'); txt.append('  - ' + line[2:])
    elif line.strip():
        doc.add_paragraph(line); txt.append(line)
    else:
        txt.append('')
doc.save(out_docx); out_txt.write_text('\n'.join(txt).strip() + '\n', encoding='utf-8')
print('wrote', out_docx, out_txt)
