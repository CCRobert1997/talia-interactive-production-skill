# Safe Talia CLI use

## Install

The CLI is open source at <https://github.com/CCRobert1997/talia-cli> (MIT). It ships a prebuilt single file, so installation needs only Node 20+:

```bash
npm i -g github:CCRobert1997/talia-cli
talia login you@example.com     # same creator account as editor.taliaapp.com
talia whoami
```

If `talia` is already on `PATH` in the workspace, use it as is. Inside the Talia editor monorepo the equivalent is `npm run cli -- <command>`.

Without `SUPABASE_URL` / `SUPABASE_ANON_KEY` the CLI targets the production Talia backend; the embedded anon key is public and RLS scopes every write to the logged-in creator. Set the two variables (or `~/.talia/config.json`) to point at another instance.

## Read machine-readable output

Every read command accepts `--json` and prints one JSON line; write commands with `--json` print `{"ok":true,"id":"…"}`. Prefer `--json` over parsing prose output. Begin with read-only checks:

```bash
talia whoami --json
talia projects --json
talia validate <projectId> --json
```

## Allowed

The skill may create a draft project; add and update nodes; set title, image, video, and auto-advance; set the start node; add/update choices; configure presentation, tap regions, and interaction templates; add variables and achievements; upload already-produced assets; import an outline; list state; and validate.

Replacing an existing node video or image URL is allowed. Record the node ID, old URL, intended new URL, and accepted local source before replacement. Replacement does not authorize deletion of the old asset.

## Excluded

Do not invoke or wrap commands that generate paid media through Talia; publish, update a published snapshot, or unpublish; delete projects, choices, assets, variables, achievements, or remote media; or change billing, credits, subscriptions, passwords, or account settings.

The installed CLI may expose excluded commands. Their presence does not include them in this skill.

## Mutation procedure

1. Confirm project ID using project records and read-only output.
2. Confirm every local media artifact passed QA.
3. Record current IDs and old values.
4. Apply the smallest changes.
5. Run `talia validate <projectId>`.
6. Record commands, affected IDs/URLs, validation output, and remaining creator actions.
7. Preview every route in the UI; the creator publishes manually.

Never put credentials in shell history, project files, examples, or logs. Use the CLI credential store or the environment's secure login flow.
