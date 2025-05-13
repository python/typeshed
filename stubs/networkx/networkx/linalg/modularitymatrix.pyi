from _typeshed import Incomplete
from collections.abc import Collection

from networkx.utils.backends import _dispatchable

from ..classes.digraph import DiGraph
from ..classes.graph import Graph

__all__ = ["modularity_matrix", "directed_modularity_matrix"]

@_dispatchable
def modularity_matrix(G: Graph[Incomplete], nodelist: Collection[Incomplete] | None = None, weight: Incomplete | None = None): ...
@_dispatchable
def directed_modularity_matrix(
    G: DiGraph[Incomplete], nodelist: Collection[Incomplete] | None = None, weight: Incomplete | None = None
): ...
