from _typeshed import Incomplete

def group_betweenness_centrality(
    G,
    C,
    normalized: bool = True,
    weight: Incomplete | None = None,
    endpoints: bool = False,
): ...
def prominent_group(
    G,
    k,
    weight: Incomplete | None = None,
    C: Incomplete | None = None,
    endpoints: bool = False,
    normalized: bool = True,
    greedy: bool = False,
): ...
def group_closeness_centrality(G, S, weight: Incomplete | None = None): ...
def group_degree_centrality(G, S): ...
def group_in_degree_centrality(G, S): ...
def group_out_degree_centrality(G, S): ...
