from typing import Any
from ldap.controls.simple import BooleanControl, ManageDSAITControl, RelaxRulesControl, ValueLessRequestControl
from ldap.controls.libldap import AssertionControl, MatchedValuesControl, SimplePagedResultsControl

__all__ = [
    "KNOWN_RESPONSE_CONTROLS",
    "AssertionControl",
    "BooleanControl",
    "LDAPControl",
    "ManageDSAITControl",
    "MatchedValuesControl",
    "RelaxRulesControl",
    "RequestControl",
    "ResponseControl",
    "SimplePagedResultsControl",
    "ValueLessRequestControl",
    "RequestControlTuples",
    "DecodeControlTuples",
]

KNOWN_RESPONSE_CONTROLS: Any

class RequestControl:
    controlType: Any
    criticality: Any
    encodedControlValue: Any
    def __init__(self, controlType: Any = ..., criticality: bool = False, encodedControlValue: Any = ...) -> None: ...
    def encodeControlValue(self) -> Any: ...

class ResponseControl:
    controlType: Any
    criticality: Any
    encodedControlValue: Any
    def __init__(self, controlType: Any = ..., criticality: bool = False) -> None: ...
    def decodeControlValue(self, encodedControlValue: Any) -> Any: ...

class LDAPControl(RequestControl, ResponseControl):
    controlType: Any
    criticality: Any
    controlValue: Any
    encodedControlValue: Any
    def __init__(
        self, controlType: Any = ..., criticality: bool = False, controlValue: Any = ..., encodedControlValue: Any = ...
    ) -> None: ...

def RequestControlTuples(ldapControls: Any) -> Any: ...
def DecodeControlTuples(ldapControlTuples: Any, knownLDAPControls: Any = ...) -> Any: ...
