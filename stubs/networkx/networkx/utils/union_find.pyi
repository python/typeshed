from _typeshed import Incomplete
from collections.abc import Generator

class UnionFind:
    parents: Incomplete
    weights: Incomplete
    def __init__(self, elements: Incomplete | None = None) -> None: ...
    def __getitem__(self, object): ...
    def __iter__(self): ...
    def to_sets(self) -> Generator[Incomplete, Incomplete, None]: ...
    def union(self, *objects): ...
