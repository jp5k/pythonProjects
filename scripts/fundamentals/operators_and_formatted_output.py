"""
Operators and Formatted Output

Covers printf-style string formatting with f-strings, floor (truncating)
division with //, and the walrus operator (:=) for assigning inside an
expression.
"""


def printf_function():
    year = 2026
    principal = 5014.888

    # This uses the print 'f' built in Python print command,
    # to pad out the year and keep to 2 decimal places.
    print(f"{year:>3d} {principal:0.2f}")


def floor_divide(x, y):
    # `//` is floor (truncating) division: it divides x by y and rounds
    # the result *down* to the nearest whole number, discarding the
    # remainder entirely. This differs from `/`, which always returns a
    # float with the remainder kept as a decimal.
    return x // y


def count_up_with_walrus(limit):
    values = []
    x = 0

    # `:=` is the "walrus operator" — it assigns to a name *and* evaluates
    # to that value in the same expression. Here it lets the while loop
    # both increment x and test the new value in one line, instead of
    # needing a separate `x = x + 1` statement above the loop condition.
    while (x := x + 1) < limit:
        values.append(x)

    return values


if __name__ == "__main__":
    # A quick, human-readable demo when running this file directly with:
    #   python scripts/fundamentals/operators_and_formatted_output.py
    printf_function()

    # 7 / 2 is 3.5, but floor division truncates down to 3.
    result = floor_divide(7, 2)
    print(f"7 // 2 = {result}")

    # Prints 1 through 9 — the walrus operator assigns x on every
    # iteration and the loop stops as soon as x reaches 10.
    numbers = count_up_with_walrus(10)
    print(f"count_up_with_walrus(10) = {numbers}")
