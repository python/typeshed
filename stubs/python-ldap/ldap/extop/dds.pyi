from typing import Any

from ldap.extop import ExtendedRequest as ExtendedRequest, ExtendedResponse as ExtendedResponse
from pyasn1.type import univ

class RefreshRequest(ExtendedRequest):
    requestName: str
    defaultRequestTtl: int

    class RefreshRequestValue(univ.Sequence):
        componentType: Any  # TODO: Precise type

    entryName: Any  # TODO: Precise type
    requestTtl: Any  # TODO: Precise type
    def __init__(self, requestName: Any | None = None, entryName: Any | None = None, requestTtl: Any | None = None) -> None: ...
    def encodedRequestValue(self): ...

class RefreshResponse(ExtendedResponse):
    responseName: str

    class RefreshResponseValue(univ.Sequence):
        componentType: Any  # TODO: Precise type

    responseTtl: Any  # TODO: Precise type
    def decodeResponseValue(self, value): ...
