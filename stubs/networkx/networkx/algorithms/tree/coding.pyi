from _typeshed import Incomplete
from collections.abc import Collection

from networkx.classes.graph import Graph, _Node
from networkx.exception import NetworkXException
from networkx.utils.backends import _dispatchable

__all__ = ["from_nested_tuple", "from_prufer_sequence", "NotATree", "to_nested_tuple", "to_prufer_sequence"]

class NotATree(NetworkXException): ...

@_dispatchable
def to_nested_tuple(T: Graph[_Node], root: _Node, canonical_form: bool = False): ...
@_dispatchable
def from_nested_tuple(sequence: Collection[Incomplete], sensible_relabeling: bool = False): ...
@_dispatchable
def to_prufer_sequence(T: Graph[_Node]) -> list[Incomplete]: ...
@_dispatchable
def from_prufer_sequence(sequence: Collection[Incomplete]): ...
