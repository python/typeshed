from collections.abc import Hashable, Mapping
from functools import cached_property
from typing import Any, ClassVar
from typing_extensions import TypeAlias

from networkx.classes.coreviews import MultiAdjacencyView
from networkx.classes.graph import Graph, _MapFactory, _Node
from networkx.classes.multidigraph import MultiDiGraph
from networkx.classes.reportviews import MultiEdgeView

_MultiEdge: TypeAlias = tuple[_Node, _Node, int]  # noqa: Y047

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
    def get_edge_data(  # type: ignore[override]
        self, u: _Node, v: _Node, key: Hashable | None = None, default: Any = None
    ) -> Mapping[str, Any]: ...
    # key : hashable identifier, optional (default=None)
    # Returns: The edge attribute dictionary, OR a dictionary mapping edge keys to attribute dictionaries
    def copy(self, as_view: bool = False) -> MultiGraph[_Node]: ...
    def to_directed(self, as_view: bool = False) -> MultiDiGraph[_Node]: ...
    def to_undirected(self, as_view: bool = False) -> MultiGraph[_Node]: ...
    def number_of_edges(self, u: _Node | None = None, v: _Node | None = None) -> int: ...
    @cached_property
    def edges(self) -> MultiEdgeView[_Node]: ...  # type: ignore[override]
    # Returns: MultiEdgeView
