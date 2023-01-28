from _typeshed import Incomplete
from typing import Any, Generic, NoReturn, TypeVar
from typing_extensions import TypeAlias

from ..util.langhelpers import memoized_property
from . import elements

_T = TypeVar("_T")
_Unused: TypeAlias = object

REQUIRED: Any

class _multiparam_column(elements.ColumnElement[_T], Generic[_T]):
    index: Any
    key: Any
    original: Any
    default: Any
    @memoized_property
    def type(self) -> Incomplete: ...
    def __init__(self, original, index) -> None: ...
    def compare(self, other: _Unused, **kw: _Unused) -> NoReturn: ...
    def __eq__(self, other) -> bool: ...  # type: ignore[override]  # isinstance check
