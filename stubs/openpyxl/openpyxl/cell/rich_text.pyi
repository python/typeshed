from collections.abc import Iterable
from typing import Any, overload
from typing_extensions import Self, TypeAlias

from openpyxl.descriptors import Strict, String, Typed

class TextBlock(Strict):
    font: Typed
    text: String

    def __init__(self, font: Typed, text: String) -> None: ...
    def __eq__(self, other: TextBlock) -> bool: ...  # type: ignore[override]

# CellRichText accepts any object that can be converted to a string,
# which is every object.
_HasStr: TypeAlias = Any

class CellRichText(list[str | TextBlock]):
    @overload
    def __init__(self, __args: list[str] | list[TextBlock] | list[str | TextBlock] | tuple[str | TextBlock, ...]) -> None: ...
    @overload
    def __init__(self, *args: str | TextBlock) -> None: ...
    @classmethod
    def from_tree(cls, node) -> Self: ...
    def __add__(self, arg: Iterable[str | TextBlock]) -> CellRichText: ...
    def append(self, arg: str | TextBlock) -> None: ...
    def extend(self, arg: Iterable[str | TextBlock]) -> None: ...
    def as_list(self) -> list[str]: ...
