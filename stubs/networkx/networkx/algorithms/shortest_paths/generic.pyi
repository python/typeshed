from _typeshed import Incomplete
from collections.abc import Iterable
from typing import TypeVar, overload

from networkx.classes.graph import Graph

_T = TypeVar("_T")

def has_path(G, source, target): ...
@overload
def shortest_path(
    G: Graph[_T], source: _T, target: _T, weight: Incomplete | None = None, method: str = "dijkstra"
) -> list[_T]: ...
@overload
def shortest_path(G: Graph[_T], target: _T, method: str = "dijkstra") -> dict[_T, list[_T]]: ...
@overload
def shortest_path(G: Graph[_T], source: _T, method: str = "dijkstra") -> dict[_T, list[_T]]: ...
def shortest_path_length(
    G,
    source: Incomplete | None = None,
    target: Incomplete | None = None,
    weight: Incomplete | None = None,
    method: str = "dijkstra",
): ...
def average_shortest_path_length(G, weight: Incomplete | None = None, method: str | None = None): ...
def all_shortest_paths(
    G: Graph[_T], source: _T, target: _T, weight: Incomplete | None = None, method: str = "dijkstra"
) -> Iterable[list[_T]]: ...
