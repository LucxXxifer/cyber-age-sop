---
name: cyber-age-sop
description: Use when a user wants to anchor, scope, design, hand off, implement, verify, review, or improve a personal software, hardware, UI, or documentation project through the Cyber-Age workflow. Do not use for standalone facilitation, self-reflection, relationship, or coaching requests.
metadata:
  short-description: Run the Cyber-Age project SOP
  version: "0.2"
  status: red-team-reviewed
---

# Cyber-Age SOP

`cyber-age-sop.skill` is the project-lifecycle skill for Cyber-Age. It turns a
stable project intention into a bounded delivery task, then checks the actual
evidence after execution.

## Hard Boundary

This skill is independent from dedicated facilitation tools.

- Do not invoke a facilitation tool automatically.
- Do not turn a project task into emotional, relationship, coaching, or
  consent-oriented facilitation.
- Borrow only the project-useful principles: preserve the user's wording,
  separate facts from assumptions, ask one high-impact question at a time, and
  converge when the next decision is clear.
- If the user asks for guided, reflective, or layered questioning, hand the
  facilitation to the appropriate dedicated tool. Do not imitate that tool's
  voice or continue project anchoring. Resume only when the user returns with a
  `Thought Brief` or explicitly asks to run the project SOP.
- If the requested facilitation tool is unavailable, state that the handoff
  cannot be performed here; do not silently substitute a coaching-style
  interaction.

`prompt-refiner` is an optional packaging tool, not a mandatory stage. The SOP
may create an Agent Brief directly when the task is already precise.

## Routing

Choose the smallest path that can safely produce the requested result:

| Situation | Path |
|---|---|
| One-file typo, formatting fix, or similarly trivial low-risk change with a known check | Use the trivial fast path below |
| Clear bounded task with more than a trivial change | Create a short Agent Brief and execute |
| Unclear project intent or scope | Run project-only anchoring below |
| Architecture, UI, or delivery choice is unsettled | Add a Shape/Decision checkpoint |
| Code, UI/documentation, or field work has different evidence needs | Load the matching task profile |
| Existing brief needs conversion to an executable prompt | Use `prompt-refiner` |

Do not force every project through every artifact.

## Trivial Fast Path

Use this path only when the change is small, reversible, low-risk, and already
well specified by the user. Examples include one typo, one formatting fix, or
one known documentation link repair.

1. Restate the one-sentence change and the one relevant check.
2. Make the smallest change.
3. Run the relevant check and inspect the diff.
4. Report the result briefly in the conversation.

Skip the full Project Anchor, task profile, full Agent Brief, external report
file, and SOP feedback for this path. If the task expands, affects behavior,
touches permissions, or has unclear evidence, return to the normal gates.

## Gate 1: Project Anchor

Use a compact anchor, not a questionnaire:

```markdown
## Project Anchor
- Human goal:
- Primary user and situation:
- Problem in one sentence:
- Confirmed facts:
- Unverified assumptions:
- In scope:
- Out of scope:
- Evidence boundary:
- Deliverables:
- Stop or recovery condition:
```

Do not print the entire anchor template as a questionnaire for an
underspecified idea. Ask exactly one plain-language question first: the one
whose answer can most change the project's scope, evidence, or delivery path.
Fill the anchor progressively as answers arrive.

Ask only the next question that can change scope, evidence, or delivery. Skip
questions already answered by the user or existing material. Stop anchoring when
the next decision no longer changes this task's direction.

If two bounded exploration passes do not produce a workable anchor, stop and
report the blocking uncertainty instead of searching the whole repository
indefinitely.

## Thought Brief Handoff

Treat a user-provided Thought Brief as authoritative when it contains a goal,
scope, non-goals, acceptance signal, and evidence or permission boundary.
Do not repeat questions already answered there. Ask only for a missing fact
that can change scope, evidence, authorization, or delivery.

## Gate 2: Task Profile

Select one primary profile and load its reference:

- `code`: behavior, allowed files, tests, build, and diff.
- `ui-doc`: user-visible states, wording boundaries, UI/documentation parity,
  static/runtime checks.
- `field`: preflight, rollback, environment, observation, and long-running
  evidence.

Read [references/task-profiles.md](references/task-profiles.md) only for the
selected profile.

## Gate 3: Delivery Contract

Before implementation, produce an Agent Brief containing:

- `Project ID`, project name, `Task ID`, and date;
- goal and user context;
- human decisions and accepted trade-offs;
- scope and non-goals;
- input files and design material;
- constraints, permissions, dependencies, and environment boundary;
- required behavior and failure behavior;
- validation commands and expected results;
- acceptance criteria;
- reporting path outside the repository;
- a `Follow-up discoveries` section for useful but out-of-scope findings.

For risky or ambiguous work, list an explicit file allowlist. Do not let a
follow-up discovery silently become implementation scope.

Use a lightweight Brief for a bounded task and a full Brief only when the task
has multiple files, multiple evidence tiers, live access, material risk, or
uncertain scope. A lightweight Brief may contain only goal, allowed files,
non-goals, one acceptance signal, one validation command, and reporting form.

## Gate 4: Execute and Verify

The Agent may inspect, restate the contract, implement the smallest change,
and run the specified checks. It must not change the project goal, access
unauthorized devices/accounts/secrets, or claim field success from local tests.

For live field or infrastructure work, do not execute a command until the
following are explicit:

- exact target and environment;
- authorized scope and who authorized it;
- intended change;
- backup or configuration capture;
- rollback method and out-of-band recovery path;
- timeout and stop condition;
- observations that will count as pass or failure.

If any item is missing, remain in planning mode and report the blocking gap.

The orchestrator independently checks the result:

1. Read the actual version-control diff and changed-file list.
2. Confirm no report, log, cache, or generated artifact landed in the repo.
3. Re-run the narrowest relevant checks, then broader checks when required.
4. Separate code, build/release, field, and long-running evidence.
5. For UI/documentation work, check state-to-wording parity and run static
   syntax checks. If a claim depends on runtime rendering, interaction, or
   responsive layout, use a real browser or mark that claim `Not verified`.

Use [references/acceptance-and-evidence.md](references/acceptance-and-evidence.md)
for the audit and report contract.

## Gate 5: Review and Improve

For normal or full tasks, end with:

```markdown
## Changed
## Verified
## Not verified
## Remaining risk
## Follow-up discoveries
## SOP feedback
```

Only promote a workflow change when a repeated failure or a meaningful
experiment supports it. Do not add a permanent rule for a one-off preference.

## Non-Negotiables

- Smallest viable slice before generalization.
- Scope and non-goals before implementation.
- Evidence before completion claims.
- Reports and temporary outputs outside the repository.
- No live deployment, external publication, credential use, or destructive
  action without explicit authorization.
- `no local warning` is not the same as `runtime success`; local success is not
  the same as field acceptance.
