from . import wasyncore as wasyncore
from typing import Any, Optional

class _triggerbase:
    kind: Any = ...
    lock: Any = ...
    thunks: Any = ...
    def __init__(self) -> None: ...
    def readable(self): ...
    def writable(self): ...
    def handle_connect(self) -> None: ...
    def handle_close(self) -> None: ...
    def close(self) -> None: ...
    def pull_trigger(self, thunk: Optional[Any] = ...) -> None: ...
    def handle_read(self) -> None: ...

class trigger(_triggerbase, wasyncore.file_dispatcher):
    kind: str = ...
    def __init__(self, map: Any) -> None: ...

class trigger(_triggerbase, wasyncore.dispatcher):
    kind: str = ...
    trigger: Any = ...
    def __init__(self, map: Any) -> None: ...
