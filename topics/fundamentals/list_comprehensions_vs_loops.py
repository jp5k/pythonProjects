"""
List comprehensions vs. for loops.

Python offers two common ways to build a new list from an existing
iterable: a traditional `for` loop, and a list comprehension. This
script shows the same piece of logic written both ways, so you can
compare them directly.

Key idea: a list comprehension is just a compact `for` loop that
builds a list. Anything you can write as one, you can write as the
other — comprehensions are a style choice (and often faster/more
readable for simple transformations), not a different capability.
"""


def squares_with_loop(numbers):
    """Return the square of each number, built with an explicit for loop."""
    # Step 1: start with an empty list to collect results.
    result = []
    # Step 2: walk through each number one at a time.
    for number in numbers:
        # Step 3: compute the square and append it to the result list.
        result.append(number ** 2)
    # Step 4: return the fully built list.
    return result


def squares_with_comprehension(numbers):
    """Return the square of each number, built with a list comprehension."""
    # This single line does exactly what squares_with_loop does above:
    #   - "for number in numbers"   -> iterate, same as the for loop
    #   - "number ** 2"             -> the expression evaluated each time
    #   - the surrounding [ ... ]   -> collect each result into a new list
    return [number ** 2 for number in numbers]


def even_numbers_with_loop(numbers):
    """Return only the even numbers, built with an explicit for loop and an if check."""
    result = []
    for number in numbers:
        # Only keep the number if it divides evenly by 2 (no remainder).
        if number % 2 == 0:
            result.append(number)
    return result


def even_numbers_with_comprehension(numbers):
    """Return only the even numbers, built with a list comprehension and a filter clause."""
    # The trailing "if number % 2 == 0" filters out odd numbers before
    # they're added to the list — comprehensions support filtering,
    # not just transforming.
    return [number for number in numbers if number % 2 == 0]


if __name__ == "__main__":
    # A quick, human-readable demo when running this file directly with:
    #   python topics/fundamentals/list_comprehensions_vs_loops.py
    sample = [1, 2, 3, 4, 5, 6]

    print("Input:", sample)
    print("Squares (loop):          ", squares_with_loop(sample))
    print("Squares (comprehension): ", squares_with_comprehension(sample))
    print("Evens (loop):            ", even_numbers_with_loop(sample))
    print("Evens (comprehension):   ", even_numbers_with_comprehension(sample))
