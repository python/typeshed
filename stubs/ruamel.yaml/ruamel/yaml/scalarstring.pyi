from collections.abc import Callable, Mapping
from typing import Any, Final, Self, SupportsIndex

from .anchor import Anchor
from .comments import CommentedMap, CommentedSeq
from .nodes import _ScalarNodeStyle

__all__ = [
    "ScalarString",
    "LiteralScalarString",
    "FoldedScalarString",
    "SingleQuotedScalarString",
    "DoubleQuotedScalarString",
    "PlainScalarString",
    "PreservedScalarString",
]

class ScalarString(str):
    def __new__(cls, value: str, /, *, anchor: str | None = None) -> Self: ...
    def replace(self, old: str, new: str, maxreplace: SupportsIndex = -1, /) -> Self: ...
    @property
    def anchor(self) -> Anchor: ...
    def yaml_anchor(self, *, any: bool = False) -> Anchor: ...
    def yaml_set_anchor(self, value: str, /, *, always_dump: bool = False) -> None: ...

class LiteralScalarString(ScalarString):
    style: Final[_ScalarNodeStyle] = "|"
    comment: str
    def __new__(cls, value: str, /, *, anchor: str | None = None) -> Self: ...

PreservedScalarString = LiteralScalarString

class FoldedScalarString(ScalarString):
    style: Final[_ScalarNodeStyle] = ">"
    fold_pos: list[int]
    comment: str
    def __new__(cls, value: str, /, *, anchor: str | None = None) -> Self: ...

class SingleQuotedScalarString(ScalarString):
    style: Final[_ScalarNodeStyle] = "'"
    def __new__(cls, value: str, /, *, anchor: str | None = None) -> Self: ...

class DoubleQuotedScalarString(ScalarString):
    style: Final[_ScalarNodeStyle] = '"'
    def __new__(cls, value: str, /, *, anchor: str | None = None) -> Self: ...

class PlainScalarString(ScalarString):
    style: Final[_ScalarNodeStyle] = ""
    def __new__(cls, value: str, /, *, anchor: str | None = None) -> Self: ...

def preserve_literal(s: str, /) -> str: ...
def walk_tree(
    base: CommentedMap[Any, Any] | CommentedSeq[Any], map: Mapping[str, Callable[[str], str]] | None = None
) -> None: ...
