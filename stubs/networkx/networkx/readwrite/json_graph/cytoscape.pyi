from _typeshed import Incomplete
from collections.abc import Mapping
from typing import Any

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

__all__ = ["cytoscape_data", "cytoscape_graph"]

# Any: Complex type union
def cytoscape_data(G: Graph[_Node], name: str = "name", ident: str = "id") -> dict[str, Any]: ...
@_dispatchable
def cytoscape_graph(data: Mapping[str, Incomplete], name: str = "name", ident: str = "id"): ...
