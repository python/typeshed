from _typeshed import Incomplete
from typing import TypeVar, overload
from typing_extensions import Literal

from openpyxl.descriptors.base import _ConvertibleToFloat

from . import Integer, MatchPattern, MinMax, String
from .serialisable import Serialisable

_N = TypeVar("_N", bound=bool)

class HexBinary(MatchPattern):
    pattern: str

class UniversalMeasure(MatchPattern):
    pattern: str

class TextPoint(MinMax):
    expected_type: Incomplete
    min: int
    max: int

Coordinate = Integer

class Percentage(MinMax[float, _N]):
    pattern: str
    min: float
    max: float
    @overload  # type:ignore[override]  # Different restrictions
    def __set__(self: Percentage[Literal[True]], instance: Serialisable, value: _ConvertibleToFloat | None) -> None: ...
    @overload
    def __set__(self: Percentage[Literal[False]], instance: Serialisable, value: _ConvertibleToFloat) -> None: ...

class Extension(Serialisable):
    uri: Incomplete
    def __init__(self, uri: Incomplete | None = None) -> None: ...

class ExtensionList(Serialisable):
    ext: Incomplete
    def __init__(self, ext=()) -> None: ...

class Relation(String):
    namespace: Incomplete
    allow_none: bool

class Base64Binary(MatchPattern):
    pattern: str

class Guid(MatchPattern):
    pattern: str

class CellRange(MatchPattern):
    pattern: str
    allow_none: bool
    def __set__(self, instance: Serialisable, value) -> None: ...
