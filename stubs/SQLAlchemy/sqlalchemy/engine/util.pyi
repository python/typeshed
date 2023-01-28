from _typeshed import Incomplete, Self
from collections.abc import Callable
from types import TracebackType

def connection_memoize(key: str) -> Callable[..., Incomplete]: ...

class TransactionalContext:
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, type_: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None
    ) -> None: ...
