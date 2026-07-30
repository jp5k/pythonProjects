import pytest

from scripts.command_line_arguments.interactive_or_argv_input import (
    main,
    read_portfolio,
)


def test_read_portfolio_parses_csv_lines(tmp_path):
    portfolio_file = tmp_path / "portfolio.csv"
    portfolio_file.write_text("GOOG,100,490.10\nAAPL,50,91.10\n")

    assert read_portfolio(portfolio_file) == [
        ("GOOG", 100, 490.10),
        ("AAPL", 50, 91.10),
    ]


def test_main_reads_filename_from_argv(tmp_path, capsys):
    portfolio_file = tmp_path / "portfolio.csv"
    portfolio_file.write_text("GOOG,100,490.10\n")

    main(["prog.py", str(portfolio_file)])

    out = capsys.readouterr().out
    assert "GOOG" in out
    assert "490.10" in out


def test_main_prompts_interactively_when_no_extra_argv(tmp_path, monkeypatch, capsys):
    portfolio_file = tmp_path / "portfolio.csv"
    portfolio_file.write_text("AAPL,50,91.10\n")

    # monkeypatch swaps out the built-in input() for the duration of
    # this test, so it returns the temp file's path instead of actually
    # blocking to wait for a real keypress.
    monkeypatch.setattr("builtins.input", lambda prompt="": str(portfolio_file))

    main(["prog.py"])

    out = capsys.readouterr().out
    assert "AAPL" in out


def test_main_raises_usage_error_with_too_many_args():
    with pytest.raises(SystemExit, match=r"Usage: prog\.py \[filename\]"):
        main(["prog.py", "a", "b"])
