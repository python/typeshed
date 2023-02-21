from _typeshed import Incomplete
from typing import Any

class QueryIterator:
    def __iter__(self): ...
    def has_next(self) -> None: ...
    def has_next_async(self) -> None: ...
    def probably_has_next(self) -> None: ...
    def next(self) -> None: ...
    def cursor_before(self) -> None: ...
    def cursor_after(self) -> None: ...
    def index_list(self) -> None: ...

class Cursor:
    @classmethod
    def from_websafe_string(cls, urlsafe): ...
    cursor: Any
    def __init__(self, cursor: Incomplete | None = ..., urlsafe: Incomplete | None = ...) -> None: ...
    def to_websafe_string(self): ...
    def urlsafe(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self) -> int: ...
