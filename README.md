# Linh Doan

Software engineer in Ho Chi Minh City, working at Be Group. I build backend
systems and developer tooling, and lately infrastructure for AI coding agents:
MCP servers, an LLM gateway, and context tooling. Most of what is below is small
open-source work I made because I needed it.

[LinkedIn](https://www.linkedin.com/in/harveydoan) ·
[DEV Community](https://dev.to/thefreepeak) ·
[Email](mailto:mnhatlinh.doan@gmail.com)

[![Tokscale Stats](https://tokscale.ai/api/embed/linhdmn/svg?tokens=compact&cost=compact)](https://tokscale.ai/u/linhdmn)

## Open source

I maintain the [FreePeak](https://github.com/FreePeak) organization. Most
projects are small; `db-mcp-server` and `LeanKG` are the most starred. Star
counts are refreshed daily by a GitHub Actions workflow.

<!-- STARS:START -->
| Project | What it does | Language | ★ |
|---|---|---|---|
| [`db-mcp-server`](https://github.com/FreePeak/db-mcp-server) | Multi-database MCP server (MySQL, PostgreSQL, SQLite, Oracle, TimescaleDB) with row limits, PII masking, query timeouts, and optional audit logs | Go | **487** |
| [`LeanKG`](https://github.com/FreePeak/LeanKG) | Self-hosted code knowledge graph that gives coding agents targeted context | Go | **222** |
| [`cortex`](https://github.com/FreePeak/cortex) | Declarative Go platform for building MCP servers: tools, resources, and prompts | Go | **27** |
| [`ktme`](https://github.com/FreePeak/ktme) | Rust CLI that generates documentation from code changes over MCP | Rust | **15** |
| [`kai`](https://github.com/FreePeak/kai) | Rust TUI for agentic coding with multiple providers and cost-aware routing | Rust | **9** |
| [`commitgen`](https://github.com/FreePeak/commitgen) | CLI that writes a commit message from staged changes | Go | **8** |
| [`cursor-usage`](https://github.com/FreePeak/cursor-usage) | VS Code and Cursor status bar extension showing request usage, extra charges, and a per-model breakdown | JavaScript | **6** |
| [`xdev`](https://github.com/FreePeak/xdev) | Lightweight Go coding agent in one static binary | Go | **5** |
| [`onegw`](https://github.com/FreePeak/onegw) | Single static Go LLM gateway with cross-API translation, fallback combos, token saver, and usage tracking | Go | **5** |
| [`dsh-feature-loop`](https://github.com/FreePeak/dsh-feature-loop) | Bounded agent loop for DeepSeek Harness with budget ceilings and cheap-first routing | TypeScript | **4** |
| [`dsh-mux`](https://github.com/FreePeak/dsh-mux) | DeepSeek Harness plugin to drive coding CLIs from the web GUI | TypeScript | **4** |
| [`devagent`](https://github.com/FreePeak/devagent) | Backend agent: ticket in, tested pull request out, with parallel workers and evidence gates | Go | **4** |
| [`mermaid-mcp-server`](https://github.com/FreePeak/mermaid-mcp-server) | MCP server that validates Mermaid diagram syntax | JavaScript | **3** |
| [`token-lens`](https://github.com/FreePeak/token-lens) | Local-only dashboard for AI coding sessions: turns, tokens, and cost | TypeScript | **2** |
<!-- STARS:END -->

### Contributions to other projects

Merged pull requests into projects I use. These are small changes to
repositories other people maintain; the star counts are theirs.

#### [`diegosouzapw/OmniRoute`](https://github.com/diegosouzapw/OmniRoute) — ★ 90,445

- [#8439 — read `INITIAL_PASSWORD` during setup](https://github.com/diegosouzapw/OmniRoute/pull/8439)
- [#10980 — surface a bare upstream close as `response.failed`](https://github.com/diegosouzapw/OmniRoute/pull/10980)
- [#11085 — restore canonical tool names so Claude Code accepts tool calls](https://github.com/diegosouzapw/OmniRoute/pull/11085)
- [#11209 — append a synthetic user turn for GLM-family upstreams](https://github.com/diegosouzapw/OmniRoute/pull/11209)
- [#11214 — floor the muse-spark output budget to prevent empty-content 502s](https://github.com/diegosouzapw/OmniRoute/pull/11214)
- [#11274 — clamp `reasoning_effort` to each model's declared vocabulary](https://github.com/diegosouzapw/OmniRoute/pull/11274)

#### [`punkpeye/awesome-mcp-servers`](https://github.com/punkpeye/awesome-mcp-servers) — ★ 98,524

- [#355 — add a multi-database MCP server to the catalog](https://github.com/punkpeye/awesome-mcp-servers/pull/355)

#### [`pulumi/pulumi`](https://github.com/pulumi/pulumi) — ★ 25,943

- [#24775 — the Go SDK marshals analyzer config schemas](https://github.com/pulumi/pulumi/pull/24775)

#### [`pterm/pterm`](https://github.com/pterm/pterm) — ★ 5,572

- [#811 — wrap long lines before the area is redrawn](https://github.com/pterm/pterm/pull/811)

## Experience

- **Be Group** — Senior Software Engineer, since September 2025
- **BlueSG** — Senior Software Engineer / SRE / DevOps; infrastructure and backend work
- **ZaloPay** — Senior Software Engineer; payment processing

Software engineer since 2018. Day to day: Go, TypeScript, Rust, Python; Docker,
Kubernetes, AWS, GitHub Actions.
