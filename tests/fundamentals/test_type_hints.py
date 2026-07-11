"""
Tests for scripts/fundamentals/type_hints.py

These tests check the runtime *behavior* of the hinted functions. They
don't (and can't) verify the hints themselves — Python doesn't enforce
type hints at runtime, so that's a static type checker's job (mypy,
pyright), not pytest's.
"""

from scripts.fundamentals.type_hints import (
    add,
    add_no_hints,
    add_wrong_but_still_runs,
    average,
    find_first_even,
    greet,
)


def test_add():
    assert add(2, 3) == 5


def test_add_no_hints_matches_add():
    assert add_no_hints(2, 3) == add(2, 3)


def test_greet():
    assert greet("Ada") == "Hello, Ada!"


def test_average():
    assert average([1.0, 2.0, 3.0]) == 2.0


def test_find_first_even_found():
    assert find_first_even([1, 3, 4, 5]) == 4


def test_find_first_even_not_found():
    assert find_first_even([1, 3, 5]) is None


def test_add_wrong_but_still_runs_violates_its_own_hint():
    # Demonstrates that Python happily runs this despite the "-> int" hint
    # promising an int — the actual return value is a str.
    result = add_wrong_but_still_runs(2, 3)
    assert isinstance(result, str)
    assert result == "2 and 3"
