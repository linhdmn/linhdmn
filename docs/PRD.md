# PRD — `linhdmn/linhdmn` (GitHub Profile README)

## 1. Purpose

This repository is the owner's GitHub **profile special repo**: the single
`README.md` renders on `https://github.com/linhdmn` and serves as the public,
discoverable professional bio. There is no code, no build, and no test suite.
Success = a recruiter/peer can read the page in under 30 seconds and know who
writes what, at what scale, and how to make contact.

## 2. Scope

**In scope**

- `README.md` — the entire deliverable. Sections, order, and accuracy of every
  claim it makes.
- Factual correctness of project attribution, employment status, and metrics.

**Out of scope**

- Profile stats cards / contribution graphs. Deliberately removed in `4bf8b5a`
  ("Remove profile stats and current focus from README") and not to be
  reintroduced: they go stale and read as noise.
- A "current focus" section — same removal applies.

## 3. Structure (current)

| Section | Content |
| --- | --- |
| Header | Name, role line, one-line positioning statement, contact badge row |
| About | Experience since 2018; focus on AI-agent/production infrastructure |
| Open Source | Table of 6 projects: description + dynamic language/stars/forks badges |
| Tech Stack | shields.io badges grouped by languages, frameworks, data, infra |
| Experience | Current employer (Be Group, since Sept 2025) + prior roles (BlueSG, ZaloPay) marked *previous* |
| Engineering Principles | DDD, TDD, event-driven, SOLID, KISS & YAGNI |
| Get in Touch | LinkedIn / GitHub / email badges |

## 4. Key decisions

- **Dynamic badges over hardcoded counts.** Stars, forks, and primary language
  come from `img.shields.io/github/{stars,forks,languages/top}/<owner>/<repo>`,
  so the page cannot rot after a merge. Verified: 47/47 badge URLs render, no
  invalid Simple Icons slugs.
- **Attribution honesty.** Five projects are maintained under the shared
  `@FreePeak` organization (6 members). `OmniRoute` is **upstream** — owned by
  `diegosouzapw`, listed with its full `owner/repo` name and an
  `upstream · contributor` marker. `FreePeak/OmniRoute` 404s, so there is no
  org-owned copy to lean on, and no claim of sole authorship appears anywhere
  on the page.
  Supporting evidence, verified via `gh api` (exact-match grep over all
  contributor pages, not read off truncated output) **as of 2026-09-07**:
  `linhdmn` is contributor #294 of 428; 9 PRs authored, 6 merged (#8439,
  #10980, #11085, #11209, #11214, #11274), 1 open (#12333), 2 closed
  superseded; 6 authored commits matching the merges.
- **Durable claims on the page, dated evidence here.** The merged-PR count is
  deliberately *not* printed in `README.md`: it is a point-in-time number that
  rots the moment #12333 merges, which would contradict the dynamic-badge
  principle above. "contributor" stays true permanently; the count lives here,
  where it is explicitly dated.
- **Employment status is explicit, titles are not invented.** Be Group is
  listed as *current (since Sept 2025)*; BlueSG and ZaloPay are marked
  *previous*. The Be Group entry carries **no job title and no responsibility
  blurb**: the owner supplied the employer and start date only, and no title
  was recoverable from the workspace (employer notes confirm the work area but
  never state a role). Reusing the headline "Senior Software Engineer" from the
  prior README would have transferred a title across employers — the same
  unsupported-claim class as the removed "full-time". **Owner to supply the
  Be Group title** (and an optional one-liner) before that line is complete.

## 5. Task record

Per repo convention, durable tasks for this repo live as GitHub issues on
`linhdmn/linhdmn`; this document is the status summary only, and no
task-tracker file is kept in a GitHub repo.

---

*Last updated: 2026-09-07 (`README.md` rewritten in a professional profile
format; Open Source section added with 6 verified projects and dynamic badges;
upstream OmniRoute attribution evidenced by 6 merged PRs; current Be Group
employer added without an inferred job title.)*
