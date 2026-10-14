import re
import sys

NAME_REGEX = r"[a-z][-a-z0-9]*[a-z0-9]"

for variable, value in [
    ("project_slug", "{{ cookiecutter.project_slug }}"),
    ("entry_point", "{{ cookiecutter.entry_point }}"),
]:
    if not re.fullmatch(NAME_REGEX, value):
        sys.exit(f"ERROR: {variable} {value!r} must match {NAME_REGEX!r}")
