"""
Objects and classes

Covers the basics of defining a class: the `self` parameter and why it's
always the first parameter of an instance method, "dunder" (double
underscore) methods like `__init__` that hook a class into the rest of
the language, a single leading underscore as the convention for marking
an attribute "private" (implementation detail, not part of the public
API), and why every class benefits from a `__repr__` method for
debugging. The example class is a simple last-in-first-out `Stack` with
`push()` and `pop()` operations.
"""


class Stack:
    """A last-in-first-out (LIFO) stack of items.

    Items go on with `push()` and come back off, most-recently-pushed
    first, with `pop()`.
    """

    def __init__(self):
        """Initialize a new, empty stack.

        `__init__` is a dunder ("double underscore") method -- its name
        starts and ends with two underscores. Python treats names that
        look like this specially: rather than being called directly,
        they're invoked automatically by the language in response to
        some event. `__init__` is invoked automatically right after a
        new instance is created, and it's where an object sets up its
        starting state. Writing `Stack()` is what triggers Python to
        create a blank instance and then call `__init__` on it.

        `self` is the instance being initialized -- the object that
        `Stack()` is in the middle of creating. It's the first parameter
        of every instance method, by convention named `self` (nothing
        magic about the name itself, but every Python programmer follows
        it), and Python supplies it automatically. When you write
        `s.push(item)`, Python translates that behind the scenes into
        `Stack.push(s, item)` -- `s` is passed in as `self` so the method
        knows *which* stack it's operating on. Without `self`, a method
        would have no way to reach the particular instance's own data;
        it's how `self._items` below ends up being *this* stack's list
        and not some other stack's.
        """
        # A single leading underscore is a naming convention, not a
        # language feature that enforces anything -- Python won't stop
        # code outside this class from reading or writing `self._items`
        # directly. The underscore is a signal to other programmers (and
        # to your future self): "this is an internal implementation
        # detail, not part of the public interface -- use push()/pop()
        # instead of touching this list yourself, because I might change
        # how it's stored later without warning."
        self._items = []

    def push(self, item):
        """Add item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the item at the top of the stack.

        list.pop() with no argument removes and returns the *last*
        element, which is exactly the "most recently pushed" item --
        that's what makes appending/popping from the end of a Python
        list an easy way to implement LIFO stack behaviour.
        """
        return self._items.pop()

    def __len__(self):
        """Return the number of items currently on the stack.

        `__len__` is another dunder method: defining it is what makes
        the built-in `len()` function work on a Stack. Without it,
        `len(s)` would raise a TypeError -- `len()` doesn't know how to
        measure an arbitrary object unless the object opts in by
        defining `__len__`. This is one of many "special methods" that
        let a custom class plug into Python's built-in functions and
        syntax (others include `__add__` for `+`, `__eq__` for `==`,
        and `__iter__` for `for x in obj`) instead of every class
        needing its own one-off `.size()`-style method with a different
        name.
        """
        return len(self._items)

    def __repr__(self):
        """Return an unambiguous, debugging-friendly string for this stack.

        `__repr__` is the dunder method behind `repr(obj)` -- and it's
        also what the interactive interpreter and debuggers print for an
        object when there's no `__str__` to prefer instead, and what
        shows up when an object appears inside a list or dict that gets
        printed. It's good practice to define `__repr__` on essentially
        every class you write, even ones without any special
        formatting needs, because the default `__repr__` inherited from
        `object` -- something like `<__main__.Stack object at
        0x7f2b1c0a4d90>` -- tells you the type and memory address but
        nothing about the object's actual state. That default is nearly
        useless when you're staring at a debugger or a traceback trying
        to figure out *what was in this thing*. A few extra minutes
        spent writing a `__repr__` that reports useful state (here, how
        many items the stack holds) pays for itself many times over the
        first time you need to debug a script that uses the class.

        `type(self).__name__` reads the class's name off the instance
        (`"Stack"`) rather than hardcoding the string `"Stack"`, so this
        still reports correctly if the class is ever renamed or
        subclassed. `id(self)` is the object's identity -- CPython uses
        it as the memory address -- formatted here as hex with `0x{...:x}`
        to look like the interpreter's own default repr. `len(self)`
        calls the `__len__` method defined above; using the built-in
        `len()` here rather than `len(self._items)` directly shows the
        two dunder methods cooperating, the same way user code would
        call `len(s)` rather than reaching into `s._items`.
        """
        return f"<{type(self).__name__} at 0x{id(self):x}, size={len(self)}>"


if __name__ == "__main__":
    # A quick, human-readable demo when running this file directly with:
    #   python scripts/fundamentals/objects_and_classes.py

    s = Stack()
    s.push("Dave")
    s.push(42)
    s.push([3, 4, 5])
    print(f"after three pushes: {s!r}")

    # pop() returns items in the reverse order they were pushed --
    # last in, first out. The list goes first because it was pushed last.
    x = s.pop()
    y = s.pop()
    print(f"x = {x!r}")
    print(f"y = {y!r}")

    # len(s) works because Stack defines __len__.
    print(f"len(s) = {len(s)}")

    # repr(s) -- and just typing `s` at an interactive prompt, or letting
    # a traceback print it -- goes through __repr__.
    print(f"repr(s) = {s!r}")
