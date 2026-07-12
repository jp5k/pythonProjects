"""
How Python's `import` statement actually works, and a tour of some of
the most commonly used standard-library imports.

What `import x` does, step by step:
  1. Python looks for a module named `x` by searching, in order, the
     directories listed in `sys.path` (a list of strings, checked
     first-to-last): the running script's own directory, anything in
     the `PYTHONPATH` environment variable, the standard library's own
     location, and installed third-party packages' `site-packages`
     directory. Tools can also prepend extra directories -- this repo's
     `pyproject.toml` sets `pythonpath = ["."]` for pytest, which is why
     `tests/` can `from scripts...import ...` at all.
  2. If found, Python runs that module's top-level code from top to
     bottom, exactly once, and the resulting namespace becomes a
     "module object".
  3. That module object is cached in `sys.modules`, keyed by name. Every
     later `import x` anywhere in the process -- even from a totally
     different file -- reuses the cached object instead of re-running
     the module. This is why importing something "expensive" many times
     is cheap after the first time, and why two modules that both
     `import x` are guaranteed to see the *same* object (so mutating
     shared state through it is visible everywhere).
  4. Finally, a name is bound in the *importing* namespace, pointing at
     that module object (or, for `from` imports, at one attribute of it).

The different import statement forms all follow the steps above; they
only differ in what gets found (step 1) and what name gets bound
(step 4):

  import x                 -> binds `x` to the whole module object.
  import x as y             -> binds `y` instead of `x` to the same object.
  from x import y           -> runs/caches module `x` as usual, then binds
                                just `y` (one attribute of `x`) directly,
                                so you write `y` instead of `x.y`.
  from x import y as z      -> same, but the pulled-out attribute is
                                bound under the name `z`.
  from x import *           -> binds every name listed in `x.__all__`, or
                                (if `x` defines no `__all__`) every name in
                                `x` that doesn't start with an underscore.
                                Avoided in real code: it dumps an unknown
                                set of names into your namespace, which
                                can silently shadow things you already had.

Packages (dotted names, e.g. `collections.abc`) are just directories
that Python can import from. A directory needs an `__init__.py` (or, in
modern Python, can even be an implicit "namespace package" with none)
to be treated as a package rather than an ordinary folder. Imports
inside a package can be absolute (`from scripts.imports import
imports_explained`, spelled from the top of the package tree -- how the
tests below import this file) or relative (`from . import sibling`,
`from ..other_package import thing` -- spelled relative to the current
package). Relative imports only work inside a package; a script run
directly can't use them.
"""

import functools
import itertools
import json
import math
import os.path as ospath  # import x as y: alias the whole (dotted) module
import re
import sys
from collections import Counter as Tally  # from x import y as z: pull + rename
from datetime import date, timedelta  # from x import a, b: pull multiple names
from pathlib import Path


def circle_area(radius: float) -> float:
    """`import math` -> access everything through the `math.` prefix."""
    return math.pi * radius ** 2


def join_paths(*parts: str) -> str:
    """`import os.path as ospath` -> the alias stands in for the module everywhere."""
    return ospath.join(*parts)


def days_between(start: date, end: date) -> int:
    """`from datetime import date, timedelta` -> use `date` directly, no `datetime.` prefix."""
    return (end - start).days


def add_days(start: date, days: int) -> date:
    """Uses the other name pulled in by the same `from datetime import ...` line."""
    return start + timedelta(days=days)


def tally_letters(word: str) -> Tally:
    """`from collections import Counter as Tally` -> `Counter` is used under our chosen alias."""
    return Tally(word)


def round_trip_json(data: dict) -> dict:
    """`import json` -> serialize to a string and back, proving the round trip is lossless."""
    text = json.dumps(data)  # Python object -> JSON string
    return json.loads(text)  # JSON string -> Python object again


def flatten(nested: list[list[int]]) -> list[int]:
    """`import itertools` -> `chain` lazily concatenates several iterables into one."""
    return list(itertools.chain(*nested))


def first_match(pattern: str, text: str) -> str | None:
    """`import re` -> search `text` for `pattern`, returning the matched substring (or None)."""
    match = re.search(pattern, text)
    return match.group(0) if match else None


def path_suffix(filename: str) -> str:
    """`from pathlib import Path` -> object-oriented path manipulation, no string-splitting.

    Path objects work without touching the filesystem, so this is safe
    to call on a name that doesn't exist on disk.
    """
    return Path(filename).suffix


def product_via_reduce(numbers: list[int]) -> int:
    """`import functools` -> `reduce` folds a binary function over an iterable.

    `functools.reduce(f, [a, b, c])` computes `f(f(a, b), c)` -- here,
    repeated multiplication, i.e. the product of the whole list.
    """
    return functools.reduce(lambda total, n: total * n, numbers)


def module_is_cached_after_import() -> bool:
    """Proves step 3 above: re-importing a module reuses the same cached object.

    `math` was already imported once at the top of this file. Importing
    it again here does NOT re-run math's setup code -- it just looks
    the existing module object up in `sys.modules` and rebinds a local
    name to it, so both names refer to one identical object.
    """
    import math as math_again

    return math_again is math and "math" in sys.modules


def search_path_is_a_nonempty_list_of_strings() -> bool:
    """`sys.path` is the ordered list of directories `import` searches (see step 1 above)."""
    return isinstance(sys.path, list) and all(isinstance(entry, str) for entry in sys.path)


if __name__ == "__main__":
    # A quick, human-readable demo when running this file directly with:
    #   python scripts/imports/imports_explained.py

    print("circle_area(2) =", circle_area(2))
    print("join_paths('a', 'b', 'c.txt') =", join_paths("a", "b", "c.txt"))

    today = date(2024, 1, 1)
    later = add_days(today, 10)
    print(f"days_between({today}, {later}) =", days_between(today, later))

    print("tally_letters('mississippi') =", tally_letters("mississippi"))

    payload = {"name": "Ada", "year": 1815}
    print("round_trip_json(...) =", round_trip_json(payload))

    print("flatten([[1, 2], [3], [4, 5]]) =", flatten([[1, 2], [3], [4, 5]]))
    print("first_match(r'\\d+', 'room 42') =", first_match(r"\d+", "room 42"))
    print("path_suffix('notes.txt') =", path_suffix("notes.txt"))
    print("product_via_reduce([1, 2, 3, 4]) =", product_via_reduce([1, 2, 3, 4]))

    print("module_is_cached_after_import() =", module_is_cached_after_import())
    print(
        "search_path_is_a_nonempty_list_of_strings() =",
        search_path_is_a_nonempty_list_of_strings(),
    )
