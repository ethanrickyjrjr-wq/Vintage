# d7 fallback captures (WebFetch / WebSearch), accessed 2026-10-29

These are NOT crawl4ai captures. WebFetch returns a small-model summary of a page; WebSearch returns result snippets. Treat as lower grade than a crawl. Quotes below are copied from the tool output.

## 1. Emily Henderson, "How much it really costs to work with a designer" (WebFetch x3; crawl4ai walled at 517 bytes, see d7-emily-henderson-cost.md)
URL: https://stylebyemilyhenderson.com/how-much-it-really-costs-to-work-with-a-designer
Byline per WebFetch: "By Velinda Hellen". Date per WebFetch: "Jan 15" (no year visible). Page text 150,301 chars; WebFetch read chars 0-100,000 only.
Quotes returned:
- "The total amount of time I've spent on the design process (so far) is right at 80 hours."
- "That's prior to installation services, which will likely add another 10 or so."
- "That also doesn't include the 55 hours spent on blog content for the project"
- "Believe it or not, 90 hours isn't that long."
- "Given we designed three small rooms; living, dining, and TV, plus knocked out a custom cabinet design"
- "to take 35-50 hours and span the course of up to 8 or 9 months" (single-room full-service; fragment as returned)
- "easily spending close to $6,000 per room for a full, designer-done makeover"
- "Using our current EHD friends & family rate of $75/hour"; "designers charging hourly typically average between $100-200/hour"; "'High End' interior designers or decorators are charging $200-300/hr"; "The mean (or average) rate of people polled was $182/ hr."
- Reader comment: "I believe I paid $1300 for 10 hours of her time."

## 2. Wadhwa & Zhang 2015 (WebFetch of https://academic.oup.com/jcr/article-abstract/41/5/1172/2962090)
Citation as returned: Monica Wadhwa and Kuangjie Zhang, "This Number Just Feels Right: The Impact of Roundedness of Price Numbers on Product Evaluations," Journal of Consumer Research 41(5), 2015, pp. 1172-1185.
Short excerpts returned: "rounded prices (e.g., $200.00) encourage reliance on feelings." and "the first research examining the differential impact of roundedness of prices on product purchase." (WebFetch declined to give the full abstract; crawl4ai got 0 bytes from OUP and PsycNET.)

## 3. NBER w24306 PDF
crawl4ai returned 4 bytes for the PDF URL. WebFetch could not read the compressed PDF but saved the binary to d7-nber-w24306.pdf; text extracted locally with pdftotext -layout -> d7-nber-w24306-text.txt. Numbers quoted in the report come from that text file. The NBER abstract page crawl is d7-nber-w24306.md.

## 4. WebSearch snippets (no page read)
- Query: vintage shop weekly price drop. Snippet: "Furnish Green (vintage furniture, Monday markdowns): The store reviews its prices weekly and lowers a handful of pieces each Monday. On average, they lower 5-7 pieces every Monday, and they are not necessarily items that have been in the showroom for a long time." Source URL given: https://old.furnishgreen.com/?p=72440 . crawl4ai of that URL returned a maintenance page (d7-furnishgreen-monday.md); furnishgreen.com returned HTTP 429 to WebFetch. UNVERIFIED.
- Query: e-design hours. Snippet summary: "I didn't find a designer who states how many hours one e-design room takes." (so a published hours-per-room figure was not found by WebSearch either.)
- Query: layaway. Snippet summary: deposits 15% to 50%, payoff windows from weeks to six months; "no vintage furniture or lamp shop with a published layaway policy in these results." The four layaway pages in the report were then crawled directly.
- Query: Etsy layaway. Snippet summary: "no official Etsy Help Center article on layaway"; community threads (not read) say reserved listings can backfire and one poster claims deposit listings break Etsy's terms. UNVERIFIED, community claims.
