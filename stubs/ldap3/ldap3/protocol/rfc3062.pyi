from typing import Any

from pyasn1.type.univ import OctetString, Sequence

class UserIdentity(OctetString):
    tagSet: Any
    encoding: str

class OldPasswd(OctetString):
    tagSet: Any
    encoding: str

class NewPasswd(OctetString):
    tagSet: Any
    encoding: str

class GenPasswd(OctetString):
    tagSet: Any
    encoding: str

class PasswdModifyRequestValue(Sequence):
    componentType: Any

class PasswdModifyResponseValue(Sequence):
    componentType: Any
