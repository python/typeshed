from _typeshed import Incomplete
from collections.abc import Mapping

from pyasn1.type.base import Asn1Type

__all__ = ["OpenType"]

class OpenType:
    def __init__(self, name, typeMap: Mapping[Incomplete, Asn1Type] | None = None) -> None: ...
    @property
    def name(self): ...
    def values(self): ...
    def keys(self): ...
    def items(self): ...
    def __contains__(self, key) -> bool: ...
    def __getitem__(self, key): ...
    def __iter__(self): ...
