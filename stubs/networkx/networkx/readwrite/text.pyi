from _typeshed import Incomplete
from collections.abc import Generator

__all__ = ["forest_str", "generate_network_text", "write_network_text"]

class _AsciiBaseGlyphs:
    empty: str
    newtree_last: str
    newtree_mid: str
    endof_forest: str
    within_forest: str
    within_tree: str

class AsciiDirectedGlyphs(_AsciiBaseGlyphs):
    last: str
    mid: str
    backedge: str

class AsciiUndirectedGlyphs(_AsciiBaseGlyphs):
    last: str
    mid: str
    backedge: str

class _UtfBaseGlyphs:
    empty: str
    newtree_last: str
    newtree_mid: str
    endof_forest: str
    within_forest: str
    within_tree: str

class UtfDirectedGlyphs(_UtfBaseGlyphs):
    last: str
    mid: str
    backedge: str

class UtfUndirectedGlyphs(_UtfBaseGlyphs):
    last: str
    mid: str
    backedge: str

def generate_network_text(
    graph,
    with_labels: bool = True,
    sources: Incomplete | None = None,
    max_depth: Incomplete | None = None,
    ascii_only: bool = False,
) -> Generator[Incomplete, None, Incomplete]: ...
def write_network_text(
    graph,
    path: Incomplete | None = None,
    with_labels: bool = True,
    sources: Incomplete | None = None,
    max_depth: Incomplete | None = None,
    ascii_only: bool = False,
    end: str = "\n",
) -> None: ...
def forest_str(
    graph, with_labels: bool = True, sources: Incomplete | None = None, write: Incomplete | None = None, ascii_only: bool = False
): ...
