
```
# Comments



Represents a collection of [IG Comments](https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-comment) on an [IG Media](https://developers.facebook.com/documentation/instagram-platform/reference/instagram-media) object.

### Non-Organic Comments {#non-organic-comments}

Comments on ads containing Instagram ad media (non-organic comments) can be returned as well.

To get comments on an ad, use the [Marketing API](https://developers.facebook.com/documentation/ads-commerce/marketing-api) to request the ad's `effective_instagram_media_id`. You can then query the returned ID's `/comments` edge to get comments on that media object, or its [`/ordered_comments`](#ordered-comments) edge to get comments in the same order as displayed in Instagram. For an ad with multiple Instagram media, such as an ad that uses [Placement Asset Customization](https://developers.facebook.com/documentation/ads-commerce/marketing-api/dynamic-creative/placement-asset-customization), the `/ordered_comments` response can include comments from all of the ad's Instagram media.

If the ad was [promoted/boosted from an existing post](https://developers.facebook.com/documentation/ads-commerce/instagram/ads-api/guides/use-posts-as-ads), querying the `/comments` edge on either the original post or the ad media returns comments from both.

Refer to the Marketing API's [Post Moderation](https://developers.facebook.com/documentation/ads-commerce/instagram/ads-api/guides/post-moderation) guide for more information.

### Requirements

|  | Instagram API with Unified Login | Instagram API with Instagram Login | Instagram API with Facebook Login |
| --- | --- | --- | --- |
| **Access Tokens** | * [Business Integration System User access token](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-unified-login/authentication) | * Instagram User access token | * [Facebook User access token](https://developers.facebook.com/documentation/facebook-login/guides/access-tokens#usertokens) |
| **Host URL** | `graph.facebook.com` | `graph.instagram.com` | `graph.facebook.com` |
| **Login Type** | Facebook Login for Business | Business Login for Instagram | Facebook Login for Business |
| [**Permissions**](https://developers.facebook.com/docs/permissions/reference#i) | * `instagram_basic`<br>* `instagram_manage_comments` | * `instagram_business_basic`<br>* `instagram_business_manage_comments` | * `instagram_basic`<br>* `instagram_manage_comments`<br>* `pages_read_engagement`<br><br>If the app user was granted a role via the Business Manager on the [Page](https://developers.facebook.com/documentation/instagram-platform/overview#pages) connected to the targeted IG User, you will also need one of:<br><br>* `ads_management`<br>* `ads_read` |

## Creating

### Creating a Comment on a Media Object

`POST /<IG_MEDIA_ID>/comments?message=<MESSAGE_CONTENT>`

Creates an [IG Comment](https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-comment) on an [IG Media](https://developers.facebook.com/documentation/instagram-platform/reference/instagram-media) object.

#### Limitations

Comments on live video IG Media are not supported.

#### Query String Parameters

Query string parameters are optional unless indicated as required.

- `<MESSAGE_CONTENT>` (required) — The text to be included in the comment.

#### Example Request

```
POST graph.facebook.com
  /17895695668004550/comments?message=This%20is%20awesome!
```

#### Example Response

```
{
  "id": "17870913679156914"
}
```

## Reading

### Getting Comments on a Media Object {#comments}

`GET /<IG_MEDIA_ID>/comments`

Returns a list of [IG Comments](https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-comment) on an [IG Media](https://developers.facebook.com/documentation/instagram-platform/reference/instagram-media) object.

#### Limitations

- Returns results in reverse chronological order by default.
- If the requested IG Media object is a post that was promoted/boosted as an ad, or the ad media from that boost, returns comments from both the original post and the ad media.
- For an ad with multiple Instagram media, such as an ad that uses Placement Asset Customization, returns only comments on the requested IG Media object. To get comments from all of the ad's Instagram media, use [`/ordered_comments`](#ordered-comments).
- Returns only top-level comments. Replies to comments are not included unless you use field expansion to request the `replies` field.
- Returns a maximum of 50 comments per query.
- Comments cannot be filtered by timestamp.

#### Permissions

An [access token](https://developers.facebook.com/documentation/instagram-platform/overview#authentication) from a User who created the [IG Media](https://developers.facebook.com/documentation/instagram-platform/reference/instagram-media) object, with the following permissions:

- `instagram_basic`
- `instagram_manage_comments`

If the token is from a User whose **Page role was granted via the Business Manager**, one of the following permissions is also required:

- `ads_management`
- `ads_read`

#### Sample Request

```
GET graph.facebook.com
  /17895695668004550/comments
```

#### Sample Response

```
{
  "data": [
    {
      "timestamp": "2017-08-31T19:16:02+0000",
      "text": "This is awesome!",
      "id": "17870913679156914"
    },
    {
      "timestamp": "2017-08-31T18:10:30+0000",
      "text": "*Sniff*",
      "id": "17873440459141021"
    }
  ]
}
```

### Getting ordered comments as displayed in Instagram {#ordered-comments}

`GET /<IG_MEDIA_ID>/ordered_comments`

Returns [IG Comments](https://developers.facebook.com/documentation/instagram-platform/instagram-graph-api/reference/ig-comment) in the same order as displayed in Instagram. For an ad with multiple Instagram media, such as an ad [boosted from an existing post](https://developers.facebook.com/documentation/ads-commerce/instagram/ads-api/guides/use-posts-as-ads) or an ad that uses [Placement Asset Customization](https://developers.facebook.com/documentation/ads-commerce/marketing-api/dynamic-creative/placement-asset-customization), the response can include comments from all of the ad's Instagram media.

This endpoint is available for the Instagram API with Facebook Login only.

#### Limitations

- Story media and carousel child media are not supported.
- The `media`, `user`, and `legacy_instagram_comment_id` fields are not returned for comments or replies.
- Only the `replies` and `from` fields support field expansion. `from` can return `id` and `username`. Within `replies`, you can request the same fields as for a comment, except `replies`. Other fields can't be expanded.

#### Permissions

A [Facebook User access token](https://developers.facebook.com/documentation/facebook-login/guides/access-tokens#usertokens) with one of the following permissions:

- `instagram_basic` for the Instagram professional account that owns the IG Media object
- `ads_management`
- `ads_read`
- `pages_manage_metadata`

If the access token doesn't have any of these permissions, the response contains an empty `data` array instead of an error.

#### Query string parameters

Query string parameters are optional.

- `fields` — A comma-separated list of fields to return. If omitted, the response includes `id`, `text`, and `timestamp`.
- `date_format` — The format for `timestamp`. Use `U` to return a Unix timestamp.
- `after` — The cursor after which to return results.
- `limit` — The maximum number of comments to return.

#### Sample request

```
GET graph.facebook.com
  /17895695668004550/ordered_comments
    ?fields=id,text,timestamp,replies{id,text,timestamp}
```

#### Sample response

In this sample, the media belongs to an ad with two Instagram media. The first comment is on the requested media, and the second comment is on the ad's other Instagram media.

```json
{
  "data": [
    {
      "id": "17870913679156914",
      "text": "This is awesome!",
      "timestamp": "2017-08-31T19:16:02+0000",
      "replies": {
        "data": [
          {
            "id": "17873440459141029",
            "text": "Thanks for sharing!",
            "timestamp": "2017-08-31T19:18:03+0000"
          }
        ]
      }
    },
    {
      "id": "17870913679106914",
      "text": "This is nice!",
      "timestamp": "2017-08-30T19:16:02+0000"
    }
  ]
}
```

## Updating

This operation is not supported.

## Deleting

This operation is not supported.

```


