# Cyber-Age SOP Task Profiles

Select one profile before writing the Agent Brief. A project may later split
into separate tasks with different profiles.

## Code

Record:

- behavior that must change;
- allowed files and explicit non-goals;
- regression or fixture strategy;
- targeted and full validation;
- syntax, lint, build, or diff checks.

Do not treat a passing local test as deployment or field evidence.

## UI / Documentation

Record a semantic map before implementation:

| State or fact | User-visible wording | What it must not imply |
|---|---|---|
| Normal | What the user can safely know | Universal availability |
| Missing or unknown | What still needs confirmation | A guessed success |
| Failure or blocked | What happened and what action is safe | Blame or unsupported diagnosis |

Keep UI and documentation descriptions consistent. Define which layer owns the
fact: engine, status JSON, UI, documentation, or field acceptance. Validate
static syntax and text contracts. If a claim depends on runtime rendering,
interaction, responsive layout, or live state, browser evidence is required;
otherwise mark that claim as unverified.

## Field / Infrastructure

Record:

- target environment and authorized access;
- exact target and authorization source;
- preflight checks;
- configuration capture or backup;
- failure and rollback guard;
- out-of-band recovery path;
- timeout and stop condition;
- exact observations that count as evidence;
- post-change and long-running checks.

Never infer field success from source code, a build artifact, or a local fixture.
