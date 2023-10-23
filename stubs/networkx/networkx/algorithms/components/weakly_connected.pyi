from collections.abc import Hashable, Iterable
from typing import TypeVar

from networkx.classes.graph import Graph

_N = TypeVar("_N")

def weakly_connected_components(G: Graph[_N]) -> Iterable[set[_N]]: ...
def number_weakly_connected_components(G: Graph[Hashable]) -> int: ...
def is_weakly_connected(G: Graph[Hashable]) -> bool: ...
