"""
Tests for scripts/fundamentals/objects_and_classes.py
"""

import re

from scripts.fundamentals.objects_and_classes import Stack


def test_new_stack_is_empty():
    s = Stack()
    assert len(s) == 0


def test_push_adds_items_and_updates_len():
    s = Stack()
    s.push("Dave")
    s.push(42)
    s.push([3, 4, 5])
    assert len(s) == 3


def test_pop_returns_items_in_lifo_order():
    s = Stack()
    s.push("Dave")
    s.push(42)
    s.push([3, 4, 5])

    x = s.pop()
    y = s.pop()

    assert x == [3, 4, 5]
    assert y == 42
    assert len(s) == 1


def test_items_are_stored_on_a_private_attribute():
    s = Stack()
    s.push("Dave")

    # Not part of the public API, but demonstrates how push()/pop() are
    # implemented under the hood: a single leading underscore is a
    # convention, not an enforced restriction.
    assert s._items == ["Dave"]


def test_repr_reports_class_name_and_size():
    s = Stack()
    s.push("Dave")
    s.push(42)

    result = repr(s)

    assert result.startswith("<Stack at 0x")
    assert result.endswith("size=2>")


def test_repr_includes_object_id_as_hex():
    s = Stack()

    result = repr(s)

    match = re.match(r"^<Stack at 0x([0-9a-f]+), size=0>$", result)
    assert match is not None
    assert int(match.group(1), 16) == id(s)
