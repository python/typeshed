from typing import Any

from ldap import __version__ as __version__
from ldap.extop.passwd import PasswordModifyResponse as PasswordModifyResponse

class ExtendedRequest:
    requestName: Any  # TODO: Precise type
    requestValue: Any  # TODO: Precise type
    def __init__(self, requestName, requestValue) -> None: ...
    def encodedRequestValue(self): ...

class ExtendedResponse:
    responseName: Any  # TODO: Precise type
    responseValue: Any  # TODO: Precise type
    def __init__(self, responseName, encodedResponseValue) -> None: ...
    def decodeResponseValue(self, value): ...
