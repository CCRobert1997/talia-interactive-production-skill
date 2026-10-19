# Image generation adapters

`capability-routing.md` decides *whether* images can be generated in this harness. An adapter says *how* for one concrete route. Read exactly one adapter: the first in this order whose preconditions the probe confirmed.

| Order | Adapter | Precondition |
|---|---|---|
| 1 | [codex-image-gen.md](codex-image-gen.md) | `codex` executable with a ChatGPT login; built-in `image_gen` tool |
| 2 | [openai-images-api.md](openai-images-api.md) | `OPENAI_API_KEY` in the environment and network access |
| 3 | [dreamina-browser.md](dreamina-browser.md) | Browser control with file upload, a logged-in Dreamina (即梦) account, and the creator chose this route |
| 4 | [order-only.md](order-only.md) | None of the above |

## Shared contract

Every adapter takes an **image order** (see `templates/image_order.md`) and must end with:

1. the accepted image saved **inside the project** at the path the order names, never only in a tool cache;
2. a new version rather than an overwrite when a file already exists;
3. one row in the handoff record (`templates/handoff_record.md`): final prompt, references in order, provider/model/settings, output path, cost when known, QA status;
4. the deliverable status `complete` only after G2 visual QA by the agent itself. A generator's own "looks correct" report is not QA.

Adapters never change the story graph, never touch Talia, and never generate video. Those are separate steps with their own gates.

## Adding an adapter

One file, under 80 lines: preconditions, invocation, how references are passed, where the output lands, known failure modes. Do not restate the workflow; link to it. Do not weaken the Talia safety boundary.
