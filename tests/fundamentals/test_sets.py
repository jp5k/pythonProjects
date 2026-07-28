"""
Tests for scripts/fundamentals/sets.py
"""

import pytest

from scripts.fundamentals.sets import (
    add_multiple_items,
    add_single_item,
    create_empty_set,
    create_set_constructor,
    create_set_literal,
    discard_item,
    remove_existing_item,
    set_difference,
    set_intersection,
    set_symmetric_difference,
    set_union,
    stock_names_from_portfolio,
)


def test_create_set_literal_drops_duplicates():
    result = create_set_literal()
    assert result == {"IBM", "MSFT", "AA"}
    assert len(result) == 3


def test_create_set_constructor_drops_duplicates():
    result = create_set_constructor()
    assert result == {"IBM", "MSFT", "HPE", "CAT"}
    assert len(result) == 4


def test_create_empty_set():
    result = create_empty_set()
    assert result == set()
    assert isinstance(result, set)


def test_stock_names_from_portfolio_folds_duplicates():
    portfolio = [
        ("GOOG", 100, 490.10),
        ("AAPL", 50, 91.10),
        ("GOOG", 25, 490.10),
    ]
    assert stock_names_from_portfolio(portfolio) == {"GOOG", "AAPL"}


def test_set_union():
    t = {"IBM", "MSFT", "AA"}
    s = {"IBM", "MSFT", "HPE", "CAT"}
    assert set_union(t, s) == {"IBM", "MSFT", "AA", "HPE", "CAT"}


def test_set_intersection():
    t = {"IBM", "MSFT", "AA"}
    s = {"IBM", "MSFT", "HPE", "CAT"}
    assert set_intersection(t, s) == {"IBM", "MSFT"}


def test_set_difference_is_not_symmetric():
    t = {"IBM", "MSFT", "AA"}
    s = {"IBM", "MSFT", "HPE", "CAT"}
    assert set_difference(t, s) == {"AA"}
    assert set_difference(s, t) == {"HPE", "CAT"}


def test_set_symmetric_difference():
    t = {"IBM", "MSFT", "AA"}
    s = {"IBM", "MSFT", "HPE", "CAT"}
    assert set_symmetric_difference(t, s) == {"AA", "HPE", "CAT"}


def test_add_single_item():
    names = {"IBM", "MSFT"}
    result = add_single_item(names, "DIS")
    assert result == {"IBM", "MSFT", "DIS"}
    # add() mutates the set in place rather than returning a new one.
    assert result is names


def test_add_single_item_is_noop_for_existing_item():
    names = {"IBM", "MSFT"}
    add_single_item(names, "IBM")
    assert names == {"IBM", "MSFT"}


def test_add_multiple_items():
    names = {"IBM"}
    result = add_multiple_items(names, {"JJ", "GE", "ACME"})
    assert result == {"IBM", "JJ", "GE", "ACME"}
    assert result is names


def test_remove_existing_item():
    names = {"IBM", "MSFT"}
    result = remove_existing_item(names, "IBM")
    assert result == {"MSFT"}
    assert result is names


def test_remove_missing_item_raises_key_error():
    names = {"IBM", "MSFT"}
    with pytest.raises(KeyError):
        remove_existing_item(names, "SCOX")
    # A failed remove() leaves the set untouched.
    assert names == {"IBM", "MSFT"}


def test_discard_existing_item():
    names = {"IBM", "MSFT"}
    result = discard_item(names, "IBM")
    assert result == {"MSFT"}
    assert result is names


def test_discard_missing_item_is_silent():
    names = {"IBM", "MSFT"}
    result = discard_item(names, "SCOX")
    # Unlike remove(), discard() raises nothing when the item is absent.
    assert result == {"IBM", "MSFT"}
