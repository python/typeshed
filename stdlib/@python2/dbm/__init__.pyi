from _typeshed import Self
from types import TracebackType
from typing import Iterator, MutableMapping
from typing_extensions import Literal

_KeyType = str | bytes
_ValueType = str | bytes

class _Database(MutableMapping[_KeyType, bytes]):
    def close(self) -> None: ...
    def __getitem__(self, key: _KeyType) -> bytes: ...
    def __setitem__(self, key: _KeyType, value: _ValueType) -> None: ...
    def __delitem__(self, key: _KeyType) -> None: ...
    def __iter__(self) -> Iterator[bytes]: ...
    def __len__(self) -> int: ...
    def __del__(self) -> None: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> None: ...

class _error(Exception): ...

error = tuple[type[_error], type[OSError]]

def whichdb(filename: str) -> str: ...
def open(file: str, flag: Literal["r", "w", "c", "n"] = ..., mode: int = ...) -> _Database: ...
