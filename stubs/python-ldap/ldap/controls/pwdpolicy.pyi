from _typeshed import Incomplete

from ldap.controls import ResponseControl

__all__ = ["PasswordExpiredControl", "PasswordExpiringControl"]

class PasswordExpiringControl(ResponseControl):
    controlType: str
    gracePeriod: Incomplete
    def decodeControlValue(self, encodedControlValue: bytes) -> None: ...

class PasswordExpiredControl(ResponseControl):
    controlType: str
    passwordExpired: Incomplete
    def decodeControlValue(self, encodedControlValue: bytes) -> None: ...
