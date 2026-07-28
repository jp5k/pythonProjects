"""
Tests for scripts/fundamentals/lists.py
"""

from scripts.fundamentals.lists import (
    access_by_index,
    access_last_item,
    append_item,
    concatenate_lists,
    create_empty_list_constructor,
    create_empty_list_literal,
    create_list,
    insert_item,
    iterate_list,
    modify_by_index,
    nested_list_access,
    parse_rows,
    replace_slice,
    slice_list,
    string_to_char_list,
    total_portfolio_cost,
)


def test_create_list():
    assert create_list() == ["Dave", "Paula", "Thomas", "Lewis"]


def test_access_by_index():
    names = create_list()
    assert access_by_index(names, 2) == "Thomas"


def test_access_last_item():
    names = create_list()
    assert access_last_item(names) == "Lewis"


def test_modify_by_index():
    names = create_list()
    result = modify_by_index(names, 2, "Tom")
    assert result == ["Dave", "Paula", "Tom", "Lewis"]
    # modify_by_index changes the list in place rather than returning a copy.
    assert result is names


def test_append_item():
    names = create_list()
    result = append_item(names, "Alex")
    assert result == ["Dave", "Paula", "Thomas", "Lewis", "Alex"]
    assert result is names


def test_insert_item():
    names = create_list()
    result = insert_item(names, 2, "Aya")
    assert result == ["Dave", "Paula", "Aya", "Thomas", "Lewis"]


def test_iterate_list():
    names = create_list()
    assert iterate_list(names) == names


def test_slice_list():
    names = create_list()
    first_two, from_index_two = slice_list(names)
    assert first_two == ["Dave", "Paula"]
    assert from_index_two == ["Thomas", "Lewis"]


def test_replace_slice_same_length():
    names = create_list()
    result = replace_slice(names, 1, 2, ["Becky"])
    assert result == ["Dave", "Becky", "Thomas", "Lewis"]


def test_replace_slice_can_change_list_length():
    names = create_list()
    result = replace_slice(names, 0, 2, ["Dave", "Mark", "Jeff"])
    assert result == ["Dave", "Mark", "Jeff", "Thomas", "Lewis"]


def test_concatenate_lists():
    assert concatenate_lists(["x", "y"], ["z", "z", "y"]) == ["x", "y", "z", "z", "y"]


def test_create_empty_list_literal():
    assert create_empty_list_literal() == []


def test_create_empty_list_constructor():
    assert create_empty_list_constructor() == []


def test_string_to_char_list():
    assert string_to_char_list("Dave") == ["D", "a", "v", "e"]


def test_nested_list_access():
    mixed, item1, item2, item3 = nested_list_access()
    assert mixed == [1, "Dave", 3.14, ["Mark", 7, 9, [100, 101]], 10]
    assert item1 == "Dave"
    assert item2 == 9
    assert item3 == 101


def test_parse_rows():
    lines = ["SYM, 123, 456.78", "AAPL, 50, 91.10"]
    assert parse_rows(lines) == [
        ["SYM", " 123", " 456.78"],
        ["AAPL", " 50", " 91.10"],
    ]


def test_total_portfolio_cost():
    rows = [["SYM", " 123", " 456.78"], ["AAPL", " 50", " 91.10"]]
    expected = 123 * 456.78 + 50 * 91.10
    assert total_portfolio_cost(rows) == expected
