from collections.abc import Iterable
from typing import Any, TypeAlias, overload
from typing_extensions import Self

from openpyxl.descriptors import Strict, String, Typed

class TextBlock(Strict):
    font: Typed
    text: String

    def __init__(self, font: Typed, text: String) -> None: ...
    def __eq__(self, other: TextBlock) -> bool: ...  # type: ignore[override]

# CellRichText accepts any object, which can be converted to a string,
# which is every object.
_HasStr: TypeAlias = Any

class CellRichText(list[_HasStr]):
    @overload
    def __init__(self, __args: list[_HasStr] | tuple[_HasStr]) -> None: ...
    @overload
    def __init__(self, *args: _HasStr) -> None: ...
    @classmethod
    def from_tree(cls, node) -> Self: ...
    def __add__(self, arg: _HasStr) -> CellRichText: ...
    def append(self, arg: _HasStr) -> None: ...
    def extend(self, arg: Iterable[_HasStr]) -> None: ...
    def as_list(self) -> list[str]: ...
