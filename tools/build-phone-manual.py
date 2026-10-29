#!/usr/bin/env python3
"""Build docs/social-manual-phone.html from the two social manual markdown files.

The page is a derived copy: edit the markdown, rerun this, republish the HTML.
Needs: pip install markdown-it-py linkify-it-py beautifulsoup4
Run:   python tools/build-phone-manual.py
"""
import copy
import datetime
import re
from pathlib import Path

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent.parent
MANUAL = ROOT / "docs/social-manual.md"
BANKS = ROOT / "docs/social-manual-appendices.md"
OUT = ROOT / "docs/social-manual-phone.html"

# Contents tiles: id key -> (short label, optional hint). Full titles stay on the headings.
SHORT = {
    "0": ("The short version", ""), "1": ("Decisions", "4 answers needed"),
    "2": ("The rules", ""), "3": ("The link rule", ""), "3A": ("How to grow", ""),
    "4": ("Step by step", "Accounts, in order"), "5": ("What others do", ""),
    "6": ("Pipeline cost", ""), "7": ("Signups and prices", ""),
    "8": ("Calendar, short", ""), "9": ("Open conflicts and tests", "5 tests"),
    "10": ("Repo changes", ""), "11": ("Verified vs review", ""), "12": ("Source index", ""),
    "A": ("Hooks, captions, replies", "Copy buttons"), "B": ("12-month calendar", ""),
    "C": ("Cover system", ""), "D": ("90-minute shoot", "Shoot day"),
    "E": ("Four-week timing test", ""), "F": ("Music and AI labels", ""),
}

md = MarkdownIt("gfm-like")  # tables + bare-URL linkify; CommonMark list nesting and start numbers


def split(text):
    """Return (intro markdown, [(heading, body markdown)]) cut at each H2."""
    text = re.sub(r"\A# .*\n", "", text)
    parts = re.split(r"(?m)^## ", text)
    tidy = lambda s: re.sub(r"\n---\s*$", "\n", s.rstrip()) + "\n"
    secs = []
    for p in parts[1:]:
        head, _, body = p.partition("\n")
        secs.append((head.strip(), tidy(body)))
    return tidy(parts[0]), secs


def soup_of(markdown):
    tokens = md.parse(markdown)
    for tok in tokens:  # keep the source's own list numbers (e.g. "8." after "4.")
        if tok.type == "list_item_open" and tok.markup in (".", ")"):
            tok.attrSet("value", tok.info)
    return BeautifulSoup(md.renderer.render(tokens, md.options, {}), "html.parser")


def cards(soup):
    """Label every cell so the CSS can stack rows into cards on a phone."""
    for t in soup.find_all("table"):
        heads = [th.get_text(" ", strip=True) for th in t.find_all("th")]
        h0 = heads[0] if heads else ""
        kn = h0 in ("#", "Rank", "Min", "Week", "ID")  # first column is a number badge
        for tr in t.find_all("tr"):
            tds = tr.find_all("td")
            if not tds:
                continue
            kn_row = kn and len(tds) > 1
            for i, td in enumerate(tds):
                if i >= (2 if kn_row else 1) and i < len(heads) and heads[i]:
                    td["data-label"] = heads[i]
            if kn_row:
                v = tds[0].get_text(strip=True)
                if h0 == "Week" and v.isdigit():
                    tds[0].string = "Week " + v
                elif h0 == "Rank" and v.isdigit():
                    tds[0].string = "Rank " + v
                elif h0 == "Min":
                    tds[0].string = v + " min"
                tds[0]["class"] = "kn"
                tds[1]["class"] = "ct"
            else:
                tds[0]["class"] = "ct"
        t.wrap(soup.new_tag("div", attrs={"class": "tw"}))


def chips(soup):
    rx = re.compile(r"^(verified|vendor claim|inferred|need review|unverified|study|observed|practitioner|computed|press)\b")
    for c in soup.find_all("code"):
        m = rx.match(c.get_text())
        if m:
            k = m.group(1)
            c["class"] = ["tag", "good" if k == "verified" else "warn" if k in ("need review", "unverified") else "plain"]


def links(soup):
    for a in soup.find_all("a"):
        h = a.get("href", "")
        if h.startswith("http"):
            a["target"], a["rel"] = "_blank", "noopener noreferrer"
            if a.get_text() == h:
                shown = re.sub(r"^https?://(www\.)?", "", h).rstrip("/")
                a.string = shown if len(shown) <= 44 else shown[:42] + "…"


def xref(soup, rx, href):
    for t in list(soup.find_all(string=rx)):
        if t.find_parent(["a", "code", "button"]):
            continue
        s, last, new = str(t), 0, []
        for m in rx.finditer(s):
            new.append(s[last:m.start()])
            a = soup.new_tag("a", href=href(m))
            a.string = m.group(0)
            new.append(a)
            last = m.end()
        new.append(s[last:])
        t.replace_with(*new)


def copy_btn(soup, host, text):
    b = soup.new_tag("button", attrs={"type": "button", "class": "copy", "data-copy": text})
    b.string = "Copy"
    host.append(b)


def own_text(li):
    c = copy.copy(li)
    for x in c.find_all(["blockquote", "ul", "ol", "button"]):
        x.decompose()
    return c.get_text(" ", strip=True)


def copy_buttons(soup):
    """Copy buttons on the text Hollie pastes: hooks, caption examples, CTA lines, canned replies."""
    for t in soup.find_all("table"):
        heads = [th.get_text(strip=True) for th in t.find_all("th")]
        col = 1 if heads[:2] == ["#", "Hook line"] else heads.index("Example") if "Example" in heads else None
        if col is None:
            continue
        for tr in t.find_all("tr"):
            tds = tr.find_all("td")
            if len(tds) > col:
                copy_btn(soup, tds[col], tds[col].get_text(" ", strip=True))
    for h in soup.find_all("h3"):
        name = h.get_text()
        if name.startswith("A.4"):
            for li in h.find_next_sibling("ol").find_all("li", recursive=False):
                copy_btn(soup, li, own_text(li))
        if name.startswith("A.5"):
            for li in h.find_next_sibling("ul").find_all("li", recursive=False):
                m = re.search(r':\s*"(.+)"\s*$', own_text(li))
                if m:
                    copy_btn(soup, li, m.group(1))


def num_title(head):
    m = re.match(r"(\d+A?|[A-F])\.\s+(.*)", head)
    return m.group(1), m.group(2)


def build():
    m_intro, m_secs = split(MANUAL.read_text(encoding="utf-8"))
    b_intro, b_secs = split(BANKS.read_text(encoding="utf-8"))

    toc = {"manual": [], "banks": []}
    manual_html, banks_html = [], []

    for part, secs in (("manual", m_secs), ("banks", b_secs)):
        for head, body in secs:
            num, title = num_title(head)
            sid = ("s" if part == "manual" else "appx-") + num.lower()
            soup = soup_of(body)
            cards(soup)
            chips(soup)
            if part == "manual":
                xref(soup, re.compile(r"\b[Ss]ection (\d+A?)\b"), lambda m: "#s" + m.group(1).lower())
            xref(soup, re.compile(r"\bAppendix ([A-F])\b"), lambda m: "#appx-" + m.group(1).lower())
            if part == "banks":
                xref(soup, re.compile(r"\bsection ([A-F])(?:\.\d+)?\b"), lambda m: "#appx-" + m.group(1).lower())
                xref(soup, re.compile(r"\b[Ss]ee section 3\b"), lambda m: "#s3")
            if sid == "appx-a":
                copy_buttons(soup)
            links(soup)
            label, hint = SHORT[num]
            toc[part].append((sid, num, label, hint))
            inner = str(soup)
            if part == "manual":
                manual_html.append(f'<section class="sec" id="{sid}"><h2><span class="num">{num}</span> {title}</h2>{inner}</section>')
            else:
                banks_html.append(f'<details class="bank" id="{sid}"><summary><span class="num">{num}</span> <span>{title}</span></summary><div class="bank-body">{inner}</div></details>')

    def tiles(items):
        out = []
        for sid, num, label, hint in items:
            small = f"<small>{hint}</small>" if hint else ""
            out.append(f'<li><a href="#{sid}"><span class="n">{num}</span><span class="l">{label}{small}</span></a></li>')
        return "<ul>" + "".join(out) + "</ul>"

    intro = soup_of(m_intro)
    chips(intro)
    links(intro)
    banks_intro = soup_of(b_intro)
    chips(banks_intro)
    links(banks_intro)

    page = TEMPLATE
    for k, v in {
        "%%DATE%%": datetime.date.today().isoformat(),
        "%%INTRO%%": str(intro),
        "%%TOC_MANUAL%%": tiles(toc["manual"]),
        "%%TOC_BANKS%%": tiles(toc["banks"]),
        "%%MANUAL%%": "\n".join(manual_html),
        "%%BANKS_INTRO%%": str(banks_intro),
        "%%BANKS%%": "\n".join(banks_html),
    }.items():
        page = page.replace(k, v)
    OUT.write_text(page, encoding="utf-8")
    print(f"wrote {OUT} ({len(page):,} bytes)")


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Holliewood and Vine Social Manual</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:wght@500;600;700&family=DM+Sans:wght@400;500;700&display=swap">
<style>
:root {
  /* one reading column; sections stack open, tables become cards under 600px, banks fold away */
  --bg: #321520;
  --surface: #451c2b;
  --ink: #f6efdf;
  --muted: #d6bcc4;
  --accent: #e5a6b4;
  --line: #6a3447;
  --good: #a9dcb1;
  --warn: #f2c98a;
  --display: "Bodoni Moda", Didot, Georgia, serif;
  --body: "DM Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  --mono: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  color-scheme: dark;
}
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
@media (prefers-reduced-motion: no-preference) { html { scroll-behavior: smooth; } }
body { margin: 0; background: var(--bg); color: var(--ink); font: 400 1rem/1.6 var(--body); padding-bottom: 5rem; overflow-wrap: break-word; }
.wrap { max-width: 56rem; margin: 0 auto; padding: 0 16px; }
a { color: var(--accent); text-underline-offset: 2px; overflow-wrap: anywhere; }
:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
p, li { max-width: 68ch; }
strong { font-weight: 700; }

.top { padding: 2rem 0 1rem; }
.eyebrow { margin: 0 0 .5rem; color: var(--accent); font-size: .8125rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; }
h1 { margin: 0 0 1rem; font: 600 clamp(1.75rem, 7vw, 2.5rem)/1.15 var(--display); font-optical-sizing: none; letter-spacing: -.01em; }
.top > p { color: var(--muted); }
.toc h2, .part-h { margin: 1.5rem 0 .6rem; font: 700 .8125rem/1.2 var(--body); letter-spacing: .08em; text-transform: uppercase; color: var(--accent); }
.toc ul { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(10.5rem, 1fr)); gap: .5rem; }
.toc li { max-width: none; display: flex; }
.toc a { flex: 1; display: flex; gap: .6rem; align-items: baseline; min-height: 48px; padding: .6rem .75rem; border: 1px solid var(--line); border-radius: 10px; background: var(--surface); color: var(--ink); text-decoration: none; }
.toc .n { min-width: 1.5rem; color: var(--accent); font-weight: 700; }
.toc small { display: block; font-size: .75rem; line-height: 1.3; color: var(--muted); }

.part { margin-top: 2.5rem; padding-top: 1rem; border-top: 3px solid var(--accent); }
.part > h2 { margin: 0 0 .5rem; font: 600 1.75rem/1.2 var(--display); font-optical-sizing: none; }
.part-note, .part-note li { color: var(--muted); font-size: .9375rem; }
.sec { margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid var(--line); scroll-margin-top: 12px; }
.sec h2, .bank summary { font: 600 1.5rem/1.2 var(--display); font-optical-sizing: none; letter-spacing: -.005em; margin: 0 0 1rem; }
.num { color: var(--accent); margin-right: .35rem; }
h3 { margin: 1.75rem 0 .5rem; font: 700 1.125rem/1.3 var(--body); color: var(--accent); }
ul, ol { padding-left: 1.3rem; }
li { margin: .35rem 0; }
blockquote { margin: 1rem 0; padding: .1rem 0 .1rem 1rem; border-left: 3px solid var(--accent); color: var(--muted); }
code { font: .875rem/1.4 var(--mono); background: var(--surface); padding: .1rem .35rem; border-radius: 4px; overflow-wrap: anywhere; }
code.tag { font: 500 .8125rem/1.3 var(--body); padding: .05rem .5rem; border-radius: 999px; white-space: nowrap; }
code.tag.good { color: var(--good); background: rgba(169, 220, 177, .14); }
code.tag.warn { color: var(--warn); background: rgba(242, 201, 138, .14); }
code.tag.plain { color: var(--muted); background: rgba(246, 239, 223, .1); }

.tw { overflow-x: auto; margin: 1rem 0; }
table { border-collapse: collapse; width: 100%; }
th, td { padding: .6rem .75rem; text-align: left; vertical-align: top; border-bottom: 1px solid var(--line); }
th { font-size: .8125rem; letter-spacing: .04em; text-transform: uppercase; color: var(--accent); background: var(--surface); }
td.ct { font-weight: 700; }

.copy { display: block; margin: .5rem 0 0; min-height: 44px; padding: .6rem 1.1rem; border: 0; border-radius: 999px; background: var(--accent); color: var(--bg); font: 700 .9375rem var(--body); cursor: pointer; }
.copy.ok { background: var(--good); }

.bank { margin: .75rem 0; border: 1px solid var(--line); border-radius: 12px; background: rgba(0, 0, 0, .14); scroll-margin-top: 12px; }
.bank summary { display: flex; gap: .5rem; align-items: baseline; margin: 0; padding: 1rem; min-height: 56px; cursor: pointer; list-style: none; }
.bank summary::-webkit-details-marker { display: none; }
.bank summary::after { content: "+"; margin-left: auto; padding-left: .75rem; color: var(--accent); font: 700 1.5rem/1 var(--body); }
.bank[open] > summary::after { content: "\2013"; }
.bank-body { padding: 0 16px 16px; }
.btn { min-height: 44px; padding: .6rem 1.1rem; border: 1px solid var(--accent); border-radius: 999px; background: transparent; color: var(--accent); font: 700 .9375rem var(--body); cursor: pointer; }

.fab { position: fixed; right: 16px; bottom: 16px; z-index: 5; min-height: 44px; padding: .8rem 1.1rem; border-radius: 999px; background: var(--accent); color: var(--bg); font-weight: 700; text-decoration: none; box-shadow: 0 6px 20px rgba(0, 0, 0, .45); }
.foot { margin-top: 3rem; padding-top: 1rem; border-top: 1px solid var(--line); color: var(--muted); font-size: .9375rem; }

@media (max-width: 599px) {
  .tw { overflow: visible; }
  table, tbody { display: block; }
  thead { display: none; }
  tr { display: block; margin: 0 0 .75rem; padding: .35rem 0; background: var(--surface); border: 1px solid var(--line); border-radius: 10px; }
  td { display: block; padding: .4rem .9rem; border: 0; }
  td[data-label]::before { content: attr(data-label); display: block; margin-bottom: .1rem; font-size: .75rem; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; color: var(--accent); }
  td.ct { font-size: 1.0625rem; }
  td.kn { display: inline-block; margin: .5rem .9rem 0; padding: .1rem .7rem; border-radius: 999px; background: var(--accent); color: var(--bg); font-size: .8125rem; font-weight: 700; }
}
</style>
</head>
<body>
<div class="wrap">
<header class="top" id="top">
  <p class="eyebrow">Phone edition, built %%DATE%%</p>
  <h1>Holliewood and Vine social manual</h1>
  %%INTRO%%
  <nav class="toc" aria-label="Sections">
    <h2>The manual</h2>
    %%TOC_MANUAL%%
    <h2>The banks</h2>
    %%TOC_BANKS%%
  </nav>
</header>

<main>
<div class="part" id="manual">
  <h2>Part 1. The manual</h2>
  %%MANUAL%%
</div>

<div class="part" id="banks">
  <h2>Part 2. The banks</h2>
  <div class="part-note">%%BANKS_INTRO%%</div>
  <p><button type="button" class="btn" id="toggle-banks">Open all banks</button></p>
  %%BANKS%%
</div>
</main>

<footer class="foot">
  <p>Built %%DATE%% from <code>docs/social-manual.md</code> and <code>docs/social-manual-appendices.md</code>. The Claude Code and Codex build spec (<code>docs/codex-handoff-social-autopilot.md</code>) is not in this edition. Prices were read on 2026-10-29; re-check them on the signup page before paying.</p>
</footer>
</div>
<a class="fab" href="#top">Contents</a>
<script>
(function () {
  function show(id) {
    var el = id && document.getElementById(id);
    if (!el) return;
    var d = el.tagName === "DETAILS" ? el : el.closest("details");
    if (d) d.open = true;
    requestAnimationFrame(function () { el.scrollIntoView(); });
  }
  function copyText(b) {
    var t = b.getAttribute("data-copy");
    function done(ok) {
      b.textContent = ok ? "Copied" : "Copy failed";
      b.classList.toggle("ok", ok);
      setTimeout(function () { b.textContent = "Copy"; b.classList.remove("ok"); }, 1800);
    }
    function fallback() {
      try {
        var ta = document.createElement("textarea");
        ta.value = t; ta.setAttribute("readonly", ""); ta.style.cssText = "position:fixed;opacity:0";
        document.body.appendChild(ta); ta.select();
        var ok = document.execCommand("copy");
        document.body.removeChild(ta); done(ok);
      } catch (e) { done(false); }
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(t).then(function () { done(true); }, fallback);
    } else { fallback(); }
  }
  document.addEventListener("click", function (e) {
    var a = e.target.closest('a[href^="#"]');
    if (a) setTimeout(function () { show(a.getAttribute("href").slice(1)); }, 0);
    var b = e.target.closest(".copy");
    if (b) copyText(b);
  });
  window.addEventListener("hashchange", function () { show(location.hash.slice(1)); });
  var tog = document.getElementById("toggle-banks");
  tog.addEventListener("click", function () {
    var open = tog.textContent === "Open all banks";
    document.querySelectorAll("details.bank").forEach(function (d) { d.open = open; });
    tog.textContent = open ? "Close all banks" : "Open all banks";
  });
  if (location.hash) show(location.hash.slice(1));
})();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    build()
