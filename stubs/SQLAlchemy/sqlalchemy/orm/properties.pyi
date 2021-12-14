from typing import Any

from .. import util
from .interfaces import PropComparator, StrategizedProperty

class ColumnProperty(StrategizedProperty):
    strategy_wildcard_key: str
    inherit_cache: bool
    columns: Any
    group: Any
    deferred: Any
    raiseload: Any
    instrument: Any
    comparator_factory: Any
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
    def copy(self): ...
    def merge(
        self, session, source_state, source_dict, dest_state, dest_dict, load, _recursive, _resolve_conflict_map
    ) -> None: ...
    class Comparator(util.MemoizedSlots, PropComparator):
        def _memoized_method___clause_element__(self): ...
        def operate(self, op, *other, **kwargs): ...
        def reverse_operate(self, op, other, **kwargs): ...
