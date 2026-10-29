# w3d: Meta API arbiter, does each automation need a legal entity? (Holliewood & Vine)

Accessed 2026-10-29 on developers.facebook.com (captures in `raw/w3d-*.md`). Budget used: 42 crawls, 3 WebFetch, 3 searches. No app created, no API called. Tags: `verified` = read live this session; `prior` = earlier session, not re-read; `unverified` = forum; `inferred` = my reading.

**Bottom line.** Publishing and comment moderation on the owner's own account need no entity (Standard Access, no App Review). Anything driven by customer events (webhooks, private replies, DM intake) is **unresolved by Meta's pages**, which lean toward "needs Live mode, and Live mode needs Business Verification". The Business Verification help page is walled, so its legal-entity wording is `prior`.

## 1. Verdict table

| Operation | Works without legal entity | Access level and mode | Deciding quote (URL under section 2) |
|---|---|---|---|
| Publish (Reels, carousel, Stories) | **Yes**, one visibility caveat | Standard Access, Instagram Login, Business-type app | App Review table: row "business I own or manage / Instagram Login": Standard Access, App Review "Not required". Caveat: App Modes says "test posts... can only be seen by role users"; App Types says "Business apps do not have app modes". |
| Poll comments `GET /{media}/comments` | **Unclear** | Standard Access (named) | Comment-moderation: "Standard Access if your app serves Instagram professional accounts you own or manage". Against: "the accessible data is limited and public". |
| Reply to a comment | **Yes**, given a comment ID | Standard Access | Same sentence; IDs come from polling or webhooks. |
| Hide, delete | **Yes**, given a comment ID | Standard Access | Same sentence. |
| Webhooks `comments` (customers) | **Leaning no** | Documented: Live, Advanced Access, Business Verification | "Advanced Access is required for `comments` and `live_comments` notifications." Counter-quote in 2.1. |
| Private reply | **Unclear** | Three pages, three answers (2.3) | Platform page: no access level. Messenger-path page: "Advanced Access". |
| DM (send, receive) | **Unclear** | Standard Access named; intake needs webhooks | "Only after an Instagram user has sent your app user's... account a message can your app send a message". |

## 2. Per-question quotes

### 2.1 Q1: Development mode, role user, `comments` webhooks

Meta never states what a Development-mode app receives for real events. What it states:

- Setup (https://developers.facebook.com/documentation/instagram-platform/webhooks/setup, `verified`): "Your app must be published or **Live** to receive notifications for app users." Table, Instagram Login: Access level "Advanced Access"; Business verification "Required for production access" (all three login types).
- Create-app (https://developers.facebook.com/documentation/instagram-platform/create-an-instagram-app, `verified`): "You're required to connect your app to a business that has completed Business Verification before you can publish your app." Step 7: "Assign an Instagram account to get access tokens for testing Instagram API calls and webhooks subscriptions."
- Messaging webhooks (https://developers.facebook.com/documentation/business-messaging/instagram-messaging/webhooks, `verified`): "Your app must be published, regardless of app review status, to receive webhooks." and "If your app has not been approved, pending, or review is not needed, Webhooks will only be sent if the person using your app has a role on the app. You can only access data you own or administer."
- Messenger webhooks (.../messenger-platform/webhooks, `verified`): "Standard Access to receive notifications from people who have a role on your app, such as your app admins, developers or testers; or Advanced Access to receive notifications from your customers, people who do not have a role on your app."
- **Counter-quote** (Business Verification, https://developers.facebook.com/documentation/development/release/business-verification, `verified`): "If your app will only be used by app users who have a role on the app itself you do not need to complete verification; these users can grant your app any permissions at any time and all features are always active."
Reframe: the owner's role is not the question; the commenter's may be. Reading A (messaging page, `inferred`): events on the owner's account are sent because the app user has a role, customers included. Reading B (Messenger page, `inferred`): only role users' (testers') events are sent. Forum threads (Comments Test button silent in Development mode, no staff answer) are `unverified` and unused.

### 2.2 Q2: Access levels, modes, and what Business Verification gates

- Overview (https://developers.facebook.com/documentation/instagram-platform/overview, `verified`): "If your app only serves your Instagram professional account or an account you manage, Standard Access is all your app needs." "Advanced Access is the access level required if your app serves Instagram professional accounts that you don't own or manage... This access level requires App Review and Business Verification." Also: "some features might not work properly until your app has been granted Advanced Access."
- Access Levels (https://developers.facebook.com/docs/graph-api/overview/access-levels): Standard permissions "can only be requested from app users who have a role on the requesting app"; Business Verification "is required to get Advanced Access."
- App modes (.../build-and-test/app-modes): Development: "Any data generated while an app is in Development mode, such as test posts, can only be seen by role users." Live: "only permissions approved through App Review."
- **Correction to w2c and w2d.** App Types (.../app-dashboard/app-types): "Business apps do not have app modes and instead rely exclusively on access levels." The Instagram product requires a Business app (create-app page). So "kept in Development mode" is not a Meta concept for this app type, yet the webhook pages still say "published" and "Live". Doc conflict; test it.
- What Business Verification gates (Release page): "Apps that request advanced access for permissions and apps that allow other Businesses to access their own data must be connected to a Business that has completed Business Verification." Create-app adds the "before you can publish" line (2.1). App Review for Instagram API (.../instagram-platform/app-review) says own-business apps need no review.
- Legal entity: the developer page says verification lets Meta "verify your identity as a business entity." The 2023 blog (https://developers.facebook.com/blog/post/2023/02/01/developer-platform-requiring-business-verification-for-advanced-access/) says "individual verification will no longer be allowed for access once the business verification process is complete." **The requirements page is walled** (4-byte captures). `prior` (desk Chrome read 2026-10-12, not re-read today): "Your business needs to be registered with local authorities"; documents such as "a business license or articles of incorporation"; "up to 14 business days." **Parent: read these in Chrome:** https://www.facebook.com/business/help/1095661473946872, .../2058515294227817, .../193400874040813, https://en-gb.facebook.com/business/help/2342133782492969.
### 2.3 Q3: Operations at Standard Access

- **Publish.** Content Publishing guide (`verified`), Instagram Login: Access Levels "Advanced Access / Standard Access". Stories: "Publishing stickers (i.e., link, poll, location) is not supported."
- **Poll comments.** Reference (.../reference/ig-media/comments): "An access token from a User who created the IG Media object." Limits: "maximum of 50 comments per query", "cannot be filtered by timestamp", top-level only. Overview: "a permission only allows access to data created by the app user who granted the permission... the accessible data is limited and public." Nothing says non-role commenters' text is withheld, or returned.
- **Reply, hide, delete.** Comment moderation (`verified`): "Standard Access if your app serves Instagram professional accounts you own or manage and have added to your app in the App Dashboard." Reply limits: "You cannot reply to hidden comments"; replies to replies attach to the top-level comment. Delete: "only be deleted by the owner of the object."
- **Private reply, all three pages.**
  1. Platform page (.../instagram-platform/private-replies): permissions table only (Instagram Login: `instagram_business_basic`, `instagram_business_manage_comments`). No access level. Limits: "Only one message can be sent to the commenter"; "within 7 days." The Instagram Login column omits a messages permission (Unified lists `instagram_manage_messages`), a doc gap.
  2. Messenger-path page (.../instagram-messaging/features/private-replies, Page ID and Page token, Facebook Login): "You will need: ... The Human Agent feature; Advanced Access" and "Standard Access apps can only access data for people who have a role on the app." Governs the Facebook Login path, not Instagram Login (`inferred`).
  3. Instagram Login messaging page (.../instagram-api-with-instagram-login/messaging-api): "Standard Access if your app serves Instagram professional accounts you own or manage or have added to your app in the App Dashboard; Some features may not work properly until your app has been granted Advanced Access." Also: "Your app testers must have a role on your app... and have a role on the Instagram professional account."
- **DM.** Same page: send only after the user messages; 24-hour window (7 days with the Human Agent tag). Intake relies on messaging webhooks (published app); a Conversations API polling fallback exists (2 calls per second), not read in depth.

### 2.4 Q4: Limits

- **API posts per 24 h, 100 vs 50.** Guide, rate-limit section: "100 API-published posts within a 24-hour moving period." Same guide, carousel limitations: "50 published posts within a 24-hour period." Endpoint reference (.../ig-user/content_publishing_limit): `quota_total` "(currently `50`)", example response 50. The endpoint reference governs because the call returns the live number (`inferred`); plan for 50. Also "400 containers" per rolling 24 h; containers expire after 24 h.
- **Private replies:** one per comment, 7 days; "750 calls per hour per Instagram professional account for private replies to comments on Instagram posts and reels"; "100 calls per second" for Live (Overview and rate-limiting page).
- **Comment replies:** no per-endpoint cap found. General limit: "Calls within 24 hours = 4800 * Number of Impressions" per app and app-user pair, so a new account has a small polling budget (`inferred`). Meta: "We strongly recommend using webhooks."

### 2.5 Q5: Tokens

- Overview: long-lived token "valid for 60 days and can be refreshed before they expire."
- Business Login: refresh needs the token "at least 24 hours old", valid (not expired), and `instagram_business_basic`. "Tokens that have not been refreshed in 60 days will expire and can no longer be refreshed." Endpoint: `GET graph.instagram.com/refresh_access_token?grant_type=ig_refresh_token`.
- Get started: dashboard "Generate token" gives 60 days; login-flow tokens last 1 hour. A lapse needs a new token (`inferred`).

### 2.6 Q6: Publishing parameters (https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-user/media, `verified`)

| Parameter | Quote | Note |
|---|---|---|
| `cover_url` | "For Reels only... If you specify both `cover_url` and `thumb_offset`, we use `cover_url` and ignore `thumb_offset`." | JPEG, 8 MB, 9:16 recommended |
| `thumb_offset` | "Location, in milliseconds, of the video or reel frame to be used as the cover thumbnail image." | default 0 |
| `alt_text` | "For image posts only... up to 1000 character... Reels and stories are not supported." | images and carousel images |
| `trial_params` | "`media_type` must be `REELS`"; `graduation_strategy` "`MANUAL` or `SS_PERFORMANCE`" | Guide example uses graph.instagram.com. The 200-follower rule (w1a) is not in the API doc. |
| `collaborators` | "For Feed image, Reels and Carousels only. A list of up to 3 instagram usernames... Not supported for Stories." | **Conflict:** Overview section "Collaborators" is headed "_Facebook Login for Business only._" Need review. |
| Scheduling | **No parameter** in the table or guide. The guide only says to enforce the limit "if your app allows app users to schedule posts." | Cron at post time; container expires in 24 h |

Facebook Login only per the reference: `poll_attachment`, `is_comment_prompt_used`, `is_paid_partnership`. `is_ai_generated` works on both; "Not available for carousel children."

## 3. One-hour throwaway test (free, no entity)

Use two commenter accounts: **T** added as an Instagram tester, **N** not. A single account cannot separate Readings A and B.

1. Create a Business-type app (use case Other), add Instagram, add the owner, accept the invite. Does the dashboard show a mode toggle or **Go live**, and does it demand Business Verification?
2. Generate a token; read `content_publishing_limit` (50 or 100?).
3. Publish a Reel with `cover_url` and `collaborators` via graph.instagram.com, an image with `alt_text`, and a Trial Reel (expect refusal under 200 followers). View each logged out from N.
4. Subscribe to `comments` via `/subscribed_apps`. Comment from T, then N. Which fire? Compare the dashboard Test button.
5. Poll `GET /{media}/comments`: is N's text returned?
6. Reply to, hide, delete a comment via the API.
7. Private-reply to T's, then N's comment. Record error codes; is the link tappable in Requests?
8. N sends a DM: does the messaging webhook fire; does a reply inside 24 h send?
9. Refresh the token under 24 hours old (expect refusal), then after.

Decision: if N works everywhere, no entity is needed. If only T works, customer-facing automation needs Live mode and a registered entity; the no-entity fallback is polling plus API replies (if step 5 passes) or a third-party tool holding an approved app.
