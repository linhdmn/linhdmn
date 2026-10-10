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
below are ordered by stars, most-adopted first; star counts are live
shields.io badges, not snapshots.

### Featured

**[`dsh-mux`](https://github.com/FreePeak/dsh-mux)** — Keep coding-CLI
conversations inside the DeepSeek Harness GUI. A Mux panel, slash commands, a
host tool, and a remote service for resumable conversations. Each turn runs one
process and resumes by the CLI's session id, with no live bidirectional PTY
required.

**[`dsh-feature-loop`](https://github.com/FreePeak/dsh-feature-loop)** — A
policy layer for bounded, reviewable agent runs. Uses the DeepSeek Harness
extension points for step ceilings, cheap-first routing, deterministic stall
detection, and pre-dispatch human approval; the standalone runner exercises the
same policies under explicit cost and step budgets.

**[`xdev`](https://github.com/FreePeak/xdev)** — A lightweight coding agent in
one static Go binary, with streaming providers, session trees, tools, and a
terminal UI.

### FreePeak projects

| Project | What it does | Language | Stars |
|---|---|---|---|
| [`db-mcp-server`](https://github.com/FreePeak/db-mcp-server) | Multi-database MCP server for structured access with configurable guardrails, result limits, masking, timeouts, and audit logging | Go | ![stars](https://img.shields.io/github/stars/FreePeak/db-mcp-server?style=flat-square) |
| [`LeanKG`](https://github.com/FreePeak/LeanKG) | Go code knowledge graph for lean agent context — stop burning tokens, start coding lean | Go | ![stars](https://img.shields.io/github/stars/FreePeak/LeanKG?style=flat-square) |
| [`cortex`](https://github.com/FreePeak/cortex) | Declarative Go platform for MCP servers: tools, resources, and prompts in a clean, structured way | Go | ![stars](https://img.shields.io/github/stars/FreePeak/cortex?style=flat-square) |
| [`ktme`](https://github.com/FreePeak/ktme) | Rust CLI that automates documentation from code changes over the Model Context Protocol | Rust | ![stars](https://img.shields.io/github/stars/FreePeak/ktme?style=flat-square) |
| [`commitgen`](https://github.com/FreePeak/commitgen) | CLI that writes the commit message from staged changes | Go | ![stars](https://img.shields.io/github/stars/FreePeak/commitgen?style=flat-square) |
| [`kai`](https://github.com/FreePeak/kai) | Rust TUI for agentic coding with multi-provider compatibility, prompt optimization, and cost-aware routing | Rust | ![stars](https://img.shields.io/github/stars/FreePeak/kai?style=flat-square) |
| [`cursor-usage`](https://github.com/FreePeak/cursor-usage) | Cursor API request usage in the VS Code status bar: usage, extra charges, per-model breakdown | JavaScript | ![stars](https://img.shields.io/github/stars/FreePeak/cursor-usage?style=flat-square) |
| [`xdev`](https://github.com/FreePeak/xdev) | Lightweight Go coding agent in one static binary: streaming providers, session trees, terminal UI | Go | ![stars](https://img.shields.io/github/stars/FreePeak/xdev?style=flat-square) |
| [`dsh-feature-loop`](https://github.com/FreePeak/dsh-feature-loop) | Bounded agent loop for DeepSeek Harness: budget ceilings, cheap-first routing, loop hygiene detectors, ops dashboard | TypeScript | ![stars](https://img.shields.io/github/stars/FreePeak/dsh-feature-loop?style=flat-square) |
| [`dsh-mux`](https://github.com/FreePeak/dsh-mux) | DeepSeek Harness plugin: talk to coding CLIs from the DSH web GUI, sessions resumed | TypeScript | ![stars](https://img.shields.io/github/stars/FreePeak/dsh-mux?style=flat-square) |
| [`devagent`](https://github.com/FreePeak/devagent) | Autonomous backend delivery: ticket in, tested pull request out, with multi-worker fan-out and evidence gates | Go | ![stars](https://img.shields.io/github/stars/FreePeak/devagent?style=flat-square) |
| [`onegw`](https://github.com/FreePeak/onegw) | Single-binary Go LLM gateway: any-to-any provider translation, fallback combos, token saver, usage tracking, ~100 MB RSS | Go | ![stars](https://img.shields.io/github/stars/FreePeak/onegw?style=flat-square) |
| [`mermaid-mcp-server`](https://github.com/FreePeak/mermaid-mcp-server) | Lightweight MCP server for real-time Mermaid diagram syntax validation, minimal memory footprint | JavaScript | ![stars](https://img.shields.io/github/stars/FreePeak/mermaid-mcp-server?style=flat-square) |
| [`token-lens`](https://github.com/FreePeak/token-lens) | Local-only dashboard for AI coding sessions: turns, tokens, and cost across Cursor, Claude Code, and OpenCode — all data stays on your machine | TypeScript | ![stars](https://img.shields.io/github/stars/FreePeak/token-lens?style=flat-square) |

### Upstream contributions

Merged pull requests to projects I use and study, upstream — each keeps its
owner link and no sole-authorship is implied:

- **[`pterm/pterm`](https://github.com/pterm/pterm)** — *merged* — long lines
  now wrap before the area is redrawn.
- **[`pulumi/pulumi`](https://github.com/pulumi/pulumi)** — *merged* — the Go
  SDK marshals analyzer config schemas correctly.
- **[`charmbracelet/bubbles`](https://github.com/charmbracelet/bubbles)** —
  *merged* — delete the word under the cursor in `textinput`.
- **[`diegosouzapw/OmniRoute`](https://github.com/diegosouzapw/OmniRoute)** —
  *merged* — six fixes across provider routing, SSE output budgets, canonical
  tool names, and setup configuration.
- **[`punkpeye/awesome-mcp-servers`](https://github.com/punkpeye/awesome-mcp-servers)**
  — *merged* — added a multi-database MCP server to the catalog.

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
