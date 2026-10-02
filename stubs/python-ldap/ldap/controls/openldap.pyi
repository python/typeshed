from typing import Any

from ldap.controls import ResponseControl, ValueLessRequestControl
from pyasn1.type import univ

__all__ = ["SearchNoOpControl", "SearchNoOpMixIn"]

class SearchNoOpControl(ValueLessRequestControl, ResponseControl):
    controlType: str
    criticality: Any  # TODO: Precise type
    def __init__(self, criticality: bool = False) -> None: ...

    class SearchNoOpControlValue(univ.Sequence): ...
    resultCode: Any  # TODO: Precise type
    numSearchResults: Any  # TODO: Precise type
    numSearchContinuations: Any  # TODO: Precise type
    def decodeControlValue(self, encodedControlValue) -> None: ...

class SearchNoOpMixIn:
    def noop_search_st(self, base, scope=..., filterstr: str = "(objectClass=*)", timeout: int = -1): ...
