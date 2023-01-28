from _typeshed import Incomplete
from collections.abc import Callable
from typing import Any, TypeVar
from typing_extensions import ParamSpec

from .. import util
from .descriptor_props import (
    CompositeProperty as CompositeProperty,
    ConcreteInheritedProperty as ConcreteInheritedProperty,
    SynonymProperty as SynonymProperty,
)
from .interfaces import PropComparator, StrategizedProperty
from .relationships import RelationshipProperty as RelationshipProperty

_T = TypeVar("_T")
_P = ParamSpec("_P")

__all__ = ["ColumnProperty", "CompositeProperty", "ConcreteInheritedProperty", "RelationshipProperty", "SynonymProperty"]

class ColumnProperty(StrategizedProperty):
    class Comparator(util.MemoizedSlots, PropComparator[_T]):
        expressions: Any
        def _memoized_method___clause_element__(self): ...
        def operate(self, op: Callable[_P, _T], *other: _P.args, **kwargs: _P.kwargs) -> _T: ...  # type: ignore[override]  # _T doesn't match
        def reverse_operate(self, op: Callable[..., _T], other, **kwargs) -> _T: ...  # type: ignore[override]  # _T doesn't match
    logger: Any
    strategy_wildcard_key: str
    inherit_cache: bool
    columns: Any
    group: Any
    deferred: Any
    raiseload: Any
    instrument: Any
    comparator_factory: Callable[[Incomplete], Comparator[Incomplete]]
    descriptor: Any
    active_history: Any
    expire_on_flush: Any
    info: Any
    doc: Any
    strategy_key: Any
    def __init__(self, *columns, **kwargs) -> None: ...
    def __clause_element__(self): ...
    @property
    def expression(self): ...
    def instrument_class(self, mapper) -> None: ...
    def do_init(self) -> None: ...
    def copy(self) -> ColumnProperty: ...
    def merge(
        self, session, source_state, source_dict, dest_state, dest_dict, load, _recursive, _resolve_conflict_map
    ) -> None: ...
