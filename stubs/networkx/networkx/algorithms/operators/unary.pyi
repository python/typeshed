from typing import TypeVar

from networkx.classes.digraph import DiGraph

_T = TypeVar("_T")

def complement(G): ...
def reverse(G: DiGraph[_T], copy: bool = True) -> DiGraph[_T]: ...
