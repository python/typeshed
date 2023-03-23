from typing import Protocol, overload
from typing_extensions import Self

from openpyxl.descriptors import Strict, String, Typed

class _HasStr(Protocol):
    def __str__(self) -> str: ...  # noqa: Y029

class TextBlock(Strict):
    font: Typed
    text: String

    def __init__(self, font: Typed, text: String) -> None: ...
    def __eq__(self, other: TextBlock) -> bool: ...  # type: ignore[override]

class CellRichText(list[_HasStr]):
    @overload
    def __init__(self, __args: list[_HasStr] | tuple[_HasStr]) -> None: ...
    @overload
    def __init__(self, *args: _HasStr) -> None: ...
    @classmethod
    def from_tree(cls, node) -> Self: ...
    def __add__(self, arg: _HasStr) -> CellRichText: ...
    def as_list(self) -> list[str]: ...
