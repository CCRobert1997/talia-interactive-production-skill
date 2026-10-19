# Image order: <IMG_ID>

Scope: generate exactly 1 image and save it into the project. Do not edit story files, do not touch Talia, do not generate video.

## Target
- Project root (absolute): `/abs/path/to/project`
- Save to: `/abs/path/to/project/images/<IMG_ID>.v1.png` (create the directory if missing; never overwrite; bump `.v2` if `.v1` exists)
- Node / beat: `<NODE_ID>` / `<IMG_ID>`
- Size and ratio: `<e.g. 1024x1536, 9:16>`

## Story purpose
<One or two sentences: what the player must understand or feel from this frame, and what it sets up.>

## References (open each before generating; keep this order)
1. `<abs path>` — identity anchor: <character name>. Must match face, age/proportion, hair, costume, markings.
2. `<abs path>` — environment anchor: <place>. Must match layout, landmarks, light direction.
3. `<abs path>` — continuity: previous frame. Use for pose and camera only, not identity.

## Identity invariants
<Bullet list of things that must survive: anatomy, face, silhouette, costume colour, props the character holds, forbidden traits.>

## Prompt
<Full prompt: style base, composition, subject state and action, camera and lens, light, environment details, props and spatial relations.>

## Forbidden
<Text in image, watermark, UI, extra people, extra limbs, modern objects in a period scene, anything the story state rules out.>

## Interaction layout (if the beat carries tap regions or a choice overlay)
<Which screen areas must stay clear or must contain the tappable object; bottom safe area if captions or buttons are burned in later.>

## Acceptance checks (G2)
- [ ] Identity matches anchor 1 on face, proportion, costume
- [ ] Environment matches anchor 2 on layout and light direction
- [ ] Story state correct: <specific check>
- [ ] No text, watermark, or UI
- [ ] Ratio and size as ordered
- [ ] Interaction targets visible and separated (if any)
