import sys
from termios import _AttrReturn
from typing import IO
from typing_extensions import TypeAlias

if sys.platform != "win32":
    __all__ = ["setraw", "setcbreak"]

    if sys.version_info >= (3, 12):
        _SetReturn: TypeAlias = _AttrReturn
    else:
        _SetReturn: TypeAlias = None

    _FD: TypeAlias = int | IO[str]

    # XXX: Undocumented integer constants
    IFLAG: int
    OFLAG: int
    CFLAG: int
    LFLAG: int
    ISPEED: int
    OSPEED: int
    CC: int
    def setraw(fd: _FD, when: int = 2) -> _SetReturn: ...
    def setcbreak(fd: _FD, when: int = 2) -> _SetReturn: ...
