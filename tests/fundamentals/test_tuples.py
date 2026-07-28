"""
Tests for scripts/fundamentals/tuples.py
"""

from scripts.fundamentals.tuples import (
    attempt_to_mutate_holding,
    create_empty_tuple,
    create_holding,
    create_one_element_tuple,
    field_from_row,
    first_row,
    load_portfolio_from_file,
    load_portfolio_from_lines,
    parse_portfolio_line,
    total_value_with_comprehension,
    total_value_with_loop,
    unpack_holding,
)


def test_create_holding():
    assert create_holding() == ("GOOG", 100, 490.10)


def test_create_empty_tuple():
    assert create_empty_tuple() == ()


def test_create_one_element_tuple():
    result = create_one_element_tuple("GOOG")
    assert result == ("GOOG",)
    # A single value in bare parentheses is not a tuple -- only the
    # trailing comma makes it one.
    assert result != "GOOG"


def test_unpack_holding():
    holding = create_holding()
    assert unpack_holding(holding) == ("GOOG", 100, 490.10)


def test_attempt_to_mutate_holding_raises_type_error():
    holding = create_holding()
    error = attempt_to_mutate_holding(holding)
    assert isinstance(error, TypeError)
    # The tuple itself is untouched by the failed mutation attempt.
    assert holding == ("GOOG", 100, 490.10)


def test_parse_portfolio_line():
    assert parse_portfolio_line("GOOG, 100, 490.10") == ("GOOG", 100, 490.10)


def test_load_portfolio_from_lines():
    lines = ["GOOG, 100, 490.10", "AAPL, 50, 91.10"]
    assert load_portfolio_from_lines(lines) == [
        ("GOOG", 100, 490.10),
        ("AAPL", 50, 91.10),
    ]


def test_load_portfolio_from_file(tmp_path):
    portfolio_path = tmp_path / "portfolio.csv"
    portfolio_path.write_text("GOOG, 100, 490.10\nAAPL, 50, 91.10\n")

    assert load_portfolio_from_file(portfolio_path) == [
        ("GOOG", 100, 490.10),
        ("AAPL", 50, 91.10),
    ]


def test_first_row():
    portfolio = load_portfolio_from_lines(["GOOG, 100, 490.10", "AAPL, 50, 91.10"])
    assert first_row(portfolio) == ("GOOG", 100, 490.10)


def test_field_from_row():
    portfolio = load_portfolio_from_lines(["GOOG, 100, 490.10", "AAPL, 50, 91.10"])
    assert field_from_row(portfolio, 1, 1) == 50


def test_total_value_with_loop():
    portfolio = [("GOOG", 100, 490.10), ("AAPL", 50, 91.10)]
    expected = 100 * 490.10 + 50 * 91.10
    assert total_value_with_loop(portfolio) == expected


def test_total_value_with_comprehension_matches_loop():
    portfolio = [("GOOG", 100, 490.10), ("AAPL", 50, 91.10)]
    assert total_value_with_comprehension(portfolio) == total_value_with_loop(portfolio)
