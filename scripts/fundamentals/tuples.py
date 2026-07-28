"""
Tuples

Covers the basics of Python's tuple type: creating a tuple, the special
syntax for 0-element and 1-element tuples, unpacking a tuple into named
variables, and why a tuple is best thought of as a single immutable
object made of several parts rather than a mutable collection like a
list. Finishes with the classic pattern of reading a file of comma
separated columns into a list of tuples -- one tuple per row -- and
then summing a column two ways: an explicit for loop that unpacks each
row, and a list comprehension that uses `_` to discard a field it
doesn't need.
"""


def create_holding():
    # A tuple literal is written with parentheses and comma-separated
    # items, e.g. a stock holding of (symbol, shares, price). Unlike a
    # list, a tuple is immutable -- once built, its items can't be
    # reassigned, grown, or removed.
    return ("GOOG", 100, 490.10)


def create_empty_tuple():
    # () is the 0-tuple: an empty tuple. It's the tuple equivalent of []
    # for lists.
    return ()


def create_one_element_tuple(item):
    # A single value in parentheses, like (item), is just `item` with
    # redundant parentheses around it -- NOT a tuple. The trailing comma
    # is what actually makes it a 1-element tuple: (item,). Leaving the
    # comma off is a common mistake, since (item) and (item,) look almost
    # identical but are different types.
    return (item,)


def unpack_holding(holding):
    # A tuple can be unpacked into a matching number of variables in one
    # statement. This reads much more clearly than repeated indexing
    # (holding[0], holding[1], holding[2]) when you already know the
    # tuple's shape.
    name, shares, price = holding
    return name, shares, price


def attempt_to_mutate_holding(holding):
    """Try to reassign an item of a tuple and return the TypeError it raises.

    A tuple is best viewed as a single immutable object with several
    parts -- like a record or a database row -- rather than as a
    collection of independent items the way a list is. Because of that,
    there's no equivalent of list's `names[0] = ...`: attempting it
    raises TypeError.
    """
    try:
        holding[0] = "MSFT"
    except TypeError as exc:
        return exc
    return None


def parse_portfolio_line(line):
    # A line of the form "name, shares, price" (as you'd find in a CSV
    # file) splits on the comma into a list of string fields. The
    # numeric fields still need converting -- split() never does that
    # for you -- before being packed into a tuple.
    row = line.split(",")
    name = row[0]
    shares = int(row[1])
    price = float(row[2])
    return (name, shares, price)


def load_portfolio_from_lines(lines):
    # Parsing every line and appending the resulting tuple builds up a
    # list of tuples -- one tuple per row. Printed, it looks like a 2D
    # array of rows and columns, but each row is a single immutable
    # tuple rather than a nested list.
    portfolio = []
    for line in lines:
        portfolio.append(parse_portfolio_line(line))
    return portfolio


def load_portfolio_from_file(path):
    # The same parsing, but reading rows from a real file one line at a
    # time instead of an in-memory list of lines -- this is the version
    # you'd actually use against a file like 'portfolio.csv'.
    portfolio = []
    with open(path) as file:
        for line in file:
            portfolio.append(parse_portfolio_line(line))
    return portfolio


def first_row(portfolio):
    # portfolio[0] reads the whole first tuple -- the whole row -- at
    # once.
    return portfolio[0]


def field_from_row(portfolio, row_index, field_index):
    # Chaining two indexes reaches into an individual field: the first
    # index picks the row (a tuple), the second picks a field within
    # that tuple. portfolio[1][1], for example, is the `shares` field of
    # the second row.
    return portfolio[row_index][field_index]


def total_value_with_loop(portfolio):
    # Unpacking directly in a for loop's target -- `for name, shares,
    # price in portfolio` -- unpacks each row's tuple on every
    # iteration, giving three named variables instead of one row tuple
    # to index into.
    total = 0.0
    for name, shares, price in portfolio:
        total += shares * price
    return total


def total_value_with_comprehension(portfolio):
    # The same loop-and-accumulate pattern as total_value_with_loop,
    # written as a list comprehension instead. `_` is the conventional
    # name for a value that's unpacked but never used -- here, each
    # row's `name`, since only shares and price are needed for the
    # total.
    return sum([shares * price for _, shares, price in portfolio])


if __name__ == "__main__":
    # A quick, human-readable demo when running this file directly with:
    #   python scripts/fundamentals/tuples.py
    holding = create_holding()
    print(f"create_holding() = {holding}")

    print(f"create_empty_tuple() = {create_empty_tuple()!r}")
    print(f"create_one_element_tuple('GOOG') = {create_one_element_tuple('GOOG')!r}")

    name, shares, price = unpack_holding(holding)
    print(f"unpack_holding(holding) -> name={name!r}, shares={shares!r}, price={price!r}")

    error = attempt_to_mutate_holding(holding)
    print(f"attempt_to_mutate_holding(holding) raised: {error!r}")

    # File containing lines of the form "name, shares, price", read here
    # from an in-memory list rather than a real 'portfolio.csv' so this
    # demo stays self-contained -- see file_input_output.py for reading
    # real files line by line.
    portfolio_lines = ["GOOG, 100, 490.10", "AAPL, 50, 91.10", "IBM, 75, 145.87"]
    portfolio = load_portfolio_from_lines(portfolio_lines)
    print(f"load_portfolio_from_lines(portfolio_lines) = {portfolio}")

    print(f"first_row(portfolio) = {first_row(portfolio)}")
    print(f"field_from_row(portfolio, 1, 1) = {field_from_row(portfolio, 1, 1)!r}")

    total_loop = total_value_with_loop(portfolio)
    print(f"total_value_with_loop(portfolio) = {total_loop:0.2f}")

    total_comprehension = total_value_with_comprehension(portfolio)
    print(f"total_value_with_comprehension(portfolio) = {total_comprehension:0.2f}")
