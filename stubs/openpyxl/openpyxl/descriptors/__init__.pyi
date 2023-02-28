from typing_extensions import Self

from .base import *
from .sequence import Sequence as Sequence

class MetaStrict(type):
    def __new__(cls, clsname: str, bases: tuple[type, ...], methods: dict[str, Descriptor]) -> Self: ...

class MetaSerialisable(type):
    def __new__(cls, clsname: str, bases: tuple[type, ...], methods: dict[str, Descriptor]) -> Self: ...

class Strict(metaclass=MetaStrict): ...

class _Serialiasable(metaclass=MetaSerialisable):
    __attrs__: tuple[str, ...]
    __namespaced__: tuple[tuple[str, str], ...]
    __nested__: tuple[str, ...]
    __elements__: tuple[str, ...]
