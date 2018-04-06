import os
import subprocess


__all__ = ['__location__', '__version__']


def is_git_repo(dir):
    return os.path.exists(os.path.join(dir, ".git"))


def is_dirty():
    base = os.path.dirname(__location__)
    if not is_git_repo(base):
        return False

    try:
        out = subprocess.check_output(["git", "status", "--porcelain"], cwd=base)
        return bool(out.strip())

    except (subprocess.CalledProcessError, OSError):
        return False


def git_revision():
    base = os.path.dirname(__location__)
    if not is_git_repo(base):
        return ""

    try:
        out = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=base)
        return out.strip().decode("utf8")

    except (subprocess.CalledProcessError, OSError):
        return ""


def maybe_git_local():
    """Append PEP 440-compliant local version identifier."""
    result = ""
    git_rev = git_revision()
    if git_rev:
        result += "+" + git_rev
        if is_dirty():
            result += ".dirty"
    return result


try:
    import pkg_resources
except ImportError:
    __location__ = os.path.dirname(os.path.dirname(__file__))
else:
    __location__ = pkg_resources.resource_filename("typeshed", "")
__version__ = "18.4.0" + maybe_git_local()


# Deprecated name kept for backwards compatibility.
typeshed = __location__
