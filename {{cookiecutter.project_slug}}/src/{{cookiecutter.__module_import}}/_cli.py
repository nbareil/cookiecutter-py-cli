"""Command-line interface for {{ cookiecutter.project_name }}."""

import click

from {{ cookiecutter.__module_import }} import __version__


@click.group()
@click.version_option(__version__)
def main() -> None:
    """{{ (cookiecutter.project_description or cookiecutter.project_name).rstrip('.') }}."""


@main.command()
@click.argument("name", default="world")
def hello(name: str) -> None:
    """Greet NAME."""
    click.echo(f"Hello, {name}!")
