from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def local_node_connectivity(G: Graph[_Node], source: _Node, target: _Node, cutoff: int = None): ...
@_dispatchable
def node_connectivity(G: Graph[_Node], s: _Node = None, t: _Node = None): ...
@_dispatchable
def all_pairs_node_connectivity(G: Graph[_Node], nbunch: Iterable = None, cutoff: int = None): ...
