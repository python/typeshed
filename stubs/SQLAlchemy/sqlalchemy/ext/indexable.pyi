from _typeshed import Incomplete
from typing import Any

from ..ext.hybrid import hybrid_property

class index_property(hybrid_property):
    attr_name: str
    index: Any
    default: Any
    datatype: Any
    onebased: bool
    def __init__(
        self, attr_name: str, index, default=..., datatype: Incomplete | None = ..., mutable: bool = ..., onebased: bool = ...
    ): ...
    def fget(self, instance): ...
    def fset(self, instance, value) -> None: ...
    def fdel(self, instance) -> None: ...
    def expr(self, model): ...
