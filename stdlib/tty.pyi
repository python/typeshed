import sys
from termios import _AttrReturn
from typing import IO, Any
from typing_extensions import TypeAlias

if sys.platform != "win32":
    __all__ = ["setraw", "setcbreak"]
    if sys.version_info >= (3, 12):
        __all__ += ["cfmakeraw", "cfmakecbreak"]

        _ModeSetterReturn: TypeAlias = _AttrReturn
    else:
        _ModeSetterReturn: TypeAlias = None

    _FD: TypeAlias = int | IO[str]

    # XXX: Undocumented integer constants
    IFLAG: int
    OFLAG: int
    CFLAG: int
    LFLAG: int
    ISPEED: int
    OSPEED: int
    CC: int
    def setraw(fd: _FD, when: int = 2) -> _ModeSetterReturn: ...
    def setcbreak(fd: _FD, when: int = 2) -> _ModeSetterReturn: ...

    if sys.version_info >= (3, 12):
        # It is: `list[int, int, int, int, int, int, list[str]]
        _Mode: TypeAlias = list[Any]

        def cfmakeraw(mode: _Mode) -> None: ...
        def cfmakecbreak(mode: _Mode) -> None: ...
