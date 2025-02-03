from _typeshed import SupportsGetItem
from collections.abc import Callable
from typing import Any

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def astar_path(
    G: Graph[_Node],
    source: _Node,
    target: _Node,
    heuristic: Callable = None,
    weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] = "weight",
    *,
    cutoff: float | None = None,
): ...
@_dispatchable
def astar_path_length(
    G: Graph[_Node],
    source: _Node,
    target: _Node,
    heuristic: Callable = None,
    weight: str | Callable[[Any, Any, SupportsGetItem[str, Any]], float | None] = "weight",
    *,
    cutoff: float | None = None,
): ...
