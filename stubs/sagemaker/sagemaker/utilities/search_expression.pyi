from _typeshed import Incomplete
from enum import Enum

from sagemaker.apiutils._base_types import ApiObject

class Operator(Enum):
    EQUALS: str
    NOT_EQUALS: str
    GREATER_THAN: str
    GREATER_THAN_OR_EQUAL: str
    LESS_THAN: str
    LESS_THAN_OR_EQUAL: str
    CONTAINS: str
    EXISTS: str
    NOT_EXISTS: str

class BooleanOperator(Enum):
    AND: str
    OR: str

class SearchObject(ApiObject):
    def to_boto(self): ...

class Filter(SearchObject):
    name: Incomplete
    operator: Incomplete
    value: Incomplete
    def __init__(self, name, operator: Incomplete | None = None, value: Incomplete | None = None, **kwargs) -> None: ...

class NestedFilter(SearchObject):
    nested_property_name: Incomplete
    filters: Incomplete
    def __init__(self, property_name, filters, **kwargs) -> None: ...

class SearchExpression(SearchObject):
    filters: Incomplete
    nested_filters: Incomplete
    operator: Incomplete
    sub_expressions: Incomplete
    def __init__(
        self,
        filters: Incomplete | None = None,
        nested_filters: Incomplete | None = None,
        sub_expressions: Incomplete | None = None,
        boolean_operator=...,
        **kwargs,
    ) -> None: ...
