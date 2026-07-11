"""
Context managers and the `with` statement.

When code needs to set something up and guarantee it's torn down again
(closing a file, releasing a lock, disconnecting a socket), the manual
way to do that is `try`/`finally`: do the work in the `try` block, and
put the cleanup in `finally` so it runs whether or not something went
wrong. That works, but it's boilerplate you have to remember to write
correctly every single time.

A context manager formalizes this pattern behind the `with` statement:
`with thing:` guarantees `thing`'s cleanup runs when the block exits,
success or failure, without you writing `try`/`finally` yourself.

There are two ways to build one:
  1. A class implementing `__enter__` (setup) and `__exit__` (teardown).
  2. A generator function decorated with `@contextlib.contextmanager`,
     where code before `yield` is setup and code after it (in a
     `finally`) is teardown.

Both are shown below, doing the exact same job, so you can compare them.
"""

from contextlib import contextmanager


class Resource:
    """A stand-in for anything that needs explicit cleanup (a file, a socket, a lock).

    We use this fake instead of a real file so the examples below have
    no actual filesystem/network side effects and stay trivial to test.
    """

    def __init__(self, name):
        self.name = name
        self.is_open = True  # flips to False once cleanup has run

    def close(self):
        self.is_open = False


def close_with_try_finally(resource, should_raise=False):
    """Manually guarantee resource.close() runs, using try/finally.

    This is the pattern context managers exist to replace. Note that
    the `finally` block runs whether or not `should_raise` triggers the
    exception below — that's the whole point of `finally`, and exactly
    the guarantee a context manager will give us for free.
    """
    try:
        if should_raise:
            raise ValueError("simulated failure while using the resource")
    finally:
        resource.close()


class ManagedResource:
    """A context manager wrapping a Resource, built with __enter__/__exit__.

    `with ManagedResource(resource):` calls __enter__ on the way in and
    __exit__ on the way out — including when the block raises.
    """

    def __init__(self, resource):
        self.resource = resource

    def __enter__(self):
        # Whatever __enter__ returns becomes the value bound by `as ...`.
        return self.resource

    def __exit__(self, exc_type, exc_value, traceback):
        # This runs on the way out of the `with` block no matter what --
        # normal exit or an exception propagating through. It's the
        # __exit__ protocol's equivalent of a `finally` block.
        self.resource.close()
        # Returning False (or None, implicitly) tells Python "I did not
        # handle this exception" -- so if one occurred, it keeps
        # propagating normally after cleanup runs.
        return False


def close_with_context_manager(resource, should_raise=False):
    """Same guarantee as close_with_try_finally, expressed with `with` instead."""
    with ManagedResource(resource):
        if should_raise:
            raise ValueError("simulated failure while using the resource")


@contextmanager
def managed_resource(resource):
    """The same context manager as ManagedResource, written as a generator.

    Everything before `yield` is __enter__; everything after it, inside
    `finally`, is __exit__. `@contextmanager` handles wiring this
    generator up to the `with` protocol for us.
    """
    try:
        yield resource  # the `with` block's body runs while we're paused here
    finally:
        resource.close()  # runs on the way out, success or failure -- same as __exit__


def close_with_generator_context_manager(resource, should_raise=False):
    """Same guarantee again, this time via the generator-based context manager."""
    with managed_resource(resource):
        if should_raise:
            raise ValueError("simulated failure while using the resource")


class SwallowValueError:
    """A context manager that suppresses ValueError (only) raised inside its block.

    This demonstrates that __exit__'s return value controls whether an
    exception propagates: return True and Python treats it as handled;
    return False (or None) and it keeps propagating.
    """

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # exc_type is None if the block exited normally, otherwise it's
        # the exception class that was raised. Only suppress ValueError.
        return exc_type is ValueError


def run_and_swallow_value_error(should_raise_value_error=False, should_raise_other=False):
    """Shows that suppression is selective: ValueError is swallowed, RuntimeError is not."""
    with SwallowValueError():
        if should_raise_value_error:
            raise ValueError("this gets swallowed by __exit__ returning True")
        if should_raise_other:
            raise RuntimeError("this does NOT get swallowed -- it propagates")
    # If a ValueError was raised and swallowed above, execution resumes
    # here, right after the `with` block, as if nothing happened.
    return "completed"


if __name__ == "__main__":
    # A quick, human-readable demo when running this file directly with:
    #   python scripts/error_handling/context_managers.py

    print("--- try/finally ---")
    r1 = Resource("r1")
    close_with_try_finally(r1, should_raise=False)
    print("No exception -> resource.is_open =", r1.is_open)

    r2 = Resource("r2")
    try:
        close_with_try_finally(r2, should_raise=True)
    except ValueError as exc:
        print(f"Caught {exc!r} -> resource.is_open =", r2.is_open)

    print("\n--- class-based context manager (__enter__/__exit__) ---")
    r3 = Resource("r3")
    close_with_context_manager(r3, should_raise=False)
    print("No exception -> resource.is_open =", r3.is_open)

    r4 = Resource("r4")
    try:
        close_with_context_manager(r4, should_raise=True)
    except ValueError as exc:
        print(f"Caught {exc!r} -> resource.is_open =", r4.is_open)

    print("\n--- generator-based context manager (@contextmanager) ---")
    r5 = Resource("r5")
    close_with_generator_context_manager(r5, should_raise=False)
    print("No exception -> resource.is_open =", r5.is_open)

    r6 = Resource("r6")
    try:
        close_with_generator_context_manager(r6, should_raise=True)
    except ValueError as exc:
        print(f"Caught {exc!r} -> resource.is_open =", r6.is_open)

    print("\n--- selective exception suppression ---")
    print(
        "ValueError swallowed ->",
        run_and_swallow_value_error(should_raise_value_error=True),
    )
    try:
        run_and_swallow_value_error(should_raise_other=True)
    except RuntimeError as exc:
        print(f"RuntimeError NOT swallowed, propagated as {exc!r}")
