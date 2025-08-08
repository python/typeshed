from collections.abc import Hashable, Mapping
from functools import cached_property
from typing import Any, ClassVar, overload
from typing_extensions import TypeAlias, TypeVar

from networkx.classes.coreviews import MultiAdjacencyView
from networkx.classes.graph import Graph, _MapFactory, _Node
from networkx.classes.multidigraph import MultiDiGraph
from networkx.classes.reportviews import MultiEdgeView

_MultiEdge: TypeAlias = tuple[_Node, _Node, int]  # noqa: Y047

_Any = TypeVar("_Any")

__all__ = ["MultiGraph"]

class MultiGraph(Graph[_Node]):
    edge_key_dict_factory: ClassVar[_MapFactory]
    def __init__(self, incoming_graph_data=None, multigraph_input: bool | None = None, **attr: Any) -> None: ...
    @cached_property
    def adj(self) -> MultiAdjacencyView[_Node, _Node, Mapping[str, Any]]: ...
    def new_edge_key(self, u: _Node, v: _Node) -> int: ...
    def add_edge(  # type: ignore[override]
        self, u_for_edge: _Node, v_for_edge: _Node, key: Hashable | int | None = None, **attr: Any
    ) -> Hashable | int: ...
    # key : hashable identifier, optional (default=lowest unused integer)
    def remove_edge(self, u, v, key=None): ...
    def has_edge(self, u: _Node, v: _Node, key=None) -> bool: ...
    @overload  # type: ignore[override]
    def get_edge_data(self, u: _Node, v: _Node, key: Hashable, default: _Any | None = None) -> Mapping[str, Any] | _Any: ...
    # key : hashable identifier, optional (default=None).
    # default : any Python object (default=None). Value to return if the specific edge (u, v, key) is not found.
    # Returns: The edge attribute dictionary.
    @overload
    def get_edge_data(
        self, u: _Node, v: _Node, key: None = None, default: _Any | None = None
    ) -> Mapping[Hashable, Mapping[str, Any] | _Any]: ...
    # default : any Python object (default=None). Value to return if there are no edges between u and v and no key is specified.
    # Returns: A dictionary mapping edge keys to attribute dictionaries for each of those edges if no specific key is provided.
    def copy(self, as_view: bool = False) -> MultiGraph[_Node]: ...
    def to_directed(self, as_view: bool = False) -> MultiDiGraph[_Node]: ...
    def to_undirected(self, as_view: bool = False) -> MultiGraph[_Node]: ...
    def number_of_edges(self, u: _Node | None = None, v: _Node | None = None) -> int: ...
    @cached_property
    def edges(self) -> MultiEdgeView[_Node]: ...  # type: ignore[override]
    # Returns: MultiEdgeView
