from _typeshed import Incomplete

from networkx.classes.graph import Graph, _EdgeData, _Node, _NodeData
from networkx.utils.backends import _dispatchable

__all__ = ["mycielskian", "mycielski_graph"]

@_dispatchable
def mycielskian(G: Graph[_Node, _NodeData, _EdgeData], iterations: int = 1) -> Graph[Incomplete]: ...
@_dispatchable
def mycielski_graph(n: int) -> Graph[Incomplete]: ...
