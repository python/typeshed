from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def min_maximal_matching(G: Graph[_Node]): ...
