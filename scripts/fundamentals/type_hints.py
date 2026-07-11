"""
Type hints: annotating function parameters and return values with the
types they're expected to be, and what Python actually does (and does
NOT do) with those annotations.

Python is dynamically typed — it never required declaring types the way
Java does with `public int add(int a, int b)`. Type hints (PEP 484, added
in Python 3.5) let you annotate types anyway, purely for documentation and
tooling: static checkers like mypy or pyright read them and flag mismatches
before you run anything. But the Python interpreter itself does NOT
enforce them at runtime — a hint is a promise to the reader, not a
contract the language checks for you.
"""

from typing import Optional


def add(a: int, b: int) -> int:
    """A fully-hinted function: two int parameters, an int return value."""
    # The ": int" after each parameter says "this should be an int".
    # The "-> int" before the final colon says "this returns an int".
    # None of this changes how the function runs — it's metadata only.
    return a + b


def add_no_hints(a, b):
    """The exact same logic with no hints — runs identically to add()."""
    # Proof that hints are optional: Python doesn't need them to execute
    # this function correctly. Hints exist for humans and tools, not the
    # interpreter.
    return a + b


def greet(name: str) -> str:
    """Hints read naturally at the call site: greet expects a str, returns a str."""
    return f"Hello, {name}!"


def average(numbers: list[float]) -> float:
    """Hints work with built-in generics too, e.g. list[float].

    (Python 3.9+ lets you write list[float] directly. Older code targeting
    earlier versions uses `from typing import List` and `List[float]`
    instead — same meaning, older spelling.)
    """
    return sum(numbers) / len(numbers)


def find_first_even(numbers: list[int]) -> Optional[int]:
    """Optional[int] means "an int, or None" — common for functions that
    might not find anything to return.

    Optional[int] is shorthand for Union[int, None]. On Python 3.10+ you
    can also write the newer `int | None` syntax — same meaning.
    """
    for number in numbers:
        if number % 2 == 0:
            return number
    return None


def add_wrong_but_still_runs(a: int, b: int) -> int:
    """Deliberately violates its own hint to prove hints aren't enforced.

    This promises `-> int` but actually returns a str. Python runs it
    without complaint — there is no runtime check. Only a static type
    checker (mypy, pyright) would catch this mismatch, and only if you
    run it as a separate step; it won't stop `python` from executing.
    """
    return f"{a} and {b}"  # Wrong on purpose! No runtime error occurs.


if __name__ == "__main__":
    # A quick, human-readable demo when running this file directly with:
    #   python scripts/fundamentals/type_hints.py
    print("add(2, 3) =", add(2, 3))
    print("greet('Ada') =", greet("Ada"))
    print("average([1.0, 2.0, 3.0]) =", average([1.0, 2.0, 3.0]))
    print("find_first_even([1, 3, 5]) =", find_first_even([1, 3, 5]))
    print("find_first_even([1, 3, 4, 5]) =", find_first_even([1, 3, 4, 5]))

    result = add_wrong_but_still_runs(2, 3)
    print("add_wrong_but_still_runs(2, 3) =", repr(result))
    print("(That returned a str despite its '-> int' hint — Python does")
    print(" not enforce type hints at runtime; a static checker would.)")
