# Acceptance and Evidence Contract

## Evidence tiers

| Tier | Proves | Does not prove |
|---|---|---|
| Code / fixture | behavior in the repository snapshot | device or user acceptance |
| Build / release | an artifact was produced and checks passed | deployment success |
| Field | the authorized environment showed the observed result | every topology or long-term stability |
| Long-running | behavior remained stable over the stated window | unrelated environments |

Do not collapse these tiers into one “done” label.

## Required final report

Use the full report for normal, risky, multi-file, UI/runtime, build/release,
or field tasks. Trivial fast-path work may report briefly in the conversation
with the changed file, check result, and remaining uncertainty.

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

- the report exists at the requested external path;
- the required headings are present;
- `git diff --name-only` is inside the allowlist;
- `git status --short --untracked-files=all` has no unexpected artifacts;
- required validation commands have fresh output and exit status.

## Completion language

Use precise claims:

- “local tests pass” for repository checks;
- “build artifact produced” for build checks;
- “field observation recorded” for authorized runtime evidence;
- “not verified” for anything outside the executed evidence.

Do not write “works everywhere”, “all clients accepted”, “production-ready”, or
similar claims unless the stated evidence actually covers that scope.
