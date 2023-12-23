from collections.abc import Iterable, Sequence
from typing import Any, Protocol, TypeVar
from typing_extensions import Literal

__all__ = ["NodeList", "EmptyNodeList", "StringTypes", "defproperty"]

_T = TypeVar("_T", covariant=True)

StringTypes: tuple[type[str]]

class NodeList(Sequence[_T], Protocol):
    @property
    def length(self) -> int: ...
    def item(self, index: int) -> _T | None: ...

class EmptyNodeList(tuple[()]):
    @property
    def length(self) -> Literal[0]: ...
    def item(self, index: int) -> None: ...
    def __add__(self, other: Iterable[_T]) -> NodeList[_T]: ...  # type: ignore[override]
    def __radd__(self, other: Iterable[_T]) -> NodeList[_T]: ...

def defproperty(klass: type[Any], name: str, doc: str) -> None: ...
