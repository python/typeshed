from _typeshed import Incomplete
from collections.abc import Generator

from networkx.utils.backends import _dispatchable

@_dispatchable
def single_source_shortest_path_length(G, source, cutoff: Incomplete | None = None): ...
@_dispatchable
def single_target_shortest_path_length(G, target, cutoff: Incomplete | None = None): ...
@_dispatchable
def all_pairs_shortest_path_length(G, cutoff: Incomplete | None = None) -> Generator[Incomplete, None, None]: ...
@_dispatchable
def bidirectional_shortest_path(G, source, target): ...
@_dispatchable
def single_source_shortest_path(G, source, cutoff: Incomplete | None = None): ...
@_dispatchable
def single_target_shortest_path(G, target, cutoff: Incomplete | None = None): ...
@_dispatchable
def all_pairs_shortest_path(G, cutoff: Incomplete | None = None) -> Generator[Incomplete, None, None]: ...
@_dispatchable
def predecessor(
    G, source, target: Incomplete | None = None, cutoff: Incomplete | None = None, return_seen: Incomplete | None = None
): ...
