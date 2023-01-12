from openpyxl.chart.data_source import NumFmt
from openpyxl.descriptors import Typed
from openpyxl.descriptors.nested import NestedMinMax

class NestedGapAmount(NestedMinMax):
    allow_none: bool
    min: int
    max: int

class NestedOverlap(NestedMinMax):
    allow_none: bool
    min: int
    max: int

class NumberFormatDescriptor(Typed):
    expected_type: type[NumFmt]
    allow_none: bool
    def __set__(self, instance, value) -> None: ...
