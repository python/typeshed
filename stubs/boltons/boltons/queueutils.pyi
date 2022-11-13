# TODO: DONE!

from typing import Any, NoReturn
from typing_extensions import TypeAlias

class BasePriorityQueue:
    def __init__(self, **kw) -> NoReturn: ...
    def add(self, task: Any, priority: int | None = ...) -> NoReturn: ...
    def remove(self, task: Any) -> NoReturn: ...
    def peek(self, default: Any = ...) -> Any | NoReturn: ...
    def pop(self, default: Any = ...) -> Any | NoReturn: ...
    def __len__(self) -> int: ...

class HeapPriorityQueue(BasePriorityQueue): ...
class SortedPriorityQueue(BasePriorityQueue): ...

PriorityQueue: TypeAlias = SortedPriorityQueue
