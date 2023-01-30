from _typeshed import Incomplete, Self
from collections.abc import Mapping
from typing import Any
from typing_extensions import TypeAlias

from ...engine import Connection, Engine
from ...sql import expression, functions
from ...sql.coercions import _CoercibleElement
from ...sql.expression import ColumnElement
from ...sql.schema import ColumnCollectionConstraint
from ...sql.type_api import TypeEngine
from ...sql.visitors import Traversible
from ...util.langhelpers import memoized_property

_Unused: TypeAlias = object

class aggregate_order_by(expression.ColumnElement[Any]):
    __visit_name__: str
    stringify_dialect: str
    target: Any
    @memoized_property
    def type(self) -> Incomplete: ...
    order_by: Any
    def __init__(self, target: _CoercibleElement, *order_by: _CoercibleElement) -> None: ...
    def self_group(self: Self, against: _Unused = ...) -> Self: ...  # type: ignore[override]  # supertype has overloads
    def get_children(self, **kwargs: _Unused) -> tuple[ColumnElement[Incomplete], Incomplete]: ...  # type: ignore[override]  # Different params

class ExcludeConstraint(ColumnCollectionConstraint):
    __visit_name__: str
    where: Traversible | None
    inherit_cache: bool
    create_drop_stringify_dialect: str
    operators: Any
    using: str
    ops: Mapping[Incomplete, Incomplete]
    def __init__(
        self,
        *elements,
        name: str | None = None,
        deferrable: bool | None = None,
        initially: str | None = None,
        using: str = "gist",
        where: str | bool | Traversible | None = None,
        ops: Mapping[Incomplete, Incomplete] = ...,
    ) -> None: ...

def array_agg(
    self, *args: ColumnElement[Incomplete], bind: Engine | Connection | None = None, type_: TypeEngine | type[TypeEngine] = ...
) -> functions.array_agg: ...
