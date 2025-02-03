from _typeshed import Incomplete
from collections.abc import Callable, Generator

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def girvan_newman(G: Graph[_Node], most_valuable_edge: Callable = None) -> Generator[Incomplete, None, Incomplete]: ...
