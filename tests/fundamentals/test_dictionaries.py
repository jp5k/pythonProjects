"""
Tests for scripts/fundamentals/dictionaries.py
"""

from collections import Counter

import pytest

from scripts.fundamentals.dictionaries import (
    add_date,
    create_dict_from_pairs,
    create_empty_dict_constructor,
    create_empty_dict_literal,
    create_stock_dict,
    format_price_lines,
    get_cost,
    get_name,
    has_symbol,
    keys_as_list,
    keys_view,
    price_lookup,
    price_lookup_with_default,
    record_price_by_date,
    remove_symbol,
    total_shares_by_counter,
    total_shares_by_dict_comprehension,
    update_shares,
    values_view,
)


def test_create_stock_dict():
    result = create_stock_dict()
    assert result == {"name": "GOOG", "shares": 100, "price": 490.10}


def test_get_name():
    s = {"name": "GOOG", "shares": 100, "price": 490.10}
    assert get_name(s) == "GOOG"


def test_get_cost():
    s = {"name": "GOOG", "shares": 100, "price": 490.10}
    assert get_cost(s) == 49010.0


def test_update_shares_modifies_existing_key():
    s = {"name": "GOOG", "shares": 100, "price": 490.10}
    result = update_shares(s, 75)
    assert result["shares"] == 75
    # update_shares() mutates the dict in place rather than returning a new one.
    assert result is s


def test_add_date_inserts_new_key():
    s = {"name": "GOOG", "shares": 100, "price": 490.10}
    result = add_date(s, "2007-06-07")
    assert result["date"] == "2007-06-07"
    assert result is s


def test_price_lookup():
    prices = {"GOOG": 490.10, "IBM": 91.23}
    assert price_lookup(prices, "IBM") == 91.23


def test_price_lookup_missing_key_raises_key_error():
    prices = {"GOOG": 490.10}
    with pytest.raises(KeyError):
        price_lookup(prices, "IBM")


def test_has_symbol_true_for_present_key():
    prices = {"GOOG": 490.10, "IBM": 91.23}
    assert has_symbol(prices, "IBM") is True


def test_has_symbol_false_for_absent_key():
    prices = {"GOOG": 490.10}
    assert has_symbol(prices, "AAPL") is False


def test_price_lookup_with_default_returns_value_when_present():
    prices = {"IBM": 91.23}
    assert price_lookup_with_default(prices, "IBM") == 91.23


def test_price_lookup_with_default_returns_default_when_absent():
    prices = {"IBM": 91.23}
    assert price_lookup_with_default(prices, "AAPL") == 0.0


def test_price_lookup_with_default_custom_default():
    prices = {"IBM": 91.23}
    assert price_lookup_with_default(prices, "AAPL", default=-1) == -1


def test_remove_symbol():
    prices = {"GOOG": 490.10, "IBM": 91.23}
    result = remove_symbol(prices, "GOOG")
    assert result == {"IBM": 91.23}
    assert result is prices


def test_remove_missing_symbol_raises_key_error():
    prices = {"IBM": 91.23}
    with pytest.raises(KeyError):
        remove_symbol(prices, "GOOG")
    # A failed del leaves the dict untouched.
    assert prices == {"IBM": 91.23}


def test_record_price_by_date_uses_composite_key():
    prices = {}
    record_price_by_date(prices, "IBM", "2015-02-03", 91.23)
    record_price_by_date(prices, "IBM", "2015-02-04", 91.42)
    assert prices == {
        ("IBM", "2015-02-03"): 91.23,
        ("IBM", "2015-02-04"): 91.42,
    }


def test_record_price_by_date_returns_same_dict():
    prices = {}
    result = record_price_by_date(prices, "IBM", "2015-02-03", 91.23)
    assert result is prices


PORTFOLIO = [
    ("ACME", 50, 92.34),
    ("IBM", 75, 102.25),
    ("PHP", 40, 74.50),
    ("IBM", 50, 124.75),
]


def test_total_shares_by_dict_comprehension_sums_repeated_names():
    result = total_shares_by_dict_comprehension(PORTFOLIO)
    assert result == {"ACME": 50, "IBM": 125, "PHP": 40}


def test_total_shares_by_dict_comprehension_returns_plain_dict():
    result = total_shares_by_dict_comprehension(PORTFOLIO)
    assert isinstance(result, dict)
    assert not isinstance(result, Counter)


def test_total_shares_by_counter_sums_repeated_names():
    result = total_shares_by_counter(PORTFOLIO)
    assert result == Counter({"ACME": 50, "IBM": 125, "PHP": 40})


def test_total_shares_by_counter_returns_counter():
    result = total_shares_by_counter(PORTFOLIO)
    assert isinstance(result, Counter)


def test_total_shares_by_counter_missing_key_defaults_to_zero():
    result = total_shares_by_counter(PORTFOLIO)
    assert result["NOPE"] == 0


def test_create_empty_dict_literal():
    result = create_empty_dict_literal()
    assert result == {}
    assert isinstance(result, dict)


def test_create_empty_dict_constructor():
    result = create_empty_dict_constructor()
    assert result == {}
    assert isinstance(result, dict)


def test_create_dict_from_pairs():
    pairs = [("IBM", 125), ("ACME", 50), ("PHP", 40)]
    assert create_dict_from_pairs(pairs) == {"IBM": 125, "ACME": 50, "PHP": 40}


def test_keys_as_list_returns_plain_list_snapshot():
    prices = {"AAPL": 645.57, "IBM": 91.23}
    result = keys_as_list(prices)
    assert result == ["AAPL", "IBM"]
    assert isinstance(result, list)

    # A snapshot list doesn't change when the source dict changes afterward.
    prices["GOOG"] = 490.10
    assert result == ["AAPL", "IBM"]


def test_keys_view_reflects_later_changes_to_the_dict():
    prices = {"AAPL": 645.57, "IBM": 91.23}
    view = keys_view(prices)
    assert list(view) == ["AAPL", "IBM"]

    # Unlike keys_as_list(), the SAME view object updates live when the
    # dict it came from changes -- no need to call keys_view() again.
    prices["GOOG"] = 490.10
    assert list(view) == ["AAPL", "IBM", "GOOG"]


def test_values_view_reflects_later_changes_to_the_dict():
    prices = {"AAPL": 645.57, "IBM": 91.23}
    view = values_view(prices)
    assert list(view) == [645.57, 91.23]

    prices["GOOG"] = 490.10
    assert list(view) == [645.57, 91.23, 490.10]


def test_format_price_lines():
    prices = {"IBM": 91.23, "GOOG": 490.10}
    assert format_price_lines(prices) == ["IBM = 91.23", "GOOG = 490.1"]
