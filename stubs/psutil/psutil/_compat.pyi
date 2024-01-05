from builtins import ChildProcessError as ChildProcessError
from builtins import FileExistsError as FileExistsError
from builtins import FileNotFoundError as FileNotFoundError
from builtins import InterruptedError as InterruptedError
from builtins import PermissionError as PermissionError
from builtins import ProcessLookupError as ProcessLookupError
from builtins import range as range
from builtins import super as super
from contextlib import redirect_stderr as redirect_stderr
from functools import lru_cache as lru_cache
from shutil import get_terminal_size as get_terminal_size
from shutil import which as which
from subprocess import TimeoutExpired
from typing import Literal

PY3: Literal[True]
long = int
xrange = range
unicode = str
basestring = str

def u(s): ...
def b(s): ...

SubprocessTimeoutExpired = TimeoutExpired
