from _typeshed import Incomplete
from collections.abc import Callable, Generator, Iterable
from enum import Enum
from typing import Final, Generic, NamedTuple, TypeVar

from networkx.classes.graph import Graph, _Node
from networkx.utils.backends import _dispatchable

_T = TypeVar("_T")

__all__ = ["read_gml", "parse_gml", "generate_gml", "write_gml"]

def escape(text): ...
def unescape(text): ...
def literal_destringizer(rep: str): ...
@_dispatchable
def read_gml(path, label: str = "label", destringizer: Callable[[Incomplete], Incomplete] | None = None): ...
@_dispatchable
def parse_gml(
    lines: str | Iterable[str], label: str = "label", destringizer: Callable[[Incomplete], Incomplete] | None = None
): ...

class Pattern(Enum):
    KEYS = 0
    REALS = 1
    INTS = 2
    STRINGS = 3
    DICT_START = 4
    DICT_END = 5
    COMMENT_WHITESPACE = 6

class Token(NamedTuple, Generic[_T]):
    category: Pattern
    value: _T
    line: int
    position: int

LIST_START_VALUE: Final = "_networkx_list_start"

def parse_gml_lines(lines, label, destringizer): ...
def literal_stringizer(value) -> str: ...
def generate_gml(
    G: Graph[_Node], stringizer: Callable[[Incomplete], str] | None = None
) -> Generator[Incomplete, Incomplete, None]: ...
def write_gml(G: Graph[_Node], path, stringizer: Callable[[Incomplete], str] | None = None) -> None: ...
