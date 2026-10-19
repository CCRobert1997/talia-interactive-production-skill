# Adapter: OpenAI Codex built-in `image_gen`

Run Codex non-interactively as an image worker. The agent writes the order; Codex only calls `image_gen` and saves the file. Verified route: one command in, one PNG on disk, no browser.

## Preconditions

- `codex` on `PATH` (`npm i -g @openai/codex`) **or** the copy bundled with the ChatGPT desktop app (macOS: `/Applications/ChatGPT.app/Contents/Resources/codex`, not on `PATH`).
- Logged in with a ChatGPT account (`codex login`; auth mode `chatgpt`). No `OPENAI_API_KEY` needed.
- `codex doctor` passes.

## Invocation

```bash
codex exec --skip-git-repo-check \
  -m "$CODEX_IMAGE_MODEL" \
  -c model_reasoning_effort=low \
  "$(cat order.md)" < /dev/null
```

- `< /dev/null` is required; otherwise Codex waits on stdin and hangs.
- Pass `-m` explicitly on every call. The model in `~/.codex/config.toml` may be an expensive reasoning model; the image work is done by `image_gen`, not by reasoning, so pick the cheapest model that writes a faithful prompt and keep effort `low`. Record the model you used.
- One order per call. Batch by looping, not by one giant order.

## The order must contain five blocks

1. **Scope line**: "Your only task is to generate 1 image and save it into the project. Do not edit scripts or docs, do not touch Talia, do not generate video, do not read unrelated files." Without it Codex explores and edits the repo.
2. **Absolute working directory.**
3. **Reference list** with roles, e.g. `identity anchor` / `environment anchor` / `previous-shot continuity`. Each local reference must be opened with `view_image` first; a bare path is not seen.
4. **Full image prompt**: aspect ratio, composition, character state, light, negative constraints.
5. **Save instruction**: target path, create the directory if missing, **never overwrite**, then report the path and a per-criterion self-check.

`image_gen` has **no output-path parameter**. Output lands in `$CODEX_HOME/generated_images/<session>/`. The order must tell Codex to `cp` it to the project path, or the image stays in the cache.

## Known behaviour

- Portrait 9:16 at roughly 941×1672 is obtainable; request the size explicitly.
- Cost per image with two or three references is tens of thousands of tokens.
- Codex's self-check is not reliable: it reports identity and proportion criteria as passed when they drifted. The agent must inspect the saved file itself (G2).
- Codex may lack `rg` in its shell and fall back to `find`; harmless.
- On quota exhaustion the call fails late or returns no file. Two consecutive failures at the same step mean stop, record, and switch adapter.
