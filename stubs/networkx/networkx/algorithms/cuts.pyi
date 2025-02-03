from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def cut_size(G: Graph[_Node], S: Iterable[_Node], T: Iterable[_Node] = None, weight: str = None): ...
@_dispatchable
def volume(G: Graph[_Node], S: Iterable[_Node], weight: str = None): ...
@_dispatchable
def normalized_cut_size(G: Graph[_Node], S: Iterable[_Node], T: Iterable[_Node] = None, weight: str = None): ...
@_dispatchable
def conductance(G: Graph[_Node], S: Iterable[_Node], T: Iterable[_Node] = None, weight: str = None): ...
@_dispatchable
def edge_expansion(G: Graph[_Node], S: Iterable[_Node], T: Iterable[_Node] = None, weight: str = None): ...
@_dispatchable
def mixing_expansion(G: Graph[_Node], S: Iterable[_Node], T: Iterable[_Node] = None, weight: str = None): ...
@_dispatchable
def node_expansion(G: Graph[_Node], S: Iterable[_Node]): ...
@_dispatchable
def boundary_expansion(G: Graph[_Node], S: Iterable[_Node]): ...
