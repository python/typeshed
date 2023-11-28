from collections.abc import Hashable
from typing import TypeVar

from networkx.classes.graph import Graph

_N = TypeVar("_N")

def weakly_connected_components(G: Graph[_N]) -> Generator[set[_N], None, None]: ...
def number_weakly_connected_components(G: Graph[Hashable]) -> int: ...
def is_weakly_connected(G: Graph[Hashable]) -> bool: ...
