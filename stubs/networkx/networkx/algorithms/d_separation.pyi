from _typeshed import Incomplete
from typing_extensions import deprecated

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["is_d_separator", "is_minimal_d_separator", "find_minimal_d_separator", "d_separated", "minimal_d_separator"]

@_dispatchable
def is_d_separator(G: DiGraph[_Node], x: _Node | set[_Node], y: _Node | set[_Node], z: _Node | set[_Node]) -> bool: ...
@_dispatchable
def find_minimal_d_separator(G, x, y, *, included=None, restricted=None) -> set[Incomplete] | None: ...
@deprecated("d_separated is deprecated and will be removed in NetworkX v3.5. Please use `is_d_separator(G, x, y, z)`.")
def d_separated(
    G: Graph[Incomplete], x: Incomplete | set[Incomplete], y: Incomplete | set[Incomplete], z: Incomplete | set[Incomplete]
) -> bool: ...
@_dispatchable
def minimal_d_separator(G, u, v): ...
@_dispatchable
def is_minimal_d_separator(
    G: DiGraph[_Node],
    x: _Node | set[_Node],
    y: _Node | set[_Node],
    z: _Node | set[_Node],
    *,
    included: _Node | set[_Node] | None = None,
    restricted: _Node | set[_Node] | None = None,
) -> bool: ...
