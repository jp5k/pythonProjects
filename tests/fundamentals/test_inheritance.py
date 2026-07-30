"""
Tests for scripts/fundamentals/inheritance.py
"""

from scripts.fundamentals.objects_and_classes import Stack
from scripts.fundamentals.inheritance import MyStack


def test_myStack_is_a_stack():
    assert isinstance(MyStack(), Stack)


def test_inherited_push_and_pop_work_unchanged():
    s = MyStack()
    s.push("Dave")
    s.push(42)

    assert len(s) == 2
    assert s.pop() == 42
    assert s.pop() == "Dave"


def test_swap_exchanges_top_two_items():
    s = MyStack()
    s.push("Dave")
    s.push(42)

    s.swap()

    assert s.pop() == "Dave"
    assert s.pop() == 42


def test_swap_leaves_len_unchanged():
    s = MyStack()
    s.push("Dave")
    s.push(42)

    before = len(s)
    s.swap()

    assert len(s) == before


def test_repr_reports_subclass_name():
    s = MyStack()

    result = repr(s)

    assert result.startswith("<MyStack")
