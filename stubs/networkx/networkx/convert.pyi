from _typeshed import Incomplete
from collections.abc import Callable, Iterable

from networkx.classes.graph import Graph, _Data, _Node
from networkx.utils.backends import _dispatchable

__all__ = [
    "from_dict_of_dicts",
    "from_dict_of_lists",
    "from_edgelist",
    "to_dict_of_dicts",
    "to_dict_of_lists",
    "to_edgelist",
    "to_networkx_graph",
]

def to_networkx_graph(
    data: _Data[_Node], create_using: Graph[_Node] | Callable[[], Graph[_Node]] | None = None, multigraph_input: bool = False
) -> Graph[_Node]: ...
@_dispatchable
def to_dict_of_lists(G: Graph[_Node], nodelist: None | Iterable[_Node] = None) -> dict[_Node, list[_Node]]: ...
@_dispatchable
def from_dict_of_lists(d: dict[_Node, Iterable[_Node]], create_using: Incomplete | None = None) -> Graph[_Node]: ...
def to_dict_of_dicts(G: Graph[_Node], nodelist=None, edge_data=None) -> dict[Incomplete, Incomplete]: ...
@_dispatchable
def from_dict_of_dicts(d, create_using=None, multigraph_input=False) -> Graph[Incomplete]: ...
@_dispatchable
def to_edgelist(G: Graph[_Node], nodelist=None): ...
@_dispatchable
def from_edgelist(edgelist, create_using=None) -> Graph[Incomplete]: ...
