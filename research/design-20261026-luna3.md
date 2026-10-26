# Category tile design references — Luna 3

Date: 2026-10-26

## Primary pages crawled with crawl4ai

- [YOWIE](https://www.shopyowie.com/) — `research/yowie-design-20261026-luna3.md`
- [Coming Soon New York](https://comingsoonnewyork.com/) — `research/comingsoon-design-20261026-luna3.md`

## Visual observation and application

Observed YOWIE's homepage at desktop width, including its hero and Collections section. The Collections section has a heading and an "Explore All" link sharing one line above a three-column grid. Cards have portrait-ish consistent frames with narrow gutters; every tile anchors its label to the same upper-left inset. The photo changes subject (embroidered cap, bread on a textile, stacked ceramic cups, jewelry), while a subdued dark treatment keeps light text readable. The two hero panels above are much larger, with category title, short description, and CTA toward the lower-left. Coming Soon's crawl exposes a broad set of named decor/tabletop/furniture collections with individual editorial collection-photo URLs; I did not visually inspect its category grid, so no visual claims are based on that source.

### Three concrete lessons for Hollywood and Vine's four tiles

1. **Make the four images feel like one set:** put all four in the same fixed-aspect frame and use a consistent `object-fit: cover` crop. Use varied, real shop photography (for example fashion, objects, art, and print) inside those frames. YOWIE shows diverse subjects but keeps the same card proportions, which lets the product imagery carry variety without making the grid feel uneven.
2. **Give the grid breathing room and a clear section boundary:** use a heading row above a 2×2 desktop grid, with a modest outer inset and even gutters (roughly 16–20 px is a sensible starting point for this site). YOWIE's “Collections / Explore All” row reads separately from the image cards; its cards have small, consistent gaps rather than touching.
3. **Keep the title placement consistent and legible over photographs:** choose one inset and one anchor (upper-left like YOWIE's collection cards, or lower-left like its hero panels) and repeat it for all four. Add a restrained dark overlay or localized text backing when an image is bright or busy; don't alter photos to force the contrast.

Source URLs: https://www.shopyowie.com/ · https://comingsoonnewyork.com/
