from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any

from ...classes.digraph import DiGraph
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
        # Any: G1 and G2 can have unrelated node and data types
        G1: Graph[Any, Any, Any],
        G2: Graph[Any, Any, Any],
        node_match: Callable[[Incomplete, Incomplete], object] | None = None,
        edge_match: Callable[[Incomplete, Incomplete], object] | None = None,
    ) -> None: ...
    def semantic_feasibility(self, G1_node, G2_node): ...

class DiGraphMatcher(vf2.DiGraphMatcher):
    node_match: Incomplete
    edge_match: Incomplete
    G1_adj: Incomplete
    G2_adj: Incomplete

    def __init__(
        self,
        # Any: G1 and G2 can have unrelated node and data types
        G1: DiGraph[Any, Any, Any],
        G2: DiGraph[Any, Any, Any],
        node_match: Callable[[Incomplete, Incomplete], object] | None = None,
        edge_match: Callable[[Incomplete, Incomplete], object] | None = None,
    ) -> None: ...
    def semantic_feasibility(self, G1_node, G2_node): ...

class MultiGraphMatcher(GraphMatcher): ...
class MultiDiGraphMatcher(DiGraphMatcher): ...
