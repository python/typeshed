from _typeshed import Incomplete
from collections.abc import Callable, Generator
from typing import ClassVar

from networkx.classes.digraph import DiGraph

__all__ = ["generate_network_text", "write_network_text"]

class BaseGlyphs:
    @classmethod
    def as_dict(cls) -> dict[str, str]: ...

class AsciiBaseGlyphs(BaseGlyphs):
    empty: ClassVar[str]
    newtree_last: ClassVar[str]
    newtree_mid: ClassVar[str]
    endof_forest: ClassVar[str]
    within_forest: ClassVar[str]
    within_tree: ClassVar[str]

class AsciiDirectedGlyphs(AsciiBaseGlyphs):
    last: ClassVar[str]
    mid: ClassVar[str]
    backedge: ClassVar[str]
    vertical_edge: ClassVar[str]

class AsciiUndirectedGlyphs(AsciiBaseGlyphs):
    last: ClassVar[str]
    mid: ClassVar[str]
    backedge: ClassVar[str]
    vertical_edge: ClassVar[str]

class UtfBaseGlyphs(BaseGlyphs):
    empty: ClassVar[str]
    newtree_last: ClassVar[str]
    newtree_mid: ClassVar[str]
    endof_forest: ClassVar[str]
    within_forest: ClassVar[str]
    within_tree: ClassVar[str]

class UtfDirectedGlyphs(UtfBaseGlyphs):
    last: ClassVar[str]
    mid: ClassVar[str]
    backedge: ClassVar[str]
    vertical_edge: ClassVar[str]

class UtfUndirectedGlyphs(UtfBaseGlyphs):
    last: ClassVar[str]
    mid: ClassVar[str]
    backedge: ClassVar[str]
    vertical_edge: ClassVar[str]

def generate_network_text(
    graph: DiGraph[Incomplete],
    with_labels: bool = True,
    sources: list[Incomplete] = None,
    max_depth: int = None,
    ascii_only: bool = False,
    vertical_chains: bool = False,
) -> Generator[Incomplete, None, Incomplete]: ...
def write_network_text(
    graph: DiGraph[Incomplete],
    path: Callable[..., Incomplete] = None,
    with_labels: bool = True,
    sources: list[Incomplete] = None,
    max_depth: int = None,
    ascii_only: bool = False,
    end: str = "\n",
    vertical_chains: bool = False,
) -> None: ...
