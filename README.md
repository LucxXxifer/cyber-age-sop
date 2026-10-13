# Cyber-Age SOP

[English](README.md) · [繁體中文](README.zh-TW.md)

Cyber-Age SOP is a deep discovery and boundary-clarification framework for designers, project owners, and Agents. It helps turn a software, hardware, UI, documentation, Skill, Docker, automation, creative, media, or game idea into clear decisions, a bounded task, and explicit evidence boundaries.

**v0.4.4 (2026-10-13): Decision Brief.** After discovery and technical translation, the skill writes a Decision Brief file (outside the repository) that a non-technical user can save, share, and hand to a developer or Agent.

It is not a project-management platform and it is not a domain solution. It does not replace a software engine, creative tool, media generator, game engine, or specialist review.

It has two coordinated layers:

- `skills/cyber-age-sop/`: the runtime Skill for anchoring, task profiling, delivery, verification, and review. **Now with facilitated discovery** to support non-technical users through guided exploration.
- `project-sop/`: durable project-type and presentation documents for keeping the same contract in a knowledge base.

This repository is a personal open-source release. It is not an official OpenAI, Codex, or GitHub project.

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

## Repository Structure

This repository contains:

| Directory | Purpose | For whom |
|---|---|---|
| `skills/cyber-age-sop/` | Runtime Skill — the installable package | **Users:** Copy this to your agent runtime's skill directory |
| `project-sop/` | Project documentation templates and patterns | **Optional:** Reference if you want to document your own projects |
| `.github/workflows/` | Validation and release automation | **Contributors:** CI/CD for the public package |

**For users installing this skill:**
- Copy `skills/cyber-age-sop/` to your agent runtime
- The skill works immediately; no additional setup needed
- `project-sop/` templates are optional — use them if you want structured project documentation

**For contributors:**
- The skill package is self-contained in `skills/cyber-age-sop/`
- `project-sop/` documents define reusable project-record patterns
- Keep private design notes and evidence chains separate (not in this public repo)

## Repository Layout

```text
skills/cyber-age-sop/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── acceptance-and-evidence.md
    ├── decision-brief-template.md
    ├── failure-path.md
    ├── regression-cases.md
    ├── task-profiles.md
    ├── technical-translation.md
    ├── visual-aids.md
    └── web-research.md

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
adapt the files to the runtime's supported Skill format.

**Network dependency:** None required. When the runtime offers a web search or fetch tool, the Skill can use it to check feasibility and prices; otherwise it answers from model knowledge and states the knowledge cutoff.

**Facilitation principles:** This Skill incorporates guided exploration principles (acknowledging, inviting description, progressive layering) adapted from facilitation and coaching practices. It does not replace dedicated facilitation or coaching skills, and does not automatically redirect to other skills. The guided discovery approach is built into the Discovery phase to help non-technical users surface their intent and boundaries.

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
- internal markdown links in the public package;
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

The current repository release is `0.4.4`.

- Runtime Skill version: `0.4.4` (decision-brief, 2026-10-13)
- Project SOP document version: `0.1`
- Repository release version: `0.4.4`

### v0.4.4 Changes (from v0.4.3)

**Added: Decision Brief (Gate 3.5)**

- The skill writes a Decision Brief file outside the repository once the user picks a direction, unless the user opts out
- Minimal version (problem, recommendation, non-goals, next step) or full version (user's words, facts vs assumptions, sourced estimates, switch cost, version 1 scope, evidence, next steps)
- New `references/decision-brief-template.md`

### v0.4.3 Changes (from v0.4.2)

**Simplified: Minimal Web Research with Model Knowledge Fallback**

Core principle: **Skill defines process flow, model provides knowledge.**

**Changes:**
- Simplified `references/web-research.md` from 541 lines to ~180 lines (-66%)
- Removed all static knowledge database concepts (no URL lists, no experience answer database)
- Defined 3-tier fallback strategy:
  1. Try available tools (tavily-search, WebSearch, WebFetch)
  2. Use model knowledge with clear timestamp: "基於模型知識（截至 2026-06），[答案]。建議查閱: [URL]"
  3. Graceful failure with research directions

**Key insight from agent/IDE research:**
- All platforms have model's built-in knowledge (training data up to 2026-06)
- Model already knows common service docs, API limits, typical timelines
- **No need for skill to duplicate this knowledge**

**Design philosophy:**
- ✅ Skill responsibility: define trigger conditions, tool detection, fallback order, citation format
- ✅ Model responsibility: provide knowledge, generate doc URLs, estimate timelines
- ❌ Skill does NOT maintain static knowledge databases

**Files changed:**
- `references/web-research.md`: -361 lines (-66%)

**Context cost:** v0.4.2 (1,887 lines) → v0.4.3 (~1,526 lines), -19%

### v0.4.2 Changes (from v0.4.1)

**Added: Visual Aids & Web Research (User-Controlled)**

Two optional capabilities to help non-technical users see product structure and verify technical decisions:

1. **Visual Aids (视觉化辅助)**
   - Purpose: Help users see product structure through simple ASCII diagrams
   - 3 diagram types: flow diagram / architecture diagram / interface layout
   - Triggering: User asks directly → generate immediately; Agent suggests when complexity justifies → wait for confirmation
   - Example suggestion: "听起来流程有几个分支，我可以画个简单流程图帮你看清楚，要吗？"

2. **Web Research (联网研究)**
   - Purpose: Verify technical feasibility, obtain cost estimates via Tavily search/extract
   - 4 trigger scenarios: uncertain feasibility / cost estimation / specific tool mentioned / need evidence for `确定不可行`
   - Citation format: 3 levels (查证 / 经验估算 / 未查证估算)
   - Example suggestion: "我不确定 XX 是否支持这个功能，我可以查一下官方文档，要吗？"

**Design principle:** Both features use user-controlled triggering to avoid token bloat. User asks → immediate action; Agent suggests → wait for confirmation; User declines or ignores → skip silently.

**Files changed:**
- `SKILL.md`: +60 lines (Visual Aids + Web Research sections)
- `references/visual-aids.md`: NEW file, 187 lines
- `references/web-research.md`: NEW file, 600 lines
- `CHANGELOG.md`: v0.4.2 entry

**Context cost:** v0.4.1 (1,040 lines, ~20K tokens) → v0.4.2 (1,887 lines, ~27K tokens), +81%

### v0.4.1 Changes (from v0.4.0)

**Added: Failure Path Protocol**

Addresses red-team B4 blocking issue — v0.4.0 only had positive path (user can answer questions).

**When User Cannot Answer (After 2 Rounds):**
1. Try Different Angle: time perspective / problem vs goal / self vs others
2. Offer Candidate Anchors: 3-5 specific scenarios user can pick or reject
3. Generate Blocked Report: markdown template with certainty labels

**Certainty labels:**
- `确定不可行`: with source + date + alternative
- `我不知道`: what external info is needed
- `有条件可行`: list preconditions with verification method

**Files changed:**
- `SKILL.md`: +90 lines (When User Cannot Answer section)
- `references/failure-path.md`: NEW file, 280 lines
- `references/acceptance-and-evidence.md`: +35 lines

### v0.4.0 Changes (from v0.3)

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
