# Capability routing

The model affects reasoning, storytelling, visual comprehension, and tool-use quality. The harness determines access to local files, images, video, audio, shell, browser, authenticated sessions, and generators. Never infer a capability from the model brand.

| Capability | Evidence | Fallback when absent |
|---|---|---|
| Files | Create and reread a disposable text file | Text handoff only |
| Shell | Run a harmless version command | Skip deterministic scripts |
| Image vision | Inspect a real image and report testable details | Visual QA is `unverified` |
| Image generation | Generate one disposable image with the configured tool | Prepare an image order |
| Video review | Direct video input, or extracted frames plus vision | Motion QA is `unverified` |
| Audio review | Playback/transcription plus stream inspection | Verify streams only |
| Browser | Open, inspect, click, type, and upload a disposable file | Prepare UI instructions |
| Talia CLI | `whoami`, project listing, and validation | Prepare a mutation manifest |
| Persistent auth | Repeat a read-only request in a new process | Creator performs authenticated work |

`scripts/capability_probe.py` detects local executables. It cannot prove vision, browser uploads, account permission, or paid-service access; test those explicitly.

## Routes

- **Images:** built-in generator → configured API → creator-selected authenticated browser → self-contained image order.
- **Video:** use the creator-selected provider. Talia paid generation is always manual. A completed remote job still requires download and G3 QA.
- **Video QA:** direct video understanding is best; otherwise extract contact sheets and targeted frames and inspect audio separately. Without vision, verify technical facts only.
- **Browser:** test file upload independently from click and type. A harness that cannot handle the upload path is not a complete production route.
