from _typeshed import Incomplete

from ldap.controls import ResponseControl, ValueLessRequestControl
from pyasn1.type import univ

__all__ = ["PasswordPolicyControl"]

class PasswordPolicyWarning(univ.Choice):
    componentType: Incomplete

class PasswordPolicyError(univ.Enumerated):
    namedValues: Incomplete
    subtypeSpec: Incomplete

class PasswordPolicyResponseValue(univ.Sequence):
    componentType: Incomplete

class PasswordPolicyControl(ValueLessRequestControl, ResponseControl):
    controlType: str
    criticality: Incomplete
    timeBeforeExpiration: int | None
    graceAuthNsRemaining: int | None
    error: int | None
    def __init__(self, criticality: bool = False) -> None: ...
    def decodeControlValue(self, encodedControlValue: bytes) -> None: ...
