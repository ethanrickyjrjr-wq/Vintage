"""Export the Facebook + eBay launch plan to Google Drive (Drive for desktop, allstatecoop@gmail.com).

    uv run --with openpyxl --with python-docx python -I tools/launch-drive-export.py "G:/My Drive/Holliewood Launch" [--todo]

Docs are re-exported every run (same path = new Drive revision, same link).
The to-do workbook is only written when it does not exist yet, or with --todo,
so ticks Ricky made in Drive are never overwritten by accident.
Also writes the repo snapshot docs/launch-todo.md.
"""
import re, sys, os
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1]
FORCE_TODO = '--todo' in sys.argv

DOCS = [  # (repo markdown, path under OUT)
    ('docs/following-2026-11.md', '01 Read first - the plan.docx'),
    ('docs/facebook-marketplace.md', 'Facebook/Facebook Marketplace setup.docx'),
    ('research/following-2026-11-09/f1-local-swfl.md', 'Facebook/Research/f1 Local SWFL groups and Pages.docx'),
    ('research/following-2026-11-09/f2-national-niche.md', 'Facebook/Research/f2 National and niche groups.docx'),
    ('research/following-2026-11-09/f3-meta-rules.md', 'Facebook/Research/f3 Meta rules and limits.docx'),
    ('research/following-2026-11-09/f4-fb-playbook.md', 'Facebook/Research/f4 Marketplace playbook.docx'),
    ('docs/ebay-setup.md', 'eBay/eBay shop setup.docx'),
    ('research/following-2026-11-09/e1-ebay-mechanics.md', 'eBay/Research/e1 eBay mechanics and policy.docx'),
    ('research/following-2026-11-09/e2-ebay-sellers-communities.md', 'eBay/Research/e2 Sellers and communities.docx'),
    ('research/following-2026-11-09/e3-ebay-playbook.md', 'eBay/Research/e3 eBay growth playbook.docx'),
]

# ---------- markdown -> docx (headings, paragraphs, lists, pipe tables, bold/code/links) ----------
INLINE = re.compile(r'(\*\*.+?\*\*|`[^`]+`|~~.+?~~|\[[^\]]+\]\([^)\s]+\)|https?://[^\s)|>]+|(?:www\.)?(?:facebook|ebay|instagram)\.com/[^\s)|,;]+)')
BARE = re.compile(r'^(?:www\.)?(?:facebook|ebay|instagram)\.com/')

def hyperlink(par, url, text):
    r_id = par.part.relate_to(url, 'http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink', is_external=True)
    h = OxmlElement('w:hyperlink'); h.set(qn('r:id'), r_id)
    r = OxmlElement('w:r'); rpr = OxmlElement('w:rPr')
    c = OxmlElement('w:color'); c.set(qn('w:val'), '1155CC'); rpr.append(c)
    u = OxmlElement('w:u'); u.set(qn('w:val'), 'single'); rpr.append(u)
    r.append(rpr); t = OxmlElement('w:t'); t.text = text; t.set(qn('xml:space'), 'preserve'); r.append(t)
    h.append(r); par._p.append(h)

def inline(par, text, size=None):
    for tok in INLINE.split(text):
        if not tok:
            continue
        run = None
        if tok.startswith('**') and tok.endswith('**') and len(tok) > 4:
            run = par.add_run(tok[2:-2]); run.bold = True
        elif tok.startswith('`') and tok.endswith('`'):
            run = par.add_run(tok[1:-1]); run.font.name = 'Consolas'
        elif tok.startswith('~~') and tok.endswith('~~'):
            run = par.add_run(tok[2:-2]); run.font.strike = True
        elif tok.startswith('[') and '](' in tok:
            label, url = tok[1:-1].split('](', 1)
            if url.startswith('http'):
                hyperlink(par, url, label)
            else:  # repo-relative link: dead in Drive, keep the words only
                run = par.add_run(label)
        elif tok.startswith('http'):
            hyperlink(par, tok, tok)
        elif BARE.match(tok):  # bare facebook.com/... style links in the reports
            hyperlink(par, 'https://' + tok.rstrip('.'), tok)
        else:
            run = par.add_run(tok)
        if run is not None and size:
            run.font.size = Pt(size)

def cells(line):
    return [c.strip().replace('\\|', '|') for c in re.split(r'(?<!\\)\|', line.strip().strip('|'))]

def md_to_docx(src, dst):
    text = re.sub(r'<!--.*?-->', '', open(src, encoding='utf-8').read(), flags=re.S)
    lines = text.splitlines()
    doc = Document()
    st = doc.styles['Normal']; st.font.name = 'Arial'; st.font.size = Pt(10.5)
    if any(l.strip().startswith('|') and len(cells(l)) > 5 for l in lines):  # wide tables: landscape
        s = doc.sections[0]; s.orientation = WD_ORIENT.LANDSCAPE
        s.page_width, s.page_height = s.page_height, s.page_width
    for s in doc.sections:
        s.left_margin = s.right_margin = s.top_margin = s.bottom_margin = Inches(0.6)
    i, buf = 0, []
    def flush():
        if buf:
            inline(doc.add_paragraph(), ' '.join(buf)); buf.clear()
    while i < len(lines):
        l = lines[i]
        m_h = re.match(r'^(#{1,4})\s+(.*)', l)
        m_b = re.match(r'^(\s*)[-*]\s+(.*)', l)
        m_n = re.match(r'^(\s*)(\d+)\.\s+(.*)', l)
        if not l.strip():
            flush()
        elif m_h:
            flush(); doc.add_heading(re.sub(r'\*\*|`', '', m_h.group(2)), level=len(m_h.group(1)))
        elif l.strip().startswith('|'):
            flush(); rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                if not re.match(r'^\s*\|?[\s:|-]+\|?\s*$', lines[i]):
                    rows.append(cells(lines[i]))
                i += 1
            ncol = max(len(r) for r in rows)
            t = doc.add_table(rows=0, cols=ncol); t.style = 'Table Grid'
            for ri, r in enumerate(rows):
                rc = t.add_row().cells
                for ci in range(ncol):
                    p = rc[ci].paragraphs[0]
                    inline(p, r[ci] if ci < len(r) else '', size=8.5 if ncol > 5 else 9.5)
                    if ri == 0:
                        for run in p.runs: run.bold = True
            doc.add_paragraph()
            continue
        elif m_b or m_n:
            flush()
            ind = len((m_b or m_n).group(1).expandtabs(2)) // 2
            if m_b:
                p = doc.add_paragraph(style=['List Bullet', 'List Bullet 2', 'List Bullet 3'][min(ind, 2)])
                body = m_b.group(2)
            else:
                p = doc.add_paragraph(); p.paragraph_format.left_indent = Inches(0.25 + 0.25 * ind)
                p.add_run(m_n.group(2) + '. '); body = m_n.group(3)
            # continuation lines of the same item
            while i + 1 < len(lines) and lines[i + 1].strip() and not re.match(r'^\s*([-*]|\d+\.|\||#)', lines[i + 1]):
                i += 1; body += ' ' + lines[i].strip()
            inline(p, body)
        else:
            buf.append(l.strip())
        i += 1
    flush()
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    doc.save(dst)

# ---------- the to-do list, in the order to do it ----------
WHO_OK = 'Claude (needs Ricky\'s OK)'
TODO = [
    # phase, task, who, needs first, link or file, when, notes
    ('A. This week: decisions and quick wins', 'Open and answer the 19 unread eBay messages. Some may be buyer questions', 'Ricky', '', 'https://www.ebay.com/mesg', 'Today', 'Nobody has opened them yet'),
    ('A. This week: decisions and quick wins', 'Watch the Alice + Olivia sandals auction (ends Tue Nov 10, 5:44 PM ET). If it sells, ship within 2 business days', 'Ricky', '', 'https://www.ebay.com/sh/ord', 'Nov 10', 'It still shows "no returns"'),
    ('A. This week: decisions and quick wins', 'DECIDE: launch Facebook Marketplace and groups in November? The social manual said November is setup only', 'Ricky', '', '01 Read first - the plan', 'This week', 'Real stock now exists, which was the manual\'s own condition'),
    ('A. This week: decisions and quick wins', 'DECIDE: heavy pieces (the $850 Bassett table). eBay local pickup only, or another way to hand over?', 'Ricky', '', '', 'This week', 'A police-station parking lot cannot take furniture'),
    ('A. This week: decisions and quick wins', 'DECIDE: keep the Bassett table in its General Promoted Listings campaign?', 'Ricky', '', 'https://www.ebay.com/sh/mkt', 'This week', 'You owe the ad fee if any buyer clicked the ad in the 30 days before the sale. Adding to a watchlist counts as a click'),
    ('A. This week: decisions and quick wins', 'APPROVE: move the 7 live eBay listings onto the HWV policies (30-day returns, 2-day handling)', 'Ricky', '', 'eBay/eBay shop setup', 'This week', 'Claude does it in Chrome after your yes'),
    ('A. This week: decisions and quick wins', 'APPROVE: two shop-kit wording fixes. Reply 11 becomes "share the pickup address in eBay Messages after the buyer has paid". Drop the feedback line from thank-you cards that go out with a gift', 'Ricky', '', 'Holliewood eBay/Shop setup', 'This week', 'Claude updates the repo and the Drive copy'),
    ('A. This week: decisions and quick wins', 'Revise the 7 live listings onto the HWV policies', WHO_OK, '6', '', 'After yes', ''),
    ('A. This week: decisions and quick wins', 'Apply the two kit fixes in the repo and in Drive "Shop setup"', WHO_OK, '7', '', 'After yes', ''),
    ('A. This week: decisions and quick wins', 'Paste profile-bio.txt into the eBay profile About box by hand (the automated save did not stick)', 'Ricky', '', 'https://www.ebay.com/usr/holliewoodandvinellc?_tab=about', 'This week', 'File: Holliewood eBay/Shop setup/profile-bio.txt (or the repo kit)'),
    ('A. This week: decisions and quick wins', 'Change the Instagram bio link from the empty Depop shop to the eBay profile', 'Hollie or Ricky', '', 'https://www.ebay.com/usr/holliewoodandvinellc', 'This week', 'Allowed: eBay\'s link rules cover listings, not Instagram'),
    ('A. This week: decisions and quick wins', 'Check the Items folder: number 09 is missing and 46 has no listing.txt', 'Ricky', '', 'Holliewood eBay/Items', 'This week', ''),
    ('A. This week: decisions and quick wins', 'Order plain thank-you cards (no promo code; no feedback line on cards that go out with a gift)', 'Ricky', '7', '', 'This week', 'Under $15'),
    ('A. This week: decisions and quick wins', 'Optional sourcing: estate sales Nov 13-14, and a Lockerfox lot Nov 14 that includes a mannequin and a wire rack', 'Ricky', '', 'Repo: docs/sourcing-calendar-2026-11.md', 'Nov 13-14', 'Not in this folder; ask Claude for it'),
    ('B. Facebook: move to Hollie\'s own account', 'Hollie gives access to her own Facebook account. She runs it day to day (Meta\'s terms bar sharing an account)', 'Hollie', '', '', 'When ready', 'Ricky, 2026-11-09: "hollie has facebook. getting it soon"'),
    ('B. Facebook: move to Hollie\'s own account', 'Check that Marketplace opens: Menu > Profile status > Marketplace', 'Hollie', '15', 'https://www.facebook.com/marketplace', '', ''),
    ('B. Facebook: move to Hollie\'s own account', 'Check professional mode is OFF. If it is on, the free Verified badge is blocked', 'Hollie', '15', '', '', ''),
    ('B. Facebook: move to Hollie\'s own account', 'Make sure the profile photo is her face, not the logo', 'Hollie', '15', '', '', 'The Verified selfie is matched against her photos'),
    ('B. Facebook: move to Hollie\'s own account', 'Add the work line "Owner at Holliewood & Vine" and the bio: "Holliewood & Vine. Curated vintage clothes, lamps, art and decor. IG @holliewoodandvine"', 'Hollie or ' + WHO_OK, '15', '', '', 'The same text the "Hollie Wood" profile has now'),
    ('B. Facebook: move to Hollie\'s own account', 'Get the free Facebook Verified badge: Settings > Verified info and badge (a video selfie, on her phone), if it is offered', 'Hollie', '17, 18', '', '', 'It shows on Marketplace. It is rolling out in stages, so it may not show yet'),
    ('B. Facebook: move to Hollie\'s own account', 'Set up payouts: bank or PayPal, plus the tax ID when asked', 'Hollie or Ricky', '15', '', '', 'Claude never enters bank or tax details'),
    ('B. Facebook: move to Hollie\'s own account', 'Recreate the item 01 draft on her account (photos and text are in Drive Items/01)', 'Hollie or ' + WHO_OK, '16', 'Holliewood eBay/Items/01 liz-claiborne-leopard-shirt-dress', '', 'Leave price and condition blank until it is measured'),
    ('B. Facebook: move to Hollie\'s own account', 'DECIDE: retire the extra "Hollie Wood" profile? Deactivating is the least destructive way', 'Ricky', '22', 'https://www.facebook.com/profile.php?id=61596451137563', '', 'Meta\'s terms allow one account per person. Claude will not delete it'),
    ('B. Facebook: move to Hollie\'s own account', 'Optional: link @holliewoodandvine in Accounts Center to auto-share posts. Do NOT sync the profile picture', 'Hollie', '15', 'https://accountscenter.facebook.com', '', 'A synced picture would put the script logo over her face'),
    ('B. Facebook: move to Hollie\'s own account', 'Like the Pages on the "FB Pages to like" tab, a few a day', 'Hollie', '18', 'Tab: FB Pages to like', '', 'Liking is low risk. Comment for real, not to promote'),
    ('C. Before the first listings', 'Measure each piece and check its condition (fill-in workbook in Holliewood eBay)', 'Hollie or Ricky', '', 'Holliewood eBay/Holliewood eBay batch 2026-11-08 - fill in.xlsx', 'Nov 12-15', 'Description errors mean you pay the return shipping'),
    ('C. Before the first listings', 'Decide where each piece goes: shipped clothes on eBay; lamps, art and decor for local pickup on Marketplace', 'Ricky + Claude', '3, 4', '', 'Nov 12-15', ''),
    ('C. Before the first listings', 'Check whether shipped eBay listings already show on Marketplace through the eBay partnership. Never list the same piece twice', 'Claude', '', 'https://www.facebook.com/marketplace', 'Nov 12-15', 'Two live copies of a one-of-one piece can sell twice'),
    ('C. Before the first listings', 'Call the Lee County Sheriff (239-477-1000) to confirm a current safe-exchange spot. Pick two public spots for daytime meetups', 'Ricky', '', '', 'Nov 12-15', 'Number is from a search result. The only spot found is Fort Myers PD, 2210 Widman Way (2018)'),
    ('C. Before the first listings', 'Write the Marketplace reply template: available, no holds, public spot, daylight', 'Claude', '29', '', 'Nov 12-15', ''),
    ('C. Before the first listings', 'Turn off Meta AI auto-replies on pieces that are also on eBay', 'Hollie', '15', '', 'Nov 12-15', 'An auto-reply can say "available" after the piece sold on eBay'),
    ('D. Week 1 (Nov 16-22)', 'eBay: publish the first 10-12 items, measured, with every item specific filled in', 'Ricky or ' + WHO_OK, '26', 'https://www.ebay.com/sh/lst/active', 'Nov 16-22', 'Use the HWV templates'),
    ('D. Week 1 (Nov 16-22)', 'eBay: turn on Best Offer for pieces over about $30, with an auto-decline floor. Use tracking on every order', 'Ricky', '32', '', 'Nov 16-22', 'Both feedbacks so far are eBay automated ones, which need tracking'),
    ('D. Week 1 (Nov 16-22)', 'Marketplace: 3 listings, at most one a day. Cut-out cover, one on-form or room shot, label and flaw close-ups', 'Hollie', '16, 18, 27, 28, 29', 'https://www.facebook.com/marketplace/create/item', 'Nov 16-22', 'Price from eBay sold listings, not 1stDibs'),
    ('D. Week 1 (Nov 16-22)', 'Reply to messages within hours. No holds. Meet in public, in daylight', 'Hollie', '34', '', 'Nov 16-22', ''),
    ('D. Week 1 (Nov 16-22)', 'After each eBay delivery, leave the buyer\'s feedback promptly', 'Ricky', '', '', 'Ongoing', ''),
    ('D. Week 1 (Nov 16-22)', 'Hold off: no Facebook groups, no boosts, no renewing in week 1', 'Hollie', '', '', 'Nov 16-22', 'Brand-new Marketplace activity is the risky part'),
    ('E. Weeks 2-4 (Nov 23 - Dec 13)', 'eBay: list about 12 more a week, with coats and party or midi dresses first. Log watchers, views and offers', 'Ricky or ' + WHO_OK, '32', '', 'Weekly', 'Holiday demand'),
    ('E. Weeks 2-4 (Nov 23 - Dec 13)', 'eBay: send 10% offers to watchers, Friday to Sunday around midday. First test Nov 20-22, then Black Friday weekend Nov 27-29', 'Ricky', '32', 'https://www.ebay.com/sh/lst/active', 'Fri-Sun', 'Free on the current account. Lasts 96 hours. Goes to the 30 most recent watchers'),
    ('E. Weeks 2-4 (Nov 23 - Dec 13)', 'Thanksgiving week: post reply-time windows. Use eBay Time Away if you won\'t ship Nov 26-27', 'Ricky + Hollie', '', '', 'Nov 23-29', ''),
    ('E. Weeks 2-4 (Nov 23 - Dec 13)', 'Marketplace: 3-4 listings a week. Ask each real buyer for a rating in the app (ratings go public at 5)', 'Hollie', '34', '', 'Weekly', 'Never offer anything for a rating'),
    ('E. Weeks 2-4 (Nov 23 - Dec 13)', 'Join Facebook groups 1-2 a week, in the order on the "FB groups in order" tab', 'Hollie', '18, 34', 'Tab: FB groups in order', 'From Nov 30', 'Read the rules first. One share per item, 5-7 days apart'),
    ('E. Weeks 2-4 (Nov 23 - Dec 13)', 'First brand post in Colourful & Maximalist (Tue, Sat or Sun; at most 2 a month; handle plus a few lines plus a photo carousel)', 'Hollie', '42', 'https://www.facebook.com/groups/1019448162828926', 'From Nov 30', 'The one big group that allows business posts'),
    ('E. Weeks 2-4 (Nov 23 - Dec 13)', 'Marketplace: renew a listing that is 7+ days old with no messages, once. Cut the price 5%+ on listings with saves but no messages', 'Hollie', '34', '', 'From Nov 30', 'Never post a second copy while the first is live'),
    ('E. Weeks 2-4 (Nov 23 - Dec 13)', 'Instagram: one post a week about new pieces (no links in any listing)', 'Hollie', '', 'https://www.instagram.com/holliewoodandvine/', 'Weekly', ''),
    ('E. Weeks 2-4 (Nov 23 - Dec 13)', 'Week-4 review: views, messages and sales per listing. Keep, reprice or retire each one', 'Ricky + Claude', '', '', 'Dec 7-13', ''),
    ('E. Weeks 2-4 (Nov 23 - Dec 13)', 'Decide on Promoted Listings: only with 20+ listings and 14+ days of data. Fixed rate, at most 5 pieces over $40', 'Ricky', '46', 'https://www.ebay.com/sh/mkt', 'Dec 7-13', 'Never use a dynamic rate'),
    ('E. Weeks 2-4 (Nov 23 - Dec 13)', 'Submit the eBay Live interest form (don\'t count on it)', 'Ricky', '', 'https://www.ebay.com/ebaylive/seller', 'Dec 7-13', 'Needs a business account. Giveaways need eBay\'s prior approval'),
    ('F. Later', 'Before buying the eBay Store: confirm at checkout which tier (Starter or Basic) unlocks newsletters, coupons, sale events and buyer groups', 'Ricky', '', 'https://www.ebay.com/sellercenter/selling/how-to-sell/set-up-your-store', 'When upgrading', 'No US page confirms that Starter gets them'),
    ('F. Later', 'After the Store: first newsletter to followers and recent buyers with an active coupon; a printed coupon code in parcels', WHO_OK, '49', '', '', 'At most one email per buyer every 14 days. No outside links'),
    ('F. Later', 'Join Quirky Groovy Vintage Buy/Sell/Trade once the profile passes its rules (photo, friends, activity); the seller subscription goes through its admins', 'Hollie', '18, 42', 'https://www.facebook.com/groups/497230079689590', '', 'The best vintage selling group found (74.9K members)'),
    ('F. Later', 'Vintage Market Days South Gulf Coast, Jan 29-31, 2027, Lee Civic Center: check the deadline for the juried application', 'Ricky', '', 'https://www.facebook.com/vmdsogulfcoastfl/', 'December', ''),
    ('F. Later', 'Collab outreach: Flamingo Island Flea Market (vendor space or a repost) and @swflgulfcoastthrifts (Kelly Chenault)', 'Hollie', '', 'https://www.instagram.com/swflgulfcoastthrifts/', '', 'Never "follow to win" anything. Meta bans rewards for engagement'),
    ('F. Later', 'Paradise Vintage Market: confirm today\'s rack price ($95 a month in 2024)', 'Ricky', '', 'https://www.facebook.com/Paradisevintagemarket/', '', 'A sales test that needs no showroom'),
]

PAGES = [  # name, url, why, source
    ('Flamingo Island Flea Market (Bonita Springs)', 'https://www.facebook.com/flamingoisland/', 'Hollie\'s town. The Instagram already reposted it. Its own Instagram is @flamingoflea', 'f1: link on its own site'),
    ('Vintage Market Days South Gulf Coast', 'https://www.facebook.com/vmdsogulfcoastfl/', 'The vintage-shopper event: Jan 29-31, 2027, Lee Civic Center. Juried', 'f1: link on its own site'),
    ('Naples Design District', 'https://www.facebook.com/naplesdesigndistrict', 'Decor shoppers, holiday stroll', 'f1: link on its own site'),
    ('Home and Salvage (Naples)', 'https://www.facebook.com/home.salvage/', 'A similar boutique in the Design District', 'f1: search result'),
    ('Paradise Vintage Market (N. Fort Myers)', 'https://www.facebook.com/Paradisevintagemarket/', 'A clothing-rack test with no showroom needed', 'f1: search result'),
    ('Gulfshore Life', 'https://www.facebook.com/GulfshoreLife/', 'Local press to pitch', 'f1: link on its own site'),
    ('Palm Beach Regency', 'https://www.facebook.com/palmbeachregency/', 'The Florida shop closest to our look', 'f2: link on its own site'),
    ('Vintage Regency Boutique', 'https://www.facebook.com/vintageregencyboutique', 'Old Florida / Palm Beach Regency style', 'f2: link on its own site'),
    ('Chairish', 'https://www.facebook.com/chairishco', 'Vintage decor, lighting, Regency', 'f2: link on its own site'),
    ('Thrifty Decor Chick', 'https://www.facebook.com/ThriftyDecorChick', 'Her readers buy decor on Marketplace', 'f2: link on its own site'),
    ('Estate Love of Southwest Florida', 'https://www.facebook.com/p/Estate-Love-of-Southwest-Florida-100067048556217/', 'Estate-sale announcements (sourcing)', 'f1: search result'),
    ('Sweetwater Trading (Bonita Springs)', 'https://www.facebook.com/swt239/', 'A local vintage peer that takes consignments', 'f1: search result'),
    ('Instagram: SWFL Gulf Coast Thrifts', 'https://www.instagram.com/swflgulfcoastthrifts/', 'Local thrift creator with 10K+ followers; a collab lead', 'f1: WINK News, June 2026'),
]

GROUPS = [  # order, name, url, members, rules, use, checked
    (1, 'Colourful & Maximalist Home Decor Inspo', 'https://www.facebook.com/groups/1019448162828926', '662,779 (Nov 9)', 'Business and Instagram posts allowed Tue, Sat and Sun, at most 2 a month: handle, a few lines, photo carousel', 'Brand posts', 'Signed-in check, Nov 9'),
    (2, 'Fort Myers Life', 'https://www.facebook.com/groups/1998697690143140', '170,636 (Nov 9)', 'Local only. No rule about selling', 'Be a neighbor', 'Signed-in check, Nov 9'),
    (3, 'Antique Lighting Collectors', 'https://www.facebook.com/groups/antiquelightingcollectors', '50,241 (Nov 9)', 'Selling OK, at most 1 item a day, and only if you also join the talk. Vintage through the 1970s', 'Lamps', 'Signed-in check, Nov 9'),
    (4, 'Quirky Groovy Vintage Buy/Sell/Trade', 'https://www.facebook.com/groups/497230079689590', '74.9K (Nov 9)', 'Paid seller subscription. PayPal or Venmo goods and services. Ship within 5 business days. Rejects profiles with no photo or few friends', 'Sales. Join last', 'Logged-out preview, Nov 9'),
    (5, 'Maximalist Design and Decor', 'https://www.facebook.com/groups/4123980350957973', '1,695,318 (Nov 9)', 'No sales, no self-promotion, no links or brand names', 'Audience only', 'Signed-in check, Nov 9'),
    (6, 'Thrifted Home Decor & More', 'https://www.facebook.com/groups/780950867281666', '73.6K (Nov 9)', 'No selling or promotion', 'Audience only', 'Logged-out preview, Nov 9'),
    (7, 'Ooh La La! 1963-1990s Vintage Hive Mind BST', 'https://www.facebook.com/groups/605944916086419', '12.0K, quiet (Nov 9)', 'Selling OK with the era stated. Photos of front, back and lining', 'Clothes', 'Logged-out preview, Nov 9'),
    (8, 'Cape Coral Community Information', 'https://www.facebook.com/groups/516061361775789', '183.9K (Nov 9)', 'No single-item sales. Business ads Mondays only, with name, address and phone', 'Low priority (the address rule clashes with no showroom)', 'Crawl, Nov 9'),
    ('Skip', 'Vintage Boss Babes', 'https://www.facebook.com/groups/vintagebossbabes', '', '"This content isn\'t available right now"', 'Gone or hidden', 'Signed-in check, Nov 9'),
    ('Skip', 'Ooh La La! 1920-1962', 'https://www.facebook.com/groups/155195171189000', '19.0K', 'Only up to 1962', 'Wrong era', 'Logged-out preview, Nov 9'),
]

SELLERS = [  # name, url, copy this
    ('Time Warp Boutique', 'https://www.ebay.com/str/timewarpboutique', 'Dress form on white, with a round label close-up inset'),
    ('Curated Estate Vintage', 'https://www.ebay.com/str/resaledivafinds', 'Cut-out on a form, white background; designer tier; only 8 categories'),
    ('vintagemartinidallas', 'https://www.ebay.com/str/martiniconsignment', 'Store categories by decade and designer'),
    ('Jade Design Vintage Clothing', 'https://www.ebay.com/str/vintageclothingonline', 'Titles: brand, type, size early, era last'),
    ('The Old Above', 'https://www.ebay.com/str/theoldabove', 'A Store category named "Hollywood Regency"; categories by room'),
    ('Classic Brass Lighting', 'https://www.ebay.com/str/classicbrasslighting', 'White-background lamp pairs, at our scale (59 sold)'),
    ('Malena\'s Vintage Boutique', 'https://www.ebay.com/str/malenasvintageboutique', 'Story-led About; featured by eBay'),
    ('american archive', 'https://www.ebay.com/str/americanarchive', 'Dress categories by decade; storewide-discount banner'),
    ('oddmidmod', 'https://www.ebay.com/str/oddmidmod', 'Category tree for decor, lighting and art; lamps shot switched on'),
    ('Vintage Icon Vault', 'https://www.ebay.com/str/authenticdesignercollections', 'Bags; "ships within 24 business hours" in the About'),
]

def write_todo(path):
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.worksheet.datavalidation import DataValidation
    wb = Workbook()
    head = Font(name='Arial', bold=True, color='FFFFFF'); fill = PatternFill('solid', fgColor='451C2B')
    phasefill = PatternFill('solid', fgColor='F5EBD9'); body = Font(name='Arial', size=10)
    wrap = Alignment(wrap_text=True, vertical='top')
    def sheet(ws, headers, rows, widths, link_col=None):
        ws.append(headers)
        for c in ws[1]: c.font, c.fill, c.alignment = head, fill, wrap
        for r in rows: ws.append(list(r))
        for row in ws.iter_rows(min_row=2):
            for c in row:
                c.font, c.alignment = body, wrap
                if isinstance(c.value, str) and c.value.startswith('http'):
                    c.hyperlink = c.value; c.font = Font(name='Arial', size=10, color='1155CC', underline='single')
        for i, w in enumerate(widths): ws.column_dimensions[chr(65 + i)].width = w
        ws.freeze_panes = 'A2'
    ws = wb.active; ws.title = 'To-do (in order)'
    rows = [(n, ph, task, who, needs, link, when, 'To do', notes) for n, (ph, task, who, needs, link, when, notes) in enumerate(TODO, 1)]
    sheet(ws, ['#', 'Phase', 'Task', 'Who', 'Do # first', 'Link or file', 'When', 'Status', 'Notes'], rows, [5, 24, 60, 18, 10, 34, 12, 11, 40])
    dv = DataValidation(type='list', formula1='"To do,Doing,Done,Skipped"', allow_blank=True)
    ws.add_data_validation(dv); dv.add(f'H2:H{len(rows) + 1}')
    prev = None
    for row in ws.iter_rows(min_row=2):
        if row[1].value != prev:
            for c in row: c.fill = phasefill
            prev = row[1].value
    sheet(wb.create_sheet('FB Pages to like'), ['Page', 'Link', 'Why', 'Source'], PAGES, [40, 55, 55, 28])
    sheet(wb.create_sheet('FB groups in order'), ['Order', 'Group', 'Link', 'Members', 'Selling rules', 'Use', 'Checked'], GROUPS, [7, 36, 50, 18, 60, 24, 24])
    sheet(wb.create_sheet('eBay sellers to study'), ['Seller', 'Link', 'Copy this'], SELLERS, [30, 50, 70])
    wb.save(path)

def write_snapshot(path):
    lines = ['# Launch to-do (snapshot of the Drive workbook as first written, 2026-11-09)', '',
             'The live copy, with statuses, is `00 To-do list (in order).xlsx` in the allstatecoop@gmail.com Drive, under `My Drive/Holliewood Launch`. '
             'The rows come from `tools/launch-drive-export.py`. This file is not updated when tasks get ticked in Drive.', '',
             '| # | Phase | Task | Who | Do # first | When |', '|---|---|---|---|---|---|']
    for n, (ph, task, who, needs, link, when, notes) in enumerate(TODO, 1):
        lines.append(f'| {n} | {ph} | {task.replace("|", "/")} | {who} | {needs} | {when} |')
    open(path, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')

NOTE = """Where the eBay working files are (they stay where they are)

My Drive/Holliewood eBay/Items          one folder per item: Photoroom photos plus listing.txt
My Drive/Holliewood eBay/Shop setup     footer, templates, customer replies, logo and billboard
My Drive/Holliewood eBay/Holliewood eBay batch 2026-11-08 - fill in.xlsx   measurements workbook

The plan and research for growing a following are in this folder. The ordered to-do list is
"00 To-do list (in order).xlsx" one folder up.
"""

if __name__ == '__main__':
    for src, rel in DOCS:
        md_to_docx(os.path.join(ROOT, src), os.path.join(OUT, rel))
        print('docx', rel)
    open(os.path.join(OUT, 'eBay', 'Where the eBay item files are.txt'), 'w', encoding='utf-8').write(NOTE)
    todo = os.path.join(OUT, '00 To-do list (in order).xlsx')
    if FORCE_TODO or not os.path.exists(todo):
        write_todo(todo); print('xlsx', todo)
    else:
        print('kept existing to-do (pass --todo to overwrite):', todo)
    write_snapshot(os.path.join(ROOT, 'docs', 'launch-todo.md'))
    # self-check: dependencies point backwards
    for n, row in enumerate(TODO, 1):
        for d in re.findall(r'\d+', row[3]):
            assert int(d) < n, (n, d)
    print('ok', len(TODO), 'tasks')
