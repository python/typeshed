from _typeshed import Incomplete

from networkx.classes.graph import Graph, _EdgeData, _Node, _NodeData
from networkx.utils.backends import _dispatchable

__all__ = ["line_graph", "inverse_line_graph"]

@_dispatchable
def line_graph(
    G: Graph[_Node, _NodeData, _EdgeData], create_using: Graph[Incomplete] | type[Graph[Incomplete]] | None = None
) -> Graph[Incomplete]: ...
@_dispatchable
def inverse_line_graph(G: Graph[_Node, _NodeData, _EdgeData]) -> Graph[Incomplete]: ...
