"""
Tests for scripts/fundamentals/iteration_and_looping.py
"""

from scripts.fundamentals.iteration_and_looping import (
    bullet_list,
    format_dict_entries,
    powers_of_two_with_list_literal,
    powers_of_two_with_range,
    range_start_stop,
    range_start_stop_step,
    range_stop_only,
    read_lines_stripped,
    uppercase_each_character,
)


def test_powers_of_two_with_list_literal():
    result = powers_of_two_with_list_literal()
    assert result[0] == "2 to the 1 power is 2"
    assert result[-1] == "2 to the 9 power is 512"
    assert len(result) == 9


def test_powers_of_two_with_range_matches_list_literal_version():
    # Both functions should produce identical output -- range(1, 10) is
    # just a shortcut for the same nine values as the list literal.
    assert powers_of_two_with_range() == powers_of_two_with_list_literal()


def test_range_stop_only():
    assert range_stop_only(5) == [0, 1, 2, 3, 4]


def test_range_stop_only_zero_produces_empty_list():
    assert range_stop_only(0) == []


def test_range_start_stop():
    assert range_start_stop(1, 8) == [1, 2, 3, 4, 5, 6, 7]


def test_range_start_stop_step():
    assert range_start_stop_step(0, 14, 3) == [0, 3, 6, 9, 12]


def test_range_start_stop_step_negative_step_counts_down():
    assert range_start_stop_step(8, 1, -1) == [8, 7, 6, 5, 4, 3, 2]


def test_uppercase_each_character():
    assert uppercase_each_character("abc") == ["A", "B", "C"]


def test_uppercase_each_character_empty_string():
    assert uppercase_each_character("") == []


def test_bullet_list():
    result = bullet_list(["apples", "bananas"])
    assert result == ["- apples", "- bananas"]


def test_bullet_list_empty():
    assert bullet_list([]) == []


def test_format_dict_entries():
    result = format_dict_entries({"GOOG": 490.10, "IBM": 91.23})
    assert result == ["GOOG: 490.1", "IBM: 91.23"]


def test_read_lines_stripped(tmp_path):
    data_path = tmp_path / "data.txt"
    data_path.write_text("first line\nsecond line\nthird line\n")

    result = read_lines_stripped(data_path)

    # Each line comes back without its trailing newline.
    assert result == ["first line", "second line", "third line"]


def test_read_lines_stripped_no_trailing_newline_on_last_line(tmp_path):
    data_path = tmp_path / "data.txt"
    data_path.write_text("only line")

    result = read_lines_stripped(data_path)

    assert result == ["only line"]
