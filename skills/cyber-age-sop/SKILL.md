---
name: cyber-age-sop
description: Use when someone has a product-shaped goal but cannot articulate boundaries, or doesn't know how to delegate it to an agent. Not for those still exploring what they want (→ guided-thinking) or who need options first (→ brainstorming). Not for domain-specific creative execution (→ huashu-design, meigen for visual work).
metadata:
  short-description: Turn fuzzy product ideas into bounded, verifiable MVP delivery
  version: "0.3"
  status: red-team-reviewed
---

# Cyber-Age SOP

`cyber-age-sop.skill` helps you turn a product idea into a bounded delivery task with clear evidence criteria, then verifies what was actually delivered.

## Routing

This skill is for someone who:
- Has a product-shaped goal ("I want to make X") but cannot scope it
- Doesn't know how to explain requirements to an agent or engineer
- Faces technical choices but lacks the context to evaluate them
- Needs to verify what "done" actually means

**Not for:**
- Exploring what you want → use `guided-thinking`
- Generating options to compare → use `brainstorming`
- Visual/brand creative execution → use `huashu-design` or `meigen`
- Facilitation, coaching, or relationship work → use `guided-thinking`

## Hard Boundaries

This skill is independent from `guided-thinking`.

- Do not invoke `guided-thinking` automatically.
- Do not turn a project task into emotional, relationship, coaching, or consent-oriented facilitation.
- Borrow only project-useful principles: preserve user wording, separate facts from assumptions, ask one high-impact question at a time, converge when the next decision is clear.
- If the user asks for 大师级引导、大師級引導、引导大师、引導大師, guided thinking, or layered questioning, hand off to `guided-thinking`. Resume only when they return with a Thought Brief or explicitly ask to run the project SOP.

`prompt-refiner` is an optional packaging tool, not a mandatory stage.

## Path Selection

Choose the smallest path that safely produces the requested result:

| Situation | Path |
|---|---|
| One-file typo, formatting fix, or trivial low-risk change with known check | Trivial fast path below |
| Clear bounded task, more than trivial | Create short Agent Brief and execute |
| Unclear project intent or scope | Project-only anchoring below |
| Architecture, UI, or delivery choice unsettled | Add Shape/Decision checkpoint |
| Code, UI/documentation, or field work with different evidence needs | Load matching task profile |
| Existing brief needs conversion to executable prompt | Use `prompt-refiner` |

Do not force every project through every artifact.

## Trivial Fast Path

Use only when the change is small, reversible, low-risk, and well-specified. Examples: one typo, one formatting fix, one known documentation link repair.

1. Restate the one-sentence change and the one relevant check.
2. Make the smallest change.
3. Run the relevant check and inspect the diff.
4. Report the result briefly in the conversation.

**Upgrade condition**: If the same kind of small change appears 3+ times, upgrade to full Brief path.

Skip full Project Anchor, task profile, full Agent Brief, external report file, and SOP feedback for this path. If the task expands, affects behavior, touches permissions, or has unclear evidence, return to normal gates.

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

**Discovery protocol**: Ask exactly one plain-language question first — the one whose answer can most change project scope, evidence, or delivery path. Fill the anchor progressively as answers arrive.

**If the user cannot answer**: After two exploration passes without a workable anchor, do not report "blocked" and stop. Instead:

1. Offer 3-5 candidate problem anchors based on what they said, let them pick one.
2. If still unclear, classify the situation:
   - "I don't know what I want yet" → hand off to `guided-thinking`
   - "I want to compare options" → hand off to `brainstorming`
   - "Definitely not feasible at MVP stage" → state this with reasoning and suggest closer alternative
   - "I cannot determine feasibility" → mark with source and date, state what info is missing

**Certainty labels**: Use `确定不可行` (definitely not feasible) vs `我不知道` (I don't know) vs `有条件可行` (feasible with conditions). Always cite source and date for feasibility claims.

Skip questions already answered by the user or existing material. Stop anchoring when the next question no longer changes this task's direction.

### MVP Framing Rules

Before defining MVP scope, write:

**Core Invariant** (cannot be substituted):
> "The user wants to change [X]. This version must not replace it with [Y]."

Then apply the narrowing question:
> "If we remove [feature], will the user notice immediately?"
> - Yes → include in MVP
> - No → move to non-goals

**Floor condition**: The MVP must let the user's specified problem be touched in a real scenario, not just any demonstrable slice.

For each cut, state explicitly: "This cut loses [capability/constraint]. Acceptable because [reason]."

## Thought Brief Handoff

Treat a user-provided Thought Brief as authoritative when it contains goal, scope, non-goals, acceptance signal, and evidence or permission boundary. Do not repeat questions already answered there. Ask only for a missing fact that can change scope, evidence, authorization, or delivery.

## Gate 2: Task Profile

Select one primary profile and load its reference:

- `code`: behavior, allowed files, tests, build, and diff.
- `ui-doc`: user-visible states, wording boundaries, UI/documentation parity, static/runtime checks.
- `field`: preflight, rollback, environment, observation, and long-running evidence.

Read [references/task-profiles.md](references/task-profiles.md) only for the selected profile.

## Gate 3: Technical Translation (when needed)

When technical choices affect product outcomes, translate them for the user:

Read [references/technical-translation.md](references/technical-translation.md) for the translation protocol.

**Decision authority**:
- **Product-visible consequences** → user decides, user can veto
- **Implementation details** → agent proposes, must disclose, user can veto

All agent implementation choices must be disclosed and allow veto.

## Gate 4: Delivery Contract

Before implementation, produce an Agent Brief containing:

- `Project ID`, project name, `Task ID`, and date
- Goal and user context
- Human decisions and accepted trade-offs
- Scope and non-goals
- Input files and design material
- Constraints, permissions, dependencies, and environment boundary
- Required behavior and failure behavior
- Validation commands and expected results
- Acceptance criteria
- Reporting path outside the repository
- A `Follow-up discoveries` section for useful but out-of-scope findings

For risky or ambiguous work, list an explicit file allowlist. Do not let a follow-up discovery silently become implementation scope.

Use lightweight Brief for bounded task; full Brief only when task has multiple files, multiple evidence tiers, live access, material risk, or uncertain scope.

## Gate 5: Execute and Verify

The Agent may inspect, restate contract, implement smallest change, and run specified checks. It must not change project goal, access unauthorized devices/accounts/secrets, or claim field success from local tests.

For live field or infrastructure work, do not execute until these are explicit:

- Exact target and environment
- Authorized scope and who authorized it
- Intended change
- Backup or configuration capture
- Rollback method and out-of-band recovery path
- Timeout and stop condition
- Observations that count as pass or failure

If any item is missing, remain in planning mode and report the blocking gap.

The orchestrator independently checks the result:

1. Read actual version-control diff and changed-file list.
2. Confirm no report, log, cache, or generated artifact landed in repo.
3. Re-run narrowest relevant checks, then broader checks when required.
4. Separate code, build/release, field, and long-running evidence.
5. For UI/documentation work, check state-to-wording parity and run static syntax checks. If a claim depends on runtime rendering, interaction, or responsive layout, use real browser or mark `Not verified`.

Use [references/acceptance-and-evidence.md](references/acceptance-and-evidence.md) for audit and report contract.

## Gate 6: Review and Improve

For normal or full tasks, end with:

```markdown
## Changed
## Verified
## Not verified
## Remaining risk
## Follow-up discoveries
## SOP feedback
```

Only promote a workflow change when a repeated failure or meaningful experiment supports it. Do not add a permanent rule for one-off preference.

## Anti-Patterns (mark these in reviews)

1. **Self-justifying completion**: Claiming success by restating what was attempted, not what was verified.
2. **Evidence tier collapse**: Treating local test pass as field success.
3. **Scope drift via follow-up**: Quietly implementing out-of-scope discoveries without user decision.

## Non-Negotiables

- Smallest viable slice before generalization
- Scope and non-goals before implementation
- Evidence before completion claims
- Reports and temporary outputs outside the repository
- No live deployment, external publication, credential use, or destructive action without explicit authorization
- `no local warning` ≠ `runtime success`; local success ≠ field acceptance
- **Product-visible consequences require user decision; implementation details require disclosure and allow veto**
- Round-trip overhead vs no-skill baseline must not exceed +1 interaction
