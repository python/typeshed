from typing import Any

from openpyxl.descriptors import (
    Alias as Alias,
    Bool as Bool,
    Convertible as Convertible,
    Integer as Integer,
    NoneSet as NoneSet,
    Sequence as Sequence,
    String as String,
)
from openpyxl.descriptors.nested import NestedText as NestedText
from openpyxl.descriptors.serialisable import Serialisable as Serialisable
from openpyxl.utils import (
    coordinate_to_tuple as coordinate_to_tuple,
    get_column_letter as get_column_letter,
    rows_from_range as rows_from_range,
)

from .cell_range import MultiCellRange as MultiCellRange

def collapse_cell_addresses(cells, input_ranges=...): ...
def expand_cell_ranges(range_string): ...

class DataValidation(Serialisable):
    tagname: str
    sqref: Any
    cells: Any
    ranges: Any
    showErrorMessage: Any
    showDropDown: Any
    hide_drop_down: Any
    showInputMessage: Any
    allowBlank: Any
    allow_blank: Any
    errorTitle: Any
    error: Any
    promptTitle: Any
    prompt: Any
    formula1: Any
    formula2: Any
    type: Any
    errorStyle: Any
    imeMode: Any
    operator: Any
    validation_type: Any
    def __init__(
        self,
        type: Any | None = ...,
        formula1: Any | None = ...,
        formula2: Any | None = ...,
        showErrorMessage: bool = ...,
        showInputMessage: bool = ...,
        showDropDown: Any | None = ...,
        allowBlank: Any | None = ...,
        sqref=...,
        promptTitle: Any | None = ...,
        errorStyle: Any | None = ...,
        error: Any | None = ...,
        prompt: Any | None = ...,
        errorTitle: Any | None = ...,
        imeMode: Any | None = ...,
        operator: Any | None = ...,
        allow_blank: Any | None = ...,
    ) -> None: ...
    def add(self, cell) -> None: ...
    def __contains__(self, cell): ...

class DataValidationList(Serialisable):
    tagname: str
    disablePrompts: Any
    xWindow: Any
    yWindow: Any
    dataValidation: Any
    __elements__: Any
    __attrs__: Any
    def __init__(
        self,
        disablePrompts: Any | None = ...,
        xWindow: Any | None = ...,
        yWindow: Any | None = ...,
        count: Any | None = ...,
        dataValidation=...,
    ) -> None: ...
    @property
    def count(self): ...
    def __len__(self): ...
    def append(self, dv) -> None: ...
    def to_tree(self, tagname: Any | None = ...): ...
