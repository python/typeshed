from typing import Any

from ldap.extop import ExtendedResponse as ExtendedResponse
from pyasn1.type import univ

class PasswordModifyResponse(ExtendedResponse):
    responseName: Any  # TODO: Precise type

    class PasswordModifyResponseValue(univ.Sequence):
        componentType: Any  # TODO: Precise type

    genPasswd: Any  # TODO: Precise type
    def decodeResponseValue(self, value): ...
