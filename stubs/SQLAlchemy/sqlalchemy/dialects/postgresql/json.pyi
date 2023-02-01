from _typeshed import Incomplete
from typing import Any

import sqlalchemy.types as sqltypes

class JSONPathType(sqltypes.JSON.JSONPathType):
    def bind_processor(self, dialect): ...
    def literal_processor(self, dialect): ...

class JSON(sqltypes.JSON):
    astext_type: Any
    def __init__(self, none_as_null: bool = ..., astext_type: Incomplete | None = ...) -> None: ...

    class Comparator(sqltypes.JSON.Comparator):
        @property
        def astext(self): ...
    comparator_factory: Any

class JSONB(JSON):
    __visit_name__: str

    class Comparator(JSON.Comparator):
        def has_key(self, other): ...
        def has_all(self, other): ...
        def has_any(self, other): ...
        def contains(self, other, **kwargs): ...
        def contained_by(self, other): ...
    comparator_factory: Any
