from typing import Protocol, TypeVar, type_check_only
from typing_extensions import Self

class weekday:
    __slots__ = ["weekday", "n"]
    def __init__(self, weekday: int, n: int | None = None) -> None: ...
    def __call__(self, n: int | None) -> Self: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    weekday: int
    n: int | None

_T_co = TypeVar("_T_co", covariant=True)
_T_contra = TypeVar("_T_contra", contravariant=True)

@type_check_only
class _SizedReader(Protocol[_T_co]):  # noqa: Y046  # Used by other modules.
    def read(self, size: int, /) -> _T_co: ...

@type_check_only
class _ReadAll(Protocol[_T_co]):  # noqa: Y046  # Used by other modules.
    def read(self) -> _T_co: ...

@type_check_only
class _TotalSeconds(Protocol):  # noqa: Y046  # Used by other modules.
    def total_seconds(self) -> float: ...

@type_check_only
class _Weekday(Protocol):  # noqa: Y046  # Used by other modules.
    @property
    def weekday(self) -> int: ...
    @property
    def n(self) -> int | None: ...

@type_check_only
class _Gettable(Protocol[_T_contra, _T_co]):
    def get(self, key: _T_contra, /) -> _T_co | None: ...

@type_check_only
class _ContainsGet(_Gettable[_T_contra, _T_co], Protocol[_T_contra, _T_co]):  # noqa: Y046  # Used by other modules.
    def __contains__(self, key: object, /) -> bool: ...
