from _typeshed import Incomplete

from ldap.controls import LDAPControl
from pyasn1.type import univ
from pyasn1_modules.rfc2251 import AttributeDescriptionList

__all__ = ["DEREF_CONTROL_OID", "DereferenceControl"]

DEREF_CONTROL_OID: str
AttributeList = AttributeDescriptionList

class DerefSpec(univ.Sequence):
    componentType: Incomplete

class DerefSpecs(univ.SequenceOf):
    componentType: Incomplete

class AttributeValues(univ.SetOf):
    componentType: Incomplete

class PartialAttribute(univ.Sequence):
    componentType: Incomplete

class PartialAttributeList(univ.SequenceOf):
    componentType: Incomplete
    tagSet: Incomplete

class DerefRes(univ.Sequence):
    componentType: Incomplete

class DerefResultControlValue(univ.SequenceOf):
    componentType: Incomplete

class DereferenceControl(LDAPControl):
    controlType = DEREF_CONTROL_OID
    derefSpecs: Incomplete
    def __init__(self, criticality: bool = False, derefSpecs: dict[str, list[str]] | None = None) -> None: ...
    def encodeControlValue(self) -> bytes: ...
    derefRes: dict[str, list[tuple[str, dict[str, list[str]]]]]
    def decodeControlValue(self, encodedControlValue: bytes) -> None: ...
