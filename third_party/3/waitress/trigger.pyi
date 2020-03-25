from . import wasyncore as wasyncore
from _thread import LockType
import os
from socket import SocketType
from typing import Callable, Dict, Optional
from typing_extensions import Literal

class _triggerbase:
    kind: Optional[str] = ...
    lock: LockType = ...
    thunks: Callable[[None], None] = ...
    def __init__(self) -> None: ...
    def readable(self) -> Literal[True]: ...
    def writable(self) -> Literal[False]: ...
    def handle_connect(self) -> None: ...
    def handle_close(self) -> None: ...
    def close(self) -> None: ...
    def pull_trigger(self, thunk: Optional[Callable[[None], None]] = ...) -> None: ...
    def handle_read(self) -> None: ...

if os.name=="posix":
    class trigger(_triggerbase, wasyncore.file_dispatcher):
        kind: str = ...
        def __init__(self, map: Dict[str, _triggerbase]) -> None: ...

else:
    class trigger(_triggerbase, wasyncore.dispatcher): # type: ignore
        kind: str = ...
        trigger: SocketType = ...
        def __init__(self, map: Dict[str, _triggerbase]) -> None: ...
