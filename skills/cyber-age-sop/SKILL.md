---
name: cyber-age-sop
description: >
  Use when someone wants to BUILD/DEVELOP a custom solution (tool, plugin, internal system) 
  and needs help scoping it into a deliverable MVP. 
  
  TRIGGER when user explicitly says:
  - "build/develop/create X for my team/company"
  - "existing tools don't fit, need custom solution"
  - "help me build X from scratch"
  
  DO NOT trigger when:
  - User wants to CHOOSE between existing tools → give direct recommendation
  - User asks "should I use A or B" → tool comparison
  - User says "I want to use/find/get X" → likely looking for existing solution
  
  When unclear: ask ONE clarifying question:
  "你是想找现成的工具使用,还是要开发一个定制的?"
metadata:
  short-description: Turn fuzzy product ideas into bounded, verifiable MVP delivery
  version: "0.4"
  status: facilitation-restored
---

# Cyber-Age SOP

`cyber-age-sop.skill` helps you turn a product idea into a bounded delivery task with clear evidence criteria, then verifies what was actually delivered.

## Routing

This skill is for someone who:
- Wants to build/develop a custom solution ("我要做一个 X 给团队用")
- Has a product-shaped goal but cannot scope it
- Doesn't know how to explain requirements to an agent or engineer
- Faces technical choices but lacks the context to evaluate them
- Needs to verify what "done" actually means

**Not for:**
- Tool selection or comparison ("该用 Notion 还是 Google Docs?") → give recommendation directly
- Exploring what you want → use `guided-thinking`
- Generating options to compare → use `brainstorming`
- Visual/brand creative execution → use `huashu-design` or `meigen`
- Facilitation, coaching, or relationship work → use `guided-thinking`

## Hard Boundaries

This skill is independent from `guided-thinking`.

- Do not invoke `guided-thinking` automatically.
- Do not turn a project task into emotional, relationship, coaching, or consent-oriented facilitation.
- Borrow facilitation principles: preserve user wording, acknowledge what they said before asking, separate facts from assumptions, ask one question at a time that invites description rather than menu selection.
- If the user asks for 大师级引导、大師級引導、引导大师、引導大師, guided thinking, or layered questioning, hand off to `guided-thinking`. Resume only when they return with a Thought Brief or explicitly ask to run the project SOP.

`prompt-refiner` is an optional packaging tool, not a mandatory stage.

## Path Selection

Choose the smallest path that safely produces the requested result:

| Situation | Path |
|---|---|
| One-file typo, formatting fix, or trivial low-risk change with known check | Trivial fast path below |
| Clear bounded task, more than trivial | Create short Agent Brief and execute |
| Unclear project intent or scope | Discovery exploration → Project Anchor |
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

## Discovery: Facilitated Exploration (before Gate 1)

When project intent or scope is unclear, create space for the user to describe their situation before filling any anchor template.

### Guiding Principles

1. **Acknowledge first, then explore**
   - Start by reflecting what the user said in their own words
   - Show you heard their uncertainty or confusion
   - Example: "你说想做一个记账工具，但不确定要做成 App 还是网页。我听到的是：你知道需要记账功能，但对实现形态还在考虑。"

2. **Ask questions that invite description, not menus**
   - ❌ Not: "你多久记一次账？A) 每次花钱 B) 每天晚上 C) 每周末"
   - ✅ Instead: "你现在是怎么记账的？或者，是什么让你觉得需要一个记账工具？"
   - Let the user tell their story; don't force them to pick from preset options

3. **One round, one open question**
   - Ask one question at a time
   - Don't chain multiple questions ("你的预算多少？用户有多少？什么时候要？")
   - Wait for the answer before deciding what to ask next

4. **Separate layers progressively**
   As the user describes, distinguish:
   - **感受/困惑**: Their uncertainty, frustration, or confusion ("不知道该怎么做")
   - **想法**: What they think might work ("可能做个 App？")
   - **意图**: What they actually want to achieve ("能方便记账")
   - **事实**: Confirmed current situation ("现在用 Excel 但经常忘记")

   Don't ask about all four layers at once. Let them emerge through natural conversation.

5. **Tone: conversational, not procedural**
   - ❌ Not: "在决定技术方案之前，我需要了解一个会影响项目范围的关键问题"
   - ✅ Instead: "在我们讨论做成什么样之前，我想先了解一下你现在的情况"

### When the User Cannot Describe Clearly

After **two rounds** of open exploration, if the project anchor is still unclear:

1. **First, try a different angle**
   - "我想从另一个方向了解：你平时在什么情况下会需要用到它？"
   - "或者这样问：设想一下，如果这个工具做好了，你会在什么时候打开它？"

2. **If still unclear, offer candidate anchors**
   - Present 3-5 possible problem anchors based on what they've said
   - Let them pick one or clarify which is closest
   - Example: "根据你说的，可能是这几个方向中的一个：1) ... 2) ... 3) ... 哪个更接近你的想法？或者都不是？"

3. **If none fit, classify and hand off**
   - "I don't know what I want yet" → hand off to `guided-thinking`
   - "I want to compare options first" → hand off to `brainstorming`
   - "Definitely not feasible at MVP stage" → state this with reasoning, suggest closer alternative
   - "I cannot determine feasibility" → mark with source and date, state what info is missing

### Discovery Output

As the conversation progresses, start filling the anchor **progressively** (not as a questionnaire):

```markdown
## Project Anchor (emerging)
- Human goal: [用户原话中的目标]
- Primary user and situation: [他们描述的使用场景]
- Problem in one sentence: [一句话总结要解决的问题]
- Confirmed facts: [用户已确认的现状]
- Unverified assumptions: [还需要验证的假设]
```

Stop discovery when you have enough to proceed to MVP Framing. Don't keep asking if the next question won't change the direction.

## Gate 1: Project Anchor

After discovery exploration, formalize the anchor:

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

Fill this progressively based on what emerged during discovery. Skip fields already clear from the user's description. Ask only when a missing fact would change scope, evidence, or delivery path.

**Certainty labels**: Use `确定不可行` (definitely not feasible) vs `我不知道` (I don't know) vs `有条件可行` (feasible with conditions). Always cite source and date for feasibility claims.

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
4. **Menu-driven questioning**: Giving the user preset options instead of letting them describe their situation.
5. **Skipping acknowledgment**: Jumping to questions without showing you heard what they said.

## Non-Negotiables

- Smallest viable slice before generalization
- Scope and non-goals before implementation
- Evidence before completion claims
- Reports and temporary outputs outside the repository
- No live deployment, external publication, credential use, or destructive action without explicit authorization
- `no local warning` ≠ `runtime success`; local success ≠ field acceptance
- **Product-visible consequences require user decision; implementation details require disclosure and allow veto**
- **Round-trip commitment (phased)**:
  - Discovery phase: +2~3 rounds to establish direction (necessary for unclear intent)
  - After anchor clear: ≤ +1 round for Technical Translation and decision
  - Trivial tasks: skip Discovery, direct execution
  - Quality trade-off: baseline gives instant output but user cannot evaluate; this skill adds exploration rounds but user can make informed decisions
- **Acknowledge what the user said before asking; invite description, not menu selection**
