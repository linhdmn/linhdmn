# PRD — `linhdmn/linhdmn` (GitHub Profile and Video Series)

## 1. Purpose

This repository is the owner's GitHub **profile special repo**: the `README.md`
rendered on `https://github.com/linhdmn` is the public professional introduction
for recruiters, collaborators, and peers. The `videos/` directory extends the
same evidence-based narrative into seven shareable vertical clips. Success = a
visitor can understand the engineer's role, selected work, and contact path
quickly, in text or video, without unsupported claims.

## 2. Scope

### In scope

- `README.md` — section hierarchy, wording, project attribution, links, and
  factual claims.
- Professional positioning around the current Senior Software Engineer role and
  AI-agent / production-infrastructure work.
- Selected open-source work, with `dsh-mux` and `dsh-feature-loop` first and
  upstream `OmniRoute` last, plus dynamic project signals.
- Seven 45-second 1080×1920 videos covering the profile, `db-mcp-server`,
  `LeanKG`, `cortex`, `devagent`, `onegw`, and `xdev`, with English voiceover,
  burned-in timed captions, and a quiet synthesized music bed.
- A local regeneration script using Python's standard library, Chrome, FFmpeg,
  and macOS `say`; no external media service or new dependency.
- Factual correctness of project attribution, employment status, and metrics.

### Out of scope

- Profile stats cards, contribution graphs, and other volatile counters. The
  previous Tokscale embed was removed because it added noise and could become
  stale without improving the professional narrative.
- A time-sensitive "current focus" section.
- A new website, custom domain, or hosted video service.
- Automating the entire 108-repository FreePeak organization into individual
  videos; this series deliberately covers the profile's selected work only.

## 3. Structure (current)

- **Header:** name, current role, SRE/DevOps experience, positioning statement,
  location, and contact badges.
- **About and areas of practice:** concise positioning around agent
  infrastructure, reliable/economical AI, and software delivery.
- **Selected work:** `dsh-mux` and `dsh-feature-loop` as featured cards,
  followed by a mobile-friendly list of selected projects.
- **Video series:** a direct link to seven 45-second MP4 introductions under
  `videos/`, with a local regeneration command and public-source links.
- **Experience:** Be Group as current; BlueSG and ZaloPay explicitly previous.
- **Technical toolkit and engineering principles:** concise, evidence-oriented
  capabilities and working values.
- **Get in touch:** LinkedIn, GitHub, email, and a short collaboration
  invitation.

## 4. Research and verification basis

The 2026-09-24 revamp used public GitHub API/repository data and official
GitHub documentation rather than copying generic portfolio templates:

- GitHub Docs, **Managing your profile README**:
  <https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme>
  — confirms the profile-special-repository model and the need for a clear,
  public README.
- GitHub Docs, **About the repository README file**:
  <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes>
  — supports standard Markdown, headings, links, and descriptive image alt text.
- Public GitHub API/repository pages for `linhdmn/linhdmn`, `FreePeak/dsh-mux`,
  `FreePeak/dsh-feature-loop`, the selected FreePeak projects, and
  `diegosouzapw/OmniRoute`, checked on 2026-09-24.
- Project READMEs and PRDs in the local repositories for the two new plugins and
  the selected supporting projects; these are the source for functional claims,
  supported tools, architecture, and licenses.

The featured-plugin descriptions were checked against the remote default-branch
sources at these commits:

- `FreePeak/dsh-mux@4d717ce014b0248c89fb28cd2e61629a0414ec89` — current
  Claude-only enablement and the disabled status of the other adapters.
- `FreePeak/dsh-feature-loop@af24efca7318fdfc7f86e14662de6c8826776b11` —
  extension-point architecture, budgets, routing, detectors, and approval gate.

The supporting-project descriptions and all six project-video scripts were
checked against their public default-branch READMEs and repository metadata on
2026-09-24. The video claims are limited to documented functionality, including
database guardrails, LeanKG's published token/tool-call results, Cortex's MCP
surface, DevAgent's evidence gates, OneGW's API translation/fallback behavior,
and Xdev's binary/memory/tool design.

## 5. Key decisions

- **Professional positioning over a personal hobby board.** The header states
  the role and concrete domain first; the practice bullets make the value
  proposition scannable without claiming a new title or inventing a current
  focus.
- **Featured work before supporting work.** `dsh-mux` and
  `dsh-feature-loop` lead the written portfolio because they are the newest
  additions. The video series follows the six projects already selected for
  the public portfolio rather than every FreePeak repository.
- **Attribution honesty.** FreePeak projects remain organization work, while
  `diegosouzapw/OmniRoute` retains its full owner/repository link and
  `upstream · contributor` marker. No sole-authorship claim is made.
- **Dynamic badges over volatile numbers.** README CI, license, language,
  stars, and forks use dynamic badges; no point-in-time counter is hardcoded.
- **Evidence-oriented descriptions.** Functional language comes from project
  READMEs and public repository metadata. LeanKG's performance result is
  explicitly attributed to its published A/B evidence.
- **Accessible written and visual content.** Markdown remains semantic and
  mobile-tolerant. Videos use large high-contrast captions and a restrained
  audio mix, with final frames that leave the project link visible for reading.
- **Local, deterministic media generation.** The standard library, installed
  Chrome/FFmpeg, and macOS `say` are reused instead of adding a dependency or
  sending portfolio material to an external service. Generated intermediates
  are ignored; only the final MP4s are tracked.
- **No generic claim inflation.** The wording emphasizes systems thinking,
  reliability, evidence, and human control rather than unsupported labels or
  guaranteed productivity gains.

## 6. Task record

Per repo convention, durable tasks for this repo live as GitHub issues on
`linhdmn/linhdmn`; this document is the status summary only, and no
task-tracker file is kept in a GitHub repo.

---

*Last updated: 2026-09-24 (`README.md` revamped into an executive-style
portfolio; `dsh-mux` and `dsh-feature-loop` added as the first featured
projects; upstream `OmniRoute` moved to the bottom with honest attribution;
seven selected-work videos added with local regeneration, 45-second timing,
voiceover, burned captions, and public-source verification.)*
