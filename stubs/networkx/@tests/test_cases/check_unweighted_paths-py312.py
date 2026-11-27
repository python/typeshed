from collections import UserDict
from typing import Any

import networkx as nx


def unweighted_paths_with_custom_attributes(graph: nx.Graph[int, UserDict[str, Any], UserDict[str, Any]]) -> None:
    nx.single_source_shortest_path_length(graph, 0)
    nx.single_target_shortest_path_length(graph, 2)
    nx.all_pairs_shortest_path_length(graph)
    nx.bidirectional_shortest_path(graph, 0, 2)
    nx.single_source_shortest_path(graph, 0)
    nx.single_target_shortest_path(graph, 2)
    nx.all_pairs_shortest_path(graph)
    nx.predecessor(graph, 0)
