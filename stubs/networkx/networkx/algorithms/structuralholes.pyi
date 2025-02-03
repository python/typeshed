from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def effective_size(G: Graph[_Node], nodes: Iterable | None = None, weight: str | None = None): ...
@_dispatchable
def constraint(G: Graph[_Node], nodes: Iterable | None = None, weight: str | None = None): ...
@_dispatchable
def local_constraint(G: Graph[_Node], u: _Node, v: _Node, weight: str | None = None): ...
