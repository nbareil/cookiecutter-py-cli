# cookiecutter-py-cli

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a
Python command-line tool built with [click](https://click.palletsprojects.com/)
and managed with [uv](https://docs.astral.sh/uv/).

## Usage

```bash
uvx cookiecutter gh:nbareil/cookiecutter-py-cli
cd <project-slug>
git init
make dev
```

`make dev` creates the virtual environment, writes `uv.lock`, and installs the
git hooks, so it needs the git repository to exist first.

## What you get

- `src/` layout, built with `uv_build`.
- A click command group with `--version` and an example `hello` subcommand,
  also runnable as `python -m <module>`.
- ruff for formatting and linting (all rules enabled), ty for type checking.
- pytest with 100% branch coverage enforced, starting with `CliRunner` tests.
- A `Makefile` with `dev`, `run`, `format`, `lint`, `test`, `audit` and
  `build` targets.
- [prek](https://github.com/j178/prek) hooks: format and lint on commit,
  tests on push.

## Variables

| Variable              | Default                        | Used for                          |
| --------------------- | ------------------------------ | --------------------------------- |
| `project_name`        | `Python CLI`                   | Human-readable name in docs       |
| `project_slug`        | `project_name`, dash-separated | Directory and distribution name   |
| `entry_point`         | `project_slug`                 | Installed command name            |
| `project_description` | empty                          | `pyproject.toml` and `--help`     |

The import name is `project_slug` with dashes replaced by underscores.
Generation stops if `project_slug` or `entry_point` isn't lowercase letters,
digits and dashes, starting with a letter.
