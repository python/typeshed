from _typeshed import Incomplete

from ldap.controls import ResponseControl, ValueLessRequestControl
from ldap.ldapobject import SimpleLDAPObject as _Base
from pyasn1.type import univ

__all__ = ["SearchNoOpControl", "SearchNoOpMixIn"]

class SearchNoOpControl(ValueLessRequestControl, ResponseControl):
    controlType: str
    criticality: Incomplete
    def __init__(self, criticality: bool = False) -> None: ...

    class SearchNoOpControlValue(univ.Sequence): ...
    resultCode: Incomplete
    numSearchResults: Incomplete
    numSearchContinuations: Incomplete
    def decodeControlValue(self, encodedControlValue: bytes) -> None: ...

class SearchNoOpMixIn(_Base):
    def __init__(self, *args, **kwargs) -> None: ...
    def noop_search_st(
        self, base: str, scope: int = ..., filterstr: str = "(objectClass=*)", timeout: int = -1
    ) -> tuple[int, int] | tuple[None, None]: ...
