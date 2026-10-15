#!/usr/bin/env python3
"""Check the implementation-readiness contract introduced in v0.4.5."""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    skill = root / "skills/cyber-age-sop/SKILL.md"
    readiness = root / "skills/cyber-age-sop/references/implementation-readiness.md"
    regression = root / "skills/cyber-age-sop/references/regression-cases.md"

    required_files = (skill, readiness, regression)
    missing = [str(path.relative_to(root)) for path in required_files if not path.exists()]
    if missing:
        print("MISSING: " + ", ".join(missing))
        return 1

    skill_text = skill.read_text(encoding="utf-8")
    readiness_text = readiness.read_text(encoding="utf-8")
    regression_text = regression.read_text(encoding="utf-8")

    skill_markers = (
        "**A Decision Brief is not an implementation contract.**",
        "**建議不等於使用者已決定。**",
        "decision-ready",
        "discovery-ready",
        "prototype-ready",
        "build-ready",
        "field-ready",
        "決策狀態",
        "implementation-readiness.md",
        "do not invent endpoints",
    )
    readiness_markers = (
        "## Readiness Matrix",
        "## Integration Contract",
        "## Discovery-Only Handoff",
        "## Build-Ready Agent Brief",
        "System of record",
        "Identity",
        "Permissions",
        "Interface",
        "Normal and failure behavior",
    )
    regression_markers = (
        "Multi-stage platform integration",
        "v0.4.5 Implementation-Readiness Acceptance",
        "discovery task",
        "build-ready",
        "source-quality labels agree",
    )

    errors: list[str] = []
    for marker in skill_markers:
        if marker not in skill_text:
            errors.append(f"SKILL.md missing marker: {marker}")
    for marker in readiness_markers:
        if marker not in readiness_text:
            errors.append(f"implementation-readiness.md missing marker: {marker}")
    for marker in regression_markers:
        if marker not in regression_text:
            errors.append(f"regression-cases.md missing marker: {marker}")

    if errors:
        print("\n".join(errors))
        return 1

    print("implementation-readiness contract valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
