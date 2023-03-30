from _typeshed import Incomplete
from typing_extensions import Literal, TypeAlias

from openpyxl.descriptors.base import NoneSet
from openpyxl.descriptors.serialisable import Serialisable

_DataValidationType: TypeAlias = Literal["whole", "decimal", "list", "date", "time", "textLength", "custom"]
_DataValidationErrorStyle: TypeAlias = Literal["stop", "warning", "information"]
_DataValidationImeMode: TypeAlias = Literal[
    "noControl",
    "off",
    "on",
    "disabled",
    "hiragana",
    "fullKatakana",
    "halfKatakana",
    "fullAlpha",
    "halfAlpha",
    "fullHangul",
    "halfHangul",
]
_DataValidationOperator: TypeAlias = Literal[
    "between", "notBetween", "equal", "notEqual", "lessThan", "lessThanOrEqual", "greaterThan", "greaterThanOrEqual"
]

def collapse_cell_addresses(cells, input_ranges=()): ...
def expand_cell_ranges(range_string): ...

class DataValidation(Serialisable):
    tagname: str
    sqref: Incomplete
    cells: Incomplete
    ranges: Incomplete
    showErrorMessage: Incomplete
    showDropDown: Incomplete
    hide_drop_down: Incomplete
    showInputMessage: Incomplete
    allowBlank: Incomplete
    allow_blank: Incomplete
    errorTitle: Incomplete
    error: Incomplete
    promptTitle: Incomplete
    prompt: Incomplete
    formula1: Incomplete
    formula2: Incomplete
    type: NoneSet[_DataValidationType]
    errorStyle: NoneSet[_DataValidationErrorStyle]
    imeMode: NoneSet[_DataValidationImeMode]
    operator: NoneSet[_DataValidationOperator]
    validation_type: Incomplete
    def __init__(
        self,
        type: _DataValidationType | Literal["none"] | None = None,
        formula1: Incomplete | None = None,
        formula2: Incomplete | None = None,
        showErrorMessage: bool = False,
        showInputMessage: bool = False,
        showDropDown: Incomplete | None = False,
        allowBlank: Incomplete | None = False,
        sqref=(),
        promptTitle: Incomplete | None = None,
        errorStyle: _DataValidationErrorStyle | Literal["none"] | None = None,
        error: Incomplete | None = None,
        prompt: Incomplete | None = None,
        errorTitle: Incomplete | None = None,
        imeMode: _DataValidationImeMode | Literal["none"] | None = None,
        operator: _DataValidationOperator | Literal["none"] | None = None,
        allow_blank: Incomplete | None = False,
    ) -> None: ...
    def add(self, cell) -> None: ...
    def __contains__(self, cell): ...

class DataValidationList(Serialisable):
    tagname: str
    disablePrompts: Incomplete
    xWindow: Incomplete
    yWindow: Incomplete
    dataValidation: Incomplete
    __elements__: Incomplete
    __attrs__: Incomplete
    def __init__(
        self,
        disablePrompts: Incomplete | None = None,
        xWindow: Incomplete | None = None,
        yWindow: Incomplete | None = None,
        count: Incomplete | None = None,
        dataValidation=(),
    ) -> None: ...
    @property
    def count(self): ...
    def __len__(self) -> int: ...
    def append(self, dv) -> None: ...
    def to_tree(self, tagname: Incomplete | None = None): ...  # type: ignore[override]
