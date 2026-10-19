# Adapter: OpenAI Images API

Direct HTTP calls, no agent in the middle. Use when the harness has network access and `OPENAI_API_KEY`.

## Preconditions

- `OPENAI_API_KEY` set in the environment (never written into project files or logs).
- `curl` or Python with `urllib`. No SDK required.
- Check the current image model name, size options, and price in OpenAI's docs at use time; they change. Record what you used.

## Invocation

Text-only order:

```bash
curl -s https://api.openai.com/v1/images/generations \
  -H "Authorization: Bearer $OPENAI_API_KEY" -H "Content-Type: application/json" \
  -d "$(jq -n --arg p "$(cat prompt.txt)" --arg m "$IMAGE_MODEL" \
        '{model:$m, prompt:$p, size:"1024x1536", n:1}')" \
  | jq -r '.data[0].b64_json' | base64 -d > out/N01_B1.v1.png
```

With reference images (identity sheet, environment anchor, previous frame), use the edits endpoint and send each reference as a file part. Name their roles in the prompt in the same order you attach them ("Image 1 is the identity anchor, Image 2 the environment…").

```bash
curl -s https://api.openai.com/v1/images/edits \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F model="$IMAGE_MODEL" -F "prompt=<prompt.txt" -F size=1024x1536 \
  -F "image[]=@anchors/CHAR_A_sheet.png" -F "image[]=@anchors/ENV_lobby.png" \
  | jq -r '.data[0].b64_json' | base64 -d > out/N01_B1.v1.png
```

## Rules

- Decode and save straight into the project path from the order; add a version suffix, never overwrite.
- Store the exact prompt and the reference order in the handoff record; the API keeps nothing.
- Content-policy rejections come back as HTTP 400 with a message. Reword once; if it fails again, record and route the shot to `order-only.md` for the creator.
- Sizes are fixed presets. If the project ratio is not offered, generate the nearest and crop locally; note the crop in the record.
