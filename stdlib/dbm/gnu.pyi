from _typeshed import Self
from types import TracebackType
from typing import  Type, TypeVar, Union, overload

_T = TypeVar("_T")
_KeyType = Union[str, bytes]
_ValueType = Union[str, bytes]

class error(OSError): ...

# Actual typename gdbm, not exposed by the implementation
class _gdbm:
    def firstkey(self) -> bytes | None: ...
    def nextkey(self, key: _KeyType) -> bytes | None: ...
    def reorganize(self) -> None: ...
    def sync(self) -> None: ...
    def close(self) -> None: ...
    def __getitem__(self, item: _KeyType) -> bytes: ...
    def __setitem__(self, key: _KeyType, value: _ValueType) -> None: ...
    def __delitem__(self, key: _KeyType) -> None: ...
    def __contains__(self, key: _KeyType) -> bool: ...
    def __len__(self) -> int: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, exc_type: Type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...
    @overload
    def get(self, k: _KeyType) -> bytes | None: ...
    @overload
    def get(self, k: _KeyType, default: bytes | _T) -> bytes | _T: ...
    def keys(self) -> list[bytes]: ...
    def setdefault(self, k: _KeyType, default: _ValueType = ...) -> bytes: ...
    # Don't exist at runtime
    __new__: None  # type: ignore
    __init__: None  # type: ignore

def open(__filename: str, __flags: str = ..., __mode: int = ...) -> _gdbm: ...
