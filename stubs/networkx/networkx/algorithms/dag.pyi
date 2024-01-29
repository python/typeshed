from _typeshed import Incomplete

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatch

@_dispatch
def descendants(G: Graph[_Node], source: _Node) -> set[_Node]: ...
@_dispatch
def ancestors(G: Graph[_Node], source: _Node) -> set[_Node]: ...
@_dispatch
def is_directed_acyclic_graph(G): ...
@_dispatch
def topological_sort(G) -> None: ...
@_dispatch
def lexicographical_topological_sort(G, key: Incomplete | None = None): ...
@_dispatch
def all_topological_sorts(G) -> None: ...
@_dispatch
def is_aperiodic(G): ...
@_dispatch
def transitive_closure(G, reflexive: bool = False): ...
@_dispatch
def transitive_reduction(G): ...
@_dispatch
def antichains(G, topo_order: Incomplete | None = None) -> None: ...
@_dispatch
def dag_longest_path(G, weight: str = "weight", default_weight: int = 1, topo_order: Incomplete | None = None): ...
@_dispatch
def dag_longest_path_length(G, weight: str = "weight", default_weight: int = 1): ...
@_dispatch
def dag_to_branching(G): ...
