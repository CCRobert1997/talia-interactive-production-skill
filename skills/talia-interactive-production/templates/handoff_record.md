# Handoff record: <PROJECT_SLUG>

One row per media artifact. Append, never rewrite history; a rejected artifact keeps its row and the replacement gets a new one.

| Artifact | Node / shot | Purpose | References (ordered) | Provider / model / settings | Prompt file | Output path | Remote job / URL | Cost | QA | Applied to Talia |
|---|---|---|---|---|---|---|---|---|---|---|
| N01_B1.v1.png | N01 / B1 | Opening frame | CHAR_A_sheet.png, ENV_lobby.png | codex image_gen / <model> / 9:16 | orders/N01_B1.md | images/N01_B1.v1.png | — | ~30k tokens | rejected: proportion drift | no |
| N01_B1.v2.png | N01 / B1 | Opening frame | same | same | orders/N01_B1.md | images/N01_B1.v2.png | — | ~28k tokens | complete | node <uuid> image |
| N02_B1 | N02 / B1 | Ending A | CHAR_A_sheet.png | none | orders/N02_B1.md | — | — | — | prepared | no |

Status vocabulary: `complete` (passed its gate), `prepared` (order ready, not generated), `unverified` (exists, could not be checked here), or `rejected: <reason>`.

Talia column: the node id (and old URL when replacing) once `talia node set <nodeId> image|video <url>` ran and `talia validate` passed; otherwise `no`.
