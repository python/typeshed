import sys
from collections.abc import Iterator
from typing import Any, Protocol, TypeVar, overload

_T = TypeVar("_T")

class PackageMetadata(Protocol):
    def __len__(self) -> int: ...
    def __contains__(self, item: str) -> bool: ...
    def __getitem__(self, key: str) -> str: ...
    def __iter__(self) -> Iterator[str]: ...
    @property
    def json(self) -> dict[str, str | list[str]]: ...
    @overload
    def get_all(self, name: str, failobj: None = None) -> list[Any] | None: ...
    @overload
    def get_all(self, name: str, failobj: _T) -> list[Any] | _T: ...
    if sys.version_info >= (3, 12):
        @overload
        def get(self, name: str, failobj: None = None) -> str | None: ...
        @overload
        def get(self, name: str, failobj: _T) -> _T | str: ...

if sys.version_info >= (3, 12):
    class SimplePath(Protocol[_T]):
        # At runtime this is defined as taking `str | _T`, but that causes trouble.
        # See #11436.
        def joinpath(self, other: str, /) -> _T: ...
        @property
        def parent(self) -> _T: ...
        def read_text(self) -> str: ...
        # As with joinpath(), this is annotated as taking `str | _T` at runtime.
        def __truediv__(self, other: str, /) -> _T: ...

else:
    class SimplePath(Protocol):
        # Actually takes only self at runtime, but that's clearly wrong
        def joinpath(self, other: Any, /) -> SimplePath: ...
        # Not defined as a property at runtime, but it should be
        @property
        def parent(self) -> Any: ...
        def read_text(self) -> str: ...
        # There was a bug in `SimplePath` definition in cpython, see #8451
        #  Strictly speaking `__div__` was defined in 3.10, not __truediv__,
        # but it should have always been `__truediv__`.
        # Also, the runtime defines this method as taking no arguments,
        # which is obviously wrong.
        def __truediv__(self, other: Any, /) -> SimplePath: ...
