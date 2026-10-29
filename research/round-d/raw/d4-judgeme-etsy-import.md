Copyright (c) 2023, Intercom, Inc. (legal@intercom.io) with Reserved Font Name "Inter". This Font Software is licensed under the SIL Open Font License, Version 1.1.[Skip to main content](https://judge.me/help/en/articles/9813259-importing-reviews-from-etsy-with-a-json-file#main-content)
[![Judge.me Help Center](https://downloads.intercomcdn.com/i/o/z09y8g87/650678/9b0f755aa57123e92d859af2172c/b6dc43419739826af915d5ead0388479.png)](https://judge.me/help/en/)
[Go to Judge.me](https://judge.me)[See latest updates](https://judge.me/unboxed)
[Go to Judge.me](https://judge.me)[See latest updates](https://judge.me/unboxed)
Search for articles...
  1. [All Collections](https://judge.me/help/en/)
  2. [Judge.me Reviews](https://judge.me/help/en/collections/19693690-judge-me-reviews)
  3. [Importing, Exporting & Syncing](https://judge.me/help/en/collections/19731351-importing-exporting-syncing)
  4. [Importing Reviews](https://judge.me/help/en/collections/19736843-importing-reviews)
  5. Importing reviews from Etsy with a JSON file


# Importing reviews from Etsy with a JSON file
August 19, 2026
Table of contents
[How it works](https://judge.me/help/en/articles/9813259-importing-reviews-from-etsy-with-a-json-file#h_c14aaa1b42)[Considerations](https://judge.me/help/en/articles/9813259-importing-reviews-from-etsy-with-a-json-file#h_1dd3dae031)[How to import reviews from Etsy JSON file](https://judge.me/help/en/articles/9813259-importing-reviews-from-etsy-with-a-json-file#h_a4c7bef34c)[Step 1: Export your reviews from Etsy](https://judge.me/help/en/articles/9813259-importing-reviews-from-etsy-with-a-json-file#h_58ac7bd213)[Step 2: Import your reviews to Judge.me](https://judge.me/help/en/articles/9813259-importing-reviews-from-etsy-with-a-json-file#h_054c85b563)
Available on the Free plan
If you have an Etsy store, you can manually export the reviews from your Etsy store and import them to Judge.me.
* * *
# How it works
Here’s a quick look at how importing reviews from Etsy works:
  1. You can export a JSON file of your reviews from Etsy at any time—either as a one-time import of your existing reviews, or whenever you receive new ones.
  2. Upload that JSON file to Judge.me.
  3. Once imported, these Etsy reviews will appear on the corresponding product pages through the installed Judge.me widgets.


* * *
# Considerations
  * If you Etsy's JSON file has more than 2000 reviews, you'd need to split it into smaller files before importing.
  * Etsy’s JSON file doesn’t include any Shopify product identifiers, so we can’t automatically match the reviews to your products. You’ll need to manually assign each review to a product during the import process, which can be time-consuming if you have many reviews or products.
  * Once the reviews from the Etsy JSON file are imported, they can’t be reassigned to a different product. If you need to change the mapping, you’ll have to undo the import and start a new one.
  * Reviews imported from Etsy won't be [verified in Judge.me](https://judge.me/help/en/articles/8376284-verified-reviews) as they don't provide verification data that meets our standards.
  * Imported reviews won’t appear in the Product Ratings feed for Google Shopping, even when they are verified.


To avoid these limitations, we suggest using the [Etsy Sync](https://judge.me/help/en/articles/10713924-syndicate-reviews-from-etsy-to-judge-me-on-shopify) feature, which automatically fetches reviews, supports large volumes, and makes sure the reviews are verified.
* * *
# How to import reviews from Etsy JSON file
## Step 1: Export your reviews from Etsy
To export your Etsy reviews:
  1. From your Etsy admin, go to **Settings** > **Options**.
[![](https://downloads.intercomcdn.com/i/o/z09y8g87/1846759536/72c4a751f88356fc8635798e4e91/how_to_reach_etsy_options_tab.gif?expires=1793279700&signature=dce0ea892d0548cd26729cc9160f55bde9b80eaa49761510740e60c99f6bd436&req=dSgjEM57lIRcX%2FMW1HO4zVML6EQrBji2FiCx%2FaJuIkZoNJ4zxVNBgKGpAhv1%0AvbSX%0A)](https://downloads.intercomcdn.com/i/o/z09y8g87/1846759536/72c4a751f88356fc8635798e4e91/how_to_reach_etsy_options_tab.gif?expires=1793279700&signature=dce0ea892d0548cd26729cc9160f55bde9b80eaa49761510740e60c99f6bd436&req=dSgjEM57lIRcX%2FMW1HO4zVML6EQrBji2FiCx%2FaJuIkZoNJ4zxVNBgKGpAhv1%0AvbSX%0A)
  2. Open the **Download Data** tab.
  3. Scroll down to the **Take your data with you** section, and click the **Download Your Reviews** button.
[![](https://downloads.intercomcdn.com/i/o/z09y8g87/1846759912/7ff5657ebfe133890391103f2d3b/how_to_export_etsy_reviews.gif?expires=1793279700&signature=b131e209dd08e4055567303a801a913d48da3b72e7b5adc5290a4db511909afe&req=dSgjEM57lIheW%2FMW1HO4zbAB3sNUzU6VVsGxpumELxDKdltZs%2FUzW%2BDhZvXN%0A2DDP%0A)](https://downloads.intercomcdn.com/i/o/z09y8g87/1846759912/7ff5657ebfe133890391103f2d3b/how_to_export_etsy_reviews.gif?expires=1793279700&signature=b131e209dd08e4055567303a801a913d48da3b72e7b5adc5290a4db511909afe&req=dSgjEM57lIheW%2FMW1HO4zbAB3sNUzU6VVsGxpumELxDKdltZs%2FUzW%2BDhZvXN%0A2DDP%0A)


Etsy will generate a JSON file of your reviews named **_reviews.json_** _,_ which you can use to import to Judge.me. 
## Step 2: Import your reviews to Judge.me
To import your Etsy JSON file to Judge.me:
  1. From your Judge.me admin, go to **Settings > Integrations**
  2. Find and click on the **Etsy** card.
  3. Scroll down to the **Import reviews manually** section at the bottom.
  4. Click the **Import reviews manually** button.
  5. Upload the `reviews.json` file you downloaded in Step 1.
  6. Click **Import**.
  7. You can select the product for each review or select a product for multiple reviews at once.
  8. Click **Import**.  
​
[![](https://downloads.intercomcdn.com/i/o/z09y8g87/1846797568/394430fa100661c1adf1eba15692/Animation.gif?expires=1793279700&signature=64dfe1946892b0bde5f78c78c8012b9571033f279283e3eb038fd5d75cd3f5a5&req=dSgjEM53moRZUfMW1HO4zRw4ySRNGIzi23amCO%2FMdu6%2FcZ7gPs5JTXwQwM5k%0A4wmx%0A)](https://downloads.intercomcdn.com/i/o/z09y8g87/1846797568/394430fa100661c1adf1eba15692/Animation.gif?expires=1793279700&signature=64dfe1946892b0bde5f78c78c8012b9571033f279283e3eb038fd5d75cd3f5a5&req=dSgjEM53moRZUfMW1HO4zRw4ySRNGIzi23amCO%2FMdu6%2FcZ7gPs5JTXwQwM5k%0A4wmx%0A)


* * *
Related Articles
  * [How do we verify reviews?](https://judge.me/help/en/articles/8287248-how-do-we-verify-reviews)
  * [Verified reviews](https://judge.me/help/en/articles/8376284-verified-reviews)
  * [Importing reviews from Amazon with a Chrome extension](https://judge.me/help/en/articles/9813299-importing-reviews-from-amazon-with-a-chrome-extension)
  * [Syncing reviews from Etsy](https://judge.me/help/en/articles/10713924-syncing-reviews-from-etsy)
  * [Reviews import log](https://judge.me/help/en/articles/12086833-reviews-import-log)


Did this answer your question?
Disappointed Reaction😞Neutral Reaction😐Smiley Reaction😃
Table of contents
[How it works](https://judge.me/help/en/articles/9813259-importing-reviews-from-etsy-with-a-json-file#h_c14aaa1b42)[Considerations](https://judge.me/help/en/articles/9813259-importing-reviews-from-etsy-with-a-json-file#h_1dd3dae031)[How to import reviews from Etsy JSON file](https://judge.me/help/en/articles/9813259-importing-reviews-from-etsy-with-a-json-file#h_a4c7bef34c)[Step 1: Export your reviews from Etsy](https://judge.me/help/en/articles/9813259-importing-reviews-from-etsy-with-a-json-file#h_58ac7bd213)[Step 2: Import your reviews to Judge.me](https://judge.me/help/en/articles/9813259-importing-reviews-from-etsy-with-a-json-file#h_054c85b563)
[![Judge.me Help Center](https://downloads.intercomcdn.com/i/o/z09y8g87/650679/8537c2d4683a1571571fc672e9b9/3d7b0d754699f052e760c723bbea9ffb.png)](https://judge.me/help/en/)
support@judge.me
  * [![](https://intercom.help/judgeme-5034134337dc/assets/svg/icon:social-linkedin/757575)](https://www.linkedin.com/company/judgeme)
  * [![](https://intercom.help/judgeme-5034134337dc/assets/svg/icon:social-facebook/757575)](https://www.facebook.com/judgedotme)
  * [![](https://intercom.help/judgeme-5034134337dc/assets/svg/icon:social-twitter-x/757575)](https://www.twitter.com/judgeme_reviews)
  * [![](https://intercom.help/judgeme-5034134337dc/assets/svg/icon:social-youtube/757575)](https://www.youtube.com/@Judgeme)



