from _typeshed import Incomplete
from collections.abc import Mapping

from networkx.utils.backends import _dispatchable

from ...classes.graph import Graph

__all__ = ["tree_data", "tree_graph"]

def tree_data(G: Graph[Incomplete], root, ident: str = "id", children: str = "children"): ...
@_dispatchable
def tree_graph(data: Mapping[str, Incomplete], ident: str = "id", children: str = "children"): ...
