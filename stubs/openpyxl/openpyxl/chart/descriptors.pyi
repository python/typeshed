from _typeshed import Incomplete
from typing import TypeVar
from typing_extensions import Literal

from openpyxl.chart.data_source import NumFmt
from openpyxl.descriptors import Typed
from openpyxl.descriptors.nested import NestedMinMax
from openpyxl.descriptors.serialisable import Serialisable

_M = TypeVar("_M", int, float)

class NestedGapAmount(NestedMinMax[_M, Incomplete]):
    allow_none: bool
    min: float
    max: float

class NestedOverlap(NestedMinMax[_M, Incomplete]):
    allow_none: bool
    min: float
    max: float

class NumberFormatDescriptor(Typed[NumFmt, Incomplete]):
    expected_type: type[NumFmt]
    allow_none: Literal[True]
    def __set__(self, instance: Serialisable, value) -> None: ...
