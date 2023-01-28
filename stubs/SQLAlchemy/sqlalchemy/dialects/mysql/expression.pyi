from _typeshed import Self
from typing import Any

from ...sql import elements
from ...sql.base import Generative

class match(Generative, elements.BinaryExpression):
    __visit_name__: str
    inherit_cache: bool
    def __init__(self, *cols, **kw) -> None: ...
    modifiers: Any
    def in_boolean_mode(self: Self) -> Self: ...
    def in_natural_language_mode(self: Self) -> Self: ...
    def with_query_expansion(self: Self) -> Self: ...
