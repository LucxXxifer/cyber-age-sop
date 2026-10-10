# Contributing

## Before Opening a Pull Request

- Read `skills/cyber-age-sop/SKILL.md`.
- Read the relevant task profile and evidence contract.
- Keep the change within a clear scope.
- Add or update a regression case when behavior or a safety boundary changes.
- Do not include private transcripts, credentials, cookies, device identifiers,
  local filesystem paths, or field logs.

## Required Checks

Run:

```bash
python3 scripts/validate_public_package.py
```

The GitHub Actions workflow runs the same validation and creates a source
archive on successful pushes.

## Pull Request Description

Describe:

- what changed;
- why it changed;
- which files are in scope;
- what was verified;
- what was not verified;
- any remaining risk;
- whether the SOP or evidence contract changed.

Do not describe local tests as field acceptance or a release artifact as
deployment success.
