from _typeshed import Incomplete

from ldap.extop import ExtendedResponse as ExtendedResponse
from pyasn1.type import univ

class PasswordModifyResponse(ExtendedResponse):
    responseName: Incomplete

    class PasswordModifyResponseValue(univ.Sequence):
        componentType: Incomplete

    genPasswd: Incomplete
    def decodeResponseValue(self, value: bytes | None) -> bytes: ...
