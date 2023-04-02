from _typeshed import Incomplete
from collections.abc import Iterator
from datetime import datetime
from typing import Any, Generic, TypeVar
from typing_extensions import Literal, Self

from openpyxl.descriptors import Sequence, Strict
from openpyxl.descriptors.base import (
    Bool,
    DateTime,
    Float,
    Integer,
    String,
    _ConvertibleToBool,
    _ConvertibleToFloat,
    _ConvertibleToInt,
)
from openpyxl.descriptors.nested import NestedText

_T = TypeVar("_T")
_N = TypeVar("_N", bound=bool)

# Does not reimplement anything, so runtime also has incompatible supertypes
class NestedBoolText(Bool[_N], NestedText): ...  # type: ignore[misc]

class _TypedProperty(Strict, Generic[_T]):
    name: String[Literal[False]]
    # Since this is internal, just list all possible values
    value: Integer | Float | String[Literal[True]] | DateTime[Literal[False]] | Bool[Literal[False]] | String[Literal[False]]
    def __init__(self, name: str, value: _T) -> None: ...
    def __eq__(self, other: _TypedProperty[Any]) -> bool: ...  # type: ignore[override]

class IntProperty(_TypedProperty[_ConvertibleToInt]):
    value: Integer

class FloatProperty(_TypedProperty[_ConvertibleToFloat]):
    value: Float

class StringProperty(_TypedProperty[str | None]):
    value: String[Literal[True]]

class DateTimeProperty(_TypedProperty[datetime]):
    value: DateTime[Literal[False]]

class BoolProperty(_TypedProperty[_ConvertibleToBool]):
    value: Bool[Literal[False]]

class LinkProperty(_TypedProperty[str]):
    value: String[Literal[False]]

CLASS_MAPPING: Incomplete
XML_MAPPING: Incomplete

class CustomPropertyList(Strict):
    props: Sequence
    def __init__(self) -> None: ...
    @classmethod
    def from_tree(cls, tree) -> Self: ...
    def append(self, prop) -> None: ...
    def to_tree(self): ...
    def __len__(self) -> int: ...
    @property
    def names(self) -> list[str]: ...
    def __getitem__(self, name): ...
    def __delitem__(self, name) -> None: ...
    def __iter__(self) -> Iterator[Incomplete]: ...
