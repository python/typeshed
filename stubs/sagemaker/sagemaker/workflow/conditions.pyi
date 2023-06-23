import abc
from _typeshed import Incomplete
from enum import Enum
from typing import Dict, List, Union

from sagemaker.workflow.entities import (
    DefaultEnumMeta,
    Entity,
    Expression,
    PrimitiveType as PrimitiveType,
    RequestType as RequestType,
)
from sagemaker.workflow.execution_variables import ExecutionVariable
from sagemaker.workflow.parameters import Parameter
from sagemaker.workflow.properties import Properties

ConditionValueType = ExecutionVariable | Parameter | Properties

class ConditionTypeEnum(Enum, metaclass=DefaultEnumMeta):
    EQ: str
    GT: str
    GTE: str
    IN: str
    LT: str
    LTE: str
    NOT: str
    OR: str

class Condition(Entity, metaclass=abc.ABCMeta):
    condition_type: ConditionTypeEnum
    def __init__(self, condition_type) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class ConditionComparison(Condition):
    left: ConditionValueType | PrimitiveType
    right: ConditionValueType | PrimitiveType
    def to_request(self) -> RequestType: ...
    def __init__(self, condition_type, left, right) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

class ConditionEquals(ConditionComparison):
    def __init__(
        self, left: ConditionValueType | PrimitiveType, right: ConditionValueType | PrimitiveType
    ) -> None: ...

class ConditionGreaterThan(ConditionComparison):
    def __init__(
        self, left: ConditionValueType | PrimitiveType, right: ConditionValueType | PrimitiveType
    ) -> None: ...

class ConditionGreaterThanOrEqualTo(ConditionComparison):
    def __init__(
        self, left: ConditionValueType | PrimitiveType, right: ConditionValueType | PrimitiveType
    ) -> None: ...

class ConditionLessThan(ConditionComparison):
    def __init__(
        self, left: ConditionValueType | PrimitiveType, right: ConditionValueType | PrimitiveType
    ) -> None: ...

class ConditionLessThanOrEqualTo(ConditionComparison):
    def __init__(
        self, left: ConditionValueType | PrimitiveType, right: ConditionValueType | PrimitiveType
    ) -> None: ...

class ConditionIn(Condition):
    value: Incomplete
    in_values: Incomplete
    def __init__(
        self, value: ConditionValueType | PrimitiveType, in_values: List[ConditionValueType | PrimitiveType]
    ) -> None: ...
    def to_request(self) -> RequestType: ...

class ConditionNot(Condition):
    expression: Incomplete
    def __init__(self, expression: Condition) -> None: ...
    def to_request(self) -> RequestType: ...

class ConditionOr(Condition):
    conditions: Incomplete
    def __init__(self, conditions: List[Condition] = None) -> None: ...
    def to_request(self) -> RequestType: ...

def primitive_or_expr(
    value: ExecutionVariable | Expression | PrimitiveType | Parameter | Properties
) -> Dict[str | str, PrimitiveType]: ...
