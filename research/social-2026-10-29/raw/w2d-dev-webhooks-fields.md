
```
# Instagram webhook fields and permissions


Subscribe only to the webhook fields required by your integration. Field availability and permission requirements depend on the Instagram API setup used by your app.

## Instagram API with Unified Login {#unified-login}

The Instagram API with Unified Login uses the same permission checks as Facebook Login for Business. Each webhook field needs the following permission:

| Instagram webhook field | Permission |
|---|---|
| `comments` | `instagram_manage_comments` |
| `live_comments` | `instagram_manage_comments` |
| `mentions` | `instagram_manage_comments` |
| `message_reactions` | `instagram_manage_messages` |
| `messages` | `instagram_manage_messages` |
| `messaging_postbacks` | `instagram_manage_messages` |
| `messaging_referral` | `instagram_manage_messages` |
| `messaging_seen` | `instagram_manage_messages` |
| `story_insights` | `instagram_manage_insights` |

See [Permissions for the Instagram API with Unified Login](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-unified-login/permissions).

## Other Instagram API setups

| Instagram Webhook field | Instagram API setup with Instagram Login permissions | Instagram API setup with Facebook Login permissions | Instagram Messaging API<br>(Messenger Platform) permissions |
| --- | --- | --- | --- |
| `comments` | * `instagram_business_basic`<br>* `instagram_business_manage_comments` | * `instagram_basic`<br>* `instagram_manage_comments`<br>* `pages_manage_metadata`<br>* `pages_read_engagement`<br>* `pages_show_list` | x |
| `live_comments` | * `instagram_business_basic`<br>* `instagram_business_manage_comments` | * `instagram_basic`<br>* `instagram_manage_comments`<br>* `pages_manage_metadata`<br>* `pages_read_engagement`<br>* `pages_show_list` | x |
| `mentions` | Included in the `comments` webhook notification | * `instagram_basic`<br>* `instagram_manage_comments`<br>* `pages_manage_metadata`<br>* `pages_read_engagement`<br>* `pages_show_list` | x |
| `message_echoes` | * `instagram_business_basic`<br>* `instagram_business_manage_comments` | x | Included in the `messages` webhook notification |
| `message_reactions` | * `instagram_business_basic`<br>* `instagram_business_manage_messages` | x | * `instagram_basic`<br>* `instagram_manage_messages`<br>* `pages_manage_metadata`<br>* `pages_read_engagement`<br>* `pages_show_list` |
| `messages` | * `instagram_business_basic`<br>* `instagram_business_manage_messages`<br><br>For eligible connected apps, the `messages` notification can include [Meta Business Agent handoff admin text and, when enabled, a structured handoff reason](https://developers.facebook.com/documentation/instagram-platform/webhooks/examples#handoff-admin-text). | x | * `instagram_basic`<br>* `instagram_manage_messages`<br>* `pages_manage_metadata`<br>* `pages_read_engagement`<br>* `pages_show_list`<br><br>For eligible connected apps, the `messages` notification can include [`message.admin_text`](https://developers.facebook.com/documentation/business-messaging/instagram-messaging/webhooks#admin-text) when a first-party Meta application hands off a conversation.<br><br>Meta Business Agent handoff notifications can also include [`message.handoff_reason`](https://developers.facebook.com/documentation/instagram-platform/webhooks/examples#handoff-admin-text) when enabled. |
| `messaging_handover` | * `instagram_business_basic`<br>* `instagram_business_manage_messages` | x | * `instagram_basic`<br>* `instagram_manage_messages`<br>* `pages_manage_metadata`<br>* `pages_read_engagement`<br>* `pages_show_list` |
| `messaging_optins` | * `instagram_business_basic`<br>* `instagram_business_manage_messages` | x | x |
| `messaging_policy_enforcement` | x | x | * `instagram_basic`<br>* `instagram_manage_messages`<br>* `pages_manage_metadata`<br>* `pages_read_engagement`<br>* `pages_show_list` |
| `messaging_postbacks` | * `instagram_business_basic`<br>* `instagram_business_manage_messages` | x | * `instagram_basic`<br>* `instagram_manage_messages`<br>* `pages_manage_metadata`<br>* `pages_read_engagement`<br>* `pages_show_list` |
| `messaging_referral` | * `instagram_business_basic`<br>* `instagram_business_manage_messages` | x | * `instagram_basic`<br>* `instagram_manage_messages`<br>* `pages_manage_metadata`<br>* `pages_read_engagement`<br>* `pages_show_list` |
| `messaging_seen` | * `instagram_business_basic`<br>* `instagram_business_manage_messages` | x | * `instagram_basic`<br>* `instagram_manage_messages`<br>* `pages_manage_metadata`<br>* `pages_read_engagement`<br>* `pages_show_list` |
| `response_feedback` | x | x | * `instagram_basic`<br>* `instagram_manage_messages`<br>* `pages_manage_metadata`<br>* `pages_read_engagement`<br>* `pages_show_list` |
| `standby` | * `instagram_business_basic`<br>* `instagram_business_manage_messages` | x | * `instagram_basic`<br>* `instagram_manage_messages`<br>* `pages_manage_metadata`<br>* `pages_read_engagement`<br>* `pages_show_list` |
| `story_insights` | x | * `instagram_basic`<br>* `instagram_manage_insights`<br>* `pages_manage_metadata`<br>* `pages_read_engagement`<br>* `pages_show_list` | x |

## Next steps

- [Set up Instagram Webhooks](https://developers.facebook.com/documentation/instagram-platform/webhooks/setup)
- [Review webhook notification examples](https://developers.facebook.com/documentation/instagram-platform/webhooks/examples)
- [Review permissions for the Instagram API with Unified Login](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-unified-login/permissions)


```


