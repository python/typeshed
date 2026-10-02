from typing import Any
from ldap.controls import LDAPControl

class PersistentSearchControl(LDAPControl):
    controlType: Any
    def __init__(
        self, criticality: bool = False, changeTypes: Any = ..., changesOnly: bool = False, returnECs: bool = False
    ) -> None: ...
    def encodeControlValue(self): ...
    def decodeControlValue(self, encodedControlValue) -> None: ...
