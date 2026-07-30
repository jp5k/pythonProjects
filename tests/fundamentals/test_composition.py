"""
Tests for scripts/fundamentals/composition.py
"""

from scripts.fundamentals.objects_and_classes import Stack
from scripts.fundamentals.composition import Calculator


def test_calculator_is_not_a_stack():
    # Composition, not inheritance: Calculator uses a Stack internally
    # but doesn't subclass it.
    assert not isinstance(Calculator(), Stack)


def test_calculator_holds_a_stack_as_a_private_attribute():
    c = Calculator()
    assert isinstance(c._stack, Stack)


def test_push_and_pop_delegate_to_internal_stack():
    c = Calculator()
    c.push(3)
    c.push(4)
    assert c.pop() == 4
    assert c.pop() == 3


def test_add():
    c = Calculator()
    c.push(3)
    c.push(4)
    c.add()
    assert c.pop() == 7


def test_mul():
    c = Calculator()
    c.push(6)
    c.push(7)
    c.mul()
    assert c.pop() == 42


def test_sub_uses_first_pushed_minus_second_pushed():
    c = Calculator()
    c.push(10)
    c.push(3)
    c.sub()
    assert c.pop() == 7


def test_div_uses_first_pushed_divided_by_second_pushed():
    c = Calculator()
    c.push(20)
    c.push(4)
    c.div()
    assert c.pop() == 5.0


def test_operations_leave_a_single_result_on_the_stack():
    c = Calculator()
    c.push(1)
    c.push(2)
    c.add()
    assert len(c._stack) == 1
