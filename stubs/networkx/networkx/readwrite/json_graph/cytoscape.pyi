from _typeshed import Incomplete
from typing import Any

from networkx.classes.graph import Graph, _EdgeData, _Node, _NodeData
from networkx.utils.backends import _dispatchable

__all__ = ["cytoscape_data", "cytoscape_graph"]

# Any: Complex type union
def cytoscape_data(G: Graph[_Node, _NodeData, _EdgeData], name: str = "name", ident: str = "id") -> dict[str, Any]: ...
@_dispatchable
def cytoscape_graph(data: dict[Incomplete, Incomplete], name: str = "name", ident: str = "id") -> Graph[Incomplete]: ...
