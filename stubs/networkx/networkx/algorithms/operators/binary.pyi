from collections.abc import Hashable, Iterable
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

_X = TypeVar("_X", bound=Hashable, covariant=True)
_Y = TypeVar("_Y", bound=Hashable, covariant=True)

@_dispatchable
def compose(G, H) -> DiGraph[_X | _Y]: ...
@_dispatchable
def union(G, H, rename: Iterable | None = ()) -> DiGraph[_X | _Y]: ...
