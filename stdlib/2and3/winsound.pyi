
import sys
from typing import Optional, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

if sys.platform == "win32":
    SND_FILENAME: Literal[131072]
    SND_ALIAS: Literal[65536]
    SND_LOOP: Literal[8]
    SND_MEMORY: Literal[4]
    SND_PURGE: Literal[64]
    SND_ASYNC: Literal[1]
    SND_NODEFAULT: Literal[2]
    SND_NOSTOP: Literal[16]
    SND_NOWAIT: Literal[8192]

    MB_ICONASTERISK: Literal[64]
    MB_ICONEXCLAMATION: Literal[48]
    MB_ICONHAND: Literal[16]
    MB_ICONQUESTION: Literal[32]
    MB_OK: Literal[0]

    def Beep(frequency: int, duration: int) -> None: ...
    def PlaySound(sound: Optional[Union[str, bytes, bytearray, memoryview]], flags: int) -> None: ...
    def MessageBeep(type: int = ...) -> None: ...
