from networkx.utils.backends import _dispatchable

from ..classes.graph import Graph

__all__ = ["is_valid_joint_degree", "is_valid_directed_joint_degree", "joint_degree_graph", "directed_joint_degree_graph"]

@_dispatchable
def is_valid_joint_degree(joint_degrees) -> bool: ...
@_dispatchable
def joint_degree_graph(joint_degrees, seed=None) -> Graph[Incomplete]: ...
@_dispatchable
def is_valid_directed_joint_degree(in_degrees, out_degrees, nkk) -> bool: ...
@_dispatchable
def directed_joint_degree_graph(in_degrees, out_degrees, nkk, seed=None) -> Graph[Incomplete]: ...
