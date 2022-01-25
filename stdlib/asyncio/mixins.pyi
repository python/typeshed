import threading
from typing import Any

_global_lock: threading.Lock

class _LoopBoundMixin:
    def __init__(self) -> None: ...
