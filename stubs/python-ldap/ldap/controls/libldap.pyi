from typing import Any
from ldap.controls import (
    KNOWN_RESPONSE_CONTROLS as KNOWN_RESPONSE_CONTROLS,
    LDAPControl as LDAPControl,
    RequestControl as RequestControl,
    ResponseControl as ResponseControl,
)
from ldap.pkginfo import __version__ as __version__

class AssertionControl(RequestControl):
    controlType: Any
    assertion: Any
    def __init__(self, assertion: Any, criticality: bool = False) -> None: ...
    def encodeControlValue(self): ...

class MatchedValuesControl(ResponseControl):
    controlType: Any
    matchedValues: Any
    def __init__(self, matchedValues: Any, criticality: bool = False) -> None: ...
    def decodeControlValue(self, encodedControlValue) -> None: ...

class SimplePagedResultsControl(RequestControl):
    controlType: Any
    size: int
    cookie: Any
    def __init__(self, size: int = 0, cookie: Any = ...) -> None: ...
    def encodeControlValue(self): ...
    def decodeControlValue(self, encodedControlValue) -> None: ...
