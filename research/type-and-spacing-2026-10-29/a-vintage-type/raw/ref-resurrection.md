# SOURCE: https://resurrectionvintage.com/
# Method: curl of the homepage HTML + up to 8 linked stylesheets (crawl4ai markdown strips CSS, so it cannot show fonts), fetched 2026-10-29T05:29:22Z, Chrome UA. Values are DECLARED in CSS/theme variables, not measured from a rendered page. px tracking converted to em = px / font-size px.

## page meta
<meta property="og:title" content="Resurrection Vintage Clothing
<meta property="og:description" content="Resurrection Vintage is the world&#39;s premier international source for luxury designer vintage, collectible clothing, archival fashion, and historical costume. Resurrection Los Angeles and Resurrection Fashion Archive offer curated collections of clothing, a
<meta property="og:site_name" content="Resurrection
<title>Resurrection Vintage Clothing</title>

## font vars and @font-face
--heading-font-family: Jost, sans-serif
--heading-font-weight: 500
--heading-text-transform: uppercase
--heading-letter-spacing: 0.15em
--text-font-family: Jost, sans-serif
--text-font-weight: 500
--text-letter-spacing: 0.0em
--button-text-transform: uppercase
--button-letter-spacing: 0.18em
--text-xs: 0.8125rem
--text-sm: 0.875rem
--text-base: 0.9375rem
--heading-letter-spacing: 0
@font-face { font-family: Jost; font-weight: 500; font-style: italic; font-display: fallback }
@font-face { font-family: Jost; font-weight: 700; font-style: normal; font-display: fallback }
@font-face { font-family: Jost; font-weight: 700; font-style: italic; font-display: fallback }

## component rules
.badge--on-sale {  }
.badge--sold-out {  }
.badge--custom {  }

## notes (mine)
--text-base .9375rem = 15px (same as this site's body). Headings: Jost 500, uppercase, tracking .15em declared in :root; one component (countdown flip) overrides to 0 -- the base value is .15em. Buttons uppercase .18em. Badge .625rem (10px) uppercase. Announcement bar .625rem.
