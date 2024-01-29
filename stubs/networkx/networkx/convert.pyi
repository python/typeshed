from _typeshed import Incomplete

from networkx.utils.backends import _dispatch

__all__ = [
    "to_networkx_graph",
    "from_dict_of_dicts",
    "to_dict_of_dicts",
    "from_dict_of_lists",
    "to_dict_of_lists",
    "from_edgelist",
    "to_edgelist",
]

def to_networkx_graph(data, create_using=None, multigraph_input=False): ...
@_dispatch
def to_dict_of_lists(G, nodelist=None) -> dict[Incomplete, Incomplete]: ...
@_dispatch
def from_dict_of_lists(d, create_using=None): ...
def to_dict_of_dicts(G, nodelist=None, edge_data=None) -> dict[Incomplete, Incomplete]: ...
@_dispatch
def from_dict_of_dicts(d, create_using=None, multigraph_input=False): ...
@_dispatch
def to_edgelist(G, nodelist=None): ...
@_dispatch
def from_edgelist(edgelist, create_using=None): ...
