from typing import Any
from ldap.controls import LDAPControl, ResponseControl

__all__ = ["PasswordExpiringControl", "PasswordExpiredControl"]

class PasswordPolicyControl(LDAPControl):
    controlType: Any
    def __init__(self, criticality: bool = False) -> None: ...
    def encodeControlValue(self): ...
    def decodeControlValue(self, encodedControlValue) -> None: ...

class PasswordExpiringControl(ResponseControl):
    controlType: str
    gracePeriod: Any  # TODO: Precise type
    def decodeControlValue(self, encodedControlValue) -> None: ...

class PasswordExpiredControl(ResponseControl):
    controlType: str
    passwordExpired: Any  # TODO: Precise type
    def decodeControlValue(self, encodedControlValue) -> None: ...
