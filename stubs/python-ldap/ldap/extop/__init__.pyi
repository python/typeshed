from _typeshed import Incomplete
from typing import Any

from ldap.extop.dds import RefreshRequest as RefreshRequest, RefreshResponse as RefreshResponse
from ldap.extop.passwd import PasswordModifyResponse as PasswordModifyResponse

__all__ = ["ExtendedRequest", "ExtendedResponse", "RefreshRequest", "RefreshResponse", "PasswordModifyResponse"]

class ExtendedRequest:
    requestName: Incomplete
    requestValue: Incomplete
    def __init__(self, requestName: str, requestValue: bytes | None) -> None: ...
    def encodedRequestValue(self) -> bytes | None: ...

class ExtendedResponse:
    responseName: str | None
    responseValue: Incomplete
    def __init__(self, responseName: str | None, encodedResponseValue: bytes | None) -> None: ...
    def decodeResponseValue(self, value: bytes | None) -> Any: ...
