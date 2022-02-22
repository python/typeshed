import sys
from typing import Any, Generic, Iterable, Mapping, TypeVar, Union, overload

if sys.version_info >= (3, 9):
    from types import GenericAlias

__all__ = ["CookieError", "BaseCookie", "SimpleCookie"]

_DataType = Union[str, Mapping[str, Union[str, Morsel[Any]]]]
_T = TypeVar("_T")

@overload
def _quote(str: None) -> None: ...
@overload
def _quote(str: str) -> str: ...
@overload
def _unquote(str: None) -> None: ...
@overload
def _unquote(str: str) -> str: ...

class CookieError(Exception): ...

class Morsel(dict[str, Any], Generic[_T]):
    value: str
    coded_value: _T
    key: str
    def __init__(self) -> None: ...
    if sys.version_info >= (3, 7):
        def set(self, key: str, val: str, coded_val: _T) -> None: ...
    else:
        def set(self, key: str, val: str, coded_val: _T, LegalChars: str = ...) -> None: ...

    def setdefault(self, key: str, val: str | None = ...) -> str: ...
    # The dict update can also get a keywords argument so this is incompatible
    @overload  # type: ignore[override]
    def update(self, values: Mapping[str, str]) -> None: ...
    @overload
    def update(self, values: Iterable[tuple[str, str]]) -> None: ...
    def isReservedKey(self, K: str) -> bool: ...
    def output(self, attrs: list[str] | None = ..., header: str = ...) -> str: ...
    __str__ = output
    def js_output(self, attrs: list[str] | None = ...) -> str: ...
    def OutputString(self, attrs: list[str] | None = ...) -> str: ...
    def __eq__(self, morsel: object) -> bool: ...
    def __setitem__(self, K: str, V: Any) -> None: ...
    if sys.version_info >= (3, 9):
        def __class_getitem__(cls, item: Any) -> GenericAlias: ...

class BaseCookie(dict[str, Morsel[_T]], Generic[_T]):
    def __init__(self, input: _DataType | None = ...) -> None: ...
    def value_decode(self, val: str) -> _T: ...
    def value_encode(self, val: _T) -> str: ...
    def output(self, attrs: list[str] | None = ..., header: str = ..., sep: str = ...) -> str: ...
    __str__ = output
    def js_output(self, attrs: list[str] | None = ...) -> str: ...
    def load(self, rawdata: _DataType) -> None: ...
    def __setitem__(self, key: str, value: str | Morsel[_T]) -> None: ...

class SimpleCookie(BaseCookie[_T], Generic[_T]): ...
