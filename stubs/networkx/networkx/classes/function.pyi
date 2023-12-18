from _typeshed import Incomplete, SupportsItems, SupportsKeysAndGetItem, Unused
from collections.abc import Generator, Hashable, Iterable, Iterator
from typing import TypeVar, overload
from typing_extensions import Literal

from networkx.algorithms.planarity import PlanarEmbedding
from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _NBunch, _Node
from networkx.classes.graphviews import reverse_view as reverse_view, subgraph_view as subgraph_view
from networkx.classes.multigraph import MultiGraph

__all__ = [
    "nodes",
    "edges",
    "degree",
    "degree_histogram",
    "neighbors",
    "number_of_nodes",
    "number_of_edges",
    "density",
    "is_directed",
    "freeze",
    "is_frozen",
    "subgraph",
    "subgraph_view",
    "induced_subgraph",
    "reverse_view",
    "edge_subgraph",
    "restricted_view",
    "to_directed",
    "to_undirected",
    "add_star",
    "add_path",
    "add_cycle",
    "create_empty_copy",
    "set_node_attributes",
    "get_node_attributes",
    "set_edge_attributes",
    "get_edge_attributes",
    "all_neighbors",
    "non_neighbors",
    "non_edges",
    "common_neighbors",
    "is_weighted",
    "is_negatively_weighted",
    "is_empty",
    "selfloop_edges",
    "nodes_with_selfloops",
    "number_of_selfloops",
    "path_weight",
    "is_path",
]
_U = TypeVar("_U")

def nodes(G): ...
def edges(G, nbunch: Incomplete | None = None): ...
def degree(G, nbunch: Incomplete | None = None, weight: Incomplete | None = None): ...
def neighbors(G, n): ...
def number_of_nodes(G): ...
def number_of_edges(G): ...
def density(G): ...
def degree_histogram(G): ...
@overload
def is_directed(G: PlanarEmbedding[Hashable]) -> Literal[False]: ...  # type: ignore[misc] # Incompatible return types
@overload
def is_directed(G: DiGraph[Hashable]) -> Literal[True]: ...  # type: ignore[misc] # Incompatible return types
@overload
def is_directed(G: Graph[Hashable]) -> Literal[False]: ...
def freeze(G): ...
def is_frozen(G): ...
def add_star(G_to_add_to, nodes_for_star, **attr) -> None: ...
def add_path(G_to_add_to, nodes_for_path, **attr) -> None: ...
def add_cycle(G_to_add_to, nodes_for_cycle, **attr) -> None: ...
def subgraph(G, nbunch): ...
def induced_subgraph(G: Graph[_Node], nbunch: _NBunch[_Node]) -> Graph[_Node]: ...
def edge_subgraph(G, edges): ...
def restricted_view(G, nodes, edges): ...
def to_directed(graph): ...
def to_undirected(graph): ...
def create_empty_copy(G, with_data: bool = True): ...

# incomplete: Can "Any scalar value" be enforced?
@overload
def set_node_attributes(G: Graph[Hashable], values: SupportsItems[_Node, Unused], name: str) -> None: ...
@overload
def set_node_attributes(
    G: Graph[_Node],
    values: SupportsItems[_Node, SupportsKeysAndGetItem[Incomplete, Incomplete] | Iterable[tuple[Incomplete, Incomplete]]],
    name: None = None,
) -> None: ...
def get_node_attributes(G: Graph[_Node], name: str) -> dict[_Node, Incomplete]: ...
@overload
def set_edge_attributes(G: Graph[_Node], values: SupportsItems[tuple[_Node, _Node], Incomplete], name: str) -> None: ...
@overload
def set_edge_attributes(G: MultiGraph[_Node], values: dict[tuple[_Node, _Node, Incomplete], Incomplete], name: str) -> None: ...
@overload
def set_edge_attributes(G: Graph[Hashable], values, name: None = None) -> None: ...
def get_edge_attributes(G: Graph[_Node], name: str) -> dict[tuple[_Node, _Node], Incomplete]: ...
def all_neighbors(graph: Graph[_Node], node: _Node) -> Iterator[_Node]: ...
def non_neighbors(graph: Graph[_Node], node: _Node) -> Generator[_Node, None, None]: ...
def non_edges(graph: Graph[_Node]) -> Generator[tuple[_Node, _Node], None, None]: ...
def common_neighbors(G: Graph[_Node], u: _Node, v: _Node) -> Generator[_Node, None, None]: ...
def is_weighted(G: Graph[_Node], edge: tuple[_Node, _Node] | None = None, weight: str = "weight") -> bool: ...
def is_negatively_weighted(G: Graph[_Node], edge: tuple[_Node, _Node] | None = None, weight: str = "weight"): ...
def is_empty(G: Graph[Hashable]) -> bool: ...
def nodes_with_selfloops(G: Graph[_Node]) -> Generator[_Node, None, None]: ...
@overload
def selfloop_edges(
    G: Graph[_Node], data: Literal[False] = False, keys: Literal[False] = False, default=None
) -> Generator[tuple[_Node, _Node], None, None]: ...
@overload
def selfloop_edges(
    G: Graph[_Node], data: Literal[True], keys: Literal[False] = False, default=None
) -> Generator[tuple[_Node, _Node, dict[str, Incomplete]], None, None]: ...
@overload
def selfloop_edges(
    G: Graph[_Node], data: str, keys: Literal[False] = False, default: _U | None = None
) -> Generator[tuple[_Node, _Node, _U], None, None]: ...
@overload
def selfloop_edges(
    G: Graph[_Node], data: Literal[False], keys: Literal[True], default=None
) -> Generator[tuple[_Node, _Node, int], None, None]: ...
@overload
def selfloop_edges(
    G: Graph[_Node], data: Literal[False] = False, *, keys: Literal[True], default=None
) -> Generator[tuple[_Node, _Node, int], None, None]: ...
@overload
def selfloop_edges(
    G: Graph[_Node], data: Literal[True], keys: Literal[True], default=None
) -> Generator[tuple[_Node, _Node, int, dict[str, Incomplete]], None, None]: ...
@overload
def selfloop_edges(
    G: Graph[_Node], data: str, keys: Literal[True], default: _U | None = None
) -> Generator[tuple[_Node, _Node, int, _U], None, None]: ...
def number_of_selfloops(G: Graph[Hashable]) -> int: ...
def is_path(G, path) -> bool: ...
def path_weight(G, path, weight) -> int: ...
