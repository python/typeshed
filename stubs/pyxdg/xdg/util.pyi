import sys
from _typeshed import StrPath
from typing_extensions import Literal, TypeVar

_StrPathT = TypeVar("_StrPathT", bound=StrPath)

PY3: Literal[True]

def u(s: str) -> str: ...

if sys.version_info >= (3, 3):
    from shutil import which as which
else:
    def which(cmd: _StrPathT, mode: int = 1, path: StrPath | None = None) -> str | _StrPathT | None: ...
