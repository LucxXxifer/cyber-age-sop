# Acceptance and Evidence Contract

## Evidence Tiers

| Tier | Proves | Does not prove |
|---|---|---|
| Code / fixture | Behavior in the repository snapshot | Device or user acceptance |
| Build / release | An artifact was produced and checks passed | Deployment success |
| Field | The authorized environment showed the observed result | Every topology or long-term stability |
| Long-running | Behavior remained stable over the stated window | Unrelated environments |

Do not collapse these tiers into one "done" label.

## Required Final Report

Use the full report for normal, risky, multi-file, UI/runtime, build/release, or field tasks. Trivial fast-path work may report briefly in the conversation with the changed file, check result, and remaining uncertainty.

Use these headings exactly:

```markdown
## Changed
## Verified
## Not verified
## Remaining risk
## Follow-up discoveries
## SOP feedback
```

The report must be outside the repository. The audit should independently check:

- The report exists at the requested external path
- The required headings are present
- `git diff --name-only` is inside the allowlist
- `git status --short --untracked-files=all` has no unexpected artifacts
- Required validation commands have fresh output and exit status

## Completion Language

Use precise claims:

- "Local tests pass" for repository checks
- "Build artifact produced" for build checks
- "Field observation recorded" for authorized runtime evidence
- "Not verified" for anything outside the executed evidence

Do not write "works everywhere", "all clients accepted", "production-ready", or similar claims unless the stated evidence actually covers that scope.

## Anti-Pattern Detection

Flag these in reviews:

1. **Self-justifying completion**: "Successfully implemented X" when only attempted, not verified
2. **Evidence tier collapse**: "Deployment successful" from local test pass
3. **Scope drift**: Implementing follow-up discoveries without explicit user decision

## Blocked Path Acceptance

When a Discovery process results in a Blocked Report (user cannot articulate needs after facilitated exploration):

### Verified

- ✓ Attempted at least 2 rounds of open exploration
- ✓ Tried different angles (time perspective / problem vs goal / self vs others)
- ✓ Offered candidate anchors (if applicable) — specific, diverse, with rejection option
- ✓ Generated Blocked Report with:
  - What was explored
  - What is still unclear
  - Why cannot proceed
  - Suggested next steps (guided-thinking / try existing tools / consult experts)
- ✓ Applied correct certainty label with required evidence:
  - `确定不可行`: source + date + specific reason
  - `我不知道`: what info is needed + why it determines feasibility
  - `有条件可行`: conditions explicitly listed + switch cost stated

### Not Verified

- Future feasibility (may change with more information or context)
- User's eventual decision (they may gain clarity later through other means)
- Whether suggested next steps will actually resolve the blockage

### Remaining Risk

- User may still be unclear after following suggested next steps
- Handed-off skill (guided-thinking) may also reach a blocked state
- User may abandon the exploration entirely

### When NOT to Use Blocked Report

❌ **Do not use Blocked Report when:**
- You haven't tried 2 rounds of open exploration yet
- You haven't tried different angles
- One more clarifying question would likely resolve it
- User is describing their needs, just slowly or in non-linear fashion
