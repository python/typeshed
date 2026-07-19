from _typeshed import Incomplete

from networkx.classes.graph import Graph, _Node
from networkx.classes.multigraph import MultiGraph
from networkx.utils.backends import _dispatchable

__all__ = ["from_sparse6_bytes", "read_sparse6", "to_sparse6_bytes", "write_sparse6"]

@_dispatchable
def from_sparse6_bytes(string: str) -> Graph[Incomplete]: ...
def to_sparse6_bytes(G: Graph[_Node], nodes: list[Incomplete] = None, header: bool = True): ...
@_dispatchable
def read_sparse6(path: str) -> MultiGraph[Incomplete]: ...
def write_sparse6(G: Graph[_Node], path: str, nodes: list[Incomplete] = None, header: bool = True) -> None: ...
