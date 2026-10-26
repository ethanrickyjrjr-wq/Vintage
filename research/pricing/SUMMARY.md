# Hollywood and Vine — price targets, first pass (2026-10-26)

Live sample storefront: https://claude.ai/artifact/GpqV98vZ4hLe4haSop78E6 (page source: `site/storefront.html`, images from `assets/`).
Targets are list prices in USD. "low–high" is the comp spread. Sources: `lighting.md`, `decor.md`, `art.md`, `print.md`, `fashion.md`
(Sonnet subagents; eBay and Etsy walled them, so most are ASKING prices or Poshmark SOLD) and `ebay-sold.md` (eBay SOLD, first page, read
through Ricky's signed-in Chrome for the items marked "eBay sold").

| id | item | target | low–high | confidence | basis |
|---|---|---|---|---|---|
| A1 | Stiffel-style brass + cream urn lamp | $95 | 45–150 | med | eBay sold; $120+ if Stiffel-stamped |
| A2 | Sea-glass tiered chandelier (tag $60) | $125 | 75–225 | low | no comps, judgment |
| A13 | Gold bust lamp | $110 | 75–165 | low | judgment |
| A17 | Brass hurricane oil lamps, pair | $85 | 55–135 | low | judgment |
| A16 | Retro turntable | $55 | 35–80 | low | if it plays |
| A9 | 8mm projector | $45 | 30–65 | low | untested |
| A14 | Ceramic leopard | $125 | 45–345 | med | eBay sold; Italy mark lifts it |
| A10 | Pink stemware, 12 pieces | $110 | 50–120 | med | eBay sold, $52–60 per 6 |
| A11 | Black + gold cocktail shaker | $28 | 18–40 | low | asking |
| A12 | Cut crystal decanter | $42 | 25–65 | low | asking |
| A15 | Black armchair, star cushion | $165 | 95–250 | low | asking |
| A20 | White ribbed chair | $275 | 175–1,150 | low | **check for Vitra / Easy Edges label: Gehry Wiggle = $700–1,150** |
| A22 | Paint-splattered dress form | $245 | 150–350 | low | asking |
| A8 | Silver busts, pair | $150 | 90–220 | low | asking |
| A19 | Cowhide throw | $110 | 70–160 | med | if stock, not staging |
| A5 | Elvis 8x10 signed Moore + Fontana | $140 | 60–200 | med | eBay sold $60–166; $250+ with JSA |
| A3 | Cubist acrylic on canvas | $275 | 150–450 | low | asking |
| A4 | Ink-and-wash face, framed | $140 | 75–225 | low | asking |
| A23 | Sneaker-leather collar art | $185 | 95–300 | low | judgment |
| C1 | Playboy Jan 1997 Marilyn | $14 | 6–25 | high | 90 eBay sold |
| C2 | Playboy Apr 1991 | $12 | 6–18 | high | eBay sold |
| C3 | Playboy Dec 1989 (Bergen) | $7 | 5–12 | med | asking |
| C4 | Playboy Jan 1970, worn | $10 | 6–18 | med | asking |
| C5 | Penthouse Sep 1977 | $14 | 8–30 | high | eBay sold |
| C6 | Midnight Playmates (1990) | $10 | 6–15 | med | asking |
| C7 | Southern Peach 2016-17 | $4 | — | low | judgment |
| C8 | Chanel book (title unconfirmed) | $20 | 12–35 | low | asking |
| B1 | Blush faux-leather trench | $58 | 35–85 | med | Poshmark sold |
| B5 | Paisley jacket | $48 | 30–70 | med | Poshmark sold |
| B6 | Feather cocktail hat | $48 | 25–75 | med | eBay + Poshmark sold |
| B7 | Leather chain harness belt | $48 | 30–70 | med | Poshmark sold |
| B9 | Gray fringed western boots | $48 | 30–70 | med | Poshmark sold |
| B10 | Neon colourblock windbreaker | $35 | 20–50 | med | eBay + Poshmark sold |
| B11 | Gold chain necklaces, set of 3 | $28 | — | med | Poshmark sold |
| B12 | Navy shirt dress, cream collar | $42 | 28–60 | med | Poshmark sold |
| B13 | Red lace dress | $32 | 20–45 | low | Poshmark sold |
| B14 | Neon track jacket + paisley leggings | $50 | 34–65 | med | $34 + $16 |
| B15 | Colourblock blouse / red embroidered jacket | $24 / $40 | — | low | Poshmark sold |
| B18 | Shoes, per pair | $14–26 | — | med | Poshmark sold |
| — | The owner, mirror selfie | $10,000,000 | firm | — | not for sale |

Sum of targets, everything except the selfie and fixtures: about $3,200 (A20 at $275).
