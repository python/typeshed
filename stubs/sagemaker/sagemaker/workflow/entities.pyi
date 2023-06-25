import abc
from _typeshed import Incomplete
from enum import EnumMeta
from typing import Any, Dict, List

PrimitiveType = str | int | bool | float | None
RequestType = dict[str | Any, list[dict[str, Any]]]

class Entity(abc.ABC, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def to_request(self) -> RequestType: ...

class DefaultEnumMeta(EnumMeta):
    default: Incomplete
    def __call__(cls, *args, value=..., **kwargs): ...
    factory = __call__

class Expression(abc.ABC, metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def expr(self) -> RequestType: ...

class PipelineVariable(Expression, metaclass=abc.ABCMeta):
    def __add__(self, other: Expression | PrimitiveType): ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def to_string(self): ...
    @property
    @abc.abstractmethod
    def expr(self) -> RequestType: ...
