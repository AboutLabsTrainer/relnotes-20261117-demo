"""Zusätzliche Abnahme für L-001; nur im Trainer-/Referenzstand."""
import pytest
from relnotes.cli import main


@pytest.mark.parametrize("flag", ["--quiet", "-q"])
@pytest.mark.parametrize("to_file", [False, True])
def test_quiet_erhaelt_nutzdaten_und_standardverhalten(tmp_path, capsys, flag, to_file):
    src = tmp_path / "commits.txt"
    src.write_text("abc123|Anna|feat: Export ergänzen\n", encoding="utf-8")
    output = tmp_path / "notes.md"
    args = ["-i", str(src)] + (["-o", str(output)] if to_file else [])
    assert main(args) == 0
    normal = capsys.readouterr()
    content = output.read_text(encoding="utf-8") if to_file else normal.out
    assert "Export ergänzen" in content
    assert "Commits verarbeitet" in normal.err
    assert main(args + [flag]) == 0
    quiet = capsys.readouterr()
    assert quiet.err == ""
    assert quiet.out == normal.out
    assert (output.read_text(encoding="utf-8") if to_file else quiet.out) == content


def test_version_ohne_input(capsys):
    with pytest.raises(SystemExit) as exc:
        main(["--version"])
    assert exc.value.code == 0
    assert "0.1.0" in capsys.readouterr().out
