.PHONY: dev{% if cookiecutter.repo_type == "CLI" %} run{% endif %} format lint test audit build

dev:
	uv sync
	uv run prek install
{%- if cookiecutter.repo_type == "CLI" %}

run:
	uv run {{ cookiecutter.entry_point }} $(ARGS)
{%- endif %}

format:
	uv run ruff format
	uv run ruff check --fix

lint:
	uv run ruff format --check
	uv run ruff check
	uv run ty check

test:
	uv run pytest $(ARGS)

audit:
	uv audit --preview-features audit-command

build:
	uv build
