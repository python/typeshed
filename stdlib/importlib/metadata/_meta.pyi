import sys
from collections.abc import Iterator
from typing import Any, Protocol, TypeVar, overload

_T = TypeVar("_T")

class PackageMetadata(Protocol):
    def __len__(self) -> int: ...
    def __contains__(self, item: str) -> bool: ...
    def __getitem__(self, key: str) -> str: ...
    def __iter__(self) -> Iterator[str]: ...
    def get_all(self, name: str, failobj: _T = ...) -> list[Any] | _T: ...
    @property
    def json(self) -> dict[str, str | list[str]]: ...
    if sys.version_info >= (3, 12):
        @overload
        def get(self, name: str, failobj: None = None) -> str | None: ...
        @overload
        def get(self, name: str, failobj: _T) -> _T | str: ...

if sys.version_info >= (3, 12):
    class SimplePath(Protocol[_T]):
        def joinpath(self) -> _T: ...
        @property
        def parent(self) -> _T: ...
        def read_text(self) -> str: ...
        def __truediv__(self, other: _T | str) -> _T: ...
else:
    class SimplePath(Protocol):
        def joinpath(self) -> SimplePath: ...
        def parent(self) -> SimplePath: ...
        def read_text(self) -> str: ...
        # There was a bug in `SimplePath` definition in cpython, see #8451
        #  Strictly speaking `__div__` was defined in 3.10, not __truediv__,
        # but it should have always been `__truediv__`.
        def __truediv__(self) -> SimplePath: ...
