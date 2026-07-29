"""
Tests for scripts/fundamentals/functions.py
"""

import scripts.fundamentals.functions as functions
from scripts.fundamentals.functions import connect, divide, read_data, remainder


def test_remainder():
    assert remainder(37, 15) == 7


def test_remainder_has_docstring_as_first_statement():
    # The docstring is the function's __doc__ attribute, not just a
    # comment -- it's introspectable at runtime.
    assert remainder.__doc__ is not None
    assert "truncating division" in remainder.__doc__


def test_divide_returns_quotient_and_remainder_tuple():
    result = divide(1456, 33)
    assert result == (44, 4)


def test_divide_result_can_be_unpacked():
    quotient, remainder_value = divide(1456, 33)
    assert quotient == 44
    assert remainder_value == 4


def test_connect_uses_default_timeout_when_omitted():
    assert connect("www.python.org", 80) == {
        "hostname": "www.python.org",
        "port": 80,
        "timeout": 300,
    }


def test_connect_overrides_default_timeout_when_given():
    assert connect("www.python.org", 80, 60) == {
        "hostname": "www.python.org",
        "port": 80,
        "timeout": 60,
    }


def test_connect_accepts_keyword_arguments_in_any_order():
    by_position = connect("www.python.org", 80)
    by_keyword = connect(port=80, hostname="www.python.org")
    assert by_keyword == by_position


def test_read_data_prints_when_debug_is_on(monkeypatch, capsys):
    monkeypatch.setattr(functions, "debug", True)

    result = read_data("data.csv")

    assert result == "data.csv"
    captured = capsys.readouterr()
    assert "Reading" in captured.out
    assert "data.csv" in captured.out


def test_read_data_silent_when_debug_is_off(monkeypatch, capsys):
    monkeypatch.setattr(functions, "debug", False)

    result = read_data("data.csv")

    assert result == "data.csv"
    captured = capsys.readouterr()
    assert captured.out == ""
