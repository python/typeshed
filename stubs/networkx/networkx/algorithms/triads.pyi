from _typeshed import Incomplete
from collections.abc import Generator

from networkx.utils.backends import _dispatch

@_dispatch
def triadic_census(G, nodelist: Incomplete | None = None): ...
@_dispatch
def is_triad(G): ...
@_dispatch
def all_triplets(G): ...
@_dispatch
def all_triads(G) -> Generator[Incomplete, None, None]: ...
@_dispatch
def triads_by_type(G): ...
@_dispatch
def triad_type(G): ...
@_dispatch
def random_triad(G, seed: Incomplete | None = None): ...
