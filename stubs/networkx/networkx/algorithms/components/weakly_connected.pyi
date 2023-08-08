from collections.abc import Iterable
from typing import Any, TypeVar

from networkx.classes.graph import Graph

_N = TypeVar("_N")

def weakly_connected_components(G: Graph[_N]) -> Iterable[set[_N]]: ...
def number_weakly_connected_components(G: Graph[Any]) -> int: ...
def is_weakly_connected(G: Graph[Any]) -> bool: ...
