from _typeshed import StrPath
from typing import Any, BinaryIO, Callable, List, Protocol, overload

class _ReadableBinary(Protocol):
    def tell(self) -> int: ...
    def read(self, size: int) -> bytes: ...
    def seek(self, offset: int) -> Any: ...

@overload
def what(file: StrPath | _ReadableBinary, h: None = ...) -> str | None: ...
@overload
def what(file: Any, h: bytes) -> str | None: ...

tests: List[Callable[[bytes, BinaryIO | None], str | None]]
