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


# Configuring Checks
In Healthchecks.io, a **Check** represents a single service you want to monitor. For example, when monitoring cron jobs, you would create a separate check for each cron job you wish to monitor. Healthchecks.io pricing plans are structured primarily around how many checks you can have in your account. You can create checks in the Healthchecks.io web interface or via [Management API](https://healthchecks.io/docs/api/).
## Name, Tags, Description
Describe each check using an optional name, slug, tags, and description fields.
![Editing name, tags and description](https://healthchecks.io/static/img/docs/edit_name.png)
  * **Name** : names are optional, but setting them is a good idea. Good naming becomes especially important as you add more checks to the account. Healthchecks.io will display check names in the web interface, email reports, and notifications.
  * **Slug** : URL-friendly identifier used in [slug-based ping URLs](https://healthchecks.io/docs/http_api/#success-slug) (an alternative to the default UUID-based ping URLs). The slug should only contain the following characters: `a-z`, `0-9`, hyphens, and underscores. If you don't plan to use slug-based ping URLs, you can leave the slug field empty.
  * **Tags** : a space-separated list of optional labels. Use tags to organize and group checks within a project. You can tag checks by the environment (`prod`, `staging`, `dev`, etc.), by role (`www`, `db`, `worker`, etc.), or by using any other system.
  * **Description** : a free-form text field with any related information for your team or your future self. Describe the cron job's role, who set it up, what to do in case of failures, and where to look for additional information.


## Simple Schedules
Healthchecks.io supports three types of schedules: **Simple** , **Cron** , and **OnCalendar**. Use Simple schedules for monitoring processes that you expect to run at relatively regular intervals: once an hour, once a day, once a week, etc.
![Editing the period and grace time](https://healthchecks.io/static/img/docs/edit_simple_schedule.png)
For the simple schedules, you can configure two parameters, Period and Grace Time.
  * **Period** is the expected time between pings.
  * **Grace Time** is the additional time to wait before sending an alert when a check is late. Use this parameter to account for minor, expected deviations in job execution times.


Note: if you use the "start" signal to [measure job run times](https://healthchecks.io/docs/measuring_script_run_time/), then Grace Time also specifies the maximum allowed time gap between "start" and "success" signals. Whenever Healthchecks.io receives a "start" signal, it expects a subsequent "success" signal within Grace Time. If the success signal does not arrive within the configured Grace Time, Healthchecks.io will mark the check as failed and send out alerts.
## Cron Schedules
Use "Cron" for monitoring cron jobs and other processes with more complex schedules. This monitoring mode ensures that jobs run **at the correct time** and not just at the correct time intervals.
See [Cron syntax cheatsheet](https://healthchecks.io/docs/cron/) for cron expression syntax examples. See [crontab(5) man page](https://www.man7.org/linux/man-pages/man5/crontab.5.html) for complete cron syntax reference.
![Editing cron schedule](https://healthchecks.io/static/img/docs/edit_cron_schedule.png)
You will need to specify Cron Expression, Server's Time Zone, and Grace Time.
  * **Cron Expression** is the cron expression you specified in the crontab.
  * **Server's Time Zone** is the timezone of your server. The cron daemon typically uses the system's local time. If the machine does not use the UTC timezone, specify its timezone here.
  * **Grace Time** , same as for simple schedules, is how long to wait before sending an alert for a late check.


## OnCalendar Schedules
Use "OnCalendar" schedules to monitor systemd timers that use `OnCalendar=` schedules. Same as with systemd timers, you can specify more than one `OnCalendar` expression (separated with newlines, one schedule per line), and Healthchecks.io will expect a ping whenever any schedule matches.
See [systemd.time(7) man page](https://www.man7.org/linux/man-pages/man7/systemd.time.7.html#CALENDAR_EVENTS) for complete OnCalendar syntax reference.
![Editing cron schedule](https://healthchecks.io/static/img/docs/edit_oncalendar_schedule.png)
## Filtering Rules
In the "Filtering Rules" dialog, you can control several advanced aspects of how Healthchecks.io handles incoming pings for a particular check.
![Setting filtering rules](https://healthchecks.io/static/img/docs/filtering_rules.png)
  * **Allowed HTTP Request Methods**. You can require the ping requests to use HTTP POST. Use the "Only POST" option if you run into issues of preview bots hitting the ping URLs when you send them in email or post them in chat.
  * **Content Filtering**. You can instruct Healthchecks.io to look for specific keywords in the subject line or the message body of email pings, and in the HTTP request body of HTTP pings.
  * **Pinging a Paused Check**. Normally, when you ping a paused check, it leaves the paused state and goes into the "up" state (or the "down" state in case of [a failure signal](https://healthchecks.io/docs/signaling_failures/)). You can change this behavior by selecting the "Ignore the ping, stay in the paused state" option. With this option selected, the paused state becomes "sticky": Healthchecks.io will ignore all incoming pings until you explicitly _resume_ the check.


### Content Filtering
If the **Request body of HTTP requests** option is checked, Healthchecks.io will classify the HTTP pings as start, success, or failure signals by looking for keywords in the first 100 kB of the request body.
If either the **Subject line of email messages** or the **Message body of email messages** option is checked, Healthchecks.io will classify email pings as start, success, or failure signals by looking for keywords in the subject line and/or message body. Healthchecks.io supports HTML emails: when looking for keywords in message body, it checks both plain text and HTML versions of the email.
You can specify multiple keywords in each of the **Start Keywords** , **Success Keywords** , and **Failure Keywords** fields by separating them with commas. The keyword matching is case-sensitive (for example, "error" and "ERROR" are different keywords).
Healthchecks.io looks for keywords in a specific order:
  * It first looks for **failure keywords**. If any are found, it classifies the ping as a failure signal and does not look further.
  * It then looks for **success keywords**. If any are found, it classifies the ping as a success signal and does not look further.
  * It then looks for **start keywords**. If any are found, it classifies the ping as a start signal.
  * Finally, if no matching keywords are found, Healthchecks.io either ignores the ping or classifies it as a failure signal, depending on the **If no keywords match** configuration option. Ignored pings are shown in the event log with an "Ignored" label, but they do not affect check's status as they are neither "success" nor "failure" nor "start" signals.


Example use case: consider a backup cron job that sends an HTTP POST request every time it completes. If the job completes successfully, the HTTP request will contain text "Backup successful". If the job fails, the request body will contain an error message. The error messages can vary, and the complete list of all possible error messages is not known. To handle this scenario, you can use content filtering as follows:
  * Enable the **Request body of HTTP requests** – enables content filtering for HTTP pings.
  * In the **Success keywords** field enter "Backup successful" – if this string is found in the request body of a HTTP ping, Healthchecks.io will classify the ping as a success signal.
  * Select the **If no keywords match: Classify the ping as failure** option – Healthchecks.io will classify all other HTTP requests as failure signals.


With these settings, Healthchecks.io will classify a HTTP ping as a success signal if and only if the request body contains text "Backup successful". If the request body does not contain this string (or the request body is absent altogether), it will classify the ping as a failure signal.
  * © 2015-2026 SIA Monkey See Monkey Do
  * [Terms](https://healthchecks.io/terms/)
  * [Privacy](https://healthchecks.io/privacy/)
  * [Pricing](https://healthchecks.io/pricing/)
  * [FAQ](https://healthchecks.io/faq/)
  * [API](https://healthchecks.io/docs/api/)
  * [Blog](https://blog.healthchecks.io)
  * [Contact](https://healthchecks.io/about/)
  * [Status](https://status.healthchecks.io/)



