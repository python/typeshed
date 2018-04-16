import os
import subprocess


__all__ = ['__location__', '__version__']


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


def git_revision():
    # type: () -> str
    base = os.path.dirname(__location__)
    if not is_git_repo(base):
        return ""

    try:
        out = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=base)
        return out.strip().decode("utf8")

    except (subprocess.CalledProcessError, OSError):
        return ""


try:
    import pkg_resources
except ImportError:
    __location__ = os.path.dirname(os.path.dirname(__file__))
else:
    __location__ = pkg_resources.resource_filename("typeshed", "")
__version__ = "18.4.0"


# Deprecated name kept for backwards compatibility.
typeshed = __location__
