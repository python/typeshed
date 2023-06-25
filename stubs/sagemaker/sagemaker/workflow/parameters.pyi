from _typeshed import Incomplete
from enum import Enum
from typing import Dict, List, Type

from sagemaker.workflow.entities import (
    DefaultEnumMeta,
    Entity,
    PipelineVariable,
    PrimitiveType as PrimitiveType,
    RequestType as RequestType,
)

class ParameterTypeEnum(Enum, metaclass=DefaultEnumMeta):
    STRING: str
    INTEGER: str
    BOOLEAN: str
    FLOAT: str
    @property
    def python_type(self) -> type: ...

class Parameter(PipelineVariable, Entity):
    name: str
    parameter_type: ParameterTypeEnum
    default_value: PrimitiveType
    def to_request(self) -> RequestType: ...
    @property
    def expr(self) -> dict[str, str]: ...
    def __init__(self, name, parameter_type, default_value) -> None: ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

ParameterBoolean: Incomplete

class ParameterString(Parameter):
    enum_values: Incomplete
    def __init__(self, name: str, default_value: str | None = None, enum_values: list[str] | None = None) -> None: ...
    def __hash__(self): ...
    def to_string(self) -> PipelineVariable: ...
    def to_request(self) -> RequestType: ...

class ParameterInteger(Parameter):
    def __init__(self, name: str, default_value: int | None = None) -> None: ...

class ParameterFloat(Parameter):
    def __init__(self, name: str, default_value: float | None = None) -> None: ...
