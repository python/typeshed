from typing import Any

from . import treebuilders as treebuilders
from .constants import (
    E as E,
    adjustMathMLAttributes as adjustMathMLAttributes,
    adjustSVGAttributes as adjustSVGAttributes,
    asciiUpper2Lower as asciiUpper2Lower,
    cdataElements as cdataElements,
    headingElements as headingElements,
    htmlIntegrationPointElements as htmlIntegrationPointElements,
    mathmlTextIntegrationPointElements as mathmlTextIntegrationPointElements,
    namespaces as namespaces,
    rcdataElements as rcdataElements,
    spaceCharacters as spaceCharacters,
    specialElements as specialElements,
    tagTokenTypes as tagTokenTypes,
    tokenTypes as tokenTypes,
)
from .treebuilders.base import Marker as Marker

def parse(doc, treebuilder: str = ..., namespaceHTMLElements: bool = ..., **kwargs): ...
def parseFragment(doc, container: str = ..., treebuilder: str = ..., namespaceHTMLElements: bool = ..., **kwargs): ...
def method_decorator_metaclass(function): ...

class HTMLParser:
    strict: Any
    tree: Any
    errors: Any
    phases: Any
    def __init__(
        self, tree: Any | None = ..., strict: bool = ..., namespaceHTMLElements: bool = ..., debug: bool = ...
    ) -> None: ...
    firstStartTag: bool
    log: Any
    compatMode: str
    innerHTML: Any
    phase: Any
    lastPhase: Any
    beforeRCDataPhase: Any
    framesetOK: bool
    def reset(self) -> None: ...
    @property
    def documentEncoding(self): ...
    def isHTMLIntegrationPoint(self, element): ...
    def isMathMLTextIntegrationPoint(self, element): ...
    def mainLoop(self) -> None: ...
    def parse(self, stream, *args, **kwargs): ...
    def parseFragment(self, stream, *args, **kwargs): ...
    def parseError(self, errorcode: str = ..., datavars: Any | None = ...) -> None: ...
    def adjustMathMLAttributes(self, token) -> None: ...
    def adjustSVGAttributes(self, token) -> None: ...
    def adjustForeignAttributes(self, token) -> None: ...
    def reparseTokenNormal(self, token) -> None: ...
    def resetInsertionMode(self) -> None: ...
    originalPhase: Any
    def parseRCDataRawtext(self, token, contentType) -> None: ...

def getPhases(debug): ...
def adjust_attributes(token, replacements) -> None: ...
def impliedTagToken(name, type: str = ..., attributes: Any | None = ..., selfClosing: bool = ...): ...

class ParseError(Exception): ...
