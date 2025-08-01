from collections.abc import Hashable
from functools import cached_property
from typing import Any, ClassVar
from typing_extensions import TypeAlias

from networkx.classes.coreviews import MultiAdjacencyView
from networkx.classes.graph import Graph, _MapFactory, _Node
from networkx.classes.multidigraph import MultiDiGraph
from networkx.classes.reportviews import OutMultiEdgeView

_MultiEdge: TypeAlias = tuple[_Node, _Node, int]  # noqa: Y047

__all__ = ["MultiGraph"]

class MultiGraph(Graph[_Node]):
    edge_key_dict_factory: ClassVar[_MapFactory]
    def __init__(self, incoming_graph_data=None, multigraph_input: bool | None = None, **attr: object) -> None: ...
    @cached_property
    def adj(self) -> MultiAdjacencyView[_Node, _Node, dict[str, Any]]: ...  # data can be any type
    def new_edge_key(self, u: _Node, v: _Node) -> int: ...
    def add_edge(  # type: ignore[override]  # Has an additional `key` keyword argument
        self, u_for_edge: _Node, v_for_edge: _Node, key: Hashable | None = None, **attr: object
    ): ...
    def remove_edge(self, u: _Node, v: _Node, key: Hashable | None = None) -> None: ...
    def has_edge(self, u: _Node, v: _Node, key: Hashable | None = None) -> bool: ...
    def get_edge_data(  # type: ignore[override]  # Has an additional `key` keyword argument
        self, u: _Node, v: _Node, key: Hashable | None = None, default: object | None = None
    ) -> dict[str, Any]: ...  # data can be any type
    def copy(self, as_view: bool = False) -> MultiGraph[_Node]: ...
    def to_directed(self, as_view: bool = False) -> MultiDiGraph[_Node]: ...
    def to_undirected(self, as_view: bool = False) -> MultiGraph[_Node]: ...
    def number_of_edges(self, u: _Node | None = None, v: _Node | None = None) -> int: ...
    @cached_property
    def edges(self) -> OutMultiEdgeView[_Node]: ...
