![banner icon](https://medusajs.com/_next/image?url=https%3A%2F%2Fassets.medusajs.com%2Fcdn-cgi%2Fimage%2Fwidth%3D128%2Cquality%3D82%2Cformat%3Dauto%2Cfit%3Dcontain%2Fuploads%2F2026%2F09%2Fsearch-icon-options-selection-2-e2ikmqx9.webp&w=128&q=75)[Announcing Medusa Search: A built-in search engine for your Medusa store](https://medusajs.com/search)
[](https://medusajs.com/ "Home")
  * Product
  * Resources
  * [Enterprise](https://medusajs.com/enterprise)
  * [Pricing](https://medusajs.com/pricing)
  * [Documentation](https://docs.medusajs.com)


[](https://github.com/medusajs/medusa)
View demo
  * [Medusa AdminExplore our commerce merchant dashboard](https://demo.medusajs.com/app/login?demo-user=true)
  * [Medusa CloudExplore our batteries-included hosting platform](https://demo.cloud.medusajs.com)


[Start for free](https://cloud.medusajs.com/signup)
  * [Commerce](https://medusajs.com/modules)
  * [Framework](https://medusajs.com/framework)
  * [Admin](https://medusajs.com/admin)
  * [Starters](https://medusajs.com/starters)
  * [Integrations](https://medusajs.com/integrations)
  * [Storefront & backend hosting](https://medusajs.com/cloud)
  * [Autoscaling](https://medusajs.com/cloud#scale)
  * [Previews](https://docs.medusajs.com/cloud/environments/preview)
  * [Pre-production environments](https://docs.medusajs.com/cloud/environments/long-lived)
  * [Cache](https://docs.medusajs.com/cloud/cache)
  * [Emails](https://docs.medusajs.com/cloud/emails)
  * [RBAC, SSO](https://medusajs.com/enterprise)
  * [Search](https://medusajs.com/search)
  * [Quickstart](https://docs.medusajs.com)
  * [MCP server](https://docs.medusajs.com/learn/introduction/build-with-llms-ai/mcp-server)
  * [Skills](https://docs.medusajs.com/learn/introduction/build-with-llms-ai/agentic-skills)
  * [Cloud CLI](https://docs.medusajs.com/cloud/cli)
  * [Platform migration](https://docs.medusajs.com/learn/introduction/build-with-llms-ai/mcp-server/migrate-from-shopify)
  * [B2C](https://medusajs.com/b2c)
  * [B2B](https://medusajs.com/b2b)
  * [Marketplaces](https://medusajs.com/marketplace)
  * [Distributors](https://medusajs.com/distributors)
  * [Blog](https://medusajs.com/blog)
  * [Case studies](https://medusajs.com/blog?filters=User+stories)
  * [User guides](https://docs.medusajs.com/user-guide)
  * [Medusa Experts](https://medusajs.com/experts)
  * [All stories](https://medusajs.com/blog?filters=User+stories)
  * [Documentation](https://docs.medusajs.com)
  * [Changelog](https://medusajs.com/changelog)
  * [Open-source repository](https://github.com/medusajs/medusa)
  * [Community](https://discord.com/invite/medusajs)
  * [Blog](https://medusajs.com/blog/how-we-built-the-medusa-mcp)


![banner icon](https://medusajs.com/_next/image?url=https%3A%2F%2Fassets.medusajs.com%2Fcdn-cgi%2Fimage%2Fwidth%3D128%2Cquality%3D82%2Cformat%3Dauto%2Cfit%3Dcontain%2Fuploads%2F2026%2F09%2Fsearch-icon-options-selection-2-e2ikmqx9.webp&w=128&q=75)[Announcing Medusa Search: A built-in search engine for your Medusa store](https://medusajs.com/search)
[](https://medusajs.com/)
View demo
  * [Medusa AdminExplore our commerce merchant dashboard](https://demo.medusajs.com/app/login?demo-user=true)
  * [Medusa CloudExplore our batteries-included hosting platform](https://demo.cloud.medusajs.com)


[Start for free](https://cloud.medusajs.com/signup)
[Overview](https://medusajs.com/integrations)
![Icon for Etsy Product Sync](https://medusajs.com/_next/image?url=https%3A%2F%2Fassets.medusajs.com%2Fcdn-cgi%2Fimage%2Fwidth%3D128%2Cheight%3D128%2Cquality%3D82%2Cformat%3Dauto%2Cfit%3Dcover%2Fuploads%2F2026%2F07%2Fjytextiles-medusa-plugin-etsy-sync-icon-l8kzfb23.webp&w=128&q=75)
# Etsy Product Sync
List and update Etsy products from your Medusa store
## @jytextiles/medusa-plugin-etsy-sync
A [Medusa v2](https://medusajs.com) plugin that syncs your Medusa products to a personal [Etsy](https://www.etsy.com) shop via the [Etsy Open API v3](https://developers.etsy.com/documentation). It handles the OAuth2 (PKCE) connect flow, draft-listing creation, listing updates, image uploads, and keeps a per-product sync record so you can publish to Etsy from the Medusa Admin.
## Features
  * **OAuth2 PKCE connect flow** — connect/disconnect an Etsy shop from **Settings → Etsy** in the Admin; tokens are stored and auto-refreshed.
  * **Product → Etsy sync** — create draft listings, update them, and upload product images (single or bulk).
  * **Readiness checks** — surfaces what's missing (shop connection, shipping profile, return policy, taxonomy) before you publish.
  * **Sync records** — every sync is tracked per product with status and the remote Etsy listing id.
  * **Scheduled token refresh** — a background job keeps the Etsy access token fresh so syncs don't fail mid-session.


## Requirements
  * Medusa **2.17.x**
  * Node.js **> = 22**
  * An Etsy app (keystring + shared secret) from the [Etsy developer portal](https://www.etsy.com/developers/your-apps)


## Install

```


12345




npm install @jytextiles/medusa-plugin-etsy-sync



# or



yarn add @jytextiles/medusa-plugin-etsy-sync



# or



pnpm add @jytextiles/medusa-plugin-etsy-sync




```

## Configure
Register the plugin in Copy to clipboard`medusa-config.ts`:

```


1234567891011121314151617




module.exports = defineConfig({




  // ...




  plugins: [




    {




      resolve: "@jytextiles/medusa-plugin-etsy-sync",




      options: {




        keystring: process.env.ETSY_KEYSTRING,




        sharedSecret: process.env.ETSY_SHARED_SECRET,




        redirectUri:




          process.env.ETSY_REDIRECT_URI ??




          "http://localhost:9000/app/settings/oauth/etsy/callback",




        scope:




          process.env.ETSY_SCOPE ?? "listings_r listings_w listings_d shops_r",




      },




    },




  ],




})




```

Options can be supplied via the Copy to clipboard`options` object above **or** the matching environment variables (env takes precedence):
Option Env var Required Description Copy to clipboard`keystring` Copy to clipboard`ETSY_KEYSTRING` yes Your Etsy app's keystring (API key). Copy to clipboard`sharedSecret` Copy to clipboard`ETSY_SHARED_SECRET` yes Your Etsy app's shared secret. Copy to clipboard`redirectUri` Copy to clipboard`ETSY_REDIRECT_URI` no OAuth callback URL. Must match your Etsy app's registered callback. Copy to clipboard`scope` Copy to clipboard`ETSY_SCOPE` no Space-separated Etsy OAuth scopes.
Add the callback URL (Copy to clipboard`redirectUri`) to your Etsy app's allowed redirect URIs in the Etsy developer portal.
After installing, run your project's migrations so the plugin's tables are created:

```

1

npx medusa db:migrate


```

## Usage
  1. In the Admin, go to **Settings → Etsy** and click **Connect** to authorize your Etsy shop.
  2. Configure your sync settings (shipping profile, return policy, taxonomy).
  3. From a product page, use the **Etsy** widget to sync the product, or sync in bulk from the Etsy settings page.


### Admin API routes
Method Route Purpose GET Copy to clipboard`/admin/etsy/status` Connection + readiness status GET / POST Copy to clipboard`/admin/etsy/settings` Read / save sync settings GET Copy to clipboard`/admin/etsy/auth/authorize` Start the OAuth2 PKCE flow GET Copy to clipboard`/admin/etsy/auth/callback` OAuth2 callback POST Copy to clipboard`/admin/etsy/auth/disconnect` Disconnect the shop POST Copy to clipboard`/admin/etsy/sync/product/:id` Sync a single product POST Copy to clipboard`/admin/etsy/sync/bulk` Sync multiple products GET Copy to clipboard`/admin/etsy/syncs` List sync records GET Copy to clipboard`/admin/etsy/taxonomy` Etsy taxonomy lookup GET Copy to clipboard`/admin/etsy/shipping-profiles` Etsy shipping profiles GET Copy to clipboard`/admin/etsy/return-policies` Etsy return policies
## Development

```


1234567891011




# Build the plugin (compiles to .medusa/server)



npm run build







# Watch mode while developing against a local Medusa app



npm run dev






# Generate a migration after changing a model



npm run db:generate







# Run tests


npm run test



```

## License
MIT
Built by
Jaal Yantra Textiles
Version
0.1.6
Category
Other
Downloads
1.1K monthly
Last updated
a month ago
[View source](https://github.com/Jaal-Yantra-Textiles/v2.git)[View on NPM](https://www.npmjs.com/package/@jytextiles/medusa-plugin-etsy-sync)
## You may also like
[Browse all integrations ](https://medusajs.com/integrations)
[ ![Icon for Product Reviews](https://assets.medusajs.com/uploads/2025/07/products-reviews-logo-604i9gz0.svg) Product Reviews By Lambda Curry Add ratings, reviews, and moderation to products 5.2K/mo](https://medusajs.com/integrations/lambdacurry-product-reviews)[ ![Icon for Wishlist](https://assets.medusajs.com/uploads/2025/07/wishlist-logo-kvp1hbj3.svg) Wishlist By Alphabite Let guests and users set up wishlists 4.3K/mo](https://medusajs.com/integrations/alphabite-wishlist)[ ![Icon for Reorder](https://assets.medusajs.com/uploads/2026/07/image-54-v1ra9nx7.svg) Reorder By Reorder Add subscriptions and recurring billing 3.6K/mo](https://medusajs.com/integrations/@reorderjsreorder)
Build your own
## Develop your own custom integration
Build your own integration with our API to speed up your processes. Make your integration available via npm for it to be shared in our Library with the broader Medusa community.
![payment icon](https://medusajs.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fpayment-icon.2bf8672f.png&w=48&q=75)![cart icon](https://medusajs.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcart-icon.3b504a3f.png&w=48&q=75)![gift icon](https://medusajs.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgift-icon.ebd226c4.png&w=48&q=75)
[Get started](https://docs.medusajs.com/resources/integrations)
![gift card interface](https://medusajs.com/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgift-card-image.e15f2dbb.png&w=3840&q=95)
## Ready to build your custom commerce setup?
[Start now](https://cloud.medusajs.com/signup)
[](https://medusajs.com/ "Home")
  * Product
  * [Starters](https://medusajs.com/starters)
  * [Admin](https://medusajs.com/admin)
  * [Modules](https://medusajs.com/modules)
  * [Framework](https://medusajs.com/framework)
  * [Cloud](https://medusajs.com/cloud)
  * [Integrations](https://medusajs.com/integrations)


  * Solutions
  * [Enterprise](https://medusajs.com/enterprise)
  * [Medusa Experts](https://medusajs.com/experts)
  * [User Stories](https://medusajs.com/blog?filters=User+stories)
  * [B2B](https://medusajs.com/b2b)
  * [B2C](https://medusajs.com/b2c)
  * [Marketplace](https://medusajs.com/marketplace)
  * [Distributors](https://medusajs.com/distributors)


  * Agent tools
  * [Medusa MCP](https://docs.medusajs.com/learn/introduction/build-with-llms-ai/mcp-server)
  * [Agentic guide](https://docs.medusajs.com/learn#get-started-with-ai-agents)
  * [Cloud CLI](https://docs.medusajs.com/cloud/cli)
  * [Agent Skills](https://docs.medusajs.com/learn/introduction/build-with-llms-ai/agentic-skills)
  * [Preview Environments](https://docs.medusajs.com/cloud/environments/preview)
  * [Medusa Development Agent](https://docs.medusajs.com/cloud/deployments/fix-with-ai)


  * Developers
  * [Documentation](https://docs.medusajs.com)
  * [Agentic development](https://docs.medusajs.com/learn/introduction/build-with-llms-ai)
  * [Recipes](https://docs.medusajs.com/resources/recipes)
  * [Changelog](https://medusajs.com/changelog)
  * [Community](https://discord.com/invite/medusajs)
  * [Blog](https://medusajs.com/blog)


  * Other
  * [Pricing](https://medusajs.com/pricing)
  * [Blog](https://medusajs.com/blog)
  * [Contact](https://medusajs.com/contact)


Newsletter
Leave this field empty
Subscribe
Get the latest product news and behind the scenes updates. Unsubscribe at any time.
  * [](https://discord.gg/medusajs "Discord")
  * [](https://twitter.com/medusajs "Twitter")
  * [](https://www.linkedin.com/company/medusajs "LinkedIn")
  * [](https://github.com/medusajs/medusa "GitHub")



