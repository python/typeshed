from collections.abc import Hashable
from typing import TypeVar

from networkx.classes.digraph import DiGraph
from networkx.utils.backends import _dispatchable

@_dispatchable
def disjoint_union(G, H): ...
@_dispatchable
def intersection(G, H): ...
@_dispatchable
def difference(G, H): ...
@_dispatchable
def symmetric_difference(G, H): ...

_X_co = TypeVar("_X_co", bound=Hashable, covariant=True)
_Y_co = TypeVar("_Y_co", bound=Hashable, covariant=True)
# GT = TypeVar('GT', bound=Graph[_Node])
# TODO: This does not handle the cases when graphs of different types are passed which is allowed

@_dispatchable
def compose(G: DiGraph[_X_co], H: DiGraph[_Y_co]) -> DiGraph[_X_co | _Y_co]: ...
@_dispatchable
def union(G: DiGraph[_X_co], H: DiGraph[_Y_co], rename=()) -> DiGraph[_X_co | _Y_co]: ...
