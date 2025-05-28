from _typeshed import Incomplete
from collections.abc import Collection

from networkx.utils.backends import _dispatchable

from ..classes.digraph import DiGraph
from ..classes.graph import Graph, _Node

__all__ = ["modularity_matrix", "directed_modularity_matrix"]

@_dispatchable
def modularity_matrix(G: Graph[_Node], nodelist: Collection[Incomplete] | None = None, weight=None): ...
@_dispatchable
def directed_modularity_matrix(G: DiGraph[_Node], nodelist: Collection[Incomplete] | None = None, weight=None): ...
