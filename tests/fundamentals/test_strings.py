"""
Tests for scripts/fundamentals/strings.py
"""

from scripts.fundamentals.strings import (
    character_at_index,
    concatenate,
    quoting_styles,
    replace_substring,
    show_repr,
    slicing_examples,
    string_length,
    string_to_int_before_math,
    strip_whitespace,
    upper_case,
)


def test_quoting_styles_are_all_equivalent_text():
    single, double, triple = quoting_styles()
    assert single == "hello"
    assert double == "hello"
    assert triple == "This string\nspans\nmultiple lines."


def test_string_length():
    assert string_length("hello world") == 11


def test_character_at_index():
    assert character_at_index("hello world", 4) == "o"


def test_slicing_examples():
    first_five, from_five, middle, last_three, every_other, reversed_s = (
        slicing_examples("hello world")
    )
    assert first_five == "hello"
    assert from_five == " world"
    assert middle == "llo w"
    assert last_three == "rld"
    assert every_other == "hlowrd"
    assert reversed_s == "dlrow olleh"


def test_replace_substring():
    assert replace_substring("hello world", "world", "there") == "hello there"


def test_strip_whitespace():
    assert strip_whitespace("   trim me   ") == "trim me"


def test_upper_case():
    assert upper_case("hello world") == "HELLO WORLD"


def test_concatenate():
    assert concatenate("foo", "bar") == "foobar"


def test_string_to_int_before_math():
    assert string_to_int_before_math("5", 10) == 15


def test_show_repr_of_string_includes_quotes():
    # repr() of a string includes the quote characters, which is what
    # makes it useful for distinguishing "5" (a string) from 5 (an int).
    assert show_repr("5") == "'5'"


def test_show_repr_of_int_has_no_quotes():
    assert show_repr(5) == "5"
