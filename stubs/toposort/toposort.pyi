from typing import Generic, Iterator, TypeVar

_T = TypeVar("_T")

class CircularDependencyError(ValueError, Generic[_T]):
    data: dict[_T, set[_T]]
    def __init__(self, data: dict[_T, set[_T]]) -> None: ...

def toposort(data: dict[_T, set[_T]]) -> Iterator[set[_T]]: ...
def toposort_flatten(data: dict[_T, set[_T]], sort: bool = ...) -> list[_T]: ...
