"""Versionsvorschlag nach Semantic Versioning (Referenzloesung ISSUE-02)."""

from __future__ import annotations

from relnotes.parser import Commit


def suggest_version(current: str, commits: list[Commit]) -> str:
    major, minor, patch = (int(part) for part in current.split("."))
    if any(commit.breaking for commit in commits):
        return f"{major + 1}.0.0"
    if any(commit.type == "feat" for commit in commits):
        return f"{major}.{minor + 1}.0"
    if any(commit.type in ("fix", "perf") for commit in commits):
        return f"{major}.{minor}.{patch + 1}"
    return current
