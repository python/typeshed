"""Utilities for setup.py to understand the state of the repository."""

import os
import subprocess

from typeshed import __location__


def is_git_repo(dir):
    # type: () -> bool
    return os.path.exists(os.path.join(dir, ".git"))


def is_dirty():
    # type: () -> bool
    base = os.path.dirname(__location__)
    if not is_git_repo(base):
        return False

    try:
        out = subprocess.check_output(["git", "status", "--porcelain"], cwd=base)
        return bool(out.strip())

    except (subprocess.CalledProcessError, OSError):
        return False


def get_revision():
    # type: () -> str
    base = os.path.dirname(__location__)
    if not is_git_repo(base):
        return ""

    try:
        out = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=base)
        return out.strip().decode("utf8")

    except (subprocess.CalledProcessError, OSError):
        return ""
