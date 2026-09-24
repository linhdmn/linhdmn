# FreePeak Open Source — 60-Second Video Series

This directory contains seven vertical, one-minute English videos introducing
Linh Doan's featured open-source work through the FreePeak organization.

| Video | Project | Core message |
| --- | --- | --- |
| `01-linh-doan.mp4` | Profile | Senior software engineer building open infrastructure where AI agents meet production. |
| `02-db-mcp-server.mp4` | db-mcp-server | Guardrailed, multi-database MCP access for AI agents. |
| `03-leankg.mp4` | LeanKG | A measured code knowledge graph that spends fewer tokens and tool calls. |
| `04-cortex.mp4` | cortex | A declarative Go platform for MCP servers. |
| `05-devagent.mp4` | devagent | Ticket in, evidence-gated tested pull request out. |
| `06-onegw.mp4` | onegw | One lightweight gateway, three LLM API formats, fallbacks, and usage control. |
| `07-xdev.mp4` | xdev | A small static Go coding agent with a bounded memory budget. |

Format: 1080×1920, 30 fps, H.264/AAC MP4, under 60 seconds, burned-in captions,
local macOS English voiceover, and no external assets or credentials. Videos use
public project names and documented claims only.

## Re-render

```bash
python3 scripts/render_videos.py
```

The renderer uses the existing Python standard library, Chrome, FFmpeg, and the
macOS `say` command already present on this machine. It creates intermediate
HTML/audio/PNG files under `build/`; only final MP4 files are tracked.

## Source verification

- `https://github.com/linhdmn`
- `https://github.com/FreePeak/db-mcp-server`
- `https://github.com/FreePeak/LeanKG`
- `https://github.com/FreePeak/cortex`
- `https://github.com/FreePeak/devagent`
- `https://github.com/FreePeak/onegw`
- `https://github.com/FreePeak/xdev`

---
*Last updated: 2026-09-24 (added approved seven-video 1080×1920 series, renderer, captions, and public-source verification.)*
