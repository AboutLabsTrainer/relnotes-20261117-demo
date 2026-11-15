# D-001 · Erster Cloud-PR mit der Versionsabfrage

**15 Minuten.** Separates RelNotes-Demo-Repo auf Starter-Basis. Issue
„Versionsausgabe ohne Eingabedatei“ und vorbereiteten Draft bereithalten.

- **0–4 Min.** Lokal `relnotes --version` ausführen und fehlende Option
  zeigen. Kriterien: Versionszeile, Exit-Code 0, keine Eingabedatei nötig.
  Erklären, welche Dateien der lokale Agent lesen kann.
- **4–9 Min.** In Cursor Web Repo und `main` wählen. „Setze [Issue-Link] auf
  einem Arbeitsbranch um. Ergänze die Versionsoption mit einem CLI-Test.
  Führe pytest aus und öffne einen PR gegen main. Bekannte Parserfehler
  dokumentieren. Kein Merge.“ Plan, VM-Umgebung und Testausgabe zeigen.
- **9–15 Min.** PR-Head, Diff und CLI-Nachweis abgleichen. Ein roter
  Actions-Check aus dem Starter ist erwartbar. Draft offen lassen. Fragen,
  welcher Nachweis die CLI-Änderung belegt und welcher den Merge blockiert.

**Fallback.** Nach fünf Minuten ohne verwertbaren Lauf zum vorbereiteten
Draft wechseln. Ohne GitHub den lokalen Diff Starter → `m001` auf
`--version` filtern und die Gegenprobe vorführen. `m001` enthält zusätzlich
die Quiet-Referenz und wird separat vom Live-Demo-Branch gehalten.
