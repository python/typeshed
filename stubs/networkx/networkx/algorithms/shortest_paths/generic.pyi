from collections.abc import Iterable
from typing import TypeVar, overload

from _typeshed import Incomplete
from networkx.classes.graph import Graph

_T = TypeVar("_T")

def has_path(G: Incomplete, source: Incomplete, target: Incomplete) -> Incomplete: ...
@overload
def shortest_path(
    G: Graph[_T],
    source: _T,
    target: _T,
    weight: Incomplete | None = ...,
    method: str = ...,
) -> list[_T]: ...
@overload
def shortest_path(
    G: Graph[_T], target: _T, method: str = ...
) -> dict[_T, list[_T]]: ...
@overload
def shortest_path(
    G: Graph[_T], source: _T, method: str = ...
) -> dict[_T, list[_T]]: ...
def shortest_path_length(
    G: Incomplete,
    source: Incomplete | None = ...,
    target: Incomplete | None = ...,
    weight: Incomplete | None = ...,
    method: str = ...,
) -> Incomplete: ...
def average_shortest_path_length(
    G: Incomplete, weight: Incomplete | None = ..., method: str = ...
) -> Incomplete: ...
def all_shortest_paths(
    G: Graph[_T],
    source: _T,
    target: _T,
    weight: Incomplete | None = ...,
    method: str = ...,
) -> Iterable[list[_T]]: ...
