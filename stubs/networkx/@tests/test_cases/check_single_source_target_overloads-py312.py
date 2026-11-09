from typing_extensions import assert_type

import networkx as nx

G: "nx.Graph[int]" = nx.Graph([(1, 2), (2, 3), (3, 4)])

# With target => (distance, path)
assert_type(nx.single_source_dijkstra(G, 1, 4), tuple[float, list[int]])
assert_type(nx.single_source_bellman_ford(G, 1, 4), tuple[float, list[int]])
assert_type(nx.multi_source_dijkstra(G, {1, 2}, 4), tuple[float, list[int]])

# Without target => (distances, paths)
assert_type(nx.single_source_dijkstra(G, 1), tuple[dict[int, float], dict[int, list[int]]])
assert_type(nx.single_source_bellman_ford(G, 1), tuple[dict[int, float], dict[int, list[int]]])
assert_type(nx.multi_source_dijkstra(G, {1, 2}), tuple[dict[int, float], dict[int, list[int]]])
