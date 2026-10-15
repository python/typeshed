from typing import Any
from ldap.controls import LDAPControl

DEREF_CONTROL_OID: str

class DereferenceControl(LDAPControl):
    controlType: Any
    derefSpecs: Any
    def __init__(self, criticality: bool = False, derefSpecs: Any = ...) -> None: ...
    def encodeControlValue(self): ...
    derefRes: Any
    def decodeControlValue(self, encodedControlValue) -> None: ...
