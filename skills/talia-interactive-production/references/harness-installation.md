# Harness installation and adaptation

The portable unit is the whole `talia-interactive-production/` folder. Keep `SKILL.md`, `references/`, `scripts/`, and `agents/` together: links are relative.

## One-line install (Agent Skills standard)

Any harness that follows the Agent Skills open standard (`<name>/SKILL.md` with YAML frontmatter) can take the folder as-is. The `skills` CLI installs into several harnesses at once:

```bash
npx skills@latest add CCRobert1997/talia-interactive-production-skill \
  --agent claude-code --agent codex --agent cursor
```

Drop `--agent` to be prompted. A project install keeps one copy under `.agents/skills/<name>/` and links each harness to it.

## Manual install paths

| Harness | User scope | Project scope | Notes |
|---|---|---|---|
| Claude Code | `~/.claude/skills/<name>/` | `.claude/skills/<name>/` | Discovers `SKILL.md` frontmatter automatically |
| OpenAI Codex | `~/.codex/skills/<name>/` | `.codex/skills/<name>/` | Reads `agents/openai.yaml` for display metadata; optional |
| Cursor / OpenCode / others on the standard | per harness docs | per harness docs | Same folder, no changes |
| Harness without skill discovery (e.g. a custom DeepSeek harness, Trae, WorkBuddy, a plain API loop) | — | anywhere in the repo | Use the instruction-only route below |

Confirm paths against the harness's current documentation rather than a model name. `<name>` is `talia-interactive-production`.

## Instruction-only harnesses

If the harness has no skill discovery, point its project instructions at `SKILL.md`. Paste into `AGENTS.md`, `CLAUDE.md`, `.cursorrules`, a Trae project rule, or the system prompt:

```markdown
## Talia interactive production
For any task that designs, continues, audits, or assembles a Talia interactive
story (image or video), first read `skills/talia-interactive-production/SKILL.md`
and follow it. Load files under its `references/` only when SKILL.md points to
them. Never publish, delete, or trigger paid generation through Talia; leave
those to the creator in the Talia UI.
```

Keep the folder structure intact so relative links resolve. Run `scripts/*.py` through the harness's shell tool when one exists. Without shell or vision, follow the fallback states in `capability-routing.md` and report work as `prepared` or `unverified`.

## Capability adapters

Do not fork the core workflow per model. Add a small adapter note only when tool invocation differs. An adapter may document:

- how to pass local images to vision;
- how to invoke the available image generator;
- how to extract or inspect video;
- how browser uploads work;
- where the Talia CLI executable lives;
- where authenticated sessions are stored, without exposing secrets.

Adapters must not weaken the boundaries around Talia paid generation, publishing, deletion, billing, credits, or account management.

## Portability test

A harness is ready when it can:

1. load `SKILL.md` and one linked reference;
2. run `scripts/capability_probe.py`, or explain why shell is unavailable;
3. validate a small test `node_graph.json` with `scripts/validate_node_graph.py`;
4. inspect a local image when vision is claimed;
5. inspect media metadata with `scripts/inspect_media.py` when `ffprobe` is claimed;
6. run a read-only Talia CLI command when CLI support is claimed;
7. refuse to mark unsupported visual or audio QA as `complete`.

## Chinese translation

`i18n/zh-CN/` holds a Simplified Chinese translation of `SKILL.md` and `references/` for human readers. English is canonical and the translation may lag; the harness loads the English `SKILL.md`.
