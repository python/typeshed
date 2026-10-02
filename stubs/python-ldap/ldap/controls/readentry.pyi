from typing import Any

from ldap.controls import KNOWN_RESPONSE_CONTROLS as KNOWN_RESPONSE_CONTROLS, LDAPControl as LDAPControl

class ReadEntryControl(LDAPControl):
    def __init__(self, criticality: bool = False, attrList: Any | None = None) -> None: ...  # TODO: Precise type for attrList
    def encodeControlValue(self): ...
    dn: Any  # TODO: Precise type
    entry: Any  # TODO: Precise type
    def decodeControlValue(self, encodedControlValue) -> None: ...

class PreReadControl(ReadEntryControl):
    controlType: Any  # TODO: Precise type

class PostReadControl(ReadEntryControl):
    controlType: Any  # TODO: Precise type
