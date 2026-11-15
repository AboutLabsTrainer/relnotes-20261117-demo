"""Conventional-Commits-Parser fuer RelNotes (Referenzloesung)."""

from __future__ import annotations

import re
from dataclasses import dataclass

KNOWN_TYPES = {"feat", "fix", "perf", "refactor", "docs", "test", "build", "ci", "chore"}

# FIX BUG-1: scope-Gruppe liegt INNERHALB der Klammern
# FIX BUG-3: [A-Za-z] statt [a-z], Typ wird spaeter normalisiert
HEADER_RE = re.compile(
    r"^(?P<type>[A-Za-z]+)"
    r"(?:\((?P<scope>[^)]+)\))?"
    r"(?P<bang>!)?"
    r":\s+(?P<desc>.+)$"
)


@dataclass
class Commit:
    hash: str
    author: str
    type: str
    scope: str | None
    description: str
    breaking: bool = False


def parse_line(line: str) -> Commit | None:
    parts = line.split("|", 2)
    if len(parts) != 3:
        return None
    sha, author, subject = parts
    subject = subject.strip()  # FIX BUG-3: Whitespace tolerieren

    match = HEADER_RE.match(subject)
    if not match:
        return None

    ctype = match.group("type").lower()  # FIX BUG-3: Typ normalisieren
    if ctype not in KNOWN_TYPES:
        return None

    # FIX BUG-2: "!" markiert einen Breaking Change
    breaking = bool(match.group("bang")) or "BREAKING CHANGE" in subject

    return Commit(
        hash=sha.strip(),
        author=author.strip(),
        type=ctype,
        scope=match.group("scope"),
        description=match.group("desc").strip(),
        breaking=breaking,
    )


def parse_lines(text: str) -> list[Commit]:
    commits: list[Commit] = []
    for line in text.splitlines():
        if not line.strip():
            continue
        commit = parse_line(line)
        if commit is not None:
            commits.append(commit)
    return commits
