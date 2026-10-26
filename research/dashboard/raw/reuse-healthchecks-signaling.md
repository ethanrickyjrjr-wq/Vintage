Toggle navigation [ ![Healthchecks.io](https://healthchecks.io/static/img/logo-rounded-ua2.svg) ](https://healthchecks.io/)
  * [Pricing](https://healthchecks.io/pricing/)
  * [Docs](https://healthchecks.io/docs/)
  * [Blog](https://blog.healthchecks.io/)
  * [About](https://healthchecks.io/about/)
  * [Log In](https://healthchecks.io/accounts/login/)


  * Healthchecks.io
  * [Introduction](https://healthchecks.io/docs/)
  * [Configuring checks](https://healthchecks.io/docs/configuring_checks/)
  * [Configuring notifications](https://healthchecks.io/docs/configuring_notifications/)
  * [Projects and teams](https://healthchecks.io/docs/projects_teams/)
  * [Badges](https://healthchecks.io/docs/badges/)
  * [FAQ](https://healthchecks.io/faq/)
  * API
  * [Pinging API](https://healthchecks.io/docs/http_api/)
  * [Management API](https://healthchecks.io/docs/api/)
  * [Slug URLs](https://healthchecks.io/docs/slug_urls/)
  * Guides
  * [Monitoring cron jobs](https://healthchecks.io/docs/monitoring_cron_jobs/)
  * [Monitoring Systemd tasks](https://healthchecks.io/docs/monitoring_systemd_tasks/)
  * [Signaling failures](https://healthchecks.io/docs/signaling_failures/)
  * [Measuring script run time](https://healthchecks.io/docs/measuring_script_run_time/)
  * [Attaching logs](https://healthchecks.io/docs/attaching_logs/)
  * [Cloning checks](https://healthchecks.io/docs/cloning_checks/)
  * [Auto provisioning](https://healthchecks.io/docs/autoprovisioning/)
  * [Configuring Prometheus](https://healthchecks.io/docs/configuring_prometheus/)
  * Pinging Examples
  * [Reliability tips](https://healthchecks.io/docs/reliability_tips/)
  * [Shell scripts](https://healthchecks.io/docs/bash/)
  * [Arduino](https://healthchecks.io/docs/arduino/)
  * [Network Routers](https://healthchecks.io/docs/network_routers/)
  * [C#](https://healthchecks.io/docs/csharp/)
  * [Email](https://healthchecks.io/docs/email/)
  * [GitHub Actions](https://healthchecks.io/docs/github_actions/)
  * [Go](https://healthchecks.io/docs/go/)
  * [Javascript](https://healthchecks.io/docs/javascript/)
  * [PHP](https://healthchecks.io/docs/php/)
  * [PowerShell](https://healthchecks.io/docs/powershell/)
  * [Python](https://healthchecks.io/docs/python/)
  * [Ruby](https://healthchecks.io/docs/ruby/)
  * Developer Tools
  * [Third-party resources](https://healthchecks.io/docs/resources/)
  * Self-hosted
  * [Overview](https://healthchecks.io/docs/self_hosted/)
  * [Configuration](https://healthchecks.io/docs/self_hosted_configuration/)
  * [Running with Docker](https://healthchecks.io/docs/self_hosted_docker/)
  * Reference
  * [Cron syntax cheatsheet](https://healthchecks.io/docs/cron/)
  * [Compared to Sentry](https://healthchecks.io/docs/healthchecks_sentry_comparison/)
  * [Compared to Cronitor](https://healthchecks.io/docs/healthchecks_cronitor_comparison/)


# Signaling failures
You can actively signal a failure to Healthchecks.io by slightly changing the ping URL: append either `/fail` or `/{exit-status}` to your normal ping URL. The exit status should be a 0-255 integer. Healthchecks.io will interpret exit status 0 as success and all non-zero values as failures.
Examples:

```
# Reports failure by appending the /fail suffix:
curl --retry 3 https://hc-ping.com/your-uuid-here/fail

# Reports failure by appending a non-zero exit status:
curl --retry 3 https://hc-ping.com/your-uuid-here/1

```

By actively signaling failures to Healthchecks.io, you can minimize the delay from your monitored service encountering a problem to you getting notified about it.
Alternatively, if using different URLs for success and failure signals is not feasible, you can configure Healthchecks.io to classify HTTP pings as success or failure signals [by looking for specific keywords in the HTTP request body](https://healthchecks.io/docs/configuring_checks/#filtering-rules).
## Shell Scripts
The below shell script appends `$?` (a special variable that contains the exit status of the last executed command) to the ping URL:

```
#!/bin/sh

/usr/bin/certbot renew
curl --retry 3 https://hc-ping.com/your-uuid-here/$?

```

## Python
Below is a skeleton code example in Python which signals a failure when the work function returns an unexpected value or throws an exception:

```
import requests
URL = "https://hc-ping.com/your-uuid-here"

def do_work():
    # Do your number crunching, backup dumping, newsletter sending work here.
    # Return a truthy value on success.
    # Return a falsy value or throw an exception on failure.
    return True

success = False
try:
    success = do_work()
finally:
    # On success, requests https://hc-ping.com/your-uuid-here
    # On failure, requests https://hc-ping.com/your-uuid-here/fail
    requests.get(URL if success else URL + "/fail")

```

  * © 2015-2026 SIA Monkey See Monkey Do
  * [Terms](https://healthchecks.io/terms/)
  * [Privacy](https://healthchecks.io/privacy/)
  * [Pricing](https://healthchecks.io/pricing/)
  * [FAQ](https://healthchecks.io/faq/)
  * [API](https://healthchecks.io/docs/api/)
  * [Blog](https://blog.healthchecks.io)
  * [Contact](https://healthchecks.io/about/)
  * [Status](https://status.healthchecks.io/)



