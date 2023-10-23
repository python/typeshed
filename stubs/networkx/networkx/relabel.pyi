from _typeshed import Incomplete
from collections.abc import Hashable, Mapping
from typing import TypeVar
from typing_extensions import Literal

from networkx.classes.graph import Graph

_X = TypeVar("_X")
_Y = TypeVar("_Y")

def relabel_nodes(G: Graph[_X], mapping: Mapping[_X, _Y], copy: bool = True) -> Graph[_X | _Y]: ...
def convert_node_labels_to_integers(
    G: Graph[Hashable],
    first_label: int = 0,
    ordering: Literal["default", "sorted", "increasing degree", "decreasing degree"] = "default",
    label_attribute: Incomplete | None = None,
) -> Graph[int]: ...
