from collections.abc import Collection

import numpy as np
from networkx._typing import Array2D
from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _EdgeData, _Node, _NodeData
from networkx.utils.backends import _dispatchable

__all__ = ["modularity_matrix", "directed_modularity_matrix"]

@_dispatchable
def modularity_matrix(
    G: Graph[_Node, _NodeData, _EdgeData], nodelist: Collection[_Node] | None = None, weight: str | None = None
) -> Array2D[np.float64]: ...
@_dispatchable
def directed_modularity_matrix(
    G: DiGraph[_Node, _NodeData, _EdgeData], nodelist: Collection[_Node] | None = None, weight: str | None = None
) -> Array2D[np.float64]: ...
