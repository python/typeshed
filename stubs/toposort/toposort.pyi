from _typeshed import SupportsItems
from typing import Any, Iterator, TypeVar

_T = TypeVar("_T")

class CircularDependencyError(ValueError):
    data: dict[Any, set[Any]]
    def __init__(self, data: dict[Any, set[Any]]) -> None: ...

def toposort(data: SupportsItems[_T, set[_T]]) -> Iterator[set[_T]]: ...
def toposort_flatten(data: SupportsItems[_T, set[_T]], sort: bool = ...) -> list[_T]: ...
