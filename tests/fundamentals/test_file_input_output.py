"""
Tests for scripts/fundamentals/file_input_output.py
"""

import pytest

from scripts.fundamentals.file_input_output import (
    read_console_input,
    read_in_chunks,
    read_line_by_line,
    read_with_encoding,
    write_compound_interest_with_print,
    write_compound_interest_with_write,
)


def test_read_line_by_line_keeps_trailing_newlines(tmp_path):
    data_path = tmp_path / "data.txt"
    data_path.write_text("first line\nsecond line\nthird line\n")

    assert read_line_by_line(data_path) == [
        "first line\n",
        "second line\n",
        "third line\n",
    ]


def test_read_in_chunks_reassembles_to_full_contents(tmp_path):
    data_path = tmp_path / "data.txt"
    data_path.write_text("abcdefghijklmnopqrstuvwxyz")

    chunks = read_in_chunks(data_path, chunk_size=10)

    assert len(chunks) == 3
    assert "".join(chunks) == "abcdefghijklmnopqrstuvwxyz"


def test_write_compound_interest_with_print(tmp_path):
    out_path = tmp_path / "out.txt"

    final_principal = write_compound_interest_with_print(
        out_path, principal=1000.0, rate=0.05, numyears=3
    )

    lines = out_path.read_text().splitlines()
    assert len(lines) == 3
    assert lines[0] == "  1 1050.00"
    # Compounding year by year (repeated multiplication) accumulates a
    # tiny floating-point rounding difference versus computing 1.05**3
    # in one step, so compare with a tolerance rather than exact ==.
    assert final_principal == pytest.approx(1000.0 * 1.05**3)


def test_write_compound_interest_with_write_matches_print_version(tmp_path):
    print_path = tmp_path / "print_out.txt"
    write_path = tmp_path / "write_out.txt"

    write_compound_interest_with_print(
        print_path, principal=500.0, rate=0.1, numyears=4
    )
    write_compound_interest_with_write(
        write_path, principal=500.0, rate=0.1, numyears=4
    )

    # Both functions build the same table; write() just needs an
    # explicit "\n" added, which the assertion here confirms lines up
    # with what print(file=...) produced automatically.
    assert write_path.read_text() == print_path.read_text()


def test_read_with_encoding(tmp_path):
    encoded_path = tmp_path / "encoded.txt"
    encoded_path.write_text("café ☃", encoding="utf-8")

    assert read_with_encoding(encoded_path, encoding="utf-8") == "café ☃"


def test_read_console_input_returns_typed_line(monkeypatch):
    # monkeypatch swaps out the built-in input() for the duration of
    # this test, so it returns a fixed string instead of actually
    # blocking to wait for a real keypress.
    monkeypatch.setattr("builtins.input", lambda prompt="": "hello from the console")

    assert read_console_input("Type something: ") == "hello from the console"
