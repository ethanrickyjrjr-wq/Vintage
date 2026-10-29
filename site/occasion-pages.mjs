// One shared layout; each occasion supplies its own opening scene and copy.
export const occasions = [
  {
    slug: "cocktail-hour", name: "Cocktail hour", accent: "#f3ce83",
    headline: "A little shaken. Very well styled.",
    description: "The ice clinks. The pink coupes catch the light. That brass bar cart? Already the most interesting guest in the room. Imagine a little corner that turns ‘just one drink’ into everybody’s favorite part of the evening.",
    alt: "Vintage brass bar cart with pink coupe glasses, a crystal decanter and a fringed lamp against a burgundy wall",
  },
  {
    slug: "dinner-party", name: "Dinner party", accent: "#f8d58a",
    headline: "Set the table. Start something.",
    description: "Candlelight in the pink glass. Brass between the flowers. Six chairs, no one in a hurry to leave. Picture a table with as much personality as the people around it, where the second bottle opens and the good stories come out.",
    alt: "Dinner table set for six with pink and green vintage glassware, brass candlesticks, plum linen and flowers",
  },
  {
    slug: "the-party", name: "The party", accent: "#f3a58e",
    headline: "Your place. Everybody’s favorite night.",
    description: "The lamps are low, the glasses don’t match, and somehow everyone ends up in that one fabulous corner. A birthday, a housewarming, absolutely no reason at all. Give the room a little main-character energy and let the evening take it from there.",
    alt: "Home lounge ready for a party with a burgundy sofa, brass coffee table, colorful glasses, flowers and metallic balloons",
  },
  {
    slug: "disco-night", name: "Disco night", accent: "#f7b8df",
    headline: "The dance floor is your living room.",
    description: "One mirror ball. A room full of little stars. The records are out, the velvet is glowing, and the coffee table has politely stepped aside. New Year’s, an awards night, a Tuesday with potential. Dress the room like the night might become a story.",
    alt: "Silver disco ball casting reflections around a burgundy living room with a pink velvet sofa and a record player",
  },
  {
    slug: "bachelorette", name: "Bachelorette", accent: "#f2b1d0",
    headline: "For the bride. And the group chat.",
    description: "Pink coupes lined up. Champagne on ice. A velvet little photo moment that makes everybody say ‘wait, one more.’ Imagine the house dressed for your favorite people, with vintage glamour, a wink of disco, and a guest of honor who gets all the good light.",
    alt: "Bachelorette lounge with a pink velvet loveseat, champagne, six pink coupes, roses, satin bows and small disco balls",
  },
  {
    slug: "proposal", name: "Proposal", accent: "#ffd7c1",
    headline: "Before the yes, set the scene.",
    description: "The familiar room, suddenly a little magical. Roses in old glass, candlelight on brass, two beautiful places to sit close. A setting that feels like the two of you, so when the question comes, everything around it already feels right.",
    alt: "Romantic home corner at dusk with two velvet chairs, roses, champagne coupes, candles and a small velvet ring box",
  },
  {
    slug: "photo-set", name: "Photo set", accent: "#f8d58a",
    headline: "Good light. A very good backdrop.",
    description: "A velvet curve, an outrageous painting, a mirror that knows its angles. Picture a corner with a point of view, ready for portraits, a creative shoot, or the best photo you’ve taken of yourself in years. You bring the look. Hollie dresses the set.",
    alt: "Editorial portrait corner with a blush velvet chair, cubist painting, ornate gold mirror and sculptural brass lamp",
  },
  {
    slug: "after-the-remodel", name: "After the remodel", accent: "#c6d9bc",
    headline: "The walls are done. Now the good part.",
    description: "Fresh paint, beautiful floors, and a room still waiting to feel like you. Now picture the lamp with a past, the art you can’t stop looking at, the chair nobody else has. A few well-cast vintage pieces, and suddenly the new room has a whole life of its own.",
    alt: "Freshly finished living room layered with a vintage rug, brass lamp, moss green chair, collected art and a sea-glass chandelier",
  },
  {
    slug: "guest-room", name: "Guest room", accent: "#efc690",
    headline: "Five-star welcome. Zero checkout time.",
    description: "A brass bed, a soft quilt, a little flower by the lamp. The kind of room that makes ‘just for the weekend’ sound negotiable. Imagine a guest room with boutique-hotel charm and the warmth of someone who’s very happy you came.",
    alt: "Welcoming guest bedroom with a vintage brass bed, blush bedding, sea-glass bedside tables and warm brass lamps",
  },
  {
    slug: "spare-room", name: "Spare room", accent: "#d0bce8",
    headline: "That extra room? It has range.",
    description: "Right now it’s the room with the things. Imagine it with a pink loveseat, a place to make something, a record playing in the corner. A little retreat, a creative hideaway, a room you actually choose to spend time in. Potential looks very good in velvet.",
    alt: "Small creative retreat with a pink vintage loveseat, writing table, green velvet chair, gallery art and a record player",
  },
  {
    slug: "home-office", name: "Home office", accent: "#c3dce4",
    headline: "A promotion for your surroundings.",
    description: "The desk has curves. The lamp has presence. The background gets compliments before you’ve said hello. Picture a home office with enough character to make Monday feel a little more like you, and a chair you’re happy to come back to.",
    alt: "Home office with a vintage burl wood desk, green velvet chair, brass desk lamp and framed art on a burgundy wall",
  },
  {
    slug: "snowbird-season", name: "Snowbird season", accent: "#b4e1d3",
    headline: "Touch down. Settle into fabulous.",
    description: "The curtains catch the sunshine. The rattan chair has your name on it. A little sea glass, a beautiful lamp, and a room that feels like the season you’ve been waiting for. Imagine arriving to a Florida home with warmth, personality, and absolutely no rush.",
    alt: "Sunny Florida condo with vintage rattan chairs, blush cushions, sea-glass vases, palm foliage and collected paintings",
  },
  {
    slug: "reading-nook", name: "Reading nook", accent: "#ffe1ab",
    headline: "Just one more chapter. Obviously.",
    description: "A velvet chair that gets you. A lamp that makes the page glow. A little table with room for tea and absolutely no urgent plans. Picture your own delicious corner of the house, made for disappearing into a book and staying a little longer.",
    alt: "Cozy reading nook with a moss green velvet armchair, blush throw, glowing brass reading lamp, books and a vintage teacup",
  },
  {
    slug: "gift-a-room", name: "Gift a room", accent: "#f5c5d6",
    headline: "Some gifts take up a little more room.",
    description: "Imagine giving someone their favorite place in the house. The chair they didn’t know they needed. The lamp that makes evenings feel softer. A whole little scene that says ‘I know you,’ every time they walk in. That’s a present with staying power.",
    alt: "Thoughtfully styled living room with a pink velvet armchair, brass lamp, flowers and a blush wrapped gift on a side table",
  },
  {
    slug: "something-else", name: "Something else", accent: "#e4df9a",
    headline: "If there’s a plot, there’s a setting.",
    description: "A wildly specific idea. A corner with an identity crisis. A celebration that hasn’t got a name yet. Picture the unexpected piece, the brilliant little clash, the room that could only belong to you. Tell Hollie the story. There’s a scene in it somewhere.",
    alt: "Playful eclectic corner with a gold mirror, zebra-pattern stool, blush curved chair, cobalt glass vase and a small disco ball",
  },
];

const origin = "https://hollywood-and-vine-vintage.allstatecoop.chatgpt.site";
const escape = value => value.replace(/[&<>"']/g, character => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[character]);

export function renderOccasionPage(occasion) {
  const index = occasions.indexOf(occasion);
  const next = occasions[(index + 1) % occasions.length];
  const number = String(index + 1).padStart(2, "0");
  const image = `/assets/occasions/${occasion.slug}.webp`;
  const url = `${origin}/occasions/${occasion.slug}.html`;
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#451c2b" />
  <title>${escape(occasion.name)} styling | Holliewood &amp; Vine</title>
  <meta name="description" content="${escape(occasion.description)}" />
  <meta property="og:title" content="${escape(occasion.name)} | Holliewood &amp; Vine" />
  <meta property="og:description" content="${escape(occasion.headline)}" />
  <meta property="og:image" content="${origin}${image}" />
  <meta property="og:url" content="${url}" />
  <meta property="og:type" content="website" />
  <link rel="canonical" href="${url}" />
  <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
  <link rel="preload" as="font" href="/assets/fonts/bodoni-moda-normal-latin.woff2" type="font/woff2" crossorigin />
  <link rel="preload" as="image" href="${image}" imagesrcset="/assets/occasions/${occasion.slug}--768.webp 768w, ${image} 1536w" imagesizes="(max-width: 800px) 100vw, 60vw" fetchpriority="high" />
  <link rel="stylesheet" href="/assets/fonts/fonts.css" />
  <link rel="stylesheet" href="/occasions.css" />
</head>
<body style="--scene-accent: ${occasion.accent}">
  <a class="skip-link" href="#main">Skip to the occasion</a>
  <header class="occasion-header">
    <a class="wordmark" href="/" aria-label="Holliewood and Vine home">Holliewood <span>&amp; Vine</span></a>
    <nav aria-label="Main navigation">
      <a href="/hire.html#hire-occasions">All occasions <span aria-hidden="true">↗</span></a>
      <a href="/#collection">Shop the collection <span aria-hidden="true">↗</span></a>
    </nav>
  </header>
  <main id="main">
    <div class="scene-breadcrumb page-width">
      <a href="/hire.html">Hire Hollie</a><span aria-hidden="true">/</span><span>${escape(occasion.name)}</span>
      <span class="scene-number">${number} <span aria-hidden="true">/</span> 15</span>
    </div>
    <section class="scene-hero page-width" aria-labelledby="scene-title">
      <div class="scene-copy">
        <p class="eyebrow">Fabulous From Online</p>
        <h1 id="scene-title">${escape(occasion.name)}</h1>
        <p class="scene-headline">${escape(occasion.headline)}</p>
        <p class="scene-description">${escape(occasion.description)}</p>
        <a class="scene-button" href="#your-scene">Make this your scene <span aria-hidden="true">↘</span></a>
        <p class="scene-signoff">You bring the plot. Hollie dresses the set.</p>
      </div>
      <figure class="scene-picture">
        <img src="${image}" srcset="/assets/occasions/${occasion.slug}--768.webp 768w, ${image} 1536w" sizes="(max-width: 800px) 100vw, 60vw" width="1536" height="1024" alt="${escape(occasion.alt)}" fetchpriority="high" />
        <figcaption><span>A little scene-setting.</span> AI-created styling inspiration.</figcaption>
      </figure>
    </section>
    <section class="scene-story page-width" aria-labelledby="story-title">
      <p class="eyebrow">Good taste. A little mischief.</p>
      <h2 id="story-title">Your home. With a little more plot.</h2>
      <div class="scene-story-body">
        <p>A find with a past. A lamp with a glow. The piece that makes your friends ask where you got it. Hollie brings a collector’s eye to the spaces where your life happens.</p>
        <p>A corner, a room, or a reason to celebrate at home. We start with what you love and build a setting that feels like you, on a very good day.</p>
      </div>
    </section>
    <section class="scene-details page-width" id="your-scene" aria-labelledby="details-title">
      <div class="section-intro">
        <div><p class="eyebrow">The next chapter</p><h2 id="details-title">The details, coming into focus.</h2></div>
        <p>There’s more to this scene.<br /> Here’s what’s taking shape.</p>
      </div>
      <div class="scene-placeholders">
        <article class="scene-placeholder"><p class="placeholder-number">01 / The inspiration</p><div class="placeholder-art" aria-hidden="true"><span></span><span></span><span></span></div><h3>The moodboard</h3><p>Colors, textures, and the little things that make the whole room click.</p><span class="coming-soon">Moodboard coming soon</span></article>
        <article class="scene-placeholder"><p class="placeholder-number">02 / The good stuff</p><div class="placeholder-art placeholder-art-details" aria-hidden="true"><span></span><span></span><span></span></div><h3>The finishing touches</h3><p>A closer look at the finds, the styling, and the ways to make it yours.</p><span class="coming-soon">Styling details coming soon</span></article>
        <article class="scene-placeholder"><p class="placeholder-number">03 / Your entrance</p><div class="placeholder-art placeholder-art-booking" aria-hidden="true"><span></span><span></span><span></span></div><h3>A plan for your place</h3><p>Packages, the practical details, and your next step with Hollie.</p><span class="coming-soon">Packages &amp; booking coming soon</span></article>
      </div>
    </section>
    <section class="scene-contact page-width" aria-labelledby="contact-title">
      <p class="eyebrow">Save a little room for fabulous.</p>
      <h2 id="contact-title">Can you picture it at your place?</h2>
      <p>Keep the idea. Start collecting your inspiration.<br />Hollie’s booking line is getting its finishing touches.</p>
      <button class="scene-button" type="button" disabled>Booking opens soon</button>
      <a class="text-link" href="/hire.html">Meet Hollie &amp; explore the styling service <span aria-hidden="true">↗</span></a>
    </section>
    <nav class="scene-explore page-width" aria-label="Explore occasions">
      <div class="section-intro"><h2>Another excuse to be fabulous.</h2><a class="text-link" href="/occasions/${next.slug}.html">Next scene: ${escape(next.name)} <span aria-hidden="true">→</span></a></div>
      <ul>${occasions.map(item => `<li><a href="/occasions/${item.slug}.html"${item === occasion ? ' aria-current="page"' : ""}>${escape(item.name)}</a></li>`).join("\n        ")}</ul>
    </nav>
  </main>
  <footer class="occasion-footer page-width"><a class="wordmark" href="/">Holliewood <span>&amp; Vine</span></a><p>Vintage with a past. Rooms with a future.</p><a href="/hire.html#hire-occasions">Back to all occasions <span aria-hidden="true">↗</span></a></footer>
</body>
</html>
`;
}
