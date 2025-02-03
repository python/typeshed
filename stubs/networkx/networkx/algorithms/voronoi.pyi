from collections.abc import Callable
from typing import Any

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def voronoi_cells(
    G: Graph[_Node], center_nodes: set, weight: str | Callable[[Any, Any, dict[str, Any]], float | None] = "weight"
): ...
