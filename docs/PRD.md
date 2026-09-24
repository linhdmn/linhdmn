# PRD — `linhdmn/linhdmn` (GitHub Profile README)

## 1. Purpose

This repository is the owner's GitHub **profile special repo**: the single
`README.md` rendered on `https://github.com/linhdmn` is the public professional
introduction for recruiters, collaborators, and peers. There is no code, build,
or test suite. Success = a visitor can understand the engineer's role, areas of
expertise, selected work, experience, and contact path in about 30 seconds
without decoding a visual layout or trusting unsupported metrics.

## 2. Scope

### In scope

- `README.md` — the public deliverable: section hierarchy, wording, project
  attribution, links, and factual claims.
- Professional positioning around the current Senior Software Engineer role and
  AI-agent / production-infrastructure work.
- Selected open-source work, with `dsh-mux` and `dsh-feature-loop` first and
  upstream `OmniRoute` last, plus dynamic project signals.
- Factual correctness of project attribution, employment status, and metrics.

### Out of scope

- Profile stats cards, contribution graphs, and other volatile counters. The
  previous Tokscale embed was removed because it added noise and could become
  stale without improving the professional narrative.
- A time-sensitive "current focus" section.
- A new website, custom domain, or visual asset not already represented by the
  GitHub README.

## 3. Structure (current)

- **Header:** name, current role, SRE/DevOps experience, positioning statement,
  location, and contact badges.
- **About:** two concise paragraphs describing the AI-agent / production-systems
  boundary and engineering values.
- **Areas of practice:** agent infrastructure, reliable/economical AI, and
  software delivery.
- **Selected work:** `dsh-mux` and `dsh-feature-loop` as featured cards, followed
  by a mobile-friendly list of selected projects.
- **Experience:** Be Group as current; BlueSG and ZaloPay explicitly previous.
- **Technical toolkit:** languages, agent/backend capabilities, and
  infrastructure grouped by practical use.
- **Engineering principles:** DDD, TDD, event-driven architecture, SOLID, KISS,
  and YAGNI.
- **Get in touch:** LinkedIn, GitHub, email, and a short invitation focused on
  relevant collaboration.

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

The supporting-project descriptions were checked against their public default
branch sources on the same date. The resulting structure uses short paragraphs,
clear sections, plain-text project descriptions, and dynamic badges rather than
hardcoded star/fork counts. The new plugin cards lead because the owner
requested the latest work to lead; `OmniRoute` is last and remains explicitly
labelled **upstream · contributor**.

## 5. Key decisions

- **Professional positioning over a personal hobby board.** The header states
  the role and concrete domain first. The practice bullets make the value
  proposition scannable without claiming a new title or inventing a current
  focus.
- **Featured work before supporting work.** `dsh-mux` gets a short product
  description of the GUI-to-CLI thread workflow, including its current
  Claude-only enablement; `dsh-feature-loop` gets its bounded policy, budget,
  routing, detector, and human-gate model. They appear before the other selected
  projects because they are the requested newest additions.
- **Attribution honesty.** FreePeak projects are presented as selected
  organization work, while `diegosouzapw/OmniRoute` retains its full owner/repo
  link and `upstream · contributor` marker. No sole-authorship claim is made
  for OmniRoute. The two plugin repositories list `linhdmn` as their GitHub
  contributor at the time of verification.
- **Dynamic badges over volatile numbers.** CI, license, language, stars, and
  forks are rendered through `img.shields.io`; no point-in-time metric is
  hardcoded in the README. This keeps the page resilient to normal repository
  changes.
- **Evidence-oriented descriptions.** Functional language comes from each
  project's README/PRD and public repository metadata. Broad claims are kept
  durable ("agent infrastructure", "reliable systems") rather than presenting
  an unverified user, revenue, or adoption number.
- **Accessible, mobile-tolerant Markdown.** The page uses semantic headings,
  descriptive image `alt` text, descriptive link labels, short paragraphs, and
  compact lists rather than a wide project table. It avoids a visual hero image
  and relies on native GitHub rendering so the content remains readable without
  JavaScript or custom CSS.
- **Employment status remains explicit.** Be Group is listed as Senior
  Software Engineer and current since September 2025; BlueSG and ZaloPay remain
  previous roles. No responsibility blurb is invented for Be Group.
- **No generic claim inflation.** The wording emphasizes systems thinking,
  reliability, evidence, and human control rather than unsupported labels such
  as "10x engineer", "AI thought leader", or guaranteed productivity gains.

## 6. Task record

Per repo convention, durable tasks for this repo live as GitHub issues on
`linhdmn/linhdmn`; this document is the status summary only, and no
task-tracker file is kept in a GitHub repo.

---

*Last updated: 2026-09-24 (`README.md` revamped into an executive-style
portfolio; `dsh-mux` and `dsh-feature-loop` added as the first featured
projects; upstream `OmniRoute` moved to the bottom and kept with honest
attribution; current remote plugin status, dynamic signals, public research
basis, and accessibility-oriented Markdown structure documented.)*
