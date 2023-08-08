from _typeshed import Incomplete
from collections.abc import Generator

class ISMAGS:
    graph: Incomplete
    subgraph: Incomplete
    node_equality: Incomplete
    edge_equality: Incomplete
    def __init__(
        self,
        graph,
        subgraph,
        node_match: Incomplete | None = None,
        edge_match: Incomplete | None = None,
        cache: Incomplete | None = None,
    ) -> None: ...
    def find_isomorphisms(
        self, symmetry: bool = True
    ) -> Generator[Incomplete, Incomplete, Incomplete]: ...
    def largest_common_subgraph(
        self, symmetry: bool = True
    ) -> Generator[Incomplete, Incomplete, None]: ...
    def analyze_symmetry(self, graph, node_partitions, edge_colors): ...
    def is_isomorphic(self, symmetry: bool = False): ...
    def subgraph_is_isomorphic(self, symmetry: bool = False): ...
    def isomorphisms_iter(
        self, symmetry: bool = True
    ) -> Generator[Incomplete, Incomplete, None]: ...
    def subgraph_isomorphisms_iter(self, symmetry: bool = True): ...
