from collections.abc import Generator

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def weakly_connected_components(G: Graph[_Node]) -> Generator[set[_Node], None, None]: ...
@_dispatchable
def number_weakly_connected_components(G: Graph[_Node]) -> int: ...
@_dispatchable
def is_weakly_connected(G: Graph[_Node]) -> bool: ...
