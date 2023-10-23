from _typeshed import Incomplete
from collections.abc import Generator
from typing import TypeVar

from networkx.classes.graph import Graph

__all__ = ["all_simple_paths", "is_simple_path", "shortest_simple_paths", "all_simple_edge_paths"]
_T = TypeVar("_T")

def is_simple_path(G: Graph[_T], nodes: list[_T]): ...
def all_simple_paths(
    G: Graph[_T], source: _T, target: _T, cutoff: Incomplete | None = ...
) -> Generator[list[_T], None, None]: ...
def all_simple_edge_paths(
    G: Graph[_T], source: _T, target: _T, cutoff: Incomplete | None = None
) -> Generator[list[_T] | list[tuple[_T, _T]], None, list[_T] | None]: ...
def shortest_simple_paths(
    G: Graph[_T], source: _T, target: _T, weight: Incomplete | None = ...
) -> Generator[list[_T], None, None]: ...

class PathBuffer:
    paths: Incomplete
    sortedpaths: Incomplete
    counter: Incomplete
    def __init__(self) -> None: ...
    def __len__(self): ...
    def push(self, cost, path) -> None: ...
    def pop(self): ...
