from collections.abc import Hashable

from networkx.classes.graph import Graph, _Node
from networkx.exception import NetworkXException

class NetworkXTreewidthBoundExceeded(NetworkXException): ...

def is_chordal(G: Graph[Hashable]) -> bool: ...
def find_induced_nodes(G: Graph[_Node], s: _Node, t: _Node, treewidth_bound: float = sys.maxsize) -> set[_Node]: ...
def chordal_graph_cliques(G: Graph[_Node]) -> Generator[frozenset[_Node], None, None]: ...
def chordal_graph_treewidth(G: Graph[Hashable]) -> int: ...
