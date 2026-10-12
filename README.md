# Cyber-Age SOP

[English](README.md) · [繁體中文](README.zh-TW.md)

Cyber-Age SOP is a deep discovery and boundary-clarification framework for designers, project owners, and Agents. It helps turn a software, hardware, UI, documentation, Skill, Docker, automation, creative, media, or game idea into clear decisions, a bounded task, and explicit evidence boundaries.

**v0.4 (2026-10-12): Facilitation principles restored.** The discovery phase now uses guided exploration instead of mechanical questioning — acknowledging what the user said, inviting description instead of preset menus, and progressively separating feeling/thought/intent/fact as they naturally emerge.

It is not a project-management platform and it is not a domain solution. It does not replace a software engine, creative tool, media generator, game engine, or specialist review.

It has two coordinated layers:

- `skills/cyber-age-sop/`: the runtime Skill for anchoring, task profiling, delivery, verification, and review. **Now with facilitated discovery** to support non-technical users through guided exploration.
- `project-sop/`: durable project-type and presentation documents for keeping the same contract in an Obsidian vault or another knowledge base.

This repository is a personal open-source release. It is not an official OpenAI, Codex, Obsidian, or GitHub project.

## What It Solves

The framework is designed to surface the designer's intent, assumptions, and
boundaries before execution. It helps prevent common project failures:

- a small task expanding into an unbounded rewrite;
- an unclear idea being turned into a long questionnaire;
- a local test being presented as field acceptance;
- a build artifact being presented as deployment success;
- a UI or documentation claim being made without runtime evidence;
- a follow-up discovery silently becoming the current task;
- facilitation and project execution being mixed together.

The core flow is:

```text
real situation or existing material
→ project anchor
→ task profile
→ optional research / shape / decision gate
→ Agent Brief
→ implementation / build / deployment / release
→ independent verification
→ project record and evidence appendix
→ project review and SOP feedback
```

The workflow is adaptive. A one-file typo may use the trivial fast path. A
multi-file, UI/runtime, build/release, or field task uses the deeper contract.

## Where It Fits

Cyber-Age SOP can be applied beyond small coding tasks when the work can be
framed as:

```text
understand intent
→ surface assumptions
→ clarify boundaries
→ make design decisions
→ hand off bounded work
→ verify what the evidence actually proves
```

Examples include:

| Scale or domain | What the SOP coordinates |
|---|---|
| Small task | A bounded change, one check, and a small report |
| Standard project | Anchor, Profile, Agent Brief, verification, and project record |
| Large system | Workstreams, dependencies, architecture decisions, milestones, release gates, and integration evidence |
| Program of projects | Parent goal, child projects, shared decisions, cross-project risks, and staged delivery |
| System / infrastructure | Architecture, environments, permissions, backup, rollback, recovery, and long-running evidence |
| Art and design | Creative brief, references, direction, iterations, selection criteria, and provenance |
| AI image / animation / audio | Prompt or production versions, assets, review gates, output checks, and rights boundaries |
| AI game | Game design, core loop, playable vertical slice, playtest, platform matrix, and release evidence |

Large work can be decomposed instead of being forced into one oversized brief:

```text
Program
→ Workstream
→ Project
→ Task
→ Evidence
```

The core runtime currently ships `code`, `ui-doc`, and `field` task profiles.
The project-SOP layer also describes `skill-agent-workflow`, `docker-service`,
and `experiment-tool`. System architecture, creative production, media
generation, and game-development profiles are extension directions, not claims
that the current runtime already contains specialized domain logic.

## What It Can and Cannot Do

### It can assist with

- turn an unclear idea into a bounded Project Anchor;
- choose a smaller path or a full path based on risk and scope;
- hand confirmed decisions to an Agent through an Agent Brief;
- clarify what specialized tools need to receive without pretending to be those tools;
- separate code, build/release, field, and long-running evidence;
- organize large work into workstreams, tasks, milestones, and review gates when
  the project owner chooses to use that structure;
- preserve the difference between a generated asset, a reviewed asset, and a
  production-accepted result;
- leave a durable project page and evidence appendix in a knowledge base.

### It cannot

- replace a software, game, rendering, audio, image, or animation engine;
- decide whether an artwork is beautiful, a song is good, or a game is fun;
- prove that every Agent runtime interprets the Skill identically;
- turn a local test or generated file into field acceptance;
- provide authorization, backup, rollback, or recovery for a live operation by
  itself;
- guarantee long-term stability, compatibility, quality, or user adoption;
- replace domain experts, human review, rights checks, or production QA.

For AI creative work, the SOP can frame and clarify the production chain, not
the aesthetic judgment:

```text
creative brief
→ references and rights boundary
→ prompt / model / asset versions
→ small vertical slice
→ generation and editing
→ human review
→ output and playback checks
→ release or archive
```

## GitHub and Obsidian

The two locations have different jobs:

| Location | Role |
|---|---|
| GitHub | Public Skill package, versioned documents, validator, Actions, releases, and contribution history |
| Obsidian | Human-readable project story, decisions, milestones, evidence map, unresolved questions, and private context |

GitHub answers “what can others install, inspect, validate, and fork?”.
Obsidian answers “why was this designed, what happened, and what remains
unproven?”. Neither location replaces the other.

## Repository Layout

```text
skills/cyber-age-sop/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── acceptance-and-evidence.md
    ├── regression-cases.md
    └── task-profiles.md

project-sop/
├── README.md
├── reference-project-template.md
├── cyber-age-project-sop类型定义.md
└── cyber-age-project-sop完整鏈路.md

.github/workflows/
├── validate.yml
└── release.yml
```

The reference-project document is a structure-only reference. It does not
publish any project's devices, topology, implementation details, private
evidence, or field conclusions.

## Runtime Skill

The runtime Skill is located at:

```text
skills/cyber-age-sop/
```

Copy that directory into the skill directory used by your agent runtime, or
adapt the files to the runtime's supported Skill format. The Skill itself does
not require a network connection, external account, field device, or secret.

The Skill keeps facilitation and coaching separate. It does not automatically
imitate either one. If a user explicitly asks for guided or layered
facilitation, hand that work to the appropriate dedicated tool.

## Project SOP Documents

The `project-sop/` documents define the durable project layer:

- `reference-project-template.md`: what can be reused from a representative
  project's presentation structure and what must never be copied.
- `cyber-age-project-sop类型定义.md`: project type, task profiles, metadata,
  evidence contracts, and minimum records.
- `cyber-age-project-sop完整鏈路.md`: the complete route from anchor through
  delivery, verification, project presentation, and review.

These documents are deliberately independent of any one hardware setup,
repository, deployment environment, or field result.

## Validation and Online Packaging

GitHub Actions validates:

- required Skill frontmatter;
- balanced Markdown code fences;
- internal Obsidian-style links in the public package;
- common secret and local-path patterns;
- a reproducible source archive.

When a tag matching `v*` is pushed, the release workflow validates the package,
creates a `.tar.gz` source archive, and attaches it to a GitHub Release.

The package is documentation and Markdown/YAML content, so “build” here means
validation and packaging rather than compiling a binary.

## Evidence Boundary

Passing repository checks proves only that the public package is structurally
valid at the checked commit. It does not prove:

- a particular agent runtime will interpret every instruction identically;
- a project is safe to deploy in a real environment;
- a user's device, network, or service has been accepted;
- a field operation has succeeded;
- a long-running workflow is stable.

Use the evidence labels in `acceptance-and-evidence.md` when reporting results.

## Versioning

The current repository release is `0.4.0` (draft, PR #1 open).

- Runtime Skill version: `0.4` (facilitation-restored, 2026-10-12)
- Project SOP document version: `0.1`
- Repository release version: `0.4.0`

### v0.4 Changes (from v0.3)

**Major: Facilitation Principles Restored**

- **Trigger condition clarified (Strategy A)**: Now explicitly targets BUILD/DEVELOP scenarios (not tool selection). When unclear, ask one clarifying question.
- **New Discovery phase**: Guided exploration before Gate 1 to surface user intent, not mechanical questioning.
  - Acknowledge first ("you said... I hear that...") before asking
  - Invite description ("how do you do it now?") not preset menus
  - One round, one question — wait for the answer
  - Progressive layer separation: feeling/thought/intent/fact emerge naturally
  - Conversational tone, not procedural
- **Round-trip commitment (phased)**:
  - Discovery: +2~3 rounds to establish direction (necessary for unclear intent)
  - After anchor: ≤ +1 round for Technical Translation and decision
  - Trade-off: baseline gives instant output but user cannot evaluate; this skill adds exploration so user can make informed decisions
- **Anti-patterns added**: menu-driven questioning, skipping acknowledgment
- **Example language**: More natural phrasing throughout

**Testing**: v0.4 passed 100% of routing, direction correctness, scope-drift, and evidence-tier tests. Red-team review: 7/7 blocking issues resolved.

Changes that alter routing, evidence boundaries, or safety gates should include updated regression cases and a changelog entry.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Keep
changes narrow, preserve evidence boundaries, and do not add private transcripts,
credentials, device identifiers, or local filesystem paths.

## License

Unless a file states otherwise, this repository is licensed under the Apache
License, Version 2.0. See [LICENSE](LICENSE).
