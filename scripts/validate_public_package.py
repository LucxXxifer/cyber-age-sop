#!/usr/bin/env python3
"""Validate the public Cyber-Age SOP package with only the standard library."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = sorted(ROOT.rglob("*.md"))
TEXT_FILES = sorted(
    path
    for path in ROOT.rglob("*")
    if path.is_file() and ".git" not in path.parts
)

ERRORS: list[str] = []


def check_frontmatter(path: Path, text: str) -> None:
    if not text.startswith("---\n"):
        return
    end = text.find("\n---\n", 4)
    if end < 0:
        ERRORS.append(f"{path.relative_to(ROOT)}: unclosed frontmatter")
        return
    frontmatter = text[4:end]
    if path.name == "SKILL.md":
        for key in ("name:", "description:"):
            if key not in frontmatter:
                ERRORS.append(f"{path.relative_to(ROOT)}: missing {key}")


def check_markdown(path: Path, text: str) -> None:
    fences = len(re.findall(r"^```", text, flags=re.MULTILINE))
    if fences % 2:
        ERRORS.append(f"{path.relative_to(ROOT)}: unbalanced code fences")

    forbidden = (
        r"/Users/",
        r"/Volumes/",
        r"/private/tmp/",
        r"BEGIN (?:RSA|OPENSSH|EC|PGP) PRIVATE KEY",
        r"(?i)(?:password|passwd|secret|api[_-]?key|token|cookie)\s*[:=]\s*\S+",
    )
    for pattern in forbidden:
        if re.search(pattern, text):
            ERRORS.append(
                f"{path.relative_to(ROOT)}: possible private material matches {pattern}"
            )


def check_wiki_links(path: Path, text: str) -> None:
    by_basename = {candidate.stem: candidate for candidate in MARKDOWN}
    for match in re.finditer(r"\[\[([^\]]+)\]\]", text):
        target = match.group(1).split("|", 1)[0].split("#", 1)[0]
        if "/" in target:
            candidates = [
                ROOT / target,
                ROOT / f"{target}.md",
                path.parent / target,
                path.parent / f"{target}.md",
            ]
            if not any(candidate.exists() for candidate in candidates):
                ERRORS.append(
                    f"{path.relative_to(ROOT)}: unresolved wiki link {target}"
                )
        elif target not in by_basename:
            ERRORS.append(
                f"{path.relative_to(ROOT)}: unresolved wiki link {target}"
            )


def main() -> int:
    required = (
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "skills/cyber-age-sop/SKILL.md",
        ROOT / "skills/cyber-age-sop/agents/openai.yaml",
        ROOT / "project-sop/cyber-age-project-sop类型定义.md",
        ROOT / "project-sop/cyber-age-project-sop完整鏈路.md",
    )
    for path in required:
        if not path.exists():
            ERRORS.append(f"missing required file: {path.relative_to(ROOT)}")

    for path in MARKDOWN:
        text = path.read_text(encoding="utf-8")
        check_frontmatter(path, text)
        check_markdown(path, text)
        check_wiki_links(path, text)

    if ERRORS:
        print("\n".join(f"ERROR: {error}" for error in ERRORS))
        return 1

    print(
        f"validated {len(MARKDOWN)} Markdown files and "
        f"{len(TEXT_FILES)} text/package files"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
