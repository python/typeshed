# Stubs for sqlalchemy.dialects.postgresql.dml (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from ...sql.elements import ClauseElement
from ...sql.dml import Insert as StandardInsert

class Insert(StandardInsert):
    def excluded(self): ...
    def on_conflict_do_update(self, constraint: Optional[Any] = ..., index_elements: Optional[Any] = ..., index_where: Optional[Any] = ..., set_: Optional[Any] = ..., where: Optional[Any] = ...): ...
    def on_conflict_do_nothing(self, constraint: Optional[Any] = ..., index_elements: Optional[Any] = ..., index_where: Optional[Any] = ...): ...

insert = ...  # type: Any

class OnConflictClause(ClauseElement):
    constraint_target = ...  # type: Any
    inferred_target_elements = ...  # type: Any
    inferred_target_whereclause = ...  # type: Any
    def __init__(self, constraint: Optional[Any] = ..., index_elements: Optional[Any] = ..., index_where: Optional[Any] = ...) -> None: ...

class OnConflictDoNothing(OnConflictClause):
    __visit_name__ = ...  # type: str

class OnConflictDoUpdate(OnConflictClause):
    __visit_name__ = ...  # type: str
    update_values_to_set = ...  # type: Any
    update_whereclause = ...  # type: Any
    def __init__(self, constraint: Optional[Any] = ..., index_elements: Optional[Any] = ..., index_where: Optional[Any] = ..., set_: Optional[Any] = ..., where: Optional[Any] = ...) -> None: ...
