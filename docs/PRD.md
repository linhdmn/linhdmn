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
- Selected open-source work: the owner's FreePeak organization projects listed in
  star order (most-adopted first), plus merged upstream contributions kept with
  honest attribution.
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
- **Selected work:** three featured projects (`dsh-mux`, `dsh-feature-loop`,
  `xdev`), then a star-ordered project table covering every FreePeak
  infrastructure repository, then a merged-only upstream contributions list.
- **Experience:** Be Group as current; BlueSG and ZaloPay explicitly previous.
- **Technical toolkit:** languages, agent/backend capabilities, and
  infrastructure grouped by practical use.
- **Engineering principles:** DDD, TDD, event-driven architecture, SOLID, KISS,
  and YAGNI.
- **Get in touch:** LinkedIn, GitHub, email, and a short invitation focused on
  relevant collaboration.

## 4. Research and verification basis

The 2026-09-24 revamp and this 2026-10-10 restructure used public GitHub
API/repository data and official GitHub documentation, not generic
portfolio templates:

- GitHub Docs, **Managing your profile README**:
  <https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme>
  — confirms the profile-special-repository model and the need for a clear,
  public README.
- GitHub Docs, **About the repository README file**:
  <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes>
  — supports standard Markdown, headings, links, and descriptive image alt text.
- Public GitHub API/repository pages for `linhdmn/linhdmn`, every FreePeak
  repository referenced in the table, and each upstream repository referenced
  under "Upstream contributions", checked on 2026-10-10.

Project descriptions come from each repository's public metadata and README.
The star ordering was computed from live `stargazers_count` values on
2026-10-10; because the badges are live shields.io images, the rendered order
can drift from a fast-moving star count, which is a known and accepted
limitation of a badge-based ranking.

The upstream section lists only pull requests with a non-null `merged_at`:
`pterm/pterm#811`, `pulumi/pulumi#24775`, `charmbracelet/bubbles#1057`,
`diegosouzapw/OmniRoute` (6 merged), and `punkpeye/awesome-mcp-servers#355`.

## 5. Key decisions

- **Professional positioning over a personal hobby board.** The header states
  the role and concrete domain first. The practice bullets make the value
  proposition scannable without claiming a new title or inventing a current
  focus.
- **Featured work before supporting work.** `dsh-mux` gets a short product
  description of the GUI-to-CLI thread workflow; `dsh-feature-loop` gets its
  bounded policy, budget, routing, detector, and human-gate model; `xdev` gets
  the single-static-binary agent summary. They lead because they are the
  owner's newest and most representative work.
- **Attribution honesty.** FreePeak projects are presented as organization
  work, while upstream repositories keep their full `owner/repo` link
  (`pterm/pterm`, not `pterm`) and a *merged* marker. No sole-authorship claim
  is made for any organization or upstream repository.
- **Complete infrastructure coverage, games excluded.** The star-ordered table
  lists all 14 FreePeak repositories that carry a description, a language, or a
  star count above zero — the entire infrastructure set. The 48 browser arcade
  games are deliberately excluded: no description, no license, no stars, and
  listing them would bury the infrastructure work. A closing line links the
  organization so they remain reachable.
- **Star order is the ranking.** The owner asked for a star-ordered list, so the
  table is sorted descending by live star count. The featured block above it is
  labelled "Featured" rather than as a ranking, so the two orderings cannot be
  read as one list.
- **Merged-only upstream section.** Upstream PRs are listed only when
  `merged_at` is non-null. Open or closed-unmerged PRs (9router, multica,
  awesome-ai-plugins) are deliberately omitted so nothing overstated survives.
- **Dynamic badges over volatile numbers.** Stars are rendered through
  `img.shields.io`; no point-in-time metric is hardcoded in the README. This
  keeps the page resilient to normal repository changes.
- **Evidence-oriented descriptions.** Functional language comes from each
  project's README and public repository metadata. Broad claims are kept
  durable ("agent infrastructure", "reliable systems") rather than presenting an
  unverified user, revenue, or adoption number.
- **Accessible, mobile-tolerant Markdown.** The page uses semantic headings,
  descriptive image `alt` text, descriptive link labels, short paragraphs, and a
  compact four-column project table rather than a wide table. It avoids a
  visual hero image and relies on native GitHub rendering so the content
  remains readable without JavaScript or custom CSS.
- **Employment status remains explicit.** Be Group is listed as Senior Software
  Engineer and current since September 2025; BlueSG and ZaloPay remain previous
  roles. No responsibility blurb is invented for Be Group.
- **No generic claim inflation.** The wording emphasizes systems thinking,
  reliability, evidence, and human control rather than unsupported labels such
  as "10x engineer", "AI thought leader", or guaranteed productivity gains.

## 6. Task record

Per repo convention, durable tasks for this repo live as GitHub issues on
`linhdmn/linhdmn`; this document is the status summary only, and no
task-tracker file is kept in a GitHub repo.

---

*Last updated: 2026-10-10 (`README.md` restructured into a star-ordered
open-source section: all 14 FreePeak infrastructure repositories listed with
live star badges, three projects featured, and a new "Upstream contributions"
section naming only merged PRs with honest `owner/repo` attribution; the 48
zero-signal arcade games excluded and linked via the organization pointer;
repository data verified against the GitHub API on 2026-10-10.)*
