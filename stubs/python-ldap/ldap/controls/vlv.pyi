from typing import Any

from ldap.controls import RequestControl, ResponseControl
from pyasn1.type import univ

__all__ = ["VLVRequestControl", "VLVResponseControl"]

class ByOffsetType(univ.Sequence):
    tagSet: Any  # TODO: Precise type
    componentType: Any  # TODO: Precise type

class TargetType(univ.Choice):
    componentType: Any  # TODO: Precise type

class VirtualListViewRequestType(univ.Sequence):
    componentType: Any  # TODO: Precise type

class VLVRequestControl(RequestControl):
    controlType: str
    before_count: Any  # TODO: Precise type
    after_count: Any  # TODO: Precise type
    offset: Any  # TODO: Precise type
    content_count: Any  # TODO: Precise type
    greater_than_or_equal: Any  # TODO: Precise type
    context_id: Any  # TODO: Precise type
    def __init__(
        self,
        criticality: bool = False,
        before_count: int = 0,
        after_count: int = 0,
        offset: Any | None = None,
        content_count: Any | None = None,
        greater_than_or_equal: Any | None = None,
        context_id: Any | None = None,
    ) -> None: ...
    def encodeControlValue(self): ...

class VirtualListViewResultType(univ.Enumerated):
    namedValues: Any  # TODO: Precise type

class VirtualListViewResponseType(univ.Sequence):
    componentType: Any  # TODO: Precise type

class VLVResponseControl(ResponseControl):
    controlType: str
    def __init__(self, criticality: bool = False) -> None: ...
    targetPosition: Any  # TODO: Precise type
    contentCount: Any  # TODO: Precise type
    virtualListViewResult: Any  # TODO: Precise type
    contextID: Any  # TODO: Precise type
    target_position: Any  # TODO: Precise type
    content_count: Any  # TODO: Precise type
    result: Any  # TODO: Precise type
    context_id: Any  # TODO: Precise type
    def decodeControlValue(self, encoded) -> None: ...
