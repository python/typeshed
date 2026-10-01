from _typeshed import Incomplete

from ldap.controls import (
    KNOWN_RESPONSE_CONTROLS as KNOWN_RESPONSE_CONTROLS,
    LDAPControl as LDAPControl,
    RequestControl as RequestControl,
)
from ldap.pkginfo import __version__ as __version__

class AssertionControl(RequestControl):
    controlType: Incomplete
    criticality: Incomplete
    filterstr: Incomplete
    def __init__(self, criticality: bool = True, filterstr: str = "(objectClass=*)") -> None: ...
    def encodeControlValue(self) -> bytes: ...

class MatchedValuesControl(RequestControl):
    controlType: Incomplete
    criticality: Incomplete
    filterstr: Incomplete
    def __init__(self, criticality: bool = False, filterstr: str = "(objectClass=*)") -> None: ...
    def encodeControlValue(self) -> bytes: ...

class SimplePagedResultsControl(LDAPControl):
    controlType: Incomplete
    criticality: Incomplete
    def __init__(self, criticality: bool = False, size: int | None = None, cookie: str | bytes | None = None) -> None: ...
    def encodeControlValue(self) -> bytes: ...
    def decodeControlValue(self, encodedControlValue: bytes) -> None: ...
