from typing import TypeVar

from _typeshed import Incomplete
from networkx.classes.digraph import DiGraph

def disjoint_union(G: Incomplete, H: Incomplete) -> Incomplete: ...
def intersection(G: Incomplete, H: Incomplete) -> Incomplete: ...
def difference(G: Incomplete, H: Incomplete) -> Incomplete: ...
def symmetric_difference(G: Incomplete, H: Incomplete) -> Incomplete: ...

_X = TypeVar("_X", covariant=True)
_Y = TypeVar("_Y", covariant=True)
# GT = TypeVar('GT', bound=Graph)
# TODO: This does not handle the cases when graphs of different types are passed which is allowed

def compose(G: DiGraph[_X], H: DiGraph[_Y]) -> DiGraph[_X | _Y]: ...
def union(
    G: DiGraph[_X],
    H: DiGraph[_Y],
    rename: Incomplete = ...,
    name: Incomplete | None = ...,
) -> DiGraph[_X | _Y]: ...
