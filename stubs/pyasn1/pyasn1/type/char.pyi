from _typeshed import Incomplete

from pyasn1.type import univ

class AbstractCharacterString(univ.OctetString):
    def __bytes__(self) -> bytes: ...
    def prettyIn(self, value): ...
    def asOctets(self, padding: bool = ...): ...
    def asNumbers(self, padding: bool = ...): ...
    def prettyOut(self, value): ...
    def prettyPrint(self, scope: int = ...): ...
    def __reversed__(self): ...

class NumericString(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete

class PrintableString(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete

class TeletexString(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete

class T61String(TeletexString):
    __doc__: Incomplete
    typeId: Incomplete

class VideotexString(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete

class IA5String(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete

class GraphicString(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete

class VisibleString(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete

class ISO646String(VisibleString):
    __doc__: Incomplete
    typeId: Incomplete

class GeneralString(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete

class UniversalString(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete

class BMPString(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete

class UTF8String(AbstractCharacterString):
    __doc__: Incomplete
    tagSet: Incomplete
    encoding: str
    typeId: Incomplete
