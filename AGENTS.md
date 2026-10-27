# Vintage (Holliewood and Vine)

Read `CLAUDE.md` in this folder for the project. This file adds the one rule Codex has been missing.

## Push when a task lands

Unpushed work is not done. When a task finishes, before a long wait, and before the session ends:

1. `git pull --rebase`
2. Grep the diff for secrets. `.env.local` is gitignored; never add it.
3. Commit only the files this task touched, with a message that says what changed.
4. `git push origin master`

If the push fails (sandbox blocks network, auth, conflict), say so in your final message with the exact error. Do not leave work uncommitted and stay quiet about it.

Pushing does not deploy. The live site is ChatGPT Sites and goes live only when it is published.
