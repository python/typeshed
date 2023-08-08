from _typeshed import Incomplete

def laplacian_matrix(G, nodelist: Incomplete | None = None, weight: str = "weight"): ...
def normalized_laplacian_matrix(
    G, nodelist: Incomplete | None = None, weight: str = "weight"
): ...
def total_spanning_tree_weight(G, weight: Incomplete | None = None): ...
def directed_laplacian_matrix(
    G,
    nodelist: Incomplete | None = None,
    weight: str = "weight",
    walk_type: Incomplete | None = None,
    alpha: float = 0.95,
): ...
def directed_combinatorial_laplacian_matrix(
    G,
    nodelist: Incomplete | None = None,
    weight: str = "weight",
    walk_type: Incomplete | None = None,
    alpha: float = 0.95,
): ...
