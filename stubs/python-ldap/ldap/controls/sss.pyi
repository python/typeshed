from typing import Any

from ldap.controls import RequestControl, ResponseControl
from pyasn1.type import univ

__all__ = ["SSSRequestControl", "SSSResponseControl"]

class SortKeyType(univ.Sequence):
    componentType: Any  # TODO: Precise type

class SortKeyListType(univ.SequenceOf):
    componentType: Any  # TODO: Precise type

class SSSRequestControl(RequestControl):
    controlType: str
    ordering_rules: Any  # TODO: Precise type
    def __init__(self, criticality: bool = False, ordering_rules: Any | None = None) -> None: ...
    def asn1(self): ...
    def encodeControlValue(self): ...

class SortResultType(univ.Sequence):
    componentType: Any  # TODO: Precise type

class SSSResponseControl(ResponseControl):
    controlType: str
    def __init__(self, criticality: bool = False) -> None: ...
    sortResult: Any  # TODO: Precise type
    attributeType: Any  # TODO: Precise type
    result: Any  # TODO: Precise type
    attribute_type_error: Any  # TODO: Precise type
    def decodeControlValue(self, encoded) -> None: ...
