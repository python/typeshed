
import sys
from typing import Optional, Union

if sys.platform == "win32":
    SND_FILENAME: int
    SND_ALIAS: int
    SND_LOOP: int
    SND_MEMORY: int
    SND_PURGE: int
    SND_ASYNC: int
    SND_NODEFAULT: int
    SND_NOSTOP: int
    SND_NOWAIT: int

    MB_ICONASTERISK: int
    MB_ICONEXCLAMATION: int
    MB_ICONHAND: int
    MB_ICONQUESTION: int
    MB_OK: int

    def Beep(frequency: int, duration: int) -> None: ...
    def PlaySound(sound: Optional[Union[str, bytes, bytearray, memoryview]], flags: int) -> None: ...
    def MessageBeep(type: int = ...) -> None: ...
