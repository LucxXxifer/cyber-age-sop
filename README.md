# Cyber-Age SOP

[English](README.md) · [繁體中文](README.zh-TW.md)

Cyber-Age SOP is a small project-lifecycle system for turning a personal
software, hardware, UI, documentation, Skill, Docker, or automation idea into
a bounded delivery task with explicit evidence boundaries.

It has two coordinated layers:

- `skills/cyber-age-sop/`: the runtime Skill for anchoring, task profiling,
  delivery, verification, and review.
- `project-sop/`: durable project-type and presentation documents for keeping
  the same contract in an Obsidian vault or another knowledge base.

This repository is a personal open-source release. It is not an official
OpenAI, Codex, Obsidian, or GitHub project.

## What It Solves

The workflow is designed to prevent common project failures:

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

The current repository release is `0.1.3`.

- Runtime Skill version: `0.2`
- Project SOP document version: `0.1`
- Repository release version: `0.1.3`

Changes that alter routing, evidence boundaries, or safety gates should include
updated regression cases and a changelog entry.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Keep
changes narrow, preserve evidence boundaries, and do not add private transcripts,
credentials, device identifiers, or local filesystem paths.

## License

Unless a file states otherwise, this repository is licensed under the Apache
License, Version 2.0. See [LICENSE](LICENSE).
