# Changelog

All notable changes to this repository are documented here.

## [0.4.5] - 2026-10-15

### Added: Integration Readiness Gate

- Distinguish decision, discovery, prototype, build, and field readiness.
- Treat a Decision Brief as a proposal unless the user explicitly confirms the direction.
- For platform, tenant, API, identity, and sensitive-data integrations, require a verified readiness matrix before labeling work build-ready.
- When tenant or interface facts are unknown, create a bounded read-only discovery task instead of inventing API contracts or implying the plan is ready to implement.
- Added integration-readiness regression criteria.

This is a workflow clarification. It does not select a vendor/platform, authorize tenant access, or change the SOP's discovery and MVP principles.

## [0.4.4] - 2026-10-13

### Added: Decision Brief (Gate 3.5)

Anchor, Technical Translation, and MVP scope used to stay in the chat and were lost when it closed. The skill now writes a Decision Brief file outside the repository after the user picks a direction, unless the user opts out.

- Minimal version (problem, recommendation, non-goals, next step) for short conversations
- Full version: user's words, facts vs assumptions, recommendation with sourced estimates and switch cost, version 1 scope, evidence, next steps and hand-off
- Path Selection now routes unclear build requests to the Brief

Files: `SKILL.md` (Gate 3.5, version 0.4.4), new `references/decision-brief-template.md`.

Not verified: whether real users save or reuse the Brief (v0.5 feedback collection).

## [0.4.3] - 2026-10-13

### Changed: Minimal web research fallback

- `references/web-research.md` cut from 541 to ~180 lines
- Fallback order: available tools → model knowledge with its cutoff date → state the limitation
- No static URL lists or answer databases in the skill

## [0.4.2] - 2026-10-12

### Added: Visual Aids & Web Research (User-Controlled)

**What:** Two optional capabilities to help non-technical users see product structure and verify technical decisions.

**Why:** User feedback identified two critical gaps:
1. Non-technical users struggle to **see** product structure from verbal descriptions
2. Users cannot trust feasibility/cost claims without verification

**Design principle:** Both features are **user-controlled** — trigger only when user asks directly OR agent suggests and user confirms. This avoids token bloat and respects user's pace.

#### 1. Visual Aids (视觉化辅助)

**Purpose:** Help users see product structure through simple ASCII diagrams (flow/architecture/layout).

**Trigger conditions:**
- User asks directly: "画个图" / "帮我画流程图" → generate immediately
- Agent suggests when: complex flow (3+ steps/branches) / multi-role / multi-module / layout → wait for confirmation

**Key safeguards:**
- Agent says "我可以画个图帮你看清楚，要吗？" (offers, doesn't assume)
- User says "好"/"要" → generate; "不用"/"先不要" or changes topic → skip silently
- Won't force visuals if user already understands

**Example suggestion:**
```
听起来流程有几个分支，我可以画个简单流程图帮你看清楚，要吗？
```

#### 2. Web Research (联网研究)

**Purpose:** Verify technical feasibility, obtain cost estimates, fact-check constraints via Tavily search/extract.

**Trigger conditions:**
- User asks directly: "查一下 XX" / "最新价格是多少" → research immediately
- Agent suggests when: uncertain feasibility / cost estimation needed / specific tool mentioned / need evidence for `确定不可行` → wait for confirmation

**Key safeguards:**
- Agent states uncertainty first: "我不确定 XX 是否支持...，我可以查一下，要吗？"
- User says "查吧"/"好" → research; "不用"/"我知道" → continue with existing info
- If user provides answer directly ("我预算是 $50/月") → use their info, skip research

**Citation format:**
- `查证`：根据 [来源](URL) (YYYY-MM-DD 验证)，...
- `经验估算`：基于类似项目经验，... (未查证)
- `未查证估算`：可能...，需要进一步确认

**Example suggestion:**
```
我不确定 Firebase 是否支持这个功能，我可以查一下官方文档，要吗？
```

#### Files Changed

- `SKILL.md`: Added "Visual Aids (Optional)" and "Web Research (Optional)" sections (~60 lines)
- `references/visual-aids.md`: NEW file — complete visual aids guide (~187 lines)
  - 3 diagram types: flow / architecture / layout
  - ASCII templates with examples
  - When to suggest vs when NOT to use
  - Quality checklist
- `references/web-research.md`: NEW file — complete web research guide (~600 lines)
  - 4 trigger scenarios with templates
  - Tavily skill usage (search/extract)
  - Citation format (3 evidence quality levels)
  - Integration with certainty labels
- `CHANGELOG.md`: This entry

**Total:** +847 lines

#### Verification

- ✓ Trigger logic is user-controlled (no auto-generation)
- ✓ Suggestion templates are standardized
- ✓ Confirmation protocol is explicit (wait for user response)
- ✓ Skip-silently behavior defined (user declines or changes topic)
- ✓ Citation format matches Technical Translation requirements
- ✓ Integrated with existing certainty labels (`确定不可行` / `我不知道` / `有条件可行`)

**Not verified:** Feature effectiveness with real users (planned for v0.5 baseline testing)

**Remaining risk:** 
- May still over-suggest in practice (needs real usage data)
- Users may not understand when to accept vs decline suggestions
- Token cost in practice unknown (design aims for low default cost)

#### Context Cost

| Version | Total Lines | Estimated Tokens | Increment |
|---|---|---|---|
| v0.4.1 | 1,040 | ~20K | baseline |
| v0.4.2 | 1,887 | ~27K | +7K (~35%) |

**Assessment:** 35% increase is within healthy range for Opus 5.5. Features are opt-in, so most conversations won't trigger both.

---

## [0.4.1] - 2026-10-12

### Added: Failure Path Protocol

**What:** Complete protocol for handling situations where users cannot articulate their needs after facilitated exploration.

**Why:** Red-team review (B4 blocking issue) identified that v0.4.0 only had a positive path — it assumed users could always answer open questions. Non-technical users often say "I don't know" or "You decide for me."

#### New: Three-Step Escalation

1. **Try Different Angle**: Reframe from time/problem-goal/self-others perspectives
2. **Offer Candidate Anchors**: 3-5 specific, diverse scenarios as exploration aids (not preset solutions)
3. **Generate Blocked Report**: Document what was explored, what's unclear, suggest next steps

#### New: Certainty Labels

When stating feasibility, use one of three explicit labels:

- `确定不可行`: verified blocker (requires source + date + specific reason)
- `我不知道`: need external info (state what info + why it determines feasibility)
- `有条件可行`: feasible with conditions (list conditions + switch cost)

#### Files Changed

- `SKILL.md`: Added "When User Cannot Answer (After 2 Rounds)" section (~90 lines)
- `references/failure-path.md`: New file — complete protocol documentation (~280 lines)
- `references/acceptance-and-evidence.md`: Added "Blocked Path Acceptance" section (~35 lines)

#### Verification

- ✓ Logical completeness: covers all blocked-path scenarios (cannot answer / rejects options / needs feasibility statement)
- ✓ Consistency with guided-thinking principles (acknowledge first / preserve autonomy / explicit uncertainty)
- ✓ Consistency with red-team B4 requirements (candidate anchors / blocked report / certainty labels)

**Not verified:** Protocol effectiveness with real users (planned for v0.5 baseline testing)

**Remaining risk:** 
- Protocol may still be too structured for some facilitation scenarios
- Certainty labels may be applied inconsistently without real usage examples

---

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
