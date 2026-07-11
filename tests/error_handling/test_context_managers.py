"""
Tests for scripts/error_handling/context_managers.py

These tests check that every variant of "guarantee resource cleanup"
(try/finally, class-based context manager, generator-based context
manager) actually closes its resource both when the block succeeds and
when it raises. They also check that exception suppression via
__exit__'s return value is selective (ValueError only).
"""

import pytest

from scripts.error_handling.context_managers import (
    ManagedResource,
    Resource,
    SwallowValueError,
    close_with_context_manager,
    close_with_generator_context_manager,
    close_with_try_finally,
    managed_resource,
    run_and_swallow_value_error,
)


def test_resource_starts_open_and_closes():
    resource = Resource("test")
    assert resource.is_open is True
    resource.close()
    assert resource.is_open is False


def test_close_with_try_finally_closes_on_success():
    resource = Resource("test")
    close_with_try_finally(resource, should_raise=False)
    assert resource.is_open is False


def test_close_with_try_finally_closes_on_exception():
    resource = Resource("test")
    with pytest.raises(ValueError):
        close_with_try_finally(resource, should_raise=True)
    assert resource.is_open is False


def test_close_with_context_manager_closes_on_success():
    resource = Resource("test")
    close_with_context_manager(resource, should_raise=False)
    assert resource.is_open is False


def test_close_with_context_manager_closes_on_exception():
    resource = Resource("test")
    with pytest.raises(ValueError):
        close_with_context_manager(resource, should_raise=True)
    assert resource.is_open is False


def test_close_with_generator_context_manager_closes_on_success():
    resource = Resource("test")
    close_with_generator_context_manager(resource, should_raise=False)
    assert resource.is_open is False


def test_close_with_generator_context_manager_closes_on_exception():
    resource = Resource("test")
    with pytest.raises(ValueError):
        close_with_generator_context_manager(resource, should_raise=True)
    assert resource.is_open is False


def test_managed_resource_and_generator_version_agree():
    # Both context manager implementations should guarantee the same
    # end state for an equivalent resource -- proving they're really
    # two ways of writing the same protocol.
    resource_a = Resource("a")
    resource_b = Resource("b")

    with ManagedResource(resource_a) as bound_a:
        pass
    with managed_resource(resource_b) as bound_b:
        pass

    assert bound_a is resource_a
    assert bound_b is resource_b
    assert resource_a.is_open is False
    assert resource_b.is_open is False


def test_run_and_swallow_value_error_suppresses_value_error():
    assert run_and_swallow_value_error(should_raise_value_error=True) == "completed"


def test_run_and_swallow_value_error_lets_other_exceptions_propagate():
    with pytest.raises(RuntimeError):
        run_and_swallow_value_error(should_raise_other=True)


def test_run_and_swallow_value_error_no_exception():
    assert run_and_swallow_value_error() == "completed"


def test_swallow_value_error_context_manager_directly():
    with SwallowValueError():
        raise ValueError("swallowed")
    # Reaching this line proves the exception above did not propagate.
