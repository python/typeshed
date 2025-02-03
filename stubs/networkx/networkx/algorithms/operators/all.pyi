from collections.abc import Iterable

from networkx.utils.backends import _dispatchable

@_dispatchable
def union_all(graphs: Iterable, rename: Iterable | None = ()): ...
@_dispatchable
def disjoint_union_all(graphs: Iterable): ...
@_dispatchable
def compose_all(graphs: Iterable): ...
@_dispatchable
def intersection_all(graphs: Iterable): ...
