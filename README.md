# cookiecutter-py-cli

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a
Python command-line tool built with [click](https://click.palletsprojects.com/),
or a plain library, managed with [uv](https://docs.astral.sh/uv/).

## Usage

```bash
uvx cookiecutter gh:nbareil/cookiecutter-py-cli
cd <project-slug>
git init
make dev
```

Pick `CLI` or `library` at the `repo_type` prompt, or pass
`repo_type=library` on the command line.

`make dev` creates the virtual environment, writes `uv.lock`, and installs the
git hooks, so it needs the git repository to exist first.

## What you get

Both project types get:

- `src/` layout, built with `uv_build`, with `__version__` read from the
  package metadata and a `py.typed` marker.
- ruff for formatting and linting (all rules enabled), ty for type checking.
- pytest with 100% branch coverage enforced.
- A `Makefile` with `dev`, `format`, `lint`, `test`, `audit` and `build`
  targets.
- [prek](https://github.com/j178/prek) hooks: format and lint on commit,
  tests on push.

A `CLI` project also gets:

- A click command group with `--version` and an example `hello` subcommand,
  also runnable as `python -m <module>`, tested with `CliRunner`.
- An installed command named after `entry_point`, and a `make run` target.

## Variables

| Variable              | Default                        | Used for                          |
| --------------------- | ------------------------------ | --------------------------------- |
| `project_name`        | `Python Project`               | Human-readable name in docs       |
| `project_slug`        | `project_name`, dash-separated | Directory and distribution name   |
| `repo_type`           | `CLI`                          | `CLI` or `library`                |
| `entry_point`         | `project_slug` (CLI only)      | Installed command name            |
| `project_description` | empty                          | `pyproject.toml` and `--help`     |

The import name is `project_slug` with dashes replaced by underscores.
Generation stops if `project_slug`, or `entry_point` for a CLI, isn't
lowercase letters, digits and dashes, starting with a letter. A library
ignores `entry_point`.
