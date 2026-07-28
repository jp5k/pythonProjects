"""
Sets

Covers the basics of Python's set type: an unordered collection of
unique, (usually) immutable objects, used to find distinct values or
answer membership questions. Covers the two ways to build a set from a
literal, building one from existing data with a set comprehension, the
empty set, the union/intersection/difference/symmetric-difference
operators, growing a set with add() and update(), and the difference
between remove() and discard() when the item being removed isn't
there.
"""


def create_set_literal():
    # {..} with comma-separated items is a set literal -- similar to a
    # list literal, but with curly braces instead of square brackets.
    # Duplicates collapse to a single entry: even though 'IBM' is
    # written twice below, the resulting set holds it only once.
    return {"IBM", "MSFT", "AA", "IBM"}


def create_set_constructor():
    # set() converts any iterable into a set, discarding duplicates
    # along the way. Passing it a list, as here, works the same way
    # list() converts an iterable into a list.
    return set(["IBM", "MSFT", "HPE", "IBM", "CAT"])


def create_empty_set():
    # {} is NOT an empty set -- it's an empty dict, since dicts got the
    # curly-brace literal syntax first. set() is the only way to write
    # an empty set.
    return set()


def stock_names_from_portfolio(portfolio):
    # {expression for item in iterable} is a *set comprehension* -- the
    # set equivalent of a list comprehension. Given a portfolio of
    # (name, shares, price) tuples, as built up in tuples.py, this
    # pulls out just the names and folds out any repeats -- e.g. two
    # separate GOOG holdings collapse into a single 'GOOG' entry.
    return {name for name, shares, price in portfolio}


def set_union(a, b):
    # `|` returns a new set containing every item that's in `a`, in
    # `b`, or in both -- i.e. everything, with overlap counted once.
    return a | b


def set_intersection(a, b):
    # `&` returns a new set containing only the items that appear in
    # BOTH `a` and `b`.
    return a & b


def set_difference(a, b):
    # `-` returns a new set containing the items in `a` that are NOT
    # also in `b`. It's not symmetric: a - b and b - a are generally
    # different sets.
    return a - b


def set_symmetric_difference(a, b):
    # `^` returns a new set containing the items that are in exactly
    # one of `a` or `b`, but not both -- the opposite of intersection.
    # It's equivalent to (a | b) - (a & b).
    return a ^ b


def add_single_item(names, item):
    # add() puts one new item into the set, in place, and returns
    # None -- much like list.append(). If the item is already present,
    # add() is a no-op: sets never hold duplicates.
    names.add(item)
    return names


def add_multiple_items(names, items):
    # update() merges every item from another iterable into the set,
    # in place. It's the set equivalent of list.extend() -- one call
    # to add several items at once instead of calling add() repeatedly.
    names.update(items)
    return names


def remove_existing_item(names, item):
    # remove() deletes `item` from the set in place. If `item` isn't
    # present, it raises KeyError -- remove() expects the item to be
    # there, so a missing item is treated as a bug worth surfacing.
    names.remove(item)
    return names


def discard_item(names, item):
    # discard() also deletes `item` from the set in place, but it's
    # silent if `item` isn't present -- no exception is raised. Use
    # discard() when "already gone" is a fine outcome, and remove()
    # when you want to be told if your assumption about what's in the
    # set was wrong.
    names.discard(item)
    return names


if __name__ == "__main__":
    # A quick, human-readable demo when running this file directly with:
    #   python scripts/fundamentals/sets.py
    names1 = create_set_literal()
    print(f"create_set_literal() = {names1}")

    names2 = create_set_constructor()
    print(f"create_set_constructor() = {names2}")
    # Only one 'IBM' survives, even though the source list had it twice.
    print(f"'IBM' appears once in names2, despite the source list having it twice")

    print(f"create_empty_set() = {create_empty_set()!r}")

    # Reuse the portfolio-of-tuples shape from tuples.py, with a
    # repeated GOOG holding to show the comprehension folding it away.
    portfolio = [
        ("GOOG", 100, 490.10),
        ("AAPL", 50, 91.10),
        ("IBM", 75, 145.87),
        ("GOOG", 25, 490.10),
    ]
    names = stock_names_from_portfolio(portfolio)
    print(f"stock_names_from_portfolio(portfolio) = {names}")

    t = {"IBM", "MSFT", "AA"}
    s = {"IBM", "MSFT", "HPE", "CAT"}
    print(f"t = {t}")
    print(f"s = {s}")
    print(f"set_union(t, s) = t | s = {set_union(t, s)}")
    print(f"set_intersection(t, s) = t & s = {set_intersection(t, s)}")
    print(f"set_difference(t, s) = t - s = {set_difference(t, s)}")
    print(f"set_difference(s, t) = s - t = {set_difference(s, t)}")
    print(f"set_symmetric_difference(t, s) = t ^ s = {set_symmetric_difference(t, s)}")

    add_single_item(t, "DIS")
    print(f"after add_single_item(t, 'DIS'): {t}")

    add_multiple_items(s, {"JJ", "GE", "ACME"})
    print(f"after add_multiple_items(s, {{'JJ', 'GE', 'ACME'}}): {s}")

    remove_existing_item(t, "IBM")
    print(f"after remove_existing_item(t, 'IBM'): {t}")

    discard_item(s, "SCOX")
    print(f"after discard_item(s, 'SCOX') (not present, no error): {s}")

    try:
        remove_existing_item(t, "SCOX")
    except KeyError as exc:
        print(f"remove_existing_item(t, 'SCOX') raised: {exc!r}")
