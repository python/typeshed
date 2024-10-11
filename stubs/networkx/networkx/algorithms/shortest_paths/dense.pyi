from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

@_dispatchable
def floyd_warshall_numpy(G, nodelist: Incomplete | None = None, weight: str = "weight"): ...
@_dispatchable
def floyd_warshall_predecessor_and_distance(G, weight: str = "weight"): ...
@_dispatchable
def reconstruct_path(source, target, predecessors): ...
@_dispatchable
def floyd_warshall(G, weight: str = "weight"): ...
