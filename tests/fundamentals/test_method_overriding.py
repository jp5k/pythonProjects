"""
Tests for scripts/fundamentals/method_overriding.py
"""

import pytest

from scripts.fundamentals.objects_and_classes import Stack
from scripts.fundamentals.method_overriding import NumericStack


def test_numericStack_is_a_stack():
    assert isinstance(NumericStack(), Stack)


def test_push_accepts_int():
    s = NumericStack()
    s.push(42)
    assert s.pop() == 42


def test_push_accepts_float():
    s = NumericStack()
    s.push(3.14)
    assert s.pop() == 3.14


def test_push_rejects_str():
    s = NumericStack()
    with pytest.raises(TypeError, match="Expected an int or float"):
        s.push("Dave")


def test_rejected_push_does_not_add_to_stack():
    s = NumericStack()
    with pytest.raises(TypeError):
        s.push("Dave")
    assert len(s) == 0


def test_override_delegates_to_super_for_valid_items():
    # A successful push still goes through Stack.push under the hood,
    # so len() and pop() behave exactly as they would on a plain Stack.
    s = NumericStack()
    s.push(1)
    s.push(2)
    assert len(s) == 2
    assert s.pop() == 2
    assert s.pop() == 1
