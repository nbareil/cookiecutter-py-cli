from click.testing import CliRunner

from {{ cookiecutter.__module_import }} import __version__
from {{ cookiecutter.__module_import }}._cli import main


def test_version() -> None:
    result = CliRunner().invoke(main, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.output


def test_hello() -> None:
    result = CliRunner().invoke(main, ["hello", "Alice"])
    assert result.exit_code == 0
    assert result.output == "Hello, Alice!\n"
