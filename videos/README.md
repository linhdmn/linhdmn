# FreePeak Open Source — 45-Second Video Series

This directory contains seven vertical, 45-second English videos introducing
Linh Doan's profile and six featured open-source projects through FreePeak.

| Video | Project | Core message |
| --- | --- | --- |
| `01-linh-doan.mp4` | Profile | Senior software engineer building open infrastructure where AI agents meet production. |
| `02-db-mcp-server.mp4` | db-mcp-server | Guardrailed, multi-database MCP access for AI agents. |
| `03-leankg.mp4` | LeanKG | A measured code knowledge graph that spends fewer tokens and tool calls. |
| `04-cortex.mp4` | cortex | A declarative Go platform for MCP servers. |
| `05-devagent.mp4` | devagent | Ticket in, evidence-gated tested pull request out. |
| `06-onegw.mp4` | onegw | One lightweight gateway, three LLM API formats, fallbacks, and usage control. |
| `07-xdev.mp4` | xdev | A small static Go coding agent with a bounded memory budget. |

Format: 1080×1920, 30 fps, H.264/AAC MP4, 45 seconds, burned-in timed captions,
local macOS English voiceover, and a quiet synthesized music bed. Videos use
public project names and documented claims only; no external assets or secrets.

## Re-render

```bash
python3 scripts/render_videos.py
```

The renderer uses only Python's standard library plus Chrome, FFmpeg, and the
macOS `say` command already present on this machine. It writes intermediate
HTML, audio, PNG, and frame-list files under `build/`; only final MP4 files are
tracked.

## Source verification

- `https://github.com/linhdmn`
- `https://github.com/FreePeak/db-mcp-server`
- `https://github.com/FreePeak/LeanKG`
- `https://github.com/FreePeak/cortex`
- `https://github.com/FreePeak/devagent`
- `https://github.com/FreePeak/onegw`
- `https://github.com/FreePeak/xdev`

*Last updated: 2026-09-24 (added approved seven-video 1080×1920 series with 45-second timing, burned captions, voiceover, and a quiet music bed.)*
*Last updated: 2026-09-24 (added approved seven-video 1080×1920 series, renderer, captions, and public-source verification.)*
