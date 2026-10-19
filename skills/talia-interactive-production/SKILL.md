---
name: talia-interactive-production
description: Design and produce Talia interactive image or video stories from branching script through media QA and a validated draft. Use when creating, continuing, auditing, or assembling a Talia project; do not use for publishing, deletion, account management, or paid generation through Talia.
---

# Talia Interactive Production

Produce a reviewable Talia draft from story design, character and environment anchors, images, video, audio, and interaction wiring. Treat the project manifest and local media as the production record. Prompts alone are prepared work, not completed media.

## Discover capabilities first

Run `scripts/capability_probe.py` in an unfamiliar harness and read [capability routing](references/capability-routing.md). Route by demonstrated capabilities rather than model names. Install paths and the instruction-only fallback are in [harness installation](references/harness-installation.md).

Use exactly one status for each deliverable:

- `complete`: artifact exists and passed the applicable QA gate.
- `prepared`: instructions or prompts are ready, but an external operation has not run.
- `unverified`: artifact exists, but the harness cannot perform the required visual, audio, or interaction check.

## Resume before producing

Read workspace instructions, project context, production status, node graph, QA log, identity sheets, environment anchors, and relevant shot orders. Verify recorded status against actual files and read-only remote state. Preserve stable IDs, filenames, accepted assets, story decisions, language, style, and delivery structure.

For a new project, create `story/node_graph.json` before media production. For an existing project, update its graph instead of creating a competing source of truth. Read [story and interaction](references/story-and-interaction.md) when designing or revising it.

## Pass explicit gates

1. **G0 Story:** every choice represents a meaningful intention and leads to a distinct consequence; every non-ending path reaches an ending.
2. **G1 Anchors:** approve character identity sheets and environment anchors.
3. **G2 Images:** inspect identity, anatomy, props, space, story state, text, watermark, and interaction layout.
4. **G3 Video:** inspect first/last/key frames, motion causality, drift, dialogue, ambience, and audio.
5. **G4 Node master:** normalize accepted media and verify technical delivery facts.
6. **G5 Talia draft:** upload accepted media, assemble nodes/choices/interactions, and validate.
7. **G6 Creator review:** the creator manually handles Talia paid generation, publishing, unpublishing, deletion, billing, credits, and account actions.

Read [media production](references/media-production.md) for G1–G4 and [QA gates](references/qa-gates.md) for rejection criteria.

## Preserve identity and use continuity intentionally

Always retain the original identity sheets as references. Generated frames or real extracted tails may add pose and temporal continuity but must not become the only identity anchors.

Use a real tail frame for a continuous action, transformation, or reveal. Prefer a clean cut for changes of location, time, dramatic beat, or camera grammar.

Choose video reference mode by need:

- `First Frame`: one approved frame fully specifies the starting cast and scene.
- `First + Last Frame`: both endpoints require control and the engine supports it.
- `Omni reference`: extra identity, environment, prop, or style references are necessary.

Do not use Omni by habit when a first frame already contains all required information.

## Operate Talia within the safe boundary

Read [Talia CLI](references/talia-cli.md) before changing a draft.

Allowed work includes inspection; upload of already-produced assets; creation and update of draft nodes, choices, presentation, tap regions, start node, auto-advance, variables, and achievements; replacement of an existing node image or video URL; outline import; and validation.

Do not invoke or wrap Talia paid generation, publishing, unpublishing, deletion, billing, credits, subscriptions, passwords, or account management. Never publish as a side effect of assembly or validation.

Before mutation, record the target project ID and current values. After mutation, record affected IDs/URLs and run validation. Preview every route in the creator UI before the creator publishes manually.

## Keep an auditable record

For every media artifact record its node/shot purpose, exact references and final prompt, provider/model/settings, local path, remote job/URL, actual cost when known, QA result or rejection reason, replacement version, and applied Talia node.

Use `scripts/validate_node_graph.py` for structural checks and `scripts/inspect_media.py` for local media facts. Scripts support QA; they do not replace visual or listening review.
