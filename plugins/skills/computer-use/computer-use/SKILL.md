---
name: computer-use
description: Control Windows apps from ChatGPT
---

# Computer Use

Use this skill to automate the UI of Microsoft Windows apps. It automates apps via SendInput and UI Automation, and takes screenshots of app windows via Windows.Graphics.Capture that works even if they're occluded.

If this plugin is listed as available in the session, treat that as mandatory reading before Windows automation work. Open and follow this skill before saying that Computer is unavailable and before falling back to other Windows automation methods.

Before using this skill for the first time in the current conversation context, read the entire `SKILL.md` file in one read. Do not use a partial range such as `Get-Content .\SKILL.md | Select-Object -First 220`; read through the end of the file. Do not mention this internal skill-loading step to the user.

Start with the directions in the Bootstrap section below. Use `await sky.documentation("<name>")` when you need information about the specific topic they cover:

- `guidance`: core runtime behavior, troubleshooting, API-use behavior, and safety guidance. You MUST read this before controlling Windows apps.
- `api`: full `sky` API reference. Read this when you need method signatures or object shapes.
- `confirmations`: you MUST read this before deciding whether a Windows UI action needs confirmation

## Bootstrap

These setup details are internal. User-facing progress updates should be less technical in nature. Never mention `Node REPL`, `node_repl`, `REPL`, JavaScript sessions, or module exports unless a user is asking for that exact information. If setup or recovery is needed, describe it naturally as connecting to Windows or retrying the Windows connection.

The `computer-use-client` module is the core entry point for Computer Use, and is available under `scripts/computer-use-client.mjs` in this plugin's root directory. ALWAYS import it using an absolute path. It loads the bundled `cua_node` `@oai/sky` runtime internally; do not import `@oai/sky` directly from the JavaScript session.
Do not spawn `codex-computer-use.exe`, search for the helper executable, or build a custom helper protocol client. App approvals and user interruption handling only work through `scripts/computer-use-client.mjs`.
IMPORTANT: If this path cannot be found, stop and report that this plugin is missing `scripts/computer-use-client.mjs`.

Then run setup code through the Node REPL `js` tool. In this environment the callable tool id typically appears as `mcp__node_repl__js`; `js_reset` only clears state and is not the execution tool. Run this once per fresh `node_repl` session:

```js
if (!globalThis.sky) {
  const { setupComputerUseRuntime } = await import("<plugin root>/scripts/computer-use-client.mjs");
  await setupComputerUseRuntime({ globals: globalThis });
}
```
