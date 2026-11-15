# D-004 · CI-Nachweis, Freigabe und Release-Stand

**15 Minuten.** Drei vorbereitete Check-Ansichten (grün, rot, grün) zu einem
Trainings-PR auf dem SemVer-Stand. Für die optionale Tag-Demo ein separates
Wegwerf-Repo mit geprüftem Integrationsstand verwenden.

- **0–5 Min.** Drei Head-SHAs und die jeweiligen Actions-Läufe zeigen.
  Im roten Lauf den isolierten Fehler in `tests/test_ci_probe.py` öffnen.
  Merge-Anzeige mit normaler Rolle und die konfigurierten Regeln vergleichen.
- **5–10 Min.** Engen Cloud-Folgeauftrag zum Entfernen der Probe zeigen.
  Im korrigierten Diff bestätigen, dass produktive Tests und Workflow
  unverändert sind. Erneutes menschliches Review und Entscheidung zeigen.
- **10–15 Min.** `release.yml` öffnen. Tag-Trigger, Tag-Stand-Test,
  Commit-Auswahl und Schreibrecht für die Veröffentlichung einordnen.
  Optional einen vorgeprüften Sandbox-Tag auslösen. Falls zeitlich knapp,
  `relnotes --input sample-data/commits.txt` lokal demonstrieren und die
  Veröffentlichung als ausstehend kennzeichnen.
