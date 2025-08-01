from _typeshed import Incomplete
from functools import cached_property

from networkx.classes.coreviews import MultiAdjacencyView
from networkx.classes.digraph import DiGraph
from networkx.classes.graph import _Node
from networkx.classes.multigraph import MultiGraph
from networkx.classes.reportviews import DiMultiDegreeView, InMultiDegreeView, OutMultiDegreeView, OutMultiEdgeView

__all__ = ["MultiDiGraph"]

class MultiDiGraph(MultiGraph[_Node], DiGraph[_Node]):
    @cached_property
    def succ(self) -> MultiAdjacencyView[_Node, _Node, dict[str, Incomplete]]: ...
    @cached_property
    def pred(self) -> MultiAdjacencyView[_Node, _Node, dict[str, Incomplete]]: ...
    @cached_property
    def edges(self) -> OutMultiEdgeView[_Node]: ...
    @cached_property
    def out_edges(self) -> OutMultiEdgeView[_Node]: ...
    @cached_property
    def degree(self) -> DiMultiDegreeView[_Node]: ...
    @cached_property
    def in_edges(self) -> OutMultiEdgeView[_Node]: ...
    @cached_property
    def in_degree(self) -> InMultiDegreeView[_Node]: ...
    @cached_property
    def out_degree(self) -> OutMultiDegreeView[_Node]: ...
    def to_undirected(self, reciprocal: bool = False, as_view: bool = False) -> MultiGraph[_Node]: ...  # type: ignore[override]
