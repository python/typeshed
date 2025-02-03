from _typeshed import Incomplete
from collections.abc import Callable, Generator

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable
from numpy.random import RandomState

@_dispatchable
def graph_edit_distance(
    G1,
    G2,
    node_match: Callable = None,
    edge_match: Callable = None,
    node_subst_cost=None,
    node_del_cost=None,
    node_ins_cost=None,
    edge_subst_cost=None,
    edge_del_cost=None,
    edge_ins_cost=None,
    roots=None,
    upper_bound: float = None,
    timeout: float = None,
): ...
@_dispatchable
def optimal_edit_paths(
    G1,
    G2,
    node_match: Callable = None,
    edge_match: Callable = None,
    node_subst_cost=None,
    node_del_cost=None,
    node_ins_cost=None,
    edge_subst_cost=None,
    edge_del_cost=None,
    edge_ins_cost=None,
    upper_bound: float = None,
): ...
@_dispatchable
def optimize_graph_edit_distance(
    G1,
    G2,
    node_match: Callable = None,
    edge_match: Callable = None,
    node_subst_cost=None,
    node_del_cost=None,
    node_ins_cost=None,
    edge_subst_cost=None,
    edge_del_cost=None,
    edge_ins_cost=None,
    upper_bound: float = None,
) -> Generator[Incomplete, None, None]: ...
@_dispatchable
def optimize_edit_paths(
    G1,
    G2,
    node_match: Callable = None,
    edge_match: Callable = None,
    node_subst_cost=None,
    node_del_cost=None,
    node_ins_cost=None,
    edge_subst_cost=None,
    edge_del_cost=None,
    edge_ins_cost=None,
    upper_bound: float = None,
    strictly_decreasing: bool = True,
    roots=None,
    timeout: float = None,
) -> Generator[Incomplete, None, Incomplete]: ...
@_dispatchable
def simrank_similarity(
    G: Graph[_Node],
    source: _Node = None,
    target: _Node = None,
    importance_factor: float = 0.9,
    max_iterations: int = 1000,
    tolerance: float = 0.0001,
): ...
@_dispatchable
def panther_similarity(
    G: Graph[_Node],
    source: _Node,
    k: int = 5,
    path_length: int = 5,
    c: float = 0.5,
    delta: float = 0.1,
    eps=None,
    weight: str | None = "weight",
): ...
@_dispatchable
def generate_random_paths(
    G: Graph[_Node],
    sample_size: int,
    path_length: int = 5,
    index_map: dict | None = None,
    weight: str | None = "weight",
    seed: int | RandomState | None = None,
) -> Generator[Incomplete, None, None]: ...
