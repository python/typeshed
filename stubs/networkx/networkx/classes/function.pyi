from _typeshed import Incomplete, SupportsItems, SupportsKeysAndGetItem, Unused
from collections.abc import Callable, Collection, Generator, Hashable, Iterable, Iterator
from typing import Any, Literal, TypeVar, overload

from networkx import _dispatchable
from networkx.algorithms.planarity import PlanarEmbedding
from networkx.classes.digraph import DiGraph
from networkx.classes.graph import Graph, _EdgeData, _NBunch, _Node, _NodeData
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
    "induced_subgraph",
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
    "remove_node_attributes",
    "set_edge_attributes",
    "get_edge_attributes",
    "remove_edge_attributes",
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
    "describe",
]

_U = TypeVar("_U")

def nodes(G: Graph[_Node, _NodeData, _EdgeData]): ...
def edges(G: Graph[_Node, _NodeData, _EdgeData], nbunch=None): ...
def degree(G: Graph[_Node, _NodeData, _EdgeData], nbunch=None, weight=None): ...
def neighbors(G: Graph[_Node, _NodeData, _EdgeData], n): ...
def number_of_nodes(G: Graph[_Node, _NodeData, _EdgeData]): ...
def number_of_edges(G: Graph[_Node, _NodeData, _EdgeData]): ...
def density(G: Graph[_Node, _NodeData, _EdgeData]): ...
def degree_histogram(G: Graph[_Node, _NodeData, _EdgeData]) -> list[int]: ...

@overload
def is_directed(G: PlanarEmbedding[Hashable]) -> Literal[False]: ...  # type: ignore[misc] # Incompatible return types
@overload
def is_directed(G: DiGraph[Hashable]) -> Literal[True]: ...  # type: ignore[misc] # Incompatible return types
@overload
def is_directed(G: Graph[Hashable]) -> Literal[False]: ...

def freeze(G: Graph[_Node, _NodeData, _EdgeData]): ...
def is_frozen(G: Graph[Incomplete]) -> bool: ...
def add_star(G_to_add_to: Graph[Incomplete], nodes_for_star: Iterable[Incomplete], **attr) -> None: ...
def add_path(G_to_add_to: Graph[Incomplete], nodes_for_path: Iterable[Incomplete], **attr) -> None: ...
def add_cycle(G_to_add_to: Graph[Incomplete], nodes_for_cycle: Iterable[Incomplete], **attr) -> None: ...
def subgraph(G: Graph[_Node, _NodeData, _EdgeData], nbunch: Iterable[Incomplete]): ...
def induced_subgraph(G: Graph[_Node, _NodeData, _EdgeData], nbunch: _NBunch[_Node]) -> Graph[_Node, _NodeData, _EdgeData]: ...
def edge_subgraph(G: Graph[_Node, _NodeData, _EdgeData], edges: Iterable[Incomplete]) -> Graph[_Node, _NodeData, _EdgeData]: ...
def restricted_view(
    G: Graph[_Node, _NodeData, _EdgeData], nodes: Iterable[Incomplete], edges: Iterable[Incomplete]
) -> Graph[_Node, _NodeData, _EdgeData]: ...
def to_directed(graph): ...
def to_undirected(graph): ...
def create_empty_copy(G: Graph[_Node, _NodeData, _EdgeData], with_data: bool = True): ...

# incomplete: Can "Any scalar value" be enforced?
@overload
def set_node_attributes(
    G: Graph[Hashable],
    values: SupportsItems[_Node, Unused],
    name: str,
    *,
    backend=None,  # @_dispatchable adds these arguments, but we can't use this decorator with @overload
    **backend_kwargs,
) -> None: ...
@overload
def set_node_attributes(
    G: Graph[_Node, _NodeData, _EdgeData],
    values: SupportsItems[_Node, SupportsKeysAndGetItem[Incomplete, Incomplete] | Iterable[tuple[Incomplete, Incomplete]]],
    name: None = None,
    *,
    backend=None,
    **backend_kwargs,
) -> None: ...

@_dispatchable
def get_node_attributes(G: Graph[_Node, _NodeData, _EdgeData], name: str, default=None) -> dict[_Node, Incomplete]: ...
@_dispatchable
def remove_node_attributes(G: Graph[_Node, _NodeData, _EdgeData], *attr_names, nbunch=None) -> None: ...

@overload
def set_edge_attributes(
    G: Graph[_Node, _NodeData, _EdgeData],
    values: SupportsItems[tuple[_Node, _Node], Incomplete],
    name: str,
    *,
    backend: str | None = None,  # @_dispatchable adds these arguments, but we can't use this decorator with @overload
    **backend_kwargs,
) -> None: ...
@overload
def set_edge_attributes(
    G: MultiGraph[_Node, _NodeData, _EdgeData],
    values: dict[tuple[_Node, _Node, Incomplete], Incomplete],
    name: str,
    *,
    backend: str | None = None,
    **backend_kwargs,
) -> None: ...
@overload
def set_edge_attributes(
    G: Graph[Hashable], values, name: None = None, *, backend: str | None = None, **backend_kwargs
) -> None: ...

@_dispatchable
def get_edge_attributes(
    G: Graph[_Node, _NodeData, _EdgeData], name: str, default=None
) -> dict[tuple[_Node, _Node], Incomplete]: ...
@_dispatchable
def remove_edge_attributes(G: Graph[_Node, _NodeData, _EdgeData], *attr_names, ebunch=None) -> None: ...
def all_neighbors(graph: Graph[_Node, _NodeData, _EdgeData], node: _Node) -> Iterator[_Node]: ...
def non_neighbors(graph: Graph[_Node, _NodeData, _EdgeData], node: _Node) -> Generator[_Node]: ...
def non_edges(graph: Graph[_Node, _NodeData, _EdgeData]) -> Generator[tuple[_Node, _Node]]: ...
def common_neighbors(G: Graph[_Node, _NodeData, _EdgeData], u: _Node, v: _Node) -> Generator[_Node]: ...
@_dispatchable
def is_weighted(
    G: Graph[_Node, _NodeData, _EdgeData], edge: tuple[_Node, _Node] | None = None, weight: str = "weight"
) -> bool: ...
@_dispatchable
def is_negatively_weighted(
    G: Graph[_Node, _NodeData, _EdgeData], edge: tuple[_Node, _Node] | None = None, weight: str = "weight"
) -> bool: ...
@_dispatchable
def is_empty(G: Graph[Hashable]) -> bool: ...
def nodes_with_selfloops(G: Graph[_Node, _NodeData, _EdgeData]) -> Generator[_Node]: ...

@overload
def selfloop_edges(
    G: Graph[_Node, _NodeData, _EdgeData], data: Literal[False] = False, keys: Literal[False] = False, default=None
) -> Generator[tuple[_Node, _Node]]: ...
@overload
def selfloop_edges(
    G: Graph[_Node, _NodeData, _EdgeData], data: Literal[True], keys: Literal[False] = False, default=None
) -> Generator[tuple[_Node, _Node, _EdgeData]]: ...
@overload
def selfloop_edges(
    G: Graph[_Node, Any, Any], data: str, keys: Literal[False] = False, default: _U | None = None
) -> Generator[tuple[_Node, _Node, _U]]: ...
@overload
def selfloop_edges(
    G: Graph[_Node, _NodeData, _EdgeData], data: Literal[False], keys: Literal[True], default=None
) -> Generator[tuple[_Node, _Node, int]]: ...
@overload
def selfloop_edges(
    G: Graph[_Node, _NodeData, _EdgeData], data: Literal[False] = False, *, keys: Literal[True], default=None
) -> Generator[tuple[_Node, _Node, int]]: ...
@overload
def selfloop_edges(
    G: Graph[_Node, _NodeData, _EdgeData], data: Literal[True], keys: Literal[True], default=None
) -> Generator[tuple[_Node, _Node, int, _EdgeData]]: ...
@overload
def selfloop_edges(
    G: Graph[_Node, Any, Any], data: str, keys: Literal[True], default: _U | None = None
) -> Generator[tuple[_Node, _Node, int, _U]]: ...

@_dispatchable
def number_of_selfloops(G: Graph[Hashable]) -> int: ...
def is_path(G: Graph[_Node, _NodeData, _EdgeData], path: Iterable[Incomplete]) -> bool: ...
def path_weight(G: Graph[_Node, _NodeData, _EdgeData], path: Collection[Incomplete], weight: str) -> int: ...
def describe(
    G: Graph[_Node, _NodeData, _EdgeData],
    describe_hook: Callable[[Graph[_Node, _NodeData, _EdgeData]], dict[str, Incomplete]] | None = None,
) -> None: ...
