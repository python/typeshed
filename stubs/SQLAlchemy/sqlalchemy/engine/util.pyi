from _typeshed import Incomplete
from collections.abc import Callable
from types import TracebackType
from typing_extensions import Self

def connection_memoize(key: str) -> Callable[..., Incomplete]: ...

class TransactionalContext:
    def __enter__(self) -> Self: ...
    def __exit__(
        self, type_: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
