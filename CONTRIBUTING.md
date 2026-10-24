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
python3 scripts/validate_implementation_readiness.py
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

## Beta Feedback / 測試版回饋

For real-use feedback, use the [bilingual guide](docs/beta-feedback.md) or the
beta feedback issue template. A useful report identifies the Skill version,
Agent/IDE, model/effort, intended outcome, confusing or incorrect excerpt,
and observed result. Redact private data before posting. Feedback is voluntary;
the Skill does not collect or upload transcripts automatically.

實際試用請記錄版本、Agent／IDE、模型與推理設定、想完成的事、問題原句及實際結果。
無需提供技術診斷；回饋前移除個資、憑證與公司資料。沒有自動收集或上傳對話。
