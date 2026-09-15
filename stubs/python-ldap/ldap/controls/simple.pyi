from _typeshed import Incomplete

from ldap.controls import (
    KNOWN_RESPONSE_CONTROLS as KNOWN_RESPONSE_CONTROLS,
    LDAPControl as LDAPControl,
    RequestControl as RequestControl,
    ResponseControl as ResponseControl,
)

class ValueLessRequestControl(RequestControl):
    controlType: Incomplete
    criticality: Incomplete
    def __init__(self, controlType: str | None = None, criticality: bool = False) -> None: ...
    def encodeControlValue(self) -> None: ...

class OctetStringInteger(LDAPControl):
    controlType: Incomplete
    criticality: Incomplete
    integerValue: Incomplete
    def __init__(self, controlType: str | None = None, criticality: bool = False, integerValue: int | None = None) -> None: ...
    def encodeControlValue(self) -> bytes: ...
    def decodeControlValue(self, encodedControlValue: bytes) -> None: ...

class BooleanControl(LDAPControl):
    controlType: Incomplete
    criticality: Incomplete
    booleanValue: Incomplete
    def __init__(self, controlType: str | None = None, criticality: bool = False, booleanValue: bool = False) -> None: ...
    def encodeControlValue(self) -> bytes: ...
    def decodeControlValue(self, encodedControlValue: bytes) -> None: ...

class ManageDSAITControl(ValueLessRequestControl):
    def __init__(self, criticality: bool = False) -> None: ...

class RelaxRulesControl(ValueLessRequestControl):
    def __init__(self, criticality: bool = False) -> None: ...

class ProxyAuthzControl(RequestControl):
    def __init__(self, criticality: bool, authzId: bytes) -> None: ...

class AuthorizationIdentityRequestControl(ValueLessRequestControl):
    controlType: str
    def __init__(self, criticality: bool) -> None: ...

class AuthorizationIdentityResponseControl(ResponseControl):
    controlType: str
    authzId: Incomplete
    def decodeControlValue(self, encodedControlValue: bytes) -> None: ...

class GetEffectiveRightsControl(RequestControl):
    controlType: str
    def __init__(self, criticality: bool, authzId: bytes | None = None) -> None: ...
