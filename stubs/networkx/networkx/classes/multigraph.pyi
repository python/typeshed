from _typeshed import Incomplete
from collections.abc import Mapping
from functools import cached_property
from typing import ClassVar
from typing_extensions import TypeAlias

from networkx.classes.coreviews import MultiAdjacencyView
from networkx.classes.graph import Graph, _MapFactory, _Node
from networkx.classes.multidigraph import MultiDiGraph
from networkx.classes.reportviews import DiMultiDegreeView, MultiDegreeView, MultiEdgeView, OutMultiEdgeView

_MultiEdge: TypeAlias = tuple[_Node, _Node, int]  # noqa: Y047

__all__ = ["MultiGraph"]

class MultiGraph(Graph[_Node]):
    edge_key_dict_factory: ClassVar[_MapFactory]
    def to_directed_class(self) -> type[MultiDiGraph[_Node]]: ...
    def to_undirected_class(self) -> type[MultiGraph[_Node]]: ...
    def __init__(self, incoming_graph_data=None, multigraph_input: bool | None = None, **attr) -> None: ...
    @cached_property
    def adj(self) -> MultiAdjacencyView[_Node, _Node, dict[str, Incomplete]]: ...
    def new_edge_key(self, u: _Node, v: _Node) -> int: ...
    def add_edge(self, u_for_edge, v_for_edge, key=None, **attr): ...  # type: ignore[override]  # Has an additional `key` keyword argument
    def remove_edge(self, u, v, key=None): ...
    def has_edge(self, u, v, key=None) -> bool: ...
    @cached_property
    def edges(self) -> MultiEdgeView[_Node] | OutMultiEdgeView[_Node]: ...  # Include subtypes' possible return types
    def get_edge_data(  # type: ignore[override]  # Has an additional `key` keyword argument
        self, u, v, key=None, default=None
    ) -> Mapping[str, Incomplete]: ...
    @cached_property
    def degree(self) -> MultiDegreeView[_Node] | DiMultiDegreeView[_Node]: ...  # Include subtypes' possible return types
    def to_directed(self, as_view: bool = False) -> MultiDiGraph[_Node]: ...
    def to_undirected(self, as_view: bool = False) -> MultiGraph[_Node]: ...
