from _typeshed import Incomplete
from collections.abc import Generator
from enum import Enum
from typing import Generic, NamedTuple, TypeVar

_T = TypeVar("_T")

__all__ = ["read_gml", "parse_gml", "generate_gml", "write_gml"]

def read_gml(path, label: str = "label", destringizer: Incomplete | None = None): ...
def parse_gml(lines, label: str = "label", destringizer: Incomplete | None = None): ...

class Pattern(Enum):
    KEYS: int
    REALS: int
    INTS: int
    STRINGS: int
    DICT_START: int
    DICT_END: int
    COMMENT_WHITESPACE: int

class Token(NamedTuple, Generic[_T]):
    category: Pattern
    value: _T
    line: int
    position: int

def generate_gml(G, stringizer: Incomplete | None = None) -> Generator[Incomplete, Incomplete, None]: ...
def write_gml(G, path, stringizer: Incomplete | None = None) -> None: ...
