"""
Tests for topics/fundamentals/list_comprehensions_vs_loops.py

These tests check two things for each pair of functions:
  1. Each function individually produces the correct result.
  2. The loop version and the comprehension version agree with each
     other — proving they really are two ways of writing the same logic.
"""

from topics.fundamentals.list_comprehensions_vs_loops import (
    even_numbers_with_comprehension,
    even_numbers_with_loop,
    squares_with_comprehension,
    squares_with_loop,
)


def test_squares_with_loop():
    assert squares_with_loop([1, 2, 3]) == [1, 4, 9]


def test_squares_with_comprehension():
    assert squares_with_comprehension([1, 2, 3]) == [1, 4, 9]


def test_squares_loop_and_comprehension_agree():
    numbers = [-2, -1, 0, 1, 2, 10]
    assert squares_with_loop(numbers) == squares_with_comprehension(numbers)


def test_even_numbers_with_loop():
    assert even_numbers_with_loop([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_even_numbers_with_comprehension():
    assert even_numbers_with_comprehension([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_even_numbers_loop_and_comprehension_agree():
    numbers = list(range(-5, 6))
    assert even_numbers_with_loop(numbers) == even_numbers_with_comprehension(numbers)


def test_empty_input_returns_empty_list():
    assert squares_with_loop([]) == []
    assert squares_with_comprehension([]) == []
    assert even_numbers_with_loop([]) == []
    assert even_numbers_with_comprehension([]) == []
