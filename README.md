# pythonProjects

A collection of Python code for learning, practicing, and understanding Python — scripts, exercises, and small projects.

## Structure

Scripts live under `scripts/<topic>/`, each with a descriptive name explaining what it teaches. Every script has a matching test under `tests/<topic>/`. See [CLAUDE.md](CLAUDE.md) for the full conventions.

## Setup

This project uses a Python **virtual environment** (`venv`) — an isolated copy of Python with its own private set of installed packages, kept separate from your system Python and from any other project. That isolation is what lets `requirements.txt` pin exact package versions for this repo without clashing with whatever other projects on your machine need.

One-time setup (creates `.venv/` and installs dependencies into it):

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

`.venv/` is excluded from git (see `.gitignore`) — it's local machine state, not something to commit.

Every time you open a new terminal to run scripts or tests, activate the environment first:

```
source .venv/bin/activate
pytest
python scripts/fundamentals/list_comprehensions_vs_loops.py
```

Activation just points `python`/`pytest` at the copies inside `.venv/` instead of the system ones. It only lasts for that terminal session — run `deactivate` to leave it, or just close the terminal.

If you're using VS Code, its Python extension usually detects `.venv/` automatically (or prompts you to select it via *Python: Select Interpreter*) and activates it for you in the integrated terminal and test runner, so manual activation often isn't needed there.
