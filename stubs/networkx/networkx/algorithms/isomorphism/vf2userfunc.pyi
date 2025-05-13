from _typeshed import Incomplete
from collections.abc import Callable

from ...classes.graph import Graph
from . import isomorphvf2 as vf2

__all__ = ["GraphMatcher", "DiGraphMatcher", "MultiGraphMatcher", "MultiDiGraphMatcher"]

class GraphMatcher(vf2.GraphMatcher):
    node_match: Incomplete
    edge_match: Incomplete
    G1_adj: Incomplete
    G2_adj: Incomplete

    def __init__(
        self,
        G1: Graph[Incomplete],
        G2: Graph[Incomplete],
        node_match: Callable[..., Incomplete] | None = None,
        edge_match: Callable[..., Incomplete] | None = None,
    ) -> None: ...
    def semantic_feasibility(self, G1_node, G2_node): ...

class DiGraphMatcher(vf2.DiGraphMatcher):
    node_match: Incomplete
    edge_match: Incomplete
    G1_adj: Incomplete
    G2_adj: Incomplete

    def __init__(
        self,
        G1: Graph[Incomplete],
        G2: Graph[Incomplete],
        node_match: Callable[..., Incomplete] | None = None,
        edge_match: Callable[..., Incomplete] | None = None,
    ) -> None: ...
    def semantic_feasibility(self, G1_node, G2_node): ...

class MultiGraphMatcher(GraphMatcher): ...
class MultiDiGraphMatcher(DiGraphMatcher): ...
