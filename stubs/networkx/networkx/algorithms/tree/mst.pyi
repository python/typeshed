from _typeshed import Incomplete
from enum import Enum

class EdgePartition(Enum):
    OPEN: int
    INCLUDED: int
    EXCLUDED: int

def minimum_spanning_edges(
    G,
    algorithm: str = "kruskal",
    weight: str = "weight",
    keys: bool = True,
    data: bool = True,
    ignore_nan: bool = False,
): ...
def maximum_spanning_edges(
    G,
    algorithm: str = "kruskal",
    weight: str = "weight",
    keys: bool = True,
    data: bool = True,
    ignore_nan: bool = False,
): ...
def minimum_spanning_tree(
    G, weight: str = "weight", algorithm: str = "kruskal", ignore_nan: bool = False
): ...
def partition_spanning_tree(
    G,
    minimum: bool = True,
    weight: str = "weight",
    partition: str = "partition",
    ignore_nan: bool = False,
): ...
def maximum_spanning_tree(
    G, weight: str = "weight", algorithm: str = "kruskal", ignore_nan: bool = False
): ...
def random_spanning_tree(
    G,
    weight: Incomplete | None = None,
    *,
    multiplicative: bool = True,
    seed: Incomplete | None = None
): ...

class SpanningTreeIterator:
    class Partition:
        mst_weight: float
        partition_dict: dict[Incomplete, Incomplete]
        def __copy__(self): ...
        def __init__(self, mst_weight, partition_dict) -> None: ...
        def __lt__(self, other): ...
        def __gt__(self, other): ...
        def __le__(self, other): ...
        def __ge__(self, other): ...
    G: Incomplete
    weight: Incomplete
    minimum: Incomplete
    ignore_nan: Incomplete
    partition_key: str
    def __init__(
        self, G, weight: str = "weight", minimum: bool = True, ignore_nan: bool = False
    ) -> None: ...
    partition_queue: Incomplete
    def __iter__(self): ...
    def __next__(self): ...
