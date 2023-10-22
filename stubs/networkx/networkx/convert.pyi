from _typeshed import Incomplete
from collections.abc import Iterable
from typing_extensions import TypeAlias

import numpy

# import scipy
from networkx.classes.graph import Graph, _EdgePlus, _Node

# this is imported from other stub files
_Data: TypeAlias = (  # noqa: Y047
    Graph[_Node]
    | dict[_Node, dict[_Node, dict[str, Incomplete]]]
    | dict[_Node, Iterable[_Node]]
    | Iterable[_EdgePlus[_Node]]
    | numpy.ndarray[_Node, Incomplete]
    # | scipy.sparse.base.spmatrix
)
