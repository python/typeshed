from collections.abc import Iterator, MutableMapping
from types import TracebackType
from typing_extensions import Self, TypeAlias

__all__ = ["error", "open"]

_KeyType: TypeAlias = str | bytes
_ValueType: TypeAlias = str | bytes

error = OSError

# This class doesn't exist at runtime. open() can return an instance of
# any of the three implementations of dbm (dumb, gnu, ndbm), and this
# class is intended to represent the common interface supported by all three.
class _Database(MutableMapping[_KeyType, bytes]):
    def __init__(self, filebasename: str, mode: str, flag: str = "c") -> None: ...
    def sync(self) -> None: ...
    def iterkeys(self) -> Iterator[bytes]: ...  # undocumented
    def close(self) -> None: ...
    def __getitem__(self, key: _KeyType) -> bytes: ...
    def __setitem__(self, key: _KeyType, val: _ValueType) -> None: ...
    def __delitem__(self, key: _KeyType) -> None: ...
    def __iter__(self) -> Iterator[bytes]: ...
    def __len__(self) -> int: ...
    def __del__(self) -> None: ...
    def __enter__(self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...

def open(file: str, flag: str = "c", mode: int = 0o666) -> _Database: ...
