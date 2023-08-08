from collections.abc import Callable, Iterable
from typing import overload
from _typeshed import Incomplete

from networkx.classes.graph import Graph, _Node
from typing_extensions import Literal

def bridges(G: Graph[_Node], root: _Node | None = ...) -> Iterable[_Node]: ...
def has_bridges(G: Graph[_Node], root: Incomplete | None = ...) -> bool: ...
@overload
def local_bridges(
    G: Graph[_Node],
    with_span: Literal[False] = ...,
    weight: str | Callable[[_Node], float] | None = ...,
) -> Iterable[tuple[_Node, _Node]]: ...
@overload
def local_bridges(
    G: Graph[_Node],
    with_span: Literal[True] = ...,
    weight: str | Callable[[_Node], float] | None = ...,
) -> Iterable[tuple[_Node, _Node, int]]: ...
