from _typeshed import Incomplete

from ldap.controls import RequestControl, ResponseControl
from pyasn1.type import univ

__all__ = ["VLVRequestControl", "VLVResponseControl"]

class ByOffsetType(univ.Sequence):
    tagSet: Incomplete
    componentType: Incomplete

class TargetType(univ.Choice):
    componentType: Incomplete

class VirtualListViewRequestType(univ.Sequence):
    componentType: Incomplete

class VLVRequestControl(RequestControl):
    controlType: str
    before_count: Incomplete
    after_count: Incomplete
    offset: Incomplete
    content_count: Incomplete
    greater_than_or_equal: Incomplete
    context_id: Incomplete
    def __init__(
        self,
        criticality: bool = False,
        before_count: int = 0,
        after_count: int = 0,
        offset: int | None = None,
        content_count: int | None = None,
        greater_than_or_equal: str | None = None,
        context_id: str | None = None,
    ) -> None: ...
    def encodeControlValue(self) -> bytes: ...

class VirtualListViewResultType(univ.Enumerated):
    namedValues: Incomplete

class VirtualListViewResponseType(univ.Sequence):
    componentType: Incomplete

class VLVResponseControl(ResponseControl):
    controlType: str
    def __init__(self, criticality: bool = False) -> None: ...
    targetPosition: Incomplete
    contentCount: Incomplete
    virtualListViewResult: Incomplete
    contextID: str | None
    target_position: Incomplete
    content_count: Incomplete
    result: Incomplete
    context_id: Incomplete
    def decodeControlValue(self, encodedControlValue: bytes) -> None: ...
