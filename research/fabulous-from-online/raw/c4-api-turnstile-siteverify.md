[Skip to content](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#main-content)
> Documentation Index  
> Fetch the complete documentation index at: https://developers.cloudflare.com/turnstile/llms.txt  
> Use this file to discover all available pages before exploring further.
[![](https://developers.cloudflare.com/_astro/logo.te5VL_aD.svg)Docs](https://developers.cloudflare.com/)[Directory](https://developers.cloudflare.com/directory/)[API](https://developers.cloudflare.com/api/)[SDKs](https://developers.cloudflare.com/fundamentals/api/reference/sdks/)[Changelog](https://developers.cloudflare.com/changelog/)
Search`Ctrl``K`[](https://github.com/cloudflare/cloudflare-docs)[Log inDashboard](https://dash.cloudflare.com/)
[](https://developers.cloudflare.com/)[Turnstile](https://developers.cloudflare.com/turnstile/)
`/`
  * [Overview](https://developers.cloudflare.com/turnstile/)
  * [Plans](https://developers.cloudflare.com/turnstile/plans/)
  * [Spin](https://developers.cloudflare.com/turnstile/spin/)
  * Concepts
    * [Turnstile widgets](https://developers.cloudflare.com/turnstile/concepts/widget/)
    * [Cloudflare Challenges ↗︎](https://developers.cloudflare.com/cloudflare-challenges/)
  * Get started
    * [Overview](https://developers.cloudflare.com/turnstile/get-started/)
    * Widget management
      * [Cloudflare dashboard](https://developers.cloudflare.com/turnstile/get-started/widget-management/dashboard/)
      * [API](https://developers.cloudflare.com/turnstile/get-started/widget-management/api/)
      * [Terraform](https://developers.cloudflare.com/turnstile/get-started/widget-management/terraform/)
    * Embed the widget
      * [Overview](https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/)
      * [Widget configurations](https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/widget-configurations/)
    * [Validate the token](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/)
    * [Mobile implementation](https://developers.cloudflare.com/turnstile/get-started/mobile-implementation/)
  * Additional configurations
    * Hostname management
      * [Overview](https://developers.cloudflare.com/turnstile/additional-configuration/hostname-management/)
      * [Pre-clearance configuration](https://developers.cloudflare.com/turnstile/additional-configuration/hostname-management/pre-clearance/)
      * [Any Hostname](https://developers.cloudflare.com/turnstile/additional-configuration/hostname-management/any-hostname/)
    * [Pre-clearance support ↗︎](https://developers.cloudflare.com/cloudflare-challenges/concepts/clearance/#pre-clearance-support-in-turnstile)
    * [Ephemeral IDs](https://developers.cloudflare.com/turnstile/additional-configuration/ephemeral-id/)
    * [Offlabel](https://developers.cloudflare.com/turnstile/additional-configuration/offlabel/)
  * Turnstile Analytics
    * [Overview](https://developers.cloudflare.com/turnstile/turnstile-analytics/)
    * [Challenge outcome](https://developers.cloudflare.com/turnstile/turnstile-analytics/challenge-outcomes/)
    * [Token validation](https://developers.cloudflare.com/turnstile/turnstile-analytics/token-validation/)
  * Migration
    * [Overview](https://developers.cloudflare.com/turnstile/migration/)
    * [Migrate from reCAPTCHA](https://developers.cloudflare.com/turnstile/migration/recaptcha/)
    * [Migrate from hCaptcha](https://developers.cloudflare.com/turnstile/migration/hcaptcha/)
  * [Tutorials](https://developers.cloudflare.com/turnstile/tutorials/)
  * Troubleshooting
    * [Testing](https://developers.cloudflare.com/turnstile/troubleshooting/testing/)
    * [Rotate secret key](https://developers.cloudflare.com/turnstile/troubleshooting/rotate-secret-key/)
    * Client-side errors
      * [Overview](https://developers.cloudflare.com/turnstile/troubleshooting/client-side-errors/)
      * [Error codes](https://developers.cloudflare.com/turnstile/troubleshooting/client-side-errors/error-codes/)
    * [Challenge solve issues ↗︎](https://developers.cloudflare.com/cloudflare-challenges/troubleshooting/challenge-solve-issues/)
    * [Feedback reports](https://developers.cloudflare.com/turnstile/troubleshooting/feedback-reports/)
  * Extensions
    * [Pages Plugin ↗︎](https://developers.cloudflare.com/pages/functions/plugins/turnstile/)
    * [Google Firebase](https://developers.cloudflare.com/turnstile/extensions/google-firebase/)
    * [Waiting Room Analytics ↗︎](https://developers.cloudflare.com/waiting-room/waiting-room-analytics/#turnstile-widget-traffic)
  * Reference
    * [Content Security Policy](https://developers.cloudflare.com/turnstile/reference/content-security-policy/)
    * [Turnstile Privacy Addendum](https://www.cloudflare.com/turnstile-privacy-policy/)
    * [Supported languages](https://developers.cloudflare.com/turnstile/reference/supported-languages/)
    * [Supported browsers ↗︎](https://developers.cloudflare.com/cloudflare-challenges/reference/supported-browsers/)
  * [Community resources](https://developers.cloudflare.com/turnstile/community-resources/)
  * [Changelog](https://developers.cloudflare.com/turnstile/changelog/)
  * Agent resources
    * [Agent setup ↗︎](https://developers.cloudflare.com/agent-setup/)
    * [Cloudflare Skills ↗︎](https://github.com/cloudflare/skills)
    * [Code Mode MCP Server ↗︎](https://github.com/cloudflare/mcp)
    * [Domain-specific MCP Servers ↗︎MCP](https://github.com/cloudflare/mcp-server-cloudflare)
    * [Turnstile llms.txt ↗︎](https://developers.cloudflare.com/turnstile/llms.txt)
    * [Turnstile llms-full.txt ↗︎](https://developers.cloudflare.com/turnstile/llms-full.txt)
    * [Cloudflare Docs llms.txt ↗︎](https://developers.cloudflare.com/llms.txt)
    * [Cloudflare Docs llms-full.txt ↗︎](https://developers.cloudflare.com/llms-full.txt)


  1. [Home](https://developers.cloudflare.com/)
  2. /[Turnstile](https://developers.cloudflare.com/turnstile/)
  3. /[Get started](https://developers.cloudflare.com/turnstile/get-started/)
  4. /Validate the token


# Validate the token
Last updated Oct 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)
Overview Process Siteverify API overview Request format Basic validation examples Advanced validation techniques API response format Response fields Error codes reference Implementation Testing Best practices Security Performance Error handling
Learn how to securely validate Turnstile tokens on your server using the Siteverify API.
Mandatory server-side validation
You must call the Siteverify API to complete your Turnstile implementation. The client-side widget alone does not protect your forms.
Server-side validation is required because:
  * **Tokens can be forged.** An attacker can submit any string to your form endpoint without completing a challenge.
  * **Tokens expire.** Each token is valid for 300 seconds (5 minutes) after generation.
  * **Tokens are single-use.** Each token can only be validated once. A replayed token will be rejected with the `timeout-or-duplicate` error code.


## Process
[](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#process)
  1. Client generates token: Visitor completes Turnstile challenge on your webpage.
  2. Token sent to server: Form submission includes the Turnstile token.
  3. Server validates token: Your server calls Cloudflare's Siteverify API.
  4. Cloudflare responds: Returns `success` or `failure` and additional data.
  5. Server takes action: Allow or reject the original request based on validation.


## Siteverify API overview
[](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#siteverify-api-overview)
Endpointshell
```
POST https://challenges.cloudflare.com/turnstile/v0/siteverify
```

### Request format
[](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#request-format)
The API accepts both `application/x-www-form-urlencoded` and `application/json` requests, but always returns JSON responses.
#### Required parameters
[](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#required-parameters)  
| Parameter  | Required  | Description  |  
| --- | --- | --- |  
| `secret`  | Yes  | Your widget's secret key from the Cloudflare dashboard  |  
| `response`  | Yes  | The token from the client-side widget  |  
| `remoteip`  | No  | The visitor's IP address  |  
| `idempotency_key`  | No  | A UUID you generate to safely retry validation requests  |  
#### Token characteristics
[](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#token-characteristics)
  * Maximum length: 2048 characters
  * Validity period: 300 seconds (5 minutes) from generation
  * Single use: Each token can only be validated once
  * Automatic expiry: Tokens automatically expire and cannot be reused


The validation token issued by Turnstile is valid for five minutes. If a user submits the form after this period, the token is considered expired. In this scenario, the server-side verification API will return a failure, and the `error-codes` field in the response will include `timeout-or-duplicate`.
To ensure a successful validation, the visitor must initiate the request and submit the token to your backend within the five-minute window. Otherwise, the Turnstile widget needs to be refreshed to generate a new token. This can be done using the `turnstile.reset` function.
* * *
## Basic validation examples
[](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#basic-validation-examples)
JavaScriptPHPPythonJavaC#
#### JSON
[](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#json)

```
const SECRET_KEY = "your-secret-key";

async function validateTurnstile(token, remoteip) {
	try {
		const response = await fetch(
			"https://challenges.cloudflare.com/turnstile/v0/siteverify",
			{
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({
					secret: SECRET_KEY,
					response: token,
					remoteip: remoteip,
				}),
			},
		);

		const result = await response.json();
		return result;
	} catch (error) {
		console.error("Turnstile validation error:", error);
		return { success: false, "error-codes": ["internal-error"] };
	}
}
```

#### Form Data
[](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#form-data)

```
const SECRET_KEY = "your-secret-key";

async function validateTurnstile(token, remoteip) {
	const formData = new FormData();
	formData.append("secret", SECRET_KEY);
	formData.append("response", token);
	formData.append("remoteip", remoteip);

	try {
		const response = await fetch(
			"https://challenges.cloudflare.com/turnstile/v0/siteverify",
			{
				method: "POST",
				body: formData,
			},
		);

		const result = await response.json();
		return result;
	} catch (error) {
		console.error("Turnstile validation error:", error);
		return { success: false, "error-codes": ["internal-error"] };
	}
}

// Usage in form handler
async function handleFormSubmission(request) {
	const body = await request.formData();
	const token = body.get("cf-turnstile-response");
	const ip =
		request.headers.get("CF-Connecting-IP") ||
		request.headers.get("X-Forwarded-For") ||
		"unknown";

	const validation = await validateTurnstile(token, ip);

	if (validation.success) {
		// Token is valid - process the form
		console.log("Valid submission from:", validation.hostname);
		return processForm(body);
	} else {
		// Token is invalid - reject the submission
		console.log("Invalid token:", validation["error-codes"]);
		return new Response("Invalid verification", { status: 400 });
	}
}
```


```
<?php
function validateTurnstile($token, $secret, $remoteip = null) {
    $url = 'https://challenges.cloudflare.com/turnstile/v0/siteverify';

    $data = [
        'secret' => $secret,
        'response' => $token
    ];

    if ($remoteip) {
        $data['remoteip'] = $remoteip;
    }

    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => http_build_query($data),
        CURLOPT_HTTPHEADER => ['Content-Type: application/x-www-form-urlencoded'],
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_CONNECTTIMEOUT => 5,
        CURLOPT_TIMEOUT => 10,
    ]);

    $response = curl_exec($ch);
    $error = curl_error($ch);
    curl_close($ch);

    if ($response === false || $error !== '') {
        return ['success' => false, 'error-codes' => ['internal-error']];
    }

    return json_decode($response, true);

}

// Usage
$secret_key = 'your-secret-key';
$token = $_POST['cf-turnstile-response'] ?? '';
$remoteip = $_SERVER['HTTP_CF_CONNECTING_IP'] ??
$_SERVER['HTTP_X_FORWARDED_FOR'] ??
$_SERVER['REMOTE_ADDR'];

$validation = validateTurnstile($token, $secret_key, $remoteip);

if ($validation['success']) {
// Valid token - process form
echo "Form submission successful!";
// Process your form data here
} else {
// Invalid token - show error
echo "Verification failed. Please try again.";
error_log('Turnstile validation failed: ' . implode(', ', $validation['error-codes']));
}
?>
```


```
import requests

def validate_turnstile(token, secret, remoteip=None):
    url = 'https://challenges.cloudflare.com/turnstile/v0/siteverify'

    data = {
        'secret': secret,
        'response': token
    }

    if remoteip:
        data['remoteip'] = remoteip

    try:
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Turnstile validation error: {e}")
        return {'success': False, 'error-codes': ['internal-error']}

# Usage with Flask
from flask import Flask, request, jsonify

app = Flask(__name__)
SECRET_KEY = 'your-secret-key'

@app.route('/submit-form', methods=['POST'])
def submit_form():
    token = request.form.get('cf-turnstile-response')
    remoteip = request.headers.get('CF-Connecting-IP') or \
               request.headers.get('X-Forwarded-For') or \
               request.remote_addr

    validation = validate_turnstile(token, SECRET_KEY, remoteip)

    if validation['success']:
        # Valid token - process form
        return jsonify({'status': 'success', 'message': 'Form submitted successfully'})
    else:
        # Invalid token - reject submission
        return jsonify({
            'status': 'error',
            'message': 'Verification failed',
            'errors': validation['error-codes']
        }), 400
```


```
import org.springframework.web.client.RestTemplate;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;

@Service
public class TurnstileService {
private static final String SITEVERIFY_URL = "https://challenges.cloudflare.com/turnstile/v0/siteverify";
private final String secretKey = "your-secret-key";
private final RestTemplate restTemplate = new RestTemplate();

    public TurnstileResponse validateToken(String token, String remoteip) {
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);

        MultiValueMap<String, String> params = new LinkedMultiValueMap<>();
        params.add("secret", secretKey);
        params.add("response", token);
        if (remoteip != null) {
            params.add("remoteip", remoteip);
        }

        HttpEntity<MultiValueMap<String, String>> request = new HttpEntity<>(params, headers);

        try {
            ResponseEntity<TurnstileResponse> response = restTemplate.postForEntity(
                SITEVERIFY_URL, request, TurnstileResponse.class);
            return response.getBody();
        } catch (Exception e) {
            TurnstileResponse errorResponse = new TurnstileResponse();
            errorResponse.setSuccess(false);
            errorResponse.setErrorCodes(List.of("internal-error"));
            return errorResponse;
        }
    }

}

// Controller usage
@PostMapping("/submit-form")
public ResponseEntity<?> submitForm(
@RequestParam("cf-turnstile-response") String token,
HttpServletRequest request) {

    String remoteip = request.getHeader("CF-Connecting-IP");
    if (remoteip == null) {
        remoteip = request.getHeader("X-Forwarded-For");
    }
    if (remoteip == null) {
        remoteip = request.getRemoteAddr();
    }

    TurnstileResponse validation = turnstileService.validateToken(token, remoteip);

    if (validation.isSuccess()) {
        // Valid token - process form
        return ResponseEntity.ok("Form submitted successfully");
    } else {
        // Invalid token - reject submission
        return ResponseEntity.badRequest()
            .body("Verification failed: " + validation.getErrorCodes());
    }

}
```


```
using System.Text.Json;

public class TurnstileService
{
    private readonly HttpClient _httpClient;
    private readonly string _secretKey = "your-secret-key";
    private const string SiteverifyUrl = "https://challenges.cloudflare.com/turnstile/v0/siteverify";

    public TurnstileService(HttpClient httpClient)
    {
        _httpClient = httpClient;
    }

    public async Task<TurnstileResponse> ValidateTokenAsync(string token, string remoteip = null)
    {
        var parameters = new Dictionary<string, string>
        {
            { "secret", _secretKey },
            { "response", token }
        };

        if (!string.IsNullOrEmpty(remoteip))
        {
            parameters.Add("remoteip", remoteip);
        }

        var postContent = new FormUrlEncodedContent(parameters);

        try
        {
            var response = await _httpClient.PostAsync(SiteverifyUrl, postContent);
            var stringContent = await response.Content.ReadAsStringAsync();

            return JsonSerializer.Deserialize<TurnstileResponse>(stringContent);
        }
        catch (Exception ex)
        {
            return new TurnstileResponse
            {
                Success = false,
                ErrorCodes = new[] { "internal-error" }
            };
        }
    }
}

// Controller usage
[HttpPost("submit-form")]
public async Task<IActionResult> SubmitForm([FromForm] string cfTurnstileResponse)
{
    var remoteip = HttpContext.Request.Headers["CF-Connecting-IP"].FirstOrDefault() ??
                   HttpContext.Request.Headers["X-Forwarded-For"].FirstOrDefault() ??
                   HttpContext.Connection.RemoteIpAddress?.ToString();

    var validation = await _turnstileService.ValidateTokenAsync(cfTurnstileResponse, remoteip);

    if (validation.Success)
    {
        // Valid token - process form
        return Ok("Form submitted successfully");
    }
    else
    {
        // Invalid token - reject submission
        return BadRequest($"Verification failed: {string.Join(", ", validation.ErrorCodes)}");
    }
}
```

* * *
## Advanced validation techniques
[](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#advanced-validation-techniques)
Idempotency keys for retry operationjs
```
const crypto = require("crypto");

async function validateWithRetry(token, remoteip, maxRetries = 3) {
	const idempotencyKey = crypto.randomUUID();

	for (let attempt = 1; attempt <= maxRetries; attempt++) {
		try {
			const formData = new FormData();
			formData.append("secret", SECRET_KEY);
			formData.append("response", token);
			formData.append("remoteip", remoteip);
			formData.append("idempotency_key", idempotencyKey);

			const response = await fetch(
				"https://challenges.cloudflare.com/turnstile/v0/siteverify",
				{
					method: "POST",
					body: formData,
				},
			);

			const result = await response.json();

			if (response.ok) {
				return result;
			}

			// If this is the last attempt, return the error
			if (attempt === maxRetries) {
				return result;
			}

			// Wait before retrying (exponential backoff)
			await new Promise((resolve) =>
				setTimeout(resolve, Math.pow(2, attempt) * 1000),
			);
		} catch (error) {
			if (attempt === maxRetries) {
				return { success: false, "error-codes": ["internal-error"] };
			}
		}
	}
}
```
Enhanced validation with custom checksjs
```
async function validateTurnstileEnhanced(
	token,
	remoteip,
	expectedAction = null,
	expectedHostname = null,
) {
	const validation = await validateTurnstile(token, remoteip);

	if (!validation.success) {
		return {
			valid: false,
			reason: "turnstile_failed",
			errors: validation["error-codes"],
		};
	}

	// Check if action matches expected value (if specified)
	if (expectedAction && validation.action !== expectedAction) {
		return {
			valid: false,
			reason: "action_mismatch",
			expected: expectedAction,
			received: validation.action,
		};
	}

	// Check if hostname matches expected value (if specified)
	if (expectedHostname && validation.hostname !== expectedHostname) {
		return {
			valid: false,
			reason: "hostname_mismatch",
			expected: expectedHostname,
			received: validation.hostname,
		};
	}

	// Check token age (warn if older than 4 minutes)
	const challengeTime = new Date(validation.challenge_ts);
	const now = new Date();
	const ageMinutes = (now - challengeTime) / (1000 * 60);

	if (ageMinutes > 4) {
		console.warn(`Token is ${ageMinutes.toFixed(1)} minutes old`);
	}

	return {
		valid: true,
		data: validation,
		tokenAge: ageMinutes,
	};
}

// Usage
const result = await validateTurnstileEnhanced(
	token,
	remoteip,
	"login", // expected action
	"example.com", // expected hostname
);

if (result.valid) {
	// Process the request
	console.log("Validation successful:", result.data);
} else {
	// Handle validation failure
	console.log("Validation failed:", result.reason);
}
```

* * *
## API response format
[](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#api-response-format)
Successful responseFailed response
Examplejson
```
{
  "success": true,
  "challenge_ts": "2022-02-28T15:14:30.096Z",
  "hostname": "example.com",
  "error-codes": [],
  "action": "login",
  "cdata": "sessionid-123456789",
  "metadata": {
    "ephemeral_id": "x:9f78e0ed210960d7693b167e"
  }
}
```

Examplejson
```
{
  "success": false,
  "error-codes": ["invalid-input-response"]
}
```

### Response fields
[](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#response-fields)  
| Field  | Description  |  
| --- | --- |  
| `success`  | Boolean indicating if validation was successful  |  
| `challenge_ts`  | ISO 8601 timestamp when the challenge was solved  |  
| `hostname`  | Hostname where the challenge was served  |  
| `error-codes`  | Array of error codes (if validation failed)  |  
| `action`  | Custom action identifier from client-side  |  
| `cdata`  | Custom data payload from client-side  |  
| `metadata.ephemeral_id`  | Device fingerprint ID (Enterprise only)  |  
### Error codes reference
[](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#error-codes-reference)  
| Error code  | Description  | Action required  |  
| --- | --- | --- |  
| `missing-input-secret`  | Secret parameter not provided  | Ensure secret key is included  |  
| `invalid-input-secret`  | Secret key is invalid or expired  | Check your secret key in the Cloudflare dashboard  |  
| `missing-input-response`  | Response parameter was not provided  | Ensure token is included  |  
| `invalid-input-response`  | Token is invalid, malformed, or expired  | User should retry the challenge  |  
| `bad-request`  | Request is malformed  | Check request format and parameters  |  
| `timeout-or-duplicate`  | Token has already been validated  | Each token can only be used once  |  
| `internal-error`  | Internal error occurred  | Retry the request  |  
* * *
## Implementation
[](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#implementation)
Example implementationjs
```
class TurnstileValidator {
	constructor(secretKey, timeout = 10000) {
		this.secretKey = secretKey;
		this.timeout = timeout;
	}

	async validate(token, remoteip, options = {}) {
		// Input validation
		if (!token || typeof token !== "string") {
			return { success: false, error: "Invalid token format" };
		}

		if (token.length > 2048) {
			return { success: false, error: "Token too long" };
		}

		// Prepare request
		const controller = new AbortController();
		const timeoutId = setTimeout(() => controller.abort(), this.timeout);

		try {
			const formData = new FormData();
			formData.append("secret", this.secretKey);
			formData.append("response", token);

			if (remoteip) {
				formData.append("remoteip", remoteip);
			}

			if (options.idempotencyKey) {
				formData.append("idempotency_key", options.idempotencyKey);
			}

			const response = await fetch(
				"https://challenges.cloudflare.com/turnstile/v0/siteverify",
				{
					method: "POST",
					body: formData,
					signal: controller.signal,
				},
			);

			const result = await response.json();

			// Additional validation
			if (result.success) {
				if (
					options.expectedAction &&
					result.action !== options.expectedAction
				) {
					return {
						success: false,
						error: "Action mismatch",
						expected: options.expectedAction,
						received: result.action,
					};
				}

				if (
					options.expectedHostname &&
					result.hostname !== options.expectedHostname
				) {
					return {
						success: false,
						error: "Hostname mismatch",
						expected: options.expectedHostname,
						received: result.hostname,
					};
				}
			}

			return result;
		} catch (error) {
			if (error.name === "AbortError") {
				return { success: false, error: "Validation timeout" };
			}

			console.error("Turnstile validation error:", error);
			return { success: false, error: "Internal error" };
		} finally {
			clearTimeout(timeoutId);
		}
	}
}

// Usage
const validator = new TurnstileValidator(process.env.TURNSTILE_SECRET_KEY);

const result = await validator.validate(token, remoteip, {
	expectedAction: "login",
	expectedHostname: "example.com",
});

if (result.success) {
	// Process the request
} else {
	// Handle failure
	console.log("Validation failed:", result.error);
}
```

* * *
## Testing
[](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#testing)
You can test the dummy token generated with testing sitekey via Siteverify API with the testing secret key. Your production secret keys will reject dummy tokens.
Refer to [Testing](https://developers.cloudflare.com/turnstile/troubleshooting/testing/) for more information.
* * *
## Best practices
[](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#best-practices)
### Security
[](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#security)
  * Store your secret keys securely. Use environment variables or secure key management.
  * Validate the token on every request. Never trust client-side validation alone.
  * Check additional fields. Validate the action and hostname when specified.
  * Monitor for abuse and log failed validations and unusual patterns.
  * Use HTTPS. Always validate over secure connections.
  * Only call the Siteverify API in your backend environment. If you expose the secret key in the front-end client code to call Siteverify, attackers can bypass the security check. Ensure that your client-side code sends the validation token to your backend, and that your backend is the sole caller of the Siteverify API.


### Performance
[](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#performance)
  * Set reasonable timeouts. Do not wait indefinitely for Siteverify responses.
  * Implement retry logic and handle temporary network issues.
  * Cache validation results for the same token, if it is needed for your flow.
  * Monitor your API latency. Track the Siteverify response time.


### Error handling
[](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#error-handling)
  * Have fallback behavior for API failures.
  * Use user-friendly messaging. Do not expose internal error details to users.
  * Properly log errors for debugging without exposing secrets.
  * Rate limit to protect against validation flooding.


[PreviousWidget configurations](https://developers.cloudflare.com/turnstile/get-started/client-side-rendering/widget-configurations/)[NextMobile implementation](https://developers.cloudflare.com/turnstile/get-started/mobile-implementation/)
Was this helpful?
YesNo
[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/turnstile/get-started/server-side-validation.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
## On this page
  * [Overview](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#_top)
  * [Process](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#process)
  * [Siteverify API overview](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#siteverify-api-overview)
  * [Request format](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#request-format)
  * [Basic validation examples](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#basic-validation-examples)
  * [Advanced validation techniques](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#advanced-validation-techniques)
  * [API response format](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#api-response-format)
  * [Response fields](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#response-fields)
  * [Error codes reference](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#error-codes-reference)
  * [Implementation](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#implementation)
  * [Testing](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#testing)
  * [Best practices](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#best-practices)
  * [Security](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#security)
  * [Performance](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#performance)
  * [Error handling](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/#error-handling)


Was this helpful?
YesNo
[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/turnstile/get-started/server-side-validation.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)
Getting started
[Plans](https://www.cloudflare.com/plans/)[Contact sales](https://www.cloudflare.com/resource/contact-enterprise-sales/)[Partners](https://www.cloudflare.com/partners/)[Find a partner](https://partnerlocator.cloudflare.com/dashboard)[Startups](https://www.cloudflare.com/startups/)[Under attack?](https://www.cloudflare.com/under-attack-hotline/)[Domain name search](https://domains.cloudflare.com/)
Company
[About](https://www.cloudflare.com/about/)[Careers](https://www.cloudflare.com/careers/)[Investors](https://cloudflare.net/)[Press](https://www.cloudflare.com/press/)[Press kit](https://www.cloudflare.com/press/press-kit/)[Global network](https://www.cloudflare.com/network/)
Public interest
[Project Galileo](https://www.cloudflare.com/galileo/)[Athenian Project](https://www.cloudflare.com/athenian/)[Cloudflare for Campaigns](https://www.cloudflare.com/campaigns/)[Project Fairshot](https://www.cloudflare.com/fair-shot/)[Impact/ESG](https://www.cloudflare.com/impact/)
Compliance
[Compliance resources](https://www.cloudflare.com/trust-hub/compliance-resources/)[Trust Hub](https://www.cloudflare.com/trust-hub/)[Data Protection](https://www.cloudflare.com/trust-hub/gdpr/)[Responsible AI](https://www.cloudflare.com/trust-hub/responsible-ai/)[Transparency report](https://www.cloudflare.com/transparency/)[Report abuse](https://www.cloudflare.com/trust-hub/abuse-approach/)
Resources
[App innovation report](https://www.cloudflare.com/resource/app-innovation-report/)[Cloudflare Radar](https://radar.cloudflare.com/)[Case studies](https://www.cloudflare.com/case-studies/)[Status](https://www.cloudflarestatus.com/)[Support](https://support.cloudflare.com/)[Events](https://www.cloudflare.com/events/)[Blog](https://blog.cloudflare.com/)
Developers
[Documentation](https://developers.cloudflare.com/)[Learning center](https://www.cloudflare.com/learning/)[Community](https://community.cloudflare.com/)
Solutions
[SSE and SASE platform](https://www.cloudflare.com/sase/)[Cloudflare AI Cloud](https://www.cloudflare.com/solutions/ai/)[AI Security](https://www.cloudflare.com/solutions/ai-security/)[Frontend Development Platform](https://www.cloudflare.com/solutions/frontends/)[Multi-Tenant Platform Development](https://www.cloudflare.com/solutions/platforms/)[Web Security Platform](https://www.cloudflare.com/solutions/security/)
[Start Building](https://dash.cloudflare.com/sign-up)[Log In](https://dash.cloudflare.com/login)
© 2026 Cloudflare, Inc.
[Privacy policy](https://www.cloudflare.com/policies/privacy/)| [Report security issues](https://www.cloudflare.com/disclosure/)| [Terms of use](https://www.cloudflare.com/policies/terms/)| [Trademark](https://www.cloudflare.com/trademark/)
|
![privacy options](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=26,height=12,format=svg/_astro/privacyoptions.BWXSiJOZ.svg)Your privacy choices
[![](https://developers.cloudflare.com/_astro/logo.te5VL_aD.svg)Docs](https://developers.cloudflare.com/)

