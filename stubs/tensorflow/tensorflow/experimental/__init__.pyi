from _typeshed import Incomplete
from abc import ABC
from typing import Generic, TypeVar

_T1 = TypeVar("_T1", covariant=True)

class Optional(Generic[_T1], ABC):
    def __getattr__(self, name: str) -> Incomplete: ...

def __getattr__(name: str) -> Incomplete: ...
