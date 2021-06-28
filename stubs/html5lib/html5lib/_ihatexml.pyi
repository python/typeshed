from typing import Any

from .constants import DataLossWarning as DataLossWarning

baseChar: str
ideographic: str
combiningCharacter: str
digit: str
extender: str
letter: Any
name: Any
nameFirst: Any
reChar: Any
reCharRange: Any

def charStringToList(chars): ...
def normaliseCharList(charList): ...

max_unicode: Any

def missingRanges(charList): ...
def listToRegexpStr(charList): ...
def hexToInt(hex_str): ...
def escapeRegexp(string): ...

nonXmlNameBMPRegexp: Any
nonXmlNameFirstBMPRegexp: Any
nonPubidCharRegexp: Any

class InfosetFilter:
    replacementRegexp: Any
    dropXmlnsLocalName: Any
    dropXmlnsAttrNs: Any
    preventDoubleDashComments: Any
    preventDashAtCommentEnd: Any
    replaceFormFeedCharacters: Any
    preventSingleQuotePubid: Any
    replaceCache: Any
    def __init__(
        self,
        dropXmlnsLocalName: bool = ...,
        dropXmlnsAttrNs: bool = ...,
        preventDoubleDashComments: bool = ...,
        preventDashAtCommentEnd: bool = ...,
        replaceFormFeedCharacters: bool = ...,
        preventSingleQuotePubid: bool = ...,
    ) -> None: ...
    def coerceAttribute(self, name, namespace: Any | None = ...): ...
    def coerceElement(self, name): ...
    def coerceComment(self, data): ...
    def coerceCharacters(self, data): ...
    def coercePubid(self, data): ...
    def toXmlName(self, name): ...
    def getReplacementCharacter(self, char): ...
    def fromXmlName(self, name): ...
    def escapeChar(self, char): ...
    def unescapeChar(self, charcode): ...
