"""
Lists

Covers the basics of Python's list type: creating a list, reading and
modifying items by index (including negative indices), growing a list
with append() and insert(), iterating over a list with a for loop,
slicing (both to read a sub-list and to replace a run of items in
place), concatenating lists with +, the idiomatic ways to create an
empty list, building a list of characters from a string, and lists
that mix different types of Python objects (including nested lists).
Finishes with the classic "pcost.py" exercise, which turns raw text
lines into a list of lists and then reduces that list to a total with
a list comprehension.
"""


def create_list():
    # A list literal is written with square brackets and comma-separated
    # items. Unlike a string, a list is mutable — its items can be
    # changed, added, or removed after it's created.
    return ["Dave", "Paula", "Thomas", "Lewis"]


def access_by_index(names, index):
    # Lists are indexed like strings: 0 is the first item, 1 the
    # second, and so on.
    return names[index]


def access_last_item(names):
    # A negative index counts from the end: -1 is the last item, -2 the
    # second-to-last. This avoids needing to know len(names) - 1.
    return names[-1]


def modify_by_index(names, index, value):
    # Because lists are mutable, assigning to names[index] replaces that
    # item in place — this is the *same* list object, not a new one.
    names[index] = value
    return names


def append_item(names, item):
    # append() adds a single item to the end of the list, growing it by
    # one element. It modifies the list in place and returns None, so
    # you never write `names = names.append(...)`.
    names.append(item)
    return names


def insert_item(names, index, item):
    # insert(index, item) shifts everything from `index` onwards one
    # place to the right and puts `item` in the gap. Unlike append(),
    # it can add an item anywhere in the list, not just at the end.
    names.insert(index, item)
    return names


def iterate_list(names):
    # The most common way to visit every item in a list is a for loop.
    # `name` is rebound to each item in turn, in order.
    #
    #   for name in names:
    #       print(name)
    #
    # Real code just does something with each `name` inside the loop
    # (here, print). To keep this function testable it collects what it
    # saw into a new list rather than printing.
    seen = []
    for name in names:
        seen.append(name)
    return seen


def slice_list(names):
    # Slicing with [start:stop] returns a *new* list containing items
    # from `start` up to (not including) `stop`. Omitting `stop` slices
    # to the end of the list.
    first_two = names[0:2]
    from_index_two = names[2:]
    return first_two, from_index_two


def replace_slice(names, start, stop, replacement_items):
    # A slice can be assigned to, not just read. This replaces
    # names[start:stop] with the items in `replacement_items` — and the
    # replacement doesn't need to be the same length as the slice it
    # replaces, so this can grow or shrink the list.
    names[start:stop] = replacement_items
    return names


def concatenate_lists(a, b):
    # `+` joins two lists end to end into a new list, leaving both
    # original lists unchanged.
    return a + b


def create_empty_list_literal():
    # [] is the idiomatic way to create an empty list: it's shorter than
    # list() and, because it's a literal rather than a function call,
    # Python doesn't have to look up a name and call it.
    return []


def create_empty_list_constructor():
    # list() also creates an empty list. It's more useful for its other
    # job — converting an existing iterable (a string, tuple, etc.) into
    # a list, as in string_to_char_list() below — than as an empty-list
    # constructor.
    return list()


def string_to_char_list(s):
    # list() converts any iterable into a list of its elements. Since
    # iterating over a string yields its characters one at a time,
    # list("Dave") gives a list of single-character strings.
    return list(s)


def nested_list_access():
    # A list can hold a mix of types in one go — an int, a str, a
    # float, another list, all side by side.
    mixed = [1, "Dave", 3.14, ["Mark", 7, 9, [100, 101]], 10]

    # Chaining index lookups drills into nested lists one level at a
    # time: a[3] is the inner list, a[3][2] is the third item of that
    # inner list, and a[3][3] is the innermost list, so a[3][3][1] reads
    # its second item.
    second_item = mixed[1]
    third_item_of_nested_list = mixed[3][2]
    second_item_of_innermost_list = mixed[3][3][1]

    return mixed, second_item, third_item_of_nested_list, second_item_of_innermost_list


def parse_rows(lines):
    # A classic small exercise (often called "pcost.py") reads input
    # lines of the form 'NAME, SHARES, PRICE', for example:
    #
    #   SYM, 123, 456.78
    #
    # Splitting each line on the comma turns it from one string into a
    # list of fields, so building up `rows` line by line produces a
    # list of lists that looks like this:
    #
    #   [
    #     ['SYM', '123', '456.78'],
    #     ...
    #   ]
    rows = []
    for line in lines:
        rows.append(line.split(","))
    return rows


def total_portfolio_cost(rows):
    # [expression for row in rows] is a *list comprehension* — a
    # compact way to write the same "build a new list from an existing
    # one" pattern as a for loop, but as a single expression instead of
    # a loop with an explicit .append() call. Here the expression
    # converts each row's shares (index 1) and price (index 2) from
    # strings to numbers and multiplies them, giving a list of costs —
    # one per row — which sum() then adds together.
    costs = [int(row[1]) * float(row[2]) for row in rows]
    return sum(costs)


if __name__ == "__main__":
    # A quick, human-readable demo when running this file directly with:
    #   python scripts/fundamentals/lists.py
    names = create_list()
    print(f"create_list() = {names}")

    a = access_by_index(names, 2)
    print(f"names[2] = {a!r}")

    modify_by_index(names, 2, "Tom")
    print(f"after modify_by_index(names, 2, 'Tom'): {names}")
    print(f"access_last_item(names) = {access_last_item(names)!r}")

    append_item(names, "Alex")
    print(f"after append_item(names, 'Alex'): {names}")

    insert_item(names, 2, "Aya")
    print(f"after insert_item(names, 2, 'Aya'): {names}")

    print("iterating over names:")
    for name in names:
        print(f"  {name}")

    b, c = slice_list(names)
    print(f"slice_list(names) = {b}, {c}")

    modify_by_index(names, 1, "Becky")
    print(f"after modify_by_index(names, 1, 'Becky'): {names}")

    replace_slice(names, 0, 2, ["Dave", "Mark", "Jeff"])
    print(f"after replace_slice(names, 0, 2, [...]): {names}")

    concatenated = concatenate_lists(["x", "y"], ["z", "z", "y"])
    print(f"concatenate_lists(['x', 'y'], ['z', 'z', 'y']) = {concatenated}")

    print(f"create_empty_list_literal() = {create_empty_list_literal()!r}")
    print(f"create_empty_list_constructor() = {create_empty_list_constructor()!r}")

    letters = string_to_char_list("Dave")
    print(f"string_to_char_list('Dave') = {letters}")

    mixed, item1, item2, item3 = nested_list_access()
    print(f"nested_list_access() = {mixed}")
    print(f"  mixed[1] = {item1!r}")
    print(f"  mixed[3][2] = {item2!r}")
    print(f"  mixed[3][3][1] = {item3!r}")

    # In the original pcost.py exercise these lines come from a file
    # opened with open(sys.argv[1]) — see file_input_output.py for that
    # part. Here they're written out directly so this demo stays
    # self-contained and focused on what the lists are doing.
    portfolio_lines = ["SYM, 123, 456.78", "AAPL, 50, 91.10", "IBM, 75, 145.87"]
    rows = parse_rows(portfolio_lines)
    print(f"parse_rows(portfolio_lines) = {rows}")

    total = total_portfolio_cost(rows)
    print(f"total_portfolio_cost(rows) = {total:0.2f}")
