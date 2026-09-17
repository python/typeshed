from _typeshed import Incomplete

from ldap.controls import RequestControl, ResponseControl
from pyasn1.type import univ

__all__ = ["SSSRequestControl", "SSSResponseControl"]

class SortKeyType(univ.Sequence):
    componentType: Incomplete

class SortKeyListType(univ.SequenceOf):
    componentType: Incomplete

class SSSRequestControl(RequestControl):
    controlType: str
    ordering_rules: Incomplete
    def __init__(self, criticality: bool = False, ordering_rules: list[str] | str = []) -> None: ...
    def asn1(self) -> SortKeyListType: ...
    def encodeControlValue(self) -> bytes: ...

class SortResultType(univ.Sequence):
    componentType: Incomplete

class SSSResponseControl(ResponseControl):
    controlType: str
    def __init__(self, criticality: bool = False) -> None: ...
    sortResult: Incomplete
    attributeType: Incomplete
    result: Incomplete
    attribute_type_error: Incomplete
    def decodeControlValue(self, encodedControlValue: bytes) -> None: ...
