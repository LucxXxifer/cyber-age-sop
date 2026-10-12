# Changelog

All notable changes to this repository are documented here.

## [0.4.0] - 2026-10-12

### Major: Facilitation Principles Restored

**Redesign: Non-technical user support through guided discovery instead of mechanical questioning**

#### Trigger Condition (Strategy A)

- Now explicitly targets BUILD/DEVELOP scenarios (vs. tool selection)
- Trigger: "build/develop/create X for my team/company", "existing tools don't fit", "help me build from scratch"
- No trigger: "should I use A or B?", "where to find a tool for X?", "tool comparison"
- Ambiguous: ask ONE clarifying question ("你是想找现成的工具使用,还是要开发一个定制的?")

#### New: Discovery: Facilitated Exploration (before Gate 1)

Replaced mechanical gate-filling with conversational discovery:
- **Acknowledge first** ("你说...我听到的是...") before asking
- **Invite description** ("你现在怎么做?") instead of preset menus  
- **One round, one question**: wait for answer before next question
- **Progressive layer separation**: feeling/thought/intent/fact emerge naturally
- **Conversational tone**: "我想先了解一下" not "我需要了解一个会影响的问题"

#### Round-Trip Commitment (Phased)

- **Discovery phase**: +2~3 rounds to establish direction (necessary for unclear intent)
- **After anchor**: ≤ +1 round for Technical Translation and decision
- **Trivial tasks**: skip Discovery, direct execution
- **Trade-off**: baseline gives instant output; this skill adds exploration so user makes informed decisions

#### Anti-Patterns Added

1. "Menu-driven questioning": giving preset options instead of letting user describe
2. "Skipping acknowledgment": jumping to questions without showing you heard

#### Example Language

- More natural phrasing throughout
- Removed procedural feel: "那我换个角度" → "我想从另一个方向了解"

### Technical Changes

- `SKILL.md` version: 0.3 → 0.4, status: red-team-reviewed → facilitation-restored
- All references: technical-translation.md, task-profiles.md, acceptance-and-evidence.md, regression-cases.md updated
- No breaking changes to Gates 2-6 or existing task profiles

### User Guidance

- Non-technical users: expect 2-3 discovery rounds, then clear decision points
- Technical users: use trivial fast path for small changes, normal path for unclear scope
- Tool selection questions: answer directly, don't trigger cyber-age-sop

---

## [0.1.4] - 2026-10-11

### Changed

- Clarify that Cyber-Age SOP is a deep discovery, design-boundary, and
  handoff framework rather than a project-management platform or domain
  solution.
- Explain how the framework can be applied to large systems, creative work,
  AI-generated media, and games without replacing domain engines or human
  review.
- Clarify the separate roles of GitHub and Obsidian.

## [0.1.3] - 2026-10-11

### Changed

- Remove private project names and named facilitation-tool references from the
  public introductions.
- Rename the project-specific reference page to
  `reference-project-template.md` and generalize its content.

## [0.1.2] - 2026-10-11

### Added

- Add a Traditional Chinese README with an English / Traditional Chinese
  language switch at the top of both project home pages.
- Update the README version section to the current repository release.

## [0.1.1] - 2026-10-11

### Fixed

- Use the canonical Apache License 2.0 text so repository license detection
  remains interoperable with GitHub and other tooling.

## [0.1.0] - 2026-10-11

### Added

- Public `cyber-age-sop` runtime Skill package.
- Code, UI/documentation, and field task profiles.
- Acceptance and evidence contract.
- Regression cases for scope, handoff, field safety, facilitation boundaries,
  and runtime UI claims.
- Public `cyber-age-project-sop` type definition and lifecycle documents.
- Structure-only reference-project sample.
- GitHub Actions validation and tagged-release packaging.

### Boundary

- No private Cyber-Age vault content, raw transcripts, device identifiers,
  deployment logs, credentials, or field evidence is included.
