# Minimal Lifecycle Traceability

Load for dependent work, changed requirements, versioned delivery, or resuming a project after context loss. Do not impose it on trivial edits.

Keep one decision source and one engineering view, using existing project files where possible. They may be sections of the same Brief. This is not a scheduler, separate Project State system, or permission to perform Git/publication operations.

## Decision Source and Reader View

Record who decided which scope and where that decision is evidenced. An API `user` role is a transport label, not proof of a human decision. Use `user-approved` only for an actual human's explicit approval; label simulation and authorized controller instructions by their real source. Neither grants authority beyond its stated scope. Keep engineering acceptance, implementer self-checks and human product acceptance separate.

Keep the current summary and eight-field Card readable without decoding technical IDs. Preserve the minimum SPEC, dependency gates, affected evidence, source identity and recovery information below in the existing engineering appendix. Cite verified records instead of copying their entire history into each response. Missing or stale evidence stays visible in the summary when it blocks the next action. Do not invent saved documents or remove essential engineering information to meet a length target.

## Minimum SPEC

Before implementing the current slice, its Agent Brief must identify:

- The accepted user need and observable behavior; a recommendation is not approval.
- Component boundaries and relevant inputs/outputs; add a small flow or wireframe only when it resolves a real product ambiguity.
- Data/format invariants, normal and failure behavior, environment and permission limits.
- Concrete acceptance examples, commands and expected observations.
- Unknowns that can change safety or correctness, with a bounded discovery task when unresolved.

Do not require the user to choose technical schemas or libraries. Read back product consequences in their language. Use the existing integration-readiness reference for external interfaces; a local SPEC cannot establish tenant/API permissions.

## Task Index

In the engineering appendix, link each accepted need to its SPEC section, task, tested source and evidence. Use stable IDs internally and everyday names for the user.

| Need / SPEC | Task / direct predecessor | Current status / deliverable | Acceptance method / checker | Source / evidence |
|---|---|---|---|---|
| [accepted behavior] | [task; exact accepted input it needs] | [actual known state] | [test and who checks it] | [version and usable record, or not verified] |

Reuse existing task records; do not duplicate full Briefs in the index. Work on one currently authorized task. Start dependent work only when the exact required predecessor output has applicable, independently checked evidence.

Keep implementation facts separate from activity gates: "existing implementation unknown" does not mean "not started." A blocked integration task may have pre-existing code. Say what is unknown and which activity cannot begin; do not overwrite history with a Card's progress label.

After implementation, run the specified checks and record actual results. Mark delivered-but-unchecked work pending acceptance. Record whether the checker is the implementer, another reviewer, or a real user; never relabel self-checks or simulated approvals as independent human acceptance.

## Change and Evidence Validity

When a requirement changes:

1. Identify the actual approval and whether product behavior, cost, scope, data or authority changed. Do not reopen an already settled decision.
2. Link the affected need, SPEC, tasks, tests and delivery claim. Update the existing source of truth, not a parallel replacement plan.
3. Preserve older evidence as valid history for its original behavior/source. Mark only the affected claims insufficient for the new revision; keep unrelated valid evidence.
4. Update implementation and relevant tests, rerun targeted checks plus necessary integration/regression checks, and have the required evidence checked again before dependent work.

A changed timestamp, reused version label or renamed evidence file cannot renew a test result. Conversely, editorial changes that do not affect behavior need not invalidate unrelated tests.

## Version Identity

Keep four identities separate: Skill version, approved SPEC revision, code baseline, delivery version/status. A proposed product version is not a release, and a release artifact is not deployment or user acceptance.

For a clean committed source, record its commit plus the relevant environment/configuration. For dirty or untracked work, record base HEAD when available and a scoped content-hash manifest covering the tested source, tests, configuration and lockfiles that affect the result. A file list or diff description alone cannot identify the exact bytes. Exclude unrelated/private files and state the boundary; missing required inputs keep reproducibility unverified.

Bind test results and deliverables to that snapshot, recording commands, expected/observed results, exit status, date and checker. Recheck source and artifact hashes before delivery; post-test edits can invalidate evidence.

Follow existing project versioning conventions. Do not force a branch or commit per task. Commit, tag, push, history changes, publication and deployment each need the applicable authorization; a local hash does not create a Git commit or grant that permission.

## Persistence and Recovery

Read the current Brief/engineering appendix and relevant actual source/evidence at session start, task switch, scope change, failed verification and delivery. Do not reread all history on every turn.

Files are an index to facts, not higher authority than actual source/tests. If they disagree, name the conflict and last verified state before advancing.

After a required update, read it back. If saving fails, report what was and was not persisted, preserve already valid evidence, and stop work dependent on that update. Do not claim success in chat, silently choose a second location or change permissions. Ask only for the missing location/authority decision; otherwise recover within the authorized scope.

Recovery must identify current applicable scope, accepted predecessor evidence, invalidated claims and next safe task. Missing context stays unknown. This protocol does not supply a background scheduler or autonomous cross-host synchronization.

## Storage Policy

Preserve user-specified locations and existing project conventions. Default new Briefs/reports outside the repository when no location is agreed.

With user approval and compatible project rules, durable Briefs, SPECs, task indexes and concise delivery records may be versioned in the repository. This is different from committing raw logs, secrets, sensitive datasets, caches or generated build artifacts; keep those outside in the approved controlled location and link a non-sensitive summary/hash when appropriate.

Do not move existing files or create a new document per row. If documents stay outside the repo, record their revision/hash with the tested source baseline. Keep the Next-Step Card as the current-work summary; detailed traceability belongs in the engineering appendix.
