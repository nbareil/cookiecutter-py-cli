from {{ cookiecutter.__module_import }} import __version__


def test_version() -> None:
    assert __version__ == "{{ cookiecutter.version }}"
