import re
import sys

NAME_REGEX = r"[a-z][-a-z0-9]*[a-z0-9]"

checks = [("project_slug", "{{ cookiecutter.project_slug }}")]
if "{{ cookiecutter.repo_type }}" == "CLI":
    checks.append(("entry_point", "{{ cookiecutter.entry_point }}"))

for variable, value in checks:
    if not re.fullmatch(NAME_REGEX, value):
        sys.exit(f"ERROR: {variable} {value!r} must match {NAME_REGEX!r}")
