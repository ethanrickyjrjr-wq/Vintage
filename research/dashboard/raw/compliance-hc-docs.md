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


# Healthchecks.io Documentation
Healthchecks.io is a service for monitoring cron jobs ([see guide](https://healthchecks.io/docs/monitoring_cron_jobs/)) and similar periodic processes:
  * Healthchecks.io **listens for HTTP requests ("pings")** from your cron jobs and scheduled tasks.
  * It **keeps silent** as long as pings arrive on time.
  * It **raises an alert** as soon as a ping does not arrive on time.


Healthchecks.io works as a [dead man's switch](https://en.wikipedia.org/wiki/Dead_man%27s_switch) for processes that need to run continuously or on a regular, known schedule. Some examples of jobs that would benefit from Healthchecks.io monitoring:
  * filesystem backups, database backups
  * task queues
  * database replication monitoring scripts
  * report generation scripts
  * periodic data import and sync jobs
  * periodic antivirus scans
  * DDNS updater scripts
  * SSL renewal scripts


Healthchecks.io is _not_ the right tool for:
  * monitoring website uptime by probing it with HTTP requests
  * collecting application performance metrics
  * log aggregation


## Concepts
A **Check** represents a single service you want to monitor. For example, when [monitoring cron jobs](https://healthchecks.io/docs/monitoring_cron_jobs/), you would create a separate check for each cron job to be monitored. Each check has a unique ping URL, schedule, and associated integrations. For the available configuration options, see [Configuring checks](https://healthchecks.io/docs/configuring_checks/).
Each check is always in one of the following states, depicted by a status icon:      **New**. A newly created check that has not received any pings yet. Each new check you create will start in this state.      **Up**. All is well. The last "success" signal has arrived on time.      **Late**. The "success" signal is due but has not arrived yet. It is not yet late by more than the check's configured **Grace Time**.      **Down**. The "success" signal has not arrived yet, and the Grace Time has elapsed. When a check transitions into the "Down" state, Healthchecks.io sends alert messages via the configured integrations.      **Paused**. You can manually pause the monitoring of specific checks. For example, if a frequently running cron job has a known problem, and a fix is in the works but not yet ready, you can pause monitoring the corresponding check temporarily to avoid unwanted alerts about a known issue.     Additionally, if the most recent received signal is a "start" signal, this will be indicated by three animated dots under the check's status icon.
* * *
**Ping URL**. Each check has a unique **Ping URL**. Clients (cron jobs, background workers, batch scripts, scheduled tasks, web services) make HTTP requests to the ping URL to signal a start of the execution, a success, or a failure.
Healthchecks.io supports two ping URL formats:
  * `https://hc-ping.com/<uuid>`  
The check is identified by its UUID. Check UUIDs are assigned automatically by Healthchecks.io, and are guaranteed to be unique.
  * `https://hc-ping.com/<project-ping-key>/<name-slug>`  
The check is identified by project's **Ping key** and check's **slug** (user-chosen, URL-friendly identifier). Optionally supports auto-provisioning: if you ping a slug value that does not have a corresponding check, Healthchecks.io can create the check automatically.


You can append `/start`, `/fail` or `/<exitcode>` to the base ping URL to send "start" and "failure" signals. The "start" and "failure" signals are optional. You don't have to use them, but you can gain additional monitoring insights if you do use them. See [Measuring script run time](https://healthchecks.io/docs/measuring_script_run_time/) and [Signaling failures](https://healthchecks.io/docs/signaling_failures/) for details.
You should treat check UUIDs and project Ping keys as secrets. If you make them public, anybody can send telemetry signals to your checks and mess with your monitoring.
Read more about Ping URLs in [Pinging API](https://healthchecks.io/docs/http_api/).
* * *
**Grace Time** is one of the configuration parameters you can set for each check. It is the additional time to wait before sending an alert when a check is late. Use this parameter to account for minor, expected deviations in job execution times.
When a check is considered _late_ depends on whether the check uses a simple or cron schedule, and whether or not you are [tracking job durations](https://healthchecks.io/docs/measuring_script_run_time/) using the "start" events.
For **simple schedules** , the check is late when the checks's configured period has passed. For example, consider a periodic task that should run every hour, and the gaps between runs should not deviate by more than 5 minutes (Period = 1 hour, Grace Time = 5 minutes). And let's say the last successful ping arrived at 12:00.
  * At 13:00 the check will be declared late (because 1 hour will have passed since the last ping).
  * At 13:05 the check will be declared down and the alerts will go out (because 1 hour + 5 minutes will have passed since the last ping).


For **cron and OnCalendar schedules** , the check enters the late state at the exact moment when the current wall clock time matches the schedule. Let's consider a cron job with the schedule `10 * * * *` (10 minutes past every hour) and grace time of 5 minutes. And let's say the last successful ping arrived at 12:30.
  * At 13:10 the check will be declared late (because 13:10 is the next scheduled time the cron job is expected to send a ping according to the cron schedule).
  * At 13:15 the check will be declared down and the alerts will go out (because 5 minutes will have passed since the time the cron job was expected to check in).


If you use "start" signals to [measure job execution time](https://healthchecks.io/docs/measuring_script_run_time/), Grace Time also sets the maximum allowed time gap between "start" and "success" signals. If a job sends a "start" signal but does not send a "success" signal within grace time, Healthchecks.io will assume failure and send out alerts.
* * *
An **Integration** is a specific method for delivering monitoring alerts when a check's change states. Healthchecks.io supports many types of integrations: email, webhooks, SMS, Slack, PagerDuty, etc. You can set up multiple integrations. For each check, you can specify which integrations it should use.
For more information on integrations, see [Configuring notifications](https://healthchecks.io/docs/configuring_notifications/).
* * *
**Project**. To keep things organized, you can group checks and integrations in **Projects**. Your account starts with a single default project, but you can create additional projects as needed. You can transfer existing checks between projects while preserving their configuration and ping URLs.
Each project has a configurable name, a separate set of API keys, and a separate project team. The project's team is the set of people you have granted read-only or read-write access to the project.
For more information on projects, see [Projects and teams](https://healthchecks.io/docs/projects_teams/).
  * © 2015-2026 SIA Monkey See Monkey Do
  * [Terms](https://healthchecks.io/terms/)
  * [Privacy](https://healthchecks.io/privacy/)
  * [Pricing](https://healthchecks.io/pricing/)
  * [FAQ](https://healthchecks.io/faq/)
  * [API](https://healthchecks.io/docs/api/)
  * [Blog](https://blog.healthchecks.io)
  * [Contact](https://healthchecks.io/about/)
  * [Status](https://status.healthchecks.io/)



