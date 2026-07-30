"""
Inheritance

Covers extending an existing class instead of writing a new one from
scratch: `class MyStack(Stack):` makes `MyStack` a *subclass* of
`Stack`, automatically inheriting every method `Stack` already defines
(`push`, `pop`, `__len__`, `__repr__`) without redefining any of them.
The subclass only needs to add what's different -- here, a `swap()`
method that exchanges the top two items on the stack.
"""

from scripts.fundamentals.objects_and_classes import Stack


class MyStack(Stack):
    """A Stack with one extra operation: swapping its top two items.

    `class MyStack(Stack):` -- the parenthesized `Stack` is what makes
    this *inheritance* rather than a brand new, unrelated class. MyStack
    doesn't need its own `__init__`, `push`, `pop`, `__len__`, or
    `__repr__` -- it gets all of them for free from Stack. An instance
    of MyStack really is a Stack (`isinstance(MyStack(), Stack)` is
    True); it just knows how to do one additional thing.
    """

    def swap(self):
        """Exchange the top two items on the stack.

        `self.pop()` and `self.push()` here are not redefined anywhere
        on MyStack -- they resolve to Stack's implementations through
        ordinary attribute lookup: Python looks for `pop` on MyStack
        first, doesn't find it, then looks on its parent class Stack
        and finds it there. That's the mechanism that lets a subclass
        call its parent's methods via `self` exactly as if they were
        its own, without importing or copy-pasting anything.

        Popping both items and pushing them back in reverse order (`a`
        first, then `b`) puts the item that was second-from-top (`b`)
        on top, and the item that was on top (`a`) just underneath it
        -- i.e. the two are swapped.
        """
        a = self.pop()
        b = self.pop()
        self.push(a)
        self.push(b)


if __name__ == "__main__":
    # A quick, human-readable demo. Run as a module from the repo root:
    #   python -m scripts.fundamentals.inheritance
    #
    # (Not `python scripts/fundamentals/inheritance.py` -- this script
    # is the first one to import from another scripts.* module, and the
    # direct-path form doesn't put the repo root on sys.path the way
    # -m does, so the `from scripts.fundamentals.objects_and_classes
    # import Stack` line above would fail to resolve.)

    s = MyStack()
    s.push("Dave")
    s.push(42)
    print(f"after two pushes: {s!r}")

    # repr(s) reports "MyStack", not "Stack" -- Stack.__repr__ uses
    # type(self).__name__, which looks up the *actual* class of the
    # instance at runtime. A subclass gets a correct-looking repr for
    # free, without having to override __repr__ itself.

    s.swap()
    print(f"after swap: {s!r}")

    # Popping now returns 'Dave' first, then 42 -- the reverse of what
    # plain push/pop order would have given without the swap() call in
    # between.
    x = s.pop()
    y = s.pop()
    print(f"x = {x!r}")
    print(f"y = {y!r}")
