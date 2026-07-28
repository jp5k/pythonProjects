"""
Dictionaries

Covers the basics of Python's dict type: a mutable mapping from keys to
values, used to look values up by name instead of by position. Covers
building a dict from a literal, reading and modifying entries with the
indexing operator, membership testing with the in operator, the get()
method for a lookup with a default, deleting an entry with del, and
using a tuple as a composite (multipart) key. Also covers tabulating
(grouping and summing) data with a dict comprehension, and doing the
same tabulation with collections.Counter. Also covers the two ways to
create an empty dict, building one from an iterable of key-value
pairs, and the three view methods -- keys(), values(), and items() --
used to iterate over a dict's contents.
"""

from collections import Counter


def create_stock_dict():
    # {key: value, ...} is a dict literal. Unlike a list or tuple,
    # a dict is indexed by these keys (here, strings) rather than by
    # position -- there's no "first" or "second" entry, just named ones.
    return {
        "name": "GOOG",
        "shares": 100,
        "price": 490.10,
    }


def get_name(s):
    # s['name'] looks up the value stored under the key 'name'. This is
    # the indexing operator, same syntax as list/tuple indexing, but
    # dicts use keys instead of integer positions.
    return s["name"]


def get_cost(s):
    # Multiple lookups can be combined in one expression, just like any
    # other values -- here, shares * price computes the position's cost.
    return s["shares"] * s["price"]


def update_shares(s, shares):
    # Assigning to an existing key, s['shares'] = ..., overwrites the
    # value stored there in place. The dict is mutated, not replaced.
    s["shares"] = shares
    return s


def add_date(s, date):
    # Assigning to a key that doesn't exist yet *inserts* a new
    # entry -- the same syntax handles both "modify" and "insert",
    # depending only on whether the key was already present.
    s["date"] = date
    return s


def price_lookup(prices, symbol):
    # prices[symbol] looks the symbol up directly. If `symbol` isn't a
    # key in the dict, this raises KeyError -- like list.remove(), a
    # plain lookup expects the key to be there.
    return prices[symbol]


def has_symbol(prices, symbol):
    # The `in` operator tests membership among the dict's KEYS (not its
    # values), returning True/False without raising. Checking `in`
    # before a plain lookup is one way to avoid a KeyError.
    return symbol in prices


def price_lookup_with_default(prices, symbol, default=0.0):
    # get() looks up `symbol` and returns its value if present, or
    # `default` if not -- no KeyError either way. It's the safe
    # alternative to prices[symbol] when a missing key is a normal,
    # expected outcome rather than a bug.
    return prices.get(symbol, default)


def remove_symbol(prices, symbol):
    # del prices[symbol] removes that key (and its value) from the
    # dict in place. Like remove(), it raises KeyError if the key isn't
    # there -- del expects the key to exist.
    del prices[symbol]
    return prices


def record_price_by_date(prices, symbol, date, price):
    # A dict key can be any hashable object, not just a string --
    # including a tuple. (symbol, date) bundles two values into a
    # single composite key, letting the same symbol have a different
    # price recorded for each date without the entries colliding.
    prices[(symbol, date)] = price
    return prices


def total_shares_by_dict_comprehension(portfolio):
    # { key: value for ... } is a *dict comprehension* -- the dict
    # equivalent of a list/set comprehension. This one seeds a running
    # total of 0 for every distinct name in the portfolio, in one line,
    # rather than needing an if/else inside the loop below to handle
    # "first time we've seen this name" vs. "seen it before".
    total_shares = {s[0]: 0 for s in portfolio}

    # With every name already present (and initialised to 0), the loop
    # itself only has to do the summing -- no need to check whether
    # `name` is already a key before adding to it.
    for name, shares, _ in portfolio:
        total_shares[name] += shares

    return total_shares


def total_shares_by_counter(portfolio):
    # Counter (from the collections module) is a dict subclass built
    # for exactly this kind of tallying. Its keys behave like a normal
    # dict's, but looking up a key that isn't there yet returns 0
    # instead of raising KeyError -- so total_shares[name] += shares
    # works immediately, with no comprehension needed to seed the
    # starting values first.
    total_shares = Counter()
    for name, shares, _ in portfolio:
        total_shares[name] += shares

    return total_shares


def create_empty_dict_literal():
    # {} creates an empty dict. This is the idiomatic way to write
    # one -- shorter than dict(), and consistent with how non-empty
    # dict literals are written.
    return {}


def create_empty_dict_constructor():
    # dict() also creates an empty dict, calling the type itself as a
    # constructor rather than using literal syntax. It's equivalent to
    # {}, just less idiomatic -- prefer {} in normal code.
    return dict()


def create_dict_from_pairs(pairs):
    # dict() can convert an iterable of (key, value) pairs -- here, a
    # list of 2-tuples -- directly into a dict, one entry per pair.
    # This is handy when the pairs already exist as data (e.g. loaded
    # from a file) rather than being typed out as a literal.
    return dict(pairs)


def keys_as_list(prices):
    # Iterating over a dict walks its keys by default, so wrapping it
    # in list() collects just the keys into an ordinary, independent
    # list -- a one-time snapshot that won't change if `prices` does.
    return list(prices)


def keys_view(prices):
    # dict.keys() returns the same keys, but as a *view* object rather
    # than a snapshot list. A view stays attached to the dict it came
    # from and updates live as the dict changes -- see the demo below,
    # where adding a key to the dict changes what the already-created
    # view reports, with no need to call keys() again.
    return prices.keys()


def values_view(prices):
    # dict.values() is the values() counterpart to keys() -- also a
    # live view, this time over the dict's values instead of its keys.
    return prices.values()


def format_price_lines(prices):
    # dict.items() yields (key, value) pairs together, so a single
    # loop can unpack both the symbol and its price at once, instead
    # of looping over keys() and then looking up prices[sym] for each.
    return [f"{sym} = {price}" for sym, price in prices.items()]


if __name__ == "__main__":
    # A quick, human-readable demo when running this file directly with:
    #   python scripts/fundamentals/dictionaries.py
    s = create_stock_dict()
    print(f"create_stock_dict() = {s}")

    print(f"get_name(s) = {get_name(s)!r}")
    print(f"get_cost(s) = {get_cost(s)}")

    update_shares(s, 75)
    print(f"after update_shares(s, 75): {s}")

    add_date(s, "2007-06-07")
    print(f"after add_date(s, '2007-06-07'): {s}")

    prices = {"GOOG": 490.10, "IBM": 91.23}
    print(f"prices = {prices}")

    print(f"price_lookup(prices, 'IBM') = {price_lookup(prices, 'IBM')}")

    print(f"has_symbol(prices, 'IBM') = {has_symbol(prices, 'IBM')}")
    print(f"has_symbol(prices, 'AAPL') = {has_symbol(prices, 'AAPL')}")

    print(
        "price_lookup_with_default(prices, 'AAPL') = "
        f"{price_lookup_with_default(prices, 'AAPL')}"
    )

    remove_symbol(prices, "GOOG")
    print(f"after remove_symbol(prices, 'GOOG'): {prices}")

    composite = {}
    record_price_by_date(composite, "IBM", "2015-02-03", 91.23)
    record_price_by_date(composite, "IBM", "2015-02-04", 91.42)
    print(f"after recording two dated prices for 'IBM': {composite}")
    print(
        "composite[('IBM', '2015-02-03')] = "
        f"{composite[('IBM', '2015-02-03')]}"
    )

    portfolio = [
        ("ACME", 50, 92.34),
        ("IBM", 75, 102.25),
        ("PHP", 40, 74.50),
        ("IBM", 50, 124.75),
    ]
    print(f"portfolio = {portfolio}")
    print(
        "total_shares_by_dict_comprehension(portfolio) = "
        f"{total_shares_by_dict_comprehension(portfolio)}"
    )
    print(
        "total_shares_by_counter(portfolio) = "
        f"{total_shares_by_counter(portfolio)}"
    )

    print(f"create_empty_dict_literal() = {create_empty_dict_literal()!r}")
    print(f"create_empty_dict_constructor() = {create_empty_dict_constructor()!r}")

    pairs = [("IBM", 125), ("ACME", 50), ("PHP", 40)]
    print(f"pairs = {pairs}")
    print(f"create_dict_from_pairs(pairs) = {create_dict_from_pairs(pairs)}")

    prices = {"AAPL": 645.57, "MSFT": 30.25, "IBM": 91.23, "GOOG": 490.10}
    print(f"prices = {prices}")
    print(f"keys_as_list(prices) = {keys_as_list(prices)}")

    view = keys_view(prices)
    print(f"keys_view(prices) = {view}")
    # Add a new key AFTER the view was created, without calling
    # keys_view() again -- the existing view still reflects it, since
    # it's a live window onto the dict rather than a frozen copy.
    prices["FB"] = 75.00
    print(f"after adding 'FB' to prices, the SAME view object now shows: {view}")

    print(f"values_view(prices) = {values_view(prices)}")

    print("format_price_lines(prices):")
    for line in format_price_lines(prices):
        print(f"  {line}")
