"""
Demonstrates a common pattern for command-line scripts: let the same
program be run either interactively (it prompts for input) or
non-interactively (the caller passes the input as a command-line
argument), and reject anything else with a usage error.

This is the "readport.py" pattern from David Beazley's *Python
Distilled*: a script that prints a small stock portfolio read from a
CSV-style file.

    $ python interactive_or_argv_input.py
    Enter filename: portfolio.csv          # no argv extra -> prompts

    $ python interactive_or_argv_input.py portfolio.csv
                                            # one argv extra -> no prompt

    $ python interactive_or_argv_input.py a b c
    Usage: interactive_or_argv_input.py [filename]   # too many -> error

The key idea is that `main()` takes `argv` as a parameter instead of
reaching into `sys.argv` itself. That's what makes it possible to unit
test every branch (empty args, one arg, too many args) without ever
touching the real command line or blocking on real keyboard input.

Note on scaling up: hand-checking `len(argv)` like this is perfectly
fine for a simple script with a single optional positional argument --
it's transparent and needs no dependencies. But it doesn't scale. Once
a script needs multiple/optional flags, auto-generated `--help` text,
type conversion or validation, or subcommands, reach for the standard
library's `argparse` module instead of hand-rolling more
`len(argv)`/`sys.argv[n]` checks. A rough equivalent of this script's
argument handling in argparse would look like:

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="?")  # optional positional arg
    args = parser.parse_args(argv[1:])
    # args.filename is None if omitted -- argparse also gives you
    # --help output and a usage message for free, without the
    # `raise SystemExit(...)` branch below.
"""


def read_portfolio(filename):
    """Read a comma-separated ``name,shares,price`` file into tuples.

    Kept intentionally simple (manual ``str.split``) to mirror the rest
    of this repo's fundamentals scripts, which avoid the ``csv`` module
    so the parsing logic itself stays visible.
    """
    portfolio = []
    with open(filename, "r") as f:
        for line in f:
            name, shares, price = line.strip().split(",")
            portfolio.append((name.strip(), int(shares), float(price)))
    return portfolio


def main(argv):
    """Decide where the filename comes from, then print the portfolio.

    - ``len(argv) == 1`` means only the program name was given, so there
      is nothing to read from the command line -- fall back to asking
      interactively with ``input()``.
    - ``len(argv) == 2`` means one extra argument was given: treat it as
      the filename and skip the prompt entirely. This is what makes the
      script scriptable/automatable (e.g. from a shell pipeline or a
      cron job) instead of always requiring a human at the keyboard.
    - Anything else is a usage error. ``raise SystemExit(message)`` is
      the idiomatic way to abort a script with a clean, non-traceback
      error message and a non-zero exit code -- Python prints the
      message to stderr and exits, instead of dumping a full traceback.
    """
    if len(argv) == 1:
        filename = input("Enter filename: ")
    elif len(argv) == 2:
        filename = argv[1]
    else:
        raise SystemExit(f"Usage: {argv[0]} [filename]")

    portfolio = read_portfolio(filename)
    for name, shares, price in portfolio:
        print(f"{name:>10s} {shares:10d} {price:10.2f}")


if __name__ == "__main__":
    import sys

    main(sys.argv)
