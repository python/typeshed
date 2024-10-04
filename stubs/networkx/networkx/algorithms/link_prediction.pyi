from _typeshed import Incomplete

from networkx.utils.backends import _dispatch

@_dispatch
def resource_allocation_index(G, ebunch: Incomplete | None = None): ...
@_dispatch
def jaccard_coefficient(G, ebunch: Incomplete | None = None): ...
@_dispatch
def adamic_adar_index(G, ebunch: Incomplete | None = None): ...
@_dispatch
def common_neighbor_centrality(G, ebunch: Incomplete | None = None, alpha: float = 0.8): ...
@_dispatch
def preferential_attachment(G, ebunch: Incomplete | None = None): ...
@_dispatch
def cn_soundarajan_hopcroft(G, ebunch: Incomplete | None = None, community: str = "community"): ...
@_dispatch
def ra_index_soundarajan_hopcroft(G, ebunch: Incomplete | None = None, community: str = "community"): ...
@_dispatch
def within_inter_cluster(G, ebunch: Incomplete | None = None, delta: float = 0.001, community: str = "community"): ...
