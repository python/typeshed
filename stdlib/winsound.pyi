import sys
from typing import overload
from typing_extensions import Literal

if sys.platform == "win32":
    SND_FILENAME: Literal[0]
    SND_ALIAS: Literal[0]
    SND_LOOP: Literal[0]
    SND_MEMORY: Literal[0]
    SND_PURGE: Literal[0]
    SND_ASYNC: Literal[0]
    SND_NODEFAULT: Literal[0]
    SND_NOSTOP: Literal[0]
    SND_NOWAIT: Literal[0]

    MB_ICONASTERISK: Literal[0]
    MB_ICONEXCLAMATION: Literal[0]
    MB_ICONHAND: Literal[0]
    MB_ICONQUESTION: Literal[0]
    MB_OK: Literal[0]
    def Beep(frequency: int, duration: int) -> None: ...
    # Can actually accept anything ORed with 4, and if not it's definitely str, but that's inexpressible
    @overload
    def PlaySound(sound: bytes | None, flags: Literal[4]) -> None: ...
    @overload
    def PlaySound(sound: str | bytes | None, flags: int) -> None: ...
    def MessageBeep(type: int = ...) -> None: ...
