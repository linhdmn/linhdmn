# Linh Doan

**Senior Software Engineer** · SRE & DevOps experience
Building dependable AI-agent infrastructure — from data access and routing to
human-in-the-loop delivery.

[![GitHub followers](https://img.shields.io/github/followers/linhdmn?style=flat-square&logo=github&label=followers&color=181717)](https://github.com/linhdmn)
[![FreePeak organization](https://img.shields.io/badge/FreePeak-181717?style=flat-square&logo=github)](https://github.com/FreePeak)
[![LinkedIn profile](https://img.shields.io/badge/LinkedIn-harveydoan-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/harveydoan)
[![DEV Community](https://img.shields.io/badge/DEV%20Community-0A0A0A?style=flat-square&logo=devdotto&logoColor=white)](https://dev.to/thefreepeak)
[![Email](https://img.shields.io/badge/Email-Linh%20Doan-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:mnhatlinh.doan@gmail.com)

Ho Chi Minh City, Vietnam · Software engineer since 2018

---

## About

I build systems at the boundary where AI agents meet production systems. My work
spans structured data access, LLM gateways and context economics, developer
tooling, and delivery systems that keep humans in control.

I value dependable interfaces, explicit trade-offs, and evidence over hype —
whether the result is guardrailed database access, a bounded agent loop, or a
tested pull request.

## Areas of practice

- **Agent infrastructure** — MCP servers, tool execution, context engineering,
  and durable sessions.
- **Reliable and economical AI** — routing, fallbacks, budgets, observability,
  and useful cost controls.
- **Software delivery** — automation that produces reviewable, testable changes
  without hiding the failure modes.

## Open source

I maintain the [@FreePeak](https://github.com/FreePeak) organization — Go, Rust,
TypeScript, and JavaScript projects for AI-agent infrastructure. The projects
below are ordered by stars, most-adopted first. Star counts are the 2026-10-11
snapshot; the ordering can drift as the numbers move.

### FreePeak projects

| Project | What it does | Language | ★ |
|---|---|---|---|
| [`db-mcp-server`](https://github.com/FreePeak/db-mcp-server) | Multi-database MCP server for structured access with configurable guardrails, result limits, masking, timeouts, and audit logging | Go | **451** |
| [`LeanKG`](https://github.com/FreePeak/LeanKG) | Go code knowledge graph for lean agent context — stop burning tokens, start coding lean | Go | **220** |
| [`cortex`](https://github.com/FreePeak/cortex) | Declarative Go platform for MCP servers: tools, resources, and prompts in a clean, structured way | Go | **27** |
| [`ktme`](https://github.com/FreePeak/ktme) | Rust CLI that automates documentation from code changes over the Model Context Protocol | Rust | **15** |
| [`commitgen`](https://github.com/FreePeak/commitgen) | CLI that writes the commit message from staged changes | Go | **8** |
| [`kai`](https://github.com/FreePeak/kai) | Rust TUI for agentic coding with multi-provider compatibility, prompt optimization, and cost-aware routing | Rust | **8** |
| [`cursor-usage`](https://github.com/FreePeak/cursor-usage) | Cursor API request usage in the VS Code status bar: usage, extra charges, per-model breakdown | JavaScript | **6** |
| [`xdev`](https://github.com/FreePeak/xdev) | Lightweight Go coding agent in one static binary: streaming providers, session trees, terminal UI | Go | **5** |
| [`dsh-feature-loop`](https://github.com/FreePeak/dsh-feature-loop) | Bounded agent loop for DeepSeek Harness: budget ceilings, cheap-first routing, loop hygiene detectors, ops dashboard | TypeScript | **4** |
| [`dsh-mux`](https://github.com/FreePeak/dsh-mux) | DeepSeek Harness plugin: talk to coding CLIs from the DSH web GUI, sessions resumed | TypeScript | **4** |
| [`devagent`](https://github.com/FreePeak/devagent) | Autonomous backend delivery: ticket in, tested pull request out, with multi-worker fan-out and evidence gates | Go | **4** |
| [`onegw`](https://github.com/FreePeak/onegw) | Single-binary Go LLM gateway: any-to-any provider translation, fallback combos, token saver, usage tracking, ~100 MB RSS | Go | **4** |
| [`mermaid-mcp-server`](https://github.com/FreePeak/mermaid-mcp-server) | Lightweight MCP server for real-time Mermaid diagram syntax validation, minimal memory footprint | JavaScript | **3** |
| [`token-lens`](https://github.com/FreePeak/token-lens) | Local-only dashboard for AI coding sessions: turns, tokens, and cost across Cursor, Claude Code, and OpenCode — all data stays on your machine | TypeScript | **2** |

### Upstream contributions

Merged pull requests into projects I use and study. Each entry links the
repository, its upstream star count, and the merged pull requests; no
sole-authorship is implied. Upstream star counts are a 2026-10-11 snapshot,
since they move on someone else's repository.

#### [`diegosouzapw/OmniRoute`](https://github.com/diegosouzapw/OmniRoute) — ★ 75,028

Six merged fixes across provider routing, SSE budgets, canonical tool names,
and setup:

- [#8439 — read `INITIAL_PASSWORD` during setup](https://github.com/diegosouzapw/OmniRoute/pull/8439)
- [#10980 — surface a bare upstream close as `response.failed`](https://github.com/diegosouzapw/OmniRoute/pull/10980)
- [#11085 — restore canonical tool names so Claude Code accepts tool calls](https://github.com/diegosouzapw/OmniRoute/pull/11085)
- [#11209 — append a synthetic user turn for GLM-family upstreams](https://github.com/diegosouzapw/OmniRoute/pull/11209)
- [#11214 — floor the muse-spark output budget to prevent empty-content 502s](https://github.com/diegosouzapw/OmniRoute/pull/11214)
- [#11274 — clamp `reasoning_effort` to each model's declared vocabulary](https://github.com/diegosouzapw/OmniRoute/pull/11274)

#### [`punkpeye/awesome-mcp-servers`](https://github.com/punkpeye/awesome-mcp-servers) — ★ 96,088

- [#355 — add a multi-database MCP server to the catalog](https://github.com/punkpeye/awesome-mcp-servers/pull/355)

#### [`pulumi/pulumi`](https://github.com/pulumi/pulumi) — ★ 25,780

- [#24775 — the Go SDK marshals analyzer config schemas](https://github.com/pulumi/pulumi/pull/24775)

#### [`pterm/pterm`](https://github.com/pterm/pterm) — ★ 5,553

- [#811 — wrap long lines before the area is redrawn](https://github.com/pterm/pterm/pull/811)

Browse the full [FreePeak organization](https://github.com/FreePeak) for more
infrastructure, including the DeepSeek Harness plugins and the browser arcade.

## Experience

- **Senior Software Engineer — Be Group** — current since September 2025.
- **Senior Software Engineer / SRE / DevOps — Startup BlueSG** — previous;
  infrastructure and backend development initiatives.
- **Senior Software Engineer — ZaloPay** — previous; payment processing and
  financial infrastructure.

## Technical toolkit

- **Languages:** Go · TypeScript · Rust · Python · Java · JavaScript
- **Agent & backend:** MCP · LLM routing · API design · databases ·
  event-driven systems
- **Infrastructure:** Docker · Kubernetes · AWS · GitHub Actions · Linux ·
  observability

## Engineering principles

I optimize for **clear boundaries, testable behavior, and pragmatic systems**.

- Domain-Driven Design (DDD)
- Test-Driven Development (TDD)
- Event-driven architecture
- SOLID principles
- KISS and YAGNI

## Get in touch

Interested in AI-agent infrastructure, reliable developer tooling, or
open-source collaboration?

[![LinkedIn](https://img.shields.io/badge/LinkedIn-harveydoan-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/harveydoan)
[![GitHub](https://img.shields.io/badge/GitHub-linhdmn-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/linhdmn)
[![Email](https://img.shields.io/badge/Email-mnhatlinh.doan%40gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:mnhatlinh.doan@gmail.com)

*Based in Ho Chi Minh City, Vietnam* 🇻🇳
