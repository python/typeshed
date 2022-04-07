from typing import Any

from . import elements
from .operators import ColumnOperators

REQUIRED: Any

class _multiparam_column(elements.ColumnElement[Any]):
    index: Any
    key: Any
    original: Any
    default: Any
    type: Any
    def __init__(self, original, index) -> None: ...
    def compare(self, other, **kw) -> None: ...
    def __eq__(self, other) -> ColumnOperators: ...
