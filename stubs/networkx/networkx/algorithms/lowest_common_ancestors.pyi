from _typeshed import Incomplete
from collections.abc import Generator

from networkx.classes.graph import _Node
from networkx.utils.backends import _dispatchable

@_dispatchable
def all_pairs_lowest_common_ancestor(G, pairs=None): ...
@_dispatchable
def lowest_common_ancestor(G, node1, node2, default: object | None = None): ...
@_dispatchable
def tree_all_pairs_lowest_common_ancestor(G, root: _Node | None = None, pairs=None) -> Generator[Incomplete, None, None]: ...
