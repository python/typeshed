from _typeshed.wsgi import WSGIEnvironment
from collections.abc import Iterator, MutableMapping
from typing import TypeVar, overload

from webob.multidict import MultiDict

__all__ = ["ResponseHeaders", "EnvironHeaders"]

_T = TypeVar("_T")

class ResponseHeaders(MultiDict[str, str]):
    def __getitem__(self, key: str) -> str: ...
    def getall(self, key: str) -> list[str]: ...
    def mixed(self) -> dict[str, str | list[str]]: ...
    def dict_of_lists(self) -> dict[str, list[str]]: ...
    def __setitem__(self, key: str, value: str) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __contains__(self, key: object) -> bool: ...
    has_key = __contains__
    def setdefault(self, key: str, default: str) -> str: ...  # type: ignore[override]
    @overload
    def pop(self, key: str) -> str: ...
    @overload
    def pop(self, key: str, default: _T) -> str | _T: ...

class EnvironHeaders(MutableMapping[str, str]):
    environ: WSGIEnvironment
    def __init__(self, environ: WSGIEnvironment) -> None: ...
    def __getitem__(self, hname: str) -> str: ...
    def __setitem__(self, hname: str, value: str) -> None: ...
    def __delitem__(self, hname: str) -> None: ...
    def keys(self) -> filter[str]: ...  # type: ignore[override]
    def __contains__(self, hname: object) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[str]: ...
