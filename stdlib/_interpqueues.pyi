from typing import Any, Literal, SupportsIndex
from typing_extensions import TypeAlias

_UnboundOp: TypeAlias = Literal[1, 2, 3]

class QueueError(RuntimeError): ...
class QueueNotFoundError(QueueError): ...

def bind(qid: SupportsIndex) -> None: ...
def create(maxsize: SupportsIndex, fmt: SupportsIndex, unboundop: _UnboundOp) -> int: ...
def destroy(qid: SupportsIndex) -> None: ...
def get(qid: SupportsIndex) -> tuple[Any, int, _UnboundOp | None]: ...
def get_count(qid: SupportsIndex) -> int: ...
def get_maxsize(qid: SupportsIndex) -> int: ...
def get_queue_defaults(qid: SupportsIndex) -> tuple[int, _UnboundOp]: ...
def is_full(qid: SupportsIndex) -> bool: ...
def list_all() -> list[tuple[int, int, _UnboundOp]]: ...
def put(qid: SupportsIndex, obj: Any, fmt: SupportsIndex, unboundop: _UnboundOp) -> None: ...
def release(qid: SupportsIndex) -> None: ...
