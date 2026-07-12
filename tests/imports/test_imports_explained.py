"""
Tests for scripts/imports/imports_explained.py

These check that each of the four import-statement forms demonstrated
in the script actually works as advertised (plain, aliased, from-import,
aliased from-import), that the tour of common standard-library imports
behaves correctly, and that the module-caching / sys.path claims hold.
"""

from datetime import date

from scripts.imports.imports_explained import (
    add_days,
    circle_area,
    days_between,
    first_match,
    flatten,
    join_paths,
    module_is_cached_after_import,
    path_suffix,
    product_via_reduce,
    round_trip_json,
    search_path_is_a_nonempty_list_of_strings,
    tally_letters,
)


def test_circle_area():
    assert circle_area(1) == 3.141592653589793


def test_join_paths():
    assert join_paths("a", "b", "c.txt") == "a/b/c.txt"


def test_days_between():
    assert days_between(date(2024, 1, 1), date(2024, 1, 11)) == 10


def test_add_days():
    assert add_days(date(2024, 1, 1), 10) == date(2024, 1, 11)


def test_tally_letters():
    counts = tally_letters("mississippi")
    assert counts["i"] == 4
    assert counts["s"] == 4
    assert counts["p"] == 2
    assert counts["m"] == 1


def test_round_trip_json():
    payload = {"name": "Ada", "year": 1815}
    assert round_trip_json(payload) == payload


def test_flatten():
    assert flatten([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]


def test_first_match_found():
    assert first_match(r"\d+", "room 42") == "42"


def test_first_match_not_found():
    assert first_match(r"\d+", "no digits here") is None


def test_path_suffix():
    assert path_suffix("notes.txt") == ".txt"


def test_product_via_reduce():
    assert product_via_reduce([1, 2, 3, 4]) == 24


def test_module_is_cached_after_import():
    assert module_is_cached_after_import() is True


def test_search_path_is_a_nonempty_list_of_strings():
    assert search_path_is_a_nonempty_list_of_strings() is True
