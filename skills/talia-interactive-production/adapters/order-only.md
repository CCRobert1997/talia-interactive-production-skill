# Adapter: order only (no generator available)

The harness cannot generate images. Produce a self-contained order a human or another agent can execute elsewhere, mark the image `prepared`, and stop at that gate.

## Output

One file per image at `orders/<img_id>.md`, written from `templates/image_order.md`, with every section filled. Self-contained means a stranger with only this file and the referenced anchor images can produce the shot: absolute project paths, numbered references with roles, the full prompt, size and ratio, negative constraints, the target save path, and the acceptance checks.

Also append a row to the handoff record with status `prepared`, provider `none`, and the order path.

## What not to do

- Do not invent a placeholder image or reuse an unrelated file to "unblock" the graph.
- Do not mark the node, the beat, or G2 as complete.
- Do not run Talia `node set image` with a missing or placeholder URL.

## Resuming

When the image arrives, the agent places it at the target path, runs G2 against the acceptance checks in the order, updates the record row to `complete` or a rejection reason, and only then continues to Talia assembly.
