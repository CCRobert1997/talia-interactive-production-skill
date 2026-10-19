# Talia Interactive Production Skill

[中文说明](README.zh-CN.md)

A model-agnostic agent skill for designing and producing Talia interactive image and video stories: branching script, media generation orders, QA gates, and a validated Talia draft assembled through the Talia CLI.

Works with any harness that reads the [Agent Skills](https://agentskills.io) `SKILL.md` format (Claude Code, OpenAI Codex, Cursor, OpenCode, and others), and with instruction-only harnesses through a one-paragraph pointer.

## Install

One command, several harnesses:

```bash
npx skills@latest add CCRobert1997/talia-interactive-production-skill \
  --agent claude-code --agent codex --agent cursor
```

Or copy `skills/talia-interactive-production/` into your harness's skill directory:

| Harness | Path |
|---|---|
| Claude Code | `~/.claude/skills/` (user) or `.claude/skills/` (project) |
| OpenAI Codex | `~/.codex/skills/` (user) or `.codex/skills/` (project) |
| No skill discovery | keep the folder in the repo and add the pointer from [harness-installation.md](skills/talia-interactive-production/references/harness-installation.md) to `AGENTS.md` / `CLAUDE.md` / your system prompt |

English `SKILL.md` is what the agent loads. A Simplified Chinese translation for human readers lives in `skills/talia-interactive-production/i18n/zh-CN/`.

## Layout

```
skills/talia-interactive-production/
├── SKILL.md                 # entry point, loaded by the harness
├── agents/openai.yaml       # Codex display metadata (optional)
├── references/              # loaded on demand from SKILL.md
│   ├── capability-routing.md
│   ├── harness-installation.md
│   ├── media-production.md
│   ├── qa-gates.md
│   ├── story-and-interaction.md
│   └── talia-cli.md
├── scripts/                 # Python 3, no third-party deps
│   ├── capability_probe.py
│   ├── validate_node_graph.py
│   └── inspect_media.py     # needs ffprobe
└── i18n/zh-CN/              # translation of SKILL.md + references
```

## Safety boundary

The skill can assemble and validate Talia drafts, including replacing an existing node image or video URL. It does not invoke Talia paid generation, publishing, unpublishing, deletion, billing, credits, subscriptions, passwords, or account management. The creator performs those actions manually in the Talia UI.

## Model and harness compatibility

The workflow routes by observed capability rather than model brand. Image generation, image/video understanding, browser upload, shell access, and persistent authentication usually depend on both the model and its harness. Unsupported work must be reported as `prepared` or `unverified`, never as complete.

## Included tools

```bash
python3 scripts/capability_probe.py
python3 scripts/validate_node_graph.py path/to/story/node_graph.json
python3 scripts/inspect_media.py path/to/video.mp4
```

Python 3 is required. `ffprobe` is required for media inspection. The Talia CLI and media/browser tools are optional capabilities supplied by the host environment.

## License

Apache-2.0.
