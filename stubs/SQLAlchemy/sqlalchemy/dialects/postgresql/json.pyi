from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any, TypeVar

from ...sql import sqltypes
from ...sql.elements import BinaryExpression

_T = TypeVar("_T")

class JSONPathType(sqltypes.JSON.JSONPathType):
    def bind_processor(self, dialect): ...
    def literal_processor(self, dialect): ...

class JSON(sqltypes.JSON):
    astext_type: Any
    def __init__(self, none_as_null: bool = False, astext_type: Incomplete | None = None) -> None: ...

    class Comparator(sqltypes.JSON.Comparator[_T]):
        @property
        def astext(self): ...
    comparator_factory: Callable[[Incomplete], Comparator[Incomplete]]

class JSONB(JSON):
    __visit_name__: str

    class Comparator(JSON.Comparator[_T]):
        def has_key(self, other) -> BinaryExpression: ...
        def has_all(self, other) -> BinaryExpression: ...
        def has_any(self, other) -> BinaryExpression: ...
        def contains(self, other: str, **kwargs) -> BinaryExpression: ...
        def contained_by(self, other) -> BinaryExpression: ...
    comparator_factory: Callable[[Incomplete], Comparator[Incomplete]]
