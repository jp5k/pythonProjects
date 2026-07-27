"""
File input/output.

Covers the standard ways to read and write text files in Python:
line-by-line iteration, reading in fixed-size chunks, writing with
print(file=...) vs file.write(), opening a file with an explicit text
encoding, and reading a line typed interactively at the console with
input().

All of the read/write functions below take a `path` argument (rather
than a hardcoded filename) so they can be pointed at a temporary file
in tests instead of writing into the repo itself.
"""

import tempfile
from pathlib import Path


def read_line_by_line(path):
    """Read a file one line at a time, the most common way to walk a text file."""
    lines = []

    # `with open(path) as file` opens the file and guarantees it gets
    # closed again when the block exits, even if an error happens
    # inside it -- same guarantee `with` gives any context manager.
    with open(path) as file:
        # Iterating over a file object hands you one line at a time,
        # without loading the whole file into memory at once. Each
        # `line` still has its trailing "\n" attached (unless it's the
        # last line and the file doesn't end with one).
        for line in file:
            lines.append(line)

    return lines


def read_in_chunks(path, chunk_size=10000):
    """Read a file in fixed-size chunks instead of line by line.

    Useful for very large files, or files with no meaningful line
    structure (e.g. binary-ish data opened in text mode), where reading
    line by line either doesn't make sense or still pulls in one huge
    "line".
    """
    chunks = []

    with open(path) as file:
        # file.read(chunk_size) returns up to chunk_size characters and
        # advances the file's position; it returns '' once there's
        # nothing left to read. The walrus operator `:=` assigns that
        # result to `chunk` *and* lets the while condition test it in
        # one expression -- the loop stops the moment chunk is ''
        # (which is falsy).
        while chunk := file.read(chunk_size):
            chunks.append(chunk)

    return chunks


def write_compound_interest_with_print(path, principal, rate, numyears):
    """Write a compound-interest table to a file using print(..., file=out).

    print() normally writes to the console, but its `file` argument
    redirects that same output to any writable file object instead --
    including adding the trailing newline automatically, just like a
    normal print() call would on screen.
    """
    year = 1

    # 'wt' opens the file for writing in text mode. 'w' truncates the
    # file if it already exists (starts it empty) and creates it if it
    # doesn't; the explicit 't' just spells out "text mode", which is
    # also the default, so 'w' alone would behave identically.
    with open(path, "wt") as out:
        while year <= numyears:
            principal = principal * (1 + rate)
            print(f"{year:>3d} {principal:0.2f}", file=out)
            year += 1

    return principal


def write_compound_interest_with_write(path, principal, rate, numyears):
    """The same table as write_compound_interest_with_print, but using file.write().

    write() is lower-level than print(file=...): it writes exactly the
    string you give it and nothing else, so unlike print() it does NOT
    add a newline for you -- you have to include "\\n" yourself.
    """
    year = 1

    with open(path, "wt") as out:
        while year <= numyears:
            principal = principal * (1 + rate)
            out.write(f"{year:>3d} {principal:0.2f}\n")
            year += 1

    return principal


def read_with_encoding(path, encoding="utf-8"):
    """Open a file with an explicit text encoding.

    open() reads text using a default encoding decided by the
    operating system, which isn't always the encoding a file was
    actually written in -- especially for files containing non-ASCII
    characters (accents, currency symbols, emoji, etc). Passing
    `encoding=` explicitly makes the assumption visible and portable,
    instead of silently depending on whatever the OS happens to pick.
    """
    with open(path, encoding=encoding) as file:
        return file.read()


def read_console_input(prompt="Enter a value: "):
    """Read one line of text typed interactively at the console.

    input() prints `prompt`, then pauses the program until the user
    types something and presses Enter. It always returns a str (the
    trailing newline is stripped for you) -- so, like text read from a
    file, it needs converting (e.g. with int()) before it can be used
    in arithmetic.
    """
    return input(prompt)


if __name__ == "__main__":
    # A quick, human-readable demo when running this file directly with:
    #   python scripts/fundamentals/file_input_output.py
    #
    # Everything below runs against a temporary directory instead of
    # real files in the repo, and that directory is cleaned up
    # automatically when the `with` block ends.
    with tempfile.TemporaryDirectory() as tmp_dir:
        data_path = Path(tmp_dir) / "data.txt"
        out_path = Path(tmp_dir) / "out.txt"
        out2_path = Path(tmp_dir) / "out2.txt"

        data_path.write_text("first line\nsecond line\nthird line\n")

        print("--- reading line by line ---")
        for line in read_line_by_line(data_path):
            # Each `line` already ends in "\n", so end='' avoids
            # printing a second, blank-looking newline after it.
            print(line, end="")

        print("\n--- reading in chunks ---")
        for chunk in read_in_chunks(data_path, chunk_size=10):
            print(chunk, end="")

        print("\n\n--- writing with print(file=out) ---")
        final_principal = write_compound_interest_with_print(
            out_path, principal=1000.0, rate=0.05, numyears=5
        )
        print(out_path.read_text(), end="")
        print(f"final principal (print version) = {final_principal:0.2f}")

        print("\n--- writing with out.write() ---")
        final_principal2 = write_compound_interest_with_write(
            out2_path, principal=1000.0, rate=0.05, numyears=5
        )
        print(out2_path.read_text(), end="")
        print(f"final principal (write version) = {final_principal2:0.2f}")

        print("\n--- opening with an explicit encoding ---")
        encoded_path = Path(tmp_dir) / "encoded.txt"
        encoded_path.write_text("café ☃", encoding="utf-8")
        print(read_with_encoding(encoded_path, encoding="utf-8"))

        print("--- reading interactive console input ---")
        # This blocks and waits for real keyboard input when the file
        # is run directly -- comment it out if you're just skimming
        # the other demos above without wanting to type a response.
        typed = read_console_input("Type something and press Enter: ")
        print(f"you typed: {typed!r}")
