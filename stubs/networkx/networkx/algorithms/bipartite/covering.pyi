from collections.abc import Callable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def min_edge_cover(G: Graph[_Node], matching_algorithm: Callable = None): ...
