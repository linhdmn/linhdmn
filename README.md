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

## Selected work

I contribute to selected open-source infrastructure through the
[@FreePeak](https://github.com/FreePeak) organization and to selected upstream
projects. The first two projects below are my newest DSH plugins.

### [`dsh-mux`](https://github.com/FreePeak/dsh-mux)

**Keep coding-CLI conversations inside the DeepSeek Harness GUI.** `dsh-mux`
adds a Mux panel, slash commands, a host tool, and a remote service for
resumable conversations. Claude Code is enabled today; the plugin also discovers
OMP, Pi, Cursor, Agy, and Command Code adapters, which remain disabled until
each has a tested answer parser, while opencode is reported missing until its
binary is available. Each turn runs one process and resumes by the CLI’s
session id, without requiring a live bidirectional PTY.

[![CI](https://img.shields.io/github/actions/workflow/status/FreePeak/dsh-mux/ci.yml?branch=main&style=flat-square&label=CI)](https://github.com/FreePeak/dsh-mux/actions/workflows/ci.yml)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![MIT license](https://img.shields.io/badge/license-MIT-green?style=flat-square)
![dsh-mux stars](https://img.shields.io/github/stars/FreePeak/dsh-mux?style=flat-square&label=stars)
![dsh-mux forks](https://img.shields.io/github/forks/FreePeak/dsh-mux?style=flat-square&label=forks)

### [`dsh-feature-loop`](https://github.com/FreePeak/dsh-feature-loop)

**A policy layer for bounded, reviewable agent runs.** `dsh-feature-loop` uses
the DeepSeek Harness extension points for step ceilings, cheap-first routing,
deterministic stall detection, and pre-dispatch human approval. Its standalone
runner exercises the same policies with explicit cost and step budgets. The
plugin is hosted on the harness rather than maintaining a vendored fork, keeping
the control plane explicit and the failure path fail-closed.

[![CI](https://img.shields.io/github/actions/workflow/status/FreePeak/dsh-feature-loop/ci.yml?branch=main&style=flat-square&label=CI)](https://github.com/FreePeak/dsh-feature-loop/actions/workflows/ci.yml)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![MIT license](https://img.shields.io/badge/license-MIT-green?style=flat-square)
![dsh-feature-loop stars](https://img.shields.io/github/stars/FreePeak/dsh-feature-loop?style=flat-square&label=stars)
![dsh-feature-loop forks](https://img.shields.io/github/forks/FreePeak/dsh-feature-loop?style=flat-square&label=forks)

### More open source

Browse the full [FreePeak organization](https://github.com/FreePeak) for more
open-source infrastructure.

- **[`db-mcp-server`](https://github.com/FreePeak/db-mcp-server)** — A
  multi-database MCP server for structured access with configurable guardrails,
  result limits, masking, timeouts, and audit logging.
- **[`LeanKG`](https://github.com/FreePeak/LeanKG)** — A Go code knowledge graph
  for lean agent context, with measured token and tool-call economics.
- **[`cortex`](https://github.com/FreePeak/cortex)** — A declarative Go framework
  for building MCP servers, tools, resources, and prompts.
- **[`devagent`](https://github.com/FreePeak/devagent)** — Autonomous backend
  delivery: ticket in, tested pull request out, with multi-worker fan-out and
  evidence gates.
- **[`onegw`](https://github.com/FreePeak/onegw)** — A single-binary Go LLM
  gateway with provider translation, fallback combos, token optimization, and
  usage telemetry.
- **[`xdev`](https://github.com/FreePeak/xdev)** — A lightweight Go coding agent
  in one static binary, with streaming providers, session trees, tools, and a
  terminal UI.
- **[`diegosouzapw/OmniRoute`](https://github.com/diegosouzapw/OmniRoute)**
  *(upstream · contributor)* — An MIT AI gateway that brings many providers and
  free tiers behind one endpoint for coding clients.

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
