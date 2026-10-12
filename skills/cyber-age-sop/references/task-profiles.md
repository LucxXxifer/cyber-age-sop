# Cyber-Age SOP Task Profiles

Select one profile before writing the Agent Brief. A project may later split into separate tasks with different profiles.

## Code

Record:

- Behavior that must change
- Allowed files and explicit non-goals
- Regression or fixture strategy
- Targeted and full validation
- Syntax, lint, build, or diff checks

Do not treat a passing local test as deployment or field evidence.

## UI / Documentation

Record a semantic map before implementation:

| State or fact | User-visible wording | What it must not imply |
|---|---|---|
| Normal | What the user can safely know | Universal availability |
| Missing or unknown | What still needs confirmation | A guessed success |
| Failure or blocked | What happened and what action is safe | Blame or unsupported diagnosis |

Keep UI and documentation descriptions consistent. Define which layer owns the fact: engine, status JSON, UI, documentation, or field acceptance. 

Validate static syntax and text contracts. If a claim depends on runtime rendering, interaction, responsive layout, or live state, browser evidence is required; otherwise mark that claim as unverified.

## Field / Infrastructure

Record:

- Target environment and authorized access
- Exact target and authorization source
- Preflight checks
- Configuration capture or backup
- Failure and rollback guard
- Out-of-band recovery path
- Timeout and stop condition
- Exact observations that count as evidence
- Post-change and long-running checks

Never infer field success from source code, a build artifact, or a local fixture.
