"""
Tests for scripts/fundamentals/operators_and_formatted_output.py
"""

from scripts.fundamentals.operators_and_formatted_output import (
    count_up_with_walrus,
    floor_divide,
)


def test_floor_divide_exact():
    assert floor_divide(6, 2) == 3


def test_floor_divide_truncates_down():
    assert floor_divide(7, 2) == 3


def test_floor_divide_negative_rounds_toward_negative_infinity():
    # Floor division rounds down, not toward zero, so -7 // 2 is -4, not -3.
    assert floor_divide(-7, 2) == -4


def test_count_up_with_walrus_stops_below_limit():
    assert count_up_with_walrus(10) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_count_up_with_walrus_limit_one_returns_empty():
    # x starts at 0 and is incremented to 1 before the check, so a limit
    # of 1 fails the condition (1 < 1 is False) on the very first pass.
    assert count_up_with_walrus(1) == []
