from abc import ABC

from pyasn1.type import univ
from pyasn1.type.tag import TagSet

class AbstractCharacterString(univ.OctetString, ABC):
    def __bytes__(self) -> bytes: ...
    def prettyIn(self, value): ...
    def asOctets(self, padding: bool = ...): ...
    def asNumbers(self, padding: bool = ...): ...
    def prettyOut(self, value): ...
    def prettyPrint(self, scope: int = ...): ...
    def __reversed__(self): ...

class NumericString(AbstractCharacterString):
    __doc__: str
    tagSet: TagSet
    encoding: str
    typeId: int

class PrintableString(AbstractCharacterString):
    __doc__: str
    tagSet: TagSet
    encoding: str
    typeId: int

class TeletexString(AbstractCharacterString):
    __doc__: str
    tagSet: TagSet
    encoding: str
    typeId: int

class T61String(TeletexString):
    __doc__: str
    typeId: int

class VideotexString(AbstractCharacterString):
    __doc__: str
    tagSet: TagSet
    encoding: str
    typeId: int

class IA5String(AbstractCharacterString):
    __doc__: str
    tagSet: TagSet
    encoding: str
    typeId: int

class GraphicString(AbstractCharacterString):
    __doc__: str
    tagSet: TagSet
    encoding: str
    typeId: int

class VisibleString(AbstractCharacterString):
    __doc__: str
    tagSet: TagSet
    encoding: str
    typeId: int

class ISO646String(VisibleString):
    __doc__: str
    typeId: int

class GeneralString(AbstractCharacterString):
    __doc__: str
    tagSet: TagSet
    encoding: str
    typeId: int

class UniversalString(AbstractCharacterString):
    __doc__: str
    tagSet: TagSet
    encoding: str
    typeId: int

class BMPString(AbstractCharacterString):
    __doc__: str
    tagSet: TagSet
    encoding: str
    typeId: int

class UTF8String(AbstractCharacterString):
    __doc__: str
    tagSet: TagSet
    encoding: str
    typeId: int
