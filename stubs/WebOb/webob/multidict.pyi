from _typeshed import SupportsItems, SupportsKeysAndGetItem
from _typeshed.wsgi import WSGIEnvironment
from cgi import FieldStorage
from collections.abc import Collection, Iterable, Iterator, MutableMapping
from typing import Any, Literal, TypeVar, overload
from typing_extensions import Self

_T = TypeVar("_T")
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")

class MultiDict(MutableMapping[_KT, _VT]):
    @overload
    def __init__(self, __m: SupportsItems[_KT, _VT], **kwargs: _VT): ...
    @overload
    def __init__(self, __m: Iterable[tuple[_KT, _VT]], **kwargs: _VT): ...
    @overload
    def __init__(self, **kwargs: _VT) -> None: ...
    @classmethod
    def view_list(cls, lst: list[tuple[_KT, _VT]]) -> MultiDict[_KT, _VT]: ...
    @classmethod
    def from_fieldstorage(cls, fs: FieldStorage) -> MultiDict[str, str | FieldStorage]: ...
    def __getitem__(self, key: _KT) -> _VT: ...
    def __setitem__(self, key: _KT, value: _VT) -> None: ...
    def add(self, key: _KT, value: _VT) -> None: ...
    @overload
    def get(self, key: _KT) -> _VT | None: ...
    @overload
    def get(self, key: _KT, default: _T) -> _VT | _T: ...
    def getall(self, key: _KT) -> list[_VT]: ...
    def getone(self, key: _KT) -> _VT: ...
    def mixed(self) -> dict[_KT, _VT | list[_VT]]: ...
    def dict_of_lists(self) -> dict[_KT, list[_VT]]: ...
    def __delitem__(self, key: _KT) -> None: ...
    def __contains__(self, key: object) -> bool: ...
    has_key = __contains__
    def clear(self) -> None: ...
    def copy(self) -> Self: ...
    @overload
    def setdefault(self, key: _KT, default: None = None) -> _VT | None: ...
    @overload
    def setdefault(self, key: _KT, default: _VT) -> _VT: ...
    @overload
    def pop(self, key: _KT) -> _VT: ...
    @overload
    def pop(self, key: _KT, default: _T) -> _VT | _T: ...
    def popitem(self) -> tuple[_KT, _VT]: ...
    @overload  # type:ignore[override]
    def update(self, __m: Collection[tuple[_KT, _VT]], **kwargs: _VT) -> None: ...
    @overload
    def update(self, **kwargs: _VT) -> None: ...
    @overload
    def extend(self, other: SupportsItems[_KT, _VT], **kwargs: _VT) -> None: ...
    @overload
    def extend(self, other: SupportsKeysAndGetItem[_KT, _VT], **kwargs: _VT) -> None: ...
    @overload
    def extend(self, other: Iterable[tuple[_KT, _VT]], **kwargs: _VT) -> None: ...
    @overload
    def extend(self, other: None = None, **kwargs: _VT) -> None: ...
    def __len__(self) -> int: ...
    def keys(self) -> Iterator[_KT]: ...  # type:ignore[override]
    __iter__ = keys
    def values(self) -> Iterator[_VT]: ...  # type:ignore[override]
    def items(self) -> Iterator[tuple[_KT, _VT]]: ...  # type:ignore[override]

class GetDict(MultiDict[str, str]):
    env: WSGIEnvironment
    @overload
    def __init__(self, data: SupportsItems[str, str], env: WSGIEnvironment) -> None: ...
    @overload
    def __init__(self, data: Iterable[tuple[str, str]], env: WSGIEnvironment) -> None: ...
    def on_change(self) -> None: ...

class NestedMultiDict(MultiDict[_KT, _VT]):
    dicts: tuple[MultiDict[_KT, _VT] | NoVars, ...]
    def __init__(self, *dicts: MultiDict[_KT, _VT] | NoVars) -> None: ...
    def __setitem__(self, key: _KT, value: _VT) -> None: ...
    def add(self, key: _KT, value: _VT) -> None: ...
    def __delitem__(self, key: _KT) -> None: ...
    def clear(self) -> None: ...
    def setdefault(self, key: _KT, default: _VT | None = ...) -> Any: ...
    def pop(self, key: _KT, default: Any = ...) -> Any: ...
    def popitem(self) -> tuple[_KT, _VT]: ...
    def update(self, *args: Any, **kwargs: _VT) -> None: ...
    def copy(self) -> MultiDict[_KT, _VT]: ...  # type:ignore[override]

class NoVars:
    reason: str
    def __init__(self, reason: str | None = None) -> None: ...
    @overload
    def get(self, key: str, default: None = None) -> None: ...
    @overload
    def get(self, key: str, default: _T) -> _T: ...
    def getall(self, key: str) -> list[str]: ...
    def mixed(self) -> dict[str, str | list[str]]: ...
    def dict_of_lists(self) -> dict[str, list[str]]: ...
    def __contains__(self, key: object) -> Literal[False]: ...
    has_key = __contains__
    def copy(self) -> Self: ...
    def __len__(self) -> Literal[0]: ...
    def __iter__(self) -> Iterator[str]: ...
    def keys(self) -> Iterator[str]: ...
    def values(self) -> Iterator[str]: ...
    def items(self) -> Iterator[tuple[str, str]]: ...
    def __bool__(self) -> Literal[False]: ...
