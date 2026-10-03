from collections.abc import Generator, Hashable
from typing import TypeVar

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

_Node2 = TypeVar("_Node2", bound=Hashable)

__all__ = [
    "vf2pp_all_monomorphisms",
    "vf2pp_is_monomorphic",
    "vf2pp_monomorphism",
    "vf2pp_all_subgraph_isomorphisms",
    "vf2pp_subgraph_is_isomorphic",
    "vf2pp_subgraph_isomorphism",
    "vf2pp_isomorphism",
    "vf2pp_is_isomorphic",
    "vf2pp_all_isomorphisms",
]

@_dispatchable
def vf2pp_isomorphism(
    FG: Graph[_Node], SG: Graph[_Node2], node_label: str | None = None, default_label: object = None
) -> dict[_Node, _Node2] | None: ...
@_dispatchable
def vf2pp_is_isomorphic(
    FG: Graph[_Node], SG: Graph[_Node2], node_label: str | None = None, default_label: object = None
) -> bool: ...
@_dispatchable
def vf2pp_all_isomorphisms(
    FG: Graph[_Node], SG: Graph[_Node2], node_label: str | None = None, default_label: object = None
) -> Generator[dict[_Node, _Node2]]: ...
@_dispatchable
def vf2pp_subgraph_isomorphism(
    FG: Graph[_Node], SG: Graph[_Node2], node_label: str | None = None, default_label: object = None
) -> dict[_Node, _Node2] | None: ...
@_dispatchable
def vf2pp_subgraph_is_isomorphic(
    FG: Graph[_Node], SG: Graph[_Node2], node_label: str | None = None, default_label: object = None
) -> bool: ...
@_dispatchable
def vf2pp_all_subgraph_isomorphisms(
    FG: Graph[_Node], SG: Graph[_Node2], node_label: str | None = None, default_label: object = None
) -> Generator[dict[_Node, _Node2]]: ...
@_dispatchable
def vf2pp_monomorphism(
    FG: Graph[_Node], SG: Graph[_Node2], node_label: str | None = None, default_label: object = None
) -> dict[_Node, _Node2] | None: ...
@_dispatchable
def vf2pp_is_monomorphic(
    FG: Graph[_Node], SG: Graph[_Node2], node_label: str | None = None, default_label: object = None
) -> bool: ...
@_dispatchable
def vf2pp_all_monomorphisms(
    FG: Graph[_Node], SG: Graph[_Node2], node_label: str | None = None, default_label: object = None
) -> Generator[dict[_Node, _Node2]]: ...
