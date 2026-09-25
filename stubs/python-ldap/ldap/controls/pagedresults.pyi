from _typeshed import Incomplete

from ldap.controls import RequestControl, ResponseControl
from pyasn1.type import univ

__all__ = ["SimplePagedResultsControl"]

class PagedResultsControlValue(univ.Sequence):
    componentType: Incomplete

class SimplePagedResultsControl(RequestControl, ResponseControl):
    controlType: str
    criticality: Incomplete
    size: Incomplete
    cookie: bytes
    def __init__(self, criticality: bool = False, size: int = 10, cookie: str | bytes | None = "") -> None: ...
    def encodeControlValue(self) -> bytes: ...
    def decodeControlValue(self, encodedControlValue: bytes) -> None: ...
