# Adapter: Dreamina (即梦) through browser control

Browser automation against jimeng.jianying.com. Use only when the creator selected this route and the harness proved it can open, snapshot, click, type, **and upload a file**. Site DOM changes without notice; snapshot before every click and treat selectors below as last-known, not guaranteed.

## Preconditions

- Browser tool (Playwright MCP or equivalent) with file-chooser support.
- The creator logs in manually; the agent never enters credentials.
- Orders ready as files; one image per order.

## Flow

1. Open the site, snapshot, confirm login. Enter **画布 (Canvas)** via the sidebar link, not by URL. Do not use the 生成 history page.
2. Pick image mode. Set model, ratio, and resolution per the order; **re-check the ratio before every generation**, the UI resets it after "重新编辑". Keep text enhancement off.
3. Type the prompt with real key presses, not a value setter; the editor ignores programmatic `fill`. Attach references through the site's reference control, one at a time.
4. Generate. Wait by polling on a timer, not on a DOM text disappearing; stuck progress indicators are common. If a job sits at 99% for a long time, cancel and retry once.
5. Retrieve the result by reading the result `<img>` URL from the DOM and downloading it. **Fetch one image per evaluate call**; batch base64 pulls can break the browser tool connection. Never navigate away from a tab that holds an un-downloaded result.
6. Save into the project path with a version suffix. Write the handoff record row. Then the next order.

## Known failure modes

- Content review rejects prompts with confrontation, violence, or weapon words and some realistic-face requests. Reword once; on a second rejection, record and route the shot to `order-only.md`.
- Daily quota exhaustion looks like a generic timeout. Two failures at the same step across orders means quota: stop, collect what exists, report.
- Reference dropdowns may list only a few recent items; describe other anchors in the prompt text.
- Strictly sequential. Do not start a generation while another runs.
