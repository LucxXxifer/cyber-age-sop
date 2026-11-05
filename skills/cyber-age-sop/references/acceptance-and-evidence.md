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

In conversation, state the actual result, checks and material limitation directly. Do not require opening an attachment or repeating empty audit headings. Keep the existing project record current when the task needs persistence.

Use the structured audit below for consequential multi-part delivery, build/release, field work or a contract that requires it. These headings are an audit template, not a required layout for every response:

```markdown
## Changed
## Verified
## Not verified
## Remaining risk
## Follow-up discoveries
## SOP feedback
```

Follow the [storage policy](lifecycle-traceability.md#storage-policy): preserve the approved location; raw/sensitive/temporary evidence stays outside the repository. The audit should independently check:

- The report exists at the approved path and can actually be read
- Applicable scope, checks, limits and remaining decisions are present
- `git diff --name-only` is inside the allowlist
- `git status --short --untracked-files=all` has no unexpected artifacts
- Required validation commands have fresh output and exit status

For versioned or changed work, each completion claim must identify the applicable SPEC, the exact tested source snapshot, and the relevant evidence. An unchanged filename or base HEAD does not identify dirty/untracked contents. Keep historical results; mark affected evidence insufficient for the new revision and rerun the relevant checks before dependent work. Record who actually checked the result; the implementer's self-report is not independent acceptance. A low-risk contract may authorize deterministic implementer self-checks; preserve their identity and do not label them human product acceptance.

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

- ✓ Tried useful open exploration without imposing a fixed round count
- ✓ Tried different angles (time perspective / problem vs goal / self vs others)
- ✓ Offered candidate anchors (if applicable) — specific, diverse, with rejection option
- ✓ Generated Blocked Report with:
  - What was explored
  - What is still unclear
  - Why cannot proceed
  - Suggested next steps (concrete example or sketch / try existing tools / consult experts; another Skill only if requested)
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
- Another exploration route may also leave key facts unknown
- User may abandon the exploration entirely

### When NOT to Use Blocked Report

❌ **Do not use Blocked Report when:**

- A fixed number of rounds is the only reason to stop or continue
- You haven't tried different angles
- One more clarifying question would likely resolve it
- User is describing their needs, just slowly or in non-linear fashion
