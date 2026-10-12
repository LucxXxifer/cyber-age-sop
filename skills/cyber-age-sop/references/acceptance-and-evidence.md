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
