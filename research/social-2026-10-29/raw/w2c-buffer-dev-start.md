![](https://developers.buffer.com/image/banner-line.svg) ![](https://developers.buffer.com/image/banner-dot.svg) ![](https://developers.buffer.com/image/banner-line.svg) ![](https://developers.buffer.com/image/banner-dot.svg)
![Buffer Commit](https://developers.buffer.com/image/banner-commit-logo.svg)
Join Buffer’s first Build Contest. October 28 - November 13
[Register](https://buffer.com/api/commit?utm_source=buffer&utm_medium=banner&utm_campaign=buffer_commit&utm_content=developer_portal)
[ ![Buffer API](https://developers.buffer.com/logo.svg) ](https://developers.buffer.com/index.html)
Search docs... `⌘K`
[ ](https://discord.gg/9skbzTz6vQ "Discord")
[API Status](https://status.buffer.com/) [Get API Key](https://publish.buffer.com/settings/api)
Guides 
[Introduction](https://developers.buffer.com/guides/introduction.html) [Quick Start](https://developers.buffer.com/guides/getting-started.html) [Authentication](https://developers.buffer.com/guides/authentication.html) [Building Apps](https://developers.buffer.com/guides/building-apps.html) [Your First Post](https://developers.buffer.com/guides/your-first-post.html) [GraphQL for REST Devs](https://developers.buffer.com/guides/graphql-intro.html) [REST API Migration](https://developers.buffer.com/guides/rest-migration.html) [Data Model](https://developers.buffer.com/guides/data-model.html) [Posts & Scheduling](https://developers.buffer.com/guides/posts-and-scheduling.html) [Ideas](https://developers.buffer.com/guides/ideas.html) [Content Items Experimental](https://developers.buffer.com/guides/content-items.html) [Hosting Media](https://developers.buffer.com/guides/hosting-media.html) [Tags Experimental](https://developers.buffer.com/guides/tags.html) [Post Metrics](https://developers.buffer.com/guides/post-metrics.html) [API Standards](https://developers.buffer.com/guides/api-standards.html) [Character Limits](https://developers.buffer.com/guides/character-limits.html) [Error Handling](https://developers.buffer.com/guides/error-handling.html) [Rate Limits](https://developers.buffer.com/guides/api-limits.html) [Pagination](https://developers.buffer.com/guides/pagination.html) [Efficient API Usage](https://developers.buffer.com/guides/efficient-api-usage.html)
Examples 
[Aggregate Post Metrics](https://developers.buffer.com/examples/aggregate-post-metrics.html) [Create Draft Post](https://developers.buffer.com/examples/create-draft-post.html) [Create Idea](https://developers.buffer.com/examples/create-idea.html) [Create Image Post](https://developers.buffer.com/examples/create-image-post.html) [Create Instagram Post With User Tags](https://developers.buffer.com/examples/create-instagram-post-with-user-tags.html) [Create Scheduled Post](https://developers.buffer.com/examples/create-scheduled-post.html) [Create Tag Experimental](https://developers.buffer.com/examples/create-tag.html) [Create Text Post](https://developers.buffer.com/examples/create-text-post.html) [Create Threaded Post](https://developers.buffer.com/examples/create-threaded-post.html) [Create Video Post](https://developers.buffer.com/examples/create-video-post.html) [Delete Tag Experimental](https://developers.buffer.com/examples/delete-tag.html) [Get Channel](https://developers.buffer.com/examples/get-channel.html) [Get Channels](https://developers.buffer.com/examples/get-channels.html) [Get Filtered Channels](https://developers.buffer.com/examples/get-filtered-channels.html) [Get Organizations](https://developers.buffer.com/examples/get-organizations.html) [Get Paginated Posts](https://developers.buffer.com/examples/get-paginated-posts.html) [Get Post Metrics](https://developers.buffer.com/examples/get-post-metrics.html) [Get Posts For Channels](https://developers.buffer.com/examples/get-posts-for-channels.html) [Get Posts With Assets](https://developers.buffer.com/examples/get-posts-with-assets.html) [Get Posts With Metrics](https://developers.buffer.com/examples/get-posts-with-metrics.html) [Get Quarterly Performance Report](https://developers.buffer.com/examples/get-quarterly-performance-report.html) [Get Scheduled Posts](https://developers.buffer.com/examples/get-scheduled-posts.html) [Get Tag Experimental](https://developers.buffer.com/examples/get-tag.html) [Get Tags Experimental](https://developers.buffer.com/examples/get-tags.html) [Update Tag Experimental](https://developers.buffer.com/examples/update-tag.html)
[ CLI](https://developers.buffer.com/guides/cli.html) [ Integrations](https://developers.buffer.com/guides/integrations.html) [ Explorer](https://developers.buffer.com/explorer.html) [ Changelog](https://developers.buffer.com/changelog.html) [ Roadmap](https://developers.buffer.com/roadmap.html) [ Legacy Apps](https://buffer.com/developers/legacy-api)
API Reference
[ Account](https://developers.buffer.com/reference.html#account)[ Organizations](https://developers.buffer.com/reference.html#organizations)[ Channels](https://developers.buffer.com/reference.html#channels)[ Tags](https://developers.buffer.com/reference.html#tags)[ Posts](https://developers.buffer.com/reference.html#posts)[ Ideas](https://developers.buffer.com/reference.html#ideas)[ Other](https://developers.buffer.com/reference.html#other)
Getting StartedQuick Start
# Quick Start
Copy Page
Ask AI assistant Chat with the docs AI assistant Copy page Copy this page as Markdown View as Markdown Open this page as plain Markdown Open in Claude Ask Claude about this page Open in ChatGPT Ask ChatGPT about this page Open in Perplexity Ask Perplexity about this page
Buffer's API is built with GraphQL. If you're new to GraphQL, we'd recommend the [official GraphQL documentation](https://graphql.org/learn/) to get familiar with the basics before diving in.
## Register for API Access[](https://developers.buffer.com/guides/getting-started.html#register-for-api-access)
To get started with the Buffer API, you'll need a Buffer account and an API key. If you don't have an account yet, you can [sign up here](https://buffer.com/signup).
Once you have an account, head to [API settings](https://publish.buffer.com/settings/api) to create your API key.
## What the API supports[](https://developers.buffer.com/guides/getting-started.html#what-the-api-supports)
Your API key lets you perform actions against **your own Buffer account**. We currently support the following operations:
  * Post Creation
  * Post Deletion
  * Post Retrieval
  * Idea Creation
  * Account Retrieval
  * Organization Retrieval
  * Channel Retrieval


## Endpoint[](https://developers.buffer.com/guides/getting-started.html#endpoint)
The Buffer GraphQL API is available at:
Copy Copied! 
```
https://api.buffer.com
```

If you'd like to use a tool like Postman or another HTTP client, point your requests to the endpoint above and follow [Postman's GraphQL guide](https://learning.postman.com/docs/sending-requests/graphql/graphql-overview/) for setup.
## Authorization[](https://developers.buffer.com/guides/getting-started.html#authorization)
Every request must include an `Authorization` header with your API key using the `Bearer` format.
GraphQLcURLNode.jsPythonPHP
Copy Copied! 
```
{
  "Authorization": "Bearer YOUR_TOKEN"
}
```

Copy Copied! 
```
-H 'Authorization: Bearer YOUR_TOKEN'
```

Copy Copied! 
```
headers: {
  'Authorization': 'Bearer YOUR_TOKEN',
}
```

Copy Copied! 
```
headers = {
    "Authorization": "Bearer YOUR_TOKEN",
}
```

Copy Copied! 
```
CURLOPT_HTTPHEADER => [
    'Authorization: Bearer YOUR_TOKEN',
]
```

## Making your first request[](https://developers.buffer.com/guides/getting-started.html#making-your-first-request)
Here's a quick query to fetch your account and organization:
GraphQLcURLNode.jsPythonPHP
Copy Copied! 
```
query GetOrganizations {
  account {
    organizations {
      id
    }
  }
}
```

Copy Copied! 
```
curl -X POST 'https://api.buffer.com' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{"query": "query GetOrganizations {\n  account {\n    organizations {\n      id\n    }\n  }\n}"}'
```

Copy Copied! 
```
async function getOrganizations() {
  const response = await fetch('https://api.buffer.com', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer YOUR_API_KEY',
    },
    body: JSON.stringify({
      query: `
      query GetOrganizations {
        account {
          organizations {
            id
          }
        }
      }
      `,
    }),
  });

  const data = await response.json();
  console.log(JSON.stringify(data, null, 2));
}

getOrganizations();
```

Copy Copied! 
```
import requests

query = """
query GetOrganizations {
  account {
    organizations {
      id
    }
  }
}
"""

response = requests.post(
    "https://api.buffer.com",
    headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_KEY",
    },
    json={
        "query": query,
    },
)

data = response.json()
print(data)
```

Copy Copied! 
```
<?php

$query = '
query GetOrganizations {
  account {
    organizations {
      id
    }
  }
}
';

$payload = [
    'query' => $query,
];

$ch = curl_init('https://api.buffer.com');
curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_HTTPHEADER => [
        'Content-Type: application/json',
        'Authorization: Bearer YOUR_API_KEY',
    ],
    CURLOPT_POSTFIELDS => json_encode($payload),
    CURLOPT_RETURNTRANSFER => true,
]);

$response = curl_exec($ch);
curl_close($ch);

$data = json_decode($response, true);
print_r($data);
```

You can run this query directly in your browser using the interactive [Buffer API Explorer](https://developers.buffer.com/explorer.html), no local setup required.
Once you have your organization ID, you can use it to fetch channels, posts, and other data for that organization.
[ Previous Introduction ](https://developers.buffer.com/guides/introduction.html) [ Next Authentication ](https://developers.buffer.com/guides/authentication.html)
On this page
[Register for API Access](https://developers.buffer.com/guides/getting-started.html#register-for-api-access) [What the API supports](https://developers.buffer.com/guides/getting-started.html#what-the-api-supports) [Endpoint](https://developers.buffer.com/guides/getting-started.html#endpoint) [Authorization](https://developers.buffer.com/guides/getting-started.html#authorization) [Making your first request](https://developers.buffer.com/guides/getting-started.html#making-your-first-request)
`Esc`
`↑``↓` Navigate `Enter` Open `Esc` Close

