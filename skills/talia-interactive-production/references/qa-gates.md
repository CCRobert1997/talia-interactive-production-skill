# QA gates

## Image gate

Reject and regenerate for a wrong identity, age, anatomy, material, silhouette, costume, or defining mark; drift from the approved sheet; missing/duplicated/fused parts; impossible contact, gaze, scale, or space; wrong story state; forbidden characters, props, transformations, text, watermark, border, or UI; or unusable interaction targets.

Minor background variation may pass only when it does not affect story, continuity, identity, interaction, or later production.

## Video gate

Inspect the first frame, last frame, every action transition and speaker change, and intervals prone to occlusion, waterline/refraction, contact, transformation, or fast motion. Check identity, action causality and direction, unwanted cuts/freezes/reverse motion/clones/text/UI, exact dialogue, language, speaker order, lip movement, ambience, BGM policy, and audio-stream presence.

Use a contact sheet for scanning and full-resolution targeted frames for suspected failures. Contact sheets cannot validate rapid deformation or exact dialogue.

## Node-master gate

Verify expected dimensions/orientation, codecs, playable duration, required audio stream, normalized sample rate/channels, absence of accidental truncation or black tail, and correct filename/node mapping.

## Talia draft gate

Verify start node, existing choice targets, reachable endings, exits from reachable non-ending nodes, media URLs, auto-advance rules, non-overlapping tap regions matching visible targets, title/cover/language/presentation, and CLI validation.

A successful mutation is not proof of a correct experience. Preview every route before manual publishing.
