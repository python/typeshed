from _typeshed import Incomplete
from typing import TypeVar

from openpyxl.descriptors.serialisable import Serialisable

from .base import Bool, Convertible, Descriptor, Float, Integer, MinMax, NoneSet, Set, String

_N = TypeVar("_N", bound=bool)
_M = TypeVar("_M", int, float)

# NOTE: # type: ignore[misc]: Class does not reimplement the relevant methods, so runtime also has incompatible supertypes

class Nested(Descriptor[Incomplete]):
    nested: bool
    attribute: str
    def __set__(self, instance: Serialisable, value) -> None: ...
    def from_tree(self, node): ...
    def to_tree(
        self, tagname: Incomplete | None = None, value: Incomplete | None = None, namespace: Incomplete | None = None
    ): ...

class NestedValue(Nested, Convertible[Incomplete, Incomplete]): ...  # type: ignore[misc]

class NestedText(NestedValue):
    def from_tree(self, node): ...
    def to_tree(
        self, tagname: Incomplete | None = None, value: Incomplete | None = None, namespace: Incomplete | None = None
    ): ...

class NestedFloat(NestedValue, Float[Incomplete]): ...  # type: ignore[misc]
class NestedInteger(NestedValue, Integer[Incomplete]): ...  # type: ignore[misc]
class NestedString(NestedValue, String[Incomplete]): ...  # type: ignore[misc]

class NestedBool(NestedValue, Bool[Incomplete]):  # type: ignore[misc]
    def from_tree(self, node): ...

class NestedNoneSet(Nested, NoneSet[Incomplete]): ...
class NestedSet(Nested, Set[Incomplete]): ...

class NestedMinMax(Nested, MinMax[_M, _N]):  # type: ignore[misc]
    expected_type: type[_M]
    allow_none: _N

class EmptyTag(Nested, Bool[Incomplete]):  # type: ignore[misc]
    def from_tree(self, node): ...
    def to_tree(
        self, tagname: Incomplete | None = None, value: Incomplete | None = None, namespace: Incomplete | None = None
    ): ...
