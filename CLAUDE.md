# pythonProjects

A collection of Python scripts for learning and reference. Each script teaches one concept; conventions below keep it useful for that purpose over time.

## Structure

```
topics/<topic>/<descriptive_name>.py     # the teaching script
tests/<topic>/test_<descriptive_name>.py # its test, same topic, mirrored path
```

## Conventions

- **Script names are descriptive**, not generic. The filename should say what it teaches, e.g. `list_comprehensions_vs_loops.py`, not `example1.py` or `test.py`.
- **Every script has a module-level docstring** at the top explaining the concept it demonstrates, so the file is useful as a standalone reference.
- **Every script gets a matching test file** in the mirrored `tests/<topic>/` path, named `test_<script_name>.py`. Do not add a script without a test — this is a hard requirement for this repo, not a suggestion.
- New concepts get their own topic folder under `topics/` (with a mirrored folder under `tests/`) when they don't fit an existing one.

## Running tests

From the repo root:

```
pytest
```

`pyproject.toml` sets `pythonpath = ["."]`, so tests import scripts as `from topics.<topic>.<script_name> import ...`.
