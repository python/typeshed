import threading
from typing import Any

_global_lock: threading.Lock
_marker: object

class _LoopBoundMixin:
    def __init__(self, *, loop: Any = ...) -> None: ...
