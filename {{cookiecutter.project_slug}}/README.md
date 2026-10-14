# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Development

Requires [uv](https://docs.astral.sh/uv/).

```bash
make dev                # create the venv and install the git hooks
{%- if cookiecutter.repo_type == "CLI" %}
make run ARGS="hello"   # run {{ cookiecutter.entry_point }} with arguments
{%- endif %}
make format             # format and autofix
make lint               # ruff and ty
make test               # pytest with 100% branch coverage (ARGS="-k foo")
make audit              # check dependencies for known vulnerabilities
make build              # build the sdist and wheel into dist/
```
