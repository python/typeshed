from collections.abc import Iterator
from typing import Generic, TypeVar

_T = TypeVar("_T")

class CancellableStream(Generic[_T]):
    def __init__(self, stream, response) -> None: ...
    def __iter__(self) -> Iterator[_T]: ...
    def __next__(self) -> _T: ...
    next = __next__
    def close(self) -> None: ...
