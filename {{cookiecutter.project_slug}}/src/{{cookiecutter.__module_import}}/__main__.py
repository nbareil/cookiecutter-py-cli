"""Entry point for `python -m {{ cookiecutter.__module_import }}`."""

if __name__ == "__main__":
    from {{ cookiecutter.__module_import }}._cli import main

    main()
