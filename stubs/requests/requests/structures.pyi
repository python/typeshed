from collections.abc import Iterable, Iterator, Mapping, MutableMapping
from typing import Any, Generic, TypeVar

_D = TypeVar("_D")
_VT = TypeVar("_VT")

class CaseInsensitiveDict(MutableMapping[str, _VT], Generic[_VT]):
    def __init__(self, data: Mapping[str, _VT] | Iterable[tuple[str, _VT]] | None = ..., **kwargs: _VT) -> None: ...
    def lower_items(self) -> Iterator[tuple[str, _VT]]: ...
    def __setitem__(self, key: str, value: _VT) -> None: ...
    def __getitem__(self, key: str) -> _VT: ...
    def __delitem__(self, key: str) -> None: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def copy(self) -> CaseInsensitiveDict[_VT]: ...

class LookupDict(dict[str, _VT]):
    name: Any
    def __init__(self, name: Any = ...) -> None: ...
    def __getitem__(self, key: str) -> _VT | None: ...  # type: ignore[override]
    def __setattr__(self, __attr: str, __value: _VT) -> None: ...
    def get(self, key: str, default: _D | None = ...) -> _VT | _D | None: ...  # type: ignore[override]
