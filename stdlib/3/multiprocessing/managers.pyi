# Stubs for multiprocessing.managers

# NOTE: These are incomplete!

from typing import Any

class BaseManager():
    def register(typeid: str, callable: Any = ...) -> None: ...

class RemoteError(Exception): ...
