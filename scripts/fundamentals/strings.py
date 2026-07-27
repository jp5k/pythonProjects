"""
Strings

Covers the basics of Python's str type: how to write string literals,
how to measure and index into them, slicing, and some of the most
common built-in string methods (replace, strip, upper), concatenation,
converting strings to numbers, and the repr() built-in.
"""


def quoting_styles():
    # Single and double quotes are interchangeable in Python — pick
    # whichever lets you avoid escaping a quote character inside the
    # string itself.
    single = 'hello'
    double = "hello"

    # Triple quotes (''' or \"\"\") start a string that can span several
    # lines without needing an explicit newline character (\n). They're
    # handy for multi-line text, and also for docstrings like the one at
    # the top of this file.
    triple = """This string
spans
multiple lines."""

    return single, double, triple


def string_length(s):
    # len() works on any sequence, and a string is a sequence of
    # characters, so it returns the character count.
    return len(s)


def character_at_index(s, index):
    # Strings are indexed like lists: s[0] is the first character.
    # Indexing returns a single-character string, not a special "char"
    # type — Python doesn't have one.
    return s[index]


def slicing_examples(s):
    # Slicing uses s[start:stop:step]. All three parts are optional and
    # the stop index is *exclusive* (not included in the result).
    first_five = s[:5]        # from the start up to (not including) index 5
    from_five = s[5:]         # from index 5 to the end
    middle = s[2:7]           # from index 2 up to (not including) index 7
    last_three = s[-3:]       # negative indices count from the end
    every_other = s[::2]      # step of 2: every second character
    reversed_s = s[::-1]      # a step of -1 walks the string backwards

    return first_five, from_five, middle, last_three, every_other, reversed_s


def replace_substring(s, old, new):
    # replace() returns a *new* string with every occurrence of `old`
    # swapped for `new` — strings are immutable, so the original is
    # never modified in place.
    return s.replace(old, new)


def strip_whitespace(s):
    # strip() removes leading and trailing whitespace (spaces, tabs,
    # newlines) by default. It does not touch whitespace in the middle
    # of the string.
    return s.strip()


def upper_case(s):
    # upper() returns a new string with every letter converted to
    # uppercase; non-letter characters are left unchanged.
    return s.upper()


def concatenate(a, b):
    # `+` joins two strings end to end into a new string. Both operands
    # must already be strings — Python won't silently convert numbers.
    return a + b


def string_to_int_before_math(s, amount):
    # Values read from input(), files, or user forms usually arrive as
    # strings, even if they "look like" numbers. int() must be used to
    # convert the string to an integer before it can take part in
    # arithmetic — "5" + 1 raises a TypeError, but int("5") + 1 works.
    return int(s) + amount


def show_repr(value):
    # repr() returns a string showing the value in a form useful for
    # debugging: for strings, that means the quotes are included, so
    # you can see at a glance both what the value is and that it's a
    # string (e.g. repr("5") -> "'5'" vs repr(5) -> '5').
    return repr(value)


if __name__ == "__main__":
    # A quick, human-readable demo when running this file directly with:
    #   python scripts/fundamentals/strings.py
    single, double, triple = quoting_styles()
    print(f"single={single!r} double={double!r}")
    print(f"triple={triple!r}")

    a = "hello world"
    print(f"len({a!r}) = {string_length(a)}")

    d = a[4]
    print(f"a[4] = {d!r}")

    c = a[:5]
    print(f"a[:5] = {c!r}")
    print(f"slicing_examples(a) = {slicing_examples(a)}")

    print(f"replace: {replace_substring(a, 'world', 'there')!r}")

    padded = "   trim me   "
    print(f"strip: {strip_whitespace(padded)!r}")

    print(f"upper: {upper_case(a)!r}")

    print(f"concatenate: {concatenate('foo', 'bar')!r}")

    total = string_to_int_before_math("5", 10)
    print(f"string_to_int_before_math('5', 10) = {total}")

    # repr(s) is useful for showing info about a value AND its type at
    # a glance — a string comes back quoted, an int doesn't.
    print(f"show_repr('5') = {show_repr('5')}")
    print(f"show_repr(5) = {show_repr(5)}")
