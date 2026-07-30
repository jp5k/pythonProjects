"""
Method overriding and super()

Covers a second way a subclass can build on a parent class: instead of
only *adding* new methods (as scripts/fundamentals/inheritance.py's
MyStack does with swap()), a subclass can *override* one of the
parent's methods -- define a method with the same name -- to change or
extend its behaviour. `super()` is how the overriding method can still
call the parent's original implementation instead of duplicating its
logic, so the override only needs to express what's different.
"""

from scripts.fundamentals.objects_and_classes import Stack


class NumericStack(Stack):
    """A Stack that only accepts int or float items.

    NumericStack inherits everything from Stack -- __init__, pop,
    __len__, __repr__ -- except push, which it overrides below.
    """

    def push(self, item):
        """Push item onto the stack, rejecting anything that isn't an int or float.

        This method has the same name as Stack.push, which is what
        makes it an *override*: for a NumericStack instance, Python
        finds this version first and the base class's push is never
        reached directly. But the override doesn't reimplement the
        actual pushing -- it only adds the validation that's new here,
        then hands off to `super().push(item)` to do the rest.

        `super()` gives access to the parent class's version of a
        method that this class has overridden. `super().push(item)`
        calls Stack.push(self, item) -- the original append-to-the-list
        behaviour -- without NumericStack needing to know or repeat how
        Stack stores its items. This is the general pattern for
        overriding: add what's new, then delegate to super() for what
        isn't.

        `isinstance(item, (int, float))` checks item's type against
        several types at once by passing a tuple -- equivalent to
        `isinstance(item, int) or isinstance(item, float)`. Note that
        this also accepts `True`/`False`: `bool` is itself a subclass
        of `int` in Python, another instance of the inheritance this
        script is about.
        """
        if not isinstance(item, (int, float)):
            raise TypeError("Expected an int or float")
        super().push(item)


if __name__ == "__main__":
    # A quick, human-readable demo. Run as a module from the repo root:
    #   python -m scripts.fundamentals.method_overriding
    #
    # (Not `python scripts/fundamentals/method_overriding.py` -- see
    # the note in inheritance.py's __main__ block for why the direct
    # path form doesn't work once a script imports another scripts.*
    # module.)

    s = NumericStack()
    s.push(42)
    print(f"push(42) succeeded: {s!r}")

    try:
        s.push("Dave")
    except TypeError as exc:
        print(f"push('Dave') raised TypeError: {exc}")
