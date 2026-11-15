# D-002 · Scope-Fehler im bestehenden PR

**15 Minuten.** Demo-Draft aus D-001 mit rotem `RelNotes tests`-Check.
Ersatzweise vorbereiteter Draft und lokale Referenzstände `m001` und `d002`.

- **0–4 Min.** Fehlenden Scope ohne Klammern im CI-Log identifizieren.
  Lokal `python -m pytest tests/test_parser.py -q -k scope` ausführen.
  Beobachtungsauftrag: Was belegt der rote Test über die Ursache?
- **4–10 Min.** Im vorhandenen Cursor-Lauf PR-Link und Head nennen.
  „Behebe nur BUG-1 im Parser. Scope ohne Klammern speichern.
  Vorher und nachher den Scope-Test, dann alle Tests ausführen.
  Bestehende Assertions erhalten. Nur den Head aktualisieren.“
- **10–15 Min.** Diff und neuen Commit prüfen. Der Zieltest ist grün.
  Die Gesamtsuite bleibt wegen BUG-2 und BUG-3 rot. Im PR den
  Unterschied zwischen neuem Lauf und ursprünglichem Befund zeigen.

**Übergabe.** Teams verwenden den Scope-Fix als ersten Schritt in L-002
und ergänzen beide offenen Korrekturen. Bei Ausfall Diffs und lokale Tests
der vorbereiteten Stände vergleichen und fehlende Actions-Evidenz markieren.
