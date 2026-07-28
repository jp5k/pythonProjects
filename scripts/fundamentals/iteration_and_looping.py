"""
Iteration and looping.

Covers Python's `for` statement, the main tool for walking through a
sequence of values one at a time. Starts with the most explicit form --
looping over a list literal typed out by hand -- then shows range() as
a shortcut for producing a sequence of numbers without typing them all
out. Covers range()'s three call signatures: stop-only (starting at 0,
counting by 1), start-and-stop, and start-stop-step (including a
negative step, which counts downward). Finishes by showing that the
same `for` statement works unchanged over several different kinds of
iterable -- a string (character by character), a list, a dict (via
.items()), and an open file (line by line) -- which is the point of
`for`: it doesn't care what kind of iterable you hand it, only that it
can be walked.
"""

import tempfile
from pathlib import Path


def powers_of_two_with_list_literal():
    """Print powers of two by looping over a list literal typed out by hand."""
    lines = []
    # [1, 2, 3, ...] is a list literal -- every value it will produce is
    # spelled out explicitly. That's fine for nine values, but doesn't
    # scale: looping over the first thousand powers of two would mean
    # typing a thousand numbers into the list.
    for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        lines.append(f"2 to the {n} power is {2 ** n}")
    return lines


def powers_of_two_with_range():
    """The same powers of two, looping over range(1, 10) instead."""
    lines = []
    # range(1, 10) produces the numbers 1 through 9 -- the stop value
    # (10) is exclusive, so it's never itself produced. range() doesn't
    # build a list in memory; it generates each number on demand as the
    # loop asks for it, which is what makes it scale to ranges far
    # bigger than you'd want to type out as a literal.
    for n in range(1, 10):
        lines.append(f"2 to the {n} power is {2 ** n}")
    return lines


def range_stop_only(stop):
    """range(stop): counts from 0 up to (but not including) stop, step 1."""
    # With a single argument, range() assumes start=0 and step=1 -- the
    # most common case, e.g. range(5) -> 0, 1, 2, 3, 4.
    return list(range(stop))


def range_start_stop(start, stop):
    """range(start, stop): counts from start up to (but not including) stop."""
    # A second argument overrides the default start of 0, e.g.
    # range(1, 8) -> 1, 2, 3, 4, 5, 6, 7. The step is still 1.
    return list(range(start, stop))


def range_start_stop_step(start, stop, step):
    """range(start, stop, step): counts by `step` instead of by 1 each time.

    A negative step counts downward instead of upward -- in that case
    `start` must be greater than `stop` for range() to produce anything,
    since it's now counting down toward (but not including) stop.
    """
    # e.g. range(0, 14, 3) -> 0, 3, 6, 9, 12 (skips by 3, stops before 14)
    # e.g. range(8, 1, -1) -> 8, 7, 6, 5, 4, 3, 2 (counts down, stops before 1)
    return list(range(start, stop, step))


def uppercase_each_character(text):
    """Loop over a string, which walks it one character at a time."""
    result = []
    # A `for` loop over a str doesn't need any special syntax -- a
    # string is an iterable of its own characters, just like a list is
    # an iterable of its elements.
    for ch in text:
        result.append(ch.upper())
    return result


def bullet_list(items):
    """Loop over a list, formatting each element into a bullet line."""
    lines = []
    # Looping over a list hands you each element in order -- the same
    # `for x in ...` shape as looping over the string above, just with
    # a list instead.
    for item in items:
        lines.append(f"- {item}")
    return lines


def format_dict_entries(prices):
    """Loop over a dict's .items(), formatting each key/value pair."""
    lines = []
    # Looping directly over a dict (`for key in prices`) walks its keys
    # only. .items() instead yields (key, value) pairs, which the loop
    # unpacks into `symbol` and `price` in one step -- see
    # scripts/fundamentals/dictionaries.py for more on dict views.
    for symbol, price in prices.items():
        lines.append(f"{symbol}: {price}")
    return lines


def read_lines_stripped(path):
    """Loop over an open file, which walks it one line at a time."""
    lines = []
    # A file object is also just an iterable -- iterating over it hands
    # you one line at a time, without reading the whole file into
    # memory first. Each line still has its trailing "\n" attached,
    # which .strip() removes here.
    with open(path) as file:
        for line in file:
            lines.append(line.strip())
    return lines


if __name__ == "__main__":
    # A quick, human-readable demo when running this file directly with:
    #   python scripts/fundamentals/iteration_and_looping.py
    print("--- looping over a list literal ---")
    for line in powers_of_two_with_list_literal():
        print(line)

    print("\n--- the same thing, looping over range(1, 10) ---")
    for line in powers_of_two_with_range():
        print(line)

    print("\n--- range() call signatures ---")
    print(f"range_stop_only(5) = {range_stop_only(5)}")
    print(f"range_start_stop(1, 8) = {range_start_stop(1, 8)}")
    print(f"range_start_stop_step(0, 14, 3) = {range_start_stop_step(0, 14, 3)}")
    print(
        "range_start_stop_step(8, 1, -1) [negative step counts down] = "
        f"{range_start_stop_step(8, 1, -1)}"
    )

    print("\n--- looping over a string ---")
    print(f"uppercase_each_character('abc') = {uppercase_each_character('abc')}")

    print("\n--- looping over a list ---")
    for line in bullet_list(["apples", "bananas", "cherries"]):
        print(line)

    print("\n--- looping over a dict ---")
    for line in format_dict_entries({"GOOG": 490.10, "IBM": 91.23}):
        print(line)

    print("\n--- looping over a file ---")
    with tempfile.TemporaryDirectory() as tmp_dir:
        data_path = Path(tmp_dir) / "data.txt"
        data_path.write_text("first line\nsecond line\nthird line\n")
        for line in read_lines_stripped(data_path):
            print(line)
