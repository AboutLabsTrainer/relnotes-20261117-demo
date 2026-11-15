# D-003 · Cloud-PR für den Typfilter und unabhängiges Review

**15 Minuten.** Separates Demo-Repo auf grünem `m002`. ISSUE-01 (`--types`)
und ein zweiter, unabhängiger GitHub-Account sind vorbereitet. Live-PR als
Ersatz vorab bereitstellen.

- **0–4 Min.** Issue und Abnahmetest für einen unbekannten Typ lesen.
  „Implementiere [Issue-Link] auf einem Arbeitsbranch. Aktiviere nur den
  ISSUE-01-Test, führe pytest aus und öffne einen PR gegen main. Kein Merge.“
  Cloud-Lauf starten und Basisbranch zeigen.
- **4–10 Min.** PR-Head, **Files changed** und **Checks** öffnen. Einen
  Randfall mit `--types` am PR-Stand nachstellen. Optional einen
  vorhandenen Bugbot-Hinweis prüfen. Autofix bleibt aus.
- **10–15 Min.** Reviewer zeigt einen Kommentar mit Anforderung, Stelle,
  Nachweis und gewünschtem Ergebnis. Bei korrekter Umsetzung den echten
  PR freigeben und für die Korrekturschleife den vorbereiteten SemVer-Diff
  `m003-review` verwenden. Dessen isolierter `perf`-Fall scheitert trotz
  grüner vorhandener Suite. Follow-up für denselben Head zeigen.

**Fallback.** Nach fünf Minuten ohne Fortschritt zum vorgeprüften PR oder
zu lokalen Diffs wechseln. Review und Repro beibehalten.
