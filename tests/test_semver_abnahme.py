"""Randfälle zu ISSUE-02; getrennt vom Teilnehmer-Starter."""
import pytest
from relnotes.parser import Commit
from relnotes.semver import suggest_version


def commit(kind, breaking=False):
    return Commit("abc", "Anna", kind, None, "Beispiel", breaking)


def test_leere_eingabe_aendert_version_nicht():
    assert suggest_version("2.3.1", []) == "2.3.1"


@pytest.mark.parametrize("reverse", [False, True])
def test_breaking_hat_vorrang_unabhaengig_von_reihenfolge(reverse):
    commits = [commit("feat"), commit("fix", True), commit("perf")]
    assert suggest_version("2.3.1", commits[::-1] if reverse else commits) == "3.0.0"


def test_kursregel_fuer_nullversion():
    assert suggest_version("0.1.0", [commit("feat", True)]) == "1.0.0"


def test_perf_allein_erhoeht_patch():
    assert suggest_version("2.3.1", [commit("perf")]) == "2.3.2"
