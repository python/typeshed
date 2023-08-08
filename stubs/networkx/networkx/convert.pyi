from collections.abc import Iterable

import numpy
from _typeshed import Incomplete

# import scipy
from networkx.classes.graph import EdgePlus, Graph, _Node
from typing_extensions import TypeAlias

# this is imported from other stub files
_Data: TypeAlias = (  # noqa: Y047
    Graph[_Node]
    | dict[_Node, dict[_Node, dict[str, Incomplete]]]
    | dict[_Node, Iterable[_Node]]
    | Iterable[EdgePlus[_Node]]
    | numpy.ndarray[_Node, Incomplete]
    # | scipy.sparse.base.spmatrix
)
