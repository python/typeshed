from _typeshed import Incomplete
from collections.abc import Hashable, Iterable
from typing import TypeVar

from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def disjoint_union(G: Graph[_Node], H: Graph[_Node]): ...
@_dispatchable
def intersection(G: Graph[_Node], H: Graph[_Node]): ...
@_dispatchable
def difference(G: Graph[_Node], H: Graph[_Node]): ...
@_dispatchable
def symmetric_difference(G: Graph[_Node], H: Graph[_Node]): ...

_X = TypeVar("_X", bound=Hashable, covariant=True)
_Y = TypeVar("_Y", bound=Hashable, covariant=True)

@_dispatchable
def compose(G: Graph[_X], H: Graph[_Y]) -> DiGraph[_X | _Y]: ...
@_dispatchable
def union(G: Graph[_X], H: Graph[_Y], rename: Iterable[Incomplete] | None = ()) -> DiGraph[_X | _Y]: ...
