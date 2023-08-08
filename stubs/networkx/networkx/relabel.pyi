from collections.abc import Mapping
from typing import Any, TypeVar
from _typeshed import Incomplete

from networkx.classes.graph import Graph
from typing_extensions import Literal

_X = TypeVar("_X")
_Y = TypeVar("_Y")

def relabel_nodes(
    G: Graph[_X], mapping: Mapping[_X, _Y], copy: bool = ...
) -> Graph[_X | _Y]: ...
def convert_node_labels_to_integers(
    G: Graph[Any],
    first_label: int = ...,
    ordering: Literal[
        "default", "sorted", "increasing degree", "decreasing degree"
    ] = ...,
    label_attribute: Incomplete | None = ...,
) -> Graph[int]: ...
