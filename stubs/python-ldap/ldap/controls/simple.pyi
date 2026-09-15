from typing import Any

from ldap.controls import (
    KNOWN_RESPONSE_CONTROLS as KNOWN_RESPONSE_CONTROLS,
    LDAPControl as LDAPControl,
    RequestControl as RequestControl,
    ResponseControl as ResponseControl,
)

class ValueLessRequestControl(RequestControl):
    controlType: Any
    criticality: Any
    def __init__(self, controlType: Any | None = None, criticality: bool = False) -> None: ...
    def encodeControlValue(self) -> None: ...

class OctetStringInteger(LDAPControl):
    controlType: Any
    criticality: Any
    integerValue: Any
    def __init__(self, controlType: Any | None = None, criticality: bool = False, integerValue: Any | None = None) -> None: ...
    def encodeControlValue(self): ...
    def decodeControlValue(self, encodedControlValue) -> None: ...

class BooleanControl(LDAPControl):
    controlType: Any
    criticality: Any
    booleanValue: Any
    def __init__(self, controlType: Any | None = None, criticality: bool = False, booleanValue: bool = False) -> None: ...
    def encodeControlValue(self): ...
    def decodeControlValue(self, encodedControlValue) -> None: ...

class ManageDSAITControl(ValueLessRequestControl):
    def __init__(self, criticality: bool = False) -> None: ...

class RelaxRulesControl(ValueLessRequestControl):
    def __init__(self, criticality: bool = False) -> None: ...

class ProxyAuthzControl(RequestControl):
    def __init__(self, criticality, authzId) -> None: ...

class AuthorizationIdentityRequestControl(ValueLessRequestControl):
    controlType: str
    def __init__(self, criticality) -> None: ...

class AuthorizationIdentityResponseControl(ResponseControl):
    controlType: str
    authzId: Any
    def decodeControlValue(self, encodedControlValue) -> None: ...

class GetEffectiveRightsControl(RequestControl):
    def __init__(self, criticality, authzId: Any | None = None) -> None: ...

class SimpleControl:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    # TODO: Add more precise attributes and methods

def create_simple_control(*args: Any, **kwargs: Any) -> Any: ...  # TODO: precise types
