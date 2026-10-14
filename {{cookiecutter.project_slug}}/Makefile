.PHONY: dev run format lint test audit build

dev:
	uv sync
	uv run prek install

run:
	uv run {{ cookiecutter.entry_point }} $(ARGS)

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
