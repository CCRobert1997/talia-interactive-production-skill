# Story and interaction

Use `story/node_graph.json` as the canonical creative structure. Keep stable IDs for the project, characters, environments, nodes, beats, images, and choices. Provider settings belong in shot orders rather than in the dramatic graph.

Each node should have a stable `id`, name, type, summary, beats, choices, and `auto_advance`. Each choice should have player-facing text, target node, interaction type, and optional presentation or tap-region data.

## Design checks

- State the player's dramatic question before branching.
- A choice represents an intention, value, risk, or strategy, not another Continue label.
- Give the player enough information to understand the decision.
- Show a visible consequence soon after selection.
- Branches need distinct emotional and causal outcomes even if they reconverge.
- Endings should resolve the promise of the choice.
- Put linear exposition in auto-advance nodes and meaningful decisions in explicit choices.
- Use tap regions only for stable, separated, readable, sufficiently large visible targets.

Tap coordinates are normalized `0..1` values: `x`, `y`, `w`, `h`. Regions must match visible objects, remain separated, avoid subtitles and UI-safe areas, and have an accessible hint when the object is ambiguous. Preserve a stable final hold for interaction.

Use real-tail continuity for an uninterrupted action, transformation, or reveal. Prefer a cut for a new place, time jump, montage beat, branch consequence, or camera grammar change.
