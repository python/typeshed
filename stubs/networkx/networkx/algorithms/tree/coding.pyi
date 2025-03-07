from _typeshed import Incomplete
from collections.abc import Iterable

from networkx.classes.graph import Graph, _Node
from networkx.exception import NetworkXException
from networkx.utils.backends import _dispatchable

class NotATree(NetworkXException): ...

@_dispatchable
def to_nested_tuple(T: Graph[_Node], root: _Node, canonical_form: bool = False): ...
@_dispatchable
def from_nested_tuple(sequence: tuple[Incomplete], sensible_relabeling: bool = False): ...
@_dispatchable
def to_prufer_sequence(T: Graph[_Node]): ...
@_dispatchable
def from_prufer_sequence(sequence: Iterable[Incomplete]): ...
