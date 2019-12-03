
from typing import Union, Optional, Type, Iterator, overload, List, TypeVar, Generic
from types import TracebackType

_T = TypeVar('_T')
_KeyType = Union[str, bytes]
_ValueType = Union[str, bytes]

class error(OSError): ...

# Actual typename gdbm, not exposed by the implementation
class _gdbm(Generic[_KeyType, _ValueType]):
    def firstkey(self) -> Optional[bytes]: ...
    def nextkey(self, key: _KeyType) -> Optional[bytes]: ...
    def reorganize(self) -> None: ...
    def sync(self) -> None: ...
    def close(self) -> None: ...
    def __getitem__(self, item: _KeyType) -> bytes: ...
    def __setitem__(self, key: _KeyType, value: _ValueType) -> None: ...
    def __delitem__(self, key: _KeyType) -> None: ...
    def __iter__(self) -> Iterator[_KeyType]: ...
    def __len__(self) -> int: ...
    def __enter__(self) -> _gdbm: ...
    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType]) -> None: ...

    @overload
    def get(self, k: _KeyType) -> Optional[_ValueType]: ...
    @overload
    def get(self, k: _KeyType, default: Union[_ValueType, _T]) -> Union[_ValueType, _T]: ...
    def keys(self) -> List[bytes]: ...
    def setdefault(self, k: _KeyType, default: _ValueType = ...) -> _ValueType: ...

    # Don't exist at runtime
    __new__: None  # type: ignore
    __init__: None  # type: ignore

def open(file: str, flag: str = ..., mode: int = ...) -> _gdbm: ...
