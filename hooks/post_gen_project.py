from pathlib import Path

if "{{ cookiecutter.repo_type }}" == "library":
    for path in [
        "src/{{ cookiecutter.__module_import }}/__main__.py",
        "src/{{ cookiecutter.__module_import }}/_cli.py",
        "test/test_cli.py",
    ]:
        Path(path).unlink()
