"""
Functions

Covers the basics of defining and calling Python functions: the `def`
statement and `return`, giving a function a documentation string as its
first statement so it can be introspected via `__doc__`/`help()`,
returning multiple values by packing them into a tuple, giving a
parameter a default value so callers can omit it, calling a function
with keyword arguments (naming which parameter each value goes to,
in any order), and how a function can read (but not, without extra
syntax, reassign) a variable defined at module level outside of it.
"""


def remainder(a, b):
    """Return the remainder of a divided by b, using truncating division.

    This docstring is the first statement in the function body. Because
    of that, Python treats it specially: it becomes the function's
    `__doc__` attribute, retrievable as `remainder.__doc__` or via
    `help(remainder)`, instead of being just an ordinary comment that
    tools have no way to find.
    """
    q = a // b  # // is truncating (floor) division -- it discards any fractional part
    r = a - q * b  # what's left over after taking out q whole multiples of b
    return r


def divide(a, b):
    """Return both the quotient and remainder of a divided by b.

    `return q, r` packs the two values into a tuple `(q, r)` -- the
    comma is what does the packing, the parentheses are optional. The
    caller can then unpack both results in a single assignment:
    `quotient, remainder = divide(...)`, rather than calling two
    separate functions or getting back only one value.
    """
    q = a // b
    r = a - q * b
    return q, r


def connect(hostname, port, timeout=300):
    """Build a connection descriptor, defaulting `timeout` to 300 seconds.

    `timeout=300` in the parameter list gives that parameter a default
    value. A caller who doesn't care about the timeout can simply leave
    it out of the call -- `connect('www.python.org', 80)` -- and 300 is
    used automatically. A caller who does care can still override it by
    passing a third argument.

    This function can't actually open a network connection in a
    self-contained teaching script, so it returns a plain dict
    describing what it *would* connect with -- enough to demonstrate
    and test the default-value and keyword-argument behaviour.
    """
    return {"hostname": hostname, "port": port, "timeout": timeout}


# A global variable: assigned here at module level, outside of any
# function. Any function defined below in this same file can read it.
debug = True


def read_data(filename):
    """Read data from filename, logging progress if the global `debug` flag is on.

    A function can look up a name that isn't one of its parameters or
    local variables by walking outward to the enclosing module's global
    scope -- that's how `read_data` sees `debug` here even though it's
    never passed in as an argument. This only works for *reading* the
    global; assigning to `debug` inside a function would instead create
    a new local variable shadowing it (Python's `global` keyword exists
    to opt into reassigning the outer name, but that's not needed here
    since this function only reads `debug`).

    There's no real file I/O in this teaching example -- it just reports
    what it would do, so the demonstration stays self-contained.
    """
    if debug:
        print("Reading", filename)
    return filename


if __name__ == "__main__":
    # A quick, human-readable demo when running this file directly with:
    #   python scripts/fundamentals/functions.py

    result = remainder(37, 15)
    print(f"remainder(37, 15) = {result}")

    # The docstring is retrievable from the function object itself.
    print(f"remainder.__doc__ starts with: {remainder.__doc__.strip().splitlines()[0]!r}")

    quotient, remainder_value = divide(1456, 33)
    print(f"divide(1456, 33) -> quotient={quotient}, remainder={remainder_value}")

    # timeout omitted -- falls back to the default of 300.
    print(f"connect('www.python.org', 80) = {connect('www.python.org', 80)}")

    # timeout supplied explicitly -- overrides the default.
    print(f"connect('www.python.org', 80, 60) = {connect('www.python.org', 80, 60)}")

    # Keyword arguments: naming each parameter lets them be passed in
    # any order, not just positionally.
    print(f"connect(port=80, hostname='www.python.org') = "
          f"{connect(port=80, hostname='www.python.org')}")

    print(f"read_data('data.csv') = {read_data('data.csv')!r}")
