from typing import Any

from ldap.controls import ResponseControl

__all__ = ["PasswordExpiringControl", "PasswordExpiredControl"]

class PasswordExpiringControl(ResponseControl):
    controlType: str
    gracePeriod: Any  # TODO: Precise type
    def decodeControlValue(self, encodedControlValue) -> None: ...

class PasswordExpiredControl(ResponseControl):
    controlType: str
    passwordExpired: Any  # TODO: Precise type
    def decodeControlValue(self, encodedControlValue) -> None: ...
