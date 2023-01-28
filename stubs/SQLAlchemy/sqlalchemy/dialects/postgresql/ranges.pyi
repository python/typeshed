from _typeshed import Incomplete

from ...sql import sqltypes
from ...sql.elements import BinaryExpression

class RangeOperators:
    class comparator_factory(sqltypes.Concatenable.Comparator[Incomplete]):
        def __ne__(self, other) -> BinaryExpression: ...  # type: ignore[override]
        def contains(self, other, **kw) -> BinaryExpression: ...
        def contained_by(self, other) -> BinaryExpression: ...
        def overlaps(self, other) -> BinaryExpression: ...
        def strictly_left_of(self, other) -> BinaryExpression: ...
        __lshift__ = strictly_left_of
        def strictly_right_of(self, other) -> BinaryExpression: ...
        __rshift__ = strictly_right_of
        def not_extend_right_of(self, other) -> BinaryExpression: ...
        def not_extend_left_of(self, other) -> BinaryExpression: ...
        def adjacent_to(self, other) -> BinaryExpression: ...
        def __add__(self, other) -> BinaryExpression: ...

class INT4RANGE(RangeOperators, sqltypes.TypeEngine):
    __visit_name__: str

class INT8RANGE(RangeOperators, sqltypes.TypeEngine):
    __visit_name__: str

class NUMRANGE(RangeOperators, sqltypes.TypeEngine):
    __visit_name__: str

class DATERANGE(RangeOperators, sqltypes.TypeEngine):
    __visit_name__: str

class TSRANGE(RangeOperators, sqltypes.TypeEngine):
    __visit_name__: str

class TSTZRANGE(RangeOperators, sqltypes.TypeEngine):
    __visit_name__: str
