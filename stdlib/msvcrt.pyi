import sys
from typing import Final, Literal

# This module is only available on Windows
if sys.platform == "win32":
    CRT_ASSEMBLY_VERSION: Final[str]
    LK_UNLCK: Literal[0]
    LK_LOCK: Literal[1]
    LK_NBLCK: Literal[2]
    LK_RLCK: Literal[3]
    LK_NBRLCK: Literal[4]
    SEM_FAILCRITICALERRORS: int
    SEM_NOALIGNMENTFAULTEXCEPT: int
    SEM_NOGPFAULTERRORBOX: int
    SEM_NOOPENFILEERRORBOX: int
    def locking(fd: int, mode: int, nbytes: int, /) -> None: ...
    def setmode(fd: int, mode: int, /) -> int: ...
    def open_osfhandle(handle: int, flags: int, /) -> int: ...
    def get_osfhandle(fd: int, /) -> int: ...
    def kbhit() -> bool: ...
    def getch() -> bytes: ...
    def getwch() -> str: ...
    def getche() -> bytes: ...
    def getwche() -> str: ...
    def putch(char: bytes | bytearray, /) -> None: ...
    def putwch(unicode_char: str, /) -> None: ...
    def ungetch(char: bytes | bytearray, /) -> None: ...
    def ungetwch(unicode_char: str, /) -> None: ...
    def heapmin() -> None: ...
    def SetErrorMode(mode: int, /) -> int: ...
    if sys.version_info >= (3, 10):
        def GetErrorMode() -> int: ...  # undocumented
