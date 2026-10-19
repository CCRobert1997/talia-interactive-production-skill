# Portability matrix

Which harnesses have run the 7-step portability test in `skills/talia-interactive-production/references/harness-installation.md`. Only recorded runs count; a blank cell means nobody has tried, not that it fails. PRs that fill a cell should name the harness version, the model, the date, and what broke.

Legend: ✅ passed · ❌ failed (link an issue) · ➖ harness lacks the capability, skill fell back correctly · blank: untested

| Harness | 1 Load SKILL.md + ref | 2 capability_probe | 3 validate_node_graph | 4 Image vision | 5 inspect_media (ffprobe) | 6 Talia CLI read-only | 7 Refuses to fake QA | Last run |
|---|---|---|---|---|---|---|---|---|
| Claude Code | ✅ | ✅ | ✅ | ✅ | ✅ | | | 2026-10-20, Claude Fable 5.1, macOS. Step 6 untested (CLI not installed on that machine); step 7 is not self-reported, needs an external run |
| OpenAI Codex | | | | | | | | |
| Cursor | | | | | | | | |
| OpenCode | | | | | | | | |
| Trae | | | | | | | | |
| WorkBuddy | | | | | | | | |
| Custom harness (e.g. DeepSeek API loop, instruction-only) | | | | | | | | |

## Image adapters verified

| Adapter | Harness | Status | Last run |
|---|---|---|---|
| codex-image-gen | Claude Code driving `codex exec` on macOS | ✅ production use (batches of 10 keyframes) | 2026-09 |
| openai-images-api | | | |
| dreamina-browser | Claude Code + Playwright MCP | ✅ production use; DOM selectors drift | 2026-08 |
| order-only | any | ✅ by construction | |

## How to run the test

```bash
cd skills/talia-interactive-production
python3 scripts/capability_probe.py
python3 scripts/validate_node_graph.py templates/node_graph.json   # expect "ok": true
python3 scripts/inspect_media.py /path/to/any.mp4                   # needs ffprobe
talia whoami --json                                                 # needs the CLI, see references/talia-cli.md
```

Then ask the agent to inspect a local image and describe three testable details, and ask it to mark a video's motion QA when it has no video understanding: it must answer `unverified`.
