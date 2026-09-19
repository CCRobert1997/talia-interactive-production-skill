# Talia Interactive Production Skill

[中文说明](README.zh-CN.md)

A model-agnostic skill for designing and producing Talia interactive image and video stories, from branching script and media generation orders to QA and a validated Talia draft.

Choose one language package and copy the whole folder into the skill directory supported by your agent harness:

- English: `skills/en/talia-interactive-production/`
- 简体中文: `skills/zh-CN/talia-interactive-production/`

Both packages have the same workflow, safety boundary, validation scripts, and skill name. Install only one language variant in a given skill root.

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

Python 3 is required. `ffprobe` is required for media inspection. Talia CLI and media/browser tools are optional capabilities supplied by the host environment.

## License

Apache-2.0.
