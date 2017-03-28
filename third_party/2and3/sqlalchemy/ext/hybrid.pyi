# Stubs for sqlalchemy.ext.hybrid (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from ..orm import attributes as attributes, interfaces as interfaces

HYBRID_METHOD = ...  # type: Any
HYBRID_PROPERTY = ...  # type: Any

class hybrid_method(interfaces.InspectionAttrInfo):
    is_attribute = ...  # type: bool
    extension_type = ...  # type: Any
    func = ...  # type: Any
    def __init__(self, func, expr: Optional[Any] = ...) -> None: ...
    def __get__(self, instance, owner): ...
    expr = ...  # type: Any
    def expression(self, expr): ...

class hybrid_property(interfaces.InspectionAttrInfo):
    is_attribute = ...  # type: bool
    extension_type = ...  # type: Any
    fget = ...  # type: Any
    fset = ...  # type: Any
    fdel = ...  # type: Any
    def __init__(self, fget, fset: Optional[Any] = ..., fdel: Optional[Any] = ..., expr: Optional[Any] = ...) -> None: ...
    def __get__(self, instance, owner): ...
    def __set__(self, instance, value): ...
    def __delete__(self, instance): ...
    def setter(self, fset): ...
    def deleter(self, fdel): ...
    expr = ...  # type: Any
    def expression(self, expr): ...
    def comparator(self, comparator): ...

class Comparator(interfaces.PropComparator):
    property = ...  # type: Any
    expression = ...  # type: Any
    def __init__(self, expression) -> None: ...
    def __clause_element__(self): ...
    def adapt_to_entity(self, adapt_to_entity): ...

class ExprComparator(Comparator):
    expression = ...  # type: Any
    hybrid = ...  # type: Any
    def __init__(self, expression, hybrid) -> None: ...
    def __getattr__(self, key): ...
    @property
    def info(self): ...
    @property
    def property(self): ...
    def operate(self, op, *other, **kwargs): ...
    def reverse_operate(self, op, other, **kwargs): ...
