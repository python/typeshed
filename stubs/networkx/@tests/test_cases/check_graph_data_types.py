from __future__ import annotations

from collections.abc import Iterator, Mapping
from typing import Any
from typing_extensions import assert_type

import networkx as nx
from networkx.utils.rcm import reverse_cuthill_mckee_ordering


class NodeData(Mapping[str, Any]):
    def __getitem__(self, key: str) -> Any: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...


# Functions that only read a graph accept any node/edge data types that satisfy
# the `Mapping[str, Any]` bound, not just the `dict[str, Any]` default.
G = nx.Graph[int, NodeData, dict[str, Any]]()
assert_type(nx.degree_histogram(G), list[int])
assert_type(nx.to_dict_of_lists(G), dict[int, list[int]])
assert_type(nx.is_weighted(G), bool)
nx.number_of_nodes(G)
nx.write_gml(G, "graph.gml")
nx.generate_adjlist(G)
nx.node_link_data(G)
nx.adjacency_matrix(G)
nx.laplacian_spectrum(G)
reverse_cuthill_mckee_ordering(G)

D = nx.DiGraph[str, NodeData, NodeData]()
nx.number_of_edges(D)
nx.write_edgelist(D, "graph.edgelist")
nx.directed_laplacian_matrix(D)

# Views keep the data types of the graph they come from.
assert_type(nx.edge_subgraph(G, [(1, 2)]), nx.Graph[int, NodeData, dict[str, Any]])
assert_type(nx.restricted_view(G, [1], [(1, 2)]), nx.Graph[int, NodeData, dict[str, Any]])

# The default data types work as before.
H = nx.Graph[str]()
assert_type(nx.to_dict_of_lists(H), dict[str, list[str]])
nx.write_gml(H, "graph.gml")
