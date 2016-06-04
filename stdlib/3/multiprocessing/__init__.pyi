# Stubs for multiprocessing

from typing import Any, Callable, Iterable, Mapping

class Lock(): ...
class Process():
    # TODO: set type of group to None
    def __init__(self,
                 group: Any = ...,
                 target: Callable = ...,
                 name: str = ...,
                 args: Iterable[Any] = ...,
                 kwargs: Mapping[Any, Any] = ...,
                 daemon: bool = ...) -> None: ...

    def start(self) -> None: ...

    def terminate(self) -> None: ...

class Queue():
    def get(self, block: bool = ..., timeout: float = ...) -> Any: ...
    def put(self, item: Any, block: bool = ..., timeout: float = ...) -> None: ...

class Value():
    def __init__(typecode_or_type: str, *args: Any, lock: bool = ...) -> None: ...

# ----- multiprocessing function stubs -----
def cpu_count() -> int: ...
