# Stubs for sqlalchemy.dialects.postgresql.array (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .base import ischema_names as ischema_names
from ...sql import expression as expression, operators as operators
from ...sql.base import SchemaEventTarget as SchemaEventTarget
from ... import types as sqltypes
from uuid import UUID as _python_UUID

def Any(other, arrexpr, operator: Any = ...): ...
def All(other, arrexpr, operator: Any = ...): ...

class array(expression.Tuple):
    __visit_name__ = ...  # type: str
    type = ...  # type: Any
    def __init__(self, clauses, **kw) -> None: ...
    def self_group(self, against: Optional[Any] = ...): ...

CONTAINS = ...  # type: Any
CONTAINED_BY = ...  # type: Any
OVERLAP = ...  # type: Any

class ARRAY(SchemaEventTarget, sqltypes.ARRAY):
    class Comparator(sqltypes.ARRAY.Comparator):
        def contains(self, other, **kwargs): ...
        def contained_by(self, other): ...
        def overlap(self, other): ...
    comparator_factory = ...  # type: Any
    item_type = ...  # type: Any
    as_tuple = ...  # type: Any
    dimensions = ...  # type: Any
    zero_indexes = ...  # type: Any
    def __init__(self, item_type, as_tuple: bool = ..., dimensions: Optional[Any] = ..., zero_indexes: bool = ...) -> None: ...
    @property
    def hashable(self): ...
    @property
    def python_type(self): ...
    def compare_values(self, x, y): ...
    def bind_processor(self, dialect): ...
    def result_processor(self, dialect, coltype): ...
